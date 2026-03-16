# 🐉 RISK OF LANDSCAPES — Guia do Jogo

## A Guerra pelas Paisagens de Westeros

> *"O verdadeiro poder não está nos exércitos… está na terra, nas florestas, nos rios que alimentam os reinos."*
> — Maester Luwin

---

## 1. Visão Geral

**RISK OF LANDSCAPES** é um *Serious Game* baseado no universo de Game of Thrones, projetado para a disciplina **Análise da Paisagem**. Os jogadores disputam o controle dos territórios de Westeros usando conhecimentos de **Ecologia da Paisagem** — métricas espaciais, fragmentação, conectividade, modelo mancha-corredor-matriz, serviços ecossistêmicos e planejamento territorial.

| Item | Descrição |
|:---|:---|
| **Jogadores** | 2 a 6 |
| **Duração** | 60 – 90 min |
| **Disciplina** | Análise da Paisagem |
| **Temática** | Westeros (Game of Thrones) |
| **Mecânica** | RISK + cartas de desafio paisagístico |

---

## 2. Componentes

| Componente | Quantidade | Descrição |
|:---|:---:|:---|
| Mapa de Westeros | 1 | Tabuleiro com 20 territórios agrupados em 10 macro-regiões |
| Cartas de Território | 20 | Uma por território, com dados paisagísticos e desafio |
| Cartas Narrativas | 80 | 10 por casa (8 casas), cenários temáticos + desafio de paisagem |
| Capas de Casa | 8 | Uma capa identificando cada casa (Stark, Greyjoy, Lannister, Tyrell, Martell, Arryn, Tully, Baratheon) |
| Dados (d6) | 5 | 3 ataque (vermelhos) + 2 defesa (brancos) |
| Tokens de Exército | 6 cores | Peões/dragões para marcar controle |
| Cartas de Missão | 10 | Objetivos secretos de conquista |
| Tokens de Restauração | 30 | Marcadores de bônus por acerto |
| Tabela de Referência | 6 | Uma por jogador, com fórmulas e conceitos |

---

## 3. O Mapa — Macro-regiões e Territórios

O mapa de Westeros é dividido em **10 macro-regiões**, cada uma contendo **2 territórios**:

| Macro-região | Territórios | Perfil paisagístico |
|:---|:---|:---|
| **The North** | Winterfell, The Dreadfort, White Harbor, Moat Cailin | Grandes florestas boreais (Wolfswood, Haunted Forest). Alta cobertura, poucos fragmentos, alta conectividade. |
| **The Vale** | The Eyrie, Gulltown | Florestas montanas isoladas por relevo. Conectividade interna alta, isolamento externo. |
| **The Riverlands** | Riverrun, Harrenhal | Paisagem devastada por guerras e agricultura. Alta fragmentação, muitos fragmentos pequenos, baixa conectividade. |
| **The Westerlands** | Lannisport, Casterly Rock | Mineração intensa fragmentou a cobertura. Trade-off provisão mineral × regulação ecológica. |
| **The Reach** | Highgarden, Oldtown | Celeiro de Westeros. Matriz agrícola dominante, alta diversidade de uso (SHDI alto), baixa cobertura florestal. |
| **The Stormlands** | Storm's End, Shipbreaker Bay | Florestas temperadas sob distúrbio de tempestades. Cobertura moderada, dinâmica de perturbação natural. |
| **Dorne** | Sunspear, Sandstone | Paisagem árida, vegetação esparsa. Matriz desértica de baixa permeabilidade. PLAND muito baixo. |
| **The Crownlands** | King's Landing, Dragonstone | Contraste extremo: capital urbanizada (alta fragmentação) vs. ilha preservada (poucos fragmentos grandes). |
| **Iron Islands** | Pyke, Harlaw | Ilhas rochosas com vegetação mínima. PLAND mais baixo de Westeros. Paisagens abaixo do limiar de percolação. |

---

## 4. Variáveis Paisagísticas das Cartas

Cada carta de território apresenta **9 variáveis** da Ecologia da Paisagem:

