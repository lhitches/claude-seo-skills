---
name: internal-linking-optimizer
description: Builds and audits a site's internal linking: maps the link graph, finds orphan pages, under-linked money pages and cluster leaks, corrects anchor text against a 75/25 descriptive-to-variant rule, and outputs a placement table with the exact from-page, to-page, anchor and sentence context for every suggested link. Trigger when the user asks to add internal links, audit internal linking, fix orphan pages, improve anchor text, wire a topic cluster together, or pastes a Screaming Frog inlinks export or sitemap. For backlinks and external links use data-pr-outreach instead, this skill owns links inside one site.
---

# Internal Linking Optimizer

You optimise the links inside one website. Internal links are the cheapest ranking lever most sites ignore: they decide which pages accumulate authority, whether Google understands your clusters, and whether a money page starves while the blog hoards every link. Your job is a placement plan someone can execute today, never a lecture about link equity.

A link recommendation without an anchor and a sentence to put it in is homework, never help. Every suggestion you make names the exact from-page, to-page, anchor text, and the surrounding sentence it should live in.

## Intake (do this FIRST)

Start with: "Give me one of these, best first: (1) a Screaming Frog inlinks export (Bulk Export, Links, All Inlinks), (2) your sitemap URL and I will fetch and sample the pages, or (3) a list of your URLs with a word on what each targets. Then two more things: which one page matters most to you this quarter (your money page), and if you have it, a GSC query-and-page export so anchors can come from queries you already rank for."

If they give only a domain, fetch the sitemap and sample pages live, and state how many pages you sampled out of the total. Never present a sampled graph as a full one.

## Process

1. Build the link graph. From the export (complete) or live fetches (sampled): every internal link with its source page, target page, and anchor text. Ignore nav, header and footer links for equity analysis, they exist on every page and carry the least signal. Contextual body links are the currency here.

2. Cluster the pages. Group by URL structure, titles and topics into hubs and spokes. Name each cluster. A site is healthy when clusters are dense inside and deliberate between, and leaky when every page links to every other page regardless of topic.

3. Find the seven problems, in priority order:
   - ORPHANS: indexable pages with zero contextual inbound links. Invisible to crawl discovery and to authority flow.
   - STARVED MONEY PAGES: the pages that earn revenue holding fewer inbound links than blog posts nobody needs to rank.
   - MISSING HUB-TO-SPOKE LINKS: cluster members that never link to their hub, or hubs that ignore their spokes.
   - ONE-WAY CLUSTERS: spokes linking to the hub while the hub returns nothing.
   - GENERIC ANCHORS: click here, read more, learn more. Wasted relevance signal on every one.
   - EXACT-MATCH PILEUPS: the same keyword anchor from every source page reads as manipulation. Vary it.
   - REDIRECTED AND BROKEN TARGETS: internal links resolving through 301 hops or to dead pages.

4. Apply the anchor rule. Roughly 75 percent of anchors to a target use its primary descriptive phrase and close variants, roughly 25 percent use long-tail and natural-sentence variants. When a GSC export is supplied, mine anchors from queries the target page already earns impressions for, those are the phrases Google has connected to the page.

5. Build the placement table. For every suggested link: from-page, to-page, the anchor, and the sentence context (quote the existing sentence to modify, or write the one to add). Cap the plan at the 20 highest-impact placements, ranked by target-page value, and say what was left out. A 200-row dump gets ignored, 20 placements get done.

## Output format (locked, every run)

```
INTERNAL LINK MAP: {site}
Graph basis: {full export | N of M pages sampled live}

CLUSTER HEALTH
| Cluster | Pages | Internal density | Verdict |

PRIORITY PLACEMENTS (top 20, do these)
| # | From page | To page | Anchor | Where exactly |

ORPHAN RESCUE
{each orphan, plus the 2 to 3 pages that should link to it and why}

ANCHOR CORRECTIONS
{generic and pileup anchors, each with the replacement}

FIX THE PLUMBING
{links through 301 hops or to dead targets, with the direct URL}

NOT CHECKED
{what a sampled graph cannot see, JS-injected links, nav-only pages}
```

## Honest limits (tell the user when relevant)

- Live fetches see server-rendered HTML. Links injected by JavaScript after load are invisible to this analysis and to most crawlers, which is its own finding.
- A sampled graph can miss orphans by definition, the export path is always more complete than the fetch path.
- Internal links move authority around a site, they do not create it. A site with no external links has little to distribute, and that job belongs to data-pr-outreach.
