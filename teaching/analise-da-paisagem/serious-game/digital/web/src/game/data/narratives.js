// 10 Cartas Narrativas por casa (80 totais).
// Stub inicial: 2 cartas por casa para o MVP funcionar; ampliar depois.
// Estrutura: { id, prompt, level: 'basico'|'intermediario'|'avancado' }

export const NARRATIVES = {
  stark: [
    { id: 'stark-01', level: 'basico',        prompt: 'Bran observa a Wolfswood: a floresta é contínua e atravessa todo o Norte. Que métrica de paisagem (PLAND, NP ou CONNECT) melhor descreve essa observação? Justifique.' },
    { id: 'stark-02', level: 'intermediario', prompt: 'Após a Long Night, 30% das árvores morrem em manchas espalhadas. Como NP, AREA_MN e CORE devem variar? Por quê?' },
  ],
  greyjoy: [
    { id: 'greyjoy-01', level: 'basico',        prompt: 'As Iron Islands têm PLAND de 12-17%. Em termos de limiar de percolação (≈59%), a paisagem está conectada estruturalmente?' },
    { id: 'greyjoy-02', level: 'intermediario', prompt: 'Theon quer restaurar Pyke. Stepping stones são a melhor estratégia em paisagens insulares — explique por que e qual a alternativa inferior.' },
  ],
  lannister: [
    { id: 'lannister-01', level: 'basico',        prompt: 'A mineração de ouro em Casterly Rock aumenta o serviço de provisão. Que serviço(s) tendem a cair em troca? Cite mecanismo.' },
    { id: 'lannister-02', level: 'intermediario', prompt: 'O conceito de dívida de extinção (extinction debt) se aplica às paisagens fragmentadas dos Westerlands? Em que escala temporal?' },
  ],
  tyrell: [
    { id: 'tyrell-01', level: 'basico',        prompt: 'Highgarden tem SHDI = 1,78 e PLAND florestal de 31%. Como uma paisagem agrícola pode ter alta diversidade composicional sem ser florestada?' },
    { id: 'tyrell-02', level: 'intermediario', prompt: 'Sebes (hedgerows) entre lavouras funcionam como qual elemento (mancha, corredor, matriz)? Que serviço ecossistêmico priorizam?' },
  ],
  martell: [
    { id: 'martell-01', level: 'basico',        prompt: 'Em Dorne, oásis funcionam como stepping stones. Defina stepping stone e diga por que é crítico em matriz desértica.' },
    { id: 'martell-02', level: 'intermediario', prompt: 'PLAND em Sunspear é 18,6%. A paisagem ultrapassou o limiar crítico de fragmentação? Que indicador adicional consultaria para confirmar?' },
  ],
  arryn: [
    { id: 'arryn-01', level: 'basico',        prompt: 'O Vale tem CONNECT = 72 mas isolamento externo extremo. Diferencie conectividade estrutural de funcional usando este caso.' },
    { id: 'arryn-02', level: 'intermediario', prompt: 'O gradiente altitudinal do Vale gera cascata de serviços ecossistêmicos. Cite 2 serviços que dependem dessa cascata e o mecanismo.' },
  ],
  tully: [
    { id: 'tully-01', level: 'basico',        prompt: 'Riverrun foi devastada pela guerra. PLAND caiu para 28%. Que função as matas ripárias remanescentes ainda exercem?' },
    { id: 'tully-02', level: 'intermediario', prompt: 'A guerra fragmentou as Riverlands. Compare resistência e resiliência — qual é mais relevante para um plano de recuperação aqui?' },
  ],
  baratheon: [
    { id: 'baratheon-01', level: 'basico',        prompt: "Storm's End sofre tempestades frequentes. Classifique segundo Tricart (estável/intergrade/instável) e justifique." },
    { id: 'baratheon-02', level: 'intermediario', prompt: 'Distúrbios naturais (tempestades, fogo) podem aumentar SHDI. Explique o mecanismo (hipótese do distúrbio intermediário).' },
  ],
};
