# CatWeb Ultimate Knowledge Base (`cwukb`)

**a combined knowledge base of what cw is**

CatWeb (shortened, `cw`) is the Roblox game where you build real 2D websites with JSON UI + block scripting (`.rbx` TLD, Chrome parody, all inside the game).

This repo merges:
- **SiteGPT V11** (by DevsLovePizza) — the most complete AI-oriented guide with exact output contracts, action IDs, parameter shapes, decoder, icons, sounds
- **Mailo037/catweb-docs** — clean structured reference
- Community wikis (Fandom + Miraheze) — lore, local pages, updates, rules, popular sites
- Working examples + hard failure lists so agents actually succeed

**Targeting CatWeb v2.19.0.0** (Unlimited Update — see `VERSION.md`)

---

## For AI agents that cannot open GitHub pages

**Start here (raw):**

```
https://raw.githubusercontent.com/angamer234k/catweb-guide/main/AI_READ_TO_NAVIGATE.md
```

That file lists **every** documentation path as a `raw.githubusercontent.com` link so agents do not have to guess.

---

## Quick Start for AI Agents

1. Load **`AI_READ_TO_NAVIGATE.md`** (raw link above) for all paths.
2. Load **`02-ai-agent/SKILL.md`** as the system / skill prompt.
3. Also load (or have available):
   - `02-ai-agent/output-contract.md`
   - `02-ai-agent/common-failures.md`
4. For full tables and edge cases → `01-core/SiteGPT-V11.md`
5. When generating a site → output **one** valid top-level JSON object only.
6. Prefer fixed `font_size` over `"scaled"` unless text must flex.
7. Never invent action IDs, property keys, or asset IDs.

### Validate / repair (required for user JSON)

**If the user asks to validate, repair, or fix their JSON, use the appropriate tools in `04-tools/`. Never try to edit, modify, or fix JSONs without the validator/repair tools.**

- `04-tools/validate.py` / `validate.js` — check integrity, count objects
- `04-tools/repair.py` / `repair.js` — conservative auto-fix; **does nothing** if the schema already looks fine

### Ready-to-study examples

- `02-ai-agent/examples/minimal_site.json` — sticky header + scrolling body + centered card
- `02-ai-agent/examples/interactive_counter.json` — button, numeric variable, Set text, click sound
- `02-ai-agent/examples/v219_shadow_attributes.json` — UIShadow, per-corner radii, attributes

---

## Folder Structure

```
cw/
├── README.md
├── AI_READ_TO_NAVIGATE.md        # ★ All raw.githubusercontent.com links
├── VERSION.md
├── LICENSE
├── CONTRIBUTING.md
│
├── 01-core/                      # Pure reference
│   ├── SiteGPT-V11.md            # Full authoritative guide (v2.19)
│   ├── SiteGPT-V19-ADDENDUM.md
│   ├── UIGPT.md
│   ├── JSONScript.md
│   ├── Assets.md
│   └── Limits.md
│
├── 02-ai-agent/                  # LLM-focused
│   ├── SKILL.md                  # ★ Main skill file
│   ├── output-contract.md
│   ├── common-failures.md
│   └── examples/
│
├── 03-community/                 # Lore & wiki
│
├── 04-tools/
│   ├── validate.py / validate.js
│   ├── repair.py / repair.js     # Conservative repair only
│   └── related-repos.md
│
└── 05-templates/
```

---

## How to use with common AI tools

| Tool | How |
|------|-----|
| **DeepSeek / agents that fail on github.com** | Paste the **raw** navigate URL first: `https://raw.githubusercontent.com/angamer234k/catweb-guide/main/AI_READ_TO_NAVIGATE.md` |
| **Claude Projects / Custom GPTs** | Upload `SKILL.md` + `output-contract.md` + `common-failures.md` (and SiteGPT if context allows) |
| **Cursor / Windsurf / etc.** | Point the agent at this repo or drop the skill files into the project |
| **Direct chat (Grok, ChatGPT, etc.)** | Paste SKILL.md + the two short rule files, then ask for a site |
| **MCP** | See Mailo’s `catweb-mcp` for searchable access to docs + templates |

---

## Credits

- **DevsLovePizza** — SiteGPT V11 (backbone of the AI contract)
- **Mailo037** — catweb-docs, additional-resources, MCP, web runner
- **Fandom / Miraheze** wiki contributors
- CatWeb creator: **HumanCat222** (@CcXxiiHuman_C4t)

---

## Contributing

See `CONTRIBUTING.md`.  
PRs that keep the output contract and action shapes accurate are very welcome.
