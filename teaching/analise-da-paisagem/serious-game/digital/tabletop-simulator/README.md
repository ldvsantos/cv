# RISK OF LANDSCAPES — Tabletop Simulator (TTS)

Caminho **mais rápido** para jogar online com a turma. Você gera as cartas a partir
do CSV, sobe um *Custom Deck* no TTS e joga em multiplayer nativo (até 10 jogadores).

## 1. Pré-requisitos

- **Você (professor):** [Tabletop Simulator](https://store.steampowered.com/app/286160/) (~R$ 50 na Steam) e Python 3.10+.
- **Alunos:** TTS na Steam **OU** convite via *Spectator Link* (gratuito, somente leitura — útil para apresentação).

> Alternativa **100 % gratuita e via navegador**: [Screentop.gg](https://screentop.gg).
> Sobe o tabuleiro como imagem, define zonas de carta, distribui baralhos.
> Mesmas cartas geradas aqui funcionam (PNG individual).

## 2. Gerar as cartas (`build_deck.py`)

No terminal, a partir desta pasta:

```powershell
# uma vez:
pip install pillow

# gera /out/cards/*.png  +  /out/deck_sheet.png  (sprite 10x7 para TTS)
python build_deck.py
```

Saída:

```
out/
├── cards/                       # 1 PNG por território (impressão / Screentop)
│   ├── 01_Winterfell.png
│   ├── 02_The_Dreadfort.png
│   └── ...
├── deck_sheet.png               # sprite sheet único (formato Custom Deck do TTS)
└── deck_back.png                # verso comum a todas as cartas
```

## 3. Importar no Tabletop Simulator

1. Crie/abra uma sala.
2. Menu **Objects → Components → Custom → Deck**.
3. Em **Face**, aponte para `out/deck_sheet.png` (URL local ou Steam Cloud).
4. Em **Back**, aponte para `out/deck_back.png`.
5. Defina **Width = 5**, **Height = 4** (20 cartas → grade 5×4). Marque
   *Unique Backs* = **off**.
6. Clique em **Import**. O baralho aparece na mesa.

## 4. Importar no Screentop.gg

1. Novo *Room* → **Add Component → Deck**.
2. Faça upload da pasta `out/cards/` (arrasta tudo de uma vez).
3. Defina o verso `out/deck_back.png`.
4. Compartilhe a URL da sala com os alunos. Pronto.

## 5. Mapa de Westeros

O TTS aceita o PDF/AI já existente:

- Exporte `../Mapa (GOT original).pdf` como PNG (300 dpi) →
  use como **Custom Table** ou **Custom Tile** (Body).
- Adjacências e fronteiras são interpretadas visualmente pelos jogadores
  (o professor arbitra dúvidas usando a Seção 3 do guia).

## 6. Tokens e dados

- TTS já tem dados d6 nativos (3 vermelhos + 2 brancos por jogador).
- Tokens: use **figuras 3D padrão** (peões coloridos) ou suba os SVGs
  de `../SVG/` como *Custom Figurines*.

## 7. Roteiro de mediação para o piloto (~90 min)

| Tempo | Atividade |
|---|---|
| 0–10 | Distribuir casas, missões secretas, posicionar 3 tokens iniciais |
| 10–70 | 4–6 turnos completos (mediador lê desafios e arbitra acertos) |
| 70–85 | Rodada final + apuração de pontuação |
| 85–90 | Aplicar formulário de feedback (Google Forms) |

## 8. Formulário de feedback (modelo)

Reaproveite a estrutura de `scripts/google_forms/atividades_analise_paisagem/atividade_07.json`.
Perguntas mínimas:

1. Clareza das regras (Likert 1–5)
2. Equilíbrio entre sorte (dados) e conhecimento (desafios) (1–5)
3. Tempo de partida adequado? (curto / ok / longo)
4. Quais conceitos de Ecologia da Paisagem foram **realmente** revisados?
5. Bug / regra ambígua que apareceu na sessão (texto livre)
6. Recomendaria a versão **web** (sem precisar Steam)? (sim / não / talvez)