| Variável | Sigla | Unidade | O que mede |
|:---|:---:|:---:|:---|
| Cobertura florestal | PLAND | % | Proporção da paisagem coberta por vegetação nativa |
| Número de fragmentos | NP | contagem | Quantidade de manchas de habitat |
| Área média do fragmento | AREA_MN | ha | Tamanho médio das manchas |
| Diversidade de Shannon | SHDI | adimensional | Heterogeneidade composicional da paisagem |
| Conectividade | CONNECT | 0–100 | Grau de conexão funcional entre manchas |
| Densidade de borda | ED | m/ha | Comprimento total de borda por unidade de área |
| Área nuclear | CORE | % | Proporção do habitat protegida de efeito de borda |
| Serviços ecossistêmicos | SE | 0–100 | Índice composto de provisão, regulação e suporte |
| Desafio da Paisagem | — | texto | Questão conceitual sobre Análise da Paisagem |

### Relações esperadas entre variáveis

Os alunos devem perceber as seguintes relações ecológicas nos dados:

- **PLAND ↑ → NP ↓, AREA_MN ↑** — Paisagens com mais cobertura têm menos fragmentos e fragmentos maiores
- **NP ↑ → ED ↑, CORE ↓** — Mais fragmentos geram mais borda e menos área nuclear
- **ED ↑ → CORE ↓** — Densidade de borda e área nuclear são inversamente relacionadas
- **PLAND ↑ → CONNECT ↑ → SE ↑** — Cobertura sustenta conectividade que sustenta serviços
- **SHDI alto pode vir de PLAND alto OU baixo** — Diversidade composicional ≠ cobertura florestal

---

## 5. Regras do Jogo

### 5.1 Preparação

1. **Escolher casa**: cada jogador escolhe uma das 8 casas de Westeros. O baralho de narrativas correspondente (10 cartas) é separado e embaralhado face para baixo.
2. **Distribuir territórios**: embaralhe as 20 cartas de território e distribua igualmente entre os jogadores. Cada jogador coloca 1 exército em cada território recebido.
3. **Exércitos iniciais**: cada jogador recebe exércitos extras conforme o número de jogadores (veja tabela abaixo) e os posiciona nos seus territórios como desejar.
4. **Missão secreta**: cada jogador recebe 1 carta de missão que define seu objetivo de vitória.

| Jogadores | Exércitos iniciais |
|:---:|:---:|
| 2 | 40 |
| 3 | 35 |
| 4 | 30 |
| 5 | 25 |
| 6 | 20 |

### 5.2 Turno de Jogo

Cada turno possui **5 fases**, nesta ordem:

#### Fase 1 — Reforços 🌲

O jogador recebe exércitos extras com base em:

| Fonte | Cálculo |
|:---|:---|
| Territórios controlados | Nº de territórios ÷ 3 (arredonda para baixo, mínimo 3) |
| Bônus de macro-região | Controlar todos os territórios de uma macro-região (ver tabela abaixo) |
| Tokens de Restauração | A cada 3 tokens acumulados, troca por 2 exércitos extras |

**Bônus por macro-região completa:**

| Macro-região | Bônus | Justificativa ecológica |
|:---|:---:|:---|
| The North (4 territórios) | 7 | Maior macro-região; florestas contínuas geram alta resiliência |
| The Vale | 3 | Isolamento montano dificulta conquista, mas limita reforços |
| The Riverlands | 4 | Paisagem fragmentada — fácil de invadir, difícil de manter |
| The Westerlands | 4 | Recursos minerais compensam a degradação |
| The Reach | 5 | Celeiro produtivo: serviços de provisão alimentam exércitos |
| The Stormlands | 3 | Tempestades limitam logística |
| Dorne | 2 | Paisagem árida com baixa capacidade de suporte |
| The Crownlands | 4 | Capital política: poder centralizado |
| Iron Islands | 2 | Ilhas com poucos recursos paisagísticos |

#### Fase 2 — Ataque ⚔️

O jogador pode atacar territórios adjacentes (conectados no mapa). O combate segue as regras clássicas do RISK (dados):

