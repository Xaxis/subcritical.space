// What the site promises about its content: the home page shows the memo's own structure, links
// and citations resolve the way tools/check.py and tools/sync.py read them, and the page's port of
// the detection bound gives the model's number to the last bit or so.
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
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
  assert.equal(
    linkCitations("[30%](numbers.md#x) and mail@example.org", label),
    "[30%](numbers.md#x) and mail@example.org",
  );
});

test("the detection bound port equals the model's number exactly", () => {
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
