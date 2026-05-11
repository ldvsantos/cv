// Auto-derivado de ../../../Cartas_de_Territorio_Paisagens_de_Westeros.csv
// Para regenerar: `npm run build:data`
// Cada território: id, nome, macroRegião, métricas paisagísticas, desafio.

export const TERRITORIES = {
  winterfell: { id: 'winterfell', name: 'Winterfell', macro: 'starks', pland: 78.4, np: 12, areaMn: 6533, shdi: 0.68, connect: 88, ed: 18.5, core: 72.1, se: 85, challenge: 'Winterfell possui 78% de cobertura florestal (Wolfswood). Qual elemento do modelo mancha-corredor-matriz predomina nesta paisagem? Justifique.' },
  dreadfort: { id: 'dreadfort', name: 'The Dreadfort', macro: 'boltons', pland: 64.2, np: 24, areaMn: 2675, shdi: 1.05, connect: 62, ed: 34.8, core: 55.3, se: 68, challenge: 'Compare NP (24) e AREA_MN (2675 ha) com Winterfell. A paisagem de Dreadfort é mais ou menos fragmentada? Justifique com ambas as métricas.' },
  whiteHarbor: { id: 'whiteHarbor', name: 'White Harbor', macro: 'starks', pland: 45.8, np: 38, areaMn: 1205, shdi: 1.42, connect: 41, ed: 48.2, core: 38.6, se: 52, challenge: 'White Harbor tem o menor PLAND de The North. Usando a relação espécie-área (S = cA^z), o que se espera para a biodiversidade local comparada a Winterfell?' },
  moatCailin: { id: 'moatCailin', name: 'Moat Cailin', macro: 'starks', pland: 52.3, np: 31, areaMn: 1688, shdi: 1.28, connect: 48, ed: 42.7, core: 44.2, se: 58, challenge: 'Moat Cailin é um gargalo entre o Norte e o Sul. Que função de corredor (conduto, filtro ou barreira) a paisagem exerce neste ponto estratégico?' },
  eyrie: { id: 'eyrie', name: 'The Eyrie', macro: 'vale', pland: 61.5, np: 18, areaMn: 3417, shdi: 0.92, connect: 72, ed: 28.4, core: 58.7, se: 76, challenge: 'A paisagem do Vale é isolada por montanhas, mas tem alta conectividade interna (72). Explique como o relevo pode aumentar a conectividade estrutural mesmo com PLAND moderado.' },
  gulltown: { id: 'gulltown', name: 'Gulltown', macro: 'vale', pland: 38.7, np: 42, areaMn: 921, shdi: 1.55, connect: 34, ed: 52.6, core: 32.4, se: 48, challenge: 'Gulltown tem 42 fragmentos com área média de 921 ha. Se a largura de borda é 100 m e os fragmentos são circulares, estime a proporção de área nuclear.' },
  riverrun: { id: 'riverrun', name: 'Riverrun', macro: 'riverlands', pland: 28.4, np: 56, areaMn: 507, shdi: 1.85, connect: 18, ed: 68.3, core: 22.5, se: 35, challenge: 'Riverrun tem PLAND de 28%. Esta paisagem ultrapassou o limiar crítico de fragmentação (20-30%)? Que consequências ecológicas esperar?' },
  harrenhal: { id: 'harrenhal', name: 'Harrenhal', macro: 'riverlands', pland: 22.1, np: 62, areaMn: 356.5, shdi: 1.92, connect: 12, ed: 75.4, core: 15.8, se: 28, challenge: 'Harrenhal tem a maior ED (75,4 m/ha) e menor área nuclear (15,8%). Explique a relação causa-efeito entre densidade de borda e área nuclear funcional.' },
  lannisport: { id: 'lannisport', name: 'Lannisport', macro: 'westerlands', pland: 35.6, np: 44, areaMn: 809, shdi: 1.62, connect: 30, ed: 55.8, core: 28.7, se: 42, challenge: 'A mineração fragmentou a paisagem. Identifique o principal trade-off entre serviços de provisão (ouro) e serviços de regulação nesta região.' },
  casterlyRock: { id: 'casterlyRock', name: 'Casterly Rock', macro: 'westerlands', pland: 42.8, np: 36, areaMn: 1189, shdi: 1.48, connect: 38, ed: 49.5, core: 35.4, se: 50, challenge: 'Casterly Rock tem SHDI = 1,48 e Winterfell tem SHDI = 0,68. Qual paisagem é mais heterogênea? Isso é ecologicamente bom ou ruim? Depende de quê?' },
  highgarden: { id: 'highgarden', name: 'Highgarden', macro: 'reach', pland: 31.5, np: 48, areaMn: 656.3, shdi: 1.78, connect: 22, ed: 62.1, core: 24.3, se: 55, challenge: 'Highgarden é o celeiro de Westeros. Por que uma paisagem com alto SHDI (1,78) pode ter baixo PLAND florestal (31,5%)? Relacione com uso agrícola.' },
  oldtown: { id: 'oldtown', name: 'Oldtown', macro: 'reach', pland: 26.8, np: 52, areaMn: 515.4, shdi: 1.88, connect: 16, ed: 70.2, core: 18.9, se: 45, challenge: 'Oldtown tem 52 fragmentos (NP). Se 12 deles têm área < 50 ha, qual a porcentagem de fragmentos abaixo do tamanho mínimo viável para grandes mamíferos?' },
  stormsEnd: { id: 'stormsEnd', name: "Storm's End", macro: 'stormlands', pland: 55.7, np: 22, areaMn: 2531.8, shdi: 1.15, connect: 58, ed: 36.2, core: 48.5, se: 65, challenge: "Storm's End tem tempestades frequentes. Classifique esta paisagem segundo Tricart: meio estável, intergrade ou instável? Justifique." },
  shipbreakerBay: { id: 'shipbreakerBay', name: 'Shipbreaker Bay', macro: 'stormlands', pland: 48.3, np: 28, areaMn: 1725, shdi: 1.35, connect: 44, ed: 44.3, core: 40.8, se: 56, challenge: 'Compare a conectividade de Shipbreaker Bay (44) com a de The Eyrie (72). Que fatores da matriz explicam a diferença?' },
  sunspear: { id: 'sunspear', name: 'Sunspear', macro: 'dorne', pland: 18.6, np: 35, areaMn: 531.4, shdi: 1.72, connect: 15, ed: 58.7, core: 12.4, se: 32, challenge: 'Sunspear tem o menor PLAND do jogo. Em qual categoria de serviço ecossistêmico (provisão, regulação, cultural, suporte) a perda é mais crítica num ambiente árido?' },
  sandstone: { id: 'sandstone', name: 'Sandstone', macro: 'dorne', pland: 24.2, np: 30, areaMn: 807, shdi: 1.58, connect: 20, ed: 53.4, core: 17.6, se: 38, challenge: 'A matriz de Dorne é desértica. A conectividade funcional para lagartos (ectotérmicos) é maior ou menor que para aves florestais? Justifique com permeabilidade da matriz.' },
  kingsLanding: { id: 'kingsLanding', name: "King's Landing", macro: 'crownlands', pland: 20.5, np: 58, areaMn: 353.4, shdi: 1.95, connect: 10, ed: 78.8, core: 13.2, se: 30, challenge: "King's Landing tem a menor conectividade (10) e maior SHDI (1,95). Por que alta diversidade composicional coexiste com baixa conectividade? Relacione com urbanização." },
  dragonstone: { id: 'dragonstone', name: 'Dragonstone', macro: 'crownlands', pland: 56.8, np: 8, areaMn: 7100, shdi: 0.72, connect: 82, ed: 15.2, core: 68.4, se: 74, challenge: 'Dragonstone é uma ilha com 8 fragmentos grandes. Compare com King\'s Landing (58 fragmentos). O isolamento insular protege ou ameaça a biodiversidade? Argumente com ambos os lados.' },
  pyke: { id: 'pyke', name: 'Pyke', macro: 'ironIslands', pland: 12.5, np: 22, areaMn: 568, shdi: 1.65, connect: 8, ed: 62.5, core: 6.8, se: 22, challenge: 'Pyke tem PLAND de 12,5% e área nuclear de apenas 6,8%. Usando o conceito de limiar de percolação, esta paisagem ainda mantém conectividade estrutural?' },
  harlaw: { id: 'harlaw', name: 'Harlaw', macro: 'ironIslands', pland: 16.8, np: 18, areaMn: 933, shdi: 1.52, connect: 14, ed: 54.8, core: 10.5, se: 26, challenge: 'Proponha um plano de restauração ecológica para Harlaw priorizando: (a) qual tipo de elemento restaurar (mancha, corredor ou stepping stone); (b) onde posicioná-lo na paisagem.' },
};

