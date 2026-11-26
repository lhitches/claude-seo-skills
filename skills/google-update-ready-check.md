---
name: google-update-ready-check
description: >
  Triage for a Google traffic drop. Checks the date the drop started against every update and
  ranking bug on Google's Search Status Dashboard, then against Google's published criteria for core
  updates, helpful content, reviews and spam. Returns one verdict, PANIC, GET TO WORK or LET IT PLAY
  OUT, plus the first thing to do. Use when someone says their traffic or rankings dropped, asks
  whether a Google update hit them, or asks what to do after a core update.
---

# Google Update Ready Check

Your traffic dropped. This skill tells you which of three situations you are in, using only what
Google itself has published: its list of ranking updates, its core update guidance, its people-first
content questions, its reviews criteria and its spam policies. No third-party ranking-factor lists.

The three verdicts:

1. **PANIC.** The drop matches something Google's spam policies target. Act now: the fix is to remove
   the pages or links that match.
2. **GET TO WORK.** The drop is real and the cause is fixable against Google's published criteria.
3. **LET IT PLAY OUT.** An update or a logged ranking bug is still rolling out, or the change is
   normal re-sorting. Changing pages now destroys your ability to tell what worked.

Built by Hawk Academy. Last updated: 30 October 2026. Google's list of updates in this file runs to
10 November 2026.

## Intake (do this FIRST, one question at a time)

Ask these in order. Wait for each answer before asking the next. Never ask all of them at once.

1. **What is the site?** A domain or the section that dropped.
2. **When did the drop start?** A date, or "about two weeks ago" is fine; work out the date.
3. **Can you share Search Console data?** Best: the Performance report with "Compare" set to the
   week before the drop against the week after, exported (Queries and Pages tabs). Acceptable: a
   screenshot of the Date chart over 16 months. If they have nothing, carry on and say which checks
   you could not run.
4. **Did anything change on the site in the month before the drop?** Migration, redesign, new URLs,
   a CMS change, a batch of new pages, sponsored or partner content, a bought domain.

If the user arrives with an answer to a later question already, skip it.

## Process

### Step 1. Rule out what is not an update

Google lists these causes of a traffic drop besides algorithmic updates: technical issues, security
issues, spam issues (including manual actions), seasonality and changing interests, site moves and
migrations, and data anomalies. Check them first, because each one has a different fix.

- **Manual action or security issue.** Ask the user to open Search Console > Security & Manual
  Actions. A manual action for spam is a PANIC verdict on its own.
- **Technical.** Did the Page indexing report or Crawl stats change at the same time? A misplaced
  noindex, a robots.txt change or server errors cause drops that look like an update.
- **Site move.** If URLs changed in the month before, Google says rankings can fluctuate while it
  recrawls, and a medium-sized site may need a few weeks.
- **Seasonality.** Does the same dip appear in the same month last year on a 16-month view? Does
  Google Trends show the topic itself falling?
- **Read the chart shape.** Google's guidance: if impressions held but clicks fell, look at titles,
  snippets and competing search features first.

If one of these explains the drop, say so, give the verdict that fits (usually GET TO WORK, or
PANIC for a manual action or hack), and stop. Do not blame an update for a noindex tag.

### Step 2. Match the drop date to Google's own timeline

Use the table in "Google's logged updates" below. If you can browse, also open
https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history and check for anything logged
after 10 November 2026. An update starts on the entry that says it was released. A preannouncement,
where Google says an update is scheduled, comes before that.

For the drop start date, list every incident whose window covers it, counting the window as the
rollout start to the rollout end plus 7 days. Then say plainly:

- **Which update or updates were running.** Overlaps happen. On 5 March 2024 a core update and a
  spam update began on the same day, and on 5 October 2023 a spam update, a core update and a
  logged ranking bug overlapped. If two were running, say both, and do not pin the drop on the
  louder one.
- **Whether a logged ranking bug overlaps.** Google logged two: "Ranking is experiencing an ongoing
  issue" from 5 October 2023 (26 days) and from 15 August 2024 (4.5 days). A drop inside a bug
  window may have nothing to do with the site.
- **Whether the rollout is finished.** If the newest matching update has no end date, or ended
  fewer than 7 days ago, the verdict is LET IT PLAY OUT. Skip to the output.

How long rollouts run, from every update on Google's Search Status Dashboard:

