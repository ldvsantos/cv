/**
 * ============================================================
 *  ANALISE DA PAISAGEM 2026.1 — Reorganização dos Google Forms
 * ============================================================
 *
 *  O que este script faz, em UMA execução:
 *    1) Renomeia os formulários existentes (titulo + descricao):
 *         Atividade 02 -> Atividade 03
 *         Atividade 03 -> Atividade 04
 *         Atividade 04 -> Atividade 05
 *         Atividade 05 -> Atividade 06
 *         Atividade 06 -> Atividade 07
 *         Atividade 07 -> Atividade 08
 *    2) Cria a NOVA Atividade 02 — "Envio das Apresentações do Seminário"
 *       (fica na pasta indicada por FOLDER_ID; se vazio, vai para "Meu Drive").
 *
 *  COMO USAR
 *  ---------
 *  A) Pré-requisito: estar logado em ldvsantos@uefs.br.
 *  B) Acesse https://script.google.com -> Novo projeto -> cole este arquivo.
 *  C) Preencha os IDs em FORM_IDS abaixo (um por atividade existente 02..07).
 *     - Para descobrir o ID de cada Form: abra o Form, copie do URL o trecho
 *       entre /d/ e /edit, ou use o método 1 abaixo (LISTAR_FORMS_DO_DRIVE).
 *  D) (Opcional) Cole o ID de uma pasta do Drive em FOLDER_ID para organizar.
 *  E) Salve, escolha a função "executarTudo" e clique em ▶ Executar.
 *     Autorize os escopos Drive + Forms quando solicitado.
 *
 *  OBSERVAÇÕES
 *  -----------
 *  - O script NÃO altera as perguntas existentes; apenas renomeia titulo/descricao
 *    dos forms 02..07 e cria o novo Form 02.
 *  - É reentrante: se você já renomeou algum, ele detecta pelo padrão atual e
 *    pula sem duplicar prefixos.
 *  - O upload de arquivo no Google Forms exige que o respondente esteja logado
 *    em uma conta Google, e os arquivos vão para uma pasta criada pelo Forms
 *    no Drive do PROPRIETÁRIO do formulário.
 */

// ==== AJUSTE AQUI =========================================================
const FORM_IDS = {
  // chave  = NOVO número de atividade (após o shift)
  // valor  = ID do Form que HOJE está com o número antigo (chave - 1)
  '03': '1l8oOX1VOS76NAi-AOzSOpvVNlLn36COWnpStqTDRDZ0', // hoje: Atividade 02 — Geossistema, ECL e MCM
  '04': '1wfO176DLftksxDUGtpyDWHQo1fYUdcX_5WkoAI1kREc', // hoje: Atividade 03 — Escalas, Fragmentação e Resiliência
  '05': '1hBynSWyQWyMA-HfuajzQ0ZewSFFM5FKFB0w3alpCNOE', // hoje: Atividade 04 — Cartografia e Interpretação Visual
  '06': '1bMcN_dboUmwu2he7T6DMPoRk121iLE1sy6PF3XRTGS0', // hoje: Atividade 05 — SR: do Pixel à Paisagem
  '07': '1XRZlXYvekKgVqJE4MWtW_HvOZIm0ouAWJO1ErUjLHE8', // hoje: Atividade 06 — FRAGSTATS, Grafos e Conectividade
  '08': '1ldpBU-oTivThjYkHIxIewHsQnEIOmTzp1laEgoWUIL4', // hoje: Atividade 07 — Diagnóstico, Zoneamento e Diretrizes
};

// (Opcional) Pasta do Drive onde o NOVO Form 02 será movido.
// Cole o ID que aparece no URL da pasta: /folders/<ID>
const FOLDER_ID = ''; // ex.: '1AbCdEfGhIjKlMnOpQrStUvWxYz'

// ID do Form 02 já criado (preenchido a partir do log da execução anterior).
const FORM_02_EXISTENTE_ID = '15oiKuws4k4VaHROy7AcXIpptCznQsf-LhqrKwNVOHb8';

