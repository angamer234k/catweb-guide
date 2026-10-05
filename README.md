# CatWeb Ultimate Knowledge Base (`cw`)

**The single source of truth for CatWeb (Roblox) — built for humans *and* AI agents.**

CatWeb is the Roblox game where you build real 2D websites with JSON UI + block scripting (`.rbx` TLD, Chrome parody, all inside the game).

This repo merges:
- **SiteGPT V11** (by DevsLovePizza) — the most complete AI-oriented guide with exact output contracts, action IDs, parameter shapes, decoder, icons, sounds
- **Mailo037/catweb-docs** — clean structured reference (CatDocs, UIGPT, JSONScript, Assets)
- Community wikis (Fandom + Miraheze) — lore, local pages, updates, rules, popular sites
- Related tools & compilers

**Targeting CatWeb ~v2.18+** (update VERSION.md when the game updates)

---

## Quick Start for AI Agents

1. Load `02-ai-agent/SKILL.md` as your system prompt / skill.
2. Follow the **OUTPUT CONTRACT** religiously — every response that generates a site **must** be a single valid JSON object.
3. Never invent action IDs or property keys. Use only what’s documented.
4. Prefer fixed `font_size` over `"scaled"` unless the text really needs to flex.
5. Validate with the tools in `04-tools/` if available.

## Folder Structure

```
cw/
├── README.md                     ← you are here
├── VERSION.md                    ← current game version we target
│
├── 01-core/                      # Pure reference material
│   ├── SiteGPT-V11.md            # Full original SiteGPT (AI contract + everything)
│   ├── UIGPT.md                  # Element schema & layout rules
│   ├── JSONScript.md             # Every event + action ID + exact shape
│   ├── Assets.md                 # Icons, sounds, decoder table
│   └── Limits.md                 # Free vs Premium, element caps, etc.
│
├── 02-ai-agent/                  # LLM-focused
│   ├── SKILL.md                  # ★ THE main skill file — drop this into any agent
│   ├── output-contract.md
│   ├── common-failures.md
│   └── examples/
│
├── 03-community/                 # Lore & wiki stuff
│   ├── local-pages.md            # catweb:// urls
│   ├── updates.md
│   ├── rules.md
│   └── popular-sites.md
│
├── 04-tools/                     # Validators, compilers, links
│   └── related-repos.md
│
└── 05-templates/                 # Ready-to-import snippets (or link to additional-resources)
```

## Credits

- **DevsLovePizza** — SiteGPT V11 (the backbone of the AI contract)
- **Mailo037** — catweb-docs, additional-resources, MCP server, web runner
- **Fandom / Miraheze wiki contributors**
- CatWeb creator: **HumanCat222** (@CcXxiiHuman_C4t)

---

## Contributing

PRs welcome. Keep the AI agent path clean — any change that breaks the output contract or invents undocumented keys gets rejected.

If you’re adding new confirmed action shapes or game changes, put them in `01-core/` and update `VERSION.md`.
