#!/usr/bin/env node
/**
 * CatWeb JSON Repair (conservative)
 *
 * Only applies fixes when the site JSON is structurally broken or uses
 * known-invalid keys/types. If the schema already looks fine, prints
 * NO_REPAIR_NEEDED and exits 0 without changing the file.
 *
 * Usage:
 *   node repair.js path/to/site.json
 *   node repair.js path/to/site.json --write
 *   node repair.js path/to/site.json --stdout
 *   cat site.json | node repair.js -
 */

const fs = require("fs");

const FORBIDDEN_KEY_MAP = {
  layout_order: "order",
  cell_size: "size",
};

const DROP_KEYS = new Set([
  "margin", "gap", "border-radius", "borderRadius",
  "flex", "justifyContent", "justify_content", "alignItems", "align_items",
]);

const VALID_GLOBALID = /^[A-Za-z0-9]{2,3}$/;
const CONTROL_IDS = new Set([
  "18", "19", "20", "21", "22", "23", "25", "112",
  "125", "126", "37", "38", "92", "93", "44", "45", "46", "47",
]);

function stringifyScalars(obj, changes, p = "root") {
  if (Array.isArray(obj)) {
    obj.forEach((v, i) => {
      const pp = `${p}[${i}]`;
      if (v !== null && typeof v === "object") stringifyScalars(v, changes, pp);
      else if (typeof v !== "string" && v !== undefined) {
        obj[i] = v === null ? "null" : String(v);
        changes.push(`stringified scalar ${pp}`);
      }
    });
    return;
  }
  if (obj && typeof obj === "object") {
    for (const k of Object.keys(obj)) {
      const pp = `${p}.${k}`;
      const v = obj[k];
      if (v !== null && typeof v === "object") stringifyScalars(v, changes, pp);
      else if (typeof v !== "string" && v !== undefined) {
        obj[k] = v === null ? "null" : String(v);
        changes.push(`stringified scalar ${pp}`);
      }
    }
  }
}

function fixKeys(obj, changes, p = "root") {
  if (Array.isArray(obj)) {
    obj.forEach((v, i) => fixKeys(v, changes, `${p}[${i}]`));
    return;
  }
  if (!obj || typeof obj !== "object") return;
  for (const k of Object.keys(obj)) {
    const pp = `${p}.${k}`;
    if (FORBIDDEN_KEY_MAP[k]) {
      const nk = FORBIDDEN_KEY_MAP[k];
      if (obj[nk] === undefined) {
        obj[nk] = obj[k];
        delete obj[k];
        changes.push(`renamed "${k}" → "${nk}" at ${pp}`);
      } else {
        delete obj[k];
        changes.push(`dropped duplicate forbidden key "${k}" at ${pp}`);
      }
    } else if (DROP_KEYS.has(k)) {
      delete obj[k];
      changes.push(`dropped invalid key "${k}" at ${pp}`);
    } else {
      fixKeys(obj[k], changes, pp);
    }
  }
}

function fixScriptControlFlow(node, changes, p = "root") {
  if (Array.isArray(node)) {
    node.forEach((c, i) => fixScriptControlFlow(c, changes, `${p}[${i}]`));
    return;
  }
  if (!node || typeof node !== "object") return;

  if (node.class === "script" && Array.isArray(node.content)) {
    const content = node.content;
    for (let i = 0; i < content.length; i++) {
      const block = content[i];
      if (!block || typeof block !== "object") continue;
      const bp = `${p}.content[${i]}`;
      const bid = String(block.id ?? "");
      if (CONTROL_IDS.has(bid) && Array.isArray(block.actions)) {
        const nested = block.actions;
        delete block.actions;
        changes.push(`flattened nested actions on control-flow id ${bid} at ${bp}`);
        content.splice(i + 1, 0, ...nested);
        i += nested.length;
      }
      if (Array.isArray(block.actions)) {
        block.actions.forEach((a, j) => fixScriptControlFlow(a, changes, `${bp}.actions[${j}]`));
      }
    }
  }
  if (Array.isArray(node.children)) {
    node.children.forEach((c, i) => fixScriptControlFlow(c, changes, `${p}.children[${i}]`));
  }
}

