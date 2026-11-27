"use client";
// The detection bound, with the ledger's inputs as the starting point: how likely independent
// channels are to all miss a secret program for its whole breakout time.
import { useId, useState } from "react";
import { missAll, missOneChannel } from "@/lib/detection";
import { fmtProb } from "@/lib/format";

export interface Inputs {
  inspections: number;
  detect: number;
  years: number;
  /** The ledger's display of the one-channel miss chance at these inputs, and its basis. */
  display: string;
}

/** What history says, from the ledger: undeclared weapons programmes and how long they went unseen. */
export interface Precedent {
  hazard: string;
  hazardLo: string;
  hazardHi: string;
  placeholderRate: string;
}

const MAX_CHANNELS = 6;
const CHANNELS = Array.from({ length: MAX_CHANNELS }, (_, k) => k + 1);

function Control(p: {
  label: string;
  min: number;
  max: number;
  step: number;
  value: number;
  shown: string;
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
        aria-valuetext={p.shown}
      />
      <output htmlFor={id} className="mono">
        {p.shown}
      </output>
    </div>
  );
}

export function DetectionBound({ start, record }: { start: Inputs; record?: Precedent }) {
  const [lam, setLam] = useState(start.inspections);
  const [p, setP] = useState(start.detect);
  const [years, setYears] = useState(start.years);
  const [channels, setChannels] = useState(1);
  const one = missOneChannel(lam, p, years);
  const all = missAll(one, channels);
  const atLedger = lam === start.inspections && p === start.detect && years === start.years;
  const W = 640;
  const H = 150;
  const bw = (W - 24) / MAX_CHANNELS;
  return (
    <figure className="figure detect">
      <Control
        label="Inspections a year"
        min={0}
        max={24}
        step={1}
        value={lam}
        shown={`${lam}/yr`}
        set={setLam}
      />
      <Control
        label="Chance each finds it"
        min={0}
        max={1}
        step={0.05}
        value={p}
        shown={`${Math.round(p * 100)}%`}
        set={setP}
      />
      <Control
        label="Breakout time"
        min={0.25}
        max={5}
        step={0.25}
        value={years}
        shown={`${years} yr`}
        set={setYears}
      />
      <Control
        label="Independent channels"
        min={1}
        max={MAX_CHANNELS}
        step={1}
        value={channels}
        shown={`${channels}`}
        set={setChannels}
      />
      <svg
        viewBox={`0 0 ${W} ${H}`}
        role="img"
        aria-label={`Chance all ${channels} channels miss: ${fmtProb(all)}`}
      >
        {CHANNELS.map((n) => {
          const k = n - 1;
          const miss = missAll(one, k + 1);
          // Scaled to one channel's miss chance, so the fall with each added channel stays visible.
          const h = (one > 0 ? miss / one : 0) * (H - 40);
          const x = 12 + k * bw + bw * 0.18;
          return (
            <g key={n} className={n === channels ? "chosen" : ""}>
              <rect
                className="miss-bar"
                x={x}
                y={H - 22 - h}
                width={bw * 0.64}
                height={Math.max(h, 1)}
                rx={3}
              />
              <text className="tick" x={x + bw * 0.32} y={H - 22 - h - 6} textAnchor="middle">
                {fmtProb(miss)}
              </text>
              <text className="tick" x={x + bw * 0.32} y={H - 6} textAnchor="middle">
                {k + 1} ch
              </text>
            </g>
          );
        })}
      </svg>
      <figcaption>
        <strong>
          {channels === 1 ? "One channel misses it" : `All ${channels} channels miss it`}:{" "}
          {fmtProb(all)}.
        </strong>{" "}
        {atLedger && channels === 1 ? (
          <>
            That is the ledger&apos;s <a href="/numbers#miss-prob-one-channel">{start.display}</a>.{" "}
          </>
        ) : null}
        <span className="muted">
          The starting inputs are the ledger&apos;s placeholders (basis: assumption), and real
          channels are not independent or identical: an evader picks the path the channels share.
          The formula is exp(-rate x chance x time) per channel, ported from the model.
        </span>{" "}
        {record && (
          <span className="muted">
            The record is worse. Covert weapons programmes were found at about{" "}
            <a href="/numbers#e5-hazard">{record.hazard}</a> (
            <a href="/numbers#e5-hazard-lo">{record.hazardLo}</a> to{" "}
            <a href="/numbers#e5-hazard-hi">{record.hazardHi}</a>), counted from each
            programme&apos;s start, against the{" "}
            <a href="/numbers#org-memo-detect-rate">{record.placeholderRate}</a> these placeholders
            imply. Even that is an upper bound for a careful evader: only programmes that were found
            or disclosed are in the record.
          </span>
        )}
      </figcaption>
    </figure>
  );
}
