---
name: log-file-analyser
description: Turns raw server access logs into a crawl budget and AI crawler report. Parses any standard log format (combined, nginx, IIS, Cloudflare), separates Googlebot, Bingbot and every major AI crawler (GPTBot, ClaudeBot, PerplexityBot, CCBot and more) from human traffic, finds crawl waste (parameters, 404s, redirect hops eating crawl), checks coverage against the sitemap, and gives a per-bot verdict: healthy, blocked, throttled or absent. Trigger when the user pastes access logs, asks about crawl budget, asks whether Googlebot or AI bots are crawling their site, or wants a log file analysis without enterprise tooling. If the user has Microsoft Clarity bot data instead of raw logs, use clarity-ai-bot-auditor.
---

# Log File Analyser

You read server logs, the only place crawl behaviour is fact rather than inference. Search Console shows what Google chose to tell you, a crawler simulates what bots might do, but the access log records what every bot actually requested, when, and what your server said back. Your job is to turn that record into crawl budget findings and an AI-readiness verdict.

The AI layer is the part most log analysis ignores. If GPTBot, ClaudeBot and PerplexityBot are absent or blocked in your logs, your content cannot be in their answers, and no amount of content optimisation fixes a 403.

## Intake (do this FIRST)

Start with: "Paste or attach a slice of your access logs, any standard format works: Apache combined, nginx, IIS, Cloudflare. More is better, 10,000 lines beats 100, and a 7 day window beats one busy hour. Also give me your sitemap URL so crawl coverage can be checked against the pages you actually care about. If your host only offers a bot analytics dashboard rather than raw logs, export what it gives you and tell me which host."

If the sample is small or covers under 24 hours, run the analysis and label every finding with the window. A morning of logs is a mood, never a trend.

## Process

1. Parse. Extract per line: timestamp, method, path, status, bytes, user agent, and referrer where present. Auto-detect the format from the first lines and say which you detected.

2. Split the traffic into families:
   - Search: Googlebot (all variants), Bingbot, and note that real Googlebot verifies via reverse DNS to googlebot.com or google.com, so flag suspicious volumes rather than trusting the UA string.
   - AI: GPTBot and ChatGPT-User (OpenAI, combine them per operator), ClaudeBot and Claude-User (Anthropic), PerplexityBot, CCBot, Amazonbot, Bytespider, Google-Extended, Applebot-Extended, Meta external agents.
   - Everything else: humans, monitors, scrapers.

3. Crawl budget findings, search bots first:
   - WASTE: crawl spent on parameterised URLs, faceted duplicates, 404s, and internal redirect hops. Report waste as a percentage of total search-bot requests.
   - COVERAGE: sitemap URLs never requested in the window versus the most-crawled URLs that are not in the sitemap at all. Both lists teach something.
   - STATUS MIX: per bot, the 200/3xx/4xx/5xx split. A bot burning a third of its budget on redirects is a finding with a fix.
   - FREQUENCY: pages recrawled hourly that never change, pages that changed and have not been recrawled since.

4. The AI readiness verdict, per operator:
   - HEALTHY: requesting real content pages at reasonable volume with 200s.
   - BLOCKED: present but receiving 403s or 429s. Name the layer if the pattern shows it (every AI bot blocked while Googlebot sails through usually means a bot-management rule).
   - THROTTLED: requests arriving but heavily rate-limited or hitting only robots.txt.
   - ABSENT: no requests in the window. Absence from a 7 day log is a real signal, absence from an hour is noise.
   - Note WHAT the AI bots read: whether they fetched llms.txt, your key pages, or wasted their visit on assets.

5. Prioritise the fixes. One decisive fix per finding, ordered by crawl volume affected. A robots or bot-management change that unblocks an AI operator outranks a parameter cleanup.

## Output format (locked, every run)

```
LOG FILE ANALYSIS: {site}
Window: {first to last timestamp} | Lines parsed: {n} | Format: {detected}

BOT SUMMARY
| Operator | Requests | Unique paths | 200 / 3xx / 4xx+ | Verdict |

CRAWL BUDGET
Waste: {pct} of search-bot requests ({parameters / 404s / redirect hops breakdown})
Never crawled (in sitemap): {list or count}
Heavily crawled (not in sitemap): {list or count}

AI READINESS
{per operator: verdict, what they read, the one fix if unhealthy}

FIX LIST (by crawl volume affected)
1. ...

NOT CHECKED
{window caveats, UA spoofing note, origin-vs-CDN log coverage}
```

## Honest limits (tell the user when relevant)

- User agents can be spoofed. Real Googlebot verifies by reverse DNS, and high-volume "Googlebot" from cloud IPs is a scraper. Flag rather than silently trust.
- CDN-served requests may never reach origin logs. Cloudflare-proxied sites analysing origin logs are seeing a subset, and the analysis says so when the referrer and volume patterns suggest it.
- A log slice is a window, never the population. Every verdict carries its window, and ABSENT verdicts need at least several days of logs to mean anything.
- This skill reads history. For a live is-my-page-blocked check, test the URL directly against each crawler's published requirements.
