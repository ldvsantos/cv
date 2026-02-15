










TAILA MILANE PEREIRA DA SILVA








**ELABORAÇÃO DE MAPAS TEMÁTICOS COMO SUBSÍDIO PARA MAPEAMENTO DE RISCO DE EROSÃO EM SOLOS DO GRUPO BARREIRAS**

















Trabalho de Conclusão de Curso

` `Nossa Senhora da Glória/SE\
agosto de 2021




Taila Milane Pereira da Silva









**ELABORAÇÃO DE MAPAS TEMÁTICOS COMO SUBSÍDIO PARA MAPEAMENTO DE RISCO DE EROSÃO EM SOLOS DO GRUPO BARREIRAS**









Trabalho de Conclusão do Curso de Graduação em Engenharia Agronômica da Universidade Federal de Sergipe, como requisito parcial à obtenção do título de bacharel em Engenharia Agronômica.








Orientador: Lucas Resmini Sartor

Coorientador: Francisco Sandro Rodrigues Holanda







TAILA MILANE PEREIRA DA SILVA

**ELABORAÇÃO DE MAPAS TEMÁTICOS COMO SUBSÍDIO PARA MAPEAMENTO DE RISCO DE EROSÃO EM SOLOS DO GRUPO BARREIRAS**

Este documento foi julgado adequado como requisito parcial à obtenção do título de bacharel em Engenharia Agronômica.



Aprovado em: \_\_\_/\_\_\_/\_\_\_/


Banca examinadora:






Prof. Dr. Lucas Resmini Sartor

Universidade Federal de Sergipe – Campus do Sertão







Prof. Dr. José Jairo Florentino Cordeiro Junior

Universidade Federal de Sergipe – Campus do Sertão







Prof. Dr. Tiago Barreto Garcez

Universidade Federal de Sergipe – Campus do Sertão








`                                                                                                                                                                        `v                     
# **AGRADECIMENTOS**
Aos meus pais, Nivaldo e Cida, pelo amor incondicional e por tudo o que fizeram e fazem por mim até hoje. Amo vocês.

Ao meu namorado, Mario, por me incentivar a sair da minha zona de conforto e evoluir, e por me aturar mesmo nos momentos mais difíceis dessa jornada. Eu te amo! Obrigada meu bem!

Aos meus irmãos, Nívia, Ariely, Henrique e Mariany, por todas as risadas compartilhadas e por adicionar leveza aos meus dias. Mesmo quando detesto vocês eu ainda os amo.

Agradeço especialmente a minha irmã Nívia, minha maior incentivadora e amiga, sem você essa caminhada teria sido bem mais difícil. Obrigada por cada conselho, ajuda e puxão de orelha. 

Às minhas companheiras de república e amigas, Keylla e Vanessa, que me acolheram sem pensar duas vezes. Obrigada pelos anos compartilhados no clube das Winx, pelas horas de conversa e pelos risos. 

<a name="_hlk77356927"></a>Às minhas amigas, Aline, Joyse e Sheylla, minhas companheiras na graduação e na vida. Obrigada por estarem sempre presentes, por cada experiência compartilhada, pela força e pela amizade.  

Ao meu cunhado Edclecio, por me acompanhar nessa jornada, a ajuda, a amizade e as várias caronas.

Ao meu duo e amigo, Herbster, por me alegrar e me distrair das dificuldades.

Aos meus colegas e amigos da turma 2016.1 e da UFS, pela amizade e companheirismo nos módulos. Em especial a Pedro, Joyse, Alisson, Duda, Mari e Tiago meus parceiros nos trabalhos, e a Valdenberg e Fellype, meus companheiros na Agrosertão Jr.

Ao meu orientador, Lucas Sartor, um profissional e uma pessoa ímpar, que me acolheu, tranquilizou e guiou nessa última e difícil etapa. Foram tempos difíceis, mas vencemos.

<a name="_hlk77357029"></a>Ao professor André Quintão de Almeida por toda a ajuda dispensada para que este trabalho se concretizasse.

Ao professor Sandro Holanda por seu acompanhamento e ajuda na elaboração do tema deste trabalho de conclusão de curso.

Agradeço, especialmente, ao professor Tiago Garcez, que me deu a oportunidade de conhecer a área que despertou minha paixão na eng. Agronômica e por toda a orientação durante os últimos anos. 

A todos os docentes do NEAS, pelos conhecimentos compartilhados tanto nas disciplinas quanto nas conversas nos corredores do Campus. VOCÊS SÃO EXCEPCIONAIS! 

