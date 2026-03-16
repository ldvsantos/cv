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
| Mapa de Westeros | 1 | Tabuleiro com 24 territórios agrupados em 11 macro-regiões |
| Cartas de Território | 24 | Uma por território, com dados paisagísticos e desafio |
| Cartas Narrativas | 80 | 10 por casa (8 casas), cenários temáticos + desafio de paisagem |
| Capas de Casa | 8 | Uma capa identificando cada casa (Stark, Greyjoy, Lannister, Tyrell, Martell, Arryn, Tully, Baratheon) |
| Dados (d6) | 5 | 3 ataque (vermelhos) + 2 defesa (brancos) |
| Tokens de Exército | 6 cores | Peões/dragões para marcar controle |
| Cartas de Missão | 10 | Objetivos secretos de conquista |
| Tokens de Restauração | 30 | Marcadores de bônus por acerto |
| Tabela de Referência | 6 | Uma por jogador, com fórmulas e conceitos |

---

## 3. O Mapa — Macro-regiões e Territórios

O mapa de Westeros é dividido em **11 macro-regiões**, totalizando **24 territórios**:

| Macro-região | Terr. | Territórios | Perfil paisagístico |
|:---|:---:|:---|:---|
| **Beyond the Wall** | 2 | Castle Black, Hardhome | Tundra e floresta boreal extrema. Paisagem selvagem sem intervenção antrópica. Conectividade natural máxima; barreira climática como fator limitante. |
| **Stark's Region** | 4 | Winterfell, White Harbor, Moat Cailin, Last Hearth | Grandes florestas boreais (Wolfswood, Haunted Forest). Alta cobertura, poucos fragmentos, alta conectividade. |
| **Bolton's Region** | 3 | The Dreadfort, Karhold, Barrowlands | Paisagem de transição: florestas fragmentadas por ocupação militar. Fragmentação crescente do norte ao sul; contraste com Stark's Region. |
| **The Vale** | 1 | The Eyrie | Fortaleza montana isolada por relevo. Conectividade interna alta, isolamento externo extremo. |
| **The Riverlands** | 2 | Riverrun, Harrenhal | Paisagem devastada por guerras e agricultura. Alta fragmentação, muitos fragmentos pequenos, baixa conectividade. |
| **The Iron Islands** | 1 | Pyke | Ilha rochosa com vegetação mínima. PLAND mais baixo de Westeros. Abaixo do limiar de percolação. |
| **The Westerlands** | 2 | Casterly Rock, Lannisport | Mineração intensa fragmentou a cobertura. Trade-off provisão mineral × regulação ecológica. |
| **The Crownlands** | 2 | King's Landing, Dragonstone | Contraste extremo: capital urbanizada (alta fragmentação) vs. ilha preservada (poucos fragmentos grandes). |
| **The Reach** | 4 | Highgarden, Oldtown, Horn Hill, Ashford | Celeiro de Westeros. Matriz agrícola dominante, alta diversidade de uso (SHDI alto), gradiente de paisagens rurais. |
| **The Stormlands** | 1 | Storm's End | Floresta temperada sob distúrbio de tempestades. Cobertura moderada, dinâmica de perturbação natural (Tricart intergrade). |
| **Dorne** | 2 | Sunspear, Sandstone | Paisagem árida, vegetação esparsa. Matriz desértica de baixa permeabilidade. PLAND muito baixo. |

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

> **Regra fundamental:** Cada casa possui **6 tokens físicos**. Todos começam com **3 tokens no mapa**. Os outros 3 ficam na **reserva pessoal** (ao lado do jogador) e só podem ser mobilizados por **mérito** (acertar desafios ou trocar Tokens de Restauração). **Cartas de território** = posse. **Tokens no mapa** = força militar.

1. **Escolher casa**: cada jogador escolhe uma das 8 casas de Westeros. Recebe os 6 tokens da sua cor, o baralho de narrativas correspondente (10 cartas, embaralhado face para baixo) e a **carta de Castelo** da casa.
2. **Distribuir territórios**: embaralhe as 24 cartas de território e distribua igualmente (veja tabela). Territórios restantes ficam **neutros** (sem dono e sem tokens).
3. **Posicionar tokens**: cada jogador coloca **3 tokens no mapa** livremente entre seus territórios, com uma obrigação: o **Castelo Principal** da sua casa deve receber **pelo menos 1 token**. Os outros **3 ficam na reserva**.
4. **Missão secreta**: cada jogador recebe 1 carta de missão que define seu objetivo de vitória.