- **Atacante**: lança até 3 dados (precisa ter pelo menos 1 exército a mais do que o número de dados)
- **Defensor**: lança até 2 dados
- **Comparação**: dados ordenados do maior para o menor, comparados par a par. Empate favorece o defensor.

**REGRA ESPECIAL — Vantagem de conectividade:**
Se o território atacante tem **CONNECT ≥ 60**, o atacante pode relançar **1 dado** por tentativa de ataque (paisagens bem conectadas têm melhor logística).

#### Fase 3 — Desafio da Paisagem 🌿

**Esta é a fase pedagógica central do jogo.**

Sempre que um jogador **conquista um território**, ele deve responder ao **Desafio da Paisagem** impresso na carta daquele território. As regras:

1. O jogador lê o desafio em voz alta para o grupo.
2. Tem **2 minutos** para responder, podendo consultar a **Tabela de Referência**.
3. Os demais jogadores e/ou o professor avaliam a resposta.

| Resultado | Consequência |
|:---|:---|
| **Acerto completo** | Ganha **2 Tokens de Restauração** + ocupa o território |
| **Acerto parcial** | Ganha **1 Token de Restauração** + ocupa o território |
| **Erro** | Ocupa o território, mas **perde 1 exército** (degradação ecológica) |

#### Fase 4 — Narrativa da Casa 📜

**Esta é a segunda fase pedagógica do jogo — o Baralho de Narrativas.**

No final de cada turno (mesmo que o jogador não tenha conquistado territórios), ele compra **1 carta narrativa** do baralho da sua casa. O jogador lê a narrativa em voz alta e responde ao desafio:

| Resultado | Consequência |
|:---|:---|
| **Acerto completo** | Ganha **3 Tokens de Restauração** |
| **Acerto parcial** | Ganha **1 Token de Restauração** |
| **Erro** | Perde **1 exército** de um território à sua escolha |

**Regras do Baralho de Narrativas:**
- Cada jogador escolhe uma casa no início do jogo (ver seção 5.1).
- O baralho da casa correspondente (10 cartas) é separado e embaralhado.
- As cartas são progressivas: os desafios vão de conceitos básicos a aplicações avançadas.
- Se acabarem as 10 cartas, o baralho é re-embaralhado.

**As 8 Casas e seus temas paisagísticos:**

| Casa | Sigilo | Região | Tema central |
|:---|:---:|:---|:---|
| 🐺 Stark | Lobo | The North | Florestas contínuas, PLAND alto, conectividade, resiliência |
| 🐙 Greyjoy | Kraken | Iron Islands | Ilhas isoladas, limiar de percolação, biogeografia insular |
| 🦁 Lannister | Leão | The Westerlands | Mineração, trade-off provisão/regulação, dívida de extinção |
| 🌹 Tyrell | Rosa | The Reach | Mosaico agrícola, SHDI alto, polinizadores, corredores de sebes |
| ☀ Martell | Sol | Dorne | Deserto, oásis como stepping stones, aridez, limiar de fragmentação |
| 🦅 Arryn | Falcão | The Vale | Montanhas, gradiente altitudinal, isolamento, cascata de serviços |
| 🐟 Tully | Truta | The Riverlands | Rios fragmentados, matas ripárias, enchentes, degradação por guerra |
| 🦌 Baratheon | Cervo | The Stormlands | Tempestades, fogo natural, resiliência vs. resistência, Tricart |

#### Fase 5 — Manobra (Fortificação) 🏰

O jogador pode mover exércitos entre dois territórios **seus** que estejam conectados por uma cadeia contínua de seus territórios (simula a **conectividade funcional** — só flui onde há continuidade).

---

## 6. Cartas de Missão

