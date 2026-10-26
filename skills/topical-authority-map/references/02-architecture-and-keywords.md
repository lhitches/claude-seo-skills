# Phase 2: Architecture and Keywords

This phase turns the classified attribute list from Phase 1 into a working site architecture: folders, buyer journey tags (TOFU, MOFU, BOFU), expanded queries with cost-of-retrieval scoring, target keywords, and the linking architecture that makes the four clusters compound.

There is one checkpoint in this phase. Pause and confirm before proceeding.

---

## STEP 6: DEFINE FOLDER STRUCTURE

Folders keep the site organised; internal links do the heavy lifting. Google says it mostly works out a site's structure from the links between pages, not from its URLs, so treat folders as a way to keep content organised, and rely on crawlable navigation and internal links to show how pages relate.

### Recommendations
1. Each major topic gets its own folder.
2. Folder name is the ROOT KEYWORD ONLY (just "divorce", not "divorce-lawyer-sydney").
3. Use Semrush Keyword Magic (or equivalent): type the root word, check all variations, pick the right root. If neither you nor the user has a keyword tool, pick the root from the language competitors and the user's customers use, and say it is unchecked.
4. Sub-topics live inside the parent folder.

### Example. Family Law.

```
/family-lawyer-sydney/          (Core hub page)
/family-law/
  /divorce/
    /divorce-application/
    /divorce-process/
    /property-settlement/
  /custody/
    /child-custody/
    /parenting-plans/
    /visitation-rights/
  /de-facto/
    /de-facto-relationships/
    /property-settlement-de-facto/
  /family-law-act/
    /section-4aa/
    /part-vii-children/
```

### Why we use folders
- Forces you to think about which category each page belongs to.
- Keeps related pages together (all `/divorce/` pages sit side by side), which makes the internal linking easier to plan.
- Easier to report on in analytics.
- Easier for people to follow. On larger sites (more than a few thousand URLs), folders can also help Google learn how often each section changes. Use internal links to show how pages relate.
- In WordPress, use Pages (not Posts) with parent and child relationships to build this structure.

### Image URLs follow folder structure
- Images embedded on pages should have URLs that include relevant keywords.
- Example: `/family-lawyer-sydney/john-bale-family-lawyer.jpg`
- Image alt tag varies by context. On profile page: "John Bale Family Law Associate". On Sydney family lawyer page: "John Bale Family Lawyer Sydney".

---

## STEP 7: MAP EVERY PAGE TO TOFU, MOFU, OR BOFU

Every page must sit in one of three buyer journey stages. (For more nuance you can split BOFU into Decision and Retention. For a public map, keep it to three.)

### TOFU. Top of Funnel
- User has a PROBLEM but is researching, not buying.
- Content type: problem-awareness, definitions, explainers, "what is" articles.
- Keyword patterns: symptom-based, question-based, problem-description, "what is", "how does", "why does".
- Examples: "my tooth hurts", "water leaking from ceiling", "what is property settlement".
- Page role: educate about the problem, introduce the solution category, link to MOFU pages.
- This is most of your AOR content.

### MOFU. Middle of Funnel
- User knows the solution exists, evaluating WHETHER and HOW to act.
- Content type: comparison content, "how to choose", buyer guides, "X vs Y" articles, pricing explainers, case studies.
- Keyword patterns: "best [service]", "how does [service] work", "[A] vs [B]", "[service] cost", "[service] near me".
- Examples: "rhinoplasty surgeon Denpasar", "emergency plumber near me", "how to choose a dining table".
- Page role: move researchers into decision mode. This is where most websites have the biggest gap.

### BOFU. Bottom of Funnel
- User is ready to act and choosing WHO.
- Content type: service pages, product pages, pricing pages, booking pages, testimonials, brand reviews.
- Keyword patterns: "[brand] reviews", "[service] [location]", "[service] pricing", "buy [product]", "book [service]".
- Examples: "rhinoplasty Bali clinic", "Dr Smith reviews", "buy Australian oak dining table".
- Page role: convert. These are your money pages.

### Optional: Retention layer
For service businesses with repeat customers (medical, legal, home services), add a fourth layer for after-service content (aftercare guides, maintenance, FAQ, support). It builds authority, drives return traffic, and generates reviews and referrals.

**Format:**