| Jogadores | Territórios/jogador | Territórios neutros | No mapa | Na reserva | Total |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 2 | 8 | 8 | 3 | 3 | 6 |
| 3 | 6 | 6 | 3 | 3 | 6 |
| 4 | 5 | 4 | 3 | 3 | 6 |
| 5 | 4 | 4 | 3 | 3 | 6 |
| 6 | 3 | 6 | 3 | 3 | 6 |

**Territórios neutros:** não pertencem a ninguém. Podem ser conquistados sem combate (basta mover 1 token), mas o jogador deve responder ao Desafio da Paisagem.

**Posse sem token:** um território sem nenhum token continua pertencendo ao dono da carta, mas está **desguarnecido** — qualquer adversário adjacente pode invadi-lo sem lançar dados respondendo uma carta desafio (ocupação automática). O novo dono fica com a carta.

**🛡️ Proteção inicial:** Durante a **primeira rodada completa** (primeiro turno de cada jogador), **castelos principais não podem ser atacados**. Isso garante que todos tenham pelo menos 1 turno para se posicionar estrategicamente.

### 5.2 Turno de Jogo

Cada turno possui **5 fases**, nesta ordem:

#### Fase 1 — Mobilização (Reforços) 🌲

No início de cada turno, o jogador pode:

1. **Reposicionar tokens** livremente entre seus territórios conectados (como a antiga Manobra).
2. **Mobilizar tokens da reserva**, mas **somente** se tiver ganho esse direito:

| Fonte | Quando pode mobilizar |
|:---|:---|
| Bônus de Excelência (turno anterior) | Acertou Desafio + Narrativa no turno anterior → coloca **1 token da reserva** em qualquer território seu |
| Bônus de macro-região | Controlar todos os territórios de uma macro-região → coloca **1 token da reserva** |
| Tokens de Restauração | Troca **3 Tokens de Restauração** → coloca **1 token da reserva** no mapa |
| Habilidade de Castelo | Algumas habilidades de castelo permitem mobilização especial (ver Seção 5.3) |

> **⚠️ Reserva vazia = sem reforço.** Se o jogador não tem tokens na reserva, não pode mobilizar nenhum. Tokens capturados de outros jogadores também vão para a reserva e podem ser mobilizados normalmente.

**Bônus por macro-região completa:**

| Macro-região | Terr. | Bônus | Justificativa ecológica |
|:---|:---:|:---:|:---|
| Beyond the Wall (2) | 2 | +1 token da reserva | Paisagem selvagem = recursos naturais intocados |
| Stark's Region (4) | 4 | +1 token da reserva + relançar 1 dado | Maior macro-região; florestas contínuas geram alta resiliência |
| Bolton's Region (3) | 3 | +1 token da reserva + relançar 1 dado | Região extensa; fragmentação oferece posições defensivas |
| The Vale (1) | 1 | +1 Token de Restauração | Controle automático; fortaleza natural compensa |
| The Riverlands (2) | 2 | +1 token da reserva | Posição central: corredores fluviais conectam |
| The Iron Islands (1) | 1 | +1 Token de Restauração | Controle automático; recursos insulares escassos |
| The Westerlands (2) | 2 | +1 token da reserva | Recursos minerais compensam a degradação |
| The Crownlands (2) | 2 | +1 token da reserva | Capital política: poder centralizado |
| The Reach (4) | 4 | +1 token da reserva + relançar 1 dado | Região extensa; celeiro produtivo de Westeros |
| The Stormlands (1) | 1 | +1 Token de Restauração | Controle automático; resiliência pós-distúrbio |
| Dorne (2) | 2 | +1 token da reserva | Paisagem árida com baixa capacidade de suporte |

