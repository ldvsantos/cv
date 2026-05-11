// As 8 Casas (Seção 5.3 do guia). castelo = território obrigatório com ≥1 token inicial.
// `ability` é o id da habilidade (implementada em ../moves/abilities.js).

export const HOUSES = {
  stark:     { id: 'stark',     name: 'Stark',     sigil: '🐺', color: '#5d6f7c', castle: 'winterfell',   ability: 'forestProtection' },
  greyjoy:   { id: 'greyjoy',   name: 'Greyjoy',   sigil: '🐙', color: '#1d3a4a', castle: 'pyke',         ability: 'maritimeBridge' },
  lannister: { id: 'lannister', name: 'Lannister', sigil: '🦁', color: '#b8860b', castle: 'casterlyRock', ability: 'mineralWealth' },
  tyrell:    { id: 'tyrell',    name: 'Tyrell',    sigil: '🌹', color: '#3a7d44', castle: 'highgarden',   ability: 'fertileGranary' },
  martell:   { id: 'martell',   name: 'Martell',   sigil: '☀',  color: '#d2691e', castle: 'sunspear',     ability: 'aridDefense' },
  arryn:     { id: 'arryn',     name: 'Arryn',     sigil: '🦅', color: '#6b8e9e', castle: 'eyrie',        ability: 'altitudinalGradient' },
  tully:     { id: 'tully',     name: 'Tully',     sigil: '🐟', color: '#2e5c8a', castle: 'riverrun',     ability: 'riparianCorridors' },
  baratheon: { id: 'baratheon', name: 'Baratheon', sigil: '🦌', color: '#5b3a2a', castle: 'stormsEnd',    ability: 'stormResilience' },
};

export const HOUSE_IDS = Object.keys(HOUSES);
export const TOKENS_PER_HOUSE = 6;     // 3 no mapa + 3 reserva
export const INITIAL_MAP_TOKENS = 3;