// ==========================================================================

/**
 * Função principal — execute esta APENAS na primeira vez (cria Form 02 + renomeia).
 * Se o Form 02 já existe, use 'apenasRenomear' + 'corrigirTituloForm02'.
 */
function executarTudo() {
  const log = [];
  log.push('--- 1/2 Renomeando forms existentes ---');
  log.push(renomearFormsExistentes());
  log.push('--- 2/2 Criando NOVA Atividade 02 ---');
  log.push(criarAtividade02_Seminario());
  Logger.log(log.join('\n\n'));
}

/**
 * Roda APENAS o shift de títulos 02..07 -> 03..08 (sem criar novo Form 02).
 * Use depois de preencher FORM_IDS.
 */
function apenasRenomear() {
  Logger.log(renomearFormsExistentes());
}

/**
 * Corrige o título e a descrição do Form 02 já criado anteriormente.
 * Preencha FORM_02_EXISTENTE_ID acima e execute.
 */
function corrigirTituloForm02() {
  if (!FORM_02_EXISTENTE_ID) {
    Logger.log('Preencha FORM_02_EXISTENTE_ID no topo do arquivo.');
    return;
  }
  const titulo = 'Atividade 02 — Envio das Apresentações do Seminário';
  const descricao = textoDescricao02_();
  const form = FormApp.openById(FORM_02_EXISTENTE_ID);
  form.setTitle(titulo);
  form.setDescription(descricao);
  // Renomeia o arquivo no Drive (o nome no Drive não acompanha setTitle automaticamente)
  try {
    DriveApp.getFileById(FORM_02_EXISTENTE_ID).setName(titulo);
  } catch (e) {
    Logger.log('Aviso: não foi possível renomear o arquivo no Drive: ' + e);
  }
  Logger.log('Form 02 atualizado:\n  Título: ' + form.getTitle() + '\n  Editar: ' + form.getEditUrl());
}

/**
 * Renomeia os Forms 02..07 para 03..08, ajustando título e descrição.
 */
function renomearFormsExistentes() {
  const ordem = ['08', '07', '06', '05', '04', '03']; // do maior para o menor
  const out = [];
  ordem.forEach(novo => {
    const id = FORM_IDS[novo];
    if (!id || id.indexOf('COLE_AQUI') === 0) {
      out.push(`[ ] Atividade ${novo}: ID não preenchido — pulando.`);
      return;
    }
    try {
      const form = FormApp.openById(id);
      const tituloAtual = form.getTitle();
      const descAtual = form.getDescription() || '';
      const antigo = pad2(parseInt(novo, 10) - 1);

      // Substitui rótulos "Atividade NN" e "ATIVIDADE NN" no título e na descrição
      const novoTitulo = substituirRotulos(tituloAtual, antigo, novo);
      const novaDesc = substituirRotulos(descAtual, antigo, novo);

      if (novoTitulo !== tituloAtual) form.setTitle(novoTitulo);
      if (novaDesc !== descAtual) form.setDescription(novaDesc);

      out.push(`[OK] ${id}\n     Título: "${tituloAtual}"\n      ->     "${novoTitulo}"`);
    } catch (e) {
      out.push(`[ERRO] Atividade ${novo} (id=${id}): ${e}`);
    }
  });
  return out.join('\n');
}

/**
 * Cria o NOVO Form da Atividade 02 — Envio das Apresentações do Seminário.
 */
