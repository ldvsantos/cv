# RISK OF LANDSCAPES — Web Multiplayer

Implementação web em **React + boardgame.io** do *Serious Game* da disciplina
**Análise da Paisagem** (UEFS). Multiplayer real-time via Socket.IO, executável
localmente para piloto em sala e implantável em provedor gratuito (Render.com,
Railway, Fly.io) para uso público.

## Stack

- **boardgame.io** 0.50 — máquina de estados e sincronização multiplayer
- **React 18** + **Vite** — UI e bundling
- **Node.js** — servidor de partidas
- **SVG** puro — mapa estilizado de Westeros (sem deps de mapa)

## Como rodar

```powershell
cd digital/web
npm install
npm run dev          # sobe servidor (8000) + cliente (5173)
```

Abra `http://localhost:5173` em **N abas** (ou em N máquinas da mesma rede),
crie uma partida e cada aba/usuário entra como um jogador.

> Para LAN/sala de aula, substitua `localhost` por `192.168.x.x` (IP do
> notebook do professor). O Vite proxy + boardgame.io já tratam o resto.

## Build de produção

```powershell
npm run build        # gera dist/
npm run server       # servir em produção (configurar PORT, ALLOWED_ORIGINS)
```

## Arquitetura

```
src/
├── game/
│   ├── Game.js                # boardgame.io: setup + moves + phases
│   └── data/
│       ├── territories.js     # 20 territórios + métricas + desafios
│       ├── adjacencies.js     # grafo de Westeros
│       ├── houses.js          # 8 casas + castelos + habilidades
│       ├── narratives.js      # baralhos por casa (stub: 2/casa, alvo: 10/casa)
│       └── mapCoords.js       # coords SVG (viewBox 1000x1400)
├── ui/
│   ├── Lobby.jsx              # criação/entrada de partidas
│   ├── Board.jsx              # tela de jogo (mapa + painel + ações)
│   ├── MapView.jsx            # SVG do mapa
│   └── Modals.jsx             # Desafio da Paisagem + Narrativa
├── App.jsx                    # roteamento Lobby ↔ Board
├── App.css                    # tema dark único
└── main.jsx
server.js                       # boardgame.io master server
```

## Estado do jogo (`G`)

```js
{
  territories: { winterfell: { owner: '0', tokens: 3 }, ... },
  players: {
    '0': {
      house: 'stark',
      reserve: 3, restoration: 0,
      narrativeDeck: [...], narrativeDiscard: [],
      lastChallengeWin: false, lastNarrativeWin: false,
      eliminated: false,
      attacksAccumulated: 0,
      currentAttack: { fromId, toId, committedTokens, dice, phase, ... } | null,
      pendingChallenge: 'highgarden' | null,
      pendingNarrative: 'stark-02' | null,
    },
    ...
  },
  round: 1,
  log: [{ round, msg }, ...]
}
```

## Mecânicas implementadas (v0.1)

| Mecânica | Status | Notas |
|---|---|---|
| Setup com 8 casas + distribuição de territórios | ✅ | Castelo principal sempre garantido |
| Mobilização da reserva (bônus excelência + macro) | ✅ | |
| Reposicionamento entre territórios próprios | ✅ | |
| Ataque P1: Teste de Mobilização (dados acumulados) | ✅ | Falha encerra ataques |
| Ataque P2: Teste do Defensor (média → tokens efetivos) | ✅ | Auto-resolvido |
| Ataque P3: Passa ou Repassa (reroll) | ✅ | Moderador clica resultado |
| Ataque P4: Combate (3v2 dados, empate→def, conquista) | ✅ | Inclui bônus CONNECT≥60 |
| Desafio da Paisagem (modal +2/+1/-1) | ✅ | Mostra todas as métricas |
| Narrativa da Casa (modal +3/+1/sacrifício) | ✅ | Stub: 2 cartas/casa |
| Fortificação com BFS de cadeia própria | ✅ | |
| Troca 3 restauração → 1 token (Lannister: 2→1) | ✅ | |
| Eliminação por captura de castelo | ✅ | |
| Proteção da 1ª rodada para castelos | ✅ | |
| Habilidades especiais dos 8 castelos | ⚠️ parcial | Apenas Lannister; faltam Winterfell, Pyke, etc. |
| Cartas de Missão secretas | ❌ | Vencer = último não-eliminado |
| Bônus de macro (relançar 1 dado por macro de 4 territórios) | ❌ | Apenas reservaTokens implementado |
| Conselheiro (jogador eliminado vira ajudante) | ❌ | UI-only |

## Próximos passos (v0.2)

1. Completar 24 territórios (faltam: Castle Black, Hardhome, Last Hearth, Karhold).
2. Expandir baralhos narrativos para 10 cartas/casa (80 totais).
3. Implementar habilidades restantes (`src/game/moves/abilities.js`).
4. Cartas de Missão secreta (10 objetivos).
5. Telemetria pedagógica: registrar acertos/erros por aluno e exportar CSV.
6. Modo bot (boardgame.io `ai`) para pré-aula / treino solo.
7. Internacionalização (PT/EN/ES) via `i18next`.

## Deploy (sugestão)

- **Frontend** (`dist/`) → Netlify ou Vercel (free)
- **Servidor** (`server.js`) → Render.com Web Service (free) ou Fly.io
- **Persistência** (opcional) → Supabase Postgres + `boardgame.io/server` storage adapter

## Licença

CC-BY 4.0 · Diego L. de V. Santos · UEFS · 2026.
