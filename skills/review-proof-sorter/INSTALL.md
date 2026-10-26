# Install the Review Proof Sorter skill

This skill runs a small Python script, so it needs **Claude Code** (the Code tab in Claude Desktop, or Claude Code in your terminal) and Python 3 on your computer. No extra packages.

## Mac and Linux

```bash
mkdir -p ~/.claude/skills
mv ~/Downloads/review-proof-sorter ~/.claude/skills/
ls ~/.claude/skills/review-proof-sorter/SKILL.md
```

## Windows (PowerShell)

```powershell
New-Item -Path "$env:USERPROFILE\.claude\skills" -ItemType Directory -Force
Move-Item "$env:USERPROFILE\Downloads\review-proof-sorter" "$env:USERPROFILE\.claude\skills\"
Test-Path "$env:USERPROFILE\.claude\skills\review-proof-sorter\SKILL.md"
```

## Run it

Start a new Claude Code session and say: **"Sort my Google reviews onto my service pages"**, then paste your reviews.

Claude asks for your service pages (and the suburbs you serve, if you like), writes the words customers use for each service, runs the script and then reads the results itself to fix the sort. You get one proof block per page.