> **Nota:** Macro-regiões com **1 território** concedem seu bônus automaticamente a quem controlar aquele território. Para compensar a facilidade, recebem **+1 Token de Restauração** (em vez de +1 token da reserva).

#### Fase 2 — Ataque ⚔️

O jogador pode atacar territórios adjacentes (conectados no mapa). Cada tentativa de ataque segue **4 passos obrigatórios**:

##### Passo 1 — Teste de Mobilização do Atacante 🎲

Antes de atacar, o jogador deve provar capacidade logística para mobilizar suas forças:

1. Escolhe quantos tokens compromete no ataque (1 a 3), deixando sempre **≥1 no território de origem**.
2. Lança **1 dado por token comprometido**.
3. Calcula a **média**: soma dos dados ÷ nº de dados.
4. A média deve ser **≥ total acumulado de tokens já movimentados em ataques nesta rodada** (soma de TODOS os ataques anteriores + o atual).

| Situação | Tokens | Dados | Média | Acumulado exigido | Resultado |
|:---|:---|:---|:---|:---|:---|
| 1º ataque | 2 | (4, 5) | 4,5 | ≥ 2 | ✅ Passa |
| 2º ataque | 1 | (2) | 2,0 | ≥ 3 (2+1) | ❌ Falha |
| 2º ataque | 1 | (5) | 5,0 | ≥ 3 (2+1) | ✅ Passa |
| 3º ataque | 2 | (3, 6) | 4,5 | ≥ 5 (2+1+2) | ❌ Falha |

- ✅ **Passa** → avança para o Passo 2.
- ❌ **Falha** → ataque cancelado. **Rodada de ataques encerrada** (não pode tentar mais ataques neste turno).

> **Efeito estratégico:** cada ataque consecutivo exige média mais alta. Comprometer poucos tokens mantém o acumulado baixo (mais ataques possíveis, porém mais fracos). Comprometer muitos é mais forte, mas eleva o patamar rapidamente. **Isso impede dominação rápida e força decisões táticas**, mesmo para o aluno que domina o conteúdo.

##### Passo 2 — Teste de Mobilização do Defensor 🛡️

O defensor testa a capacidade de organizar sua defesa:

1. Lança dados igual ao nº de tokens no território (**máximo 2 dados**, mínimo 1).
2. Calcula a **média**: soma ÷ nº de dados.
3. Tokens efetivos para defesa = **⌊média⌋** (arredondado para baixo, **mínimo 1**).
4. O defensor usará **dados = tokens efetivos** no combate (máximo 2).

| Tokens no território | Dados | Média | Tokens efetivos (dados no combate) |
|:---|:---|:---|:---|
| 3 | (5, 4) | 4,5 → 4 | 2 (máx. dados defesa) |
| 3 | (2, 1) | 1,5 → 1 | **1** (mobilização fraca!) |
| 2 | (3, 6) | 4,5 → 4 | 2 |
| 2 | (1, 2) | 1,5 → 1 | **1** |
| 1 | (4) | 4,0 | 1 |

> **Efeito estratégico:** mesmo um território "forte" (3 tokens) pode ter defesa enfraquecida por má mobilização — simula surpresa tática ou desorganização. O defensor **não pode contar automaticamente com toda sua guarnição**.

##### Passo 3 — Passa ou Repassa 📚

Antes do combate, um **desafio educacional obrigatório** no formato *Passa ou Repassa*:

1. O professor (ou jogador designado) lê uma **pergunta** da carta do território atacado.
2. O **atacante responde primeiro**:
   - ✅ **Acertou** → ganha o direito de **relançar 1 dado** no combate (escolhe qual após ver o resultado).
   - ❌ **Errou ou passou** → a pergunta é **repassada ao defensor**.
3. Se repassada ao defensor:
   - ✅ **Defensor acertou** → defensor ganha o direito de **relançar 1 dado** no combate.
   - ❌ **Ambos erraram** → combate sem bônus. Ambos perdem **1 Token de Restauração** (se tiverem) — ignorância degrada a paisagem!

> **Efeito pedagógico:** a cada tentativa de ataque, pelo menos 1 jogador é forçado a responder sobre Ecologia da Paisagem. Mesmo ataques fracassados geram aprendizado. Combinado com o Teste de Mobilização, **impede que conhecimento sozinho garanta dominação**.

