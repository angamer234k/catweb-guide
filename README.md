# CatWeb Ultimate Knowledge Base (`cw`)

**a combined knowledge base of what cw is**

CatWeb is the Roblox game where you build real 2D websites with JSON UI + block scripting (`.rbx` TLD, Chrome parody, all inside the game).

This repo merges:
- **SiteGPT V11** (by DevsLovePizza) — the most complete AI-oriented guide with exact output contracts, action IDs, parameter shapes, decoder, icons, sounds
- **Mailo037/catweb-docs** — clean structured reference
- Community wikis (Fandom + Miraheze) — lore, local pages, updates, rules, popular sites
- Working examples + hard failure lists so agents actually succeed

**Targeting CatWeb ~v2.18+** (see `VERSION.md`)

---

## Quick Start for AI Agents

1. Load **`02-ai-agent/SKILL.md`** as the system / skill prompt.
2. Also load (or have available):
   - `02-ai-agent/output-contract.md`
   - `02-ai-agent/common-failures.md`
3. For full tables and edge cases → `01-core/SiteGPT-V11.md`
4. When generating a site → output **one** valid top-level JSON object only.
5. Prefer fixed `font_size` over `"scaled"` unless text must flex.
6. Never invent action IDs, property keys, or asset IDs.

### Ready-to-study examples

- `02-ai-agent/examples/minimal_site.json` — sticky header + scrolling body + centered card
- `02-ai-agent/examples/interactive_counter.json` — button, numeric variable, Set text, click sound

---

## Folder Structure

```
cw/
├── README.md
├── VERSION.md
├── LICENSE
├── CONTRIBUTING.md
│
├── 01-core/                      # Pure reference
│   ├── SiteGPT-V11.md            # Full authoritative guide
│   ├── UIGPT.md                  # Element schema & layout
│   ├── JSONScript.md             # Events + actions survival guide
│   ├── Assets.md                 # 84 icons + 8 sounds + decoder note
│   └── Limits.md                 # Free vs Premium, caps, gamepasses
│
├── 02-ai-agent/                  # LLM-focused
│   ├── SKILL.md                  # ★ Main skill file
│   ├── output-contract.md        # Hard output rules
│   ├── common-failures.md        # What breaks import/publish
│   └── examples/
│       ├── minimal_site.json
│       └── interactive_counter.json
│
├── 03-community/                 # Lore & wiki
│   ├── local-pages.md            # catweb:// urls
│   ├── rules.md
│   ├── popular-sites.md
│   └── updates.md
│
├── 04-tools/
│   └── related-repos.md          # Mailo, Catpile, compilers, etc.
│
└── 05-templates/                 # Extra ready-to-import snippets
```

---

## How to use with common AI tools

| Tool | How |
|------|-----|
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
