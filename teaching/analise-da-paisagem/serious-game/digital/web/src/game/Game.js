// Lógica central de Risk of Landscapes — definida via boardgame.io.
// Estado (G):
//   territories: { [id]: { owner: playerId|null, tokens: number } }
//   players:     { [pid]: { house, reserve, restoration, narrativeDeck:[],
//                           narrativeDiscard:[], lastChallengeWin, lastNarrativeWin,
//                           eliminated, attacksAccumulated, currentAttack } }
//   round, log
// turn.phases: setup → mobilization → attack → fortify (challenge/narrative entram inline)

import { TERRITORIES, TERRITORY_IDS, MACRO_REGIONS } from './data/territories.js';
import { ADJACENCY, isAdjacent } from './data/adjacencies.js';
import { HOUSES, INITIAL_MAP_TOKENS, TOKENS_PER_HOUSE } from './data/houses.js';
import { NARRATIVES } from './data/narratives.js';

const TURN_ORDER = { first: () => 0, next: ({ ctx }) => (ctx.playOrderPos + 1) % ctx.numPlayers };

// ───────────────────────────── helpers ──────────────────────────────────────

const log = (G, msg) => {
  G.log.push({ round: G.round, msg });
  if (G.log.length > 60) G.log.shift();
};

const shuffle = (random, arr) => random.Shuffle([...arr]);

const ownedTerritories = (G, pid) =>
  TERRITORY_IDS.filter((t) => G.territories[t].owner === pid);

const controlsMacro = (G, pid, macroId) => {
  const inMacro = TERRITORY_IDS.filter((t) => TERRITORIES[t].macro === macroId);
  return inMacro.every((t) => G.territories[t].owner === pid);
};

const completedMacros = (G, pid) =>
  Object.keys(MACRO_REGIONS).filter((m) => controlsMacro(G, pid, m));

const totalTokensOnMap = (G, pid) =>
  ownedTerritories(G, pid).reduce((s, t) => s + G.territories[t].tokens, 0);

const checkElimination = (G, pid) => {
  const p = G.players[pid];
  if (p.eliminated) return;
  // Eliminado se castelo principal foi tomado.
  const castle = HOUSES[p.house].castle;
  if (G.territories[castle].owner !== pid) {
    p.eliminated = true;
    log(G, `☠️ ${HOUSES[p.house].name} foi eliminado (perdeu ${castle}).`);
  }
};

// ───────────────────────────── setup ────────────────────────────────────────

function setupGame({ ctx, random }) {
  // distribui casas (ordem da playOrder) e territórios.
  const houseIds = shuffle(random, Object.keys(HOUSES)).slice(0, ctx.numPlayers);
  const territoriesShuffled = shuffle(random, TERRITORY_IDS);
  const perPlayer = Math.floor(territoriesShuffled.length / ctx.numPlayers);

  const players = {};
  const territories = {};
  for (const t of TERRITORY_IDS) territories[t] = { owner: null, tokens: 0 };

  for (let i = 0; i < ctx.numPlayers; i++) {
    const pid = String(i);
    const house = houseIds[i];
    const myTerritories = territoriesShuffled.slice(i * perPlayer, (i + 1) * perPlayer);
    // garante que o castelo principal vá para o jogador
    const castle = HOUSES[house].castle;
    if (!myTerritories.includes(castle)) {
      myTerritories[0] = castle; // sobrescreve para garantir
    }
    for (const t of myTerritories) territories[t].owner = pid;

    // posiciona INITIAL_MAP_TOKENS, ≥1 no castelo
    territories[castle].tokens = 1;
    let remaining = INITIAL_MAP_TOKENS - 1;
    const others = myTerritories.filter((t) => t !== castle);
    let i2 = 0;
    while (remaining > 0 && others.length) {
      territories[others[i2 % others.length]].tokens += 1;
      remaining -= 1;
      i2 += 1;
    }

    players[pid] = {
      house,
      reserve: TOKENS_PER_HOUSE - INITIAL_MAP_TOKENS,
      restoration: 0,
      narrativeDeck: shuffle(random, NARRATIVES[house].map((c) => c.id)),
      narrativeDiscard: [],
      lastChallengeWin: false,
      lastNarrativeWin: false,
      eliminated: false,
      attacksAccumulated: 0,
      currentAttack: null,
      pendingChallenge: null,
      pendingNarrative: null,
    };
  }

  return {
    territories,
    players,
    round: 1,
    lastDice: null,
    log: [{ round: 1, msg: '🎲 Partida iniciada.' }],
  };
}

