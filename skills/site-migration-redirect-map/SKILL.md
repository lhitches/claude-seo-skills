---
name: site-migration-redirect-map
description: Builds and verifies the redirect map for a site migration, ordered by what is actually at risk rather than by URL count. Joins the old URL set to Search Console impressions, clicks and queries so the pages carrying real demand are mapped first, matches every old URL to its best new destination with a stated confidence, flags the ones that need a human decision instead of guessing, and after launch reads the live response chain per URL to prove the redirects shipped. Trigger when the user mentions a site migration, replatform, domain change, URL structure change, HTTPS or www consolidation, a redirect map or redirect plan, or asks why traffic dropped after a relaunch. For crawl and indexing problems unrelated to a migration, use technical-seo-audit.
---

# Site Migration and Redirect Map

Migrations lose traffic for one reason above all others: the redirect map was built from a URL list instead of from a demand list. A spreadsheet that diffs old URLs against new URLs treats a page with 40,000 impressions and a page nobody has ever visited as the same row of work, so the team spends its attention evenly and the expensive mistakes hide in the middle of it.

Your job is to invert that. Rank the old URL set by what it earns before you map a single destination, map the top of that list carefully, and prove afterwards that the redirects actually shipped by reading what the server returns rather than by re-reading the plan that was supposed to produce them.

## Intake (do this FIRST)

Ask for all of these, then start with whatever arrives:

"To build this properly I need four things.

1. The old URL set. A crawl export (Screaming Frog, Sitebulb), the old sitemap.xml, or a plain list. Whatever is most complete.
2. A Search Console export for the old site, Pages and Queries, 12 or 16 months if you can get it. This is the one that decides the order of the work, and without it I can only sort by URL structure.
3. The new URL set, or the URL rules if the new site is not live yet. A sitemap, a staging crawl, or the pattern (for example /blog/{slug} becomes /resources/{slug}).
4. What kind of migration this is: domain change, replatform, URL restructure, HTTPS or www consolidation, site merge, or several at once.

If you also have a backlink export for the old site, send it. Links change which URLs matter."

If the Search Console export is missing, say so plainly and proceed: "No GSC export, so ordering is by URL structure and crawl depth, which is a weaker proxy for value. The map will be complete and the priority order will be a guess. Get the export before launch if you can."

Ask one thing before mapping anything: **is any page being retired on purpose?** A migration is the moment teams quietly kill pages, and a retired page mapped to a near-match destination is worse than a clean 410.

## Process

1. **Rank before you map.** Join the old URL set to the GSC Pages export. Sort by clicks first, then impressions. Compute what share of total clicks sits in the top 50 URLs and say it out loud, because on most sites it is a large majority and it tells the team where the care belongs. Segment the remainder into: earns clicks, earns impressions only, earns nothing but is linked internally, and earns nothing and is linked from nowhere.

2. **Match each old URL to a destination**, working down the ranked list, and record a confidence with every row:
   - EXACT: same content at a new address. Safe to automate.
   - PATTERN: covered by a rule (a path prefix change, a domain swap). Safe to automate, but spot-check five URLs per rule against the live new site, because a rule that is 99% right is 100% wrong on the pages it misses.
   - CLOSEST: no equivalent page, but a genuinely relevant destination exists. Needs a human to confirm.
   - CONSOLIDATE: several old URLs collapse into one new page. Record every source, because these are the rows that later explain a query losing its ranking.
   - NO MATCH: nothing relevant exists. Do not invent one.

3. **Never redirect to the homepage to make the map look finished.** A redirect to an irrelevant destination is treated as a soft 404 and passes nothing, so it costs the same as a 404 while hiding the problem from every report. For a NO MATCH row the honest options are: build the destination, redirect to the closest relevant category or parent, or serve 410 Gone deliberately. Say which one you recommend per row and why. A page earning clicks almost never deserves a 410.

4. **Check the query layer on every CONSOLIDATE row.** Pull the queries each source URL ranked for from the GSC Queries export. If two sources rank for different intents, consolidating them means one intent loses. Flag it before launch rather than diagnosing it after.

5. **Find the chains and the loops before launch, not after.** Where old rules already exist, resolve every mapped source through the full chain. Anything reaching its destination in more than one hop gets rewritten to point straight at the final URL. Chains dilute, slow crawling, and quietly break when someone removes a middle rule later.

6. **Cover the things a URL list does not contain.** Walk these explicitly and report each as covered or not applicable: canonical tags pointing at old URLs, hreflang clusters referencing old URLs, XML sitemaps (submit the new one, keep the old one available briefly), internal links still pointing at old URLs (redirects are a safety net, never a substitute for updating the link), image and PDF URLs, paginated series, parameterised and faceted URLs, and the robots.txt of the new site (a staging `Disallow: /` shipped to production is the single most common catastrophic migration error).

7. **Prioritise the launch checklist** by the ranking from step 1, not by category. The top 50 URLs by clicks get verified individually and by hand. Everything else gets verified by sample.

8. **Verify after launch by reading the live response.** Request each mapped source URL, following redirects, and record the full chain: every hop, every status code, and the final URL and status. A row passes only when the chain is a single 301 to the intended destination and that destination returns 200. Test the redirects, never the spreadsheet: a map that says a rule exists is a description of intent, and only the response proves it shipped. Re-run at 24 hours, 7 days and 30 days, and read Search Console coverage and the old property's impressions alongside it.

## Output format (locked, every run)

```
MIGRATION REDIRECT MAP: {old site} to {new site}
Type: {domain change / replatform / restructure / consolidation / merge}
Old URLs: {n} | Mapped: {n} | Needs a decision: {n} | Data: {GSC window, or "no GSC export"}

WHERE THE VALUE SITS
Top 50 URLs carry {pct} of clicks and {pct} of impressions
Earns clicks: {n} | Impressions only: {n} | Internal links only: {n} | Nothing: {n}

THE MAP (ordered by clicks, highest first)
| # | Old URL | Clicks | Impressions | New URL | Confidence | Note |

NEEDS A HUMAN DECISION
{NO MATCH and CLOSEST rows that earn traffic, each with a recommendation and the reason}

CONSOLIDATION RISK
{each many-to-one row, the queries each source ranked for, and the intent at risk}

CHAINS AND LOOPS
{every source resolving in more than one hop, rewritten target}

BEYOND THE URL LIST
{canonicals, hreflang, sitemaps, internal links, images and PDFs, pagination, parameters, robots.txt: covered or not applicable}

LAUNCH CHECKLIST (in order)
1. ...

POST-LAUNCH VERIFICATION
| Old URL | Hops | Chain | Final status | Pass or fail |

NOT CHECKED
{what was missing, what was sampled rather than tested, what only time can confirm}
```

## Honest limits (tell the user when relevant)

- Without a Search Console export the priority order is a guess. The map will be complete and the ordering will be structural, which is the weakest part of this skill and the easiest to fix.
- A redirect map cannot tell you whether the new page is as good as the old one. Redirects preserve the address, never the content quality, and a migration that redirects perfectly into thinner pages still loses rankings. That is a content problem wearing a technical disguise.
- Recovery takes time and some loss is normal. Report what was verified rather than promising a recovery window, and do not attribute a drop to the migration until the redirect chains have been read and confirmed clean.
- Sampled rows are stated as sampled. A rule verified on five URLs is evidence about those five, and a pattern is not proven until the count of URLs it matched is compared against the count of URLs it should have matched.
- If the old site is already switched off, the old URL set and its GSC history may be unrecoverable. Say so rather than reconstructing a list from the new site, which can only ever contain the URLs that survived.
