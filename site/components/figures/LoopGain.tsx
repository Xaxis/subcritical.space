"use client";
// D2, the loop gain, as something to move. Each bar is the capability gained so far after n rounds
// of AI-driven research with the human-held inputs fixed, in units of the first round's gain. Below
// g = 1 the bars level off under a ceiling; at 1 and above they run off the top.
import { useId, useState } from "react";
import { loopGains, loopLimit } from "@/lib/detection";

const ROUNDS = 16;
const YMAX = 12;
const W = 640;
const H = 260;
const PAD = { l: 40, r: 12, t: 14, b: 30 };

const fmt = (x: number) =>
  x >= 100 ? Math.round(x).toLocaleString("en-US") : x.toFixed(x >= 10 ? 1 : 2);

export function LoopGain({ initial = 0.8 }: { initial?: number }) {
  const [g, setG] = useState(initial);
  const id = useId();
  const series = loopGains(g, ROUNDS);
  const limit = loopLimit(g);
  const last = series[series.length - 1]?.total ?? 0;
  const critical = g >= 1;
  const iw = W - PAD.l - PAD.r;
  const ih = H - PAD.t - PAD.b;
  const bw = iw / ROUNDS;
  const y = (v: number) => PAD.t + ih - (Math.min(v, YMAX) / YMAX) * ih;
  const head = critical ? "Supercritical." : "Subcritical.";
  const body = critical
    ? `After ${ROUNDS} rounds the total is ${fmt(last)} first-round gains and still growing, with no limit.`
    : `After ${ROUNDS} rounds the total is ${fmt(last)} first-round gains, and it can never pass ${fmt(limit ?? 0)}.`;
  const state = `g = ${g.toFixed(2)}: ${head} ${body}`;

  return (
    <figure className={`figure loop ${critical ? "is-critical" : "is-sub"}`}>
      <div className="figure-controls">
        <label htmlFor={id}>
          Loop gain <var>g</var>
        </label>
        <input
          id={id}
          type="range"
          min={0.5}
          max={1.25}
          step={0.01}
          value={g}
          onChange={(e) => setG(Number(e.target.value))}
          aria-valuetext={`g = ${g.toFixed(2)}`}
        />
        <output htmlFor={id} className="mono">
          {g.toFixed(2)}
        </output>
      </div>
      <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={state}>
        {[0, 4, 8, 12].map((t) => (
          <g key={t}>
            <line className="grid" x1={PAD.l} x2={W - PAD.r} y1={y(t)} y2={y(t)} />
            <text className="tick" x={PAD.l - 8} y={y(t) + 4} textAnchor="end">
              {t}
            </text>
          </g>
        ))}
        {series.map((s, n) => {
          const x = PAD.l + n * bw + bw * 0.14;
          const w = bw * 0.72;
          const prev = n === 0 ? 0 : (series[n - 1]?.total ?? 0);
          const over = s.total > YMAX;
          return (
            // biome-ignore lint/suspicious/noArrayIndexKey: the rounds are a fixed sequence
            <g key={n}>
              <rect className="bar-base" x={x} y={y(prev)} width={w} height={y(0) - y(prev)} />
              <rect
                className="bar-gain"
                x={x}
                y={y(s.total)}
                width={w}
                height={Math.max(0, y(prev) - y(s.total))}
              />
              {over && (
                <path className="bar-over" d={`M${x} ${PAD.t + 6} l${w / 2} -6 l${w / 2} 6`} />
              )}
              <text className="tick" x={x + w / 2} y={H - PAD.b + 16} textAnchor="middle">
                {n + 1}
              </text>
            </g>
          );
        })}
        {limit !== null && limit <= YMAX && (
          <g>
            <line className="ceiling" x1={PAD.l} x2={W - PAD.r} y1={y(limit)} y2={y(limit)} />
            <text className="ceiling-label" x={W - PAD.r - 4} y={y(limit) - 6} textAnchor="end">
              ceiling 1 / (1 - g) = {fmt(limit)}
            </text>
          </g>
        )}
        <text className="axis-label" x={PAD.l} y={H - 2}>
          round of AI-driven research
        </text>
      </svg>
      <figcaption>
        <strong className="state">{head}</strong> {body}{" "}
        <span className="muted">
          An illustration of definition D2, not a measurement: the experiment that estimates g (E4)
          has not run yet.
        </span>
      </figcaption>
    </figure>
  );
}
