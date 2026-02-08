# Site Acadêmico - Diego Vidal

Este é o site acadêmico pessoal de Diego Vidal, Engenheiro Agrônomo, Doutor em Propriedade Intelectual e Empreendedorismo, e PhD em Agricultura e Biodiversidade.

## Informações Pessoais

- **Nome:** Diego Vidal
- **Instituição:** UEFS (Universidade Estadual de Feira de Santana)
- **Localização:** Aracaju, Sergipe, Brasil
- **Email:** ldvsantos@uefs.br
- **ORCID:** [0000-0001-8659-8557](https://orcid.org/0000-0001-8659-8557)
- **Lattes:** [7491112603328096](http://lattes.cnpq.br/7491112603328096)

## Estrutura do Site

O site está construído com Quarto e inclui as seguintes seções:

- **Início:** Página principal com biografia e links
- **Publicações:** Lista de publicações acadêmicas
- **Ensino:** Informações sobre atividades de ensino e orientação
- **Mídia:** Aparições na mídia e entrevistas
- **Blog:** Artigos e posts sobre temas de pesquisa
- **Palestras:** Palestras e apresentações

## Como Personalizar

### Adicionar sua foto

Substitua o arquivo `img/portrait_2x3midres.jpeg` pela sua foto pessoal.

### Adicionar suas publicações

Edite o arquivo `papers/index.qmd` e adicione suas publicações seguindo o formato acadêmico padrão.

### Adicionar posts no blog

Crie uma nova pasta dentro de `posts/` com o nome do seu post e adicione um arquivo `index.qmd` com o conteúdo.

### Configurar domínio personalizado

Edite o arquivo `CNAME` e adicione seu domínio personalizado (ex: diegovidal.com.br).

## Como Construir o Site

```bash
quarto render
```

## Como Visualizar Localmente

```bash
quarto preview
```

## Próximos Passos

1. **Adicionar sua foto** em `img/portrait_2x3midres.jpeg`
2. **Adicionar suas publicações** em `papers/index.qmd`
3. **Revisar o conteúdo** das páginas principais
4. **Adicionar suas redes sociais** (se desejar) no `index.qmd`
5. **Configurar domínio** quando estiver pronto para publicar

## Publicação

O site pode ser publicado no GitHub Pages, Netlify ou qualquer outro serviço de hospedagem estática.

## Observações

- Os scripts em `scripts/` foram ajustados mas alguns podem não funcionar até que você configure serviços específicos (como Rogue Scholar para DOIs)
- A pasta `posts/` contém posts do blog do autor original - você pode removê-los e adicionar seus próprios posts
- A pasta `media/` pode ser usada para adicionar suas aparições na mídia
