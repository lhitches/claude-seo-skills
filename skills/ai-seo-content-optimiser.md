---
name: ai-seo-content-optimiser
description: Optimises an existing web page so AI search tools (ChatGPT, Google AI Overviews and AI Mode, Gemini, Perplexity) are more likely to cite it. Checks first that it is the right page to work on, scores it against a 12-rule passage checklist, then returns a scorecard, before/after edits and a source-checked list of statistics. Never invents a number. Use when someone says "optimise this page for AI", "make this page citable", "AEO this page" or "AI SEO content optimiser".
---

# AI SEO Content Optimiser

Built by Hawk Academy from published AI search studies and StudioHawk's own testing. Give it a URL or paste the page, plus the question the page should answer.

**If you cannot run a step yourself, say so.** Some steps need things you may not have in this chat: live answers from other AI tools, or a fetch that sends an AI crawler's user agent. Do not guess the result. Write NOT CHECKED for that step, tell the user how to check it, and carry on with the rest.

## Step 0. Is this the right page? (do not skip)

1. **Name the question.** Write the one question the page should win, plus 5 to 10 related questions people ask around it. AI tools expand a question into several sub-searches ("fan-out"), and that set changes from run to run, so work on the questions that keep coming up, not one exact list.
2. **Check who AI cites today.** Ask ChatGPT, Google AI Mode and Perplexity the main question. Note which pages they cite. If you cannot ask those tools yourself, ask the user to run the question in each one and paste the answers with their cited links; until they do, mark this check NOT CHECKED. In Google, the cited link often ends in `#:~:text=...`, which shows the exact sentence it used. If AI already cites a different page on the same site, optimise that page or merge the two, rather than splitting one question across several thin pages.
3. **Check AI can read the page.** Fetch the URL with the user agents of the AI crawlers (GPTBot, ClaudeBot, PerplexityBot), not just a browser. Some sites redirect browsers and Google but send AI crawlers a 404. A page the crawler cannot fetch cannot be cited. If you cannot send those user agents yourself, mark this check NOT CHECKED. Point the user to the free checker at https://hawkacademy.co/seo-tools/ai-crawler-access-checker/ to see whether their robots.txt lets those crawlers in. That checker reads robots.txt only, so a 404 sent to crawlers by the server still needs a request that sends the crawler's user agent (for example with `curl -A`), run by the user or their developer.
4. **Set expectations.** Page content is only part of AI visibility. Brand recognition and mentions on other websites do much of the rest: most brand mentions in AI answers come from third-party sites. Being cited as a source is also different from being recommended. Say this in the report so nobody expects one page edit to do everything.

## Step 1. Score the page, passage by passage

Score each rule PASS / PART / FAIL and quote the line that proves it.

| # | Rule | Test |
|---|---|---|
| 1 | **Answer first** | The first sentence under each heading answers that heading, using the heading's own words. The first 40 to 60 words are the answer, not a lead-in. |
| 2 | **Key answer high on the page** | A short summary or key takeaways near the top. Studies of ChatGPT citations find a large share come from the first third of a page. |
| 3 | **Self-contained passages** | Each paragraph names what it is about. No "it" or "this tool" carrying the meaning, because AI lifts passages out of context. |
| 4 | **One idea per passage** | Roughly 60 to 120 words per paragraph. A paragraph mixing two ideas gets split. |
| 5 | **Facts over adjectives** | Claims carry numbers, names and dates. "Fast" becomes "processes 10,000 keywords in 4 seconds". |
| 6 | **Definitive language** | Facts are stated plainly. No "will", "should", "might", "could" or "may" inside a factual claim. |
| 7 | **Entities named** | People, brands, products, places and standards are named, using the same words people search with. |
| 8 | **Tables for comparisons** | Anything compared across 3 or more items on 2 or more points becomes a table. |
| 9 | **Real FAQs** | Questions people actually ask, each answered straight after the question in a short, direct answer (20 to 25 words is this skill's starting length, not a measured rule). |
| 10 | **Plain words** | Any term a beginner would not know is explained in the sentence where it first appears. |
| 11 | **Proof on the page** | Claims about the business (awards, years trading, results) link to a third-party page that confirms them. |
| 12 | **One page per question** | No other page on the site chases the same question. |

## Step 2. Rewrite: edits, not a new page

- Give edits as **before / after pairs**, one per failing rule, highest impact first. Leave everything that already passes exactly as it is.
- **Never invent a statistic.** For every number added or kept, put the source link next to it, then open that source and confirm the number is actually on the page. If it is not, drop the number and say so.
- If there is no real statistic for a point, make the claim concrete another way: a named example, a step, a date.
- Keep the author's voice. Do not turn the whole page into bullets: use tables and lists for comparisons and lists, and keep prose for arguments.
- Do not add length for its own sake. Longer pages are not cited more just because they are longer.
- Avoid the tells of AI-written text: em dashes, "it's not X, it's Y", lists of three for rhythm, vague words like "seamless" or "game-changing".

## Step 3. Report, in one message

1. **Right page?** Four lines: the question, who AI cites today, whether AI crawlers can fetch the page, and the expectations note.
2. **Scorecard:** the 12 rules, PASS / PART / FAIL, one line each.
3. **Edits:** before / after pairs, highest impact first.
4. **Statistics:** each number, its source link, and VERIFIED (found on the source) or DROPPED.
5. **After publishing:** request indexing, then in 2 to 4 weeks ask the main question again in ChatGPT, AI Mode and Perplexity, and note which sentence gets cited.
