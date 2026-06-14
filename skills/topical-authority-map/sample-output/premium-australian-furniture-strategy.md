# Topical Authority Map: Premium Australian Furniture

**Sample strategy document.** This is a worked example of what the Topical Authority Map skill produces when run on the seed keyword "premium Australian furniture". Brand details are illustrative. Replace with your own.

**Brand:** Atlas & Oak (illustrative). Australian-made hardwood furniture maker, premium positioning, ships nationally.

**Run date:** 2026-04-28
**Seed keyword:** premium Australian furniture
**Output paired with:** `premium-australian-furniture.xlsx`

---

## 1. Central Entity Definition

**Central entity:** premium Australian-made furniture (premium hardwood furniture, made in Australia).

**Format:** [product] + [provenance modifier].

**Why this entity, not a broader one.**
- "Furniture" alone is too broad. Google sees IKEA, Temple & Webster, Freedom on every commercial query.
- "Australian-made furniture" is the lane. It excludes 95% of competitors who import flatpack from Asia.
- "Premium" is the calibration. It excludes the local-but-cheap segment.
- The combination defines a defensible position: Australian-made, hardwood, built to last, not cheap.

### EAV (Entity-Attribute-Value) breakdown

| Attribute | Values |
|---|---|
| Materials | European oak, American oak, Tasmanian oak, blackwood, jarrah, spotted gum |
| Products | Dining tables, sideboards, bed frames, bedside tables, wardrobes, coffee tables, custom commissions |
| Construction | Mortise and tenon joinery, dovetail drawers, kiln-dried timber, hand-finished |
| Provenance | Australian-made, AFS-certified timber where used, locally sourced |
| Service tier | Off-the-shelf, custom commissions, design consultations |
| Customer language | "Solid oak dining table", "Australian-made furniture", "handmade furniture Australia", "heirloom furniture" |

---

## 2. Source Context and Persona

### Source context

| Question | Answer |
|---|---|
| Business type | Direct-to-consumer maker plus retailer (vertical: own factory, own showroom, own e-commerce) |
| Location and market | Australia, national. Showroom in Melbourne. Ships AU-wide. |
| Unique angle | Australian-made hardwood, master joinery, kiln-dried timber, 25-year structural guarantee. Most competitors at this price point are imported. |
| Customer language | "Australian-made dining tables", "solid oak", "handmade in Australia", "30-year furniture", "heirloom" |
| Knowledge Panel test | "Atlas & Oak is an Australian furniture maker producing premium hardwood dining tables, sideboards, and bedroom collections from its Melbourne workshop, with national delivery and a 25-year structural guarantee." |

### Persona

| Field | Value |
|---|---|
| Name | Marcus Hale |
| Title | Founder and Master Joiner |
| Qualifications | 22 years cabinet-making, qualified Australian joiner, AFS-certified timber sourcing |
| Memberships | Furniture Industry Association of Australia |
| Career summary | Started as an apprentice in a Tasmanian workshop in 2003. Founded Atlas & Oak in 2014 to make heirloom-grade hardwood furniture in Australia at a price that beats imported veneer alternatives over a 30-year horizon. |

This persona signs all educational content (AOR articles) where appropriate. It is what makes "how to identify quality joinery" credible: the writer is an actual joiner.

---

## 3. Knowledge Graph Summary

Key entities in the cluster, with topic distance:

**Close (own pages):**
- Dining tables, sideboards, bedside tables, bed frames, wardrobes, coffee tables (each is a Core attribute).
- European oak, American oak, Tasmanian oak (timber types).
- Dining table sizing, dining table heights, dining table shapes (sub-attributes).

**Medium (own pages, lighter coverage):**
- Joinery types (mortise and tenon, dovetail).
- Kiln-drying.
- Timber moisture content.
- Janka hardness.
- Australian Made certification.

**Far (paragraphs, not pages):**
- Forestry. Sustainability. AFS certification (one paragraph in "AFS-certified timber" article).
- Cabinet-making history. Australian craft heritage.
- Interior design styles (covered selectively where they connect to product).

**Too far (skip):**
- Outdoor furniture. Office chairs. Lighting. Soft furnishings (rugs, cushions).
- These would dilute the topical focus.

---

## 4. Folder Structure

```
/                                   (homepage)
/dining-tables/                     (Core hub)
  /solid-oak-dining-tables/         (Core)
  /european-oak-dining-tables/      (Core)
  /american-oak-dining-tables/      (Core)
  /extending-dining-tables/         (Core)
  /round-dining-tables/             (Core)
/sideboards/                        (Core hub)
  /buffet-sideboards/               (Core)
/bedroom/                           (Core hub)
  /bed-frames/                      (Core)
  /bedside-tables/                  (Core)
  /wardrobes/                       (Core)
/coffee-tables/                     (Core)
/office/                            (Core)
/custom/                            (Core, bespoke commissions hub)
/guides/
  /buying/                          (AOR sub-topic A: dining table buying and sizing)
  /timber/                          (AOR sub-topic B: timber types and quality)
  /australian-made/                 (AOR sub-topic C: provenance and Australian-made)
  /care/                            (AOR sub-topic D: care and maintenance)
  /styling/                         (AOR sub-topic E: interior design and styling)
  /investment/                      (AOR sub-topic F: investment and long-term value)
```

