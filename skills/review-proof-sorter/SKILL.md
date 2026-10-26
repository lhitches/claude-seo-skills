---
name: review-proof-sorter
description: >
  Turns a business's Google reviews into proof for its service pages. Takes the reviews
  (pasted, or exported as CSV/JSON/text) and the list of service pages, sorts every review
  by the service and the suburb or city it talks about, and writes a proof block for each
  page: the best quotes word for word, the words customers use for that job, the places they
  name, and which pages have too few reviews to prove anything yet. Use whenever a user asks
  to "use my reviews on my website", "sort my Google reviews", "put reviews on my service
  pages", "which reviews go on which page", "turn reviews into proof", "review proof sorter", or
  invokes /review-proof-sorter. Also use when a page audit says a service page has no social proof.
  Produces sorted-reviews.csv and proof-blocks.md. Works with the reviews a business already
  has; for getting more reviews, use the separate Review Engine skill.
---

# Review Proof Sorter: Google reviews into proof on every service page

Most businesses have their best proof sitting on a Google Business Profile, and a service page
with none. A review about fixing someone's hot water belongs on the hot water page, because
that's the job the visitor on that page needs done. This skill sorts the reviews and hands back
a block of proof for each page, ready to paste.

Keep it practical. The deliverable is one proof block per page the owner can add this week.

## Bundled resources
- `scripts/review_proof_sorter.py`: sorts reviews by service and place with a keyword first pass,
  picks whole-sentence quotes, lists the words customers repeat, writes the outputs. Stdlib only,
  no network.
- `assets/services-template.csv` and `assets/places-template.csv`: the two input layouts.

## Step 1: Get the inputs (don't guess)
If `./business-context.md` exists, read it first and confirm rather than re-ask.

1. **The reviews.** Any of these works:
   - Pasted straight into the chat. Save them to `reviews.txt`, one review per block with a
     blank line between (keep the reviewer name, date and stars on the first line if they
     pasted them).
   - An export or a reviews-widget download as CSV or JSON. The script reads columns called
     text/review/comment, name/author, date, rating/stars and place/location.
   - If the business has several Google profiles (several branches), keep which profile each
     review came from in a `place` column.
   Never make up, edit or "tidy" a review. If the user can't get their reviews out, stop and
   tell them how: open the Business Profile, copy the reviews, paste them here.
2. **The service pages.** The URL and name of each service page. Offer to read the site's menu
   or sitemap to list them, then confirm the list with the user.
3. **The places** (optional). Suburbs, towns or cities they serve, and the location page for each
   if they have one.

## Step 2: Write the keyword lists (you do this, the user checks)
For each service, write the words a customer would use in a review, not the business's own
jargon. A plumber's "hot water system replacement" page gets: hot water; hot water system;
water heater; no hot water; heat pump; instantaneous. Save as `services.csv` (layout in
`assets/services-template.csv`, keywords separated by `;`). Add suburb aliases to `places.csv`
(e.g. "St Kilda; St Kilda East").

Avoid keywords that also show up in general praise ("sales" catches "no sales pitch"; "new"
catches everything). Show the user the lists in one short table and ask if anything is missing.

## Step 3: Run the first pass
```
python3 scripts/review_proof_sorter.py --reviews reviews.csv --services services.csv --places places.csv --business "<Business name>" --out "<workspace>/review-proof-sorter"
```
On Windows, `python3` is often just `python`. Use whichever runs Python 3. The script needs no extra packages.
It prints how many reviews landed on each service and place, and how many it couldn't sort.

## Step 4: Read and fix the sort (this is the important part)
The keyword pass is a first pass. Now read `proof-blocks.md` and `sorted-reviews.csv` yourself:
- **Wrong matches:** a keyword hit that isn't about that service (e.g. "we designed a new
  website" on a migrations page). Move or drop it.
- **Unsorted reviews:** read every one in the "Not sorted" list and assign it by meaning. General
  praise with no job in it ("great to deal with, on time") suits the homepage or About page, not a
  service page. Say so rather than forcing it onto a service.
- **Quotes:** each quote must be whole sentences copied exactly, including the reviewer's spelling.
  You may pick a different sentence from the same review if it's more specific (a job, a result, a
  timeframe, a suburb). Never join sentences from different reviews, never cut words out of the
  middle, never fix grammar.
Then rewrite `proof-blocks.md` as the final version: per page, 3 to 5 quotes, most specific first.

## Step 5: Hand over the proof blocks
For each service page give:
1. **Where it goes:** near the top, beside or just under the main call to action, not on a
   separate reviews page. People read proof on the page they land on.
2. **The quotes** with attribution: first name and last initial, "Google review", and the month
   and year. Link the block to the Google Business Profile so anyone can check them.
3. **Words customers use:** the phrases customers repeat for this job. Suggest using them in the
   page's headings and copy where they're true, because that's how buyers describe the job.
4. **Places named:** if reviews name suburbs, add those quotes to the matching location pages too.
5. **Thin pages:** any service with fewer than three reviews. Suggest asking the next few customers
   for that job for a review that names the job and the suburb.

Finish with a three-line summary: pages covered, pages that are thin, and the one page to update
first (the one with the most traffic or enquiries, if the user knows it).

## Rules
- **Never invent, edit or merge reviews.** Word for word or not at all.
- **Only use 4 and 5 star reviews as proof**, but never hide or delete the others anywhere.
- **Health practitioners in Australia:** Ahpra's rules ban testimonials about clinical care in
  advertising (Health Practitioner Regulation National Law, s133). For a registered health
  business, only use reviews about non-clinical things (booking, parking, front desk, wait time)
  and tell the user why.
- **Don't add Review or AggregateRating schema for the business's own reviews** on its own
  pages expecting stars in Google: Google's review snippet guidelines don't show self-serving
  reviews for LocalBusiness or Organization. Plain text on the page is the point.
- **First name and last initial only.** No surnames, photos or profile links to the reviewer.
- **Australian English**, plain words. The user is a business owner.
- **Don't promise results.** Proof on the page helps visitors decide; it isn't a ranking guarantee.
