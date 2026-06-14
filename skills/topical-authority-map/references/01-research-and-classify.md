# Phase 1: Research and Classification

This phase produces the foundation. You define the central entity, set source context and persona, do deep research on the topic and the Knowledge Graph, then classify every attribute as Core or AOR with depth calibration.

There are three checkpoints in this phase. Pause at each one and confirm with the user before proceeding.

---

## STEP 1: DEFINE THE CENTRAL ENTITY

Take the user's seed keyword and define the central entity.

**The central entity is the ONE thing the site is about, expressed as a keyword.**

Ask yourself: "If Google gave this site a Knowledge Panel, what would the title be?"

**Format:** `[service or product] + [location or modifier]` where applicable.
- "family lawyer Sydney"
- "rhinoplasty Denpasar"
- "SEO agency Melbourne"
- "premium Australian furniture"
- "online casino" (no location for digital-only)

**Entity-Attribute-Value (EAV) thinking.** The entity has attributes (things Google knows about it) and values (specific data points). Your topical map must cover all the important attributes.

Example. Entity: Michael Jordan
- Attribute: height. Value: 1.98m
- Attribute: team. Value: Chicago Bulls
- Attribute: spouse. Value: Yvette Prieto
- Each of these is a separate entity in Google's system

Example. Entity: Family Lawyer Sydney
- Attribute: services. Values: divorce, custody, property settlement
- Attribute: jurisdiction. Value: NSW, Family Law Act 1975
- Attribute: qualifications. Value: Law Society accredited specialist

**Checkpoint 1.** Confirm with the user:
- "Is [central entity] correct as your main entity?"
- "Is there a location component?"
- "Any modifier I should add (for example 'affordable', 'specialist', 'emergency', 'premium')?"

Wait for the user to confirm before continuing.

---

## STEP 2: SOURCE CONTEXT AND PERSONA

Before picking any topics, define WHAT the site is and WHO is behind it. Both change the entire map.

### 2A: Source Context

Ask the user these five questions:

1. **Business type.** Service provider, retailer, manufacturer, affiliate, media, SaaS, marketplace, or other?
2. **Location and market.** Local (single city), regional, national, or international? Note the state or jurisdiction. Laws and regulations may be state-specific.
3. **Unique angle.** What makes this business different from competitors? (Cheapest, fastest, most experienced, only one doing X, etc.)
4. **Customer language.** How do customers describe this business? (Not how the business describes itself.)
5. **Knowledge Panel test.** If Google created a Knowledge Panel for this business, what would the two-sentence description say?

**Why source context matters.**
- A casino AFFILIATE needs comparison content, bonus pages, review pages.
- A casino OPERATOR needs game pages, responsible gambling, licensing pages.
- A casino TECH PROVIDER needs integration docs, API pages, case studies.
- Same niche, completely different maps.
- Source context determines which attributes matter most and how content is framed.

### 2B: Create a Persona

Google expects expert writers on topics. Your topical map must reflect a credible persona.

**Research process.**
1. Look at competitor About pages. What qualifications, job titles, and credentials do they list?
2. Create a persona with: name, job title, qualifications, professional memberships, career summary.
3. This persona determines what topics you can credibly cover.

**Example. Family Law.**
- Name: John Bale
- Title: Senior Associate, Family Law
- Qualifications: Law Society accredited specialist, qualified mediator
- Memberships: Law Society of New South Wales

**Why this matters.** If your topical map calls for an article on "battery chemistry" but your site sells electric scooters, you do not need 100 articles on chemistry. You need one or two to show Google you have knowledge of that adjacent topic. The persona keeps you grounded in what is credible.

**Checkpoint 2.** Confirm source context and persona with the user before proceeding.

---

## STEP 3: DEEP RESEARCH ON THE TOPIC

You cannot build a good topical map without deeply understanding the topic first. Keyword research alone is not enough. You need to understand the relationships between entities.

### 3A: Knowledge Graph Research

Use these tools to map the entity's Knowledge Graph neighbourhood:

1. **Wikipedia.** Search for the entity type. Section headings are attributes. Related articles are adjacent entities. "See also" is closely related topics.
2. **Wikipedia Graph visualiser** (blinpete.github.io/wiki-graph). Visualise connected topics. Note DISTANCE. Topics close together are strongly related, distant ones are weakly related.
3. **Wikidata.** Structured entity data with explicit relationships.
4. **DBpedia** (dbpedia.org). Knowledge base derived from Wikipedia.

**Key concept: topic distance in vector space.**

