import { ClaimCards } from "@/components/ClaimCards";
import { Footer } from "@/components/Footer";
import { CoupledLoops } from "@/components/figures/CoupledLoops";
import { DetectionBound } from "@/components/figures/DetectionBound";
import { LoopGain } from "@/components/figures/LoopGain";
import { TheLine } from "@/components/figures/TheLine";
import { Header } from "@/components/Header";
import { Markdown } from "@/components/Markdown";
import { Stage } from "@/components/three/Stage";
import { VerificationGrid } from "@/components/VerificationGrid";
import { experimentPlan, experimentResult, ranking, verificationRecord } from "@/lib/docs";
import { entry, ledger } from "@/lib/ledger";
import { LOOPS } from "@/lib/loops";
import { progress } from "@/lib/progress";
import { repoLink, SITE } from "@/lib/site";
import { sourceIndex, sources } from "@/lib/sources";
import { capital, citeLabel } from "@/lib/text";

const WORDS = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"];
const word = (n: number) => WORDS[n] ?? String(n);
const thousands = (n: number) => n.toLocaleString("en-US");

/** A chapter's heading block: its number, its name, its title. */
function Kicker({ n, children }: { n: number; children: string }) {
  return (
    <p className="kicker">
      <span className="kicker-n">{String(n).padStart(2, "0")}</span>
      {children}
    </p>
  );
}