| Update family | Updates logged | Median rollout | Shortest | Longest |
|---|---|---|---|---|
| Core updates | 17 | 14 days | 6.1 days | 45 days |
| Spam updates (including link spam) | 12 | 7.5 days | 0.8 days | 29 days |
| Reviews updates | 7 | 14 days | 6 days | 29 days |
| Helpful content updates | 3 | 15 days | 13.4 days | 38 days |

If no update or bug matches the date, say so. The drop is either Step 1 territory or one of the
smaller unannounced updates Google says it runs continually. Carry on to Step 3 and Step 4 anyway.

### Step 3. Size the drop the way Google does

Google's core update guide: wait at least a full week after the update completes, then compare the
week after with the week before the update started. Review top pages and queries.

Google's own examples:

- **Small drop in position, "dropping from position 2 to 4":** "There's no need to take drastic
  action." This points to LET IT PLAY OUT.
- **Large drop in position, "dropping from position 4 to 29":** "Do a deeper assessment." Go to
  Step 4.

Also check each search type separately (Web, Images, Video, News), as Google recommends. A drop in
one type only is a narrower problem.

If there is no Search Console data, say the size is unknown and treat Step 4 as a precaution.

### Step 4. Check the site against what each update family targets

Work through the families in this order, because a spam match changes everything after it. For each,
look at the site's pages that dropped most (or the homepage and two key pages if there is no data).
Quote what you found. Never guess what a page says; if you cannot read it, ask for the URL or text.

**A. Spam policies (a match means PANIC).** From Google's spam policies:

- **Scaled content abuse:** "many pages are generated for the primary purpose of manipulating Search
  rankings and not helping users", "no matter how it's created". Signs: a batch of near-identical
  pages (one per city, one per keyword variant), pages published faster than anyone could check them.
- **Site reputation abuse:** "third-party pages are published with little or no first-party oversight
  or involvement, where the purpose is to manipulate Search rankings by taking advantage of the
  first-party site's ranking signals." Signs: sponsored, partner or coupon sections unrelated to the
  site's purpose.
- **Expired domain abuse:** "an expired domain name is purchased and repurposed primarily to
  manipulate Search rankings by hosting content that provides little to no value to users."
- **Link spam:** paid or exchanged links, link networks. Google warns that after a link spam update
  "any ranking benefit the links may have previously generated for your site is lost" and "cannot be
  regained". Say this plainly if it applies: the fix is earning new links.

This is the **Spam Sprint** pattern: volume made to rank. The old way: pumping out pages in volume
(by AI or by people), buying links, buying old domains. Instead: fewer pages, each one something people
would want if Google did not exist.

**B. Core update and people-first content (a slip means GET TO WORK).** Google says to assess "your
site overall". Use these questions from Google's self-assessment, and
quote the page line that answers each one:

- Does the content provide original information, reporting, research, or analysis?
- Does your content clearly demonstrate first-hand expertise and a depth of knowledge?
- Is this content written or reviewed by an expert or enthusiast who demonstrably knows the topic well?
- Did you decide to enter some niche topic area without any real expertise, but instead mainly
  because you thought you'd get search traffic?
- Are you producing lots of content on many different topics in hopes that some of it might perform
  well in search results?
- Is the content primarily made to attract visits from search engines?
- Are you mainly summarizing what others have to say without adding much value?
- Does your content leave readers feeling like they need to search again to get better information
  from other sources?

Two patterns sit in these questions.

- **Topic by Topic: fake expertise.** Google says its systems "identify expertise on a topic-by-topic
  basis" (February 2026 Discover update). The old way: covering every keyword in and next to your
  industry. Instead: go deep on the topics you are actually expert in, with proof you did the work.
- **The Swallow: content made for search engines.** Google's named systems keep being swallowed into
  the core update: helpful content became part of the core ranking systems in March 2024, and the
  reviews system now improves "at a regular and ongoing pace" without announced updates. The old way:
  chasing update names, checklists and third-party "authority" scores, which Google says "don't
  correspond to any of Google's own signals". Instead: one question per page. Is this the most useful
  answer for the person searching?

For a full page-by-page grade against all of Google's self-assessment questions, point the user to the
free Helpful Content Audit skill: https://hawkacademy.co/claude-seo-skills/helpful-content-audit

