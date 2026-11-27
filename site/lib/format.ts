// How the site writes a probability: whole percent down to 1% (the ledger's "%" format), then
// "1 in N", so small chances stay readable instead of rounding to 0%.
export function fmtProb(p: number): string {
  if (p >= 0.01) return `${Math.round(p * 100)}%`;
  if (p <= 0) return "0";
  const n = 1 / p;
  const shown =
    n >= 1e6 ? n.toExponential(1).replace("e+", "e") : Math.round(n).toLocaleString("en-US");
  return `1 in ${shown}`;
}
