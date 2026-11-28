import type { Metadata } from "next";
import { LedgerFilter } from "@/components/LedgerFilter";
import { Page } from "@/components/Page";
import { BASES, type Entry, ledger } from "@/lib/ledger";
import { repoLink } from "@/lib/site";
import { capital } from "@/lib/text";

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

/** The file a number comes from, named for a reader: which part of the work, and what kind. */
function groupName(file: string): string {
  if (file === "data/inputs.toml") return "The memo's placeholders";
  const input = /^data\/inputs\/\d+-([a-z0-9-]+)\.toml$/.exec(file);
  if (input) return `${capital((input[1] as string).replace(/-/g, " "))}: inputs`;
  const part = /^model\/parts\/\d+_([a-z0-9_]+)\.py$/.exec(file);
  if (part) return `${capital((part[1] as string).replace(/_/g, " "))}: derived`;
  if (file.startsWith("model/")) return "Derived in the model";
  const result = /^data\/results\/e(\d+)_([a-z0-9_]+)\.json$/.exec(file);
  if (result)
    return `E${Number(result[1])}, ${(result[2] as string).replace(/_/g, " ")}: experiment`;
  return file;
}

function Row({ id, e, all }: { id: string; e: Entry; all: Record<string, Entry> }) {
  return (
    <details
      id={id}
      className={`lrow basis-${e.basis}`}
      data-basis={e.basis}
      data-q={`${id} ${e.label}`.toLowerCase()}
    >
      <summary>
        <code className="lrow-id">{id}</code>
        <span className="lrow-label">{e.label}</span>
        <span className="lrow-value mono">{e.display}</span>
      </summary>
      <dl className="meta">
        <dt>basis</dt>
        <dd>
          {e.basis}, {BASES[e.basis] ?? ""}
        </dd>
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
                  <a href={`#${i}`}>{i}</a> = {all[i]?.display}
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
              {e.date ? `, ${e.date}` : ""}
            </dd>
          </>
        )}
        {e.note && (
          <>
            <dt>note</dt>
            <dd>{e.note}</dd>
          </>
        )}
        <dt>defined in</dt>
        <dd>{definedAt(e.defined_in)}</dd>
      </dl>
    </details>
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
  // One group per file, in the ledger's order.
  const groups = new Map<string, string[]>();
  for (const id of ids) {
    const file = (L[id]?.defined_in ?? "").split("#")[0] ?? "";
    groups.set(file, [...(groups.get(file) ?? []), id]);
  }
  return (
    <Page
      current="/numbers"
      eyebrow="The ledger"
      title="Every number, and where it comes from"
      lead={
        <p>
          Each of the {ids.length.toLocaleString("en-US")} numbers is an input with a stated basis
          and source, or is computed from inputs by the model in the repository. The research links
          to these entries instead of typing numbers, and the check fails if any link shows a stale
          value. Open a row for its formula, its inputs and where it is defined.
        </p>
      }
    >
      <LedgerFilter
        total={ids.length}
        files={groups.size}
        bases={Object.keys(BASES).map((b) => ({
          basis: b,
          meaning: BASES[b] ?? "",
          count: counts[b] ?? 0,
        }))}
      />
      <div className="ledger">
        {[...groups].map(([file, members]) => (
          <details key={file} className="lgroup" data-group>
            <summary>
              <span className="lgroup-name">{groupName(file)}</span>
              <span className="lgroup-count mono">{members.length}</span>
              <code className="lgroup-file">{file}</code>
            </summary>
            <div className="lrows">
              {members.map((id) => {
                const e = L[id];
                return e ? <Row key={id} id={id} e={e} all={L} /> : null;
              })}
            </div>
          </details>
        ))}
      </div>
    </Page>
  );
}
