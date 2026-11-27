// The experiment plan in research/04-claims.md, read from its "## Experiments" list. Pure, so the
// tests read the real file the same way the page does. Each item has the shape
//   N. **E4, title.** what it does ... `heavy`, time. `e04_loop_gain`. C4, C2. Browser: yes.
// and an item that names no script (E4's later parts) shares its code but has no result of its own.

export interface Planned {
  /** Its place in the build order. */
  order: number;
  code: string;
  title: string;
  /** What it does, as Markdown, without the closing particulars. */
  body: string;
  /** tools/exp/<script>.py and data/results/<script>.json, when the item names one. */
  script: string | null;
  runner: "heavy" | "gpu" | null;
  time: string;
  /** The claims and open questions it serves, as Markdown. */
  serves: string;
  browser: boolean;
}

export interface Phase {
  title: string;
  items: Planned[];
}

const ITEM = /^(\d+)\. \*\*(E\d+), (.+?)\*\*\s*([\s\S]*)$/;
const PHASE = /^\*\*(Phase \d+: .+?)\*\*/;

function parseItem(text: string): Planned {
  const m = ITEM.exec(text);
  if (!m) throw new Error(`not an experiment item: ${text.slice(0, 60)}`);
  const [, order, code, rawTitle, rest] = m as unknown as [string, string, string, string, string];
  const browser = /Browser: yes\.?\s*$/.test(rest);
  const before = rest.replace(/\s*Browser: (yes|no)\.?\s*$/, "");
  const run = /`(heavy|gpu)`, ([^.]+)\./.exec(before);
  const script = /`(e\d{2}_[a-z0-9_]+)`/.exec(before);
  // What it serves is the last sentence before "Browser".
  const cut = Math.max(before.lastIndexOf("`. "), before.lastIndexOf(". "));
  const serves = (cut < 0 ? "" : before.slice(cut).replace(/^`?\. /, "")).replace(/\.$/, "");
  const end = run ? run.index : before.length;
  return {
    order: Number(order),
    code,
    title: rawTitle.replace(/\.$/, ""),
    body: before.slice(0, end).trim(),
    script: script ? (script[1] as string) : null,
    runner: run ? (run[1] as "heavy" | "gpu") : null,
    time: run ? (run[2] as string).trim() : "",
    serves: serves.trim(),
    browser,
  };
}

export function parseExperiments(claims: string): Phase[] {
  const at = claims.search(/^## Experiments\b/m);
  if (at < 0) throw new Error('the claims file has no section "## Experiments"');
  const section = claims.slice(at).split(/\n## /)[0] ?? "";
  const phases: Phase[] = [];
  let item: string[] | null = null;
  const flush = () => {
    if (!item) return;
    const phase = phases.at(-1);
    if (!phase) throw new Error("an experiment comes before any phase heading");
    phase.items.push(parseItem(item.join(" ")));
    item = null;
  };
  for (const line of section.split("\n")) {
    const phase = PHASE.exec(line);
    if (phase) {
      flush();
      phases.push({ title: (phase[1] as string).replace(/\.$/, ""), items: [] });
    } else if (/^\d+\. \*\*E\d+/.test(line)) {
      flush();
      item = [line.trim()];
    } else if (item && /^\s+\S/.test(line)) {
      item.push(line.trim());
    } else if (item && line.trim() === "") {
      flush();
    }
  }
  flush();
  return phases;
}
