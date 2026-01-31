---
tags: [system, migration, setup]
system: System
date_created: 2026-01-31
---

# Migration Guide: Linux to macOS (Mac Mini)

---

## Prerequisites

- Mac Mini with macOS
- Python 3.12+ installed (`brew install python3` if needed)
- Git configured with SSH keys for GitHub
- Network access for package installation

---

## Step 1: Transfer the Repository

From the Linux machine, copy VibologyOS to the Mac Mini. Any of these methods work:

**Option A — Git clone (cleanest):**
```bash
# On Mac Mini
cd ~
git clone git@github.com:shadesofjoe/VibologyOS.git
cd VibologyOS
git submodule update --init --recursive
```

**Option B — rsync over network:**
```bash
# On Mac Mini (replace IP/hostname)
rsync -av --exclude='.venv' --exclude='__pycache__' \
  joe@linux-pc:/home/joe/VibologyOS/ ~/VibologyOS/
```

**Option C — USB/external drive:**
Copy the entire `VibologyOS/` folder. The `.venv` directories can be excluded — they'll be recreated.

> **Note:** If using Option B or C, verify the git submodule is intact:
> ```bash
> cd ~/VibologyOS/System/humandesign_api
> git status
> ```
> If it shows errors, run `git submodule update --init --recursive` from the repo root.

---

## Step 2: Install Claude Code

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Then authenticate:
```bash
claude login
```

---

## Step 3: Recreate Python Environments

The project uses two requirements files. All three `.venv` directories need recreation since virtual environments contain platform-specific binaries.

**Main environment (used by chart scripts and HD API):**
```bash
cd ~/VibologyOS
python3 -m venv .venv
source .venv/bin/activate
pip install -r System/Scripts/requirements.txt
pip install -r System/humandesign_api/requirements.txt
```

**Verify installations:**
```bash
python3 -c "import kerykeion; print('Astrology OK')"
python3 -c "import fastapi; print('FastAPI OK')"
python3 -c "import swisseph; print('Swiss Ephemeris OK')"
```

> **Dependencies summary:**
> - `System/Scripts/requirements.txt` — kerykeion, httpx
> - `System/humandesign_api/requirements.txt` — fastapi, uvicorn, pyswisseph, pandas, numpy, geopy, timezonefinder, matplotlib, Pillow, reportlab, svgpath2mpl, and others

---

## Step 4: Verify the HD API

```bash
cd ~/VibologyOS
source .venv/bin/activate
cd System/humandesign_api
uvicorn humandesign.api:app --host 127.0.0.1 --port 9021 &

# Test it
curl http://127.0.0.1:9021/health
```

Should return a healthy response. Kill the background process when done:
```bash
kill %1
```

---

## Step 5: Test Chart Calculation

**Astrology:**
```bash
cd ~/VibologyOS
source .venv/bin/activate
python3 System/Scripts/get_astro_data.py \
  --name "Test" --year 1990 --month 1 --day 1 \
  --hour 12 --minute 0 --lat 40.7128 --lng -74.0060 \
  --timezone "America/New_York" --pretty
```

**Human Design (requires API running on port 9021):**
```bash
python3 System/Scripts/get_hd_data.py \
  --name "Test" --year 1990 --month 1 --day 1 \
  --hour 12 --minute 0 --lat 40.7128 --lng -74.0060 --pretty
```

Both should produce JSON output without errors.

---

## Step 6: Update Hardcoded Paths

~~Two documentation files referenced `/home/joe/` explicitly.~~ **Done.** Both files now use portable paths (`~/` or relative):

- **System/Technical Setup.md** — Now uses `~/VibologyOS`
- **System/Templates/_TEMPLATE - Initial Client Report.md** — Now uses relative `sys.path.insert` (works from repo root)

> No manual path updates needed on macOS.

---

## Step 7: Verify Claude Code Session

```bash
cd ~/VibologyOS
claude
```

Claude should greet you with context from NEXT.md and recent git history. Verify that:
- CLAUDE.md instructions are loaded (Claude will reference the Observatory, pillars, etc.)
- Git history is intact (`git log --oneline -5` from within the session)

---

## Step 8: Reconfigure Claude Code Settings (if needed)

User-level settings live in `~/.claude/` on each machine and don't transfer with the project. If you had custom configurations on Linux:

- **Permissions:** Use `/permissions` within a Claude session
- **MCP servers:** `claude mcp add` for any global servers
- **Keybindings:** Copy or recreate `~/.claude/keybindings.json`

The project-level `.claude/settings.local.json` transfers with the repo automatically.

---

## Step 9: Install Obsidian (Optional)

If you use Obsidian for browsing the vault:

1. Install Obsidian from https://obsidian.md
2. Open vault: select `~/VibologyOS` as the vault folder
3. Obsidian will detect the existing `.obsidian/` config directory

---

## What Transfers Automatically

| Component | Status |
|-----------|--------|
| All Library files (747) | Transfers with repo |
| CLAUDE.md governance | Transfers with repo |
| System protocols & templates | Transfers with repo |
| Git history | Transfers with repo |
| Chart scripts | Use relative paths — work as-is |
| HD API (git submodule) | Transfers with repo |
| `.env` (HD API token) | Transfers with repo |
| Wikilinks | Filename-based — unaffected |

## What Needs Rebuilding

| Component | Action |
|-----------|--------|
| Python `.venv` (x3) | Recreate from requirements.txt (Step 3) |
| Claude Code auth | `claude login` (Step 2) |
| Claude user settings | Reconfigure if customized (Step 8) |
| ~~2 hardcoded doc paths~~ | ~~Optional update (Step 6)~~ — Done |
| Git SSH keys | Configure on Mac if not already set |

---
