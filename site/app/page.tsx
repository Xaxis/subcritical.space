import { Footer } from "@/components/Footer";
import { CoupledLoops } from "@/components/figures/CoupledLoops";
import { DetectionBound } from "@/components/figures/DetectionBound";
import { LoopGain } from "@/components/figures/LoopGain";
import { TheLine } from "@/components/figures/TheLine";
import { Header } from "@/components/Header";
import { Markdown } from "@/components/Markdown";
import { memo, ranking } from "@/lib/docs";
import { entry } from "@/lib/ledger";
import { progress } from "@/lib/progress";
import { repoFileExists } from "@/lib/repo";
import { repoLink, SITE } from "@/lib/site";
import { citeLabel, sourceIndex } from "@/lib/sources";

const WORDS = [
  "none",
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
  "ten",
];
const capital = (w: string) => w.charAt(0).toUpperCase() + w.slice(1);

export default function Home() {
  const m = memo();
  const def = (code: string) => m.definitions.find((d) => d.code === code);
  const d4 = def("D4");
  const steps = progress();
  const miss = entry("miss-prob-one-channel");
  const [lead, ...ideaRest] = m.idea.split("\n\n");
  const ranked = ranking();
  const byKey = sourceIndex();
  const cite = (key: string) => ({
    href: `/sources#${byKey.get(key)?.key ?? key}`,
    label: citeLabel(byKey.get(key), key),
  });
  const novelty = repoFileExists("research/03-novelty.md");
  const revised = (
    <p className="revised">
      These are the memo&apos;s words, written before the survey. The survey has since found prior
      work for several of them, including the line (D4), the loop gain (D2) and the comparison
      against organisations (D1).{" "}
      {novelty ? (
        <a href="/research/novelty">The novelty file</a>
      ) : (
        <a href="/research#survey">The survey notes</a>
      )}{" "}
      says what remains ours.
    </p>
  );

  return (
    <>
      <Header />
      <main id="main">
        <section className="hero">
          <div className="wrap hero-grid">
            <div className="hero-text">
              <p className="eyebrow">An open research program, begun {SITE.started}</p>
              <h1>
                Prevent superintelligence.
                <br />
                <span className="accent">Keep useful AI.</span>
              </h1>
              <div className="lead">
                <Markdown md={lead ?? ""} />
              </div>
              {ideaRest.length > 0 && <Markdown md={ideaRest.join("\n\n")} />}
              <p className="status-note">
                A design and a research plan. Nothing here is deployed or tested against a real
                adversary, and every definition below is a candidate until it passes six independent
                checks.
              </p>
              <p className="actions">
                <a className="button primary" href="/research/memo">
                  Read the memo
                </a>
                <a className="button" href="#progress">
                  Where the work stands
                </a>
              </p>
            </div>
            <div className="hero-figure">
              <LoopGain />
            </div>
          </div>
        </section>

        <section className="band" id="line">
          <div className="wrap two-col">
            <div>
              <p className="eyebrow">The line</p>
              <h2>Useful AI or weapons-grade, decided by time</h2>
              {d4 && (
                <p>
                  <strong>
                    {d4.code}. {d4.title}.
                  </strong>{" "}
                  <Markdown md={d4.text} inline />
                </p>
              )}
              <p className="muted">
                Breakout time (D3) comes from measured inputs: compute, algorithmic efficiency and
                the loop gain (D2). The response time is the protocol&apos;s own detection
                guarantee. So the line is tied to what the regime can actually see.
              </p>
            </div>
            <TheLine />
          </div>
        </section>

        <section className="band" id="loops">
          <div className="wrap two-col">
            <div>
              <p className="eyebrow">Why the name</p>
              <h2>Loops that are safe alone can run away together</h2>
              <p>
                AI can improve itself through several loops at once: better algorithms, better
                chips, money that buys compute, learning after deployment, and copying itself to
                more machines. Each loop on its own may die out, every round adding less than the
                last. But each also feeds the others, and the system as a whole runs away when its
                combined gain, the spectral radius, reaches 1.
              </p>
              <p>
                A subcritical reactor still makes useful power. The protocol asks the same of AI:
                useful systems that keep improving, with the combined gain of every loop held below
                1 and measured, not one loop at a time.
              </p>
            </div>
            <CoupledLoops cite={[cite("davidson2026feedback"), cite("burtsev2026criticality")]} />
          </div>
        </section>

        <section className="band alt" id="anatomy">
          <div className="wrap">
            <p className="eyebrow">Part I, the centre of the work</p>
            <h2>How superintelligence forms, from five perspectives</h2>
            <p className="section-lead">
              About half the research defines what superintelligence is and the mechanisms that form
              it. Each gets a precise definition, a measurement, and the evidence for and against.
              The protocol then limits them one by one. These are the memo&apos;s candidates, before
              the survey.
            </p>
            <div className="perspectives">
              {m.perspectives.map((p) => (
                <article key={p.name} className="card perspective">
                  <h3>{p.name}</h3>
                  <ul>
                    {p.mechanisms.map((mech) => (
                      <li key={mech.code}>
                        <details>
                          <summary>
                            <span className="code">{mech.code}</span> {mech.title}
                          </summary>
                          <p>
                            <Markdown md={mech.text} inline />
                          </p>
                        </details>
                      </li>
                    ))}
                  </ul>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section className="band" id="definitions">
          <div className="wrap">
            <p className="eyebrow">Candidate definitions</p>
            <h2>Six definitions a protocol can trigger on</h2>
            <p className="section-lead">
              Each must be new or clearly improve on existing ones, and come with a test that can be
              run.
            </p>
            {revised}
            <div className="definitions">
              {m.definitions.map((d) => (
                <article key={d.code} className="card definition" id={d.code.toLowerCase()}>
                  <h3>
                    <span className="code">{d.code}</span> {d.title}
                  </h3>
                  <p>
                    <Markdown md={d.text} inline />
                  </p>
                </article>
              ))}
            </div>
            <div className="strongest card">
              <h3>What looks strongest now</h3>
              <Markdown md={m.strongest} />
            </div>
          </div>
        </section>

        <section className="band alt" id="pathways">
          <div className="wrap">
            <p className="eyebrow">Which systems cross the line</p>
            {ranked ? (
              <>
                <h2>{`${capital(WORDS[ranked.rows.length] ?? String(ranked.rows.length))} pathways, ranked on the evidence`}</h2>
                <p className="section-lead">
                  Part I re-ranked the memo&apos;s pathways on the survey&apos;s evidence
                  {ranked.added > 0 ? ` and added ${WORDS[ranked.added] ?? ranked.added}` : ""}.
                  Pathways the evidence cannot separate share a rank. Provisional until the
                  experiments run; the ranking decides what the protocol restricts, meters or
                  watches.
                </p>
                {/* biome-ignore lint/a11y/noNoninteractiveTabindex: a wide table scrolls, and a keyboard must reach it */}
                <div className="table-wrap" tabIndex={0}>
                  <table>
                    <thead>
                      <tr>
                        {ranked.header.map((h) => (
                          <th key={h} scope="col">
                            {h}
                          </th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {ranked.rows.map((r) => (
                        <tr key={r[1]}>
                          {r.map((c, i) =>
                            i === 1 ? (
                              <th key={ranked.header[i]} scope="row">
                                <Markdown md={c} inline />
                              </th>
                            ) : (
                              <td key={ranked.header[i]}>
                                <Markdown md={c} inline />
                              </td>
                            ),
                          )}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
                <p className="prose narrow">
                  The evidence for each, what moved it and the weakest judgements:{" "}
                  <a href="/research/pathways">the pathways chapter</a>.
                </p>
                <details className="before">
                  <summary>The memo&apos;s ranking, before the survey</summary>
                  {/* biome-ignore lint/a11y/noNoninteractiveTabindex: a wide table scrolls, and a keyboard must reach it */}
                  <div className="table-wrap" tabIndex={0}>
                    <table>
                      <thead>
                        <tr>
                          {m.pathways.header.map((h) => (
                            <th key={h} scope="col">
                              {h}
                            </th>
                          ))}
                        </tr>
                      </thead>
                      <tbody>
                        {m.pathways.rows.map((r) => (
                          <tr key={r[0]}>
                            {r.map((c, i) =>
                              i === 0 ? (
                                <th key={m.pathways.header[i]} scope="row">
                                  {c}
                                </th>
                              ) : (
                                <td key={m.pathways.header[i]}>{c}</td>
                              ),
                            )}
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                  <div className="prose narrow">
                    <Markdown md={m.pathways.reasons} />
                  </div>
                </details>
              </>
            ) : (
              <>
                <h2>Five candidate pathways, ranked before testing</h2>
                <p className="section-lead">
                  Candidates to test, not conclusions. The survey and experiments decide the final
                  ranking, and the ranking decides what the protocol restricts.
                </p>
                {/* biome-ignore lint/a11y/noNoninteractiveTabindex: a wide table scrolls, and a keyboard must reach it */}
                <div className="table-wrap" tabIndex={0}>
                  <table>
                    <thead>
                      <tr>
                        {m.pathways.header.map((h) => (
                          <th key={h} scope="col">
                            {h}
                          </th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {m.pathways.rows.map((r) => (
                        <tr key={r[0]}>
                          {r.map((c, i) =>
                            i === 0 ? (
                              <th key={m.pathways.header[i]} scope="row">
                                {c}
                              </th>
                            ) : (
                              <td key={m.pathways.header[i]}>{c}</td>
                            ),
                          )}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
                <div className="prose narrow">
                  <Markdown md={m.pathways.reasons} />
                </div>
              </>
            )}
          </div>
        </section>

        <section className="band" id="protocol">
          <div className="wrap">
            <p className="eyebrow">Part II</p>
            <h2>The protocol&apos;s shape</h2>
            <p className="section-lead">
              Nuclear safeguards do not ban fission; they separate the material that runs reactors
              from the material that makes weapons. The protocol tries the same for AI, with no
              single party trusted to check.
            </p>
            <div className="two-col">
              <ol className="planks">
                {m.protocol.map((p) => (
                  <li key={p.title}>
                    <strong>{p.title}.</strong> <Markdown md={p.text} inline />
                  </li>
                ))}
              </ol>
              <div>
                <h3 className="figure-title">Why several channels</h3>
                <DetectionBound
                  start={{
                    inspections: entry("inspections-per-year").value,
                    detect: entry("detect-prob-per-inspection").value,
                    years: entry("breakout-years").value,
                    display: miss.display,
                  }}
                  record={{
                    median: entry("org-covert-years-median").display,
                    hazard: entry("org-covert-hazard").display,
                    placeholderRate: entry("org-memo-detect-rate").display,
                  }}
                />
              </div>
            </div>
          </div>
        </section>

        <section className="band alt" id="progress">
          <div className="wrap">
            <p className="eyebrow">Where the work stands</p>
            <h2>The plan, read from the repository</h2>
            <p className="section-lead">
              A step shows as written when its file exists in the{" "}
              <a href={SITE.repo} rel="noopener">
                repository
              </a>
              , so this list cannot claim more than has been written. Written is not verified: each
              claim still has to pass six independent levels.
            </p>
            <ol className="steps">
              {steps.map((s) => (
                <li key={s.name} className={`step state-${s.state.replace(" ", "-")}`}>
                  <span className="step-state">{s.state}</span>
                  <span className="step-name">
                    {s.state === "not begun" ? (
                      s.name
                    ) : (
                      <a href={repoLink(s.where)} rel="noopener">
                        {s.name}
                      </a>
                    )}
                  </span>
                  <span className="step-detail">{s.detail}</span>
                </li>
              ))}
            </ol>
          </div>
        </section>
      </main>
      <Footer />
    </>
  );
}
