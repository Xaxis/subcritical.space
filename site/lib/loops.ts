// Coupled improvement loops (the memo's Y3), as plain linear algebra the page and the 3D scene
// share. Each loop's level next round is its own gain times its level, plus what the other loops
// feed it, plus a steady drive from human-held inputs: x' = G x + u. The system runs away when the
// spectral radius of G is 1 or more, even when every loop's own gain is below 1. The condition is
// prior work (Davidson, Halperin, Houlden and Korinek 2026; Burtsev 2026); this only illustrates it.

/** G for n loops, each with own gain g, each feeding every other loop with weight c. */
export function uniformCoupling(n: number, g: number, c: number): number[][] {
  return Array.from({ length: n }, (_, i) =>
    Array.from({ length: n }, (_, j) => (i === j ? g : c)),
  );
}

/** For that G the eigenvalues are g + (n - 1) c (once) and g - c, so the radius is the larger size. */
export function radiusUniform(n: number, g: number, c: number): number {
  return Math.max(Math.abs(g + (n - 1) * c), Math.abs(g - c));
}

/** The spectral radius of a non-negative matrix, by power iteration (its Perron root). */
export function spectralRadius(G: number[][], iterations = 500): number {
  const n = G.length;
  let v = new Array<number>(n).fill(1 / Math.sqrt(n));
  let lambda = 0;
  for (let k = 0; k < iterations; k++) {
    const w = G.map((row) => row.reduce((s, gij, j) => s + gij * (v[j] ?? 0), 0));
    const norm = Math.hypot(...w);
    if (norm === 0) return 0;
    lambda = norm;
    v = w.map((x) => x / norm);
  }
  return lambda;
}

/** One round: x' = G x + u, each level capped so a runaway stays drawable. */
export function step(x: number[], G: number[][], u: number, cap: number): number[] {
  return G.map((row) =>
    Math.min(
      cap,
      row.reduce((s, gij, j) => s + gij * (x[j] ?? 0), u),
    ),
  );
}

/** Where a subcritical system settles with every loop alike: u / (1 - radius). Null if it runs away. */
export function steadyLevel(radius: number, u: number): number | null {
  return radius < 1 ? u / (1 - radius) : null;
}

/** The five loops the memo names, in the order the scene places them. */
export const LOOPS = ["software", "hardware", "economic", "experiential", "acquisitive"] as const;
