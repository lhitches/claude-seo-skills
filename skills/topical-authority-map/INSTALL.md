# Install the Topical Authority Map skill

This skill works in **Claude Code** (the CLI) and the **Claude app** (claude.ai and the desktop app). Each path takes about a minute.

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

## Option 2: The Claude app (claude.ai or desktop)

The Claude app installs a skill from a zip. `topical-authority-map.zip` is already in the right shape, with the references and the sample output inside it. Skills work on every plan, including Free.

1. Turn on code execution, which skills need to run. On a Free, Pro or Max plan, go to **Settings > Capabilities** and switch on **Code execution and file creation**. On a Team plan skills are on by default. If they are off on a Team or Enterprise plan, an owner turns them on in **Organization settings > Plugins & skills**, on the Policy tab.
2. Go to **Customize > Skills**. Click the **+** button, then **Create skill**, then **Upload a skill**.
3. Choose `topical-authority-map.zip`. Upload it as it is. Do not unzip it first.
4. Check the skill is switched on in your skills list.
5. Start a new chat and type:

```
Build a topical authority map for [your seed keyword]
```

The skill triggers from your request and loads the reference files as the workflow progresses.

---

## Option 3: The Projects fallback (no Skills feature needed)

Use this only if you cannot use the Skills feature, for example because your organisation has switched it off. It uses a Project instead, and Projects are available on every plan.

1. In the Claude app, create a new **Project** named `Topical Authority Map`.
2. Open `SKILL.md` in a text editor. Copy everything **below** the frontmatter, that is everything after the second `---` line near the top. Paste it into the Project's instructions.
3. Add the three files in `references/` to the Project's knowledge.
4. Start a chat inside that Project and type the prompt above.

The Skills feature in Options 1 and 2 is tidier because the skill triggers automatically. The Projects method does the same job.

---

## What to expect when you run it

Claude will pause at five checkpoints. Answer each one and confirm before it proceeds.

1. **Central entity confirmation.** Claude proposes the one thing your site is allowed to be known for. You confirm or refine.
2. **Source context plus persona.** Claude asks five questions about your business (type, market, angle, customer language, Knowledge Panel test) and asks who the real author or expert reviewer is, with credentials that can be checked. It never invents one.
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

In the Claude app, check the skill is switched on under **Customize > Skills**, then start a new chat. A chat that was already open before the upload does not pick the skill up. If you used the Projects fallback, start the chat inside the Project, because Project instructions do not load into general chats.

### "The output stops after a few rows."

The xlsx generation can hit token limits on large maps. If Claude stops mid-sheet, ask:

```
Continue the spreadsheet from where you left off. Resume Tab [N] at row [X].
```

Claude will pick up from the exact row.

### "Some checkpoints feel slow. Can I skip them?"

You can, but you should not. The checkpoints are where the strategy gets calibrated to your business. Skipping Checkpoint 2 (source context plus persona) is the most common reason a topical map ends up generic. Spend the five minutes per checkpoint. The 12-week publishing order is only as good as the entity decision in Checkpoint 1.

### "Can I run it on a niche I do not own?"

Yes. The skill works on any seed keyword. You can run it on a competitor's niche, a niche you are considering entering, or a hypothetical business. Just answer the source context questions as if you were that business. Any persona in a practice run is an example: label it as one, and never publish it as a real person.

---

## Need help?

- Watch the full walkthrough: [Topical Authority with Claude (Build the 4-Cluster Map for Free)](https://www.youtube.com/@HarrySanders) on YouTube.
- Read the step-by-step guide: [How to use the Topical Authority Map skill](https://hawkacademy.co/seo-guides/topical-authority-map-guide).
- Browse other free skills: [hawkacademy.co/claude-seo-skills](https://hawkacademy.co/claude-seo-skills).
