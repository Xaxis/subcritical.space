// The ledger: every number Subcritical publishes, as `make model` wrote it to data/numbers.json.
// The site shows each number's `display` exactly as the model formatted it and never types one.
import "server-only";
import { readRepoFile } from "./repo";

export interface Entry {
  value: number;
  display: string;
  unit: string;
  basis: string;
  label: string;
  formula: string;
  inputs: string[];
  source: string;
  date: string;
  note: string;
  defined_in: string;
}

export type Ledger = Record<string, Entry>;

let cached: Ledger | null = null;

export function ledger(): Ledger {
  cached ??= JSON.parse(readRepoFile("data/numbers.json")) as Ledger;
  return cached;
}

export function entry(id: string): Entry {
  const e = ledger()[id];
  if (!e) throw new Error(`the ledger has no number ${id}; run make model`);
  return e;
}

/** What each basis means, from research/numbers.md. */
export const BASES: Record<string, string> = {
  measured: "an independent measurement",
  vendor: "a claim by an interested party",
  spec: "fixed by a protocol rule",
  design: "a choice this design makes",
  assumption: "a number picked where no source fixes it",
  modelled: "the output of a published model",
  experiment: "a result of this project's experiments, rerunnable from tools/exp/",
  derived: "computed from the others",
};
