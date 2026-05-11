import React from 'react';
import { TERRITORIES } from '../game/data/territories.js';

export function ChallengeModal({ territoryId, onResolve, title = '🌿 Desafio da Paisagem' }) {
  if (!territoryId) return null;
  const t = TERRITORIES[territoryId];
  return (
    <div className="modal-backdrop">
      <div className="modal">
        <h2>{title}</h2>
        <p style={{ color: 'var(--muted)', fontSize: 12 }}>
          Território: <b>{t.name}</b> · Macro: {t.macro}
        </p>

        <div className="metric-grid">
          <div className="metric"><span className="label">PLAND</span><span className="value">{t.pland}%</span></div>
          <div className="metric"><span className="label">NP</span><span className="value">{t.np}</span></div>
          <div className="metric"><span className="label">AREA_MN</span><span className="value">{t.areaMn} ha</span></div>
          <div className="metric"><span className="label">SHDI</span><span className="value">{t.shdi}</span></div>
          <div className="metric"><span className="label">CONNECT</span><span className="value">{t.connect}</span></div>
          <div className="metric"><span className="label">ED</span><span className="value">{t.ed} m/ha</span></div>
          <div className="metric"><span className="label">CORE</span><span className="value">{t.core}%</span></div>
          <div className="metric"><span className="label">SE</span><span className="value">{t.se}</span></div>
        </div>

        <p style={{ background: '#0a0d12', padding: 10, borderRadius: 4, lineHeight: 1.5 }}>
          {t.challenge}
        </p>

        <p style={{ color: 'var(--warn)', fontSize: 12 }}>
          ⏱️ 2 min para responder. Após o grupo avaliar, marque o resultado:
        </p>

        <div className="modal-actions">
          <button onClick={() => onResolve('full')}    style={{ background: 'var(--accent)' }}>✅ Acerto completo (+2)</button>
          <button onClick={() => onResolve('partial')} style={{ background: 'var(--warn)' }}>🟡 Acerto parcial (+1)</button>
          <button onClick={() => onResolve('wrong')}   style={{ background: 'var(--danger)' }}>❌ Erro (-1 token)</button>
        </div>
      </div>
    </div>
  );
}

export function NarrativeModal({ cardId, narrativeData, onResolve, ownedTerritoryIds }) {
  const [sacrifice, setSacrifice] = React.useState(ownedTerritoryIds[0] || '');
  if (!cardId) return null;
  const card = narrativeData.find((c) => c.id === cardId);
  if (!card) return null;

  return (
    <div className="modal-backdrop">
      <div className="modal">
        <h2>📜 Narrativa da Casa</h2>
        <p style={{ color: 'var(--muted)', fontSize: 12 }}>
          Carta {card.id} · Nível: {card.level}
        </p>
        <p style={{ background: '#0a0d12', padding: 10, borderRadius: 4, lineHeight: 1.5 }}>
          {card.prompt}
        </p>
        <div className="action-row" style={{ marginTop: 8 }}>
          <label style={{ fontSize: 12, color: 'var(--muted)' }}>Se errar, sacrificar token de:</label>
          <select value={sacrifice} onChange={(e) => setSacrifice(e.target.value)}>
            {ownedTerritoryIds.map((tid) => <option key={tid} value={tid}>{TERRITORIES[tid].name}</option>)}
          </select>
        </div>
        <div className="modal-actions">
          <button onClick={() => onResolve('full')}    style={{ background: 'var(--accent)' }}>✅ Completo (+3)</button>
          <button onClick={() => onResolve('partial')} style={{ background: 'var(--warn)' }}>🟡 Parcial (+1)</button>
          <button onClick={() => onResolve('wrong', sacrifice)} style={{ background: 'var(--danger)' }}>❌ Erro</button>
        </div>
      </div>
    </div>
  );
}
