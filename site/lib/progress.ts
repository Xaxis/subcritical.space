// Where the work stands, read from the repository rather than written by hand: a step counts as
// begun when its file exists. The plan is the handoff's, in its order.
import "server-only";
import { existsSync, readdirSync } from "node:fs";
import path from "node:path";
import { TRACKS } from "./docs";
import { ROOT, repoFileExists } from "./repo";

export interface Step {
  name: string;
  where: string;
  /** written: the file exists and awaits the six verification levels; done: nothing left to do. */
  state: "done" | "written" | "begun" | "not begun";
  detail: string;
}

function count(folder: string, ext: string): number {
  const dir = path.join(ROOT, folder);
  return existsSync(dir) ? readdirSync(dir).filter((f) => f.endsWith(ext)).length : 0;
}

export function tracksReported(): Set<string> {
  const dir = path.join(ROOT, "research/notes");
  const have = existsSync(dir) ? readdirSync(dir) : [];
  return new Set(TRACKS.filter(([n, slug]) => have.includes(`${n}-${slug}.md`)).map(([n]) => n));
}

/** Part I: the definitions and one chapter per perspective. */
const PART_I = [
  "research/01-anatomy.md",
  "research/011-physical.md",
  "research/012-computational.md",
  "research/013-dynamical.md",
  "research/014-cognitive.md",
  "research/015-organisational.md",
];

export function progress(): Step[] {
  const tracks = tracksReported().size;
  const results = count("data/results", ".json");
  const has = (f: string) => repoFileExists(f);
  const doc = (name: string, file: string, detail: string): Step => ({
    name,
    where: file,
    state: has(file) ? "written" : "not begun",
    detail,
  });
  const partI = PART_I.filter(has).length;
  return [
    {
      name: "Memo: candidate definitions and the protocol's shape",
      where: "research/00-memo.md",
      state: has("research/00-memo.md") ? "done" : "not begun",
      detail: "Candidates before the survey, not findings.",
    },
    {
      name: "Survey of the literature, ten tracks",
      where: "research/notes/",
      state: tracks === TRACKS.length ? "done" : tracks > 0 ? "begun" : "not begun",
      detail: `${tracks} of ${TRACKS.length} tracks have reported. Every source is opened before it is cited.`,
    },
    {
      name: "Part I: what superintelligence is and how it forms",
      where: "research/01-anatomy.md",
      state: partI === PART_I.length ? "written" : partI > 0 ? "begun" : "not begun",
      detail: `The definitions and the five perspectives, each mechanism defined, measured, with the evidence for and against (${partI} of ${PART_I.length} chapters).`,
    },
    doc(
      "The pathways, ranked by evidence",
      "research/02-pathways.md",
      "Which capabilities or architectures actually lead there.",
    ),
    doc(
      "Novelty: what is new, what extends prior work",
      "research/03-novelty.md",
      "With the closest prior work and the searches tried.",
    ),
    doc(
      "Claims, each with a runnable test",
      "research/04-claims.md",
      "A claim without a test is not a claim here.",
    ),
    {
      name: "Experiments on real data and models",
      where: "tools/exp/",
      state: results > 0 ? "begun" : "not begun",
      detail: `${results} of 11 planned experiments have results.`,
    },
    doc(
      "Proofs of the key properties",
      "research/05-formal.md",
      "Detection bound, equilibrium, coalition threshold, runaway condition.",
    ),
    doc(
      "The protocol, derived from the mechanisms",
      "research/06-protocol.md",
      "One limit per mechanism, its verification channel and its cost to useful AI.",
    ),
    doc(
      "Verification at six independent levels",
      "research/07-verification.md",
      "Anything that fails a level is cut or downgraded.",
    ),
    {
      name: "The paper, in Paperwright",
      where: "paper/",
      state: count("paper", ".md") > 0 ? "begun" : "not begun",
      detail: "Written, checked and reviewed through Paperwright's desks.",
    },
  ];
}
