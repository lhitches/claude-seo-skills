---
name: ai-visibility-dashboard
description: Runs the book's chapter 11 measurement loop in three modes. Builds a 10 to 20 prompt library for your category by interviewing you, runs a scoring round of those prompts in AI assistants (brand named, recommended, your site linked, an external page about you linked) and compares it with your last round, then turns the latest round plus your GA4 and Search Console exports into the four-gauge board slide (Eligible, Chosen, Arriving, Paying off) with AI-referred revenue. Use this when someone says "build my prompt library", "build my AI visibility dashboard", "how often does ChatGPT cite us", "track my AI citations", "what is my citation share", "run this month's AI visibility round", "score these ChatGPT answers", "how much revenue does AI traffic drive", "is the AI Assistant channel in GA4 converting", "build the board slide for AI search", or "report our AI search results to the board". Works for any business and locale, defaults to Australia.
---

# AI Visibility Dashboard

> Chapter 11, E for Evaluation · Be the SOURCE · SOURCE: Evaluation (E)

## What this does
Runs the measurement method from chapter 11, in three modes you pick from:

1. **Build the prompt library.** Interviews you one question at a time about what you sell, who buys, who you compete with and why people hesitate, then writes 10 to 20 prompts in the book's three layers (head, constrained, skeptical) with a scoring key: the page you hope gets cited for each. Saves `prompt-library.md`.
2. **Run a round.** Runs the library through the book's worksheet: fixed wording, country, assistant and settings, each prompt three times in fresh sessions, four yes/no columns per answer. Claude runs the prompts itself if Claude in Chrome is connected; otherwise it hands you a copy-ready prompt pack and scores the answers you paste back. Saves `ai-visibility-round-YYYY-MM-DD.md` and compares it with your previous round.
3. **Build the board slide.** Combines the latest round with exports you upload from GA4 and Search Console (and optionally Bing Webmaster Tools and a rank tracker) into four gauges, one line each, plus three sentences: what moved, the one constraint to fix next quarter, and what it will cost. Adds the Evaluation 2x2 for your key pages when page data is available.

What it cannot do, so you know up front: Claude cannot log into ChatGPT, Gemini, Perplexity, GA4 or Search Console on its own. Without Claude in Chrome, the answers and the numbers come from you. It does not run on a schedule by itself: you run a round when it is due. And every AI traffic figure it reports is a floor, not a total (see Notes).

## When to use it
- You have never measured AI visibility and want a baseline you can repeat.
- "Build my prompt library" or "what questions should I be testing in ChatGPT?"
- It is day one, day eight or month end and a round is due.
- You have AI answers in front of you and want them scored the same way every time.
- "Is AI traffic actually converting?" or "how much revenue do AI referrals drive?"
- Someone above you wants one page on search and AI, every month.

