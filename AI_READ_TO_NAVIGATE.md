# AI Read / Navigate — Raw Links (do not guess paths)

**Repo:** https://github.com/angamer234k/catweb-guide  
**Branch:** `main`  
**Raw base:** `https://raw.githubusercontent.com/angamer234k/catweb-guide/main/`

Paste **this file’s raw URL** first when an agent cannot open the GitHub UI:

```
https://raw.githubusercontent.com/angamer234k/catweb-guide/main/AI_READ_TO_NAVIGATE.md
```

Then load the files below by purpose. Prefer **raw** URLs over github.com HTML pages.

---

## Start here (generation)

| File | Raw URL |
|------|---------|
| **SKILL.md** (main agent prompt) | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/02-ai-agent/SKILL.md |
| **output-contract.md** | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/02-ai-agent/output-contract.md |
| **common-failures.md** | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/02-ai-agent/common-failures.md |

---

## Core reference

| File | Raw URL |
|------|---------|
| **SiteGPT-V11.md** (full bible) | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/01-core/SiteGPT-V11.md |
| **SiteGPT-V19-ADDENDUM.md** | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/01-core/SiteGPT-V19-ADDENDUM.md |
| **UIGPT.md** | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/01-core/UIGPT.md |
| **JSONScript.md** | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/01-core/JSONScript.md |
| **Assets.md** | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/01-core/Assets.md |
| **Limits.md** | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/01-core/Limits.md |

---

## Examples (valid site JSON)

| File | Raw URL |
|------|---------|
| minimal_site.json | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/02-ai-agent/examples/minimal_site.json |
| interactive_counter.json | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/02-ai-agent/examples/interactive_counter.json |
| v219_shadow_attributes.json | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/02-ai-agent/examples/v219_shadow_attributes.json |

---

## Community / lore

| File | Raw URL |
|------|---------|
| overview.md | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/03-community/overview.md |
| updates.md | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/03-community/updates.md |
| badges.md | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/03-community/badges.md |
| popular-sites.md | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/03-community/popular-sites.md |
| local-pages.md | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/03-community/local-pages.md |
| rules.md | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/03-community/rules.md |
| tutorials.md | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/03-community/tutorials.md |
| elements-wiki.md | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/03-community/elements-wiki.md |

---

## Tools (validate / repair)

| File | Raw URL |
|------|---------|
| validate.py | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/04-tools/validate.py |
| validate.js | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/04-tools/validate.js |
| repair.py | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/04-tools/repair.py |
| repair.js | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/04-tools/repair.js |
| related-repos.md | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/04-tools/related-repos.md |

---

## Meta

| File | Raw URL |
|------|---------|
| README.md | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/README.md |
| VERSION.md | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/VERSION.md |
| CONTRIBUTING.md | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/CONTRIBUTING.md |
| LICENSE | https://raw.githubusercontent.com/angamer234k/catweb-guide/main/LICENSE |

---

## Suggested load order for agents

1. This file (navigate)  
2. `02-ai-agent/SKILL.md`  
3. `02-ai-agent/output-contract.md`  
4. `02-ai-agent/common-failures.md`  
5. As needed: `01-core/UIGPT.md`, `01-core/JSONScript.md`, `01-core/SiteGPT-V11.md`  
6. Validate/repair: run tools under `04-tools/` — do **not** hand-edit user JSON without them  

**Validate / repair rule:** If the user asks to validate, repair, or fix their JSON, use the appropriate tools in `04-tools/`. Never try to edit, modify, or fix JSONs without the validator/repair tools.