export const TERRITORY_IDS = Object.keys(TERRITORIES);

// Macro-regiões e bônus (Seção 5.2 do guia).
// reservaTokens: tokens da reserva concedidos quando macro completo;
// bonusReroll: relançamento de dado adicional na fase de ataque;
// restorationTokens: tokens de restauração (alternativa para macros de 1 território).
export const MACRO_REGIONS = {
  starks:       { name: "Stark's Region",  reservaTokens: 1, bonusReroll: true,  restorationTokens: 0 },
  boltons:      { name: "Bolton's Region", reservaTokens: 1, bonusReroll: true,  restorationTokens: 0 },
  vale:         { name: 'The Vale',        reservaTokens: 0, bonusReroll: false, restorationTokens: 1 },
  riverlands:   { name: 'The Riverlands',  reservaTokens: 1, bonusReroll: false, restorationTokens: 0 },
  ironIslands:  { name: 'The Iron Islands',reservaTokens: 0, bonusReroll: false, restorationTokens: 1 },
  westerlands:  { name: 'The Westerlands', reservaTokens: 1, bonusReroll: false, restorationTokens: 0 },
  crownlands:   { name: 'The Crownlands',  reservaTokens: 1, bonusReroll: false, restorationTokens: 0 },
  reach:        { name: 'The Reach',       reservaTokens: 1, bonusReroll: true,  restorationTokens: 0 },
  stormlands:   { name: 'The Stormlands',  reservaTokens: 0, bonusReroll: false, restorationTokens: 1 },
  dorne:        { name: 'Dorne',           reservaTokens: 1, bonusReroll: false, restorationTokens: 0 },
};
