// The pathway ranking in research/02-pathways.md, read from its "## The ranking" table. Pure, so
// the tests read the real file the same way the page does. Columns are found by name: if the
// chapter renames one the page shows, the build fails here instead of showing the wrong column.

export interface Ranking {
  /** The columns the page shows, in this order, named as the chapter names them. */
  header: string[];
  rows: string[][];
  /** How many pathways the memo did not list (its rank cell does not start with a digit). */
  added: number;
}

export const SHOWN = [
  "Rank now",
  "Pathway",
  "Necessary?",
  "Sufficient?",
  "Cost of a limit to useful AI",
  "The channel that sees it",
  "Memo's rank",
] as const;

function cells(line: string): string[] {
  return line
    .replace(/^\||\|$/g, "")
    .split("|")
    .map((c) => c.trim());
}

export function parseRanking(text: string): Ranking {
  const lines = text.split("\n");
  const at = lines.findIndex((l) => l.startsWith("## The ranking"));
  if (at < 0) throw new Error('the pathways chapter has no section "## The ranking"');
  const rest = lines.slice(at + 1);
  const end = rest.findIndex((l) => l.startsWith("## "));
  const body = end < 0 ? rest : rest.slice(0, end);
  const first = body.findIndex((l) => l.startsWith("|"));
  if (first < 0) throw new Error("the ranking section has no table");
  const table: string[] = [];
  for (const l of body.slice(first)) {
    if (!l.startsWith("|")) break;
    table.push(l);
  }
  const all = cells(table[0] ?? "");
  const idx = SHOWN.map((name) => {
    const i = all.indexOf(name);
    if (i < 0) throw new Error(`the ranking table has no column "${name}"`);
    return i;
  });
  const rows = table.slice(2).map((l) => {
    const c = cells(l);
    return idx.map((i) => c[i] ?? "");
  });
  const memo = SHOWN.indexOf("Memo's rank");
  return {
    header: [...SHOWN],
    rows,
    added: rows.filter((r) => !/^\d/.test(r[memo] ?? "")).length,
  };
}