export default function Home() {
  const record = verificationRecord();
  const rows = record?.rows ?? [];
  const standing = (s: string) => rows.filter((r) => r.standing.status === s).length;
  // Levels no claim has been through yet: every cell in the column is still pending.
  const unrun = (record?.levels ?? []).filter((_, i) =>
    rows.every((r) => r.levels[i]?.status === "pending"),
  );
  const plan = (experimentPlan() ?? []).flatMap((p) => p.items);
  const planned = new Set(plan.map((e) => e.code)).size;
  const ran = new Set(plan.filter((e) => e.script && experimentResult(e.script)).map((e) => e.code))
    .size;
  const numbers = Object.keys(ledger()).length;
  const sourceCount = sources().length;
  const byKey = sourceIndex();
  const cite = (key: string) => ({
    href: `/sources#${byKey.get(key)?.key ?? key}`,
    label: citeLabel(byKey.get(key), key),
  });
  const miss = entry("miss-prob-one-channel");
  const ranked = ranking();
  const col = (name: string) => ranked?.header.indexOf(name) ?? -1;
  const steps = progress();

  return (
    <>
      <Header />
      <main id="main">
        <section className="hero on-dark" aria-labelledby="hero-title">
          <div className="wrap hero-grid">
            <div className="hero-text">
              <p className="kicker">
                <span className="kicker-n">Open research</span>begun {SITE.started}
              </p>
              <h1 id="hero-title">
                Prevent superintelligence. <span className="accent">Keep useful AI.</span>
              </h1>
              <p className="hero-dek">
                A protocol, worked out in the open, that would stop the development of
                superintelligence while useful AI keeps improving: the way a reactor runs
                subcritical, steady power and no runaway. Every number here is computed from a
                sourced input, and every claim is put through tests built to break it.
              </p>
              <p className="badge-row">
                <span className="badge">A design, not a result</span>
                <span>Nothing here is deployed or tested against a real adversary.</span>
              </p>
              <p className="actions">
                <a className="button primary" href="#findings">
                  What the tests found
                </a>
                <a className="button" href="/paper">
                  Read the paper
                </a>
              </p>
            </div>
            <Stage
              scene="loops"
              step={1}
              param={0.7}
              param2={0.05}
              className="stage-hero"
              label={`Five improvement loops, ${LOOPS.join(", ")}, drawn as rings of light on a dark stage, each feeding the others along arcs. Each loop's own gain is below 1 and the coupling is weak, so together they settle: subcritical.`}
            />
          </div>
          <div className="wrap">
            <ul className="stats">
              <li className="stat">
                <span className="stat-value">
                  {standing("contribution")} <small>of {rows.length}</small>
                </span>
                <span className="stat-label">claims have passed all six levels</span>
                <span className="stat-note">
                  {standing("candidate") === 0
                    ? "No claim is still a candidate"
                    : `${capital(word(standing("candidate")))} still standing as candidates`}
                  {unrun.length > 0
                    ? `; ${unrun.length === 1 ? "one level has" : `${word(unrun.length)} levels have`} yet to run`
                    : ""}
                  .
                </span>
              </li>
              <li className="stat">
                <span className="stat-value">
                  {ran} <small>of {planned}</small>
                </span>
                <span className="stat-label">experiments run on real data</span>
                <span className="stat-note">Each reruns from its script and seed.</span>
              </li>
              <li className="stat">
                <span className="stat-value">{thousands(numbers)}</span>
                <span className="stat-label">numbers, none typed by hand</span>
                <span className="stat-note">Each a sourced input, or computed from them.</span>
              </li>
              <li className="stat">
                <span className="stat-value">{thousands(sourceCount)}</span>
                <span className="stat-label">sources, each with an identifier</span>
                <span className="stat-note">Every citation resolves to one.</span>
              </li>
            </ul>
          </div>
        </section>

        <section className="chapter" id="line" aria-labelledby="line-title">
          <div className="wrap chapter-grid">
            <div className="chapter-text">
              <Kicker n={1}>The line</Kicker>
              <h2 id="line-title">Useful AI or weapons-grade, decided by time</h2>
              <p>
                A system, or a stock of chips and weights, is weapons-grade when it could break out
                to superintelligence faster than a regime could notice and respond, with a margin to
                spare. Everything slower stays useful AI, and may keep improving through gates that
                people hold.
              </p>
              <p>
                The idea is borrowed: nuclear safeguards judge diverted material by whether it would
                be caught in time. What the work adds is the arithmetic for AI, and the tests found
                its inputs cannot yet be measured well enough to draw the line for a real party. The
                frontier&apos;s rate of algorithmic progress is not identified from public data, and
                the historical record shows responses that wait on political decisions.
              </p>
              <p className="chapter-more">
                <a href="/research/claims">The line, claim by claim</a>
              </p>
            </div>
            <TheLine />
          </div>
        </section>

        <section className="chapter alt" id="loops" aria-labelledby="loops-title">
          <div className="wrap">
            <div className="chapter-grid">
              <div className="chapter-text">
                <Kicker n={2}>Why the name</Kicker>
                <h2 id="loops-title">Loops that are safe alone can run away together</h2>
                <p>
                  AI can improve itself through several loops at once: better algorithms, better
                  chips, money that buys compute, learning after deployment, and copying itself to
                  more machines. A loop whose gain is below 1 dies out, each round adding less than
                  the last.
                </p>
                <p>
                  But the loops feed each other, and the system as a whole runs away when its
                  combined gain reaches 1, even if every loop alone is below it. A subcritical
                  reactor still makes useful power. The protocol asks the same of AI: keep the
                  combined gain below 1, judged for all the loops together. No one can yet measure
                  that gain for a real system; the work sets out what measuring it would take.
                </p>
              </div>
              <LoopGain />
            </div>
            <div className="chapter-wide">
              <CoupledLoops cite={[cite("davidson2026feedback"), cite("burtsev2026criticality")]} />
            </div>
          </div>
        </section>

        <section className="chapter" id="channels" aria-labelledby="channels-title">
          <div className="wrap chapter-grid">
            <div className="chapter-text">
              <Kicker n={3}>Verification</Kicker>
              <h2 id="channels-title">No single party is trusted to check</h2>
              <p>
                A secret program has to hide from every channel at once: chip accounting, power and
                heat signatures, challenge inspections, hardware attestation and rewarded
                whistleblowers. Each misses on its own often enough to matter. Together, if they
                fail independently, they rarely all miss.
              </p>
              <p>
                That is a big if. An evader picks the path the channels share, so the protocol
                counts dependent channels as one. And the historical record of covert weapons
                programmes shows detection far slower than the placeholder rates assumed.
              </p>
              <p className="chapter-more">
                <a href="/research/protocol">The protocol, derived</a>
              </p>
            </div>
            <DetectionBound
              start={{
                inspections: entry("inspections-per-year").value,
                detect: entry("detect-prob-per-inspection").value,
                years: entry("breakout-years").value,
                display: miss.display,
              }}
              record={{
                hazard: entry("e5-hazard").display,
                hazardLo: entry("e5-hazard-lo").display,
                hazardHi: entry("e5-hazard-hi").display,
                placeholderRate: entry("org-memo-detect-rate").display,
              }}
            />
          </div>
        </section>

        {record && (
          <section className="chapter alt" id="findings" aria-labelledby="findings-title">
            <div className="wrap">
              <Kicker n={4}>What the tests found</Kicker>
              <h2 id="findings-title">Each claim, put through six levels built to break it</h2>
              <p className="chapter-lead">
                A claim counts as a contribution only after it passes all six: a prior-art search by
                a helper who did not propose it, a proof, experiments on real data, a red team, the
                integrity and review desks, and a fresh reviewer. A claim that fails a level is cut
                or downgraded, never argued around. Of the {word(rows.length)} claims,{" "}
                {standing("contribution") === 0
                  ? "none has passed all six yet"
                  : `${word(standing("contribution"))} passed all six`}
                {unrun.length > 0 &&
                  `, and ${unrun.length === 1 ? "one level" : `${word(unrun.length)} levels`} (${unrun.join(", ")}) ${unrun.length === 1 ? "has" : "have"} not run`}
                .
              </p>
              <ClaimCards record={record} />
              <details className="grid-details">
                <summary>Every claim, level by level</summary>
                <VerificationGrid record={record} />
                <p className="chapter-more">
                  <a href="/research/verification">The verification record says why</a>
                </p>
              </details>
            </div>
          </section>
        )}

        {ranked && (
          <section className="chapter" id="pathways" aria-labelledby="pathways-title">
            <div className="wrap chapter-grid">
              <div className="chapter-text">
                <Kicker n={5}>Which systems cross the line</Kicker>
                <h2 id="pathways-title">{`${capital(word(ranked.rows.length))} pathways, ranked by evidence`}</h2>
                <p>
                  The ranking sets which limits the protocol puts first. The evidence fixes only
                  part of the order, and not its top; the rest is judgement, and pathways it cannot
                  separate share a rank.
                </p>
                <p className="chapter-more">
                  <a href="/research/pathways">The evidence for each pathway</a>
                </p>
              </div>
              <ol className="ranked">
                {ranked.rows.map((r) => (
                  <li key={r[col("Pathway")]}>
                    <span className="ranked-n">
                      {(r[col("Rank now")] ?? "").replace(/\s*\(tied\)/, "")}
                    </span>
                    <div>
                      <p className="ranked-name">
                        <Markdown md={r[col("Pathway")] ?? ""} inline />
                        {/\(tied\)/.test(r[col("Rank now")] ?? "") && (
                          <span className="ranked-tied">tied</span>
                        )}
                      </p>
                      <p className="ranked-meta">
                        <span>Seen by</span>{" "}
                        <Markdown md={r[col("The channel that sees it")] ?? ""} inline />
                      </p>
                      <p className="ranked-meta">
                        <span>Cost of a limit</span>{" "}
                        <Markdown md={r[col("Cost of a limit to useful AI")] ?? ""} inline />
                      </p>
                    </div>
                  </li>
                ))}
              </ol>
            </div>
          </section>
        )}

        <section className="chapter alt" id="progress" aria-labelledby="progress-title">
          <div className="wrap">
            <Kicker n={6}>Where the work stands</Kicker>
            <h2 id="progress-title">Everything is open, down to the numbers</h2>
            <p className="chapter-lead">
              Each step shows as written once its file exists in the{" "}
              <a href={SITE.repo} rel="noopener">
                repository
              </a>
              , so this list cannot claim more than has been written. Written is not verified.
            </p>
            <ul className="step-cards">
              {steps.map((s) => (
                <li key={s.name} className={`step-card state-${s.state.replace(" ", "-")}`}>
                  {s.state === "not begun" ? (
                    <div className="step-inner">
                      <span className="step-state">{s.state}</span>
                      <span className="step-name">{s.name}</span>
                      <span className="step-detail">{s.detail}</span>
                    </div>
                  ) : (
                    <a
                      className="step-inner"
                      href={s.href ?? repoLink(s.where)}
                      rel={s.href ? undefined : "noopener"}
                    >
                      <span className="step-state">{s.state}</span>
                      <span className="step-name">{s.name}</span>
                      <span className="step-detail">{s.detail}</span>
                    </a>
                  )}
                </li>
              ))}
            </ul>
          </div>
        </section>
      </main>
      <Footer />
    </>
  );
}
