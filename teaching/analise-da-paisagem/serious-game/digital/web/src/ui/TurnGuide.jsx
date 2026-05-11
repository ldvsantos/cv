import React from 'react';

/**
 * TurnGuide — banner gigante "FAÇA ISSO AGORA".
 * Mostra UMA única instrução por vez + 1-2 botões.
 *
 * Props:
 *  - title: string (ex.: "PASSO 1 — Mobilizar")
 *  - instruction: string (ex.: "Clique no território verde e depois em 'Adicionar token'")
 *  - icon?: emoji
 *  - color?: 'green' | 'red' | 'blue' | 'yellow'
 *  - primary?: { label, onClick, disabled? }
 *  - secondary?: { label, onClick }
 *  - hint?: string menor (linha auxiliar)
 */
export function TurnGuide({ title, instruction, icon = '👉', color = 'yellow',
                            primary, secondary, hint }) {
  return (
    <div className={`turn-guide tg-${color}`}>
      <div className="tg-head">
        <span className="tg-icon">{icon}</span>
        <h2>{title}</h2>
      </div>
      <p className="tg-instruction">{instruction}</p>
      {hint && <p className="tg-hint">{hint}</p>}
      <div className="tg-actions">
        {primary && (
          <button className="tg-btn primary"
                  onClick={primary.onClick}
                  disabled={primary.disabled}>
            {primary.label}
          </button>
        )}
        {secondary && (
          <button className="tg-btn secondary" onClick={secondary.onClick}>
            {secondary.label}
          </button>
        )}
      </div>
    </div>
  );
}

/**
 * WaitingScreen — quando NÃO é seu turno: tela cheia em modo "espere".
 */
export function WaitingScreen({ currentPlayerName, currentHouseSigil }) {
  return (
    <div className="waiting-overlay">
      <div className="waiting-card">
        <div style={{ fontSize: 60 }}>⏳</div>
        <h2>Aguarde</h2>
        <p>É a vez de <b>{currentHouseSigil} {currentPlayerName}</b>.</p>
        <p style={{ fontSize: 12, color: 'var(--muted)' }}>
          Você pode observar o mapa enquanto espera.
        </p>
      </div>
    </div>
  );
}

/**
 * WelcomeIntro — overlay grande na primeira vez que o jogador entra.
 */
export function WelcomeIntro({ houseSigil, houseName, onClose }) {
  return (
    <div className="welcome-overlay" onClick={onClose}>
      <div className="welcome-card" onClick={(e) => e.stopPropagation()}>
        <div style={{ fontSize: 48 }}>{houseSigil}</div>
        <h1>Bem-vindo, Casa {houseName}</h1>
        <p>Seu objetivo: <b>conquistar territórios</b> e responder corretamente
           aos <b>desafios da paisagem</b>.</p>
        <ol style={{ textAlign: 'left', lineHeight: 1.6 }}>
          <li>🎯 No seu turno, o jogo dirá <b>exatamente o que fazer</b>.</li>
          <li>🗺️ <b>Verde</b> no mapa = ação possível agora.</li>
          <li>🎲 Combate = você rola dados de cubo (D6).</li>
          <li>📜 Conquistou? Responda ao desafio para ganhar Restauração.</li>
        </ol>
        <button className="tg-btn primary" onClick={onClose}>
          Entendi, vamos jogar!
        </button>
      </div>
    </div>
  );
}
