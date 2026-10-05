#!/usr/bin/env node
/**
 * CatWeb JSON Validator & Object Counter
 * Usage:
 *   node validate.js path/to/site.json
 *   node validate.js path/to/folder/          (recursive)
 *   node validate.js site.json --strict
 *
 * Checks:
 *  - Valid JSON
 *  - Top-level shape (favicon, title, background, webcontent)
 *  - All scalars are strings
 *  - globalid uniqueness + charset
 *  - alias uniqueness
 *  - Forbidden property keys
 *  - Element counting (including styling + scripts)
 *  - Basic script structure warnings
 */

const fs = require("fs");
const path = require("path");

const FORBIDDEN_KEYS = new Set([
  "layout_order", "cell_size", "padding", "margin", "gap",
  "border-radius", "borderRadius", "flex", "justifyContent"
]);

const VALID_GLOBALID = /^[A-Za-z0-9]{2,3}$/;

function walk(node, stats, pathSoFar = "root") {
  if (!node || typeof node !== "object") return;

  if (Array.isArray(node)) {
    node.forEach((child, i) => walk(child, stats, `${pathSoFar}[${i}]`));
    return;
  }

  if (node.class) {
    stats.elements++;
    stats.byClass[node.class] = (stats.byClass[node.class] || 0) + 1;

    if (node.globalid) {
      if (!VALID_GLOBALID.test(node.globalid)) {
        stats.errors.push(`Invalid globalid "${node.globalid}" at ${pathSoFar} (must be 2-3 alphanumeric)`);
      }
      if (stats.globalids.has(node.globalid)) {
        stats.errors.push(`Duplicate globalid "${node.globalid}" at ${pathSoFar}`);
      }
      stats.globalids.add(node.globalid);
    }

    if (node.alias) {
      if (stats.aliases.has(node.alias)) {
        stats.errors.push(`Duplicate alias "${node.alias}" at ${pathSoFar}`);
      }
      stats.aliases.add(node.alias);
    }

    for (const k of Object.keys(node)) {
      if (FORBIDDEN_KEYS.has(k)) {
        stats.errors.push(`Forbidden key "${k}" at ${pathSoFar}`);
      }
      const v = node[k];
      if (v !== null && typeof v !== "object" && typeof v !== "string") {
        stats.errors.push(`Non-string scalar "${k}": ${typeof v} at ${pathSoFar}`);
      }
    }

    if (node.class === "script") {
      stats.scripts++;
      if (!Array.isArray(node.content)) {
        stats.errors.push(`script.content must be an array at ${pathSoFar}`);
      } else {
        node.content.forEach((block, i) => {
          if (!block.id) stats.errors.push(`Script block missing id at ${pathSoFar}.content[${i}]`);
          if (block.actions && !Array.isArray(block.actions)) {
            stats.errors.push(`actions must be array at ${pathSoFar}.content[${i}]`);
          }
          const controlIds = new Set(["18","19","20","21","22","23","25","112","125","126","37","38","92","93","44","45","46","47"]);
          if (controlIds.has(String(block.id)) && block.actions) {
            stats.errors.push(`Control-flow id ${block.id} has nested "actions" at ${pathSoFar}.content[${i}] — must be flat`);
          }
        });
      }
    }
  }

  if (node.children) walk(node.children, stats, `${pathSoFar}.children`);
}

function validateFile(filePath, strict = false) {
  const raw = fs.readFileSync(filePath, "utf8");
  let data;
  try {
    data = JSON.parse(raw);
  } catch (e) {
    return { file: filePath, ok: false, errors: [`JSON parse error: ${e.message}`], stats: null };
  }

  const stats = {
    elements: 0,
    scripts: 0,
    byClass: {},
    globalids: new Set(),
    aliases: new Set(),
    errors: [],
    warnings: []
  };

  if (typeof data !== "object" || Array.isArray(data)) {
    stats.errors.push("Root must be a JSON object (full site), not an array");
  } else {
    if (!data.favicon) stats.warnings.push("Missing favicon");
    if (!data.title) stats.warnings.push("Missing title");
    if (!data.background) stats.warnings.push("Missing background");
    if (!data.webcontent) {
      stats.errors.push("Missing webcontent array");
    } else if (!Array.isArray(data.webcontent)) {
      stats.errors.push("webcontent must be an array");
    } else {
      walk(data.webcontent, stats, "webcontent");
    }
  }

  const ok = stats.errors.length === 0 && (!strict || stats.warnings.length === 0);
  return { file: filePath, ok, errors: stats.errors, warnings: stats.warnings, stats };
}

function collectFiles(target) {
  const st = fs.statSync(target);
  if (st.isFile()) return [target];
  const results = [];
  function rec(dir) {
    for (const name of fs.readdirSync(dir)) {
      const p = path.join(dir, name);
      const s = fs.statSync(p);
      if (s.isDirectory()) rec(p);
      else if (name.endsWith(".json")) results.push(p);
    }
  }
  rec(target);
  return results;
}

const args = process.argv.slice(2);
if (args.length === 0) {
  console.log("Usage: node validate.js <file-or-folder> [--strict]");
  process.exit(1);
}

const strict = args.includes("--strict");
const target = args.find(a => !a.startsWith("--"));
const files = collectFiles(target);

let totalErrors = 0;
for (const f of files) {
  const r = validateFile(f, strict);
  console.log(`\n=== ${r.file} ===`);
  if (r.stats) {
    console.log(`Elements: ${r.stats.elements}  |  Scripts: ${r.stats.scripts}`);
    console.log("By class:", Object.entries(r.stats.byClass).map(([k,v]) => `${k}:${v}`).join(", ") || "(none)");
  }
  if (r.errors.length) {
    console.log("ERRORS:");
    r.errors.forEach(e => console.log("  ✗", e));
    totalErrors += r.errors.length;
  }
  if (r.warnings.length) {
    console.log("WARNINGS:");
    r.warnings.forEach(w => console.log("  ⚠", w));
  }
  if (r.ok) console.log("✓ OK");
}

process.exit(totalErrors > 0 ? 1 : 0);