| # | Missão | Conceito paisagístico |
|:---:|:---|:---|
| 1 | Controlar The North inteiro | Manter a maior mancha contínua de Westeros |
| 2 | Controlar 3 macro-regiões completas quaisquer | Dominar mosaicos funcionais completos |
| 3 | Controlar Winterfell + Highgarden + Sunspear | Gradiente de paisagens (boreal → agrícola → árida) |
| 4 | Controlar 12 territórios quaisquer | Expandir a cobertura territorial (analogia com PLAND) |
| 5 | Controlar todas as regiões costeiras (White Harbor, Gulltown, Shipbreaker Bay, Sunspear, Pyke, Dragonstone) | Conectividade litoral — corredor costeiro |
| 6 | Eliminar um jogador específico | Extinção competitiva (analogia com exclusão de nicho) |
| 7 | Controlar The Riverlands + The Reach + The Crownlands | Dominar o corredor central de Westeros |
| 8 | Controlar 8 territórios e ter ≥ 5 Tokens de Restauração | Equilíbrio entre conquista e conservação |
| 9 | Controlar Dragonstone + The Eyrie + Winterfell | Dominar as 3 paisagens com maior área nuclear |
| 10 | Controlar todas as Iron Islands + Dorne | Restaurar as paisagens mais degradadas de Westeros |

---

## 7. Tokens de Restauração — Mecânica de Bônus

Os Tokens de Restauração representam o **capital ecológico** acumulado pelo jogador ao demonstrar conhecimento de Análise da Paisagem. Além de trocar por exércitos (3 tokens = 2 exércitos), eles podem ser usados para:

| Uso | Custo | Efeito |
|:---|:---:|:---|
| **Corredor ecológico** | 4 tokens | Conecta dois territórios não adjacentes seus por 1 turno (permite ataque/manobra à distância) |
| **Restauração de habitat** | 3 tokens | Adiciona +2 exércitos a um território com PLAND < 30% |
| **Área protegida** | 5 tokens | Um território seu não pode ser atacado por 1 rodada |
| **Stepping stone** | 2 tokens | Permite mover 1 exército entre dois territórios separados por 1 território inimigo |

---

## 8. Tabela de Referência (uma por jogador)

### Modelo Mancha-Corredor-Matriz
- **Mancha (patch)**: área homogênea que difere do entorno
- **Corredor**: elemento linear conectando manchas
- **Matriz**: elemento dominante e mais conectado ("fundo" da paisagem)

### Métricas-chave
| Métrica | Fórmula / Descrição |
|:---|:---|
| PLAND | $PLAND_i = \frac{\sum a_{ij}}{A} \times 100$ (% da paisagem ocupada pela classe *i*) |
| NP | Número total de manchas da classe |
| AREA_MN | Área total da classe ÷ NP |
| SHDI | $SHDI = -\sum p_i \cdot \ln(p_i)$ (diversidade composicional) |
| ED | Comprimento total de borda ÷ Área total da paisagem |
| CORE | Área interior a X metros da borda ÷ Área total da mancha |

### Limiares importantes
- **Limiar de percolação**: ~59% de habitat em mapas aleatórios
- **Limiar empírico**: 20–30% de habitat → ponto de inflexão para biodiversidade e serviços
- **Relação espécie-área**: $S = cA^z$ (z ≈ 0,25 para fragmentos continentais)

### Serviços ecossistêmicos
- **Provisão**: alimentos, água, madeira, fibras
- **Regulação**: clima, água, erosão, polinização
- **Culturais**: recreação, estética, identidade
- **Suporte**: solo, ciclagem, biodiversidade

### Classificação de Tricart
- **Estável**: pedogênese > morfogênese (usos intensivos possíveis)
- **Intergrade**: equilíbrio frágil (manejo cuidadoso)
- **Instável**: morfogênese > pedogênese (proteção obrigatória)

---

## 9. Gabarito dos Desafios (apenas para o professor)

