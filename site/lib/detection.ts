// The detection bound, ported from model/subcritical.py so the page can move its inputs.
// test/content.test.ts checks it against data/numbers.json: equal within a few ulps (V8's Math.exp
// and Python's math.exp can differ in the last bit) and identical once displayed.
//
// A secret program that must run for T years before it reaches the line is missed by inspections
// arriving as a Poisson process at rate lam a year, each catching it with probability p, with
// probability exp(-lam * p * T). Independent channels each have to miss it.

export function missOneChannel(
  inspectionsPerYear: number,
  detectProb: number,
  years: number,
): number {
  return Math.exp(-inspectionsPerYear * detectProb * years);
}

/** The chance that every one of `channels` independent, identical channels misses the program. */
export function missAll(oneChannel: number, channels: number): number {
  return oneChannel ** channels;
}

/** D4: a holding is weapons-grade when its breakout time is under margin x response time. */
export function weaponsGrade(breakout: number, response: number, margin: number): boolean {
  return breakout < margin * response;
}

/**
 * D2 illustrated: with the human-held inputs fixed, round n of AI-driven research adds g^(n-1)
 * times the first round's gain. Below g = 1 the total converges to 1 / (1 - g); at or above 1 it
 * has no limit.
 */
export function loopGains(g: number, rounds: number): { gain: number; total: number }[] {
  const out: { gain: number; total: number }[] = [];
  let total = 0;
  for (let n = 0; n < rounds; n++) {
    const gain = g ** n;
    total += gain;
    out.push({ gain, total });
  }
  return out;
}

export function loopLimit(g: number): number | null {
  return g < 1 ? 1 / (1 - g) : null;
}
