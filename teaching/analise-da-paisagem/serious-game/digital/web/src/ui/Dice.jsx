import React from 'react';

const FACES = {
  1: [[0.5, 0.5]],
  2: [[0.25, 0.25], [0.75, 0.75]],
  3: [[0.25, 0.25], [0.5, 0.5], [0.75, 0.75]],
  4: [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]],
  5: [[0.25, 0.25], [0.75, 0.25], [0.5, 0.5], [0.25, 0.75], [0.75, 0.75]],
  6: [[0.25, 0.2], [0.75, 0.2], [0.25, 0.5], [0.75, 0.5], [0.25, 0.8], [0.75, 0.8]],
};

export function Die({ value, color = '#fff', size = 44, label }) {
  const pips = FACES[value] || [];
  return (
    <div className="die-wrap" title={label}>
      <svg width={size} height={size} viewBox="0 0 100 100">
        <rect x="4" y="4" width="92" height="92" rx="14" ry="14"
              fill={color} stroke="#222" strokeWidth="3" />
        {pips.map(([x, y], i) => (
          <circle key={i} cx={x * 100} cy={y * 100} r="9" fill="#222" />
        ))}
      </svg>
      {label && <div className="die-label">{label}</div>}
    </div>
  );
}

export function DiceRow({ dice, color, label, highlight = [] }) {
  if (!dice || dice.length === 0) return null;
  return (
    <div className="dice-row">
      {label && <div className="dice-label">{label}</div>}
      <div className="dice-list">
        {dice.map((v, i) => (
          <div key={i} className={highlight.includes(i) ? 'die-highlight' : ''}>
            <Die value={v} color={color} size={44} />
          </div>
        ))}
      </div>
    </div>
  );
}