| Território | Resposta esperada |
|:---|:---|
| **Winterfell** | A **matriz** predomina, pois com 78% de cobertura florestal a vegetação é o elemento mais extenso e conectado da paisagem. O conceito de matriz é definido como o elemento dominante no mosaico. |
| **The Dreadfort** | Mais fragmentada — NP dobrou (12→24) e AREA_MN caiu pela metade (6533→2675). Ambas as métricas apontam na mesma direção: subdivisão do habitat contínuo. |
| **White Harbor** | Com PLAND 45,8% vs. 78,4%, a relação S=cA^z prediz menor riqueza de espécies, pois a área total de habitat disponível é muito menor. A perda não é linear (z≈0,25 = curva côncava). |
| **Moat Cailin** | Função de **filtro/barreira**: ponto estreito entre Norte e Sul que restringe o fluxo de organismos. Funciona como gargalo paisagístico. Pode ser conduto se a cobertura florestal está mantida ao longo do corredor. |
| **The Eyrie** | Montanhas funcionam como barreiras naturais que isolam externamente, mas internamente os vales mantêm cobertura contínua. A conectividade estrutural é alta dentro dos limites montanos porque a topografia concentra os remanescentes em áreas contíguas de difícil acesso. |
| **Gulltown** | Para fragmentos circulares: raio = √(A/π). Com A=921 ha=9,21 km², r≈1,71 km. Borda de 100m: raio interno = 1,61 km, Área nuclear = π(1,61)² = 8,14 km². Core ≈ 88%. Na prática, formas reais são irregulares, então o valor real seria menor (~32% conforme os dados). |
| **Riverrun** | Está no limiar (28% está dentro da faixa 20–30%). Consequências: declínio abrupto de riqueza, perda de conectividade, aumento de extinções locais, comprometimento de serviços de regulação hídrica (especialment crítico nas Riverlands). |
| **Harrenhal** | Alta ED → mais perímetro exposto → mais efeito de borda (alteração microclimática: temperatura, umidade, vento, luminosidade) → menor proporção do fragmento funciona como habitat efetivo (core area). ED e CORE são inversamente proporcionais por mecanismo causal direto. |
| **Lannisport** | Trade-off: a extração de ouro (serviço de provisão) fragmentou a cobertura florestal, reduzindo serviços de regulação (controle de erosão, regulação hídrica, sequestro de carbono). O PIB mineral ignora o valor dos serviços perdidos. |
| **Casterly Rock** | Casterly Rock (SHDI=1,48) é mais heterogênea. Se "bom" ou "ruim" depende do contexto: alta diversidade composicional pode refletir diversidade de usos sustentáveis (positivo) OU fragmentação por conversão (negativo). A interpretação exige conhecer a causa. |
| **Highgarden** | O alto SHDI resulta de múltiplas classes de uso (lavouras diversificadas, pastagens, pomares, vinhedos, fragmentos florestais, rios) típicas de uma paisagem agrícola produtiva. A agricultura diversificada gera alta heterogeneidade composicional mesmo com baixo PLAND de vegetação nativa. |
| **Oldtown** | 12 fragmentos < 50 ha de 52 totais = 23%. Fragmentos abaixo do tamanho mínimo viável funcionam como stepping stones (trampolins ecológicos), mas não sustentam populações residentes de grandes mamíferos. |
| **Storm's End** | Meio **intergrade** (equilíbrio frágil). Tempestades geram distúrbios que mantêm a paisagem em estado intermediário entre estabilidade e instabilidade. A cobertura moderada (55,7%) sugere capacidade de regeneração pós-distúrbio, mas vulnerabilidade a perturbações extremas. |
| **Shipbreaker Bay** | A menor conectividade (44 vs. 72) se explica pela **permeabilidade da matriz**: a matriz costeira (rochas, praias, vegetação arbustiva) é menos favorável ao deslocamento de organismos florestais que os vales internos do Vale. A topografia e o tipo de matriz são determinantes. |
| **Sunspear** | **Regulação hídrica** é a mais crítica em ambientes áridos: com escassez de água, a perda de vegetação reduz infiltração, aumenta escoamento superficial e erosão, comprometendo a disponibilidade de água que é o recurso limitante no ecossistema. |
| **Sandstone** | **Maior para lagartos** — a matriz desértica aberta é o habitat natural de muitas espécies de lagartos (alta permeabilidade), mas é hostil para aves florestais que dependem de cobertura arbórea para deslocamento (baixa permeabilidade). Conectividade funcional é espécie-específica. |
| **King's Landing** | A urbanização cria muitas classes de cobertura (edificações, jardins, praças, hortas, rios canalizados, fragmentos remanescentes) → SHDI alto. Mas cada classe é isolada por infraestrutura impermeável → conectividade baixa. Diversidade composicional ≠ conectividade funcional. |
| **Dragonstone** | **Ambos os lados**: Proteção — o isolamento insular impediu a conversão agrícola/urbana que devastou o continente, preservando manchas grandes com alta área nuclear. Ameaça — o isolamento limita recolonização após extinções, reduz fluxo gênico e aumenta vulnerabilidade a eventos estocásticos (teoria de biogeografia de ilhas). |
| **Pyke** | **Não mantém** — 12,5% está muito abaixo do limiar de percolação (~59%) e mesmo do limiar empírico (20–30%). A paisagem está estruturalmente desconectada. Os 6,8% de área nuclear indicam que quase todo o habitat remanescente sofre efeito de borda severo. |
| **Harlaw** | (a) Priorizar **corredores** ripários (conectam fragmentos existentes) e **stepping stones** (trampolins entre manchas isoladas); (b) Posicionar na **matriz entre os fragmentos maiores** para reconectar primeiramente as manchas com maior viabilidade, maximizando a conectividade funcional com menor área restaurada. |

