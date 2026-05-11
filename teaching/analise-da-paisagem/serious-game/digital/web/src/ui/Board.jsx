import React, { useState, useEffect, useMemo } from 'react';
import { MapView } from './MapView.jsx';
import { ChallengeModal, NarrativeModal } from './Modals.jsx';
import { DiceRow } from './Dice.jsx';
import { TurnGuide, WaitingScreen, WelcomeIntro } from './TurnGuide.jsx';
import { TERRITORIES } from '../game/data/territories.js';
import { ADJACENCY, isAdjacent } from '../game/data/adjacencies.js';
import { HOUSES } from '../game/data/houses.js';
import { NARRATIVES } from '../game/data/narratives.js';

const ALL_NARRATIVES = Object.values(NARRATIVES).flat();

// ───────────────────── Hook: estado do tutorial ─────────────────────
//   sub-etapas dentro do meu turno: 'intro' → 'mobilize' → 'attack' → 'end'
//   sub-etapas de combate são derivadas de me.currentAttack.phase
function useTurnSubStep(playerID, isMyTurn, ctx) {
  const [step, setStep] = useState('intro');
  // Reset quando vira meu turno
  useEffect(() => {
    if (isMyTurn) setStep('intro');
  }, [ctx.turn, isMyTurn]);
  return [step, setStep];
}

