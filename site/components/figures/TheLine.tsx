"use client";
// D4, the line between useful AI and the path to superintelligence, as something to move: a holding
// is weapons-grade when its breakout time is shorter than the margin times the regime's guaranteed
// time to detect and respond.
import { useId, useState } from "react";
import { weaponsGrade } from "@/lib/detection";

const SPAN = 60; // months shown
const W = 640;
const H = 120;
const PAD = { l: 12, r: 12 };

function Slider(p: {
  label: string;
  unit: string;
  min: number;
  max: number;
  step: number;
  value: number;
  set: (v: number) => void;
}) {
  const id = useId();
  return (
    <div className="figure-controls">
      <label htmlFor={id}>{p.label}</label>
      <input
        id={id}
        type="range"
        min={p.min}
        max={p.max}
        step={p.step}
        value={p.value}
        onChange={(e) => p.set(Number(e.target.value))}
        aria-valuetext={`${p.value} ${p.unit}`}
      />
      <output htmlFor={id} className="mono">
        {p.value} {p.unit}
      </output>
    </div>
  );
}

export function TheLine() {
  const [breakout, setBreakout] = useState(30);
  const [response, setResponse] = useState(6);
  const [margin, setMargin] = useState(2);
  const window_ = margin * response;
  const bad = weaponsGrade(breakout, response, margin);
  const x = (m: number) => PAD.l + (Math.min(m, SPAN) / SPAN) * (W - PAD.l - PAD.r);
  const head = bad ? "Weapons-grade." : "Useful AI.";
  const body = bad
    ? `A breakout of ${breakout} months beats the ${window_}-month window the regime needs to detect and respond with its margin.`
    : `A breakout of ${breakout} months is longer than the ${window_}-month window, so the regime would see it and respond in time. It may keep improving through the metered gates.`;
  const verdict = `${head} ${body}`;
  return (
    <figure className={`figure line ${bad ? "is-critical" : "is-sub"}`}>
      <Slider
        label="Breakout time"
        unit="months"
        min={1}
        max={SPAN}
        step={1}
        value={breakout}
        set={setBreakout}
      />
      <Slider
        label="Detect and respond"
        unit="months"
        min={1}
        max={24}
        step={1}
        value={response}
        set={setResponse}
      />
      <Slider
        label="Safety margin"
        unit="x"
        min={1}
        max={4}
        step={0.5}
        value={margin}
        set={setMargin}
      />
      <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={verdict}>
        <rect className="window" x={x(0)} y={30} width={x(window_) - x(0)} height={44} rx={4} />
        <text className="window-label" x={x(0) + 8} y={56}>
          margin x response = {window_} mo
        </text>
        <line className="axis" x1={x(0)} x2={x(SPAN)} y1={86} y2={86} />
        {[0, 12, 24, 36, 48, 60].map((t) => (
          <g key={t}>
            <line className="axis" x1={x(t)} x2={x(t)} y1={86} y2={91} />
            <text
              className="tick"
              x={x(t)}
              y={106}
              textAnchor={t === 0 ? "start" : t === SPAN ? "end" : "middle"}
            >
              {t}
            </text>
          </g>
        ))}
        <line className="breakout" x1={x(breakout)} x2={x(breakout)} y1={18} y2={86} />
        <text
          className="breakout-label"
          x={x(breakout)}
          y={13}
          textAnchor={breakout > SPAN * 0.8 ? "end" : breakout < SPAN * 0.2 ? "start" : "middle"}
        >
          breakout {breakout} mo
        </text>
      </svg>
      <figcaption>
        <strong className="state">{head}</strong> {body}{" "}
        <span className="muted">
          The positions are for illustration. No breakout time has been computed yet: that is
          definition D3, from measured inputs.
        </span>
      </figcaption>
    </figure>
  );
}