function ensureRootShape(data, changes) {
  if (!data || typeof data !== "object" || Array.isArray(data)) {
    changes.push("root was not an object — cannot auto-wrap safely");
    return data;
  }
  if (data.webcontent === undefined) {
    if (data.class) {
      const metaKeys = ["favicon", "title", "background", "thumbnail_id", "thumbnail"];
      const el = { ...data };
      const meta = {};
      for (const k of metaKeys) {
        if (el[k] !== undefined) {
          meta[k] = el[k];
          delete el[k];
        }
      }
      data = {
        favicon: meta.favicon || "128490289676597",
        title: meta.title || "Untitled",
        background: meta.background || "#ffffff",
        webcontent: [el],
      };
      changes.push("wrapped single element into top-level site object with webcontent");
    } else {
      changes.push("missing webcontent — cannot invent tree");
    }
  } else if (!Array.isArray(data.webcontent)) {
    data.webcontent = [data.webcontent];
    changes.push("wrapped webcontent into array");
  }
  for (const [key, def] of [
    ["favicon", "128490289676597"],
    ["title", "Untitled"],
    ["background", "#ffffff"],
  ]) {
    if (data[key] === undefined) {
      data[key] = def;
      changes.push(`added missing top-level "${key}"`);
    } else if (typeof data[key] !== "string") {
      data[key] = String(data[key]);
      changes.push(`stringified top-level "${key}"`);
    }
  }
  return data;
}

function fixGlobalids(data, changes) {
  const used = new Set();
  let counter = 0;
  const alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  function nextGid() {
    while (true) {
      const n = counter++;
      let gid;
      if (n < 62 * 62) {
        gid = alphabet[Math.floor(n / 62) % 62] + alphabet[n % 62];
      } else {
        const n2 = n - 62 * 62;
        const a = Math.floor(n2 / (62 * 62)) % 62;
        const b = Math.floor(n2 / 62) % 62;
        const c = n2 % 62;
        gid = alphabet[a] + alphabet[b] + alphabet[c];
      }
      if (!used.has(gid)) return gid;
    }
  }

  function walk(node, p) {
    if (Array.isArray(node)) {
      node.forEach((c, i) => walk(c, `${p}[${i}]`));
      return;
    }
    if (!node || typeof node !== "object") return;
    if (node.class) {
      const gid = node.globalid;
      if (!gid || typeof gid !== "string" || !VALID_GLOBALID.test(gid) || used.has(gid)) {
        const ng = nextGid();
        node.globalid = ng;
        changes.push(`assigned globalid "${ng}" at ${p}`);
        used.add(ng);
      } else {
        used.add(gid);
      }
    }
    if (node.children) walk(node.children, `${p}.children`);
    if (node.class === "script" && Array.isArray(node.content)) {
      node.content.forEach((block, i) => {
        if (!block || typeof block !== "object") return;
        const bg = block.globalid;
        if (block.id !== undefined) {
          if (!bg || typeof bg !== "string" || !VALID_GLOBALID.test(String(bg)) || used.has(bg)) {
            const ng = nextGid();
            block.globalid = ng;
            changes.push(`assigned globalid "${ng}" at ${p}.content[${i}]`);
            used.add(ng);
          } else {
            used.add(bg);
          }
        }
        if (Array.isArray(block.actions)) {
          block.actions.forEach((act, j) => {
            if (!act || typeof act !== "object") return;
            const ag = act.globalid;
            if (!ag || typeof ag !== "string" || !VALID_GLOBALID.test(String(ag)) || used.has(ag)) {
              const ng = nextGid();
              act.globalid = ng;
              changes.push(`assigned globalid "${ng}" at ${p}.content[${i}].actions[${j}]`);
              used.add(ng);
            } else {
              used.add(ag);
            }
          });
        }
      });
    }
  }
  if (data && Array.isArray(data.webcontent)) walk(data.webcontent, "webcontent");
}

