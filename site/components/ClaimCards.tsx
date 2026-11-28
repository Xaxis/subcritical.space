// Where each claim stands, as cards grouped by standing: the claim, what the standing says, what the
// experiments found, and a mark per level. Read from research/07-verification.md like the grid, so a
// card can never say more than the record does. Every mark has its status in words for a reader who
// cannot see the shapes, and the shapes differ, so colour is never the only signal.
import { Markdown } from "@/components/Markdown";
import { capital, docHref } from "@/lib/text";
import type { Row, VerificationRecord } from "@/lib/verification";

const GROUPS = [
  ["contribution", "Contributions", "Passed all six levels."],
  ["candidate", "Still candidates", "Standing, with levels still to run."],
  ["downgraded", "Downgraded", "A level narrowed the claim to something smaller."],
  [
    "application",
    "Credited to prior work",
    "The method exists already; its use on AI is what is here.",
  ],
  ["cut", "Cut", "Failed a level."],
] as const;

/** "[C1, the line](04-claims.md#...)" as its code, its name and the page it links to. */
export function claimTitle(row: Row): { code: string; name: string; href: string | null } {
  const m = /^\[([^\]]+)\]\(([^)]+)\)$/.exec(row.claim.trim());
  const text = m ? (m[1] as string) : row.claim;
  const name = text.replace(/^C\d+,\s*/, "");
  return { code: row.code, name: capital(name), href: m ? docHref(m[2] as string) : null };
}

function Card({ row, levels }: { row: Row; levels: string[] }) {
  const t = claimTitle(row);
  const l3 = levels.findIndex((l) => /^L3\b/.test(l));
  const found = l3 >= 0 ? row.levels[l3] : undefined;
  return (
    <li className={`claim tone-${row.standing.tone}`}>
      <h4 className="claim-title">
        <span className="claim-code">{t.code}</span>
        {t.href ? <a href={t.href}>{t.name}</a> : t.name}
      </h4>
      {row.standing.detail && (
        <p className="claim-detail">
          {capital(row.standing.status)}: <Markdown md={row.standing.detail} inline />
        </p>
      )}
      {found && (
        <p className="claim-found">
          <span className="claim-found-label">Experiments</span> {found.status}
          {found.detail && (
            <>
              : <Markdown md={found.detail} inline />
            </>
          )}
        </p>
      )}
      <ol className="pips" aria-label={`${t.code} level by level`}>
        {row.levels.map((c, i) => {
          const level = levels[i] ?? `L${i + 1}`;
          const short = /^L\d+/.exec(level)?.[0] ?? level;
          return (
            <li key={level} className={`v v-${c.tone}`} title={`${level}: ${c.status}`}>
              <span aria-hidden="true">{short}</span>
              <span className="visually-hidden">
                {level}: {c.status}
              </span>
            </li>
          );
        })}
      </ol>
    </li>
  );
}

export function ClaimCards({ record }: { record: VerificationRecord }) {
  return (
    <div className="claim-groups">
      {GROUPS.map(([status, heading, gloss]) => {
        const rows = record.rows.filter((r) => r.standing.status === status);
        if (rows.length === 0) return null;
        return (
          <section key={status} className="claim-group" aria-labelledby={`standing-${status}`}>
            <h3 id={`standing-${status}`}>
              <span className={`v v-${rows[0]?.standing.tone ?? "open"}`}>{heading}</span>
              <span className="count">{rows.length}</span>
            </h3>
            <p className="claim-gloss">{gloss}</p>
            <ul className="claims">
              {rows.map((r) => (
                <Card key={r.code} row={r} levels={record.levels} />
              ))}
            </ul>
          </section>
        );
      })}
    </div>
  );
}
