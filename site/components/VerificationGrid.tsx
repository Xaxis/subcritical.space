// Where each claimed contribution stands at each of the six levels, from research/07-verification.md.
// Every cell shows its status in words and as a mark (filled: passed; half: corrected or narrowed;
// cross: failed; ring: not yet run), so the grid never relies on colour alone.
import { Markdown } from "@/components/Markdown";
import type { VerificationRecord } from "@/lib/verification";

export function VerificationGrid({ record }: { record: VerificationRecord }) {
  return (
    // biome-ignore lint/a11y/noNoninteractiveTabindex: a wide table scrolls, and a keyboard must reach it
    <div className="table-wrap vgrid-wrap" tabIndex={0}>
      <table className="vgrid">
        <caption className="visually-hidden">
          Each claim's result at each verification level, and its standing
        </caption>
        <thead>
          <tr>
            <th scope="col">Claim</th>
            {record.levels.map((l) => (
              <th key={l} scope="col">
                {l}
              </th>
            ))}
            <th scope="col">Standing</th>
          </tr>
        </thead>
        <tbody>
          {record.rows.map((r) => (
            <tr key={r.code}>
              <th scope="row">
                <Markdown md={r.claim} inline />
              </th>
              {[...r.levels, r.standing].map((c, i) => (
                <td key={`${r.code}-${record.levels[i] ?? "standing"}`}>
                  <span className={`v v-${c.tone}`}>{c.status}</span>
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