**C. Reviews system (only if the site publishes reviews, comparisons or "best" lists).** Google says
the system rewards "insightful analysis and original research" by "experts or enthusiasts who know
the topic well", and evaluates page by page unless the site has a lot of review content. Check the
pages that dropped against Google's review guidance:

- Provide evidence such as visuals, audio, or other links of your own experience with what you are
  reviewing.
- Share quantitative measurements about how something measures up in various categories of
  performance.
- Explain what sets something apart from its competitors.
- Discuss the benefits and drawbacks of something, based on your own original research.
- When recommending something as the best, include why, with first-hand supporting evidence.

A review page with none of these, during or after a reviews or core update, is GET TO WORK.

### Step 5. Give the verdict

Choose one verdict. Rules:

- Any spam policy match, a manual action or a security issue: **PANIC**, whatever else is true.
- The update is still rolling out, ended under 7 days ago, a logged bug overlaps, or the drop is small
  in Google's terms: **LET IT PLAY OUT**, unless a spam match overrides it.
- A large, sustained drop after the rollout plus a week, with slips found in Step 4 or a cause found in
  Step 1: **GET TO WORK**.
- If the evidence is thin (no Search Console data, pages you could not read), give the most likely
  verdict and say what would change it.

## Output structure

```
VERDICT: PANIC / GET TO WORK / LET IT PLAY OUT
Confidence: high / medium / low, and why in one line

What was running: <update names and their dates from Google's dashboard, or "no logged update">
Rollout status: <finished on DATE / still rolling out / ended N days ago>
Size of the drop: <small / large / unknown, with the positions or clicks you compared>

Family by family
- Spam policies: clear / at risk / match. <the line or page you found>
- Core and people-first: clear / at risk / slip. <the line or page you found>
- Reviews: clear / at risk / slip / not applicable. <the line or page you found>
- Not an update: <anything from Step 1, or "nothing found">

What passed: <2 to 4 bullets>
What is at risk: <2 to 4 bullets, each tied to a Google question or policy>

First move: <ONE action, with a date. For LET IT PLAY OUT this is the date to re-check, which is the
rollout end plus 7 days. For PANIC it is the removal or the manual action fix. For GET TO WORK it is
the single highest-impact fix.>

Do not: <the one tempting move that would make this worse>
```

## Latest learnings from StudioHawk's client base

Updated monthly by Lawrence Hitches at StudioHawk. Use these as context for the verdict, never as
a replacement for Google's own criteria above. If the newest entry is more than two months older than
today, tell the user to download the latest version from
https://hawkacademy.co/claude-seo-skills/google-update-ready-check

### 2026-10-30