`                                                                                                                                                                     `v
# <a name="_toc386542664"></a>**ÍNDICE**
[**Resumo	**8****](#_toc78740310)

[**1.**	**Introdução	**9****](#_toc78740311)

[**2.**	**Objetivos	**11****](#_toc78740312)

[2.1	Objetivo geral	11](#_toc78740313)

[2.2	Objetivos específicos	11](#_toc78740314)

[**3.**	**Desenvolvimento	**12****](#_toc78740315)

[3.1	Revisão bibliográfica	12](#_toc78740316)

[3.1.1           Sensoriamento remoto	12](#_toc78740317)

[3.1.2           Sistemas de informações geográficas	13](#_toc78740318)

[3.1.3           Aplicação dos SIGs e do SR em estudos sobre erosão	14](#_toc78740319)

[3.2	Metodologia	16](#_toc78740320)

[3.2.1           Caracterização da área	16](#_toc78740321)

[3.2.2           Obtenção de imagens	16](#_toc78740322)

[3.2.3	Processamento de imagens	17](#_toc78740323)

[3.3	Resultados	18](#_toc78740324)

[3.3.1           Mapa de declividade	18](#_toc78740325)

[3.3.2           Mapa pedológico	20](#_toc78740326)

[3.3.3           Mapa de uso e ocupação do solo	22](#_toc78740327)

[3.3.4           Índice de Vegetação por Diferença Normalizada	24](#_toc78740328)

[**4.**	**Considerações finais	**26****](#_toc78740329)

[**5.**	**Referências bibliográficas	**27****](#_toc78740330)







vii

































# <a name="_toc78740310"></a>**ELABORAÇÃO DE MAPAS TEMÁTICOS COMO SUBSÍDIO PARA MAPEAMENTO DE RISCO DE EROSÃO EM SOLOS DO GRUPO BARREIRAS**
**Resumo**

A fim de realizar o manejo adequado do solo e evitar altos custos com obras de recuperação de processos erosivos, é imprescindível a obtenção de informações detalhadas sobre o risco de erosão, as quais são fornecidas por mapas temáticos que podem ser gerados a partir da utilização de Sistemas de Informações Geográficas (SIG). Desta forma, objetivou-se com este trabalho elaborar mapas temáticos para subsidiar estudos de riscos de erosão de solos do Grupo Barreiras. O estudo foi conduzido na Estação Experimental Campus Rural, da Universidade Federal de Sergipe, situada no município de São Cristóvão – SE. Foram obtidas imagens georreferenciadas por meio do levantamento aéreo com drone e imagens de satélite Planet. As imagens provindas do levantamento fotogramétrico foram trabalhadas no software Agisoft Metashape Professional para formação do Modelo Digital de Terreno (MDT) e do ortomosaico. A partir do MDT foi criado um raster de declividade que foi reclassificado em cinco classes de declividade (0 a 3, 3 a 8, 8 a 20, 20 a 45 e > 45 %). Fazendo uso do mapa de declividade e de observações em campo foi posteriormente gerado o mapa pedológico correlacionando as classes de declividade e de solos presentes na área. Para avaliação do uso e cobertura do solo foram utilizadas as imagens de satélite Planet e o ortomosaico que foram trabalhados no QGIS por meio da vetorização em tela. Por fim, foi realizado o cálculo do Índice de Vegetação por Diferença Normalizada (NDVI), utilizando a imagem de satélite Planet. Com base nos mapas gerados observou-se que a maior parte da área do Campus Rural possui relevo que varia de plano a ondulado. A partir dessas classes de relevo foram alocadas as cinco ordens de solo encontradas na área, com os Neossolos e Gleissolos alocados nas áreas de relevo plano, o Argissolo e a associação Argissolo + Plintossolo identificados nas áreas de relevo suavemente ondulado e ondulado, enquanto nas áreas de relevo fortemente ondulado e montanhoso foram classificados os Plintossolos. As ordens que ocupam maiores áreas são os Neossolos, os Argissolos e associação Argissolo + Plintossolo. Quanto ao uso e ocupação do solo, foram identificados na área sete classes, com as maiores porcentagens associadas as áreas florestais e a áreas com pouca cobertura vegetal. O NDVI apresentou resultados que se assemelham aos observados nos mapas de declividade e uso e ocupação, com as áreas com menor cobertura vegetal coincidindo com a área com maior declive e com solo exposto. Fundamentado nessas observações, conclui-se que as áreas de ocorrência de Plintossolo apresentam a maior suscetibilidade a erosão, o que implica na necessidade de planejamento de ações com vistas a diminuir o risco de erosão nestas áreas.


**Palavras-chave:** Sensoriamento remoto; Fotogrametria; Sistema de Informações Geográficas.

1. # <a name="_toc78740311"></a>**Introdução**
A erosão é um processo natural que pode ser definido como um conjunto de ações que culminam na desagregação, arraste e deposição de materiais rochosos e de solo na superfície terrestre. Embora ocorra naturalmente, a erosão também pode ser influenciada por ações antrópicas, como a retirada da cobertura vegetal, que aumentam os efeitos da erosão, caracterizando-a como erosão acelerada (BRITO, 2012).

A erosão hídrica é responsável pela maior parte da perda de solo, tendo início a partir do impacto das gotas de chuvas com a superfície do solo, causando desagregação das partículas que são posteriormente carregadas pela enxurrada. Se o solo estiver descoberto e a erosividade da chuva for elevada, pode haver grande degradação, potencializando grandes perdas de solo, de água e de nutrientes. Com a continuação deste processo, pode haver a remoção completa do horizonte superficial, além de outros prejuízos como o assoreamento de cursos d’água (CARDOSO *et al.*, 2012). 

Os efeitos da perda de solo por erosão exercem alto impacto ambiental, o que, por sua vez, é refletido na qualidade de vida, pois acarreta grandes prejuízos econômicos e sociais advindos do decréscimo da produtividade e do aumento de gastos com insumos agrícolas (BRITO, 2012). Em Sergipe, a erosão é evidente em todas as regiões, com destaque para a região semiárida devido à ação das chuvas torrenciais sobre o solo descoberto da maioria das áreas destinadas às atividades agropecuárias. Apesar disso, o processo erosivo também é evidente no agreste e na zona da mata, independente da condição climática. Na zona da mata encontram-se os tabuleiros costeiros, formado pela cobertura sedimentar da formação Barreiras (DUARTE *et al*., 2000). Estas áreas são bastante susceptíveis à degradação, pois formam solos normalmente com elevados teores de areia e fraca estruturação. A exploração destes solos, quando realizada de forma desordenada, pode ocasionar sua degradação pelos processos de erosão, tornando-os inadequados para o cultivo e acarretando prejuízo econômico ao agricultor. 

A fim de evitar o elevado custeio de obras de recuperação de processos erosivos, e realizar um adequado manejo do solo, tendo em vista a sustentabilidade, a alternativa mais sensata é a prevenção. Para atingir o objetivo de mitigação dos processos erosivos é imprescindível a obtenção de informações detalhadas a respeito do risco de erosão, que pode ser entendido como a probabilidade de desencadeamento de erosão futura. Estes dados podem ser fornecidos por mapas temáticos para o estudo de risco de erosão (PANDEY; CHOWDARY; MAL, 2007; ROSÁRIO, 2010). Estes mapas podem ser gerados a partir da aplicação de procedimentos de integração de dados empregando o uso de Sistemas de Informações Geográficas (SIG) (LIMA; KUX; SAUSEN, 1992), ferramenta amplamente utilizada nos estudos de erosão por possibilitarem a localização e monitoramento facilitado de áreas de interesse, sendo o foco deste trabalho, que é complementar ao desenvolvido por Nascimento (2021) na mesma área. 






























1. # <a name="_toc78740312"></a>**Objetivos**
   1. ## <a name="_toc382409755"></a><a name="_toc382409962"></a><a name="_toc382410107"></a><a name="_toc382424406"></a><a name="_toc78740313"></a>**Objetivo geral**
Elaborar mapas temáticos para subsidiar estudos de riscos de erosão de solos do Grupo Barreiras localizados na Unidade Experimental Campus Rural, da Universidade Federal de Sergipe.
1. ## <a name="_toc382409756"></a><a name="_toc382409963"></a><a name="_toc382410108"></a><a name="_toc382424407"></a><a name="_toc78740314"></a>**Objetivos específicos**
1) Gerar um modelo digital de elevação do terreno do Campus Rural;
1) Gerar o mapa de declividade; 
1) Criar um mapa pedológico do local estudado;
1) Elaborar um mapa de uso e ocupação do solo;
1) Gerar um mapa do índice de vegetação por diferença normalizada. 




















1. # <a name="_toc78740315"></a><a name="_toc9241127"></a><a name="_toc9330022"></a>**Desenvolvimento** 
   1. ## <a name="_toc78740316"></a>**Revisão bibliográfica** 
### <a name="_toc78740317"></a>**3.1.1    <a name="_hlk78746654"></a>Sensoriamento remoto** 
O termo sensoriamento remoto (SR) se refere a obtenção de informações sobre uma determinada superfície ou objeto sem contato físico, com estes sendo imageados pelo sensor por meio da aferição da radiação eletromagnética, como a luz solar, refletida em sua superfície. Seu desenvolvimento está interligado ao da fotografia, sendo as fotografias aéreas o primeiro tipo de sensoriamento remoto utilizado, e à pesquisa espacial (NOVO; PONZONI, 2001). 

Nos anos 60 teve início a corrida espacial, caracterizada pelo rápido desenvolvimento de foguetes capazes de lançar satélites artificiais no espaço. Os pioneiros foram os satélites meteorológicos, e por meio deles o sensoriamento remoto foi iniciado. O TIROS-1 foi o primeiro satélite a ser lançado no espaço e suas imagens mostravam feições da superfície da terra, ainda que em baixa qualidade (MENESES *et al*., 2012). 

Atualmente podem ser encontradas imagens de sensoriamento remoto com resolução espectral, que se resume a obtenção de imagens em múltiplas bandas de forma simultânea, de centenas de bandas e de resolução espacial, que representa a capacidade de distinguir objetos, determinando o tamanho do menor objeto que pode ser visualizado na imagem, de menos de 1 metro (MENEZES *et al*., 2012). 

A evolução dos sensores e a facilidade de acesso às imagens fizeram com que o sensoriamento remoto se tornasse o meio mais eficiente para a realização de análises ambientais, podendo ser aplicados na criação de mapas temáticos, monitoramento de áreas de difícil acesso, como a Amazônia, identificação de desastres naturais, cadastramentos para múltiplos fins, na agricultura e na cartografia de precisão (FONTES; POZZETTI, 2016). 

No período vigente, o acesso a imagens coletadas por meio do sensoriamento remoto é bastante facilitado, e sua obtenção pode ser realizada por meio de imageamento utilizando diversas plataformas, como satélites, drones, balões, aeronaves, entre outros (BRANDÃO; ZONTA; SHIRATSUCHI, 2018).

Drone é uma denominação genérica aplicada a qualquer aeronave sem tripulação, controlada por meio de uma estação remota, abrangendo desde os aeromodelos até os Veículos Aéreos Não Tripulados (VANTs). O primeiro relato de utilização de aeronaves não tripuladas foi durante um ataque com balões carregados com explosivos no ano de 1849. A partir daí foram criados novos modelos até se chegar aos que são encontrados atualmente (MCDAID; OLIVER, 2003).

São considerados como VANTs as máquinas com rotores, sensores, GPS e câmera para captura de fotografias e vídeo em alta resolução. Suas aplicações fora do âmbito militar são diversas e se estendem desde a segurança pública, à logística de empresas, monitoramento climático, cartografia, e as mais diversas aplicações ambientais (PRUDKIN, 2016).

O avanço da tecnologia permitiu a integração da fotogrametria com os VANTs por meio dada implementação de sensores, além de GPS, com maior acurácia. O produto desse monitoramento passa por um processamento em programas específicos em que ocorre a fototriangulação, geração de nuvem de pontos, modelos digitais, ortofotos, entre outros (SILVA, 2015).

A aplicação dos VANTs em pesquisas ambientais, em conjunto com a fotogrametria, é uma inovação que permite maior precisão na coleta de dados para posterior análise e diagnóstico. Neste âmbito, vários trabalhos já foram realizados com resultados positivos, podendo se citar como exemplo o de Tagliarini (2020), que utilizou imagens de drone para calcular o Índice de Vegetação por Diferença Normalizada (NDVI) em Áreas de Preservação Permanente (APP), e o de Niemann et al., (2016), que tinha por objetivo a geração de Modelos Digitais de Terreno (MDTs) a partir de imageamento por VANT.

Entretanto, apesar de todos os benefícios sua utilização ainda possui alguns gargalos, como o uso restrito a pequenas áreas devido a pequena capacidade de carga da bateria e a necessidade de conhecimentos específicos para manejo do equipamento, bem como no processamento das imagens, onde ainda há dificuldade na automatização, prevalecendo a interpretação e classificação em tela (SILVA, *et al*., 2019; RUZA, *et al*., 2017).
### <a name="_toc78740318"></a>**3.1.2   Sistemas de informações geográficas**
<a name="_hlk77891248"></a>No âmbito das análises geográficas, várias tecnologias se interligam, dentre estas o sensoriamento remoto e os Sistemas de Informações Geográficas (SIGs), as quais possuem uma importância inegável na observação e monitoramento da superfície terrestre. Os SIGs se enquadram dentro das atividades de geoprocessamento, e são compostos por um conjunto de softwares, hardwares e peoplewares, que, integrados, tornam possível a coleta, o armazenamento, o processamento e a análise de informações georreferenciadas (ROSA, 2013; ZAIDAN, 2017).

A aplicação dos SIGs é ampla, mas seu uso pode ser evidenciado na produção de mapas temáticos, como os mapas pedológicos que apresentam as informações a respeito da distribuição espacial dos solos, mapas cadastrais, como os utilizados no Cadastro de Imóveis Rurais (CAR), processamento de imagens de satélite, e a geração dos Modelos Digitais de Elevação (MDE). Estes últimos podem ser divididos em Modelos Digitais de Superfície (MDS), que englobam dados de elevação da superfície topográfica (todas as estruturas que existem sobre o terreno), e Modelos Digitais do Terreno (MDT), que contêm informações da superfície terrestre sem a influência da vegetação e demais estruturas (CÂMARA; DAVIS; MONTEIRO, 2001; OLIVEIRA *et al*., 2017). 

Atualmente, há uma enorme gama de softwares SIG disponíveis e outros tantos em desenvolvimento, sejam eles gratuitos ou não. O QGIS é um dos mais conhecidos softwares livres, sendo utilizado tanto para fins acadêmicos quanto profissionais. Isso se deve às atualizações constantes, à presença de vários recursos nativos e à possibilidade de instalação de inúmeros complementos. É um programa aberto, o que permite que qualquer pessoa com conhecimento de programação possa realizar alterações e implementar melhorias no programa (BRUNO, 2017).
### <a name="_toc78740319"></a>**3.1.3   Aplicação dos SIGs e do SR em estudos sobre erosão**
Informações precisas sobre o risco de erosão e valores de perda de solo são indispensáveis quando se pensa em mitigação da erosão e de seus efeitos. Nesse contexto, a integração entre o sensoriamento remoto e os Sistemas de Informações Geográficas se apresenta como uma poderosa ferramenta de monitoramento e avaliação. A utilização da cartografia, ferramenta de análise e representação espacial, em ambiente SIG, se apresenta como uma das formas mais viáveis de analisar o risco de erosão, considerando-se como base os condicionantes dos processos erosivos e o uso e ocupação do solo (SENA, 2008).

Os processos erosivos são condicionados pelo clima, a vegetação, o solo e a topografia do terreno. Além da precipitação, o clima também tem efeito decisivo no fator cobertura vegetal, determinando a proteção do solo. A vegetação tem por papel reduzir a velocidade do escoamento superficial e o impacto das gotas de chuva no solo, bem como melhorar sua agregação e a porosidade, abrandando assim, a capacidade da chuva de remover e transportar as partículas do solo (OLIVEIRA; SANTOS; ARAUJO, 2018).  

Assim como a vegetação, o solo tem grande importância no processo erosivo devido a sua maior ou menor propensão a erosão. A suscetibilidade do solo à erosão é determinada por suas características físicas e químicas, as quais diferem o comportamento dos solos que, em condições semelhantes de clima, topografia e vegetação, se comportam de maneira diferente devido a maior ou menor resistência à ação da água e do vento conferidas por sua textura, composição, estrutura e porosidade (OLIVEIRA; SANTOS; ARAUJO, 2018).

Quanto à topografia, sua importância no processo erosivo está ligada à declividade e ao comprimento da rampa, influenciando diretamente na velocidade de escoamento da água. Terrenos com relevo irregular e declives mais acentuados promovem a concentração e aumento do fluxo de água. A declividade e o comprimento da rampa são interdependentes, visto que quanto maior o comprimento da rampa, maior importância a declividade ganha, enquanto a influência do comprimento tende a ser maior à medida que a declividade aumenta (BERTONI; LOMBARDI NETO, 2008).

A aplicação dos SIGs em trabalhos sobre erosão não é recente, e se estende desde a aplicação de Equação Universal de Perda de Solo (EUPS), conjugada aos softwares SIG, até o mapeamento individual de características como a declividade, cobertura vegetal, pedologia e uso e ocupação do solo. 

A declividade é um dos fatores que regulam os processos erosivos, logo o mapa de declividade se mostra como um instrumento adequado para identificar o relevo. Este mapa pode ser obtido, dentre outras formas, a partir da digitalização de cartas pré-existentes e da utilização de um MDT, que pode ser gerado a partir do SR. Sua integração com outros mapas temáticos, como o de uso e ocupação do solo, mapas que identificam a cobertura vegetal, o pedológico, possibilita a visualização do risco de erosão no local que se deseja estudar (SILVEIRA; CUNHA, 2006; OLIVEIRA; PINTO; LOMBARDI NETO, 2007). 

Os modelos de perda de solo, como a EUPS, também podem ser modificados e ajustados para serem aplicados em ambiente SIG. Estudos corroboram que os resultados obtidos nesse processo são bastante críveis e auxiliam na identificação de locais prioritários para a aplicação de práticas de conservação do solo (TAMENE *et al*., 2017). Isto pode ser observado no trabalho desenvolvido por Tomazoni e Guimarães (2005), que utilizaram a EUPS no SPRING para determinar a perda de solo por erosão laminar na bacia do rio Jirau. Os autores observaram que o uso do SIG foi eficiente no monitoramento e quantificação da erosão laminar, visto que confrontando os mapas obtidos com a realidade em campo as informações correspondiam. Resultados semelhantes foram obtidos por Cerri *et al*., (1998), que trabalhando com a EUPS no ARC-INFO e no ARCVIEW concluíram que a metodologia se mostrava adequada para analisar os fatores da EUPS e identificar possíveis métodos de remediação.

Outros trabalhos também podem ser citados, como o de Reis, Costa e Ribeiro (2014), que com o objetivo de realizar o mapeamento da suscetibilidade à erosão em áreas protegidas se utilizaram do ArcGIS e de imagens advindas do SR para gerar mapas de uso e ocupação do solo, de declividade e pedológico, constatando a eficiência do uso do geoprocessamento nas análises sobre os condicionantes dos processos erosivos. Na mesma linha de pesquisa, Costa Neto (2010), buscando elaborar mapas de vulnerabilidade natural à erosão, utilizou imagens de SR e bases cartográficas pré-existentes para gerar mapas temáticos que quando sobrepostos geraram o mapa de vulnerabilidade a erosão. O autor concluiu que a metodologia se mostrou eficiente e possibilitou a obtenção de resultados com alta confiabilidade.

A utilização dos SIGs em conjunto com dados de alta resolução podem gerar os mais diversos mapas, com alta aplicabilidade nos estudos sobre erosão, permitindo a análise, identificação de áreas suscetíveis à perda de solo, e a criação de propostas para mitigar os riscos de erosão (VIEL; ROSA; HOFF, 2017).  
1. ## <a name="_toc78740320"></a>**Metodologia**
### <a name="_toc62463732"></a><a name="_toc73386004"></a><a name="_toc78740321"></a>**3.2.1   <a name="_hlk78226465"></a>Caracterização da área**
O estudo foi conduzido na Estação Experimental Campus Rural, da Universidade Federal de Sergipe (UFS), situada no povoado Timbó, município de São Cristóvão – SE, nas coordenadas geográficas 10º55´S de latitude e 37º11´O de longitude. O Campus Rural possui uma área de 181 hectares ocupados com benfeitorias, ensaios experimentais e vegetação nativa. O clima do local é classificado como tropical com chuvas de inverno (As’) concentradas entre os meses de abril a setembro (ALVARES *et al*., 2013). São encontrados na área, predominantemente, três classes de solo: Neossolo Flúvico Psamítico, Argissolo Vermelho Amarelo Distrófico e Plintossolo Háplico Distrófico. Há uma prevalência de relevo plano, suave ondulado e ondulado. 
### <a name="_toc73386006"></a><a name="_toc78740322"></a>**3.2.2   Obtenção de imagens**
Para realização do trabalho foram obtidas imagens georreferenciadas com alta resolução espacial (1 m), por meio do levantamento aéreo utilizando um DJI Phantom 4 PRO (SZ DJI Technology Co., Ltd., Shenzen, China) plataforma UAV (Unmanned Aerial Vehicle), no dia 27 de setembro de 2018. Foram realizados dois voos, com intersecção de imagens, a fim de cobrir cerca de 50 ha da área total do Campus Rural, correspondendo a área ocupada com benfeitorias e dedicada a instalação de experimentos. Os parâmetros adotados durantes os voos estão identificados na tabela 1. Também foram utilizadas imagens do satélite Planet com resolução espacial de três metros e quatro bandas espectrais (RGB e infra vermelho próximo). As imagens de satélite Planet foram fornecidas pela empresa em colaboração com o professor André Quintão de Almeida, tornando possível a elaboração dos mapas e a execução deste trabalho.

Tabela 1. Parâmetros adotados nos voos com DJI Phantom 4 PRO 

|**Parâmetros**| |
| - | - |
|Área de cobertura (ha)|52 (voo 1) / 45 (voo 2)|
|Altura de voo (m)|120|
|Velocidade de voo (m/s)|10|
|Tempo de voo (min)|15|
|Sobreposição frontal (%)|75|
|Sobreposição lateral (%)|70|
|Sensor|1" CMOS 20M pixel|
|Faixas espectrais|Red, Green, Blues|
|Distância da amostra do solo (cm)|3,2|
|Número de imagens|221 (voo 1) / 213 (voo 2)|
|Formato das imagens|JPG|

Fonte: Almeida *et al.* (2020)
1. ### <a name="_toc73386007"></a><a name="_toc78740323"></a>**Processamento de imagens**
O processamento fotogramétrico para geração do MDT e da nuvem de pontos foi realizado utilizando o software Agisoft Metashape Professional Edition 1.6. O software se utilizou de uma combinação de algoritmos de estrutura de movimento para alinhar a câmera, encontrar pontos semelhantes nas imagens sobrepostas e realizar a reconstrução da geometria 3D. Em seguida foi realizado um processo intermediário para otimizar o posicionamento e alinhamento das câmeras. No georreferenciamento das imagens, foram aleatoriamente distribuídos 41 pontos de controle de solo tridimensionais (GCPs), dos quais 31 foram utilizados como controle e 10 como pontos de verificação. As coordenadas dos GCPs foram coletadas por um receptor GNSS modelo FOIF A60 no modo RTK, com precisão horizontal de ± 0,007 m, e precisão vertical de ± 0,011 m. O módulo denso de nuvem foi utilizado para construir a nuvem densa de pontos. Os valores do erro quadrático médio da raiz horizontal e vertical (RMSE), calculados a partir dos dez pontos de verificação, foram de 0,04 e 0,11 m, respectivamente. Por fim, as nuvens de pontos foram exportadas para o formato LAS, e o MDT foi gerado a partir da nuvem de pontos usando a Adaptative Triangulated Irregular Network (TIN). Como produtos desse processamento foram obtidos o MDT e o ortomosaico.

Com o MDT, em formato GeoTIFF, no software QGIS 3.16 (QGIS.ORG, 2021), foi elaborado um raster de declividade em porcentagem. Com o raster pronto, foi realizada a reclassificação da declividade presente na área em 5 classes (0 a 3, 3 a 8, 8 a 20, 20 – 45 e > 45 %), conforme classificação sugerida por Ramalho Filho e Beek (1995). Nesta etapa foi empregada o módulo Reclass no QGIS.

O mapa pedológico foi elaborado no QGIS correlacionando a posição do relevo com as classes de solo presentes na área por meio da sobreposição do mapa de declividade. A partir do mapa de declividade e de informações levantadas em visita a campo, foi criado um arquivo shapefile e por meio da vetorização em tela foi criado o mapa pedológico, com a identificação de 4 ordens de solo levantadas a campo, que foram alocadas principalmente de acordo com a declividade da área. 

Para avaliação do uso e cobertura do solo, foram utilizadas as imagens de satélite Planet, trabalhadas no QGIS por meio da vetorização em tela, utilizando as ferramentas de criação e edição de polígonos. Também foi utilizado o ortomosaico, produto gerado no fim do processamento fotogramétrico. O polígono da área foi delimitado e sobreposto a imagem de satélite, e por meio da interpretação das cores, formas e texturas, foi realizada a criação de polígonos delimitando cada uso do solo. Em caso de dúvida a respeito da classificação, foi consultado o ortomosaico, visto que sua resolução espacial é maior.

O Índice de Vegetação por Diferença Normalizada (NDVI) indica o vigor e a caracterização da vegetação presente em uma determinada área, a partir do uso de imagens de satélite. Para o cálculo do NDVI foi utilizada a imagem Planet. Seu cálculo é realizado a partir da Equação 1:

NDVI = NIR – R / NIR + R                                                                 (1)

Onde: 

NIR = Infravermelho próximo

R = Vermelho
1. ## <a name="_toc78740324"></a>**Resultados**
### <a name="_toc78740325"></a>**3.3.1    Mapa de declividade**
Na figura 1 é possível visualizar o mapa de declividade da área estudada. O mapa de declividade é uma ferramenta indispensável no planejamento ambiental, uma vez que possibilita a visualização da inclinação das vertentes em classes. Essa classificação permite identificar as possibilidades e potencialidades de uso da área estudada (PINHEIRO; SILVA; REIS, 2014). 

![](Aspose.Words.8e7a61f7-d13b-4152-834d-4095ff0bf259.001.jpeg)

Figura 1. Mapa de declividade a área.

Fonte: Autoria própria.

A partir do mapa é possível observar que há uma grande variação na declividade da área estudada, com a presença de todas as classes de declividade. A maior parte da área possui declividade que varia entre 0 a 3 % a e 8 a 20 %, conforme consta na tabela 2, cujos dados são oriundos de uma análise executada dentro do software QGIS. 

Tabela 2. Porcentagem das classes de declividade presentes na área

|**Relevo**|**Classes de declividade (%)**|**Área (%)**|
| :- | :-: | :-: |
|Plano|0-3|20|
|Suavemente ondulado|3-8|22|
|Ondulado|8-20|45|
|Fortemente ondulado|20-45|11|
|Montanhoso|>45|2|

Fonte: Autoria própria.

A declividade tem grande interferência na perda de solo por erosão, visto que esta reflete a inclinação do terreno em relação a um eixo horizontal (OLIVEIRA; PINTO; LOMBARDI NETO, 2007). Ela influencia, logicamente, a velocidade de escoamento superficial, sendo diretamente proporcional ao grau de inclinação do terreno, se considerada isoladamente. A classe de relevo plano cobre um total de 20 % da área total. Estas áreas, quando observadas apenas do ponto de vista da declividade, praticamente não oferecem limitações para uso e estão menos propensas aos efeitos da erosão hídrica. Quanto à classe suavemente ondulado, esta corresponde a 22 %, também não oferecendo limitações ao uso, desde que associadas a alguma prática conservacionista. 

A classe predominante é o relevo ondulado, perfazendo 45 % da área total. Nestas áreas, a velocidade do escoamento superficial é moderada e seu uso para fins agrícolas deve, imprescindivelmente, vir acompanhado do uso de práticas conservacionistas a fim de diminuir os efeitos da erosão. O restante da área é de relevo fortemente ondulado, correspondendo a 11 %, e montanhoso, com 2 %. Estas áreas devem ser protegidas e destinadas ao abrigo da flora e fauna devido à alta susceptibilidade à erosão. 
### <a name="_toc78740326"></a>**3.3.2   Mapa pedológico**
Ao analisar a figura 2, que corresponde ao mapa pedológico, observa-se a presença de cinco ordens de solo que foram identificadas a partir do mapa de declividade, em função da influência do relevo na formação do solo, e de observação em campo. Em locais com relevo predominantemente plano, foram alocados os Neossolos Flúvicos, que são solos formados por sedimentos aluviais e geralmente ocupam as áreas de baixada (TULLIO, 2019), e o Gleissolo Háplico, identificado em visita a campo. As áreas com relevo predominantemente suave ondulado e ondulado foram classificadas como Argissolo Vermelho Amarelo Distrófico e Argissolo Vermelho Amarelo Distrófico em associação com Plintossolo Háplico, esta associação, assim como o Gleissolo, foi identificada em visita a campo, todavia, precisam ser realizadas análises mais detalhadas a fim de confirmar a classificação prévia. O caráter distrófico foi determinado com base em informações secundários de levantamentos pedológicos realizados no estado de Sergipe (JACOMINE *et al*., 1975). Estas ordens são encontradas em relevos mais acidentados. Por outro lado, as áreas classificadas como fortemente onduladas e montanhosas foram identificadas como Plintossolo Háplico.

![](Aspose.Words.8e7a61f7-d13b-4152-834d-4095ff0bf259.002.jpeg)

Figura 2. Mapa pedológico da área.

Fonte: Autoria própria.

A partir da tabela 3 é possível observar que três das cinco ordens de solo ocupam mais de 80 % da área total mapeada (Neossolo Flúvico, Argissolo Vermelho Amarelo e a associação de Argissolo Vermelho Amarelo Distrófico + Plintossolo Háplico). Esses valores se relacionam com os observados na tabela 2. 

Tabela 3. Porcentagem de ocupação das classes de solo da área.

|**Ordens**|**Área (%)**|
| - | :-: |
|Neossolo Flúvico|27,3|
|Argissolo Vermelho Amarelo Distrófico|25,9|
|Argissolo Vermelho Amarelo Distrófico + Plintossolo Háplico|29,3|
|Plintossolo Háplico|11,1|
|Gleissolo Háplico|6,4|

Fonte: Autoria própria.

O mapeamento do solo permite a visualização e identificação das potencialidades e restrições ao uso do solo, sendo uma ferramenta indispensável para o planejamento do uso racional dos recursos disponíveis. A classificação dos solos da área se apresenta como fator importante na determinação do risco de erosão, considerando-se que cada ordem de solo tem características físicas e químicas distintas que influenciam a maior ou menor suscetibilidade do solo à erosão (BERTONI; LOMBARDI NETO, 2008). 

Os Argissolos Vermelho Amarelos da área de estudo são solos minerais com presença de horizonte diagnóstico B textural, formados a partir ou sob a influência das rochas cristalinas do Grupo Barreiras, sendo profundos, bem drenados, fracamente estruturados no horizonte A e moderadamente estruturados em Bt, e com presença de argila 1:1, podendo ser altamente susceptíveis à erosão nos horizontes arenosos superficiais (SILVA; OLIVEIRA NETO, 2001). Os Neossolos Flúvicos são solos formados por sedimentos aluviais, podendo estar associados com Neossolos Quartzarênicos e Gleissolos. Apresentam horizonte A sobre C e sua textura é predominantemente arenosa ao longo do perfil, o que implica em fraca ou ausência de agregação e estruturação. Apesar disso, foi detectada baixa de erodibilidade relacionado aos Neossolos Flúvicos desta área (Nascimento, 2021). Isso pode ser explicado pela alta cobertura vegetal, associada a baixa declividade presente na área de ocorrência dessa ordem. 

Os Gleissolos são solos minerais, mal drenados ou muito mal drenados, formados pelo processo de gleização, que consiste na redução do íon ferro (Fe<sup>3+</sup>) em condições de ausência de oxigênio, o que é propiciado pela saturação por água por uma grande parte do ano. Sua ocorrência está associada às margens de cursos d’água e planícies inundadas. A gleização também propicia o aparecimento de cores esverdeadas, azuladas ou acinzentadas (SANTOS *et al*., 2018). Quanto aos Plintossolos, são solos minerais, caracterizados pela presença significativa de plintita, formados em situação de restrição a percolação de água no perfil. O Plintossolo Háplico presente no Campus Rural se apresenta como o mais suscetível à erosão (NASCIMENTO, 2021), o tornando impróprio para uso agrícola. Assim, recomenda-se incluí-lo em área de preservação permanente.  
### <a name="_toc78740327"></a>**3.3.3   Mapa de uso e ocupação do solo**
O uso do solo corresponde a parcela de interferência antrópica na superfície terrestre. O uso do solo, sem levar em conta suas características e capacidade de uso, pode acarretar em diversos problemas, que vão desde a perda de solo por erosão, que consequentemente diminui a fertilidade natural do solo e a produtividade agrícola, até a contaminação e assoreamento de cursos d’água, comprometendo o abastecimento de água (OLIVEIRA; PINTO; LOMBARDI NETO, 2007).

A partir da confecção do mapa de uso e ocupação do solo (figura 3), foi possível identificar 7 classes de uso do solo. A identificação do uso do solo foi facilitada pelo uso da imagem de satélite associada ao ortomosaico, que possibilitou o reconhecimento de objetos muito pequenos. 

![](Aspose.Words.8e7a61f7-d13b-4152-834d-4095ff0bf259.003.png)

Figura 3. Mapa de uso e ocupação do solo da área.

Fonte: Autoria própria.

Observando a tabela 4 vê-se que a maior parte da área mapeada corresponde à área florestal (47 %) e à área com pouca cobertura vegetal (36 %), seguido da área destinada à agricultura (8 %) e da área com solo exposto (7 %). Da área total mapeada, 90 % permanece pouco antropizada, entretanto, é preocupante notar que as áreas com solo exposto e com pouca cobertura vegetal estão associadas aos maiores percentuais de declividade, o que implica em alto risco de erosão. 

Tabela 4. Uso e ocupação do solo do Campus Rural da Universidade Federal de Sergipe

|**Uso e ocupação do solo**|**Área (%)**|
| :- | :-: |
|Área florestal|47|
|Área destinada à agricultura|8|
|Área com pouca cobertura vegetal|36|
|Solo exposto|7|
|Reservatórios de água|0,4|
|Plantio de eucalipto|0,9|
|Área com presença de construções|0,7|

Fonte: Autoria própria.
### <a name="_toc78740328"></a>**3.3.4   Índice de Vegetação por Diferença Normalizada**
O índice de Vegetação por Diferença Normalizada (figura 4) indica a quantidade e a qualidade da vegetação, variando de -1 a 1, com os valores mais próximos de 1 representando uma alta cobertura da vegetação, enquanto os valores mais próximos de -1 indicam um baixo índice de cobertura da vegetação (GAMEIRO et al., 2016). 

![](Aspose.Words.8e7a61f7-d13b-4152-834d-4095ff0bf259.004.jpeg)

Figura 4. Índice de vegetação por diferença normalizada da área.

Fonte: Autoria própria.

O NDVI da área estudada variou entre 0,75 e 0,14, com o valor mais alto representando a vegetação arbórea, evidenciada pela alta atividade fotossintética, e o menor valor representando áreas com solo exposto. Os valores intermediários evidenciam as áreas destinadas à agricultura e as áreas indicadas no mapa de uso e ocupação do solo como área com pouca cobertura vegetal. De forma geral, é possível verificar visualmente que uma extensa área apresenta as colorações verdes, indicando uma alta cobertura vegetal, demonstrando a presença de vegetação de porte arbóreo para a tonalidade mais escura, e arbustivo para a tonalidade mais clara. Já o azul, indica a presença de vegetação herbácea, que oferece pouca cobertura vegetal, enquanto as tonalidades de laranja e vermelho indicam áreas com solo exposto, afloramentos rochosos ou construções (TAGLIARINI, 2020).

É possível verificar que o NDVI corrobora as informações obtidas por meio dos mapas anteriores, comprovando a fragilidade das áreas em que ocorrem os maiores níveis de declividades e os Plintossolos.






























1. # <a name="_toc9241128"></a><a name="_toc9330023"></a><a name="_toc78740329"></a>**Considerações finais**
A integração do sensoriamento remoto com os SIGs tem cada vez mais ganhado espaço no monitoramento e nas análises ambientais. A utilização do geoprocessamento aliado ao sensoriamento remoto se mostrou um método eficiente no monitoramento e avaliação da suscetibilidade a erosão. Os mapas elaborados contribuíram para análise e compreensão do relevo, ocupação e distribuição dos solos e cobertura vegetal, se provando uma alternativa válida para monitoramento dos riscos de erosão, principalmente quando não se tem a possibilidade de realizar levantamentos em campo com frequência. 

Os resultados obtidos são semelhantes aos já observados por Nascimento (2021), que apresenta as áreas com ocorrência de Neossolo Flúvico e relevo plano como as menos suscetíveis a erosão, e respalda a maior fragilidade nas áreas de ocorrência de Plintossolo, que coincidem com as áreas de maior declividade e menor cobertura vegetal, o que implica na necessidade de planejamento de ações com vistas a diminuir o risco de erosão nestas áreas.





















1. # <a name="_toc9241129"></a><a name="_toc9330024"></a><a name="_toc78740330"></a>**Referências bibliográficas**
Agisoft LLC, S.P. *Agisoft Metashape Professional Edition v.1.6*. 2019. Disponível online em: http://www.agisoft.com/pdf/metashape-pro\_1\_5\_en.pdf. Acesso em 20 fev. 2020.

ALMEIDA, A.; GONÇALVES, F.; SILVA, G.; SOUZA, R.; TREUHAFT, R.; SANTOS, W.; LOUREIRO, D.; FERNANDES, M. Estimating Structure and Biomass of a Secondary Atlantic Forest in Brazil Using Fourier Transforms of Vertical Profiles Derived from UAV Photogrammetry Point Clouds. **Remote Sensing**, Switzerland, v. 12, n. 21, p. 3560, 30 out. 2020. MDPI AG. doi:10.3390/rs12213560.

ALVARES, C. A.; STAPE, J. L.; SENTELHAS, P. C.; GONÇALVES, J. L. de M.; SPAROVEK, G. Köppen's climate classification map for Brazil. **Meteorologische Zeitschrift**, [S.L.], v. 22, n. 6, p. 711-728, 1 dez. 2013. Schweizerbart. doi:[10.1127/0941-2948/2013/0507](http://dx.doi.org/10.1127/0941-2948/2013/0507). 

BERTONI, J.; LOMBARDI NETO, F. **Conservação do solo**. Ícone, 6ª ed. São Paulo, 2008, 355p.

BRANDÃO, Z. N.; ZONTA, J. H.; SHIRATSUCHI, L. S. Sensoriamento remoto na cultura do algodão. In: TULLIO, L. (org.). **Aplicações e princípios do sensoriamento remoto**. Ponta Grossa - PR: Atena, 2018. Disponível em: https://www.atenaeditora.com.br/wp-content/uploads/2018/10/E-book-Aplica%C3%A7%C3%B5es-e-Princ%C3%ADpios-do-Sensoriamento-Remoto-1.pdf. Acesso em: 04 jul. 2021.

BRITO, A. de O. **Estudos da erosão no ambiente urbano, visando planejamento e controle ambiental no Distrito Federal**. 2012. 77 f. Dissertação (Mestrado) - Curso de Engenharia Florestal, Departamento de Engenharia Florestal, Universidade de Brasília, Brasília, 2012.

BRUNO, L. O. Aplicabilidade de Sistemas de Informações Geográficas (SIGs) livres nas ciências ambientais: o uso do QGIS. **Revista Brasileira de Gestão Ambiental e Sustentabilidade**, [S.L.], v. 4, n. 8, p. 321-326, nov. 2017. [doi:10.21438/rbgas.040807](http://dx.doi.org/10.21438/rbgas.040807).

CARDOSO, D. P.; SILVA, M. L. N.; CARVALHO, G. J. de; FREITAS, D. A. F.; AVANZIA, J. C. Plantas de cobertura no controle das perdas de solo, água e nutrientes por erosão hídrica. **Revista Brasileira de Engenharia Agrícola e Ambiental**, Campina Grande, PB, v. 16, n. 6, p. 632-638, 23 ago. 2012.

CERRI, C. E. P.; BALLESTER, M. V. R.; MARTINELLI, L. A.; VETTORAZZI, C. A. Mapas de risco à erosão do solo na bacia do rio Piracicaba utilizando técnicas de geoprocessamento. In: SIMPÓSIO BRASILEIRO DE SENSORIAMENTO REMOTO, 9., 1998, Santos. **Anais 9º Simpósio Brasileiro de Sensoriamento Remoto.** Santos: Inpe, 1998. p. 513-523.

COSTA NETO, J. F. Elaboração de mapas de vulnerabilidade natural à erosão como subsídio ao zoneamento ambiental em bacias hidrográficas com o uso de geoprocessamento. **Revista Brasileira de Espeleologia**, [S.L], v. 1, n. 1, p. 52-60, jun. 2010.

DUARTE, M. N.; CURI, N.; PÉREZ, D. V.; KÄMPF, N.; CLAESSEN, M. E. C. Mineralogia, química e micromorfologia de solos de uma microbacia nos tabuleiros costeiros do Espírito Santo. **Pesquisa Agropecuária Brasileira**, [S.L.], v. 35, n. 6, p. 1237-1250, jun. 2000. FapUNIFESP (SciELO). doi:[10.1590/s0100-204x2000000600021](http://dx.doi.org/10.1590/s0100-204x2000000600021).

FONTES, J. C.; POZZETTI, V. C. O Uso dos Veículos não Tripulados no Monitoramento Ambiental na Amazônia. **Revista de Direito e Sustentabilidade**, [S.L.], v. 2, n. 2, p. 149-164, 1 dez. 2016. Conselho Nacional de Pesquisa e Pós-graduação em Direito - CONPEDI. doi:[10.26668/indexlawjournals/2525-9687/2016.v2i2.1257](http://dx.doi.org/10.26668/indexlawjournals/2525-9687/2016.v2i2.1257).

GAMEIRO, S.; TEIXEIRA, C. P. B.; SILVA NETO, T. A.; LOPES, M. F. L.; DUARTE, C. R.; SOUTO, M. V. S.; ZIMBACK, C. R. L. Avaliação da cobertura vegetal por meio de índices de vegetação (NDVI, SAVI e IAF) na Sub-Bacia Hidrográfica do Baixo Jaguaribe, CE. **Terrae**, [S. L.], v. 13, n. 1, p. 15-22, maio 2016.

JACOMINE, P. K. T.; MONTENEGRO, J. O.; RIBEIRO, M. R.; FORMIGA, R. A. **Levantamento exploratório-reconhecimento de solos do estado de Sergipe**. Recife: Embrapa, 1975. 506 p. Boletim Técnico nº 36.

LIMA, E. R. V. de; KUX, H. J. H.; SAUSEN, T. M. Sistema de Informações Geográficas e técnicas de sensoriamento remoto na elaboração de mapa de risco de erosão no Sertão da Paraíba. **Revista Brasileira de Ciência do Solo**, Campinas, v. 16, n., p. 257-263, 1992.

MCDAID, H.; OLIVER, D. **Remote Piloted Aerial Vehicles: An Anthology**. Disponível em: http://www.ctie.monash.edu.au/hargrave/rpav\_home.html#Beginnings. Acesso em: 18 jun. 2021.

MENESES, P. R.; ALMEIDA, T.; ROSA, A. N. de C. S.; SANO, E. E.; SOUZA, E. B.; BAPTISTA, G. M. de M.; BRITES, R. S. **Introdução ao processamento de imagens de sensoriamento remoto**. Brasília: Universidade de Brasília, 2012. 266 p. Disponível em: http://memoria.cnpq.br/documents/10157/56b578c4-0fd5-4b9f-b82a-e9693e4f69d8. Acesso em: 25 jun. 2021.

NASCIMENTO, M. R. S. **Diagnóstico e análise dos processos erosivos na Estação Experimental Campus Rural em São Cristovão - Sergipe**. 2021. 26 f. TCC (Graduação) - Curso de Engenharia Agronômica, Núcleo de Graduação de Agronomia do Sertão, Universidade Federal de Sergipe - Campus do Sertão, Nossa Senhora da Glória - SE, 2021.

NIEMANN, R. S.; SILVA, T. S. F.; CANCIAN, L. F.; GROHMANN, C. H.; MORELLATO, L. P. C.; A LONGHITANO, G. A. Extração de modelo digital de terreno a partir de nuvem de pontos obtida por Veículo Aéreo Não-Tripulado. In: SIMPÓSIO NACIONAL DE GEOMORFOLOGIA, 11., 2016, Maringá. **Anais do 11º SINAGEO.** Maringá: [S.I.], 2016. p. 1-5.

NOVO, E. M. L. M; PONZONI, F. J. **Introdução ao Sensoriamento Remoto***.* Instituto Nacional de pesquisas Espaciais, Divisão de Sensoriamento Remoto, 2001. Disponível em <http://www.agro.unitau.br/sensor_remoto/apofla.pdf>. Acesso em 30/06/2021.

OLIVEIRA, A. M. M.; PINTO, S. A. F.; LOMBARDI NETO, F. Caracterização de indicadores da erosão do solo em bacias hidrográficas com o suporte de geotecnologias e modelo predictivo. **Estudos Geográficos**: Revista Eletrônica de Geografia, Rio Claro - SP, v. 5, n. 1, p. 63-86, 25 set. 2007.

OLIVEIRA, D. R.; CICERELLI, R. E.; ALMEIDA, T. DE; MAROTTA, G. S. Geração de modelo digital do terreno a partir de imagens obtidas por veículo aéreo não tripulado. **Revista Brasileira de Cartografia**, [S.L.], v. 69, n. 6, 15 jun. 2017.

OLIVEIRA, F. F.; SANTOS, R. E. S. dos; ARAUJO, R. C. de. Processos erosivos: Dinâmica, agentes causadores e fatores condicionantes. **Revista Brasileira de Iniciação Científica**, São Paulo, v. 5, n. 3, p. 60-83, abr/jun. 2018. Trimestral.

PANDEY, A.; CHOWDARY, V. M.; MAL, B. C. Identification of critical erosion prone areas in the small agricultural watershed using USLE, GIS and remote sensing. **Water Resources Management**, [S.L.], v. 21, n. 4, p. 729-746, 8 Jul. 2006. Springer Science and Business Media LLC. [doi:10.1007/s11269-006-9061-z](http://dx.doi.org/10.1007/s11269-006-9061-z).

PINHEIRO, M. A.; SILVA, J. M. O.; REIS, E. M. Mapeamento das classes de declividade da microbacia do rio Salamanca – Barbalha - Ceará. In: SIMPÓSIO NACIONAL DE GEOMORFOLOGIA, 10, 2014, Manaus - AM. **Anais do 10º Sinageo.** Manaus - AM: S.I, 2014. p. 1-5.

PRUDKIN, G. El Periodismo Drone: contextualización histórica y posibles usos periodísticos. **Comunicação & Inovação**, São Caetano do Sul - SP, v. 17, n. 33, p. 07-21, 8 mar. 2016. doi:10.13037/ci.vol17n33.3560.

QGIS association. **QGIS Geographic Information System.** QGIS.Org, 2021.

RAMALHO FILHO, A.; BEEK, K. L. **Sistema de avaliação da aptidão agrícola das terras**. 3 ed. Rio de Janeiro: EMBRAPA, CNPS, 1995. 65p.

REIS, T. E.; COSTA, V. C.; RIBEIRO, M. F. Mapeamento de susceptibilidade à erosão em zona de amortecimento de áreas protegidas brasileiras, utilizando técnicas de geoprocessamento. **Multidimensão e Territórios de Risco**, [S.L.], p. 141-145, dez. 2014. Imprensa da Universidade de Coimbra. http://dx.doi.org/10.14195/978-989-96253-3-4\_24. 

ROSA, R. **Introdução ao geoprocessamento**. Uberlândia: Universidade Federal de Uberlândia, 2013. 139 p.

ROSÁRIO, G, O. **Análise espacial aplicada à determinação do risco de erosão do solo na porção Noroeste do município de Itabirito**. 2010. 33 f. Monografia (Especialização) - Curso de Especialização em Geoprocessamento, Instituto de Geociências, Universidade Federal de Minas Gerais, Belo Horizonte, 2010.

RUZA, M. S.; CORTE, A. P. D.; HENTZ, A. M. K.; SANQUETTA, C. R.; SILVA, C. A.; SCHOENINGER, E. R. Inventário de Sobrevivência de povoamento de Eucalyptus com uso de Redes Neurais Artificiais em Fotografias obtidas por VANTs. **Advances In Forestry Science**, Cuiabá, v. 4, n. 1, p. 83-88, 31 mar. 2017. Disponível em: https://periodicoscientificos.ufmt.br/ojs/index.php/afor/article/view/4169. Acesso em: 04 jul. 2021.

SENA, J. N. **O uso de sistema de informação geográfica na avaliação de diferentes alternativas de geração de cartas de suscetibilidade à erosão**. 2008. 83 f. Dissertação (Mestrado) - Curso de Engenharia Civil, Faculdade de Engenharia de Ilha Solteira, Universidade Estadual Paulista, Ilha Solteira, 2008.

SILVA, D. C. Evolução da Fotogrametria no Brasil. **Revista Brasileira de Geomática**, [S.L.], v. 3, n. 2, p. 81-96, 14 dez. 2015. Universidade Tecnológica Federal do Paraná (UTFPR). doi:10.3895/rbgeo.v3n2.5467.

SILVA, M. S. L.; OLIVEIRA NETO, M. B. **Argissolos Vermelho-Amarelos**. 2001. Empresa Brasileira de Pesquisa Agropecuária - EMBRAPA. Disponível em: https://www.agencia.cnptia.embrapa.br/gestor/territorio\_mata\_sul\_pernambucana/arvore/CONT000gt7eon7k02wx7ha087apz2axe8nfr.html. Acesso em: 20 jul. 2021.

SILVA, P. R. da; MATTEDI, M. A.; LUDWIG, L.; RIBEIRO, E. A. W. Gestão Ambiental na Era Moderna: a socialização de novas tecnologias com uso de drones para monitoramento ambiental no Vale do Itajaí - Santa Catarina. **Revista da Extensão**, [S. L.], v. [S. I.], n. 19, p. 45-50, nov. 2019. Universidade Federal do Rio Grande do Sul. Disponível em: https://www.seer.ufrgs.br/revext/article/view/98892/55151. Acesso em: 04 jul. 2021.

SILVEIRA, A.; CUNHA, C. M. L. A influência da declividade nos processos erosivos da bacia do Tijuco Preto – SP. In: SIMPÓSIO NACIONAL DE GEOMORFOLOGIA, 6, 2006, Goiânia. **Anais do 6º Sinageo.** Goiânia - Go: S. I, 2006. p. 1-9.

TAGLIARINI, F. S. N. **Imagens de drone e Índice de Vegetação por Diferença Normalizada (NDVI) para classificação segmentada em Áreas de Preservação Permanente (APP)**. 2020. 148 f. Tese (Doutorado) - Curso de Agronomia, Faculdade de Ciências Agronômicas, Universidade Estadual Paulista (Unesp), Botucatu - SP, 2020.

TAMENE, L.; ADIMASSU, Z.; AYNEKULU, E.; YAEKOB, T. Estimating landscape susceptibility to soil erosion using a GIS-based approach in Northern Ethiopia. **International Soil and Water Conservation Research**, [S.L.], v. 5, n. 3, p. 221-230, set. 2017. Elsevier BV. http://dx.doi.org/10.1016/j.iswcr.2017.05.002.

TOMAZONI, J. C.; GUIMARÃES, E. A sistematização dos fatores da EUPS em SIG para quantificação da erosão laminar na bacia do rio Jirau. **Revista Brasileira de Cartografia**, [S.L.], v. 57, n. 3, p. 235-244, dez. 2005.

TULLIO, L. (org.). **Formação, classificação e cartografia dos solos**. Ponta Grossa - Pr: Atena Editora, 2019. 126 p. Disponível em: https://www.atenaeditora.com.br/wp-content/uploads/2019/09/E-book-Formacao-Classificacao-e-Cartografia-dos-Solos.pdf. Acesso em: 20 jul. 2021.

VIEL, J. A.; ROSA, K. K.; HOFF, R. Estudo da erosão superficial do solo por meio de SIG na região da denominação de origem Vale dos Vinhedos (Brasil). **Revista Brasileira de Geomorfologia**, [S.L.], v. 18, n. 3, p. 521-533, 11 ago. 2017. http://dx.doi.org/10.20502/rbg.v18i3.1197.

ZAIDAN, R. T. Geoprocessamento conceitos e definições. **Revista de Geografia - Ppgeo - Ufjf**, Juiz de Fora - Mg, v. 7, n. 2, p. 195-201, 28 set. 2017. Universidade Federal de Juiz de Fora. doi:10.34019/2236-837x.2017.v7.18073.
23

