// What the site promises about its content: the home page shows the memo's own structure, links
// and citations resolve the way tools/check.py and tools/sync.py read them, and the page's port of
// the detection bound gives the model's number to the last bit or so.
import assert from "node:assert/strict";
import { existsSync, readFileSync } from "node:fs";
import { test } from "node:test";
import { loopGains, loopLimit, missAll, missOneChannel, weaponsGrade } from "../lib/detection.ts";
import { fmtProb } from "../lib/format.ts";
import { parseMemo } from "../lib/memo.ts";
import { docHref, docSlug, ledgerId, linkCitations, slugify } from "../lib/text.ts";

const root = new URL("../../", import.meta.url);
const read = (f: string) => readFileSync(new URL(f, root), "utf8");
const numbers = JSON.parse(read("data/numbers.json")) as Record<
  string,
  { value: number; display: string }
>;

test("the memo parses into its five perspectives, six definitions and five pathways", () => {
  const m = parseMemo(read("research/00-memo.md"));
  assert.deepEqual(
    m.perspectives.map((p) => p.name),
    [
      "Physical and energetic",
      "Computational and algorithmic",
      "Dynamical",
      "Cognitive and functional",
      "Organisational and economic",
    ],
  );
  assert.deepEqual(
    m.perspectives.flatMap((p) => p.mechanisms.map((x) => x.code)),
    [
      "P1",
      "P2",
      "P3",
      "P4",
      "A1",
      "A2",
      "A3",
      "A4",
      "A5",
      "Y1",
      "Y2",
      "Y3",
      "F1",
      "F2",
      "F3",
      "O1",
      "O2",
      "O3",
    ],
  );
  const p4 = m.perspectives[0]?.mechanisms[3];
  assert.equal(p4?.title, "Footprint, and its floor");
  assert.match(p4?.text ?? "", /footprint floor/);
  assert.deepEqual(
    m.definitions.map((d) => d.code),
    ["D1", "D2", "D3", "D4", "D5", "D6"],
  );
  assert.match(m.definitions[3]?.text ?? "", /T_b < m \* T_r/);
  assert.equal(m.pathways.header[0], "Pathway");
  assert.equal(m.pathways.rows.length, 5);
  assert.match(m.pathways.rows[0]?.[0] ?? "", /Recursive self-improvement/);
  assert.equal(m.protocol[0]?.title, "Who it binds");
  assert.ok(m.protocol.some((p) => /numbers\.md#miss-prob-one-channel/.test(p.text)));
  assert.equal(m.written, "2026-11-26");
});

test("ledger links, cross-links and anchors resolve as the repository's tools read them", () => {
  assert.equal(ledgerId("numbers.md#miss-prob-one-channel"), "miss-prob-one-channel");
  assert.equal(ledgerId("../research/numbers.md#breakout-years"), "breakout-years");
  assert.equal(ledgerId("https://example.org/numbers.md#x"), null);
  assert.equal(docHref("01-anatomy.md#p4"), "/research/anatomy#p4");
  assert.equal(docHref("../research/06-protocol.md"), "/research/protocol");
  assert.equal(docHref("numbers.md#x"), null);
  // From research/verification/, one level down: the ledger and documents are one level up.
  assert.equal(ledgerId("../numbers.md#e5-hazard"), "e5-hazard");
  assert.equal(docHref("../04-claims.md#c4-x"), "/research/claims#c4-x");
  assert.equal(docHref("verification/l4-red-team.md#c1"), "/verification/l4-red-team#c1");
  assert.equal(
    docHref("../verification/l1-prior-art-c1-c6.md"),
    "/verification/l1-prior-art-c1-c6",
  );
  assert.equal(docSlug("research/00-memo.md"), "memo");
  assert.equal(slugify("The protocol's shape"), "the-protocols-shape");
  assert.equal(slugify("D4 [line](numbers.md#x) *now*"), "d4-line-now");
});

test("citations become links to the source list, and ordinary links are left alone", () => {
  const label = (k: string) => k.toUpperCase();
  assert.equal(
    linkCitations("as shown [@shavit2023].", label),
    "as shown ([SHAVIT2023](/sources#shavit2023)).",
  );
  assert.equal(
    linkCitations("[see @ab; @b-2, p. 3]", label),
    "([AB](/sources#ab); [B-2](/sources#b-2))",
  );
  // An alias links to the key its work is listed under.
  assert.equal(
    linkCitations("[@old-key]", label, (k) => (k === "old-key" ? "newkey" : k)),
    "([OLD-KEY](/sources#newkey))",
  );
  assert.equal(
    linkCitations("[30%](numbers.md#x) and mail@example.org", label),
    "[30%](numbers.md#x) and mail@example.org",
  );
});

test("the detection bound port matches the model within a few ulps", () => {
  const got = missOneChannel(
    numbers["inspections-per-year"]?.value ?? Number.NaN,
    numbers["detect-prob-per-inspection"]?.value ?? Number.NaN,
    numbers["breakout-years"]?.value ?? Number.NaN,
  );
  // V8's Math.exp and Python's math.exp may differ in the last bit, so within a few ulps.
  const want = numbers["miss-prob-one-channel"]?.value ?? Number.NaN;
  assert.ok(Math.abs(got - want) <= 4 * Number.EPSILON * want, `${got} vs ${want}`);
  assert.equal(fmtProb(got), numbers["miss-prob-one-channel"]?.display);
  assert.equal(missAll(0.5, 3), 0.125);
});

test("the line and the loop behave as definitions D4 and D2 say", () => {
  assert.equal(weaponsGrade(10, 6, 2), true);
  assert.equal(weaponsGrade(12, 6, 2), false);
  assert.equal(loopLimit(0.8)?.toFixed(6), "5.000000");
  assert.equal(loopLimit(1), null);
  const sub = loopGains(0.5, 30);
  assert.ok((sub.at(-1)?.total ?? 0) < 2);
  const sup = loopGains(1.1, 30);
  assert.ok((sup.at(-1)?.total ?? 0) > 100);
  assert.equal(fmtProb(0.001), "1 in 1,000");
});

test("coupled loops: subcritical alone, supercritical together, and the radius matches power iteration", async () => {
  const { radiusUniform, spectralRadius, step, steadyLevel, uniformCoupling } = await import(
    "../lib/loops.ts"
  );
  // Five loops at 0.7 each, coupled at 0.05: 0.7 + 4 * 0.05 = 0.9, subcritical.
  assert.ok(Math.abs(radiusUniform(5, 0.7, 0.05) - 0.9) < 1e-12);
  // The same loops coupled at 0.1: 1.1, supercritical although each alone is 0.7.
  assert.ok(Math.abs(radiusUniform(5, 0.7, 0.1) - 1.1) < 1e-12);
  for (const [g, c] of [
    [0.7, 0.05],
    [0.7, 0.1],
    [0.4, 0.2],
  ] as const)
    assert.ok(Math.abs(spectralRadius(uniformCoupling(5, g, c)) - radiusUniform(5, g, c)) < 1e-9);
  // Iterated, a subcritical system settles at u / (1 - radius); a supercritical one hits the cap.
  const run = (g: number, c: number) => {
    let x = [0, 0, 0, 0, 0];
    const G = uniformCoupling(5, g, c);
    for (let k = 0; k < 400; k++) x = step(x, G, 0.12, 8);
    return x;
  };
  const settled = steadyLevel(0.9, 0.12) ?? Number.NaN;
  for (const v of run(0.7, 0.05)) assert.ok(Math.abs(v - settled) < 1e-6);
  for (const v of run(0.7, 0.1)) assert.equal(v, 8);
  assert.equal(steadyLevel(1.1, 0.12), null);
});

test("the pathways chapter's ranking table parses into the columns the home page shows", async () => {
  const { parseRanking, SHOWN } = await import("../lib/pathways.ts");
  const r = parseRanking(read("research/02-pathways.md"));
  assert.deepEqual(r.header, [...SHOWN]);
  assert.ok(r.rows.length >= 5, `only ${r.rows.length} pathways`);
  for (const row of r.rows) {
    assert.equal(row.length, SHOWN.length);
    assert.match(row[0] ?? "", /^\d/, `rank "${row[0]}" for ${row[1]}`);
    assert.ok((row[1] ?? "").length > 0);
  }
  // Every one of the memo's five keeps a rank from the memo; the rest are the ones Part I added.
  assert.equal(r.rows.length - r.added, 5);
  assert.throws(() => parseRanking("## The ranking\n\n| Pathway |\n|---|\n| x |\n"), /no column/);
});

test("the planned experiments are counted from the claims file's numbered list", async () => {
  const { plannedExperiments } = await import("../lib/text.ts");
  assert.equal(plannedExperiments(null), 11);
  const n = plannedExperiments(read("research/04-claims.md"));
  // E4 is listed twice (its CPU and GPU parts), so the count is of distinct codes.
  assert.ok(n >= 20 && n <= 30, `${n} experiments`);
  assert.equal(
    plannedExperiments("## Experiments\n\n1. **E1, a.** x\n2. **E4, b.** y\n3. **E4, c.** z\n"),
    2,
  );
});

test("the experiment plan parses from the claims file, every item with its claims", async () => {
  const { parseExperiments } = await import("../lib/experiments.ts");
  const plan = parseExperiments(read("research/04-claims.md"));
  const items = plan.flatMap((p) => p.items);
  assert.ok(plan.length >= 2, "at least the CPU and GPU phases");
  assert.deepEqual(
    items.map((e) => e.order),
    items.map((_, i) => i + 1),
    "numbered 1 to N in build order",
  );
  for (const e of items) {
    assert.match(e.code, /^E\d+$/);
    assert.ok(e.title.length > 3, `${e.code} has a title`);
    assert.ok(e.body.length > 20, `${e.code} says what it does`);
    assert.ok(e.serves.length > 0, `${e.code} says what it serves`);
    assert.ok(
      !/Browser:|`heavy`|`gpu`/.test(e.body),
      `${e.code}'s body ends before its particulars`,
    );
  }
  const e2 = items.find((e) => e.code === "E2");
  assert.equal(e2?.script, "e02_time_horizons");
  assert.equal(e2?.runner, "heavy");
  // A script named in the plan and a result file must agree on the name.
  assert.ok(existsSync(new URL("data/results/e02_time_horizons.json", root)));
  const sample = parseExperiments(
    "## Experiments\n\n**Phase 1: CPU.**\n\n1. **E9, returns.** r refitted from [@x].\n   `heavy`, minutes. `e09_returns`. C4, C6. Browser: yes.\n2. **E4, later parts.** (b) an agent.\n   `gpu`, weeks; needs E3. C4, C11. Browser: no.\n\n## Cut\n",
  );
  assert.deepEqual(
    sample[0]?.items.map((e) => [e.code, e.script, e.runner, e.time, e.serves, e.browser]),
    [
      ["E9", "e09_returns", "heavy", "minutes", "C4, C6", true],
      ["E4", null, "gpu", "weeks; needs E3", "C4, C11", false],
    ],
  );
});

test("every source gets a citation label naming a person or an organisation", async () => {
  const { citeLabel } = await import("../lib/text.ts");
  const { parse } = await import("smol-toml");
  const all = (parse(read("research/sources.toml")) as { source: Record<string, never> }).source;
  for (const [key, s] of Object.entries(all)) {
    const label = citeLabel(s, key);
    assert.doesNotMatch(label, /[()]|al\. et al\./, `${key}: ${label}`);
    assert.match(label, /(\d{4}|n\.d\.)$/, `${key} ends in its year: ${label}`);
  }
  const at = (authors: string) => citeLabel({ authors, year: 2026, title: "T" }, "k");
  assert.equal(at("Epoch AI"), "Epoch AI 2026");
  assert.equal(at("Gregory C. Allen (CSIS)"), "Allen 2026");
  assert.equal(at("Ryan Greenblatt et al."), "Greenblatt et al. 2026");
  assert.equal(at("Jakub Łucki, Boyi Wei, Yangsibo Huang"), "Łucki et al. 2026");
  assert.equal(at("Keller Jordan and contributors"), "Jordan et al. 2026");
  assert.equal(at("Donald A. Mahley, US Department of State"), "Mahley 2026");
  assert.equal(
    at("Bureau of Industry and Security, US Department of Commerce"),
    "Bureau of Industry and Security 2026",
  );
  assert.equal(at("Memphis Light, Gas and Water"), "Memphis Light, Gas and Water 2026");
  assert.equal(at("METR (Tom Cunningham, Nate Rush)"), "METR 2026");
  assert.equal(at("David Reber Jr. (NVIDIA)"), "Reber 2026");
});

test("the verification record parses, and a status outside the vocabulary fails", async () => {
  const { parseRecord } = await import("../lib/verification.ts");
  const table = (row: string) =>
    `# V\n\n## The record\n\n| Claim | L1 prior art | L2 proof | Standing |\n|---|---|---|---|\n${row}\n\n## Next\n`;
  const r = parseRecord(
    table(
      "| [C1, the line](04-claims.md#c1) | **prior work**: EASI | **proved under assumptions** | **application** |",
    ),
  );
  assert.deepEqual(r.levels, ["L1 prior art", "L2 proof"]);
  assert.equal(r.rows[0]?.code, "C1");
  assert.deepEqual(
    r.rows[0]?.levels.map((c) => [c.status, c.tone, c.detail]),
    [
      ["prior work", "fail", "EASI"],
      ["proved under assumptions", "partial", ""],
    ],
  );
  assert.equal(r.rows[0]?.standing.tone, "partial");
  assert.throws(
    () => parseRecord(table("| C2 | **fine** | **proved** | **application** |")),
    /not a status/,
  );
  assert.throws(
    () => parseRecord(table("| C2 | proved | **proved** | **application** |")),
    /bold status/,
  );
});
