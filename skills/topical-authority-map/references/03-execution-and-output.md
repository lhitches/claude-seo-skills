# Phase 3: Execution and Output

This phase finishes the map. You define how the central entity appears on every page, optionally check NLP categories, build content briefs for the first 30 articles, sequence the publishing order across 12 weeks, then generate the .xlsx (five tabs) and the strategy .md.

There are no checkpoints in this phase. The map should be complete and confirmed by the time you arrive here.

---

## STEP 11: CENTRAL ENTITY SITEWIDE PRESENCE

Define exactly how the central entity appears on EVERY page.

### Template for every page

1. **Header or nav (template-level):** business name plus what you do.
   - Example: "Dr. Smith. Rhinoplasty Surgeon, Denpasar."

2. **Footer (template-level):** two or three sentence company description that includes the central entity.
   - Example: "Dr. Smith is Denpasar's leading rhinoplasty surgeon, helping patients achieve natural-looking results through advanced surgical techniques."

3. **Every page's intro paragraph:** ONE natural mention of the central entity.
   - Example on AOR page: "At [Clinic Name], our rhinoplasty surgeons in Denpasar recommend the following recovery timeline."

4. **Every page's supplementary section (above footer):** ONE natural mention plus CTA.
   - Example: "If you are considering rhinoplasty in Denpasar, our board-certified surgeons can walk you through the full recovery process during your free consultation."

5. **Every page:** ONE internal link to the main core page.
   - Example: "Learn more about our [rhinoplasty services in Denpasar](/rhinoplasty-denpasar/)."

### Central search intent. Consistent language sitewide.

- Consistent verbs: "provide", "offer", "specialise in".
- Consistent nouns: your services, products, entity names.
- Consistent adjectives: "expert", "experienced", "affordable", "premium".
- These appear in title tags, H1s, heading structure, paragraphs, and image alt text.
- Our working theory: a paragraph that drifts off topic weakens that section, the section weakens the page, and a weaker page is a weaker page to link from. Keep the context consistent.

### What NOT to do
- Do not force the entity into every paragraph. That is keyword stuffing.
- Do not write unnatural sentences to cram it in.
- ONE intro mention, ONE supplementary mention, ONE internal link is enough.

---

## STEP 12: NLP CATEGORY CHECK (OPTIONAL DIAGNOSTIC)

This step is optional. It is a diagnostic for spotting pages that drift off topic, with no pass or fail. Google Cloud's Natural Language API is a separate Google Cloud product: it is not a Google Search ranking test, and no documented Google Search rule says pages must share a category.

### How to check
- Use Google Cloud's Natural Language API (the classifyText method), or manually assess: "What category would this page fall into?"
- Most pages on a focused site should land in the site's main category. A family law site would expect `/Law & Government/Legal` for most pages. Use the API's own category names, which use "&".
- The narrower `/Law & Government/Legal/Family Law` is a V2 category. The API uses the older V1 categories unless you ask for V2, so to get it, add `"classificationModelOptions": {"v2Model": {"contentCategoriesVersion": "V2"}}` to the request.
- A page can legitimately get a different category, or several. A family law page that comes back as `/Health` or `/Shopping` is worth a look, not an automatic rewrite.

### If a page drifts
Look at why first. If it has wandered off topic:
- Rewrite the intro and headings to use language consistent with the site's topic.
- Add the central entity mention (Step 11) to anchor it.
- Check that internal links FROM this page use anchor text relevant to the site's main topic.

If the page is on topic and simply serves a different need, leave it. Note any pages that drift, and what you found, in the strategy document.

---

## STEP 13: CONTENT BRIEFS FOR THE FIRST 30 ARTICLES

A topical map without content briefs is incomplete. You do NOT need briefs for all 90 articles before you can start. Generate briefs for the first 30 (the AOR wave that publishes in weeks 1 to 6) so the user can hand them to a writer immediately.

For the remaining 60, list page title, target keyword, URL slug, and one-line scope. The user can ask for full briefs in a second pass.

### Content Brief Format (first 30)