| Page | Stage | Content Type | Target Keyword |
|---|---|---|---|
| Rhinoplasty Services | BOFU | Service page | rhinoplasty denpasar |
| How to choose a dining table | MOFU | Buyer guide | how to choose a dining table |
| What is European oak | TOFU | Definition | what is european oak |
| Dr Smith vs Competitors | MOFU | Comparison | best rhinoplasty surgeon bali |
| Recovery Timeline | Retention | Aftercare guide | rhinoplasty recovery |

**Gap check.** If any stage has zero pages, flag it. Ask the user: "You have no [TOFU / MOFU / BOFU] stage content. Should we add pages for this stage?" The most common gap by far is MOFU. That is where most of the conversion work happens, and where most websites are weakest.

**Checkpoint 5.** Present the buyer journey mapping. Flag any gaps and propose new pages to fill them.

---

## STEP 8: QUERY EXPANSION AND COST OF RETRIEVAL

For each page, identify ALL the sub-queries Google would expand the target keyword into. Then score the page's cost of retrieval.

### How to find expanded queries

1. **Web search:** `[target keyword]`. Capture PAA questions.
2. **Think through the seven query types.** For each page's keyword, ask:
   - What is [keyword]? (Definition.)
   - How to [keyword]? (Instruction.)
   - [keyword] vs [alternative]? (Comparison.)
   - Why [keyword]? (Reason.)
   - [keyword] cost or price? (Short fact.)
   - Is [keyword] worth it? (Boolean.)
   - What happens if [keyword]? (Consequence.)
3. **Check competitor headings.** What H2s do the top 5 results use? Each H2 is a sub-query they are targeting.

### Decide. Page or section?

For each expanded query:
- If competitors have DEDICATED PAGES, it needs its own page (add to map).
- If competitors cover it as an H2 or section, cover it as an H2 on your page.
- If no competitors cover it, that is potential information gain (cover it as an H2).

### Cost of retrieval score

For each page, give it an editorial score out of 10. This is our own heuristic, not a measure of anything Google calculates: "How clearly does this page answer its target queries?"

A 10 of 10 page:
- Every heading maps to an actual search query.
- Every paragraph answers a potential question.
- Every image could rank in image search for a related query.
- The title, H1, URL, and meta description all reinforce the same keyword.
- A clear, short answer could be lifted straight out as a featured snippet.

A 1 of 10 page:
- Generic headings ("Our Services", "About").
- No clear keyword targeting.
- Content that does not answer any specific query.
- It is hard to tell what the page is about.

**Format:**

| Page | Expanded Query | Competitors: Page or Section? | Decision | CoR Score |
|---|---|---|---|---|
| Rhinoplasty Cost | how much does rhinoplasty cost in bali | 3 of 5 have dedicated page | OWN PAGE (already in map) | 8/10 |
| Rhinoplasty Cost | is rhinoplasty covered by insurance | 0 of 5 have page, 2 of 5 have H2 | H2 SECTION | n/a |
| Rhinoplasty Cost | rhinoplasty financing options | 0 of 5 cover this at all | H2 SECTION (info gain) | n/a |

**Passage ranking note.** Google can find answers DEEP in your article. A concise answer to "how long does the divorce process take" buried as a paragraph in your divorce article can rank for that specific query via passage ranking. Every paragraph should answer a potential question concisely.

**If this step generates NEW pages not already in the map, add them and re-run Steps 4 and 5 for the new pages.**

---

## STEP 9: KEYWORD SELECTION FOR PAGE TITLES

For each page in the map, select the exact target keyword using this process.

### Step 9A: Find the root word
- Go to Semrush Keyword Magic (or equivalent) and type the ROOT of the keyword.
- For "divorce", type just "divorce".
- For "car accident lawyer", type "car accident" or "car accident lawyer".
- The root word lets you see all variations and pick the right one.

### Step 9B: Pick the page title keyword
- Look at search volume for all variations.
- Pick the variation that matches your SOURCE CONTEXT.
- "Divorce application" (transactional, user intent is apply for divorce). Use if you help people apply.
- "Royal divorce" (news topic, too distant) unless you are specifically a royal family law specialist.
- "Divorce rate" could work for an AOR article with statistics.

### Step 9C: Keyword selection strategy. The mix.

You need a MIX of:

**One or two high-competition, high-volume keywords per topic folder.**
- These establish your authority on the broad topic.
- You will rank lower at first, but we think they help show Google you are in this space.
- Examples: "divorce" (4,000/mo), "child custody" (2,000/mo). (Illustrative figures. Use real volumes from a keyword tool, never estimates.)