##### Passo 4 — Resolução do Combate ⚔️

1. **Atacante** lança novos dados = tokens comprometidos (máximo **3 dados**).
2. **Defensor** lança novos dados = **tokens efetivos** do Passo 2 (máximo **2 dados**).
3. Quem venceu o **Passa ou Repassa** pode **relançar 1 dado** à sua escolha (fica com o melhor resultado).
4. Dados ordenados do **maior ao menor**, comparados **par a par**. **Empate favorece o defensor.**
5. **Perdedor** de cada par **remove 1 token** → retorna para a **reserva pessoal** do dono.
6. **Território a 0 tokens** → **conquistado**: atacante move ≥1 token e pega a carta.

---

**🏆 Captura de tokens:** ao conquistar, o atacante **captura todos os tokens restantes** do defensor ali — vão para a **reserva do atacante**. Um jogador agressivo pode acumular **mais de 6 tokens** ao longo do jogo! (Representam tropas capturadas / recursos saqueados.)

**Conquistar território neutro:** o Teste de Mobilização (Passo 1) se aplica e **conta no acumulado da rodada**, mas **não há Teste do Defensor, Passa ou Repassa, nem combate**. Basta mover 1 token. Deve responder ao Desafio da Paisagem (Fase 3).

**Conquistar território desguarnecido (0 tokens):** mesmo procedimento do neutro — Teste de Mobilização, ocupação automática, move 1 token e pega a carta. Deve responder ao Desafio.

**REGRA ESPECIAL — Vantagem de conectividade:**
Se o território atacante tem **CONNECT ≥ 60**, o atacante pode relançar **1 dado adicional** por tentativa de ataque (paisagens bem conectadas têm melhor logística). Esse bônus é **cumulativo** com o do Passa ou Repassa — o atacante pode relançar até **2 dados** no total.

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
| **Erro** | Ocupa o território, mas **1 token volta para a reserva** (degradação ecológica) |

#### Fase 4 — Narrativa da Casa 📜

**Esta é a segunda fase pedagógica do jogo — o Baralho de Narrativas.**

No final de cada turno (mesmo que o jogador não tenha conquistado territórios), ele compra **1 carta narrativa** do baralho da sua casa. O jogador lê a narrativa em voz alta e responde ao desafio:

| Resultado | Consequência |
|:---|:---|
| **Acerto completo** | Ganha **3 Tokens de Restauração** |
| **Acerto parcial** | Ganha **1 Token de Restauração** |
| **Erro** | **1 token** de um território à sua escolha **volta para a reserva** |

**Regras do Baralho de Narrativas:**
- O baralho da casa correspondente (10 cartas) é separado e embaralhado no início.
- As cartas são progressivas: os desafios vão de conceitos básicos a aplicações avançadas.
- Se acabarem as 10 cartas, o baralho é re-embaralhado.

> **🎯 BÔNUS DE EXCELÊNCIA** — Se no mesmo turno o jogador acertou **completamente** pelo menos 1 Desafio da Paisagem (Fase 3) **E** a Narrativa da Casa (Fase 4), ele pode imediatamente **mobilizar 1 token da reserva** para qualquer território seu. Esta é a **principal forma de crescer suas forças** — recompensa o conhecimento de Ecologia da Paisagem!

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

#### Fase 5 — Fortificação 🏰

O jogador pode realizar **uma** transferência de tokens entre dois territórios **seus** conectados por cadeia contínua de territórios próprios (simula a **conectividade funcional** — só flui onde há continuidade). Pode mover quantos tokens quiser nessa transferência.

> **⚠️ Atenção:** território com 0 tokens fica **desguarnecido** e pode ser invadido automaticamente. Não é permitido devolver tokens ao reserva nesta fase — tokens só voltam à reserva por recuo em combate, erro em desafio, ou habilidade especial.

---

### 5.3 Regra do Castelo (Regra Coringa) 👑

Cada casa possui um **Castelo Principal** — o território-capital da sua região. Esta é a mecânica mais importante do jogo:

