// The mark: three generations of a chain reaction, each smaller than the last, so it dies out.
// That is what subcritical means, and what the protocol asks of AI's improvement loops.
export const GENERATIONS = [
  { cx: 8, r: 5.6 },
  { cx: 18.6, r: 3.9 },
  { cx: 26.4, r: 2.4 },
] as const;

export function Logo({ size = 28 }: { size?: number }) {
  return (
    <svg
      className="logo"
      width={size}
      height={size}
      viewBox="0 0 32 32"
      aria-hidden="true"
      focusable="false"
    >
      {GENERATIONS.map((g, i) => (
        <circle key={g.cx} cx={g.cx} cy="16" r={g.r} className={`gen gen-${i}`} />
      ))}
    </svg>
  );
}
