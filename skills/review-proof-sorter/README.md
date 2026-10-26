# review-proof-sorter: Google reviews into proof on every service page (Claude Skill)

A Claude skill that takes a business's Google reviews and its service pages, sorts every review
by the service and the suburb it talks about, and writes a proof block for each page: the best
quotes word for word, the words customers use for that job, and the pages that need more reviews.

## What it does
1. Takes the reviews (pasted, or a CSV/JSON/text export) and the list of service pages.
2. Claude writes the customer words for each service; the script sorts the reviews with them.
3. Claude reads the unsorted and doubtful ones and assigns them by meaning.
4. Hands back `proof-blocks.md` (one block per service and location page) and `sorted-reviews.csv`.

## How to use
Ask Claude: **"Sort my Google reviews onto my service pages"** and paste your reviews.

## What's inside
```
review-proof-sorter/
├── SKILL.md                         # instructions Claude follows
├── INSTALL.md                       # how to install it
├── scripts/review_proof_sorter.py   # sorts reviews, picks quotes, writes the outputs (Python 3, no extra packages)
└── assets/
    ├── services-template.csv        # service, url, keywords
    └── places-template.csv          # place, url, aliases
```

## Notes
- Quotes are always whole sentences, word for word. The skill never edits a review.
- Australian health practitioners: Ahpra bans testimonials about clinical care in advertising,
  so the skill only uses non-clinical reviews for them.
