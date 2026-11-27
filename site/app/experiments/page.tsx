import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { Markdown, Num } from "@/components/Markdown";
import { Page } from "@/components/Page";
import { experimentPlan, experimentResult } from "@/lib/docs";
import type { Planned } from "@/lib/experiments";
import { entry } from "@/lib/ledger";
import { repoLink } from "@/lib/site";
import { capital, slugify } from "@/lib/text";

export const metadata: Metadata = {
  title: "Experiments",
  description:
    "The experiment plan from the claims file, in build order, with each finished experiment's results from the ledger.",
  alternates: { canonical: "/experiments" },
};

/** One anchor per item: E4's later parts share its code, so they take their place in the order. */
function anchor(e: Planned, seen: Set<string>): string {
  const base = e.code.toLowerCase();
  const id = seen.has(base) ? `${base}-${e.order}` : base;
  seen.add(base);
  return id;
}

function Item({ e, id }: { e: Planned; id: string }) {
  const result = e.script ? experimentResult(e.script) : null;
  return (
    <li className={`exp card${result ? " has-result" : ""}`} id={id}>
      <h3>
        <span className="code">{e.code}</span>
        {capital(e.title)}
      </h3>
      <p className="exp-meta">
        <span className={`exp-state ${result ? "state-ran" : "state-planned"}`}>
          {result ? "has results" : "planned"}
        </span>
        {e.runner && (
          <span>
            {e.runner === "gpu" ? "GPU" : "CPU"}, {e.time}
          </span>
        )}
        {e.browser && <span>could run in a browser</span>}
      </p>
      <Markdown md={e.body} />
      {e.serves && (
        <p className="exp-serves">
          Serves: <Markdown md={e.serves} inline />.
        </p>
      )}
      {result && (
        <div className="exp-result">
          {/* biome-ignore lint/a11y/noNoninteractiveTabindex: a wide table scrolls, and a keyboard must reach it */}
          <div className="table-wrap" tabIndex={0}>
            <table>
              <thead>
                <tr>
                  <th scope="col">Result</th>
                  <th scope="col">What it is</th>
                </tr>
              </thead>
              <tbody>
                {result.ids.map((n) => (
                  <tr key={n}>
                    <td className="exp-value">
                      <Num id={n} />
                    </td>
                    <td>{entry(n).label}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <p className="exp-provenance">
            Data:{" "}
            {result.data.map((d, i) => (
              <span key={d.url}>
                {i > 0 && "; "}
                <a href={d.url} rel="noopener">
                  {d.what}
                </a>{" "}
                <span className="code" title={`sha256 ${d.sha256}`}>
                  sha256 {d.sha256.slice(0, 12)}
                </span>
              </span>
            ))}
            . Seed {result.seed}. Rerun:{" "}
            <a href={repoLink(result.script)} rel="noopener">
              <code>{result.script}</code>
            </a>
            , which writes{" "}
            <a href={repoLink(`data/results/${e.script}.json`)} rel="noopener">
              <code>data/results/{e.script}.json</code>
            </a>
            .
          </p>
        </div>
      )}
    </li>
  );
}

export default function Experiments() {
  const plan = experimentPlan();
  if (!plan) notFound();
  const all = plan.flatMap((p) => p.items);
  const codes = new Set(all.map((e) => e.code));
  const ran = new Set(all.filter((e) => e.script && experimentResult(e.script)).map((e) => e.code));
  const seen = new Set<string>();
  return (
    <Page
      current="/experiments"
      eyebrow="Experiments"
      title="The experiments, in build order"
      toc={plan.map((p) => ({
        id: slugify(p.title),
        text: capital(p.title.replace(/^Phase \d+: /, "")),
      }))}
      lead={
        <>
          <p>
            The one list of experiments, read from{" "}
            <a href="/research/claims#experiments">the claims file</a>, with the claims each one
            could cut. {ran.size} of {codes.size} have results so far.
          </p>
          <p>
            Each experiment is a script that fetches public data and records its checksum, takes its
            randomness from a fixed seed, and writes one result file. Its numbers enter{" "}
            <a href="/numbers">the ledger</a> with the basis <em>experiment</em>, so a rerun on
            changed data shows. A result that cuts against a claim is reported like one that
            supports it.
          </p>
        </>
      }
    >
      {plan.map((p) => (
        <section key={p.title} aria-labelledby={slugify(p.title)}>
          <h2 id={slugify(p.title)}>{p.title}</h2>
          <ol className="exps">
            {p.items.map((e) => (
              <Item key={`${e.code}-${e.order}`} e={e} id={anchor(e, seen)} />
            ))}
          </ol>
        </section>
      ))}
    </Page>
  );
}
