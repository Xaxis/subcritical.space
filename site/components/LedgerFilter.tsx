"use client";
// Search and basis filters for the ledger page. The rows are rendered on the server, so the page
// works without script; this only hides rows that do not match and opens the groups that do. A link
// to /numbers#id opens that number's group and row and scrolls to it.
import { useEffect, useId, useRef, useState } from "react";

type Basis = { basis: string; meaning: string; count: number };

function rows(): HTMLDetailsElement[] {
  return Array.from(document.querySelectorAll<HTMLDetailsElement>(".lrow"));
}

function groups(): HTMLDetailsElement[] {
  return Array.from(document.querySelectorAll<HTMLDetailsElement>("details[data-group]"));
}

/** Open the row the address names, and its group, and bring it into view. */
function reveal() {
  const id = decodeURIComponent(window.location.hash.slice(1));
  if (!id) return;
  const el = document.getElementById(id);
  if (!(el instanceof HTMLDetailsElement) || !el.classList.contains("lrow")) return;
  const group = el.closest<HTMLDetailsElement>("details[data-group]");
  if (group) group.open = true;
  el.open = true;
  el.scrollIntoView({ block: "center" });
}

export function LedgerFilter({
  total,
  files,
  bases,
}: {
  total: number;
  files: number;
  bases: Basis[];
}) {
  const [query, setQuery] = useState("");
  const [off, setOff] = useState<Set<string>>(new Set());
  const [shown, setShown] = useState(total);
  const searchId = useId();
  const filtered = useRef(false);

  useEffect(() => {
    reveal();
    window.addEventListener("hashchange", reveal);
    return () => window.removeEventListener("hashchange", reveal);
  }, []);

  useEffect(() => {
    const words = query.toLowerCase().split(/\s+/).filter(Boolean);
    // Only a search unfolds the groups; a basis filter just thins the rows inside them.
    const searching = words.length > 0;
    let n = 0;
    for (const r of rows()) {
      const q = r.dataset.q ?? "";
      const ok = !off.has(r.dataset.basis ?? "") && words.every((w) => q.includes(w));
      r.hidden = !ok;
      if (ok) n += 1;
    }
    for (const g of groups()) {
      const any = g.querySelector(".lrow:not([hidden])") !== null;
      g.hidden = !any;
      // While a search is on, every group with a match stands open; clearing it folds them again.
      if (searching) g.open = any;
      else if (filtered.current) g.open = false;
    }
    filtered.current = searching;
    setShown(n);
  }, [query, off]);

  const toggle = (b: string) =>
    setOff((prev) => {
      const next = new Set(prev);
      if (next.has(b)) next.delete(b);
      else next.add(b);
      return next;
    });

  return (
    <div className="lfilter">
      <label htmlFor={searchId} className="visually-hidden">
        Search the ledger
      </label>
      <input
        id={searchId}
        type="search"
        className="lsearch"
        placeholder="Search: breakout, e22, h100"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        autoComplete="off"
        spellCheck={false}
      />
      <fieldset className="lbases">
        <legend className="visually-hidden">Show numbers of these bases</legend>
        {bases.map((b) => (
          <button
            key={b.basis}
            type="button"
            className={`lbasis basis-${b.basis}`}
            aria-pressed={!off.has(b.basis)}
            title={b.meaning}
            onClick={() => toggle(b.basis)}
          >
            {b.basis} <span className="mono">{b.count}</span>
          </button>
        ))}
      </fieldset>
      <p className="lshown" aria-live="polite">
        {shown === total
          ? `${total.toLocaleString("en-US")} numbers from ${files} files`
          : `${shown.toLocaleString("en-US")} of ${total.toLocaleString("en-US")} numbers match`}
      </p>
    </div>
  );
}
