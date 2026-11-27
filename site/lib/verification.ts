// The verification record in research/07-verification.md, read from its "## The record" table: one
// row per claim, one column per level, and the claim's standing. Each cell opens with a bold status
// from a fixed vocabulary, so the page can show at a glance where every claim stands. A status
// outside the vocabulary fails the build rather than showing as something it is not.

export type Tone = "pass" | "partial" | "fail" | "open";

/** Every status a cell may open with, and how it reads at a glance. */
export const STATUS: Record<string, Tone> = {
  new: "pass",
  proved: "pass",
  supports: "pass",
  survives: "pass",
  passed: "pass",
  // A standing: a contribution has passed all six levels; a candidate is alive with levels to go.
  contribution: "pass",
  candidate: "open",
  extends: "partial",
  "proved under assumptions": "partial",
  corrected: "partial",
  mixed: "partial",
  "survives with corrections": "partial",
  downgraded: "partial",
  application: "partial",
  "prior work": "fail",
  false: "fail",
  against: "fail",
  fails: "fail",
  cut: "fail",
  "cut in part": "fail",
  pending: "open",
  empirical: "open",
  untested: "open",
};

export interface Cell {
  status: string;
  tone: Tone;
  /** The rest of the cell, as Markdown. */
  detail: string;
}

export interface Row {
  /** The claim's code and short name, as Markdown (it links to the claim). */
  claim: string;
  code: string;
  levels: Cell[];
  standing: Cell;
}

export interface VerificationRecord {
  /** The level columns' headings, in order. */
  levels: string[];
  rows: Row[];
}

function cells(line: string): string[] {
  return line
    .replace(/^\||\|$/g, "")
    .split("|")
    .map((c) => c.trim());
}

function cell(text: string, where: string): Cell {
  const m = /^\*\*([^*]+)\*\*[:.]?\s*([\s\S]*)$/.exec(text);
  if (!m)
    throw new Error(`${where}: a cell must open with a bold status, got "${text.slice(0, 40)}"`);
  const status = (m[1] as string).trim().toLowerCase();
  const tone = STATUS[status];
  if (!tone) throw new Error(`${where}: "${status}" is not a status the record uses`);
  return { status, tone, detail: (m[2] as string).trim() };
}

export function parseRecord(text: string): VerificationRecord {
  const lines = text.split("\n");
  const at = lines.findIndex((l) => l.startsWith("## The record"));
  if (at < 0) throw new Error('the verification file has no section "## The record"');
  const rest = lines.slice(at + 1);
  const first = rest.findIndex((l) => l.startsWith("|"));
  if (first < 0) throw new Error("the record section has no table");
  const table: string[] = [];
  for (const l of rest.slice(first)) {
    if (!l.startsWith("|")) break;
    table.push(l);
  }
  const head = cells(table[0] ?? "");
  if (head[0] !== "Claim" || head.at(-1) !== "Standing")
    throw new Error('the record table runs from "Claim" to "Standing"');
  const levels = head.slice(1, -1);
  const rows = table.slice(2).map((l, i) => {
    const c = cells(l);
    if (c.length !== head.length) throw new Error(`record row ${i + 1} has ${c.length} cells`);
    const claim = c[0] as string;
    const code = /\bC\d+\b/.exec(claim)?.[0];
    if (!code) throw new Error(`record row ${i + 1} names no claim`);
    return {
      claim,
      code,
      levels: c.slice(1, -1).map((t, j) => cell(t, `${code}, ${levels[j]}`)),
      standing: cell(c.at(-1) as string, `${code}, standing`),
    };
  });
  return { levels, rows };
}