| Casa | Castelo Principal |
|:---|:---|
| 🐺 Stark | Winterfell |
| 🐙 Greyjoy | Pyke |
| 🦁 Lannister | Casterly Rock |
| 🌹 Tyrell | Highgarden |
| ☀ Martell | Sunspear |
| 🦅 Arryn | The Eyrie |
| 🐟 Tully | Riverrun |
| 🦌 Baratheon | Storm's End |

**Eliminação por Castelo:** Se um jogador conquista o Castelo Principal de um oponente, **esse oponente é eliminado do jogo**, independentemente de quantos territórios e tokens ele ainda possua. O conquistador recebe:

- ✅ **Todos os territórios** (cartas) do eliminado
- ✅ **Todos os tokens** do eliminado (mapa + reserva) — passa a usar ambos os conjuntos de peças
- ✅ A **habilidade especial** do castelo conquistado (acumulativa com as que já possui)

**Proteção inicial:** Na primeira rodada completa, castelos não podem ser atacados.

**Jogador eliminado como Conselheiro:** O jogador eliminado não sai da mesa — ele se torna **Conselheiro** do conquistador, podendo ajudar a responder os desafios das cartas. Isso mantém o engajamento pedagógico e promove aprendizado cooperativo.

#### Habilidades Especiais dos Castelos

Cada castelo oferece uma vantagem única baseada na ecologia da paisagem local. Há **trade-offs**: quem tem abundância de um recurso tem escassez de outro — refletindo os serviços ecossistêmicos reais.

| Castelo | Habilidade | Base Ecológica | Trade-off |
|:---|:---|:---|:---|
| **Winterfell** | **Proteção Florestal**: +1 dado de defesa em todos os territórios de Stark's Region | PLAND 78% = cobertura florestal contínua oferece cobertura defensiva natural | Posição periférica ao norte, longe dos centros de recursos |
| **Pyke** | **Ponte Marítima**: pode atacar/mover tokens para qualquer território costeiro, mesmo não adjacente | Stepping stones oceânicos = dispersão marítima entre ilhas | PLAND 12,5% = território próprio extremamente frágil |
| **Casterly Rock** | **Riqueza Mineral**: troca apenas **2** Tokens de Restauração (em vez de 3) para mobilizar 1 token | SE alto de provisão = recursos minerais abundantes | CONNECT 38 = baixa conectividade, sem bônus de relançamento |
| **Highgarden** | **Celeiro Fértil**: ganha **+1 Token de Restauração** extra em qualquer acerto (completo ou parcial) de desafio | SHDI alto = matriz agrícola diversificada, produção abundante | PLAND 22% = pouca vegetação nativa, território ecologicamente frágil |
| **Sunspear** | **Defesa Árida**: o primeiro ataque contra Sunspear em cada rodada **falha automaticamente** | Deserto como barreira natural, custos logísticos extremos de invasão | SE 25 = pouquíssimos serviços ecossistêmicos, sem bônus produtivo |
| **The Eyrie** | **Fortaleza Montana**: The Eyrie só pode ser atacada se o atacante tiver **≥3 tokens** no território de origem | Isolamento montano = barreira topográfica extrema que dificulta acesso | Poucos territórios na macro-região, difícil expandir |
| **Riverrun** | **Corredores Fluviais**: territórios do Riverlands são considerados adjacentes a **qualquer território que faça fronteira com rios** | Rios como corredores ecológicos de alta conectividade linear | PLAND 28% = no limiar de fragmentação, território inerentemente vulnerável |
| **Storm's End** | **Resiliência**: ao perder 1 token em combate, jogue 1 dado — resultado **5 ou 6** = o token permanece no mapa | Tricart intergrade = capacidade natural de recuperação pós-distúrbio | Posição geográfica mediana, sem vantagem posicional forte |

---

## 6. Cartas de Missão