- Across 219 client websites and the nine Google updates from March 2025 to September 2026, the median site moved between -2.8% and +3.8% in the week after each update, and three quarters of all site-and-update pairs sat within 20 points of that. Most of our clients moved less than 20% in an update week. (StudioHawk client data, GA4 and Search Console, Google's week-after method, 30 Oct 2026.)
- Check brand searches before you panic or celebrate. Of the apparent post-update wins we could test in Search Console, 11 of 35 were brand-demand spikes (sales, launches, press), not ranking gains. Of the apparent losses, 30 of 32 were real on non-brand clicks. (Same dataset, 67 Search Console checks, 30 Oct 2026.)
- Check your own calendar before you check Google's. Six of the seven sites that looked like repeat winners were repeating their own seasonal pattern: event weeks, Boxing Day, end of financial year, spring. Compare with the same weeks a year earlier first. (Same dataset, 30 Oct 2026.)
- The clearest repeat losers had drifted off topic. A business-coaching site that dropped across the March and August 2025 updates had published unrelated viral-topic articles and added agency-service pages. A jeweller that dropped across the May and September 2026 updates had thin category pages that didn't match what searchers wanted. Removing or deepening those pages, not writing more, is what we're doing. (StudioHawk account notes and Search Console, 2025 to 2026.)
- The spam updates since August 2025 produced about three times as many clear losers per update among our clients as the core updates with comparable data (5.75 against 2.0 a window), and no more clear gainers. If your drop landed on a spam-update date, look at bulk pages, bought links and off-topic content first. (Same dataset. Hypothesis strength: four spam windows against two clean core windows, Search Console reaching back to July 2025.)

## Google's logged updates

Every ranking update and ranking bug on Google's Search Status Dashboard from 3 November 2021 to
10 November 2026. Dates are US/Pacific. "Days" is the rollout length Google logged. Entries before
March 2023 were backfilled by Google onto the dashboard on 22 March 2023.

| Began | Days | Type | Update |
|---|---|---|---|
| 2021-11-03 | 8 | spam | [November 2021 spam update](https://status.search.google.com/incidents/AFdXceQVsh1GEfKFvHyD) |
| 2021-11-17 | 13 | core | [November 2021 core update](https://status.search.google.com/incidents/FncPfR7zRSZ3diemah4o) |
| 2021-12-01 | 20 | reviews | [December 2021 product reviews update](https://status.search.google.com/incidents/hgwP7ei5H1uKbYSeZrBZ) |
| 2022-02-22 | 9 | other | [Page experience update for desktop](https://status.search.google.com/incidents/zDCQR5mxLU3ZrQeQvwqN) |
| 2022-03-23 | 14 | reviews | [March 2022 product reviews update](https://status.search.google.com/incidents/iYWoNu4QXRsQUrzxrbLv) |
| 2022-05-25 | 15 | core | [May 2022 core update](https://status.search.google.com/incidents/GHwLLtDS64a7nDng8xhD) |
| 2022-07-27 | 6 | reviews | [July 2022 product reviews update](https://status.search.google.com/incidents/Xiid524od7fpCak86sNS) |
| 2022-08-25 | 15 | helpful content | [August 2022 helpful content update](https://status.search.google.com/incidents/sbKc4YSptrSxcUZFDKwU) |
| 2022-09-12 | 14 | core | [September 2022 core update](https://status.search.google.com/incidents/Y2Cg5k2xLJvfNqR58kEt) |
| 2022-09-20 | 6 | reviews | [September 2022 product reviews update](https://status.search.google.com/incidents/ZYwuBXDhkwaoop2V5epM) |
| 2022-10-19 | 2 | spam | [October 2022 spam update](https://status.search.google.com/incidents/SAeYuxVSo39HHotQNXHr) |
| 2022-12-05 | 38 | helpful content | [December 2022 helpful content update](https://status.search.google.com/incidents/XMdX5PmbMvKW4fv3CRvn) |
| 2022-12-14 | 29 | link spam | [December 2022 link spam update](https://status.search.google.com/incidents/CxXUEK28vCKqkNocPhKR) |
| 2023-02-21 | 14 | reviews | [February 2023 product reviews update](https://status.search.google.com/incidents/NDjZ11MEUJb5i62hy5aN) |
| 2023-03-15 | 13.3 | core | [March 2023 core update](https://status.search.google.com/incidents/Cou8Tr74r7EXNthuEsaG) |
| 2023-04-12 | 13.1 | reviews | [April 2023 reviews update](https://status.search.google.com/incidents/5XRfC46rorevFt8yN8iR) |
| 2023-08-22 | 16.1 | core | [August 2023 core update](https://status.search.google.com/incidents/nBtYtBeex4GYBbdDS2LX) |
| 2023-09-14 | 13.4 | helpful content | [September 2023 helpful content update](https://status.search.google.com/incidents/53diuQvcEsgzqXTPBb8p) |
| 2023-10-04 | 15.5 | spam | [October 2023 spam update](https://status.search.google.com/incidents/NzcEhGMDhbQEdXCS35xL) |
| 2023-10-05 | 26 | ranking bug | [Ranking is experiencing an ongoing issue](https://status.search.google.com/incidents/fCUAy6TvbDMkkLAGcwkj) |
| 2023-10-05 | 14 | core | [October 2023 core update](https://status.search.google.com/incidents/VKyoS53ULWzSp8BoDxqk) |
| 2023-11-02 | 25.8 | core | [November 2023 core update](https://status.search.google.com/incidents/WtY1CQgfqrr2cjxKbyUk) |
| 2023-11-08 | 29 | reviews | [November 2023 reviews update](https://status.search.google.com/incidents/VqRTcmyQCwfpuYeaVNfn) |
| 2024-03-05 | 45 | core | [March 2024 core update](https://status.search.google.com/incidents/1jW2F89qC2NxJBWGiKxE) |
| 2024-03-05 | 14.9 | spam | [March 2024 spam update](https://status.search.google.com/incidents/iXz2PJfodvyjaVUeqxZE) |
| 2024-06-20 | 7 | spam | [June 2024 spam update](https://status.search.google.com/incidents/QdUeCQx3LRVbzQ3E7FiD) |
| 2024-08-15 | 19.2 | core | [August 2024 core update](https://status.search.google.com/incidents/gVx6b2o78zke7GrMidGy) |
| 2024-08-15 | 4.5 | ranking bug | [Ranking is experiencing an ongoing issue.](https://status.search.google.com/incidents/42XCLGtpuCZkzqe4dc6S) |
| 2024-11-11 | 23.5 | core | [November 2024 core update](https://status.search.google.com/incidents/G7rp11wqTaTGn6JjiPF3) |
| 2024-12-12 | 6.1 | core | [December 2024 core update](https://status.search.google.com/incidents/V9nDKuo6nWKh2ThBALgA) |
| 2024-12-19 | 7.1 | spam | [December 2024 spam update](https://status.search.google.com/incidents/UUq2WSouY7PhSm8zvtD1) |
| 2025-03-13 | 13.9 | core | [March 2025 core update](https://status.search.google.com/incidents/zpmwuSwifjDjfrVdaZUx) |
| 2025-06-30 | 16.7 | core | [June 2025 core update](https://status.search.google.com/incidents/riq1AuqETW46NfBCe5NT) |
| 2025-08-26 | 26.6 | spam | [August 2025 spam update](https://status.search.google.com/incidents/a7Aainy6E9rZsmfq82xt) |
| 2025-12-11 | 18.1 | core | [December 2025 core update](https://status.search.google.com/incidents/DsirqJ1gpPRgVQeccPRv) |
| 2026-02-05 | 21.7 | discover | [February 2026 Discover update](https://status.search.google.com/incidents/mYbNTqV1ytDc2fA8hUz4) |
| 2026-03-24 | 0.8 | spam | [March 2026 spam update](https://status.search.google.com/incidents/VbnSXAH4SmEcxPtx4YSD) |
| 2026-03-27 | 12.2 | core | [March 2026 core update](https://status.search.google.com/incidents/7eTbAa2jWdToLkraZj5y) |
| 2026-05-21 | 11.9 | core | [May 2026 core update](https://status.search.google.com/incidents/wdAXJk6LRRihEjpzEeWE) |
| 2026-06-24 | 2 | spam | [June 2026 spam update](https://status.search.google.com/incidents/YUX1peHev5a4fkxLDiUQ) |
| 2026-08-18 | 2.7 | spam | [August 2026 spam update](https://status.search.google.com/incidents/LEubPCm2octf2uMqCFKE) |
| 2026-09-24 | 13.7 | spam | [September 2026 spam update](https://status.search.google.com/incidents/XhUDXP7A67iHCD2kmbVu) |
| 2026-11-10 | 13.8 | core | [November 2026 core update](https://status.search.google.com/incidents/WLxcJyC6jMWMfryxsKMc) |

## Rules

- Quote Google's wording when you cite a criterion. Never invent a ranking factor, a threshold or a
  statistic.
- Never tell the user to change pages while an update is still rolling out. You lose the evidence of
  what the update did, and any recovery can no longer be traced to a fix.
- Deleting content is Google's "last resort". Recommend it only for pages that match a spam policy or
  cannot be salvaged.
- Avoid "quick fix" advice, such as removing a page element because someone said it was bad for SEO.
  Google warns against exactly this.
- One verdict. If two families are at risk, the verdict follows the order PANIC, then GET TO WORK,
  then LET IT PLAY OUT.
- Say what you could not check. A check you skipped is "not checked", never "clear".

## Voice

Plain, calm and direct. The user is worried, so lead with the verdict, then the reason. Australian
English. No em dashes or en dashes. Explain any SEO term the first time you use it.

## Edge cases

- **Discover-only drop.** Google logged a separate Discover update (February 2026). If only Discover
  traffic fell, say so and check that update.
- **Drop before the first update in the table.** Say the table does not cover it and work from Steps
  1, 3 and 4.
- **Recovery questions.** Google says improvements "could take several months" to show, and some sites
  wait for the next core update. Smaller unannounced core updates can also lift a site.
- **The user wants a guarantee.** Google itself says there is "no guarantee" changes will move
  rankings. Say so.