**Why this structure:**
- Five Core hubs (dining tables, sideboards, bedroom, coffee tables, custom) so Google sees the product taxonomy.
- All AOR content lives under `/guides/[sub-topic]/` so the URL signals "supporting content" not "buying intent".
- `/dining-tables/` is the deepest folder because it is the highest-revenue product category. Every AOR article on dining tables routes back here.

---

## 5. Central Entity Template (sitewide presence)

Apply on every page.

**Header:** "Atlas & Oak. Premium Australian-made hardwood furniture."

**Footer (every page):** "Atlas & Oak makes premium hardwood dining tables, sideboards, bed frames, and custom furniture in our Melbourne workshop. Every piece is built from kiln-dried Australian and European oak, hand-jointed, and backed by a 25-year structural guarantee."

**Intro paragraph (every page):** ONE natural mention of "Australian-made hardwood furniture" or the relevant sub-entity for that page.

**Supplementary section (every page, above footer):** ONE CTA mention of the central entity. Example on an AOR page: "If you are looking for an Australian-made dining table built to last 30+ years, our solid oak collection is hand-built in Melbourne and shipped nationally."

**One internal link** from every page back to the most relevant Core page.

---

## 6. NLP Category Target

Target: `/Home and Garden/Home Furnishings/Furniture` for every page.

**Drift risks:**
- "Modern Australian interior design" articles can drift toward `/Arts and Entertainment/Visual Art and Design`. Anchor with at least two product mentions and one internal link to a Core page.
- "Sustainable timber" articles can drift toward `/Science/Ecology`. Anchor with timber-as-material framing, not forestry-as-environmental-cause framing.
- "Australian craft heritage" articles can drift toward `/Reference/Humanities/History`. Keep the angle on cabinet-making craft, not on cultural history broadly.

---

## 7. Linking Rules Summary

| Direction | Rule | Notes |
|---|---|---|
| AOR to Core | MANDATORY in body content | Every AOR article links to one or two Core pages with exact-match or partial-match anchor. |
| AOR to AOR | ENCOURAGED | Helps cluster depth. |
| Core to AOR | RARE | Core pages link out only to a "buying guide" or "care guide" sidebar at most. |
| Homepage to Core | ALL FIVE HUBS | Direct from homepage nav and hero. |
| Homepage to AOR | NONE | Homepage stays commercial. |

**Anchor text mix per Core page:**
- First incoming link: exact match (e.g. "Australian-made dining tables").
- Second incoming link: partial match (e.g. "our dining table collection").
- Third incoming link: branded (e.g. "Atlas & Oak dining tables").

**Reader-relevance check:** every link is paired with a sentence that would make sense to the reader of the source page. No "related products" widgets. No automated "you might also like" sidebars.

See the Linking Map tab for every internal link in full.

---

## 8. Buyer Journey Gaps

Three-stage tagging applied across all 85 pages.

| Stage | Page count | Notes |
|---|---|---|
| TOFU | 50 articles | Strongest cluster. Sub-topics A, B, C, D, E mostly TOFU. |
| MOFU | 20 articles | Lighter than ideal. The map adds 12 buyer guides ("how to choose", "X vs Y") to fill this. |
| BOFU | 15 pages | The Core money pages. |

**Key gap:** MOFU is the conversion layer and the original audit (250 existing posts) had only six MOFU articles. The new map shifts 20% of new content into MOFU buyer guides specifically.

**Retention layer (optional 4th tier):** 5 care-and-maintenance articles. Tagged Retention. Drive return traffic and reviews.

---

## 9. Information Gain Opportunities

Queries no major competitor covers in depth. These are where Atlas & Oak can create unique authority:

1. "European oak vs American oak vs Tasmanian oak" three-way comparison (most competitors do European vs American only).
2. "Total cost of ownership: solid timber vs MDF over 10 years" with real maintenance costs and resale data.
3. "Pendant light heights over a dining table" interior-design crossover that connects to dining table sizing.
4. "How to value used solid timber furniture" (resale market, no major Australian retailer covers this).
5. "Why solid wood furniture moves and what to do" honest content about timber expansion and contraction. Most retailers avoid this.
6. "AFS-certified timber: what it is and why it matters" niche but defensible authority on Australian timber sourcing.
7. "Counter-height vs standard dining tables" Australian-context article (most existing content is US-focused).
8. "Australian style: defining the look" interior design crossover with first-party photography of Atlas & Oak products in real Australian homes.

---

## 10. Content Priorities (Avalanche Theory)

