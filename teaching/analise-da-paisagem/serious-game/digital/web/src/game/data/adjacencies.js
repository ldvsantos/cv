// Grafo de adjacências de Westeros (não-direcionado).
// Baseado na geografia do mapa GOT original. Lista compacta de pares;
// `expand()` produz o dicionário { id: [vizinhos] } usado pela lógica do jogo.

const EDGES = [
  // North core
  ['winterfell', 'whiteHarbor'],
  ['winterfell', 'moatCailin'],
  ['winterfell', 'dreadfort'],
  ['whiteHarbor', 'moatCailin'],
  ['dreadfort', 'moatCailin'],
  // North → Vale / Riverlands
  ['moatCailin', 'riverrun'],
  ['moatCailin', 'eyrie'],
  // Vale
  ['eyrie', 'gulltown'],
  ['gulltown', 'kingsLanding'],
  // Riverlands
  ['riverrun', 'harrenhal'],
  ['riverrun', 'casterlyRock'],
  ['harrenhal', 'kingsLanding'],
  ['harrenhal', 'eyrie'],
  // Westerlands
  ['casterlyRock', 'lannisport'],
  ['casterlyRock', 'highgarden'],
  ['lannisport', 'highgarden'],
  // Iron Islands (insular: ligado a Westerlands costeira)
  ['pyke', 'lannisport'],
  ['pyke', 'harlaw'],
  ['harlaw', 'casterlyRock'],
  // Reach
  ['highgarden', 'oldtown'],
  ['highgarden', 'stormsEnd'],
  ['oldtown', 'sunspear'],
  // Stormlands
  ['stormsEnd', 'shipbreakerBay'],
  ['stormsEnd', 'kingsLanding'],
  ['shipbreakerBay', 'kingsLanding'],
  ['shipbreakerBay', 'dragonstone'],
  // Crownlands
  ['kingsLanding', 'dragonstone'],
  // Dorne
  ['sunspear', 'sandstone'],
  ['sandstone', 'highgarden'],
  ['sandstone', 'stormsEnd'],
];

function expand() {
  const adj = {};
  for (const [a, b] of EDGES) {
    (adj[a] ||= []).push(b);
    (adj[b] ||= []).push(a);
  }
  return adj;
}

export const ADJACENCY = expand();
export const isAdjacent = (a, b) => ADJACENCY[a]?.includes(b) ?? false;