Google thinks about topics like GPS coordinates. Topics close together can be connected naturally. Topics far apart cannot.

- Car accidents and car maintenance are CLOSE (a sentence connecting them makes sense: "poor car maintenance has led to the car accident").
- Car accidents and racing helmets are TOO FAR (even though "car" appears in both).
- Drinking water and luxury water are CLOSE.
- Drinking water and fecal coliform are FAR (probably do not need a whole page on it for a water brand).

**Your job.** Decide which connected topics are close enough to your central entity to warrant coverage, and how much coverage (own page vs paragraph vs skip entirely).

**Node importance. How to judge what deserves more coverage.**
- **Degree.** How many connections does this topic have? More connections, more important, more coverage.
- **Eigenvalue.** Is it connected to OTHER important nodes? (Scottie Pippen matters more than Jordan's dad because Pippen is independently significant.)
- **Betweenness.** Must you pass through this topic to reach other topics? (To talk about water and human health, you must go through drinking water.)
- **Closeness.** How close is it to other important topics in your niche?

The size of a topic on your website should roughly match its importance in the Knowledge Graph.

### 3B: Competitor Research

1. **Extract competitor sitemaps.** Find three to five competitors and grab their sitemaps and site structures.
2. **Analyse their folder structures.** What topics do they cover? What is their hierarchy?
3. **Note gaps.** What topics are they missing? (These are your information gain opportunities.)
4. **Note thin content.** Competitors with 50-word pages on important topics are easy to beat.
5. **Research their About pages.** What personas and credentials do they use?

### 3C: Client and Customer Situation Mapping

For service businesses, map out the specific SITUATIONS your clients find themselves in. This is critical because:
- Each situation creates a unique content angle.
- Each situation determines which internal links make sense.
- You do not link to child custody content from an article about unmarried couples with no kids.

**Example. Family Law.**

| Persona | Situation | Services Needed | Related Topics |
|---|---|---|---|
| Father | Wants full custody of son | Child custody, parenting plans | Visitation rights, father's rights |
| Mother | Separating, cannot support herself | Spousal maintenance, property settlement | Financial agreements, Centrelink |
| Grandparent | Wants to see grandchildren | Visitation hours, grandparent rights | Custody arrangements |
| Unmarried couple | De facto relationship ending, no kids | Property settlement, de facto law | Section 4AA Family Law Act |
| Married couple | Divorcing with significant assets | Divorce, property settlement | Consent orders, binding financial agreements |

Each situation drives content creation AND internal linking decisions.

### 3D: Find Every Attribute of the Entity

Research ALL attributes using these sources. Do them all. No shortcuts.

#### Source 1: Top 5 Google Results
- Web search: `[central entity]`
- Open the top 5 organic results.
- List every SERVICE, FEATURE, PRODUCT, or SUB-TOPIC mentioned on each page.
- Note which attributes appear on three or more of the five pages. Those are mandatory.

#### Source 2: People Also Ask
- Web search: `[central entity]`
- Capture every PAA question visible.
- Each PAA reveals an attribute users care about.
- Click into two or three PAAs to reveal nested PAAs and capture those too.

#### Source 3: Wikipedia
- Section headings on the Wikipedia page are entity attributes.
- Related articles linked from the Wikipedia page are adjacent entities (potential AOR topics).
- The "See also" section is closely related topics.
- For law, finance, medical, or other regulated industries, note the specific legislation (for example Family Law Act 1975 for Australian family law).

#### Source 4: Keyword Tools and Google Autocomplete
- Web search: `[central entity] a`, `[central entity] b`, `[central entity] c`, through the alphabet.
- Each autocomplete suggestion is a potential attribute.
- Also search: `[central entity] for`, `[central entity] vs`, `[central entity] how`, `[central entity] cost`, `[central entity] best`.
- Group results by intent type (informational, commercial, navigational).

#### Source 5: Business Service or Product List
- Ask the user: "List every service, product, or offering this business provides."
- Each one is a mandatory core attribute regardless of search volume.

#### Source 6: Relevant Laws, Regulations, Standards
- For regulated industries, identify the specific legislation, regulations, or industry standards.
- These MUST be part of your topical map. You cannot discuss the topic without referencing them.
- Example: Family Law Act 1975, Section 4AA (de facto relationships), Part VII (children).

**Compile the master attribute list.** Format:

| # | Attribute | Source(s) Found | Intent Type | KG Distance | Notes |
|---|---|---|---|---|---|
| 1 | Cost or pricing | Google results, PAA, autocomplete | Commercial | Close | All 5 competitors have this |
| 2 | Recovery timeline | Wikipedia, PAA | Informational | Close | Strong AOR candidate |
| 3 | Battery chemistry | Wikipedia (adjacent) | Informational | Medium-far | 1-2 articles max, not core topic |

**Checkpoint 3.** Present the full attribute list AND client situation map to the user. Ask: "Are there any attributes missing? Any services I have not captured? Any client situations I am missing?"

---

## STEP 4: CLASSIFY EACH ATTRIBUTE AS CORE OR AOR

Split every attribute into one of two buckets.

### Core Pages (the money pages)
- Commercial or transactional intent.
- Pages that convert visitors into customers or leads.
- Service pages, product pages, pricing pages, booking pages, landing pages.
- Keywords contain: "buy", "hire", "cost", "near me", "best", "[service] + [location]", "[product] review".

### AOR Pages (Areas of Relevance)
- Informational intent.
- Pages that build authority and funnel it to core.
- Guides, how-tos, explainers, listicles, comparisons, history, tips.
- Keywords contain: "how to", "what is", "guide to", "tips for", "history of", "vs", "types of", "examples of".

For each attribute, tag it:

| Attribute | Classification | Reasoning |
|---|---|---|
| Rhinoplasty cost | CORE | Commercial intent, users are price-shopping |
| Recovery timeline | AOR | Informational, supports the core pages |
| Before and after | AOR | Educational, but could be CORE if it has a gallery and CTA |

---

## STEP 5: MERGE AND SPLIT DECISIONS PLUS DEPTH CALIBRATION

For each attribute, decide if it gets its own page or merges into another page. Then calibrate the DEPTH of coverage.

### The exact thresholds

| Search Volume (monthly) | Decision | Condition |
|---|---|---|
| 100+ | **Own page** | Enough demand to justify a dedicated page |
| 10 to 99 | **Check competitors** | If 2+ competitors have dedicated pages, own page. If none do, merge |
| Under 10 | **Merge** | Add as a section or paragraph on a related page |
| Any volume | **Own page (override)** | If it is a core service you actively sell, own page regardless |

### How to check competitor pages
- Web search: `[attribute] + [location or modifier]`
- Check if the top 5 results have DEDICATED pages for this attribute.
- A dedicated page means the URL slug contains the attribute AND the page is 500+ words specifically about it.
- A mention on a broader page does NOT count as a dedicated page.

### Depth calibration. How much coverage?

The page vs paragraph vs sentence decision:

If you cover something as a WHOLE PAGE (it becomes the title), you are signalling to Google this is a very important topic directly connected to your central entity.

If you cover it as a PARAGRAPH within a page, you are signalling it is related but secondary.

If you cover it as a SENTENCE, it is tangentially relevant.

**Match depth to Knowledge Graph importance.**
- High-degree node (many connections, high search volume): own page or multiple pages.
- Medium node: own page with moderate depth.
- Low node (few connections, but still relevant): paragraph within a related page.
- Very distant node: one sentence or skip entirely.

**Example. Electric Scooter Site.**
- Battery life: OWN PAGE (core attribute, high search volume).
- Battery chemistry: 1-2 ARTICLES (adjacent topic, proves knowledge, but do not write 100 articles).
- Lithium mining: ONE PARAGRAPH in battery chemistry page (too distant).

**Example. Dental Implants.**
- Dental implants: CORE (hub page).
- Bone grafting: OWN PAGE (important sub-topic).
- Bone grafting materials: OWN PAGE (deeper depth, if competitors cover it).
- Human bone vs animal bone: SECTION within bone grafting materials (too narrow for own page).

**Format the decisions:**

| Attribute | Volume | Competitors w/ Page | KG Importance | Decision | If Merge, Into Which Page | Depth |
|---|---|---|---|---|---|---|
| Child custody | 320/mo | 4 of 5 | High | OWN PAGE | n/a | Full depth |
| Relocation disputes | 10/mo | 0 of 5 | Low | MERGE | Child custody page | H2 section |
| Battery chemistry | 20/mo | 0 of 5 | Medium | OWN PAGE | n/a | 1-2 articles only |

**Checkpoint 4.** Present merge and split decisions to the user. Ask: "Do these split and merge decisions look right? Any pages you definitely want separate regardless of volume?"

---

End of Phase 1. Once Checkpoint 4 is confirmed, load `references/02-architecture-and-keywords.md` and continue with Phase 2.
