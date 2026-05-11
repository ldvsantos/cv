import React, { useRef, useState, useCallback, useMemo } from 'react';
import { ADJACENCY, isAdjacent } from '../game/data/adjacencies.js';
import { TERRITORIES } from '../game/data/territories.js';
import { TERRITORY_COORDS } from '../game/data/mapCoords.js';
import { HOUSES } from '../game/data/houses.js';

const VB_W = 1000;
const VB_H = 1400;
const MIN_ZOOM = 0.5;
const MAX_ZOOM = 4;

export function MapView({
  G, ctx, playerID,
  selected, target, onSelect,
  onDragMove,
  highlightIds, // Set<string> de territórios para destacar/pulsar
}) {
  const hl = highlightIds || new Set();
  const hasHighlight = hl.size > 0;
  const svgRef = useRef(null);
  const [vb, setVb] = useState({ x: 0, y: 0, w: VB_W, h: VB_H });
  const panState = useRef(null);
  const dragState = useRef(null);
  const [dragFromId, setDragFromId] = useState(null);
  const [hoverId, setHoverId] = useState(null);
  const [pointerSvg, setPointerSvg] = useState(null);

  const screenToSvg = useCallback((cx, cy) => {
    const svg = svgRef.current;
    if (!svg) return { x: 0, y: 0 };
    // Usa getScreenCTM para respeitar preserveAspectRatio (letterboxing).
    const ctm = svg.getScreenCTM();
    if (!ctm) return { x: 0, y: 0 };
    const pt = svg.createSVGPoint();
    pt.x = cx; pt.y = cy;
    const p = pt.matrixTransform(ctm.inverse());
    return { x: p.x, y: p.y };
  }, []);

  const zoomBy = useCallback((factor, ax, ay) => {
    setVb((cur) => {
      const newW = Math.min(VB_W / MIN_ZOOM, Math.max(VB_W / MAX_ZOOM, cur.w * factor));
      const newH = newW * (VB_H / VB_W);
      const px = ax ?? (cur.x + cur.w / 2);
      const py = ay ?? (cur.y + cur.h / 2);
      const rx = (px - cur.x) / cur.w;
      const ry = (py - cur.y) / cur.h;
      return { x: px - rx * newW, y: py - ry * newH, w: newW, h: newH };
    });
  }, []);

  const onWheel = useCallback((e) => {
    e.preventDefault();
    const { x, y } = screenToSvg(e.clientX, e.clientY);
    zoomBy(e.deltaY > 0 ? 1.15 : 1 / 1.15, x, y);
  }, [screenToSvg, zoomBy]);

  const resetView = () => setVb({ x: 0, y: 0, w: VB_W, h: VB_H });

  const findTerritoryAt = useCallback((sx, sy) => {
    let best = null, bd = Infinity;
    for (const [id, c] of Object.entries(TERRITORY_COORDS)) {
      const d = Math.hypot(sx - c.x, sy - c.y);
      if (d < 32 && d < bd) { best = id; bd = d; }
    }
    return best;
  }, []);

  const onPointerDownBg = useCallback((e) => {
    if (dragState.current) return;
    const p0 = screenToSvg(e.clientX, e.clientY);
    panState.current = { sxSvg: p0.x, sySvg: p0.y, vb: { ...vb } };
    e.currentTarget.setPointerCapture(e.pointerId);
  }, [vb, screenToSvg]);

  const onPointerMove = useCallback((e) => {
    const p = screenToSvg(e.clientX, e.clientY);
    setPointerSvg(p);
    if (panState.current && !dragState.current) {
      const { sxSvg, sySvg, vb: sv } = panState.current;
      // diferença em coordenadas SVG
      const dx = p.x - sxSvg;
      const dy = p.y - sySvg;
      setVb({ x: sv.x - dx, y: sv.y - dy, w: sv.w, h: sv.h });
      return;
    }
    if (dragState.current) setHoverId(findTerritoryAt(p.x, p.y));
  }, [screenToSvg, findTerritoryAt]);

  const onPointerUpBg = useCallback(() => {
    panState.current = null;
    if (dragState.current) {
      const tgt = hoverId, from = dragState.current.fromId;
      dragState.current = null;
      setDragFromId(null);
      setHoverId(null);
      if (tgt && tgt !== from) onDragMove?.(from, tgt);
    }
  }, [hoverId, onDragMove]);

  const onPointerDownTerritory = useCallback((e, id) => {
    e.stopPropagation();
    const t = G.territories[id];
    const myTurn = ctx.currentPlayer === playerID;
    if (myTurn && t.owner === playerID && t.tokens > 0) {
      dragState.current = { fromId: id };
      setDragFromId(id);
      svgRef.current.setPointerCapture(e.pointerId);
    } else {
      onSelect(id);
    }
  }, [G, playerID, ctx.currentPlayer, onSelect]);

  const lines = useMemo(() => {
    const drawn = new Set(), out = [];
    for (const [a, ns] of Object.entries(ADJACENCY)) for (const b of ns) {
      const k = [a, b].sort().join('-');
      if (drawn.has(k)) continue;
      drawn.add(k);
      const ca = TERRITORY_COORDS[a], cb = TERRITORY_COORDS[b];
      if (ca && cb) out.push(<line key={k} className="adjacency-line" x1={ca.x} y1={ca.y} x2={cb.x} y2={cb.y} />);
    }
    return out;
  }, []);

  const dropClassFor = (id) => {
    if (!dragFromId || id === dragFromId) return null;
    if (!isAdjacent(dragFromId, id)) return null;
    return G.territories[id].owner === playerID ? 'drop-valid' : 'drop-attack';
  };

  const cls = ['map-svg'];
  if (panState.current) cls.push('panning');
  if (dragFromId) cls.push('dragging-token');

  return (
    <>
      <svg ref={svgRef} className={cls.join(' ')}
           viewBox={`${vb.x} ${vb.y} ${vb.w} ${vb.h}`}
           preserveAspectRatio="xMidYMid meet"
           onWheel={onWheel}
           onPointerDown={onPointerDownBg}
           onPointerMove={onPointerMove}
           onPointerUp={onPointerUpBg}
           onPointerCancel={onPointerUpBg}>
        <rect x="0" y="0" width={VB_W} height={VB_H} fill="#1a2332" />
        <defs>
          <pattern id="sea" patternUnits="userSpaceOnUse" width="20" height="20">
            <path d="M0 10 Q5 5,10 10 T20 10" stroke="#4a90e2" strokeWidth="0.5" fill="none" opacity="0.4" />
          </pattern>
        </defs>
        <rect x="0" y="0" width={VB_W} height={VB_H} fill="url(#sea)" opacity="0.15" />
        {lines}
        {Object.entries(TERRITORIES).map(([id, t]) => {
          const c = TERRITORY_COORDS[id];
          if (!c) return null;
          const ts = G.territories[id];
          const owner = ts.owner;
          const houseColor = owner !== null ? HOUSES[G.players[owner].house].color : '#555';
          const isCastle = owner !== null && HOUSES[G.players[owner].house].castle === id;
          const cs = ['territory-circle'];
          if (selected === id) cs.push('selected');
          if (target === id) cs.push('target');
          if (dragFromId === id) cs.push('drag-source');
          if (hl.has(id)) cs.push('hl-pulse');
          else if (hasHighlight) cs.push('dimmed');
          const drop = dropClassFor(id);
          if (drop && hoverId === id) cs.push(drop);
          return (
            <g key={id} onPointerDown={(e) => onPointerDownTerritory(e, id)}>
              <circle cx={c.x} cy={c.y} r={isCastle ? 26 : 20} className={cs.join(' ')} fill={houseColor} />
              <text x={c.x} y={c.y - 30} className="territory-label">{t.name}</text>
              {ts.tokens > 0 && <text x={c.x} y={c.y + 5} className="territory-tokens">{ts.tokens}</text>}
              {isCastle && <text x={c.x} y={c.y + 22} className="territory-label" style={{ fontSize: 14 }}>👑</text>}
            </g>
          );
        })}
        {dragFromId && pointerSvg && (
          <line className="drag-arrow"
                x1={TERRITORY_COORDS[dragFromId].x} y1={TERRITORY_COORDS[dragFromId].y}
                x2={pointerSvg.x} y2={pointerSvg.y}
                markerEnd="url(#arrow)" />
        )}
        <defs>
          <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
            <path d="M0,0 L10,5 L0,10 z" fill="#e1b12c" />
          </marker>
        </defs>
      </svg>

      <div className="map-controls">
        <button onClick={() => zoomBy(0.8)} title="Aproximar (+)">＋</button>
        <button onClick={() => zoomBy(1.25)} title="Afastar (−)">−</button>
        <button onClick={resetView} title="Resetar visão">⟲</button>
      </div>
      <div className="map-help">
        🖱️ Roda: zoom · Arraste fundo: pan · Arraste território seu sobre outro: mover/atacar
      </div>
    </>
  );
}
