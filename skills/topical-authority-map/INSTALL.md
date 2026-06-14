# Install the Topical Authority Map skill

This skill works in **Claude Code** (the CLI) and **Claude Desktop** (the app and web). The Claude Code path takes 30 seconds. The Claude Desktop path takes 2 minutes (Projects setup).

---

## Option 1: Claude Code (recommended, fastest)

Claude Code auto-loads any skill placed in `~/.claude/skills/`. Drop this folder there and you are done.

### Mac and Linux

```bash
# 1. Make sure the skills folder exists
mkdir -p ~/.claude/skills

# 2. Move the unzipped topical-authority-map folder into ~/.claude/skills/
mv ~/Downloads/topical-authority-map ~/.claude/skills/

# 3. Verify
ls ~/.claude/skills/topical-authority-map/SKILL.md
```

If the last command prints the path, the skill is installed.

### Windows (PowerShell)

```powershell
# 1. Make sure the skills folder exists
New-Item -Path "$env:USERPROFILE\.claude\skills" -ItemType Directory -Force

# 2. Move the unzipped topical-authority-map folder into %USERPROFILE%\.claude\skills\
Move-Item "$env:USERPROFILE\Downloads\topical-authority-map" "$env:USERPROFILE\.claude\skills\"

# 3. Verify
Test-Path "$env:USERPROFILE\.claude\skills\topical-authority-map\SKILL.md"
```

If the last command prints `True`, the skill is installed.

### First run

Open Claude Code in any project folder:

```bash
claude
```

Then type:

```
Build a topical authority map for [your seed keyword]
```

Example:

```
Build a topical authority map for premium australian furniture
```

Claude detects the trigger, loads the skill, and walks you through the five checkpoints.

---

## Option 2: Claude Desktop (web or app)

Claude Desktop does not auto-load skills the same way as Claude Code. Use a **Project** instead. The skill content becomes the Project's instructions. The reference files become Project Knowledge.

### Step 1. Create a new Project

1. Open [claude.ai](https://claude.ai) or the Claude Desktop app.
2. Click **Projects** in the sidebar.
3. Click **+ Create project**.
4. Name it: `Topical Authority Map`.
5. Description: `Builds a 4-cluster topical authority map from a seed keyword.`

### Step 2. Paste the skill into the Project's instructions

1. Open `SKILL.md` in any text editor.
2. Copy the entire body of the file (everything after the `---` frontmatter block).
3. In your new Project, click **Edit project instructions** (or **Custom instructions**).
4. Paste the skill body in.
5. Save.

### Step 3. Add the references as Project Knowledge

1. In the same Project, click **Add knowledge** (or **+ Files**).
2. Upload these three files:
   - `references/01-research-and-classify.md`
   - `references/02-architecture-and-keywords.md`
   - `references/03-execution-and-output.md`
3. Optionally upload `sample-output/premium-australian-furniture.xlsx` and `sample-output/premium-australian-furniture-strategy.md` so Claude can reference the example output during the run.

### Step 4. First run

Start a new chat in the Project. Type:

```
Build a topical authority map for [your seed keyword]
```

Claude will use the skill instructions and load the reference files from the Project Knowledge as the workflow progresses.

---

## What to expect when you run it

Claude will pause at five checkpoints. Answer each one and confirm before it proceeds.

1. **Central entity confirmation.** Claude proposes the one thing your site is allowed to be known for. You confirm or refine.
2. **Source context plus persona.** Claude asks five questions about your business (type, market, angle, customer language, Knowledge Panel test) and proposes a credible writer persona.
3. **Attribute list and client situations.** Claude does the deep research and presents the full list of attributes (every sub-topic, service, related entity) plus a client situation map. You add anything missing.
4. **Merge and split decisions.** Claude tells you which attributes get their own page and which get merged into another page. You confirm or override.
5. **Buyer journey gaps.** Claude tags every page TOFU, MOFU, or BOFU and flags gaps. You decide whether to add pages to fill them.

After Checkpoint 5 the skill produces:
1. The 5-tab spreadsheet (.xlsx).
2. The strategy document (.md).

Total runtime depends on how thoroughly you want the research done. A focused run on a single niche can complete in 30 to 45 minutes. A full enterprise-style run with three to five competitors analysed in depth can take 90 minutes. The output is the same shape either way.

---

## Output files

By default, Claude saves the output to your current working directory. Both files use the seed keyword as the filename:

- `premium-australian-furniture-topical-map.xlsx`
- `premium-australian-furniture-strategy.md`

You can ask Claude to save them anywhere you like, or to email them, or to push them to Google Drive.

---

## Troubleshooting

### "Claude does not seem to know the skill exists."

Check the folder structure. `~/.claude/skills/topical-authority-map/SKILL.md` must exist exactly at that path. If you moved the folder by hand, make sure the folder name is `topical-authority-map` (with hyphens, no spaces, all lowercase).

In Claude Code, restart the CLI (close and re-run `claude`) so it re-scans the skills directory.

In Claude Desktop, make sure you are in the Project (not a fresh chat). The Project instructions are not loaded into general chats.

### "The output stops after a few rows."

The xlsx generation can hit token limits on large maps. If Claude stops mid-sheet, ask:

```
Continue the spreadsheet from where you left off. Resume Tab [N] at row [X].
```

Claude will pick up from the exact row.

### "Some checkpoints feel slow. Can I skip them?"

You can, but you should not. The checkpoints are where the strategy gets calibrated to your business. Skipping Checkpoint 2 (source context plus persona) is the most common reason a topical map ends up generic. Spend the five minutes per checkpoint. The 12-week publishing order is only as good as the entity decision in Checkpoint 1.

### "Can I run it on a niche I do not own?"

Yes. The skill works on any seed keyword. You can run it on a competitor's niche, a niche you are considering entering, or a hypothetical business. Just answer the source context questions as if you were that business.

---

## Need help?

- Watch the full walkthrough: [Topical Authority with Claude (Build the 4-Cluster Map for Free)](https://www.youtube.com/@HarrySanders) on YouTube.
- Read the step-by-step guide: [How to use the Topical Authority Map skill](https://hawkacademy.co/seo-guides/topical-authority-map-guide).
- Browse other free skills: [hawkacademy.co/claude-seo-skills](https://hawkacademy.co/claude-seo-skills).