| # | Missão | Conceito paisagístico |
|:---:|:---|:---|
| 1 | Controlar Stark's Region inteira (4 terr.) | Manter a maior mancha contínua de Westeros |
| 2 | Controlar 3 macro-regiões completas quaisquer | Dominar mosaicos funcionais completos |
| 3 | Controlar Winterfell + Highgarden + Sunspear | Gradiente de paisagens (boreal → agrícola → árida) |
| 4 | Controlar 12 territórios quaisquer | Expandir a cobertura territorial (analogia com PLAND) |
| 5 | Controlar todas as regiões costeiras (White Harbor, Hardhome, Sunspear, Pyke, Dragonstone, Oldtown) | Conectividade litoral — corredor costeiro |
| 6 | Conquistar o Castelo Principal de um jogador específico | Extinção competitiva (analogia com exclusão de nicho) |
| 7 | Controlar The Riverlands + The Reach + The Crownlands (8 terr.) | Dominar o corredor central de Westeros |
| 8 | Controlar 8 territórios e ter ≥ 5 Tokens de Restauração | Equilíbrio entre conquista e conservação |
| 9 | Controlar Dragonstone + The Eyrie + Winterfell | Dominar as 3 paisagens com maior área nuclear |
| 10 | Controlar Beyond the Wall + Dorne (4 terr.) | Conectar extremos climáticos — restaurar paisagens extremas |

---

## 7. Tokens de Restauração — Mecânica de Bônus

Os Tokens de Restauração representam o **capital ecológico** acumulado pelo jogador ao demonstrar conhecimento de Análise da Paisagem. A principal função é trocar por mobilização de tokens da reserva (3 Tokens de Restauração = 1 token da reserva no mapa, ou 2 se possuir Casterly Rock). Além disso, podem ser usados para habilidades especiais:

| Uso | Custo | Efeito |
|:---|:---:|:---|
| **Mobilizar token** | 3 tokens | Coloca 1 token da reserva em qualquer território seu (2 se tiver Casterly Rock) |
| **Corredor ecológico** | 4 tokens | Conecta dois territórios não adjacentes seus por 1 turno (permite ataque/manobra à distância) |
| **Área protegida** | 5 tokens | Um território seu não pode ser atacado por 1 rodada |
| **Stepping stone** | 2 tokens | Permite mover 1 token entre dois territórios separados por 1 território inimigo |

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
| **Castle Black** | A Muralha funciona como **barreira ecológica artificial**: impede o fluxo de organismos entre Norte e Sul. Apesar de PLAND altíssimo (>85%), a conectividade funcional é bloqueada na direção norte-sul. A barreira evidencia que conectividade estrutural ≠ conectividade funcional. |
| **Hardhome** | Paisagem **sem fragmentação antrópica**: PLAND próximo de 90%, pouquíssimos fragmentos, todos grandes. Serve como **referência (controle)** para comparar com paisagens degradadas ao sul. Demonstra o estado pré-perturbação do ecossistema boreal. |
| **Winterfell** | A **matriz** predomina, pois com 78% de cobertura florestal a vegetação é o elemento mais extenso e conectado da paisagem. O conceito de matriz é definido como o elemento dominante no mosaico. |
| **White Harbor** | Com PLAND 45,8% vs. 78,4%, a relação S=cA^z prediz menor riqueza de espécies, pois a área total de habitat disponível é muito menor. A perda não é linear (z≈0,25 = curva côncava). |
| **Moat Cailin** | Função de **filtro/barreira**: ponto estreito entre Norte e Sul que restringe o fluxo de organismos. Funciona como gargalo paisagístico. Pode ser conduto se a cobertura florestal está mantida ao longo do corredor. |
| **Last Hearth** | Paisagem de **transição boreal**: PLAND 65% marca a fronteira onde a cobertura contínua começa a se fragmentar. Demonstra o conceito de **gradiente latitudinal** — a paisagem muda progressivamente com a latitude, e com ela mudam as métricas. |
| **The Dreadfort** | Mais fragmentada — NP dobrou (12→24) e AREA_MN caiu pela metade (6533→2675). Ambas as métricas apontam na mesma direção: subdivisão do habitat contínuo. |
| **Karhold** | Paisagem com **fragmentação intermediária**: PLAND ~40%, NP moderado. Demonstra a relação **não-linear** entre perda de habitat e número de fragmentos — a fragmentação se acelera na faixa 30-60% de PLAND (curva em sino de NP). |
| **Barrowlands** | Planícies com **fragmentos residuais** em matriz agrícola. Contraste com Bolton's Dreadfort demonstra como a distância à fonte (floresta boreal do norte) afeta a recolonização — **teoria de metapopulações** (efeito resgate). |
| **The Eyrie** | Montanhas funcionam como barreiras naturais que isolam externamente, mas internamente os vales mantêm cobertura contínua. A conectividade estrutural é alta dentro dos limites montanos porque a topografia concentra os remanescentes em áreas contíguas de difícil acesso. |
| **Riverrun** | Está no limiar (28% está dentro da faixa 20–30%). Consequências: declínio abrupto de riqueza, perda de conectividade, aumento de extinções locais, comprometimento de serviços de regulação hídrica (especialmente crítico nas Riverlands). |
| **Harrenhal** | Alta ED → mais perímetro exposto → mais efeito de borda (alteração microclimática: temperatura, umidade, vento, luminosidade) → menor proporção do fragmento funciona como habitat efetivo (core area). ED e CORE são inversamente proporcionais por mecanismo causal direto. |
| **Pyke** | **Não mantém** — 12,5% está muito abaixo do limiar de percolação (~59%) e mesmo do limiar empírico (20–30%). A paisagem está estruturalmente desconectada. Os 6,8% de área nuclear indicam que quase todo o habitat remanescente sofre efeito de borda severo. |
| **Casterly Rock** | Casterly Rock (SHDI=1,48) é mais heterogênea. Se "bom" ou "ruim" depende do contexto: alta diversidade composicional pode refletir diversidade de usos sustentáveis (positivo) OU fragmentação por conversão (negativo). A interpretação exige conhecer a causa. |
| **Lannisport** | Trade-off: a extração de ouro (serviço de provisão) fragmentou a cobertura florestal, reduzindo serviços de regulação (controle de erosão, regulação hídrica, sequestro de carbono). O PIB mineral ignora o valor dos serviços perdidos. |
| **King's Landing** | A urbanização cria muitas classes de cobertura (edificações, jardins, praças, hortas, rios canalizados, fragmentos remanescentes) → SHDI alto. Mas cada classe é isolada por infraestrutura impermeável → conectividade baixa. Diversidade composicional ≠ conectividade funcional. |
| **Dragonstone** | **Ambos os lados**: Proteção — o isolamento insular impediu a conversão agrícola/urbana que devastou o continente, preservando manchas grandes com alta área nuclear. Ameaça — o isolamento limita recolonização após extinções, reduz fluxo gênico e aumenta vulnerabilidade a eventos estocásticos (teoria de biogeografia de ilhas). |
| **Highgarden** | O alto SHDI resulta de múltiplas classes de uso (lavouras diversificadas, pastagens, pomares, vinhedos, fragmentos florestais, rios) típicas de uma paisagem agrícola produtiva. A agricultura diversificada gera alta heterogeneidade composicional mesmo com baixo PLAND de vegetação nativa. |
| **Oldtown** | 12 fragmentos < 50 ha de 52 totais = 23%. Fragmentos abaixo do tamanho mínimo viável funcionam como stepping stones (trampolins ecológicos), mas não sustentam populações residentes de grandes mamíferos. |
| **Horn Hill** | Zona de **transição floresta-campo**: PLAND ~35%, ED alta. Demonstra o conceito de **ecótono** — faixa de transição entre dois ecossistemas com propriedades emergentes (maior diversidade de borda, espécies generalistas). |
| **Ashford** | Paisagem agrícola com **corredores de sebes** (hedgerows). SHDI alto, CONNECT moderado. As sebes funcionam como corredores ecológicos lineares para invertebrados e aves, compensando parcialmente a fragmentação. Conceito de **paisagem complementar**. |
| **Storm's End** | Meio **intergrade** (equilíbrio frágil). Tempestades geram distúrbios que mantêm a paisagem em estado intermediário entre estabilidade e instabilidade. A cobertura moderada (55,7%) sugere capacidade de regeneração pós-distúrbio, mas vulnerabilidade a perturbações extremas. |
| **Sunspear** | **Regulação hídrica** é a mais crítica em ambientes áridos: com escassez de água, a perda de vegetação reduz infiltração, aumenta escoamento superficial e erosão, comprometendo a disponibilidade de água que é o recurso limitante no ecossistema. |
| **Sandstone** | **Maior para lagartos** — a matriz desértica aberta é o habitat natural de muitas espécies de lagartos (alta permeabilidade), mas é hostil para aves florestais que dependem de cobertura arbórea para deslocamento (baixa permeabilidade). Conectividade funcional é espécie-específica. |

