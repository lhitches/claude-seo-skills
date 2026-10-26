#!/usr/bin/env python3
"""
review_proof_sorter.py - sort a business's Google reviews by service and place, and
draft a proof block for each service page.

Standard library only. No network access: the reviews and the service list are
inputs you give it.

Usage:
  python3 review_proof_sorter.py \
      --reviews reviews.csv \
      --services services.csv \
      [--places places.csv] \
      [--business "Example Plumbing"] \
      [--max-quotes 5] \
      --out ./review-proof-sorter-output

Inputs
  --reviews   .csv, .json or .txt
              csv/json: one review per row/object. Text column is required and can be
              called text, review, comment or content. Optional: name/author,
              date, rating/stars, place/location (e.g. which Google profile it came from).
              txt: reviews separated by a blank line or a line of three dashes.
  --services  .csv with columns: service, url, keywords
              keywords = words or phrases customers would use for that service,
              separated by ";". If blank, the service name is used.
  --places    optional .csv with columns: place, url, aliases
              Suburbs, towns or cities you serve. aliases separated by ";".
              A review counts for a place if it names the place or an alias, or if
              its place/location column matches.

Outputs (in --out)
  sorted-reviews.csv   every review with its matched services and places
  proof-blocks.md      one proof block per service page and per place page,
                       plus the reviews the first pass couldn't sort
  summary.json         counts per service and place, for the report

The keyword pass is a FIRST PASS. The assistant then reads the unsorted reviews and
any doubtful matches and assigns them by meaning (see SKILL.md). Quotes are always
whole sentences copied word for word; the script never rewrites a review.
"""
import argparse, csv, json, os, re, sys, collections, datetime

STOP = set("""a about above after again against all am an and any are as at be because been
before being below between both but by can could did do does doing down during each few for
from further had has have having he her here hers herself him himself his how i if in into is
it its itself just me more most my myself no nor not now of off on once only or other our ours
ourselves out over own same she should so some such than that the their theirs them themselves
then there these they this those through to too under until up very was we were what when where
which while who whom why will with would you your yours yourself yourselves also really highly
would've they've we've i've i'm it's they're we're you're don't didn't can't team work working
worked job great amazing thank thanks recommend recommended best good excellent awesome
fantastic service services company business us one get got always well even much many every
made make time looking across nothing back including seen help helping started
quite ready provided new continue feel pleasure group getting knows know lovely nice happy
professional friendly easy definitely absolutely experience need needed took went came""".split())

NAMES = set()
TEXT_KEYS = ["text", "review", "comment", "content", "body"]
NAME_KEYS = ["name", "author", "reviewer"]
DATE_KEYS = ["date", "time", "published"]
RATING_KEYS = ["rating", "stars", "score"]
PLACE_KEYS = ["place", "location", "profile", "branch"]


def pick(row, keys):
    low = {str(k).strip().lower(): v for k, v in row.items()}
    for k in keys:
        if k in low and str(low[k]).strip():
            return str(low[k]).strip()
    return ""


def load_reviews(path):
    ext = os.path.splitext(path)[1].lower()
    rows = []
    if ext == ".csv":
        with open(path, encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))
    elif ext == ".json":
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        rows = data if isinstance(data, list) else data.get("reviews", [])
    else:
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        chunks = re.split(r"\n\s*(?:---+)?\s*\n", raw)
        rows = [{"text": c.strip()} for c in chunks if c.strip()]
    out = []
    for i, r in enumerate(rows):
        text = pick(r, TEXT_KEYS)
        if not text:
            continue
        rating = pick(r, RATING_KEYS)
        try:
            rating = float(re.findall(r"[\d.]+", rating)[0]) if rating else None
        except (IndexError, ValueError):
            rating = None
        out.append({
            "id": i + 1,
            "name": pick(r, NAME_KEYS),
            "date": pick(r, DATE_KEYS),
            "rating": rating,
            "place_field": pick(r, PLACE_KEYS),
            "text": re.sub(r"\s+", " ", text),
        })
    return out


def load_terms(path, name_col, extra_col):
    items = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            low = {str(k).strip().lower(): (v or "").strip() for k, v in r.items()}
            name = low.get(name_col, "")
            if not name:
                continue
            terms = [t.strip().lower() for t in low.get(extra_col, "").split(";") if t.strip()]
            if not terms:
                terms = [name.lower()]
            if name.lower() not in terms:
                terms.append(name.lower())
            items.append({"name": name, "url": low.get("url", ""), "terms": terms})
    return items