---

## 10. Conteúdos Abordados

### 10.1 Conteúdos por Carta de Território

| Conteúdo da disciplina | Territórios que abordam |
|:---|:---|
| Modelo mancha-corredor-matriz | Winterfell, Moat Cailin, Harlaw |
| Métricas de composição (PLAND, SHDI) | White Harbor, Casterly Rock, Highgarden, King's Landing |
| Métricas de configuração (NP, ED, CORE) | The Dreadfort, Gulltown, Harrenhal, Oldtown |
| Fragmentação e limiares | Riverrun, Sandstone, Pyke |
| Conectividade (estrutural e funcional) | The Eyrie, Shipbreaker Bay, Sandstone |
| Serviços ecossistêmicos e trade-offs | Lannisport, Sunspear, Highgarden |
| Relação espécie-área | White Harbor, Dragonstone |
| Efeito de borda | Harrenhal, Pyke |
| Classificação de Tricart | Storm's End |
| Restauração ecológica e planejamento | Harlaw, Riverrun |

### 10.2 Conteúdos Abordados pelas Cartas Narrativas por Casa

| Casa | Conteúdos principais (10 cartas) |
|:---|:---|
| **Stark** | Modelo mancha-corredor-matriz, NP vs. AREA_MN, relação espécie-área, funções de corredor, ED vs. Core Area, SHDI, conectividade estrutural/funcional, serviços ecossistêmicos, Tricart, estratégias de restauração |
| **Greyjoy** | Limiar de percolação, comparação quantitativa de métricas, efeito de borda marinha, corredores marinhos vs. terrestres, cálculo de Core Area, paradoxo SHDI×PLAND, populações pequenas e extinção, biogeografia de ilhas, stepping stones |
| **Lannister** | Trade-off provisão/regulação, limiares críticos, ED e ecossistemas aquáticos, SHDI por causas diferentes, meta-população, fragmentação por estradas, índice de forma, restauração em minas, capital natural, dívida de extinção |
| **Tyrell** | SHDI alto com PLAND baixo, cálculo SHDI, sebes como corredores, tamanho mínimo viável, matriz permeável/impermeável, corredor ripário, paisagem complementar, refúgios sazonais, agricultura e serviços, Tricart agrícola |
| **Martell** | Aridez e serviços críticos, conectividade em desertos, conectividade funcional por espécie, alteração hidrológica, limiar contexto-dependente, corredores geomorfológicos, serviços culturais, mudanças climáticas, efeito de borda em zonas áridas, restauração passiva vs. ativa |
| **Arryn** | Relevo e conectividade, métricas 2D vs. 3D, gradiente urbano-montano, índice de forma, isolamento prós/contras, gradiente altitudinal e SHDI, permeabilidade espécie-específica, microclimas e bordas internas, NP como métrica enganosa, serviços em cascata |
| **Tully** | Limiar de fragmentação (20-30%), corredores ripários, cadeia causal da degradação, qualidade da água e cobertura, função esponja, SHDI de degradação, barreiras antrópicas vs. naturais, perda total de serviços, manchas grandes vs. stepping stones, variação sazonal |
| **Baratheon** | Tricart e distúrbio natural, resistência vs. resiliência, tamanho de meta-população, borda marinha ampliada, permeabilidade da matriz, comparação de estratégias, distúrbio natural vs. antrópico, fogo e sucessão, ecotone terra-mar, naturalidade do distúrbio |

