import { Footer } from "@/components/Footer";
import { DetectionBound } from "@/components/figures/DetectionBound";
import { LoopGain } from "@/components/figures/LoopGain";
import { TheLine } from "@/components/figures/TheLine";
import { Header } from "@/components/Header";
import { Markdown } from "@/components/Markdown";
import { memo } from "@/lib/docs";
import { entry } from "@/lib/ledger";
import { progress } from "@/lib/progress";
import { repoLink, SITE } from "@/lib/site";

export default function Home() {
  const m = memo();
  const def = (code: string) => m.definitions.find((d) => d.code === code);
  const d4 = def("D4");
  const steps = progress();
  const miss = entry("miss-prob-one-channel");
  const [lead, ...ideaRest] = m.idea.split("\n\n");

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
              run. The labels in the text are beliefs before the independent prior-art search.
            </p>
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
              A step shows as begun when its file exists in the{" "}
              <a href={SITE.repo} rel="noopener">
                repository
              </a>
              , so this list cannot claim more than has been written.
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
