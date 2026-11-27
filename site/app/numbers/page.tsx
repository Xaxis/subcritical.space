import type { Metadata } from "next";
import { Page } from "@/components/Page";
import { BASES, ledger } from "@/lib/ledger";
import { repoLink } from "@/lib/site";

export const metadata: Metadata = {
  title: "Numbers",
  description:
    "The ledger: every number Subcritical publishes, with its basis, its formula and where it is defined.",
  alternates: { canonical: "/numbers" },
};

/** "model/subcritical.py#L46" as a link to that line on GitHub. */
function definedAt(where: string) {
  const [file, line] = where.split("#L");
  return (
    <a href={repoLink(file ?? where, line ? Number(line) : undefined)} rel="noopener">
      <code>{where}</code>
    </a>
  );
}

export default function Numbers() {
  const L = ledger();
  const ids = Object.keys(L);
  const counts = ids.reduce<Record<string, number>>((acc, id) => {
    const b = L[id]?.basis ?? "";
    acc[b] = (acc[b] ?? 0) + 1;
    return acc;
  }, {});
  return (
    <Page
      current="/numbers"
      eyebrow="The ledger"
      title="Every number, and where it comes from"
      lead={
        <p>
          Each number is an input with a stated basis, or is derived from inputs by the model in the
          repository. Documents link to these entries instead of typing numbers, and the check fails
          if any link shows a stale value.
        </p>
      }
    >
      <dl className="bases">
        {Object.entries(BASES).map(([b, meaning]) => (
          <div key={b} className={`basis basis-${b}`}>
            <dt>
              {b} <span className="count">{counts[b] ?? 0}</span>
            </dt>
            <dd>{meaning}</dd>
          </div>
        ))}
      </dl>
      <p className="callout">
        So far the ledger holds only the memo&apos;s placeholder inputs for the detection bound, all
        of basis <em>assumption</em>. The survey replaces them with sourced values, and the
        experiments add measured ones.
      </p>
      <div className="ledger">
        {ids.map((id) => {
          const e = L[id];
          if (!e) return null;
          return (
            <article key={id} id={id} className={`card entry basis-${e.basis}`}>
              <header>
                <h2>
                  <a href={`#${id}`}>{id}</a>
                </h2>
                <span className="value mono">{e.display}</span>
              </header>
              <p>{e.label}</p>
              <dl className="meta">
                <dt>basis</dt>
                <dd>{e.basis}</dd>
                {e.formula && (
                  <>
                    <dt>formula</dt>
                    <dd>
                      <code>{e.formula}</code>
                    </dd>
                  </>
                )}
                {e.inputs.length > 0 && (
                  <>
                    <dt>inputs</dt>
                    <dd>
                      {e.inputs.map((i, k) => (
                        <span key={i}>
                          {k > 0 && ", "}
                          <a href={`#${i}`}>{i}</a> = {L[i]?.display}
                        </span>
                      ))}
                    </dd>
                  </>
                )}
                {e.source && (
                  <>
                    <dt>source</dt>
                    <dd>
                      <a href={`/sources#${e.source}`}>{e.source}</a>
                    </dd>
                  </>
                )}
                <dt>defined in</dt>
                <dd>{definedAt(e.defined_in)}</dd>
              </dl>
            </article>
          );
        })}
      </div>
    </Page>
  );
}