export function Board({ G, ctx, moves, playerID }) {
  const me = G.players[playerID];
  const isMyTurn = ctx.currentPlayer === playerID;
  const myHouse = me && HOUSES[me.house];
  const ownedIds = useMemo(
    () => Object.entries(G.territories).filter(([, t]) => t.owner === playerID).map(([id]) => id),
    [G.territories, playerID]
  );

  const [selected, setSelected] = useState(null);
  const [target, setTarget] = useState(null);
  const [committedTokens, setCommittedTokens] = useState(1);
  const [substep, setSubstep] = useTurnSubStep(playerID, isMyTurn, ctx);
  const [showInvite, setShowInvite] = useState(false);
  // Tour inicial: 0=casa, 1=castelo, 2=reserva, 3=fim do tour
  const [tourStep, setTourStep] = useState(0);
  const inTour = tourStep < 3;

  // Auto-resolve teste do defensor
  const myAttack = me?.currentAttack;
  useEffect(() => {
    if (isMyTurn && myAttack && myAttack.phase === 'defenderTest') {
      moves.resolveDefenderTest(playerID);
    }
  }, [myAttack?.phase, isMyTurn, playerID, moves]);

  // Limpa seleção quando muda substep
  useEffect(() => { setSelected(null); setTarget(null); }, [substep]);

  // ───────────────── Game over ─────────────────
  if (ctx.gameover) {
    const winnerHouse = HOUSES[G.players[ctx.gameover.winner].house];
    return (
      <div className="board">
        <div className="board-map" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ textAlign: 'center', color: 'var(--accent)' }}>
            <h1 style={{ fontSize: 48 }}>🏆 Fim de jogo</h1>
            <p style={{ fontSize: 24 }}>{winnerHouse.sigil} {winnerHouse.name} venceu!</p>
          </div>
        </div>
      </div>
    );
  }

  // ───────────────── HANDLERS DE MAPA ─────────────────
  function handleSelect(id) {
    if (!isMyTurn) return;
    const t = G.territories[id];

    if (substep === 'mobilize') {
      if (t.owner === playerID) setSelected(id);
      return;
    }
    if (substep === 'attack') {
      if (t.owner === playerID) { setSelected(id); setTarget(null); return; }
      if (selected && isAdjacent(selected, id) && t.owner !== playerID) {
        setTarget(id);
      }
    }
  }

  function handleDragMove(fromId, toId) {
    if (!isMyTurn) return;
    const fromT = G.territories[fromId];
    const toT = G.territories[toId];
    if (substep !== 'attack') return; // só permite arrastar na fase de ataque
    if (toT.owner === playerID) {
      moves.redeployReserve(fromId, toId, 1);
    } else if (isAdjacent(fromId, toId)) {
      const tokens = Math.min(committedTokens, fromT.tokens - 1) || 1;
      moves.declareAttack(fromId, toId, tokens);
    }
  }

  // ───────────────── DERIVAÇÕES DE UI ─────────────────
  const myCastle = myHouse?.castle;
  // Quais territórios destacar no mapa para esta etapa?
  const highlightIds = useMemo(() => {
    if (inTour) {
      if (tourStep === 0) return new Set(ownedIds);          // casa: todos os meus
      if (tourStep === 1) return new Set(myCastle ? [myCastle] : []); // só castelo
      return new Set();                                      // reserva: nada no mapa
    }
    if (!isMyTurn) return new Set();
    if (substep === 'mobilize') return new Set(ownedIds);
    if (substep === 'attack') {
      if (!selected) return new Set(ownedIds.filter((t) => G.territories[t].tokens >= 2));
      // alvos: vizinhos não-meus
      return new Set((ADJACENCY[selected] || []).filter((n) => G.territories[n].owner !== playerID));
    }
    return new Set();
  }, [inTour, tourStep, isMyTurn, substep, selected, ownedIds, myCastle, G.territories, playerID]);

  // Pode mobilizar?
  const macros = useMemo(() => {
    // simplificação: assume que mobilização é sempre permitida se há reserva
    return [];
  }, []);
  const canMobilize = me && me.reserve > 0;

  // ───────────────── CONSTRUÇÃO DO GUIA (FAÇA ISSO AGORA) ─────────────────
  let guide = null;
  // TOUR INICIAL — antes de tudo, ensina o jogador onde ele está
  if (inTour) {
    if (tourStep === 0) {
      const tNames = ownedIds.slice(0, 3).map((t) => TERRITORIES[t].name).join(', ');
      guide = (
        <TurnGuide
          color="green"
          icon={myHouse.sigil}
          title={`BEM-VINDO, CASA ${myHouse.name}`}
          instruction={`Você comanda ${ownedIds.length} territórios (verdes pulsando no mapa): ${tNames}${ownedIds.length > 3 ? '…' : ''}`}
          hint="Esses são SEUS — você defende e ataca a partir deles."
          primary={{ label: 'Próximo (1/3) →', onClick: () => setTourStep(1) }}
        />
      );
    } else if (tourStep === 1) {
      guide = (
        <TurnGuide
          color="yellow"
          icon="👑"
          title="SEU CASTELO PRINCIPAL"
          instruction={`${TERRITORIES[myCastle]?.name} é o coração da Casa ${myHouse.name}. Veja o 👑 pulsando no mapa.`}
          hint="⚠️ Se perder o castelo, você é eliminado. Protegido só na 1ª rodada."
          primary={{ label: 'Próximo (2/3) →', onClick: () => setTourStep(2) }}
        />
      );
    } else if (tourStep === 2) {
      guide = (
        <TurnGuide
          color="blue"
          icon="🛡"
          title="SUA RESERVA DE TROPAS"
          instruction={`Você tem ${me.reserve} tokens na reserva (não estão no mapa ainda). A cada turno você pode mobilizar até 1 token básico para o mapa.`}
          hint="Acertar desafios e completar regiões aumenta o quanto você pode mobilizar."
          primary={{ label: 'Entendi, vamos jogar! (3/3) ✓', onClick: () => setTourStep(3) }}
        />
      );
    }
  } else if (isMyTurn) {
    // Modais de prioridade máxima: desafio e narrativa não disparam guide (têm modal próprio)
    if (me.pendingChallenge || me.pendingNarrative) {
      guide = null;
    } else if (myAttack) {
      // Sub-fluxo de ataque
      const tName = TERRITORIES[myAttack.toId].name;
      if (myAttack.phase === 'challenge') {
        guide = (
          <TurnGuide
            color="yellow"
            icon="📚"
            title="PASSA OU REPASSA"
            instruction={`Pergunta sobre ${tName}: "${TERRITORIES[myAttack.toId].challenge}"`}
            hint="Quem respondeu corretamente? (acerto = re-rolar 1 dado no combate)"
          />
        );
      } else if (myAttack.phase === 'combat') {
        guide = (
          <TurnGuide
            color="red"
            icon="⚔️"
            title="HORA DE ROLAR OS DADOS"
            instruction={`Combate em ${tName}. Clique abaixo para rolar.`}
            primary={{
              label: '🎲 ROLAR DADOS DE COMBATE',
              onClick: () => moves.resolveCombat(playerID),
            }}
          />
        );
      } else if (myAttack.phase === 'resolved') {
        const conquered = myAttack.conquered;
        guide = (
          <TurnGuide
            color={conquered ? 'green' : 'yellow'}
            icon={conquered ? '🏆' : '⚔️'}
            title={conquered ? `CONQUISTOU ${tName}!` : 'COMBATE RESOLVIDO'}
            instruction={`Atacante perdeu ${myAttack.attackerLost} · Defensor perdeu ${myAttack.defenderLost}`}
            hint={conquered ? 'Você responderá ao desafio da paisagem em seguida.' : null}
            primary={{ label: 'OK, próximo →', onClick: () => moves.closeAttackSummary() }}
          />
        );
      }
    } else if (substep === 'intro') {
      guide = (
        <TurnGuide
          color="green"
          icon="🎯"
          title="É O SEU TURNO!"
          instruction="Você fará 3 ações: (1) Mobilizar tokens, (2) Atacar, (3) Encerrar."
          hint="Não precisa fazer todas — pode pular qualquer uma."
          primary={{ label: '▶ Começar passo 1', onClick: () => setSubstep('mobilize') }}
          secondary={{ label: 'Pular tudo, encerrar turno', onClick: () => moves.endTurn() }}
        />
      );
    } else if (substep === 'mobilize') {
      if (!canMobilize) {
        guide = (
          <TurnGuide
            color="yellow"
            icon="🛡"
            title="PASSO 1 — Mobilizar"
            instruction="Você não tem tokens na reserva."
            primary={{ label: 'Próximo passo →', onClick: () => setSubstep('attack') }}
          />
        );
      } else if (!selected) {
        guide = (
          <TurnGuide
            color="green"
            icon="🛡"
            title={`PASSO 1 — Mobilizar (reserva: ${me.reserve})`}
            instruction="👉 Clique em UM dos seus territórios (destacados no mapa)."
            hint="Você vai colocar tokens nele para reforçar suas tropas."
            secondary={{ label: 'Pular para ataque →', onClick: () => setSubstep('attack') }}
          />
        );
      } else {
        guide = (
          <TurnGuide
            color="green"
            icon="🛡"
            title={`Adicionar tokens em ${TERRITORIES[selected].name}`}
            instruction={`Quantos tokens? (você tem ${me.reserve} na reserva)`}
            primary={{
              label: `+1 token aqui`,
              onClick: () => { moves.mobilizeReserve(selected, 1); setSelected(null); },
              disabled: me.reserve < 1,
            }}
            secondary={{ label: 'Próximo passo (atacar) →', onClick: () => setSubstep('attack') }}
          />
        );
      }
    } else if (substep === 'attack') {
      if (!selected) {
        guide = (
          <TurnGuide
            color="red"
            icon="⚔️"
            title="PASSO 2 — Atacar"
            instruction="👉 Clique em UM território seu com 2+ tokens (destacados no mapa)."
            hint="Você precisa deixar pelo menos 1 token guarnecendo o local de origem."
            secondary={{ label: 'Pular para encerrar →', onClick: () => setSubstep('end') }}
          />
        );
      } else if (!target) {
        guide = (
          <TurnGuide
            color="red"
            icon="⚔️"
            title={`Atacar a partir de ${TERRITORIES[selected].name}`}
            instruction="👉 Agora clique em um vizinho INIMIGO (destacado em vermelho)."
            hint="Ou arraste o território selecionado direto sobre o alvo."
            secondary={{ label: '← Trocar origem', onClick: () => setSelected(null) }}
          />
        );
      } else {
        const fromT = G.territories[selected];
        const maxTokens = Math.min(3, fromT.tokens - 1);
        guide = (
          <div className="turn-guide tg-red">
            <div className="tg-head">
              <span className="tg-icon">⚔️</span>
              <h2>Atacar {TERRITORIES[target].name}</h2>
            </div>
            <p className="tg-instruction">
              Quantos tokens comprometer? (1–{maxTokens})
            </p>
            <div className="tg-token-picker">
              {Array.from({ length: maxTokens }, (_, i) => i + 1).map((n) => (
                <button key={n}
                        className={`tg-token-btn ${committedTokens === n ? 'on' : ''}`}
                        onClick={() => setCommittedTokens(n)}>
                  {n} 🪙
                </button>
              ))}
            </div>
            <p className="tg-hint">Mais tokens = mais dados de ataque (e mais risco se falhar).</p>
            <div className="tg-actions">
              <button className="tg-btn primary"
                      onClick={() => {
                        moves.declareAttack(selected, target, committedTokens);
                        setSelected(null); setTarget(null);
                      }}>
                ⚔️ ATACAR COM {committedTokens} TOKEN{committedTokens > 1 ? 'S' : ''}
              </button>
              <button className="tg-btn secondary" onClick={() => setTarget(null)}>
                ← Outro alvo
              </button>
            </div>
          </div>
        );
      }
    } else if (substep === 'end') {
      guide = (
        <TurnGuide
          color="blue"
          icon="✅"
          title="PASSO 3 — Encerrar turno"
          instruction="Tudo certo? Pode comprar uma carta narrativa antes de encerrar."
          primary={{ label: '▶ Encerrar turno', onClick: () => moves.endTurn() }}
          secondary={{ label: '📜 Comprar carta narrativa', onClick: () => moves.drawNarrative() }}
        />
      );
    }
  }

  // ───────────────── DADOS visíveis (sempre que houver) ─────────────────
  const dicePanel = (myAttack || G.lastDice) && (
    <div className="panel dice-panel">
      <h3>🎲 Dados desta jogada</h3>
      {!myAttack && G.lastDice?.kind === 'mobilizationFail' && (
        <DiceRow dice={G.lastDice.dice} color="#c0392b"
                 label={`Mobilização FALHOU · média ${G.lastDice.avg.toFixed(1)} < ${G.lastDice.required}`} />
      )}
      {myAttack?.mobilizationDice && (
        <DiceRow dice={myAttack.mobilizationDice} color="#fff"
                 label={`Mobilização atacante · média ${myAttack.mobilizationAvg.toFixed(1)} (≥${myAttack.mobilizationRequired})`} />
      )}
      {myAttack?.defenderDice?.length > 0 && (
        <DiceRow dice={myAttack.defenderDice} color="#aaa"
                 label={`Mobilização defensor · efetivo ${myAttack.defenderEffective}`} />
      )}
      {myAttack?.attackerCombatDice && (
        <DiceRow dice={myAttack.attackerCombatDice} color="#e74c3c" label="⚔ Atacante (combate)" />
      )}
      {myAttack?.defenderCombatDice?.length > 0 && (
        <DiceRow dice={myAttack.defenderCombatDice} color="#3498db" label="🛡 Defensor (combate)" />
      )}
    </div>
  );

  // Botões "Passa ou Repassa" quando aplicável
  const challengeButtons = isMyTurn && myAttack?.phase === 'challenge' && (
    <div className="panel" style={{ background: '#3a2a00' }}>
      <div style={{ display: 'flex', gap: 4 }}>
        <button className="tg-btn primary" onClick={() => moves.resolveChallenge(playerID, 'attacker')}>
          Atacante acertou ✓
        </button>
        <button className="tg-btn secondary" onClick={() => moves.resolveChallenge(playerID, 'defender')}>
          Defensor acertou ✓
        </button>
        <button className="tg-btn secondary" onClick={() => moves.resolveChallenge(playerID, 'none')}>
          Ninguém ✗
        </button>
      </div>
    </div>
  );

  const otherPlayer = G.players[ctx.currentPlayer];
  const otherHouse = otherPlayer ? HOUSES[otherPlayer.house] : null;

  return (
    <div className="board">
      <div className="board-map">
        <MapView G={G} ctx={ctx} playerID={playerID}
                 selected={selected} target={target}
                 onSelect={handleSelect} onDragMove={handleDragMove}
                 highlightIds={highlightIds} />
        {!isMyTurn && otherHouse && (
          <WaitingScreen currentPlayerName={otherHouse.name} currentHouseSigil={otherHouse.sigil} />
        )}
      </div>

      <div className="board-side">
        {/* IDENTIDADE compacta */}
        <div className="panel id-panel" style={{ background: myHouse ? myHouse.color + '22' : undefined }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <div style={{ fontWeight: 'bold' }}>{myHouse?.sigil} Casa {myHouse?.name}</div>
              <div style={{ fontSize: 11, color: 'var(--muted)' }}>Você · jogador {Number(playerID)+1}</div>
            </div>
            <button onClick={() => setShowInvite((s) => !s)} style={{ fontSize: 11 }}>
              📋 Convidar
            </button>
          </div>
          <div style={{ display: 'flex', gap: 12, fontSize: 13, marginTop: 6 }}>
            <span title="Tokens na reserva">🛡 <b>{me?.reserve}</b></span>
            <span title="Tokens de Restauração">♻ <b>{me?.restoration}</b></span>
            <span title="Rodada">🕒 R<b>{G.round}</b></span>
          </div>
        </div>

        {/* CONVITE (toggle) */}
        {showInvite && <InvitePanel matchID={getMatchIdFromUrl()} />}

        {/* GUIA PRINCIPAL — o coração do tutorial */}
        {guide}

        {/* PASSA OU REPASSA */}
        {challengeButtons}

        {/* DADOS */}
        {dicePanel}

        {/* JOGADORES (compacto) */}
        <div className="panel">
          <h3>🏰 Jogadores</h3>
          {Object.entries(G.players).map(([pid, p]) => {
            const h = HOUSES[p.house];
            const cls = ['player-card'];
            if (pid === playerID) cls.push('me');
            if (pid === ctx.currentPlayer) cls.push('current');
            if (p.eliminated) cls.push('eliminated');
            const territoryCount = Object.values(G.territories).filter((t) => t.owner === pid).length;
            return (
              <div key={pid} className={cls.join(' ')} style={{ background: h.color + '22' }}>
                <span><span className="sigil">{h.sigil}</span>{h.name}</span>
                <span style={{ fontSize: 11 }}>🗺{territoryCount} 🛡{p.reserve}</span>
              </div>
            );
          })}
        </div>

        {/* HISTÓRICO compactado */}
        <div className="panel">
          <h3 style={{ cursor: 'pointer' }}>📜 Histórico</h3>
          <div className="log">
            {G.log.slice().reverse().slice(0, 8).map((l, i) => (
              <div key={i} className="log-entry"><b>R{l.round}</b> · {l.msg}</div>
            ))}
          </div>
        </div>
      </div>

      {/* MODAIS */}
      {isMyTurn && me?.pendingChallenge && (
        <ChallengeModal territoryId={me.pendingChallenge}
                        onResolve={(r) => moves.resolveLandscapeChallenge(r)} />
      )}
      {isMyTurn && me?.pendingNarrative && (
        <NarrativeModal cardId={me.pendingNarrative}
                        narrativeData={ALL_NARRATIVES}
                        ownedTerritoryIds={ownedIds}
                        onResolve={(r, sac) => moves.resolveNarrative(r, sac)} />
      )}
    </div>
  );
}

// ───────────────── helpers ─────────────────
function getMatchIdFromUrl() {
  // boardgame.io não expõe matchID via window — armazenamos via App.jsx (sessionStorage)
  return sessionStorage.getItem('rol_matchID') || '';
}

function InvitePanel({ matchID }) {
  const url = matchID
    ? `${window.location.origin}${window.location.pathname}?match=${matchID}`
    : window.location.href;
  const copy = async () => {
    try { await navigator.clipboard.writeText(url); alert('Link copiado!'); }
    catch { window.prompt('Copie o link:', url); }
  };
  return (
    <div className="panel" style={{ background: '#1a2a3a' }}>
      <h3>📨 Convidar jogadores</h3>
      <p style={{ fontSize: 11, color: 'var(--muted)' }}>
        Envie este link/ID. Eles abrem e clicam em "Entrar".
      </p>
      {matchID && (
        <div style={{ background: '#000', padding: 6, borderRadius: 4, fontFamily: 'monospace',
                       fontSize: 11, wordBreak: 'break-all', marginBottom: 6 }}>
          {matchID}
        </div>
      )}
      <button className="tg-btn primary" style={{ width: '100%' }} onClick={copy}>
        📋 Copiar link de convite
      </button>
    </div>
  );
}