---

## 10. Conteúdos Abordados

### 10.1 Conteúdos por Carta de Território

| Conteúdo da disciplina | Territórios que abordam |
|:---|:---|
| Modelo mancha-corredor-matriz | Winterfell, Moat Cailin, Ashford |
| Métricas de composição (PLAND, SHDI) | White Harbor, Casterly Rock, Highgarden, King's Landing, Last Hearth |
| Métricas de configuração (NP, ED, CORE) | The Dreadfort, Karhold, Harrenhal, Oldtown, Horn Hill |
| Fragmentação e limiares | Riverrun, Sandstone, Pyke, Karhold |
| Conectividade (estrutural e funcional) | The Eyrie, Castle Black, Sandstone |
| Serviços ecossistêmicos e trade-offs | Lannisport, Sunspear, Highgarden |
| Relação espécie-área | White Harbor, Dragonstone |
| Efeito de borda | Harrenhal, Pyke, Horn Hill |
| Classificação de Tricart | Storm's End |
| Restauração ecológica e planejamento | Barrowlands, Riverrun |
| Paisagem de referência (controle) | Hardhome, Castle Black |
| Ecótono e gradiente | Last Hearth, Horn Hill |
| Metapopulações e efeito resgate | Barrowlands, Karhold |
| Paisagem complementar e corredores de sebes | Ashford |

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

O jogo termina quando:

1. **Missão Secreta cumprida**: um jogador revela a carta e demonstra que cumpriu o objetivo. **Vitória imediata.**
2. **Dominação total**: um jogador elimina todos os outros via Regra do Castelo. **Vitória automática.**
3. **Tempo esgotado**: se nenhuma missão for cumprida em 90 minutos, vence o jogador com a maior **Pontuação de Paisagem**:

$$Pontuação = (N_{territorios} \times 3) + (N_{tokens\_no\_mapa} \times 2) + (N_{castelos} \times 5) + Bonus_{macro-regi\tilde{o}es}$$

---

## 12. Variantes

### 12.1 Modo Cooperativo — "Restauração de Westeros"
Os jogadores trabalham **juntos** contra o tabuleiro. A cada rodada, um “Evento de Degradação” é sorteado (queimada, invasão, seca) que remove tokens de territórios aleatórios. Os jogadores devem acertar os desafios para ganhar Tokens de Restauração e “curar” os territórios antes que todos caiam.

### 12.2 Modo Debate — "Conselho de Mestres"
Ao conquistar um território, o jogador deve defender sua resposta ao desafio perante os demais jogadores, que podem fazer perguntas. O grupo vota se a resposta é satisfatória. Incentiva argumentação científica oral.

### 12.3 Modo Rápido — "Skirmish"
Usa apenas 11 territórios (um por macro-região, escolhidos aleatoriamente). Jogo em 30–45 minutos.

### 12.4 Modo Narrativa Intensiva — "Crônicas de Westeros"
Cada jogador usa **todas as 10 cartas** da sua casa em sequência obrigatória (Carta 01 → Carta 10). Não se avança para a próxima carta sem acertar a atual. Em compensação, cada acerto completo vale **5 Tokens de Restauração** em vez de 3. O primeiro jogador a completar as 10 cartas da sua casa vence automaticamente.

---

## 13. Impressão e Materiais

Todos os componentes do jogo estão disponíveis em um único arquivo para impressão:

| Arquivo | Conteúdo |
|:---|:---|
| `risk-of-landscapes-print-all.html` | **Arquivo unificado** com todas as cartas (território, missão, referência, narrativas), mapa SVG e painel de controle para impressão seletiva |
| `Cartas_de_Territorio_Paisagens_de_Westeros.csv` | Dados brutos das 24 cartas de território |

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
