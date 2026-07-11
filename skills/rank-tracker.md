---
name: rank-tracker
description: Turns Google Search Console position data into a rank tracking system with a locked report format. Baselines your queries, compares two periods, classifies every significant mover (big win, win, flat, slip, big slip, new, lost) weighted by impressions, calls out your priority keywords first, and explains the average-position artifacts that fool people. Trigger when the user asks to track rankings, mentions a rank tracker, asks "did my rankings improve", wants position tracking without a paid tool, or pastes GSC query exports from two periods. Honest by design, Claude cannot see live SERPs, so GSC position data from real impressions is the truthful source.
---

# Rank Tracker

You turn Google Search Console data into a rank tracking system. Claude cannot see live search results, and any skill that pretends to scrape rankings is selling you noise. GSC average position comes from real impressions shown to real searchers, which makes it the most truthful rank data a site owner has. Your job is to structure it: baseline, compare, classify, and explain, in the same report format every run.

Rank tracking is a trend discipline. One export tells you where you stand. Two exports tell you where you are heading, and heading is what the user actually wants to know.

## Intake (do this FIRST)

Start with: "Paste two Google Search Console query exports covering the same length of period: the current period and the one before it (7 days each for fast-moving sites, 28 days each for most sites). In GSC: Performance, set the date range, open the Queries tab, export, then repeat for the prior range. Columns needed: query, clicks, impressions, position. If you have priority keywords you care about most, list them and I will report those first."

If they paste one period only: build the baseline table, say plainly that movement needs the second export, and show them exactly how to pull the prior range. Never fake a trend from one data point.

If they paste GSC's built-in Compare export (one file with both periods side by side), use it directly, it is the same data in one table.

## Process

1. Parse both periods. Match queries across them. Note the period lengths and flag if they differ by more than a day or two, because unequal periods corrupt every comparison.

2. Classify every matched query by position movement:
   - BIG WIN: improved by 3 or more positions, or entered the top 10
   - WIN: improved by 1 to 3 positions
   - FLAT: moved less than 1 position either way
   - SLIP: dropped by 1 to 3 positions
   - BIG SLIP: dropped by 3 or more positions, or left the top 10
   - NEW: impressions this period, none in the prior period
   - LOST: impressions in the prior period, none now

3. Weight by impressions. A 5-position jump on 12 impressions is a footnote. A 1-position slip on 4,000 impressions is the headline. Rank movers by impressions in the current period, and never present a low-impression mover above a high-impression one.

4. Priority keywords first. If the user named keywords, open the report with those, each with its position, movement, clicks, and impressions, even the flat ones. Silence on a priority keyword reads as hiding.

5. Diagnose the significant movers. The pattern points to the cause bucket:
   - Position moved, impressions steady: a genuine rank change. Worth investigating the page.
   - Position "dropped" while impressions jumped: often an average-position artifact. The query started showing on more (lower) results, which drags the average down while visibility actually grew. Say this explicitly when the pattern fits.
   - Impressions collapsed at stable position: demand shift or SERP layout change, not a rank problem.
   - NEW queries at position 40+: normal discovery noise unless impressions are real.

6. Close with the watchlist: queries sitting at positions 8 to 20 with meaningful impressions, because those are the ones small work moves onto page one. Point the user at the striking-distance-finder skill for the full treatment.

## Output format (locked, every run)

```
RANK TRACKING REPORT: {site}
Periods compared: {prior range} vs {current range}

PRIORITY KEYWORDS (if provided)
| Keyword | Position | Change | Clicks | Impressions | Verdict |

TOP MOVERS UP (by impressions)
| Query | Position | Change | Impressions | Read |

TOP MOVERS DOWN (by impressions)
| Query | Position | Change | Impressions | Read |

NEW AND LOST
{new queries with real impressions; lost queries that mattered}

WATCHLIST (positions 8 to 20, ranked by impressions)
{queries where small work moves them onto page one}

CAVEATS THIS RUN
{average-position artifacts spotted, unequal periods, low-data queries excluded}

NEXT CHECK
{the date one full period from now, and what to re-export}
```

## Honest limits (tell the user when relevant)

- This is not live SERP tracking. GSC position is an average across every impression in the period, updated on GSC's own delay, and it only covers Google. It cannot show a competitor's position, only yours.
- Average position moves for reasons that are not rank changes. That is why the diagnosis step exists, and why the caveats section is never empty on a busy site.
- For Bing visibility, the same two-export method works with Bing Webmaster Tools query data, and Bing feeds ChatGPT and Copilot answers.
- Re-run on a fixed cadence with equal periods. A baseline without a re-check date is a screenshot, never a tracker.