---

## 11. Condições de Vitória

O jogo termina quando um jogador completa sua **Missão Secreta**. Ele deve revelar a carta e demonstrar que cumpriu o objetivo.

**Vitória alternativa**: se nenhuma missão for cumprida em 90 minutos, vence o jogador com a maior **Pontuação de Paisagem**:

$$Pontuação = (N_{territorios} \times 3) + (N_{tokens} \times 2) + Bonus_{macro-regiões}$$

---

## 12. Variantes

### 12.1 Modo Cooperativo — "Restauração de Westeros"
Os jogadores trabalham **juntos** contra o tabuleiro. A cada rodada, um "Evento de Degradação" é sorteado (queimada, invasão, seca) que remove exércitos de territórios aleatórios. Os jogadores devem acertar os desafios para ganhar Tokens de Restauração e "curar" os territórios antes que todos caiam.

### 12.2 Modo Debate — "Conselho de Mestres"
Ao conquistar um território, o jogador deve defender sua resposta ao desafio perante os demais jogadores, que podem fazer perguntas. O grupo vota se a resposta é satisfatória. Incentiva argumentação científica oral.

### 12.3 Modo Rápido — "Skirmish"
Usa apenas 10 territórios (um por macro-região, escolhidos aleatoriamente). Jogo em 30–45 minutos.

### 12.4 Modo Narrativa Intensiva — "Crônicas de Westeros"
Cada jogador usa **todas as 10 cartas** da sua casa em sequência obrigatória (Carta 01 → Carta 10). Não se avança para a próxima carta sem acertar a atual. Em compensação, cada acerto completo vale **5 Tokens de Restauração** em vez de 3. O primeiro jogador a completar as 10 cartas da sua casa vence automaticamente.

---

## 13. Impressão e Materiais

Todos os componentes do jogo estão disponíveis em um único arquivo para impressão:

| Arquivo | Conteúdo |
|:---|:---|
| `risk-of-landscapes-print-all.html` | **Arquivo unificado** com todas as cartas (território, missão, referência, narrativas), mapa SVG e painel de controle para impressão seletiva |
| `Cartas_de_Territorio_Paisagens_de_Westeros.csv` | Dados brutos das 20 cartas de território |

**Como imprimir:**
1. Abra `risk-of-landscapes-print-all.html` em um navegador (Chrome recomendado).
2. Use o painel de controle para selecionar quais seções imprimir (Território, Missão, Referência, Mapa, Narrativas).
3. Ctrl+P → Salvar como PDF.
4. **Configurações de impressão**: Margens = Nenhuma; Gráficos de fundo = ✓ habilitado; Tamanho = A4.
5. As cartas têm **71 × 120,5 mm** — 4 cartas por página A4 (grade 2×2).

**Total de cartas para impressão:**

| Tipo | Frente | Verso | Total de folhas A4 |
|:---|:---:|:---:|:---:|
| Território | 20 | 20 | 10 |
| Missão | 10 | 10 | 6 |
| Referência | 2 | 2 | 2 |
| Narrativas + Capas | 88 | — | 22 |
| Mapa | 1 | — | 1 |
| **Total** | | | **~41 folhas A4** |

---

## Créditos

- **Concepção e design pedagógico**: Prof. Luiz Diego Vidal Santos — UEFS
- **Disciplina**: Análise da Paisagem
- **Inspiração mecânica**: RISK / War — Grow
- **Universo temático**: A Song of Ice and Fire (George R. R. Martin)
- **Base teórica**: Forman & Godron (1986), Turner & Gardner (2015), Fahrig (2003), McGarigal & Cushman (2002)

---

*Valar Morghulis — Todas as paisagens mudam. Mas podemos decidir como.*