**Several easy-to-rank, lower-volume keywords.**
- These get you actual clicks and user data quickly (Avalanche Theory).
- Look for keywords where competitors are ranking BY ACCIDENT (poor page, no SEO).
- Examples: "divorce application QLD" (200/mo, weak competition). (Illustrative.)

**The Avalanche Theory. Publishing order.** (Our working theory, not a confirmed Google mechanism.)
1. Publish easy-to-rank articles FIRST.
2. Get clicks and start building a track record on the topic.
3. We think that track record builds trust over time.
4. THEN tackle competitive keywords.
5. Our working theory: the trust earned from easy wins helps the hard keywords rank.

### Step 9D: SERP analysis per keyword

For each keyword, check the SERP:
- Are competitors ranking by accident (thin pages, no optimisation)? EASY WIN.
- Are there mostly government or authority sites? HARDER but possible with better content.
- Is the whole first page news sites? SKIP unless you are a news publisher.
- Are competitors using the SAME keyword in their title and URL? DIRECT competition, need strong content.

---

## STEP 10: DEFINE THE LINKING ARCHITECTURE

This is the cluster most websites get wrong, even when the rest of the map is solid.

### The Authority Flow Model

```
[AOR Page A] -----> [Core Page 1] <----- [AOR Page B]
     |                                         |
     v                                         v
[AOR Page C] <----------------------------     |
                                               v
                                          [Core Page 2]
```

The arrows show the main direction. Core pages link back to AOR pages wherever it helps the reader.

### Linking rules. Use these as your default.

| Link Direction | Rule | Reason |
|---|---|---|
| AOR to Core | MANDATORY. Every AOR page links to one or two relevant core pages in body content (nav or footer alone does not count). | Takes readers who are ready to act to the page that serves them, and shows which money page the supporting content backs up. |
| AOR to AOR | ENCOURAGED. Link freely between related AOR pages. | Builds topical cluster depth. |
| Core to AOR | ENCOURAGED. Link from core pages to supporting pages wherever it helps the reader (for example a service page linking to its buying guide or FAQ). | Helps readers who need more before they buy, and keeps the cluster connected both ways. |
| Homepage to Core | MANDATORY. Direct links to most important core pages. | Makes the most important pages easy to reach. Google treats pages with more internal links as more important. |
| Homepage to AOR | OPTIONAL. | Less important than homepage to core. |

### Anchor text guidance
- **Descriptive anchors.** The anchor should tell the reader what the target page is about.
- **A natural mix.** Across the links pointing at a page, a mix works well: some exact-match keyword anchors, some partial matches, some branded or natural-language variations. This is a default, not a fixed sequence, and the same exact-match anchor on every link reads as forced.
- **Never** use "click here", "read more", or naked URLs.
- **Place links** within contextual sentences where the surrounding text reinforces the target page's topic.

### Link placement
- We think body content links carry more weight than nav, sidebar, or footer links.
- Editorial links inside article copy should sit in a contextual paragraph, not a list of links dumped at the bottom. Keep useful crawlable navigation, breadcrumbs and category or related-page lists as well: Google uses links from menus to categories to products to find pages and understand the structure.
- Surrounding text matters. The paragraph around the link should use language relevant to the TARGET page.

### Client-situation-based linking

Internal links must be RELEVANT TO THE READER of the current page.
- An article about "unmarried couple separating, no kids" should NOT link to child custody.
- An article about "father's rights in custody" SHOULD link to parenting plans and visitation.
- Think: "Would the reader of THIS page actually want to read THAT page?" If no, do not link.
- Related-post widgets and automated "related posts" often link to irrelevant pages. This hurts more than it helps.

**Build the linking map:**

| Source Page | Target Page | Anchor Text | Placement | Link Type | Reader Relevance Check |
|---|---|---|---|---|---|
| Recovery Timeline (AOR) | Rhinoplasty Services (Core) | rhinoplasty in Denpasar | Supplementary section | AOR to Core | Yes. Reader is researching rhinoplasty. |
| Father's Rights (AOR) | Child Custody (Core) | child custody arrangements | Body paragraph | AOR to Core | Yes. Father wants custody info. |
| De Facto No Kids (AOR) | Child Custody (Core) | n/a | DO NOT LINK | n/a | No. Reader has no kids. |

---

End of Phase 2. Once you have the folder structure, buyer journey mapping (Checkpoint 5 confirmed), expanded queries, target keywords, and linking map, load `references/03-execution-and-output.md` and continue with Phase 3.
