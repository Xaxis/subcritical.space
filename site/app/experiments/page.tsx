import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { claimTitle } from "@/components/ClaimCards";
import { Markdown, Num } from "@/components/Markdown";
import { Page } from "@/components/Page";
import { experimentPlan, experimentResult, verificationRecord } from "@/lib/docs";
import type { Planned } from "@/lib/experiments";
import { entry } from "@/lib/ledger";
import { repoLink } from "@/lib/site";
import { capital, slugify } from "@/lib/text";
import type { VerificationRecord } from "@/lib/verification";

export const metadata: Metadata = {
  title: "Experiments",
  description:
    "The experiment plan from the claims file, in build order, with each finished experiment's results from the ledger and where the claims it serves stand.",
  alternates: { canonical: "/experiments" },
};

/** One anchor per item: E4's later parts share its code, so they take their place in the order. */
function anchor(e: Planned, seen: Set<string>): string {
  const base = e.code.toLowerCase();
  const id = seen.has(base) ? `${base}-${e.order}` : base;
  seen.add(base);
  return id;
}

/** Where each claim the experiment serves stands at level 3, the experiments, from the record. */
function Verdicts({ e, record }: { e: Planned; record: VerificationRecord | null }) {
  if (!record) return null;
  const l3 = record.levels.findIndex((l) => /^L3\b/.test(l));
  const codes = [...new Set(e.serves.match(/\bC\d+\b/g) ?? [])];
  const rows = codes.flatMap((c) => record.rows.filter((r) => r.code === c));
  if (l3 < 0 || rows.length === 0) return null;
  return (
    <div className="exp-verdicts">
      <p className="exp-label">Its claims at level 3, on all their experiments</p>
      <ul>
        {rows.map((r) => {
          const t = claimTitle(r);
          const c = r.levels[l3];
          if (!c) return null;
          return (
            <li key={r.code}>
              <span className="exp-claim">
                {t.href ? <a href={t.href}>{t.code}</a> : t.code} {t.name}
              </span>
              <span className={`v v-${c.tone}`}>{c.status}</span>
              {c.detail && (
                <span className="exp-verdict-detail">
                  <Markdown md={c.detail} inline />
                </span>
              )}
            </li>
          );
        })}
      </ul>
    </div>
  );
}

function Item({ e, id, record }: { e: Planned; id: string; record: VerificationRecord | null }) {
  const result = e.script ? experimentResult(e.script) : null;
  return (
    <li className={`exp${result ? " has-result" : ""}`} id={id}>
      <div className="exp-head">
        <span className="exp-code">{e.code}</span>
        <h3>{capital(e.title)}</h3>
        <span className={`exp-state ${result ? "state-ran" : "state-planned"}`}>
          {result ? "has results" : "planned"}
        </span>
      </div>
      <p className="exp-meta">
        {e.runner && (
          <span>
            {e.runner === "gpu" ? "GPU" : "CPU"}, {e.time}
          </span>
        )}
        {e.browser && <span>could run in a browser</span>}
        {e.serves && (
          <span>
            Serves <Markdown md={e.serves} inline />
          </span>
        )}
      </p>
      <Verdicts e={e} record={record} />
      <details className="exp-more">
        <summary>What it does</summary>
        <div className="exp-body">
          <Markdown md={e.body} />
        </div>
      </details>
      {result && (
        <details className="exp-more">
          <summary>All {result.ids.length} results, and how to rerun it</summary>
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
        </details>
      )}
    </li>
  );
}

export default function Experiments() {
  const plan = experimentPlan();
  if (!plan) notFound();
  const record = verificationRecord();
  const all = plan.flatMap((p) => p.items);
  const codes = new Set(all.map((e) => e.code));
  const hasResult = (e: Planned) => Boolean(e.script && experimentResult(e.script));
  const ran = new Set(all.filter(hasResult).map((e) => e.code));
  const seen = new Set<string>();
  const ids = new Map(plan.flatMap((p) => p.items).map((e) => [e, anchor(e, seen)] as const));
  return (
    <Page
      current="/experiments"
      eyebrow="Experiments"
      title="The experiments, and what they found"
      lead={
        <>
          <p>
            {ran.size} of {codes.size} planned experiments have run, each a script that fetches
            public data, records its checksum, takes its randomness from a fixed seed and writes one
            result file. A result that cuts against a claim is reported like one that supports it.
          </p>
          <p>
            The plan is read from <a href="/research/claims#experiments">the claims file</a>, and
            each result enters <a href="/numbers">the ledger</a> with the basis <em>experiment</em>,
            so a rerun on changed data shows.
          </p>
        </>
      }
    >
      <nav className="exp-map" aria-label="Every experiment">
        {plan.map((p) => (
          <div key={p.title} className="exp-map-phase">
            <p className="exp-label">
              <a href={`#${slugify(p.title)}`}>{p.title.replace(/:.*/, "")}</a>
              {": "}
              {capital(p.title.replace(/^Phase \d+: /, ""))}
            </p>
            <ol>
              {p.items.map((e) => (
                <li key={`${e.code}-${e.order}`}>
                  <a
                    href={`#${ids.get(e)}`}
                    className={`exp-chip ${hasResult(e) ? "state-ran" : "state-planned"}`}
                    title={`${e.code}, ${e.title}: ${hasResult(e) ? "has results" : "planned"}`}
                  >
                    {e.code}
                  </a>
                </li>
              ))}
            </ol>
          </div>
        ))}
        <p className="exp-map-key">
          <span className="exp-chip state-ran">has results</span>
          <span className="exp-chip state-planned">planned</span>
        </p>
      </nav>
      {plan.map((p) => (
        <section key={p.title} aria-labelledby={slugify(p.title)} className="exp-phase">
          <h2 id={slugify(p.title)}>{p.title}</h2>
          <ol className="exps">
            {p.items.map((e) => (
              <Item key={`${e.code}-${e.order}`} e={e} id={ids.get(e) ?? ""} record={record} />
            ))}
          </ol>
        </section>
      ))}
    </Page>
  );
}
