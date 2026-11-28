// The research documents as pages: every research/*.md except the ledger (which is /numbers), and
// the survey notes in research/notes/. Server only.
import "server-only";
import { type Phase, parseExperiments } from "./experiments";
import { parseMemo } from "./memo";
import { parseRanking, type Ranking } from "./pathways";
import { markdownIn, readRepoFile, repoFileExists } from "./repo";
import { docSlug, slugify } from "./text";
import { parseRecord, type VerificationRecord } from "./verification";

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

/** Where each claim stands at each level, once research/07-verification.md exists. */
export function verificationRecord(): VerificationRecord | null {
  const file = "research/07-verification.md";
  return repoFileExists(file) ? parseRecord(readRepoFile(file)) : null;
}

/** The verification reports, one per level and helper, as their helpers wrote them. */
export function verificationReports(): Doc[] {
  return markdownIn("research/verification").map(load);
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

/** The experiment plan in research/04-claims.md, once it exists. */
export function experimentPlan(): Phase[] | null {
  const file = "research/04-claims.md";
  return repoFileExists(file) ? parseExperiments(readRepoFile(file)) : null;
}

/** What an experiment wrote to data/results/<script>.json (tools/exp/lib.py's Results). */
export interface ExperimentResult {
  experiment: string;
  script: string;
  seed: number;
  data: { url: string; sha256: string; what: string }[];
  /** Its numbers' ids, sorted as the file stores them; the page shows the ledger's values. */
  ids: string[];
}

export function experimentResult(script: string): ExperimentResult | null {
  const file = `data/results/${script}.json`;
  if (!repoFileExists(file)) return null;
  const r = JSON.parse(readRepoFile(file)) as Omit<ExperimentResult, "ids"> & {
    numbers: Record<string, unknown>;
  };
  return {
    experiment: r.experiment,
    script: r.script,
    seed: r.seed,
    data: r.data ?? [],
    ids: Object.keys(r.numbers),
  };
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

/** One file of the paper: its title, its part (from the file's number) and its body. */
export interface PaperSection {
  file: string;
  /** The anchor for the section, from its file name: "11-physical". */
  id: string;
  title: string;
  part: string;
  body: string;
  words: number;
}

/** The paper's files in paper/, in order. Part I is 1x, Part II 2x, Part III 3x. */
export function paperSections(): PaperSection[] {
  const part = (n: number) =>
    n < 10
      ? "Introduction"
      : n < 20
        ? "Part I: what superintelligence is and how it forms"
        : n < 30
          ? "Part II: the protocol"
          : n < 40
            ? "Part III: what holds"
            : "Conclusion";
  return markdownIn("paper").map((file) => {
    const text = readRepoFile(file)
      .replace(/\r\n/g, "\n")
      .replace(/<!--[\s\S]*?-->\n?/g, "");
    const m = /^# (.+)$/m.exec(text);
    const name = file.replace(/^paper\//, "").replace(/\.md$/, "");
    const body = m ? text.slice((m.index ?? 0) + m[0].length).trim() : text;
    return {
      file,
      id: name,
      title: m?.[1]?.trim() ?? name,
      part: part(Number(/^(\d+)/.exec(name)?.[1] ?? 99)),
      body,
      words: body.split(/\s+/).filter(Boolean).length,
    };
  });
}