function needsRepair(data) {
  const issues = [];
  if (!data || typeof data !== "object" || Array.isArray(data)) {
    issues.push("root_not_object");
    return issues;
  }
  if (data.webcontent === undefined) issues.push("missing_webcontent");
  else if (!Array.isArray(data.webcontent)) issues.push("webcontent_not_array");

  function scan(node, p = "root") {
    if (Array.isArray(node)) {
      node.forEach((c, i) => scan(c, `${p}[${i}]`));
      return;
    }
    if (!node || typeof node !== "object") return;
    for (const [k, v] of Object.entries(node)) {
      if (FORBIDDEN_KEY_MAP[k] || DROP_KEYS.has(k)) issues.push(`bad_key:${k}@${p}`);
      if (v !== null && v !== undefined && typeof v !== "object" && typeof v !== "string") {
        issues.push(`non_string:${k}@${p}`);
      }
    }
    if (node.class === "script" && Array.isArray(node.content)) {
      node.content.forEach((block, i) => {
        if (block && typeof block === "object") {
          const bid = String(block.id ?? "");
          if (CONTROL_IDS.has(bid) && block.actions) {
            issues.push(`nested_actions@${p}.content[${i}]`);
          }
        }
      });
    }
    if (node.class && node.globalid !== undefined) {
      if (typeof node.globalid !== "string" || !VALID_GLOBALID.test(node.globalid)) {
        issues.push(`bad_globalid@${p}`);
      }
    }
    if (node.children) scan(node.children, `${p}.children`);
  }
  if (Array.isArray(data.webcontent)) scan(data.webcontent, "webcontent");
  return issues;
}

function repair(data) {
  const changes = [];
  data = JSON.parse(JSON.stringify(data));
  data = ensureRootShape(data, changes);
  fixKeys(data, changes);
  stringifyScalars(data, changes);
  if (data && Array.isArray(data.webcontent)) {
    data.webcontent.forEach((el, i) => fixScriptControlFlow(el, changes, `webcontent[${i}]`));
  }
  fixGlobalids(data, changes);
  return { data, changes };
}

function main() {
  const argv = process.argv.slice(2);
  const write = argv.includes("--write");
  const stdoutOnly = argv.includes("--stdout");
  const args = argv.filter((a) => !a.startsWith("--"));
  if (!args.length) {
    console.error("Usage: node repair.js <file.json|- > [--write] [--stdout]");
    process.exit(1);
  }
  const target = args[0];
  let raw;
  let filePath = null;
  if (target === "-") {
    raw = fs.readFileSync(0, "utf8");
  } else {
    filePath = target;
    raw = fs.readFileSync(filePath, "utf8");
  }

  let data;
  try {
    data = JSON.parse(raw);
  } catch (e) {
    console.error("PARSE_ERROR:", e.message);
    process.exit(1);
  }

  const issues = needsRepair(data);
  if (!issues.length) {
    console.log("NO_REPAIR_NEEDED");
    console.log("Schema looks fine — no automatic changes applied.");
    if (stdoutOnly) console.log(JSON.stringify(data, null, 2));
    process.exit(0);
  }

  const { data: repaired, changes } = repair(data);
  console.log(`REPAIRED (${changes.length} change(s))`);
  for (const c of changes) console.log("  •", c);
  const out = JSON.stringify(repaired, null, 2);
  if (stdoutOnly) {
    console.log(out);
  } else if (write && filePath) {
    const outPath = filePath.replace(/\.json$/i, "") + ".repaired.json";
    fs.writeFileSync(outPath, out + "\n", "utf8");
    console.log("Wrote", outPath);
  } else {
    console.log("--- repaired JSON ---");
    console.log(out);
  }
  process.exit(0);
}

main();