function criarAtividade02_Seminario() {
  const titulo = 'Atividade 02 — Envio das Apresentações do Seminário';
  const descricao = textoDescricao02_();

  // Cria, depois força título e descrição (workaround para casos em que o
  // construtor não fixa o título corretamente quando há cadeia longa).
  const form = FormApp.create(titulo);
  form.setTitle(titulo);
  form.setDescription(descricao);
  form.setCollectEmail(true)
      .setAllowResponseEdits(true)
      .setLimitOneResponsePerUser(false)
      .setShowLinkToRespondAgain(false)
      .setConfirmationMessage(
        'Apresentação recebida. Em caso de revisão posterior, reenvie por este ' +
        'mesmo formulário; consideraremos a versão mais recente. Boa apresentação!'
      );
  // Renomeia o arquivo no Drive para refletir o título
  try { DriveApp.getFileById(form.getId()).setName(titulo); } catch (e) {}

  // ---- Seção 1: Identificação do grupo ----
  form.addPageBreakItem()
      .setTitle('Seção 1 — Identificação do grupo');

  form.addTextItem()
      .setTitle('Nome do(a) discente responsável pelo envio')
      .setRequired(true);

  form.addTextItem()
      .setTitle('Matrícula do(a) responsável pelo envio')
      .setRequired(true);

  form.addTextItem()
      .setTitle('Identificação do grupo (número ou nome)')
      .setHelpText('Use o mesmo identificador combinado em sala (ex.: "Grupo 03" ou "Grupo Caatinga").')
      .setRequired(true);

  form.addParagraphTextItem()
      .setTitle('Integrantes do grupo (nome completo + matrícula, um por linha)')
      .setHelpText('Liste TODOS os(as) integrantes, inclusive o(a) responsável. Formato: "Nome Sobrenome — 2024xxxxx".')
      .setRequired(true);

  // ---- Seção 2: Tema e escopo ----
  form.addPageBreakItem()
      .setTitle('Seção 2 — Tema e escopo do seminário')
      .setHelpText('Estas informações orientam a avaliação e organizam a sequência de apresentações.');

  form.addTextItem()
      .setTitle('Tema/título do seminário')
      .setRequired(true);

  form.addListItem()
      .setTitle('Eixo temático do seminário')
      .setChoiceValues([
        'Conceito e evolução da paisagem',
        'Geossistema e leitura sistêmica',
        'Ecologia da paisagem (mancha-corredor-matriz)',
        'Escala, padrão e processo',
        'Cartografia temática e interpretação visual',
        'Sensoriamento remoto aplicado à paisagem',
        'Métricas, fragmentação e conectividade',
        'Unidades de paisagem e diagnóstico integrado',
        'Planejamento territorial e zoneamento',
        'Outro (especificar no campo seguinte)'
      ])
      .setRequired(true);

  form.addTextItem()
      .setTitle('Caso tenha selecionado "Outro", especifique o eixo temático')
      .setRequired(false);

  form.addParagraphTextItem()
      .setTitle('Resumo do seminário (máx. 10 linhas)')
      .setHelpText('Apresente objetivo, recorte (área de estudo, se houver), principais referências e contribuição esperada para a turma.')
      .setRequired(true);

  // ---- Seção 3: Envio da apresentação ----
  form.addPageBreakItem()
      .setTitle('Seção 3 — Envio da apresentação')
      .setHelpText('Anexe o arquivo final OU informe o link público. Pelo menos um dos dois deve ser preenchido.');

  // OBS: o Google Apps Script NÃO permite criar itens "Upload de arquivo" via FormApp.
  // Adicione o campo manualmente após rodar o script:
  //   abra o Form -> "+" -> "Upload de arquivo" -> tipos: PDF, Apresentação;
  //   máx. 3 arquivos, 100 MB cada; obrigatório: NÃO.
  // O placeholder textual abaixo deixa o local marcado para você inserir o item.
  form.addSectionHeaderItem()
      .setTitle('⤓ Upload de arquivo (adicionar manualmente após criar)')
      .setHelpText('Após a execução do script, abra este formulário e adicione AQUI um item do tipo "Upload de arquivo" (PDF/PPTX/ODP, até 3 arquivos × 100 MB, opcional).');

  form.addTextItem()
      .setTitle('Link público da apresentação (Google Slides, Drive, OneDrive)')
      .setHelpText('Habilite "Qualquer pessoa com o link pode visualizar". Cole o URL completo (https://...). Obrigatório se você NÃO anexou arquivo no campo acima.')
      .setRequired(false);

  form.addCheckboxItem()
      .setTitle('Materiais complementares incluídos')
      .setChoiceValues([
        'Slides finais',
        'Roteiro/script da apresentação',
        'Lista de referências bibliográficas',
        'Material visual de apoio (mapas, fotos, vídeos)',
        'Nenhum complementar (apenas slides)'
      ])
      .setRequired(true);

  // ---- Seção 4: Declarações ----
  form.addPageBreakItem()
      .setTitle('Seção 4 — Declarações e observações');

  form.addCheckboxItem()
      .setTitle('Declarações do grupo (todas obrigatórias)')
      .setChoiceValues([
        'Declaramos que o conteúdo apresentado é de autoria do grupo, com as devidas citações às fontes consultadas.',
        'Declaramos ciência de que o uso não creditado de IA generativa caracteriza falta acadêmica.',
        'Declaramos que todos(as) os(as) integrantes listados(as) participaram da elaboração.'
      ])
      .setRequired(true);

  form.addParagraphTextItem()
      .setTitle('Observações ao(à) docente')
      .setHelpText('Necessidade de equipamento específico, restrições de horário, ajustes pendentes etc.')
      .setRequired(false);

  // Move para a pasta indicada (se houver)
  if (FOLDER_ID && FOLDER_ID.trim() !== '') {
    try {
      const file = DriveApp.getFileById(form.getId());
      const dest = DriveApp.getFolderById(FOLDER_ID);
      dest.addFile(file);
      DriveApp.getRootFolder().removeFile(file);
    } catch (e) {
      Logger.log('Aviso: não foi possível mover para a pasta ' + FOLDER_ID + ': ' + e);
    }
  }

  return [
    'NOVO Form criado:',
    '  Título: ' + form.getTitle(),
    '  ID:     ' + form.getId(),
    '  Editar: ' + form.getEditUrl(),
    '  Responder: ' + form.getPublishedUrl()
  ].join('\n');
}

