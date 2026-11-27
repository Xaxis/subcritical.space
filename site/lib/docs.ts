// The research documents as pages: every research/*.md except the ledger (which is /numbers), and
// the survey notes in research/notes/. Server only.
import "server-only";
import { parseMemo } from "./memo";
import { parseRanking, type Ranking } from "./pathways";
import { markdownIn, readRepoFile, repoFileExists } from "./repo";
import { docSlug, slugify } from "./text";

export interface Doc {
  file: string;
  slug: string;
  title: string;
  /** The first paragraph after the title, as Markdown. */
  lead: string;
  /** Everything after the lead, as Markdown. */
  body: string;
  /** Second-level headings, for the page's contents. */
  headings: { id: string; text: string }[];
}

function load(file: string): Doc {
  const text = readRepoFile(file)
    .replace(/\r\n/g, "\n")
    .replace(/<!--[\s\S]*?-->\n?/g, "");
  const titleMatch = /^# (.+)$/m.exec(text);
  const title = titleMatch?.[1]?.trim() ?? docSlug(file);
  let body = titleMatch ? text.slice((titleMatch.index ?? 0) + titleMatch[0].length) : text;
  body = body.replace(/^\s+/, "");
  let lead = "";
  if (!/^(#|\||>|-|\d+\.|!\[|```)/.test(body)) {
    const end = body.indexOf("\n\n");
    lead = end < 0 ? body : body.slice(0, end);
    body = end < 0 ? "" : body.slice(end + 2);
  }
  const headings = [...body.matchAll(/^## (.+)$/gm)].map((m) => ({
    id: slugify(m[1] as string),
    text: (m[1] as string).replace(/\[([^\]]*)\]\([^)]*\)/g, "$1").replace(/[*_`]/g, ""),
  }));
  return { file, slug: docSlug(file), title, lead, body, headings };
}

/** The research documents, in their numbered order. */
export function researchDocs(): Doc[] {
  return markdownIn("research")
    .filter((f) => !f.endsWith("/numbers.md"))
    .map(load);
}

/** The survey notes, raw, in track order. */
export function surveyNotes(): Doc[] {
  return markdownIn("research/notes").map(load);
}

export function memo() {
  return parseMemo(readRepoFile("research/00-memo.md"));
}

/** The pathways re-ranked on Part I's evidence, once research/02-pathways.md exists. */
export function ranking(): Ranking | null {
  const file = "research/02-pathways.md";
  return repoFileExists(file) ? parseRanking(readRepoFile(file)) : null;
}

/** The ten survey tracks the plan names, so the site can say which have reported. */
export const TRACKS = [
  ["01", "definitions", "Definitions and thresholds in force"],
  ["02", "physics", "Physics of computation"],
  ["03", "algorithms", "Algorithms: scaling, progress, inference"],
  ["04", "dynamics", "Dynamics: returns to research, takeoff"],
  ["05", "cognition", "Cognition and function"],
  ["06", "economics", "Economics and organisation"],
  ["07", "compute-governance", "Compute governance and hardware"],
  ["08", "arms-control", "Arms control and verification"],
  ["09", "mechanism-design", "Mechanism design"],
  ["10", "gameable-evals", "Evaluations that can be gamed"],
] as const;
