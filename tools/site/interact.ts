// What the home page's figures and the theme toggle must do in a real browser (tools/site/deploy.sh
// runs it on the live site; run it on a local server before a deploy):
//   - the loop gain turns supercritical above 1 and back below it, and its bars change;
//   - the line turns weapons-grade when breakout drops under margin x response;
//   - the detection bound counts channels, and at the ledger's inputs shows the ledger's number;
//   - the coupled loops' 3D stage draws, turns supercritical together when the coupling pushes the
//     combined gain past 1 though each loop alone is below it, changes its picture, and pauses;
//     under reduced motion it holds a still frame with no pause button, and without WebGL it says
//     in words what it would show;
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
    ledgerShown !== "" && start.includes(`misses it: ${ledgerShown}`),
    "detection bound shows the ledger's number",
  );
  await page.locator(`${detect} input[type=range]`).nth(3).fill("3");
  expect(
    (await caption(page, detect)).startsWith("All 3 channels miss it"),
    "detection bound counts 3 channels",
  );

  // The coupled loops in 3D.
  const loops = "figure.loops3d";
  const stage = page.locator(`${loops} .stage`);
  await stage.evaluate((el) => el.scrollIntoView({ block: "center" }));
  await page
    .waitForFunction(
      () => document.querySelector("figure.loops3d .stage")?.getAttribute("data-status") !== "idle",
      null,
      { timeout: 60_000 },
    )
    .catch(() => {});
  expect(
    (await stage.getAttribute("data-status")) === "ready" &&
      (await stage.locator("canvas").count()) === 1,
    `the coupled loops' WebGL stage is drawing (${await stage.getAttribute("data-status")})`,
  );
  expect(
    (await caption(page, loops)).startsWith("Subcritical together."),
    "coupled loops start subcritical together",
  );
  const pause = stage.getByRole("button", { name: "Pause the animation" });
  await pause.click();
  expect((await pause.getAttribute("aria-pressed")) === "true", "the stage's pause button pauses");
  await page.waitForTimeout(500);
  const subShot = await stage.screenshot();
  // A flat stage compresses to almost nothing; rings, links and glow do not.
  expect(subShot.length > 15_000, `the stage draws a picture (${subShot.length} bytes of PNG)`);
  await page.locator(`${loops} input[type=range]`).nth(1).fill("0.1");
  const together = await caption(page, loops);
  expect(
    together.startsWith("Supercritical together.") && /although none would alone/.test(together),
    "loops each below 1 run away together at c = 0.1",
  );
  await page.waitForTimeout(800);
  expect(
    !subShot.equals(await stage.screenshot()),
    "the paused stage redraws when the model goes supercritical",
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

  // Reduced motion: a still frame, so no pause button.
  const still = await browser.newContext({
    viewport: { width: 1280, height: 900 },
    reducedMotion: "reduce",
  });
  const sp = await still.newPage();
  await sp.goto(`${base}/`, { waitUntil: "networkidle" });
  const sStage = sp.locator("figure.loops3d .stage");
  await sStage.evaluate((el) => el.scrollIntoView({ block: "center" }));
  await sp
    .waitForFunction(
      () => document.querySelector("figure.loops3d .stage")?.getAttribute("data-status") !== "idle",
      null,
      { timeout: 60_000 },
    )
    .catch(() => {});
  expect(
    (await sStage.getAttribute("data-status")) === "ready" &&
      (await sStage.locator(".stage-pause").count()) === 0,
    "under reduced motion the stage holds a still frame with no pause button",
  );
  await still.close();
} finally {
  await browser.close();
}

// Without WebGL the stage says in words what it would show.
const plain = await chromium.launch({
  headless: true,
  args: [...CHROMIUM_ARGS, "--disable-webgl", "--disable-3d-apis"],
});
try {
  const page = await plain.newPage({ viewport: { width: 1280, height: 900 } });
  await page.goto(`${base}/`, { waitUntil: "networkidle" });
  const stage = page.locator("figure.loops3d .stage");
  await stage.evaluate((el) => el.scrollIntoView({ block: "center" }));
  await page
    .waitForFunction(
      () =>
        document.querySelector("figure.loops3d .stage")?.getAttribute("data-status") === "failed",
      null,
      { timeout: 30_000 },
    )
    .catch(() => {});
  const words = (await stage.locator(".stage-fallback").textContent()) ?? "";
  expect(
    words.startsWith("Five improvement loops"),
    "without WebGL the stage describes the loops in words",
  );
} finally {
  await plain.close();
}
for (const p of passed) console.log(`  ok  ${p}`);
for (const p of problems) console.error(`interact: ${p}`);
process.exit(problems.length === 0 ? 0 : 1);