// ===== utilitários ========================================================

function pad2(n) { return (n < 10 ? '0' : '') + n; }

function textoDescricao02_() {
  return (
    'Este formulário destina-se ao envio dos arquivos das apresentações do ' +
    'seminário em grupo da disciplina Análise da Paisagem (UEFS 2026.1).\n\n' +
    'Cada grupo deve realizar UMA única submissão (preferencialmente pelo(a) ' +
    'discente coordenador(a) do grupo). Demais integrantes podem reenviar ' +
    'versões revisadas; consideraremos a mais recente.\n\n' +
    'Formatos aceitos: PDF, PPTX, ODP ou link público (Google Slides/Drive/OneDrive).\n\n' +
    'Prazo: até 24 h antes do encontro de apresentação, salvo orientação em aula.'
  );
}

function substituirRotulos(texto, antigo, novo) {
  if (!texto) return texto;
  // Substitui ocorrências como "Atividade 02", "ATIVIDADE 02" e "atividade 02"
  const re = new RegExp('(\\b[Aa][Tt][Ii][Vv][Ii][Dd][Aa][Dd][Ee])\\s+0?' + parseInt(antigo, 10) + '\\b', 'g');
  return texto.replace(re, function(_m, prefix) {
    // mantém maiúsculas/minúsculas do prefixo
    return prefix + ' ' + novo;
  });
}

/**
 * Utilitário: lista TODOS os Google Forms do seu Drive e imprime ID + título.
 * Use isto para descobrir os IDs e preencher FORM_IDS no topo do arquivo.
 */
function LISTAR_FORMS_DO_DRIVE() {
  const it = DriveApp.getFilesByType(MimeType.GOOGLE_FORMS);
  const linhas = [];
  while (it.hasNext()) {
    const f = it.next();
    linhas.push(f.getId() + '\t' + f.getName());
  }
  Logger.log(linhas.join('\n'));
}
