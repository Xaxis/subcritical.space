// What the home page's figures and the theme toggle must do in a real browser (tools/site/deploy.sh
// runs it on the live site; run it on a local server before a deploy):
//   - the loop gain turns supercritical above 1 and back below it, and its bars change;
//   - the line turns weapons-grade when breakout drops under margin x response;
//   - the detection bound counts channels, and at the ledger's inputs shows the ledger's number;
//   - the theme toggle flips the theme, and the choice survives a reload;
//   - no page error and nothing the Content-Security-Policy refuses.
//
//   ~/.claude/claude-core/bin/heavy node tools/site/interact.ts --url URL
import { parseArgs } from "node:util";
import { chromium, type Page } from "playwright-core";
import { CHROMIUM_ARGS } from "../lib/chromium.ts";

const { values } = parseArgs({ options: { url: { type: "string" } } });
if (values.url === undefined) {
  console.error("usage: node tools/site/interact.ts --url URL");
  process.exit(2);
}
const base = values.url.replace(/\/$/, "");
const problems: string[] = [];
const passed: string[] = [];

function expect(ok: boolean, what: string) {
  (ok ? passed : problems).push(what);
}

async function caption(page: Page, figure: string): Promise<string> {
  return ((await page.locator(`${figure} figcaption`).textContent()) ?? "").replace(/\s+/g, " ");
}

const browser = await chromium.launch({ headless: true, args: CHROMIUM_ARGS });
try {
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await context.newPage();
  page.on("pageerror", (e) => problems.push(`page error: ${e.message}`));
  page.on("console", (m) => {
    if (m.type() === "error") problems.push(`console error: ${m.text().slice(0, 300)}`);
  });
  await page.goto(`${base}/`, { waitUntil: "networkidle" });

  // The loop gain.
  const loop = "figure.loop";
  const bars = async () =>
    page
      .locator(`${loop} .bar-gain`)
      .evaluateAll((els) => els.map((e) => e.getAttribute("height")));
  const before = await bars();
  expect((await caption(page, loop)).startsWith("Subcritical."), "loop gain starts subcritical");
  await page.locator(`${loop} input[type=range]`).fill("1.1");
  expect(
    (await caption(page, loop)).startsWith("Supercritical."),
    "loop gain at 1.10 is supercritical",
  );
  expect(JSON.stringify(await bars()) !== JSON.stringify(before), "loop gain bars change with g");
  expect(
    (await page.locator(`${loop} .bar-over`).count()) > 0,
    "supercritical bars run off the chart",
  );
  await page.locator(`${loop} input[type=range]`).fill("0.9");
  const sub = await caption(page, loop);
  expect(
    sub.startsWith("Subcritical.") && /never pass 10\.0/.test(sub),
    "loop gain at 0.90 has ceiling 10",
  );

  // The line.
  const line = "figure.line";
  expect(
    (await caption(page, line)).startsWith("Useful AI."),
    "the line starts on the useful side",
  );
  await page.locator(`${line} input[type=range]`).first().fill("6");
  expect(
    (await caption(page, line)).startsWith("Weapons-grade."),
    "a 6-month breakout is weapons-grade",
  );

  // The detection bound.
  const detect = "figure.detect";
  const start = await caption(page, detect);
  const ledgerLink = page.locator(`${detect} a[href="/numbers#miss-prob-one-channel"]`);
  const ledgerShown =
    (await ledgerLink.count()) > 0 ? ((await ledgerLink.textContent()) ?? "") : "";
  expect(
    ledgerShown !== "" && start.includes(`miss it: ${ledgerShown}`),
    "detection bound shows the ledger's number",
  );
  await page.locator(`${detect} input[type=range]`).nth(3).fill("3");
  expect(
    (await caption(page, detect)).startsWith("All 3 channels miss it"),
    "detection bound counts 3 channels",
  );

  // The theme.
  const theme = () => page.evaluate(() => document.documentElement.dataset.theme ?? "");
  const was = await theme();
  await page.locator(".site-header .icon-button").click();
  const now = await theme();
  expect(
    now !== was && (now === "dark" || now === "light"),
    `theme toggles (${was || "device"} to ${now})`,
  );
  await page.reload({ waitUntil: "networkidle" });
  expect((await theme()) === now, "the chosen theme survives a reload");

  // The research page renders the memo with ledger numbers as links.
  await page.goto(`${base}/research/memo`, { waitUntil: "networkidle" });
  const num = page.locator('a.num[href="/numbers#miss-prob-one-channel"]');
  expect((await num.count()) > 0, "the memo shows its ledger number as a link to the ledger");
  await context.close();
} finally {
  await browser.close();
}
for (const p of passed) console.log(`  ok  ${p}`);
for (const p of problems) console.error(`interact: ${p}`);
process.exit(problems.length === 0 ? 0 : 1);