def term_hits(text_low, terms):
    hits = []
    for t in terms:
        if re.search(r"(?<![a-z])" + re.escape(t) + r"(?![a-z])", text_low):
            hits.append(t)
    return hits


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(])", text)
    return [p.strip() for p in parts if p.strip()]


def attribution(name):
    """First name plus last initial, e.g. 'Sarah K.'"""
    bits = [b for b in re.split(r"\s+", name.strip()) if b]
    if not bits:
        return "Google review"
    first = bits[0][:1].upper() + bits[0][1:]
    return first + (" " + bits[-1][:1].upper() + "." if len(bits) > 1 else "")


def specificity(s):
    score = 0
    score += 2 if re.search(r"\d", s) else 0                 # numbers
    score += len(re.findall(r"\b(before|after|since|within|weeks?|months?|days?|hours?)\b", s, re.I))
    score += 1 if 60 <= len(s) <= 260 else 0
    return score


def best_quote(review, hit_terms):
    sents = sentences(review["text"])
    low_terms = [t.lower() for t in hit_terms]
    scored = []
    for idx, s in enumerate(sents):
        sl = s.lower()
        kw = sum(1 for t in low_terms if t in sl)
        scored.append((kw * 3 + specificity(s), -idx, s))
    scored.sort(reverse=True)
    top = scored[0][2] if scored else review["text"]
    # take the next sentence too if the quote is very short
    if len(top) < 60 and len(sents) > 1:
        i = sents.index(top)
        if i + 1 < len(sents):
            top = top + " " + sents[i + 1]
    return top


def rank_review(review, hits):
    r = review["rating"] if review["rating"] is not None else 4.5
    return (r >= 4, len(hits), specificity(review["text"]), len(review["text"]) <= 900, r)


def proper_nouns(reviews):
    """Words that are nearly always capitalised mid-sentence: staff and client names."""
    caps, total = collections.Counter(), collections.Counter()
    for rv in reviews:
        for m in re.finditer(r"[A-Za-z][A-Za-z'-]*", rv["text"]):
            w = m.group(0)
            total[w.lower()] += 1
            if w[0].isupper():
                caps[w.lower()] += 1
    return {w for w, n in total.items() if caps[w] / n >= 0.8 and w not in STOP}