// ───────────────────────────── moves ────────────────────────────────────────

const moves = {
  // FASE 1 — Mobilização
  mobilizeReserve: ({ G, playerID }, targetTerritory, qty = 1) => {
    const p = G.players[playerID];
    if (G.territories[targetTerritory].owner !== playerID) return 'INVALID_MOVE';
    if (p.reserve < qty) return 'INVALID_MOVE';
    // Direito = 1 básico + bônus de macros + bônus de excelência (desafio E narrativa)
    const macros = completedMacros(G, playerID);
    const bonusMacros = macros.reduce((s, m) => s + MACRO_REGIONS[m].reservaTokens, 0);
    const bonusExcel = (p.lastChallengeWin && p.lastNarrativeWin) ? 1 : 0;
    const cap = 1 + bonusMacros + bonusExcel;
    p.tokensMobilizedThisTurn = (p.tokensMobilizedThisTurn || 0);
    if (p.tokensMobilizedThisTurn + qty > cap) return 'INVALID_MOVE';
    G.territories[targetTerritory].tokens += qty;
    p.reserve -= qty;
    p.tokensMobilizedThisTurn += qty;
    log(G, `${HOUSES[p.house].name} mobilizou ${qty} para ${TERRITORIES[targetTerritory].name}.`);
  },

  redeployReserve: ({ G, playerID }, fromId, toId, qty) => {
    // Reposiciona tokens entre territórios próprios (não usa reserva).
    const p = G.players[playerID];
    if (G.territories[fromId].owner !== playerID) return 'INVALID_MOVE';
    if (G.territories[toId].owner !== playerID) return 'INVALID_MOVE';
    if (G.territories[fromId].tokens - qty < 1) return 'INVALID_MOVE';
    G.territories[fromId].tokens -= qty;
    G.territories[toId].tokens += qty;
    log(G, `${HOUSES[p.house].name} reposicionou ${qty} tokens.`);
  },

  // FASE 2 — Ataque (Passo 1: Teste de Mobilização do Atacante)
  declareAttack: ({ G, playerID, random }, fromId, toId, committedTokens) => {
    const p = G.players[playerID];
    if (G.territories[fromId].owner !== playerID) return 'INVALID_MOVE';
    if (!isAdjacent(fromId, toId)) return 'INVALID_MOVE';
    if (committedTokens < 1 || committedTokens > 3) return 'INVALID_MOVE';
    if (G.territories[fromId].tokens - committedTokens < 1) return 'INVALID_MOVE';

    // Proteção da 1ª rodada: castelos de oponentes.
    const targetOwner = G.territories[toId].owner;
    if (G.round === 1 && targetOwner !== null) {
      const targetHouse = G.players[targetOwner].house;
      if (HOUSES[targetHouse].castle === toId) {
        log(G, `🛡️ Castelo ${TERRITORIES[toId].name} protegido na 1ª rodada.`);
        return 'INVALID_MOVE';
      }
    }

    // Passo 1: lança 1 dado por token comprometido, calcula média.
    const dice = Array.from({ length: committedTokens }, () => random.D6());
    const avg = dice.reduce((s, d) => s + d, 0) / dice.length;
    const required = p.attacksAccumulated + committedTokens;

    if (avg < required) {
      log(G, `❌ ${HOUSES[p.house].name} falhou mobilização (média ${avg.toFixed(1)} < ${required}). Rodada de ataques encerrada.`);
      G.lastDice = { kind: 'mobilizationFail', dice, avg, required, by: HOUSES[p.house].name };
      p.attacksAccumulated = Infinity;
      return;
    }

    p.attacksAccumulated += committedTokens;
    p.currentAttack = {
      fromId, toId, committedTokens,
      mobilizationDice: dice, mobilizationAvg: avg, mobilizationRequired: required,
      defenderDice: null, defenderAvg: null, defenderEffective: null,
      attackerCombatDice: null, defenderCombatDice: null,
      attackerLost: 0, defenderLost: 0,
      phase: 'defenderTest',
      attackerReroll: false, defenderReroll: false,
      conquered: false,
    };
    G.lastDice = null;
    log(G, `⚔️ ${HOUSES[p.house].name} ataca ${TERRITORIES[toId].name} com ${committedTokens} (média ${avg.toFixed(1)} ≥ ${required}).`);
  },

  // Passo 2: Teste de Mobilização do Defensor (chamado pelo defensor OU auto se neutro)
  resolveDefenderTest: ({ G, random }, attackerPid) => {
    const p = G.players[attackerPid];
    const atk = p.currentAttack;
    if (!atk || atk.phase !== 'defenderTest') return 'INVALID_MOVE';
    const defenderOwner = G.territories[atk.toId].owner;

    // Neutro/desguarnecido: pula direto para desafio (não há combate).
    const defenderTokens = G.territories[atk.toId].tokens;
    if (defenderOwner === null || defenderTokens === 0) {
      atk.defenderEffective = 0;
      atk.defenderDice = [];
      atk.phase = 'challenge';
      return;
    }
    const nDice = Math.min(2, defenderTokens);
    const defDice = Array.from({ length: nDice }, () => random.D6());
    const avg = defDice.reduce((s, d) => s + d, 0) / nDice;
    atk.defenderDice = defDice;
    atk.defenderAvg = avg;
    atk.defenderEffective = Math.max(1, Math.floor(avg));
    atk.phase = 'challenge';
    log(G, `🛡️ Defensor mobilizou ${atk.defenderEffective} dado(s) (média ${avg.toFixed(1)}).`);
  },

  // Passo 3: Passa ou Repassa — moderador (host) marca quem acertou.
  resolveChallenge: ({ G }, attackerPid, result /* 'attacker' | 'defender' | 'none' */) => {
    const p = G.players[attackerPid];
    const atk = p.currentAttack;
    if (!atk || atk.phase !== 'challenge') return 'INVALID_MOVE';
    if (result === 'attacker') atk.attackerReroll = true;
    if (result === 'defender') atk.defenderReroll = true;
    if (result === 'none') {
      // ambos perderam 1 token de restauração (se tiverem)
      const def = G.territories[atk.toId].owner;
      if (p.restoration > 0) p.restoration -= 1;
      if (def !== null && G.players[def].restoration > 0) G.players[def].restoration -= 1;
    }
    atk.phase = 'combat';
    log(G, `📚 Passa ou Repassa: ${result === 'none' ? 'ambos erraram' : result + ' acertou'}.`);
  },

  // Passo 4: Combate
  resolveCombat: ({ G, random }, attackerPid) => {
    const p = G.players[attackerPid];
    const atk = p.currentAttack;
    if (!atk || atk.phase !== 'combat') return 'INVALID_MOVE';

    const rollWithReroll = (n, allowReroll) => {
      let dice = Array.from({ length: n }, () => random.D6());
      if (allowReroll) {
        // re-rola o pior dado
        const min = Math.min(...dice);
        const idx = dice.indexOf(min);
        dice[idx] = random.D6();
      }
      return dice.sort((a, b) => b - a);
    };

    // Bônus de conectividade (CONNECT ≥ 60 do território de origem)
    const connectBonus = TERRITORIES[atk.fromId].connect >= 60;
    const aRerolls = (atk.attackerReroll ? 1 : 0) + (connectBonus ? 1 : 0);

    let aDice = Array.from({ length: atk.committedTokens }, () => random.D6());
    for (let i = 0; i < aRerolls; i++) {
      const min = Math.min(...aDice);
      const idx = aDice.indexOf(min);
      aDice[idx] = random.D6();
    }
    aDice = aDice.sort((a, b) => b - a).slice(0, 3);

    const defenderTokens = G.territories[atk.toId].tokens;
    let dDice = [];
    if (defenderTokens > 0) {
      const nDice = Math.min(2, atk.defenderEffective);
      dDice = rollWithReroll(nDice, atk.defenderReroll);
    }

    let aLost = 0, dLost = 0;
    const pairs = Math.min(aDice.length, dDice.length);
    for (let i = 0; i < pairs; i++) {
      // empate favorece defensor
      if (aDice[i] > dDice[i]) dLost += 1;
      else aLost += 1;
    }

    const defenderPid = G.territories[atk.toId].owner;
    G.territories[atk.fromId].tokens -= aLost;
    p.reserve += aLost; // tokens recuados voltam à reserva
    if (defenderPid !== null) {
      G.territories[atk.toId].tokens -= dLost;
      G.players[defenderPid].reserve += dLost;
    }

    log(G, `🎲 Atacante [${aDice.join(',')}] vs Defensor [${dDice.join(',')}] → A perde ${aLost}, D perde ${dLost}.`);
    atk.attackerCombatDice = aDice;
    atk.defenderCombatDice = dDice;
    atk.attackerLost = aLost;
    atk.defenderLost = dLost;

    // Conquista?
    if (G.territories[atk.toId].tokens === 0 && atk.committedTokens - aLost > 0) {
      // captura tokens restantes (na verdade já são 0; carta passa de mão)
      G.territories[atk.toId].owner = attackerPid;
      // move 1 token para o conquistado
      G.territories[atk.fromId].tokens -= 1;
      G.territories[atk.toId].tokens = 1;
      log(G, `🏆 ${HOUSES[p.house].name} conquistou ${TERRITORIES[atk.toId].name}.`);
      // gatilho de desafio da paisagem (Fase 3)
      p.pendingChallenge = atk.toId;
      atk.conquered = true;
      // se era castelo, eliminação acontece em checkAll
      if (defenderPid !== null) checkElimination(G, defenderPid);
    }
    // mantém currentAttack para UI mostrar resultado; usuário limpa com move 'closeAttackSummary'
    atk.phase = 'resolved';
  },

  // Limpa o resumo do ataque após o jogador ler os dados
  closeAttackSummary: ({ G, playerID }) => {
    const p = G.players[playerID];
    if (p.currentAttack && p.currentAttack.phase === 'resolved') {
      p.currentAttack = null;
    }
  },

  // FASE 3 — Desafio da Paisagem (resultado avaliado por moderador)
  resolveLandscapeChallenge: ({ G, playerID }, result /* 'full'|'partial'|'wrong' */) => {
    const p = G.players[playerID];
    if (!p.pendingChallenge) return 'INVALID_MOVE';
    const tId = p.pendingChallenge;
    if (result === 'full')    { p.restoration += 2; p.lastChallengeWin = true; }
    if (result === 'partial') { p.restoration += 1; p.lastChallengeWin = true; }
    if (result === 'wrong')   {
      // 1 token volta à reserva
      if (G.territories[tId].tokens > 0) {
        G.territories[tId].tokens -= 1;
        p.reserve += 1;
      }
      p.lastChallengeWin = false;
    }
    log(G, `🌿 Desafio (${TERRITORIES[tId].name}): ${result}.`);
    p.pendingChallenge = null;
  },

  // FASE 4 — Narrativa da Casa (compra carta no fim do turno)
  drawNarrative: ({ G, playerID, random }) => {
    const p = G.players[playerID];
    if (p.pendingNarrative) return 'INVALID_MOVE';
    if (p.narrativeDeck.length === 0) {
      p.narrativeDeck = random.Shuffle([...p.narrativeDiscard]);
      p.narrativeDiscard = [];
    }
    const cardId = p.narrativeDeck.shift();
    p.pendingNarrative = cardId;
    log(G, `📜 ${HOUSES[p.house].name} comprou narrativa.`);
  },

  resolveNarrative: ({ G, playerID }, result /* 'full'|'partial'|'wrong' */, sacrificeTerritory) => {
    const p = G.players[playerID];
    if (!p.pendingNarrative) return 'INVALID_MOVE';
    if (result === 'full')    { p.restoration += 3; p.lastNarrativeWin = true; }
    if (result === 'partial') { p.restoration += 1; p.lastNarrativeWin = true; }
    if (result === 'wrong')   {
      if (sacrificeTerritory && G.territories[sacrificeTerritory].owner === playerID
          && G.territories[sacrificeTerritory].tokens > 0) {
        G.territories[sacrificeTerritory].tokens -= 1;
        p.reserve += 1;
      }
      p.lastNarrativeWin = false;
    }
    p.narrativeDiscard.push(p.pendingNarrative);
    p.pendingNarrative = null;
    log(G, `📜 Narrativa: ${result}.`);
  },

  // Troca 3 Tokens de Restauração → 1 token na reserva colocado em território
  exchangeRestoration: ({ G, playerID }, targetTerritory) => {
    const p = G.players[playerID];
    const cost = HOUSES[p.house].ability === 'mineralWealth' ? 2 : 3;
    if (p.restoration < cost) return 'INVALID_MOVE';
    if (G.territories[targetTerritory].owner !== playerID) return 'INVALID_MOVE';
    if (p.reserve < 1) return 'INVALID_MOVE';
    p.restoration -= cost;
    p.reserve -= 1;
    G.territories[targetTerritory].tokens += 1;
    log(G, `♻️ ${HOUSES[p.house].name} trocou ${cost} restauração por 1 token em ${TERRITORIES[targetTerritory].name}.`);
  },

  // FASE 5 — Fortificação
  fortify: ({ G, playerID }, fromId, toId, qty) => {
    const p = G.players[playerID];
    if (G.territories[fromId].owner !== playerID) return 'INVALID_MOVE';
    if (G.territories[toId].owner !== playerID) return 'INVALID_MOVE';
    if (G.territories[fromId].tokens - qty < 1) return 'INVALID_MOVE';
    if (qty < 1) return 'INVALID_MOVE';
    // exige cadeia de territórios próprios — verificação BFS
    const visited = new Set([fromId]);
    const queue = [fromId];
    let ok = false;
    while (queue.length) {
      const cur = queue.shift();
      if (cur === toId) { ok = true; break; }
      for (const n of (ADJACENCY[cur] || [])) {
        if (!visited.has(n) && G.territories[n].owner === playerID) {
          visited.add(n); queue.push(n);
        }
      }
    }
    if (!ok) return 'INVALID_MOVE';
    G.territories[fromId].tokens -= qty;
    G.territories[toId].tokens += qty;
    log(G, `🏰 Fortificou ${TERRITORIES[toId].name} com ${qty}.`);
  },

  endTurn: ({ events, G, playerID }) => {
    // reset flags de excelência para o próximo turno
    const p = G.players[playerID];
    p.attacksAccumulated = 0;
    p.currentAttack = null;
    p.tokensMobilizedThisTurn = 0;
    // Não limpa lastChallengeWin/lastNarrativeWin: a mobilização do PRÓXIMO turno
    // depende do RESULTADO deste turno. Limpamos no início do próximo (via onTurnBegin).
    events.endTurn();
  },
};

// ───────────────────────────── definition ───────────────────────────────────

export const RiskOfLandscapes = {
  name: 'risk-of-landscapes',
  minPlayers: 2,
  maxPlayers: 6,

  setup: setupGame,
  moves,
  turn: {
    order: TURN_ORDER,
    onBegin: ({ G, ctx }) => {
      // após mobilização inicial usar o estado, então só limpa DEPOIS de mobilizar.
      // aqui marcamos a rodada se completou ciclo
      if (ctx.playOrderPos === 0 && ctx.turn > 1) G.round += 1;
    },
    onEnd: ({ G, ctx }) => {
      const pid = ctx.currentPlayer;
      const p = G.players[pid];
      // limpa flags para próximo turno deste jogador
      p.lastChallengeWin = false;
      p.lastNarrativeWin = false;
    },
  },

  endIf: ({ G, ctx }) => {
    const alive = Object.entries(G.players).filter(([, p]) => !p.eliminated);
    if (alive.length === 1) return { winner: alive[0][0] };
  },
};

export { TERRITORIES, MACRO_REGIONS, ADJACENCY, HOUSES, NARRATIVES };