| Field | Value |
|---|---|
| Page Title | The page title |
| Target Keyword | The target keyword |
| URL Slug | The URL slug (`/folder/keyword/`) |
| H1 | H1 text |
| Title Tag | Title tag, keyword in first five words, no length target (Google sets no limit and cuts titles to fit the screen) |
| Meta Description | Keyword and the reason to click up front, no length target |
| Buyer Stage | TOFU, MOFU, or BOFU (plus Retention if applicable) |
| Word Count Target | A rough range from competitor analysis. A guide, not a rule: cover what the reader needs |
| H2 Sections | List of H2s, each mapping to an expanded query |
| Internal Links Out | Which pages to link TO, with anchor text |
| Internal Links In | Which pages should link TO this page |
| Entities to Mention | Key entities from Knowledge Graph research |
| Information Gain Angles | What competitors do NOT cover |
| Image Requirements | Number of images, alt tag keywords |
| CTA | What action should the reader take? |
| Persona Angle | How does the real author's or reviewer's expertise frame this content? |
| Client Situation | Which client situation(s) does this page serve? |

### Brief format for articles 31 to 90 (lighter)

| Field | Value |
|---|---|
| Page Title | The title |
| Target Keyword | The keyword |
| URL Slug | `/folder/keyword/` |
| Buyer Stage | TOFU, MOFU, or BOFU |
| One-line scope | What this article must cover |
| Links to (Core) | Which core page it links to |

These can be expanded to full briefs in a follow-up pass once the first wave is shipping.

---

## STEP 14: PUBLISHING ORDER ACROSS 12 WEEKS (AVALANCHE THEORY)

Publish in sequence, not all at once. The plan spreads 90 articles across 12 weeks, but timing varies by site: set the pace by what the team can write well, and adjust as results come in. Here is the order.

### Phase 1: Foundation (week 0, before week 1)
Before the 12-week clock starts, the user should already have:
- Homepage live with central entity mentions (Step 11) wired in.
- Core service or product pages live (the BOFU money pages).
- About page with the real author's or reviewer's details.
- Contact page.

If any of these are missing, week 1 starts here. The 12-week schedule below assumes they exist.

Fix anything broken on the core pages straight away, whatever the week: wrong intent, thin content, pages that are not indexed. Do not save those fixes for later. Only the big core-page rewrites wait for Phase 4.

### Phase 2: AOR Wave (weeks 1 to 6, 30 articles)
- 30 AOR articles targeting low-to-medium competition keywords.
- Five articles per week. Hand the first 30 content briefs straight to a writer.
- Each article links to one or two relevant core pages in the body content.
- Our working theory: these build a track record on the topic before the big core-page rewrites.

We think this is the wave that shows Google you specialise in the topic.

### Phase 3: MOFU Wave (weeks 7 to 10, 40 articles)
- Buyer guides ("how to choose between X and Y").
- Comparisons ("X vs Y").
- Decision-stage content (case studies, brand reviews, pricing explainers).
- 10 articles per week.
- These convert TOFU researchers into BOFU buyers.

In our experience this is the wave most websites skip, and the one that produces most of the conversion lift.

### Phase 4: Core Optimisation (weeks 11 to 12, 20 articles)
- Do the big rewrites of the existing BOFU core pages now that the supporting content is live, so they can link to it and build on it. (Anything broken was fixed in the Foundation phase.)
- Add new BOFU pages where the map has gaps.
- Add a Retention layer if relevant (aftercare, maintenance, FAQ).
- Our working theory: the supporting content from Phases 2 and 3 helps the core pages compete for the high-competition keywords.

### Publishing frequency

Five to ten articles per week suits most teams, but set the pace by what you can publish at a consistently high standard, and adjust it as results come in. Do not rush out a batch of weak articles to hit a number.

### The order, in one sentence

Fix anything broken on the core pages now. Then AOR first, linking woven in throughout, MOFU buyer guides next, and the big core-page rewrites last. How fast results follow varies by site: Google says some changes show within days and others take several months.

---

# OUTPUT GENERATION

## Deliverable 1: spreadsheet (.xlsx) with five tabs

Generate using the xlsx skill. If you cannot create files in this environment, output each tab as its own CSV code block instead, and say so.

### Tab 1: Core Pages

| Page Title | URL Slug | Folder | Target Keyword | Search Volume | Buyer Stage | H1 | Title Tag | Meta Description | Competition Level |

