# Claude SEO Skills

> 32 free Claude Skills for SEO and AI search. Built by [Hawk Academy](https://hawkacademy.co) and the [StudioHawk](https://studiohawk.com.au) senior team. Drop into Claude Desktop and run.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-32-orange.svg)](#the-32-skills)
[![Hawk Academy](https://img.shields.io/badge/free-Hawk%20Academy-7C3AED.svg)](https://hawkacademy.co/claude-seo-skills)

These are the [Claude](https://www.anthropic.com/claude) Skills [StudioHawk](https://studiohawk.com.au) uses across 500+ live client SEO campaigns. We open-sourced them through [Hawk Academy](https://hawkacademy.co) so any SEO, founder, or in-house marketer can run agency-grade audits and briefs straight inside Claude Desktop, free.

Every skill has a matching landing page at [hawkacademy.co/claude-seo-skills](https://hawkacademy.co/claude-seo-skills) with worked examples, sample output, and the StudioHawk thinking behind it.

### Watch first: "Don't Use Claude for SEO Until You Watch This"

[![Don't Use Claude for SEO Until You Watch This](https://img.youtube.com/vi/S18roQFhxUQ/maxresdefault.jpg)](https://www.youtube.com/watch?v=S18roQFhxUQ)

A short walkthrough of how StudioHawk actually uses these Claude Skills on live client SEO work. Click the thumbnail to play on YouTube.

---

## Why we built this

Most SEO tools are either expensive SaaS subscriptions or one-off paid prompts. Neither is how StudioHawk's own SEO specialists actually work day to day. We run Claude Skills, drop in our own crawl data, and let Claude do the audit, the brief, or the report.

These 32 skills are the exact set our team uses on live client work. Now they live in your Claude Desktop too.

**Free, MIT-licensed, no upsell.** You will not find a paywall, an email gate, or a "premium tier" in this repo. [Hawk Academy](https://hawkacademy.co) is funded by StudioHawk's agency business. The skills are the giveaway.

---

## Who this is for

- **In-house SEOs** who want StudioHawk-grade audit and briefing skills without the StudioHawk retainer
- **Freelance SEO consultants** who want a faster audit + briefing workflow than running Screaming Frog by hand
- **Founders and marketers** who do not have an SEO team but need to ship audits, content briefs, and reports
- **Agency teams** evaluating which Claude Skills are worth standardising across their workflow

If you have ever spent three hours building a content brief in Google Docs or four hours writing up a technical SEO audit, these skills delete most of that.

---

## What people say about the underlying training

These skills sit underneath the free [Hawk Academy](https://hawkacademy.co) course. The training the course teaches is what the skills automate.

> "Hands down one of the most comprehensive SEO Courses I've encountered. A huge time saver."
>
> — **Daniel Gladki**, eCommerce Director, Uniqlo

> "I thought I already knew SEO, having done it for 5 years, but the technical SEO and link-building stuff is incredible."
>
> — **Harvey**, Terrain Tamer

> "We enrolled our entire team. The quizzes and real-world examples make it so much easier to actually retain and apply the knowledge."
>
> — **Will Rosindell**, Medicart

More reviews on [hawkacademy.co](https://hawkacademy.co). Over 6,000 students are enrolled in the free course these skills come from.

---

## Install (90 seconds)

Drop into Claude Desktop's skills folder. No build step, no API keys, no dependencies.

### macOS / Linux

```bash
git clone https://github.com/lhitches/claude-seo-skills.git
mkdir -p ~/.claude/skills/
cp claude-seo-skills/skills/*.md ~/.claude/skills/
cp -r claude-seo-skills/skills/topical-authority-map ~/.claude/skills/
```

Restart Claude Desktop. The skills appear in your Skills picker.

### Windows (PowerShell)

```powershell
git clone https://github.com/lhitches/claude-seo-skills.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item claude-seo-skills\skills\*.md "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse claude-seo-skills\skills\topical-authority-map "$env:USERPROFILE\.claude\skills\"
```

Restart Claude Desktop.

### Or grab individual skills

If you only want one or two skills, every landing page on [hawkacademy.co/claude-seo-skills](https://hawkacademy.co/claude-seo-skills) has a one-line `curl` command to install that skill alone. Faster than cloning the whole repo.

---

## The 32 skills

Grouped by job. Every link goes to the Hawk Academy landing page with worked examples, sample output, and the install snippet.

### Audit and diagnose

| Skill | What it does |
|---|---|
| [Technical SEO Audit](https://hawkacademy.co/claude-seo-skills/technical-seo-audit) | Finds the technical issues stopping Google from reading your site. Redirect chains, duplicate titles, indexing problems, orphan pages, cannibalisation. |
| [Website Score](https://hawkacademy.co/claude-seo-skills/website-score) | Free SEO score for any URL via Claude. The opening move on every StudioHawk audit. |
| [Striking Distance Finder](https://hawkacademy.co/claude-seo-skills/striking-distance-finder) | Surfaces the pages you rank positions 8 to 20 for. Small CTR or content gains push them onto page one. |
| [GSC Quick Start](https://hawkacademy.co/claude-seo-skills/gsc-quick-start) | Pulls your Google Search Console data and ranks the highest-leverage pages to fix first. |
| [Screaming Frog Analyser](https://hawkacademy.co/claude-seo-skills/screaming-frog-analyser) | Drop your Screaming Frog export, get a StudioHawk-style audit back. |
| [Google Trust Check](https://hawkacademy.co/claude-seo-skills/google-trust) | Scores any page on the trust signals Google actually weights. Author entity, E-E-A-T, brand authority. |
| [Cannibalization Detector](https://hawkacademy.co/claude-seo-skills/cannibalization-detector) | Finds the queries where two of your own pages compete and split the signal. Picks the keeper and gives one fix: consolidate, canonical, or differentiate. |
| [Schema Markup Generator](https://github.com/lhitches/claude-seo-skills/blob/main/skills/schema-generator.md) | Generates and validates clean JSON-LD for any page type, with required vs recommended properties and a rich-result test checklist. |

### Industry-specific audits

| Skill | What it does |
|---|---|
| [Ecommerce SEO Audit](https://hawkacademy.co/claude-seo-skills/ecommerce-seo-audit) | Product, collection, and category-page audit. The issues StudioHawk fixes on every ecommerce client. |
| [Agentic Product Page Auditor](https://hawkacademy.co/claude-seo-skills/agentic-product-page-auditor) | Audits whether an AI shopping agent can read and buy from your product page. Scores the product graph across six layers and gives one template-level fix per problem, ranked by what blocks a sale. |
| [B2B SEO Audit](https://hawkacademy.co/claude-seo-skills/b2b-seo-audit) | Long sales cycles, decision committees, and the content that actually converts the buyer. |
| [SaaS SEO Audit](https://hawkacademy.co/claude-seo-skills/saas-seo-audit) | Feature pages, comparison pages, free tools, and product-led growth content that compounds. |
| [Local SEO Audit](https://hawkacademy.co/claude-seo-skills/local-seo-audit) | GBP, NAP citations, local landing pages, and review strategy in one skill. |
| [Restaurant SEO Audit](https://hawkacademy.co/claude-seo-skills/restaurant-seo-audit) | Hospitality-specific. Menu schema, opening hours, reservations, and the local intent that drives bookings. |

### Content and topical strategy

| Skill | What it does |
|---|---|
| [Content Brief Draft](https://hawkacademy.co/claude-seo-skills/content-brief-draft) | Generates a content brief any writer can ship from. Audience, angle, structure, internal linking, distribution. |
| [Information Gain](https://hawkacademy.co/claude-seo-skills/information-gain) | Finds the unique angle competitors are missing on a query. Use before you write. |
| [Title Tag Optimizer](https://hawkacademy.co/claude-seo-skills/title-tag-optimizer) | The title-tag rewrite skill. Tested against Google's CTR signals StudioHawk monitors. |
| [Topical Authority Map](https://hawkacademy.co/claude-seo-skills/topical-authority-map) | Builds the cluster architecture for an entire topic from a single seed keyword. |
| [Keyword Clustering](https://github.com/lhitches/claude-seo-skills/blob/main/skills/keyword-clustering.md) | Groups a raw keyword list into page-level clusters by search intent, with target pages and cannibalisation flags. |
| [Website Gap](https://hawkacademy.co/claude-seo-skills/website-gap) | Compares your site to a competitor and tells you the keywords, topics, and pages they cover that you do not. |
| [Competitor Gap](https://hawkacademy.co/claude-seo-skills/competitor-gap) | Inverse of website-gap. Identifies the topics you cover that competitors miss, so you can defend them. |
| [3 Ranking Laws Cheat Sheet](https://hawkacademy.co/claude-seo-skills/3-ranking-laws-cheat-sheet) | Every Google patent and the 2024 API leak distilled into 3 laws. Audits your site against NavBoost, siteFocusScore, and information gain. |

### AI search

| Skill | What it does |
|---|---|
| [AI Visibility](https://hawkacademy.co/claude-seo-skills/ai-visibility) | Scores any page on the on-page factors most likely to win an AI citation. Run it before you publish. |
| [AI Citation Monitor](https://hawkacademy.co/claude-seo-skills/ai-citation-monitor) | Tracks whether ChatGPT, Claude, and Perplexity cite your site for the queries that matter. |
| [Claude Code SEO](https://hawkacademy.co/claude-seo-skills/claude-code-seo) | Plug Claude Code into your SEO workflow for code-level fixes, schema injection, and automated audits. |
| [Clarity AI Bot Auditor](https://hawkacademy.co/claude-seo-skills/clarity-ai-bot-auditor) | Paste your Microsoft Clarity AI bot data. Diagnoses every AI bot as healthy, blocked, throttled, or over-scraping, with one decisive fix per bot. |
| [Citation Share Auditor](https://hawkacademy.co/claude-seo-skills/citation-share-auditor) | Reads your Bing Citation Share data and shows your slice of AI answers, the topics and intents you own, and where to grow it. |

### Outreach, links, and reviews

| Skill | What it does |
|---|---|
| [Data PR Outreach](https://hawkacademy.co/claude-seo-skills/data-pr-outreach) | The pitch process StudioHawk uses for Digital PR campaigns at scale. |
| [Google Review Handler](https://hawkacademy.co/claude-seo-skills/google-review-handler) | Drafts review responses that protect rank without sounding canned. |

### Calculators and helpers

| Skill | What it does |
|---|---|
| [Ad Spend Calculator](https://hawkacademy.co/claude-seo-skills/ad-spend-calculator) | What your Google Ads spend would have bought as SEO investment. The conversation that closes SEO deals. |
| [Calculator Page Builder](https://hawkacademy.co/claude-seo-skills/calculator-page-builder) | Builds the spec for a free calculator page on your site (a backlink magnet). |
| [GBP Analytics Connector](https://hawkacademy.co/claude-seo-skills/gbp-analytics-connector) | Pulls Google Business Profile insights into the StudioHawk local-SEO reporting format. |
| [Winner or Loser](https://hawkacademy.co/claude-seo-skills/winner-or-loser) | Did the latest Google update boost or hurt you? Quick diagnostic on any GSC export. |

---

## About the makers

These skills are built and maintained by the StudioHawk senior team, distributed free through Hawk Academy.

- **[Harry Sanders](https://hawkacademy.co/about/harry-sanders)** is the founder of [StudioHawk](https://studiohawk.com.au), Australia's largest dedicated SEO agency, and Hawk Academy. Forbes 30 Under 30. 1,000-plus SEO campaigns delivered with zero algorithmic penalisations. AWIA Board Member.
- **[Lawrence Hitches](https://hawkacademy.co/about/lawrence-hitches)** is Chief of Staff at StudioHawk and an AI SEO consultant based in Melbourne. Young Search Professional of the Year (Semrush 2021). Speaker at SEO conferences across Asia-Pacific.

The skills reflect how a 120-person SEO agency actually runs audits, briefs, and reports. They are not generic prompts.

### StudioHawk has been recognised by

US Search Awards · UK Search Awards · APAC Search Awards (4× Best Large SEO Agency) · Global Search Awards · SEMrush Search Awards · Global Digital Excellence Awards · Global Marketing Awards · Global Agency Awards · The Drum Awards · Marketing Innovation Awards · Mumbrella

### StudioHawk clients (a sample)

Nike · New Balance · Fujifilm · Officeworks · Kao · Weber · Bondi Sands · Intuit QuickBooks · Kogan · The Good Guys · Ryobi · Moonpig · Employment Hero · PETstock · Samsung

---

## Use cases

- **Junior SEO standardisation.** Drop the audit skills onto a junior's machine, get StudioHawk-grade output on day one
- **Agency QA.** Run every client audit through the same Claude skill so reports are consistent across consultants
- **Freelancer leverage.** A solo SEO consultant can punch above their weight using the same workflow we run at 120-person scale
- **Founder DIY.** Founder-led SEO that does not require hiring an in-house SEO until the business is much bigger
- **In-house team scale-up.** A two-person in-house SEO team can match the output of a much larger team

---

## The full Hawk Academy roadmap

These skills sit inside a larger 10-step SEO roadmap. If you want to know where each skill fits in a complete SEO programme, see:

**[The Hawk Academy SEO Roadmap](https://hawkacademy.co/resources/seo-roadmap)** — 10 steps from SEO fundamentals to AI search, with every step linked to a free Hawk Academy resource plus the specific course module that teaches it inside the free Hawk Academy course.

If you want the structured course version of the same material with video walkthroughs and quizzes, [enrol free at learn.hawkacademy.co/register](https://learn.hawkacademy.co/register).

---

## Contributing

Found a bug, want to improve a skill, or have an idea for a new one? Open an issue or a pull request. We read every one.

If you ship something interesting on top of these skills, we want to know. Tag [@studiohawkseo](https://www.instagram.com/studiohawkseo/) on Instagram or mention [@StudioHawk](https://www.linkedin.com/company/studiohawk/) on LinkedIn.

---

## License

MIT. See [LICENSE](LICENSE).

You can use these skills in client work, in commercial products, in agency engagements, in courses. Attribution back to Hawk Academy is appreciated but not required.

---

## Links

- **Hawk Academy SEO Skills hub:** [hawkacademy.co/claude-seo-skills](https://hawkacademy.co/claude-seo-skills) (canonical home, all 25 skills with worked examples)
- **The Hawk Academy SEO Roadmap:** [hawkacademy.co/resources/seo-roadmap](https://hawkacademy.co/resources/seo-roadmap)
- **Free Hawk Academy course:** [learn.hawkacademy.co/register](https://learn.hawkacademy.co/register)
- **StudioHawk:** [studiohawk.com.au](https://studiohawk.com.au) (the parent agency)
- **About Harry Sanders:** [hawkacademy.co/about/harry-sanders](https://hawkacademy.co/about/harry-sanders)
- **About Lawrence Hitches:** [hawkacademy.co/about/lawrence-hitches](https://hawkacademy.co/about/lawrence-hitches)

Built with Claude.