**Phase 0. Foundation (already in place):**
- Homepage live with new central entity template applied.
- Five Core hub pages live (dining tables, sideboards, bedroom, coffee tables, custom).
- About page rewritten around Marcus Hale and the workshop.
- Contact page.

**Phase 1. AOR Wave (weeks 1 to 6, 30 articles):**
- Five articles per week.
- Sub-topic mix: 8 from buying/sizing, 8 from timber, 4 from Australian-made, 4 from care, 3 from styling, 3 from investment.
- Each article links to one or two relevant Core pages in the body.

**Phase 2. MOFU Wave (weeks 7 to 10, 40 articles):**
- 10 articles per week.
- Heavy buyer-guide angle ("how to choose", "X vs Y").
- Includes 12 NEW MOFU pieces specifically built to fill the conversion-layer gap.
- Plus the remaining 28 AOR articles from the cluster.

**Phase 3. Core Optimisation (weeks 11 to 12, 20 articles):**
- All 15 Core pages get rewritten using the central entity template.
- Five new BOFU sub-pages launched (e.g. "extending oak dining tables Melbourne", "round Tasmanian oak dining tables").
- Internal linking sweep: confirm every Phase 1 and Phase 2 article links into the right Core page.

By week 12, Google has six weeks of authority signals routed in from 30+ articles, four weeks of MOFU buyer guides feeding warm traffic into the comparison decision, and only then do the Core pages get optimised. The compounding effect lands on the Core pages.

See the Publishing Order tab for the exact 90-row sequence.

---

## 11. Off-Site Topical Authority Plan

The on-site map handles the topical structure. Off-site amplifies it.

**Branded search:**
- Run YouTube content under "Atlas & Oak workshop tour" / "how we make a dining table" series. Branded SERPs reinforce the entity.
- Push customers toward Google reviews mentioning "Australian-made", "solid oak", "joinery".

**Link building targets:**
- Australian interior design blogs (Est Living, The Local Project, Habitus Living): pitch case studies of Atlas & Oak pieces in real Australian homes.
- Australian Made certification body (australianmade.com.au): get listed in the official directory.
- Sustainability publications (Domain Sustainability, Houses Magazine): pitch articles on AFS-certified timber sourcing.

**Media opportunities:**
- Trade press: Furniture Industry Association of Australia bulletin.
- Mainstream design press: Belle, Vogue Living, Inside Out (high-end Australian interior magazines).

---

## 12. Buyer Journey Gaps (Recommended Pages to Add)

If the audit shows gaps, the skill adds them automatically. For Atlas & Oak the recommended additions are:

| Stage | Page Title | Why |
|---|---|---|
| MOFU | How to choose a dining table for an open plan home | Top buyer search, currently uncovered. |
| MOFU | Solid oak vs Tasmanian oak: which is right for your home | High-volume comparison query, no competitor owns it. |
| MOFU | Custom commissions: what to expect and how it works | Educates the bespoke buyer who is the highest-margin customer. |
| MOFU | Total cost of ownership: solid timber vs MDF over 10 years | Information gain piece, anchors the premium pricing. |
| MOFU | Australian-made vs imported: how to tell the difference | Defensible MOFU piece, only Atlas & Oak can speak credibly to this. |
| BOFU | Round Tasmanian oak dining tables | Sub-attribute Core page, search volume justifies its own page. |
| BOFU | Extending oak dining tables Melbourne | Local + product modifier, easy ranking win. |

---

## 13. Quality Standards

Every article in this map must meet:

1. **Length matches intent.** Buyer guides 2,000+ words. Definitions 600 to 1,000 words. Comparisons 1,500+ words. Care guides 800 to 1,200 words.
2. **First-party photography.** Every product mention has a real Atlas & Oak photo. No stock images of generic furniture.
3. **Persona attribution.** AOR articles signed by Marcus Hale or a named workshop joiner.
4. **One central entity mention** in intro paragraph plus one in supplementary section plus one internal link to a Core page. No more, no less.
5. **No keyword stuffing.** Natural language, customer phrasing.
6. **No AI-generated padding.** Concrete details, real measurements, real timber characteristics. If the writer cannot speak with authority, the persona is wrong for that topic.

A topical map filled with low-quality articles will hurt Atlas & Oak. The map is permission to publish with strategy, not permission to publish more.

---

## 14. Dynamic Updates

Review this map quarterly. Specifically check:

1. Has Google merged any of the "X vs Y" comparison queries into a single intent? (If yes, consolidate the two pages.)
2. Are any AOR articles outranking the Core page they link into? (If yes, the Core page needs more depth or the AOR is over-optimised.)
3. Is the MOFU layer producing conversions? (Check assisted conversion data in GA4.)
4. Are there new sub-attributes appearing in PAA that the map does not cover? (Add them as new pages or H2 sections.)

The map is a living document. Google's view of the topic shifts. The map shifts with it.

---

End of strategy document. Pair with `premium-australian-furniture.xlsx` for the full 5-tab spreadsheet.