12 to 20 rows. Search Volume holds a real figure from a keyword tool or the user's keyword data, or "no data". Never an estimate, and never Search Console impressions: if the user supplied those, add them as an extra column headed "GSC impressions (date range)". These are the BOFU money pages.

### Tab 2: AOR Pages

| Page Title | URL Slug | Folder | Target Keyword | Search Volume | Buyer Stage | Links To (Core) | H1 | Title Tag | Meta Description | Competition Level |

60 to 80 rows. These are the supporting authority articles.

### Tab 3: Linking Map

| Source Page | Target Page | Anchor Text | Link Type | Placement | Reader Relevance |

Every internal link, with anchor text, link type (AOR to Core, AOR to AOR, etc.), and a reader-relevance check.

### Tab 4: Buyer Journey

| Page | Stage | Content Type | Target Keyword | Notes |

Every page tagged TOFU, MOFU, or BOFU (plus Retention if used). Use cell colour to make the three tiers instantly readable: light yellow for TOFU, light blue for MOFU, light green for BOFU. Retention can be light grey.

### Tab 5: Publishing Order

| Week | # | Page Title | Cluster | Target Keyword | Buyer Stage | Brief Link | Notes |

90 rows. Sequenced AOR Wave (weeks 1 to 6), MOFU Wave (weeks 7 to 10), Core Optimisation (weeks 11 to 12). List any urgent core-page fixes (wrong intent, thin content, not indexed) above them as week 0. Briefs for rows 1 to 30 should be linked or expanded inline. Rows 31 to 90 use the lighter brief format.

## Deliverable 2: strategy document (.md)

Generate a markdown file containing:

1. **Central Entity Definition.** What it is, location, modifier, EAV attributes.
2. **Source Context and Persona.** Business type, market, angle, customer language, and the real author or reviewer with their checkable credentials.
3. **Knowledge Graph Summary.** Key entities, relationships, topic distances.
4. **Folder Structure.** Full hierarchy with rationale.
5. **Central Entity Template.** Exact copy for header, footer, intro, supplementary, and internal link.
6. **NLP Category Check (optional).** The site's main category and any pages that drift from it.
7. **Linking Rules Summary.** The linking rules plus client-situation-based linking decisions.
8. **Buyer Journey Gaps.** Any stages without coverage and the recommended pages to fill them.
9. **Information Gain Opportunities.** Queries and angles no competitor covers.
10. **Content Priorities.** Ordered publishing schedule (Avalanche Theory) and why this order.
11. **Off-Site Topical Authority Plan.** Link building targets, branded search strategies, media opportunities.
12. **Quality Standards.** The minimum quality bar per article. The warning about low-quality content dragging down the whole site.
13. **Dynamic Updates.** Note that the map should be reviewed quarterly as Google's indexes evolve.
14. **Folder Structure, Client Situations, Query Expansion, and Merged Attributes.** These are documented in the .md (not in separate tabs of the spreadsheet) so the user has a single strategy document plus a single spreadsheet.

---

## Final step. Present both deliverables.

When the spreadsheet and strategy document are done, present them with this short summary:

"You have two files:
1. A spreadsheet with five tabs. Open Core first to confirm your money pages. Then read AOR for your authority gaps. Then look at the Linking Map for where to route signals. Then check Buyer Journey for which stages are missing content. Then the Publishing Order tells you exactly what to ship and in what order across the next 12 weeks.
2. A strategy document. Read it once before you start writing. It has the rules of how every page should mention your business, how to link between pages, and what NOT to do.

Fix anything broken on your Core pages first (wrong intent, thin content, pages not indexed). Then start the AOR Wave: hand the first 30 content briefs to a writer, and save the big Core page rewrites until the supporting content is live. Timing varies by site, so treat the 12 weeks as a plan, not a ranking forecast."

---

**The map is dynamic, not static.** Search results change. Predicates that used to share results (like "install" and "setup") can return different result sets as Google's systems change, for example after a core update. When that happens, recheck the intent and the overlap before deciding whether they still share a page. Review and update the map quarterly.

**Research tools for Knowledge Graph work:**
- Wikipedia Graph visualiser: blinpete.github.io/wiki-graph
- Wikidata: wikidata.org
- DBpedia: dbpedia.org