## What to ask the user first
1. **Look before you ask.** Check the project for `business-context.md`, `prompt-library.md`, earlier `ai-visibility-round-*.md` and `ai-visibility-board-*.md` files, and a saved Mirror card (the three prompts from the book's introduction). Never re-ask what they answer.
2. **Which mode?** Suggest one from what exists: no library means mode 1; a library but no round this month means mode 2; a round done this month means mode 3. The user decides.
3. **The basics, if not on file:** brand name and any trading names or common misspellings, website domain(s), the country and cities you sell in, and your business model (ecommerce, SaaS, B2B services, local or other).
4. **For mode 2:** which assistants. Default to one, the one your buyers most likely use. ChatGPT is the usual first pick; the book also says Google AI Overviews reach the most buyers if time is short. Adding Gemini, Perplexity or Claude multiplies the work (see the budget in mode 2). Also ask whether Claude in Chrome is connected and whether this is a day-one baseline, the day-eight repeat, or a monthly round.
5. **For mode 3:** the reporting month, the exports listed in mode 3 step 1, and two cost figures if you want cost per acquisition: monthly SEO cost (retainer, content, tools) and monthly paid search spend with its conversions.

## How to run it

### Mode 1: Build the prompt library
1. **Read first, then interview.** Fetch the homepage, main service or category pages, pricing (if published), About and case studies. Read `business-context.md` and the Mirror card if present. Draft what you think the answers are, marked "from your site, please confirm", so the interview confirms and sharpens rather than starting blank.
2. **Interview one question at a time**, using each answer to decide the next question, as the book's interview prompt does. Cover:
   - what you sell and the category a buyer would put you in
   - your customers and their segments (size, industry, location)
   - your real competitors and alternatives, including doing nothing, doing it in-house, a freelancer, or a do-it-yourself tool
   - your price point
   - the constraints and use cases your best customers have
   - the objections buyers raise
   - where you are genuinely better, and where you are genuinely worse, than the alternatives

   Drill into vague answers: "small businesses" is not an answer until you know roughly how many staff, what they sell and what made them start looking. Stop when you can be specific, usually after six to ten questions. If the owner is not available, keep the site-based drafts, label every one "unconfirmed", and list the questions still open at the top of the library.
3. **Write the library: 10 to 20 prompts**, exactly as a buyer would type them, naming the country and, where it matters, the city or suburb. The three Mirror prompts from the book's introduction go in first as M1 to M3: the exact wording the user ran if they have a Mirror card (so it becomes the first data point in the series), otherwise the book's templates filled in: "Best [what you sell] for [your customer type] in [your city or country]. Provide citations.", "Who should I hire for [the thing you do], and why them? Provide citations." and "What do you know about [your brand]? Provide citations." They count toward the 20 and give mode 2 its minimum round. Then:
   - **Head (H):** "best [category] for [customer] in [place]", "[product type] vs [alternative]", "how much does [thing] cost in [country]".
   - **Constrained (C):** the question behind the question, with the details a real buyer adds: size, budget, platform, deadline, the thing they hate about the status quo. This is where citation share is won or lost, so give it the most prompts.
   - **Skeptical (S):** "is [brand] worth it", "alternatives to [brand]", "[brand] vs [competitor]", "what do customers say about [brand]", and one do-nothing or do-it-yourself prompt.

   Adjust by business model, as the book does. Ecommerce: category-level prompts, and watch which product pages get quoted. SaaS: weight toward alternatives and versus prompts. B2B services: fewer, higher-value prompts. Local: add suburb qualifiers.
4. **Tag each prompt** with its layer, and its group: **Brand** (the prompt names you) or **Category** (it does not). The two groups are always reported separately, because brand prompts name you by design.
5. **Write the scoring key.** For each prompt: the page you hope gets cited (a URL on your site, or an external page about you such as a review profile), and the competitor or third-party page you expect to see instead. Where no page of yours could deserve the citation, write "no page yet": that is a content gap before you run anything.
6. **Curate with the user.** Read the list back and cross out any prompt a real buyer would never type (insider jargon, keyword-style phrasing, questions only you care about). Keep 10 to 20.
7. **Freeze the setup** at the top of the file: library version and date, country, the assistant list, settings (temporary chat or memory off, web search as observed), and the citation line. The citation line is "Provide citations." added to the end of every prompt in a chat assistant (M1 to M3 already end with it, so do not add it twice). Do not add it on Google Search surfaces (AI Overviews, AI Mode): there it changes the search, and those surfaces show links anyway.
8. **Save `prompt-library.md`** and tell the user the rule: never edit a prompt mid-series. A changed prompt gets a new ID and its own baseline. Review the library quarterly (Bing's grounding queries and Search Console queries are good sources of new prompts).

### Mode 2: Run a round (the worksheet)
1. **Load the library and the frozen setup.** If there is no library, run mode 1 first, or run the three Mirror prompts (templates in mode 1, step 3) on their own as a minimum round.
2. **Budget the round and agree it.** Answers per round = prompts × 3 runs × assistants. Fifteen prompts on four assistants is 180 answers, so start smaller: the full library on one assistant (30 to 60 answers), or the three Mirror prompts on one assistant (9 answers), which is the book's minimum.
3. **Rules for every run:** a fresh session for every single answer (a new temporary chat, never the next message in the same chat), memory and chat history off where the assistant allows it (ChatGPT: a Temporary Chat), exact library wording plus the citation line. Record the date, the assistant, the model if shown, and whether it visibly searched the web (a "searched" note or a sources list). Save the full answer and every cited URL.
4. **Route A, Claude in Chrome connected.** Tell the user how many answers the round will take and get a go-ahead, because it runs in their own logged-in accounts. The user signs in themselves; Claude never types a password, and if a login wall, CAPTCHA or usage limit appears, Claude stops and hands back. For each answer: open a new temporary chat, type the prompt, wait for the answer to finish, read the answer and its sources, and append them to `ai-visibility-answers-YYYY-MM-DD.md`. For Google AI Overviews or AI Mode, run the prompt as a Google search and record "no AI answer shown" when none appears. The browser is signed in to the user's Google account, so note that the result is personalised.
5. **Route B, no browser tools.** Write `ai-visibility-answers-YYYY-MM-DD.md` as the prompt pack: one block per prompt and assistant, holding the exact text to copy (citation line already on it) and three answer slots, Run 1 to Run 3, each with a line for the model shown and "searched: yes or no". Tell the user: every run gets its own new temporary chat, so one prompt means three separate chats; paste the prompt, copy the full answer into its slot. If the copied text lost its links, open the answer's sources panel and paste those URLs too. They can paste back in batches in chat, or fill in the file and upload it. Allow a minute or two per answer.
6. **Score each answer**, four separate yes/no columns:
   - **Named:** your brand or a trading name (misspellings included) appears in the answer text. A mention only inside a cited URL does not count.
   - **Recommended:** the answer presents you as a choice the buyer should consider: on the shortlist, or as the answer. A neutral mention, a warning or "also exists" is a no. For brand prompts: yes if the verdict is broadly in your favour. Note a short phrase from the answer when the call is borderline.
   - **Your site linked:** at least one cited URL is on your domain. Ignore tracking tags such as utm_source=chatgpt.com when matching.
   - **External page about you linked:** a cited URL on another domain whose page describes you (a review profile, directory listing, news story, or a list article that includes you). Open the link to check. If it will not open, mark it "unchecked" and count unchecked cells separately.

   Also record for each answer: every competitor named, any fact about you that is wrong, and every external URL cited.
7. **Log failed runs separately** (refused, errored, cut off, hit a usage limit, no AI answer shown). Retry once. Report what stays unresolved; failed runs never enter the denominator.
8. **Report counts over completed answers**, never bare percentages: "named in 9 of 42". Split by assistant and by group (Brand vs Category). The headline **citation share** follows the book's definition (the AI names you, quotes you or pulls from your page): category answers that name you or link your site, over completed category answers, per assistant. Show the four columns beside it. Tally each competitor the same way (named or its site linked) so you can see who is chosen instead of you.
9. **Sort each prompt into one of the book's three piles**, by the majority of its runs, because this is what turns the round into a to-do list:
   - **Named favourably, or your page is the source:** recommended, or your site is cited. Guard the pages and signals producing it.
   - **Competitors instead:** other businesses are named or their pages cited, and you are neither recommended nor cited (a passing mention does not count). A gap, usually thin offsite authority or a page that does not go deep enough.
   - **Unclaimed:** no business in your category is named or cited. There for the taking once you build the content that addresses it properly.

   Mark a prompt "mixed" when its runs split with no majority.
10. **Compare with the previous round.** Find the most recent earlier `ai-visibility-round-*.md`. Compare only prompts with identical wording, the same assistant and the same settings; new or changed prompts start their own series. Ask what changed on the site or offsite since then and record it. Day one and day eight are both baselines taken before planned changes: the gap between them shows how much answers vary on their own. Two rounds show variation; they do not set a noise threshold (chapter 11). Report each round's counts over completed answers, note what changed in between, and call something a trend only when it holds across several later rounds on the same prompts, assistants and settings. Write "moved after the change", never "because of it".
11. **Save `ai-visibility-round-YYYY-MM-DD.md`** (the date the round started). Hand wrong facts to the Brand Hallucination Monitor skill, and add the external pages that shape your category answers but leave you out to the chapter 7 (Offsite) target list: the Brand Mention Builder skill works from that list.

### Mode 3: Build the board slide
1. **Collect the inputs.** Ask for exports for the reporting month and the month before, and read nothing from memory:
   - **Latest round file** (and the previous one) for Chosen.
   - **GA4:** Reports, Acquisition, Traffic acquisition. The built-in **AI Assistant** channel holds visits from ChatGPT, Gemini, Copilot and others. Export Sessions, Key events and Total revenue by channel (share icon, Download file, CSV), with the Key events column set to the event that matters if there are several. Optional: Reports, Engagement, Landing page filtered to AI Assistant (for the 2x2), and the same report filtered to Direct (for deep-landing Direct visits). Steps: https://thesourceframework.com/how/ga4
   - **Search Console:** Performance, Search results, with the built-in **Branded** query filter (clicks and impressions), plus the unfiltered totals for the same dates. If there is no Branded option, use Queries containing your brand name, or Custom (regex) for misspellings. The four numbers typed in are fine. Add the Queries export (it has positions) if there is no rank tracker. Steps: https://thesourceframework.com/how/search-console
   - **Optional:** Bing Webmaster Tools AI Performance (citations in Copilot and Bing AI summaries, cited pages, grounding queries); Search Console's Generative AI performance report (impressions only, by page); a rank tracker export (positions and share of voice against named competitors); an AI visibility tracker export; a CRM export of qualified leads or pipeline by source.
   - If Claude in Chrome is connected, Claude can open these reports in the user's browser and read the figures on screen instead. Say which figures were read that way.
2. **Parse carefully.** GA4 CSVs start with comment lines beginning with "#"; skip them. Match periods exactly and name the period and the source on every figure.
3. **Eligible:** rankings and share of voice across your keyword set. With a rank tracker: keywords in the top 10 and share of voice against your top rival. Without one: how many of your target queries sit in the top 10 in the Search Console export, and say that share of voice needs a rank tracker. List positions 4 to 15 separately: the book calls them your best opportunity list.
4. **Chosen:** citation share from the latest round (Category group, per assistant), your site's citation count, and the competitor chosen most often. Add Bing's monthly citation count in brackets if you have it. Never mix a tracker's number with a manual round's number in one figure.
5. **Arriving:** AI Assistant sessions, read beside branded clicks from Search Console and Direct sessions from GA4. Label it a floor, every time.
6. **Paying off:** key events and revenue from Organic Search and AI Assistant, or qualified pipeline from the CRM for lead-gen businesses. If key events carry no value, estimate a value per lead as average deal value × lead-to-close rate and label it an estimate. Organic cost per acquisition = monthly SEO cost ÷ organic key events (or customers); paid = ad spend ÷ paid key events. If a cost is missing, write what is missing rather than guessing. Where the GA4 User acquisition report is available, show first-touch (first user channel) beside the last-click figure, because AI often opens a deal that another channel closes.
7. **Read the gauges together** before naming the weak one:
   - rankings climbing, citation share flat: the pages give AI nothing unique to quote (Uniqueness, chapter 8)
   - citations rising, rankings flat: the content works but authority lags (Offsite, chapter 7)
   - branded search up, rankings drifting down: AI is building demand ahead of your rankings
   - Direct and branded search rising together with no paid brand campaign: a possible sign AI is recommending you, and a reason to check the prompt rounds before claiming it (Direct also collects email, messaging and broken tracking)
   - traffic arriving but not converting: the landing pages or key event set-up, not visibility
8. **Write the three sentences:** what moved since last month (give the counts, for example 4 of 18 to 7 of 18, and say how many rounds the move has held for; one round's move is not yet a trend), the one constraint being fixed next quarter (the weakest gauge and the SOURCE pillar that fixes it), and what it will cost. Take the cost from the user; if you propose one, label it "estimate, to confirm".
9. **The Evaluation 2x2 (when page data exists).** For each key page, citations come from the round's cited URLs plus Bing's cited pages; AI-referred traffic comes from the GA4 Landing page report filtered to AI Assistant. Split high and low at the median of the pages plotted (or the user's own threshold) and say which. Place each page:
   - **Strategic Priority** (high citations, high AI traffic): study it and use it as the template.
   - **Evidence Asset** (high citations, low AI traffic): leave it alone and let it work; it plants your name before buyers are ready to click.
   - **Hidden Opportunity** (low citations, high AI traffic): the demand is proven; earn the citation through Structure and Credibility (tighter extractable answers, a named expert).
   - **Dead Weight** (low on both): run it through the other five pillars; if the question is dead, repurpose the page.

   With single-digit counts, say the placement is provisional.
10. **Save `ai-visibility-board-YYYY-MM.md`.** Keep the same four lines in the same order every month.

## Evidence rules

These apply to every finding this skill reports.

1. **Label every finding** Observed, Inferred or Not checked, and name its source: the page, export, file or answer it came from. Observed means you saw it in data the user gave you or a page you fetched. Inferred means you reasoned to it from something observed; say from what. Not checked means you could not see the evidence; say what would settle it. Never score a Not checked item as a failure. If the output table has no room for the labels and sources, add an "Evidence" section after the actions, one line per finding.
2. **What an AI assistant says comes only from real answers**, run in the user's own browser (Claude in Chrome) or pasted in by the user, each with the assistant, the date and the exact prompt. A web search, a fetched page or your own knowledge is never a record of what ChatGPT, Gemini, Perplexity, Claude, Copilot or Google's AI Overviews and AI Mode told a buyer. Run them signed out or with memory off: a signed-in account carries history and settings (Google lets people mark preferred sources) that can tilt answers toward the brand. Without real answers, hand over the prompts and mark those rows Not checked. Google's AI Overviews appear on some searches only, so "no AI Overview shown" is a result in its own right: record it.
3. **A web fetch is a first look.** It can drop scripts, schema, links and parts of the page, so something it does not show is Not checked, not absent. Many fetch and search tools also pass the page through a summarising model: a fact you saw only in a tool's summary or in a search-result title is Inferred until you see it in the raw HTML (for example with curl). A page that blocks you (a 403) is Not checked; say so. The raw HTML, a Search Console export or the user's own screenshot is the proof.
4. **A web search is a sample, not a ranking.** It usually shows a handful of results, often from another country. Record what it showed, with the date and the query, as Inferred. A position ("ranks in the top 20", "does not rank") needs Search Console or a rank check set to the buyer's location; without one, write that the ranking is Not checked.
5. **Never invent a number.** Where a figure depends on data you do not have (a price, a count, a statistic, a date), write a placeholder such as [your figure] and say where it would come from. Label any estimate as an estimate.
6. **One before-and-after is not proof.** Report counts with their denominators and dates, name anything else that changed in the same period, and write "moved after the change", not "because of it". Two baseline rounds show how much answers vary; they do not set a noise threshold. Call something a trend only when it holds across several rounds on the same prompts, assistants and settings.
7. **Destructive advice needs evidence.** Deleting, merging, redirecting or noindexing a page, or adding, changing or removing a canonical that points at another URL, needs observed evidence in the same row: its traffic, links, conversions or citations. Without it, recommend the check, not the change. Improve a relevant existing page before building a new one.
8. **Unknown is an answer, and the run still finishes.** If the evidence is thin, say so plainly and say what would settle it. When a step needs a browser, a login or an answer you do not have, finish everything else, mark that step Not checked, and list what would fill it, rather than stopping to wait. Questions the skill asks the user after the report is finished, such as the Journey questions, are not evidence and still wait for real answers.

## Output
Every mode ends with a short summary in chat (the headline numbers and the next step) and a saved file.

**Mode 1, `prompt-library.md`:** the frozen setup, any unconfirmed interview answers, then the library:

| ID | Layer | Group | Prompt, exactly as typed | Page you hope gets cited | Expected instead |
|---|---|---|---|---|---|
| C1 | Constrained | Category | We run a 12-person agency in Brisbane that bills hourly. Which project management software should we use? | yoursite.com.au/agencies/ | Competitor's comparison page |

**Mode 2, `ai-visibility-answers-YYYY-MM-DD.md`** (the prompt pack, then the raw answers and links) and **`ai-visibility-round-YYYY-MM-DD.md`**:
- Header: round type (day one, day eight or monthly), library version, series, country, assistants, settings, route (Chrome or paste-back), changes shipped since the last round.
- Results, counts over completed answers:

| Assistant | Group | Completed | Citation share (named or site linked) | Named | Recommended | Your site linked | External page about you linked |
|---|---|---|---|---|---|---|---|
| ChatGPT | Category | 42 of 42 | 11 | 9 | 6 | 4 | 3 |
| ChatGPT | Brand | 15 of 15 | 15 | 15 | 11 | 8 | 10 |

- Competitor tally (category answers naming each competitor or linking its site), the three piles by prompt, the comparison with the previous round, external URLs for the Offsite list, wrong facts, failed runs, and the answer log: ID, assistant, run, model, searched, the four columns, competitors named, cited URLs, note.

**Mode 3, `ai-visibility-board-YYYY-MM.md`:**

> **Search and AI, [Month YYYY]**
> **Eligible:** 14 of 40 target keywords in the top 10 (was 11); share of voice 9% vs [rival] 15%. Rank tracker, [month].
> **Chosen:** named or cited in 11 of 42 ChatGPT category answers (was 7 of 42); our site linked in 4; [rival] chosen in 18. Round of [date].
> **Arriving:** 212 AI Assistant sessions (was 180), beside 1,140 branded clicks and 2,300 Direct sessions. A floor: Copilot lands in Direct, AI Overviews in Organic.
> **Paying off:** 31 organic and AI key events worth $46,500 (estimated value per lead); organic cost per lead $180 vs paid $410. GA4, [month].
>
> What moved: [one sentence]. Next quarter's constraint: [one sentence]. What it will cost: [one sentence].

A gauge with no data says so on its line, with what is needed to fill it. Below the slide: the supporting figures and sources, and the 2x2 table (page, citations, AI sessions, quadrant, fix).

## Notes
- **Every AI traffic number is a floor.** Depending on whose study you read, a third to two thirds of AI-referred visits arrive with no source at all. Copilot sends no referrer and lands in Direct; clicks from untagged links in ChatGPT's apps arrive bare; Google AI Overviews and AI Mode clicks sit inside Organic Search. Deep-landing Direct visits (a blog post or comparison page, not the homepage) are very likely AI answers that lost their referrer. The current platform list lives at https://thesourceframework.com/measure
- **Search Console's Branded filter** only appears on top-level properties with enough impressions and is classified by Google's AI. Its Generative AI performance report shows impressions only, with no queries: read it beside the prompt library, not instead of it.
- **A round measures your chosen questions, not the whole market.** Answers vary run to run, which is why each prompt runs three times and why the day-eight repeat exists. Run it from your own account without temporary chat and the model bends toward you, because it has watched you research your own market.
- **Trackers** (Profound, Peec AI, Otterly, freeSOV; current list at https://thesourceframework.com/measure) run the library at scale from clean accounts. If you use one, upload its export for the Chosen line and note which of the four columns it actually measures.
- **Last-click undersells AI.** A buyer who meets you in an AI answer in January and fills in a form in April gives April all the credit. B2B services: a "how did you hear about us" field on every lead form is the cheapest attribution you will get.
- Evaluation closes the SOURCE formula, (O × U × R × C) ÷ S, measured by E: it tells you whether the work on the other five pillars moved anything and where to point it next. It is a to-do list generator, not a report card.

## The Journey closing step (Hawk Academy students)

If the user is working through the Hawk Academy "Be the SOURCE" Journey (they mention the
Journey or a module, a SOURCE Workbook, or a `business-context.md` in the project says
they are on the Journey), finish every run with two extra steps. If none of those signals are present, skip
this section entirely.

1. Read `business-context.md` first if it exists, and never re-ask anything it already
   answers.
2. Ask these judgment questions, one at a time, in plain language, and wait for real answers.
   Do not answer them yourself and do not skip them:
   - The two number baseline, written and dated before anything else: citation share and AI referred sessions per month.
   - Prompt library curation: of the drafted prompts, which would a real buyer never type? Cross those out together; keep ten to fifteen.
   - The triage in one line: my symptom is X, so my order is A then B then C.
3. Append the answers to the END of this skill's saved output file, under a heading
   `## Your calls`, dated today, in the user's own words. The saved file is the record the
   later modules read; nothing gets copied into a second document. Their pen-and-paper
   workbook holds only the book's own cards (the Mirror, the rent ledger, the head to head,
   and the ninety day grid), so do not tell them to transcribe this output anywhere.