def customer_words(reviews, exclude, names=frozenset()):
    counts = collections.Counter()
    for rv in reviews:
        words = [w for w in re.findall(r"[a-z][a-z'-]+", rv["text"].lower())]
        seen = set()
        for n in (1, 2):
            for i in range(len(words) - n + 1):
                gram = words[i:i + n]
                if any(w in STOP or w in names or len(w) < 3 for w in gram):
                    continue
                g = " ".join(gram)
                if g in exclude or g in seen:
                    continue
                seen.add(g)
                counts[g] += 1
    common = [(g, c) for g, c in counts.most_common(60) if c >= 2]
    # prefer two-word phrases, drop single words already inside a kept phrase
    phrases = [g for g, c in common if " " in g][:8]
    singles = [g for g, c in common if " " not in g and not any(g in p for p in phrases)][:8]
    return phrases + singles


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reviews", required=True)
    ap.add_argument("--services", required=True)
    ap.add_argument("--places")
    ap.add_argument("--business", default="")
    ap.add_argument("--max-quotes", type=int, default=5)
    ap.add_argument("--out", default="./review-proof-sorter-output")
    a = ap.parse_args()

    reviews = load_reviews(a.reviews)
    services = load_terms(a.services, "service", "keywords")
    places = load_terms(a.places, "place", "aliases") if a.places else []
    if not reviews:
        sys.exit("No reviews found in %s (need a text/review/comment column)." % a.reviews)
    if not services:
        sys.exit("No services found in %s (need a service column)." % a.services)
    os.makedirs(a.out, exist_ok=True)

    global NAMES
    NAMES = proper_nouns(reviews)
    for t in re.findall(r"[a-z]+", a.business.lower()):
        NAMES.add(t)
    NAMES |= {"seo", "agency", "google", "review", "reviews"}
    for rv in reviews:
        low = rv["text"].lower()
        rv["services"] = {}
        for s in services:
            h = term_hits(low, s["terms"])
            if h:
                rv["services"][s["name"]] = h
        rv["places"] = {}
        pf = rv["place_field"].lower()
        for p in places:
            h = term_hits(low, p["terms"])
            if not h and pf and any(t in pf for t in p["terms"]):
                h = ["(from the profile it was left on)"]
            if h:
                rv["places"][p["name"]] = h
        rv["primary"] = max(rv["services"], key=lambda k: len(rv["services"][k])) if rv["services"] else ""

    # sorted-reviews.csv
    with open(os.path.join(a.out, "sorted-reviews.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "date", "rating", "primary_service", "all_services",
                    "places", "matched_words", "text"])
        for rv in reviews:
            w.writerow([rv["id"], rv["name"], rv["date"], rv["rating"], rv["primary"],
                        "; ".join(rv["services"]), "; ".join(rv["places"]),
                        "; ".join(sorted({t for h in rv["services"].values() for t in h})),
                        rv["text"]])

    summary = {"business": a.business, "reviews": len(reviews),
               "generated": datetime.date.today().isoformat(), "services": {}, "places": {},
               "unsorted": 0}
    md = ["# Proof blocks%s" % (" for " + a.business if a.business else ""), "",
          "First pass by keyword, %s. Quotes are whole sentences, word for word. "
          "Check every block before it goes on a page." % datetime.date.today().isoformat(), ""]

    def block(title, url, bucket_key, bucket_terms, members):
        members = sorted(members, key=lambda rv: rank_review(rv, rv[bucket_key].get(title, [])), reverse=True)
        rated = [rv["rating"] for rv in members if rv["rating"] is not None]
        avg = round(sum(rated) / len(rated), 1) if rated else None
        md.append("## %s" % title)
        if url:
            md.append("Page: %s" % url)
        md.append("Reviews that mention it: %d%s" % (len(members), (", average %s stars" % avg) if avg else ""))
        md.append("")
        if not members:
            md.append("No reviews name this yet. Ask your next few customers for this job to "
                      "say what you did and where.")
            md.append("")
            return {"count": 0, "avg": None}
        md.append("**Quotes to use (verbatim):**")
        used = 0
        for rv in members:
            if rv["rating"] is not None and rv["rating"] < 4:
                continue
            q = best_quote(rv, rv[bucket_key].get(title, []))
            when = (", " + rv["date"]) if rv["date"] else ""
            md.append('- "%s" - %s, Google review%s' % (q, attribution(rv["name"]), when))
            used += 1
            if used >= a.max_quotes:
                break
        words = customer_words(members, set(bucket_terms), NAMES)
        if words:
            md.append("")
            md.append("**Words these customers use:** " + ", ".join(words))
        if bucket_key == "services" and places:
            named = collections.Counter(p for rv in members for p in rv["places"])
            if named:
                md.append("")
                md.append("**Places named in these reviews:** " +
                          ", ".join("%s (%d)" % (p, c) for p, c in named.most_common()))
        if len(members) < 3:
            md.append("")
            md.append("Thin: fewer than three reviews. Ask recent customers for this job for a "
                      "review that names the job and the suburb.")
        md.append("")
        return {"count": len(members), "avg": avg}

    md.append("# Service pages")
    md.append("")
    for s in services:
        members = [rv for rv in reviews if s["name"] in rv["services"]]
        summary["services"][s["name"]] = block(s["name"], s["url"], "services", s["terms"], members)
    if places:
        md.append("# Place pages")
        md.append("")
        for p in places:
            members = [rv for rv in reviews if p["name"] in rv["places"]]
            summary["places"][p["name"]] = block(p["name"], p["url"], "places", p["terms"], members)

    unsorted = [rv for rv in reviews if not rv["services"]]
    summary["unsorted"] = len(unsorted)
    md.append("# Not sorted by the keyword pass (%d)" % len(unsorted))
    md.append("")
    md.append("Read these and assign them by meaning. Many are general praise that suits the "
              "homepage or About page rather than one service.")
    md.append("")
    for rv in unsorted:
        md.append("- [%s] %s: %s" % (rv["id"], attribution(rv["name"]),
                                    rv["text"][:280] + ("..." if len(rv["text"]) > 280 else "")))
    with open(os.path.join(a.out, "proof-blocks.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    with open(os.path.join(a.out, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=1)

    print("Reviews read: %d" % len(reviews))
    for k, v in summary["services"].items():
        print("  %-40s %3d%s" % (k, v["count"], ("  avg %s" % v["avg"]) if v["avg"] else ""))
    for k, v in summary["places"].items():
        print("  [place] %-32s %3d" % (k, v["count"]))
    print("Unsorted (read by hand): %d" % len(unsorted))
    print("Wrote %s" % os.path.abspath(a.out))


if __name__ == "__main__":
    main()
