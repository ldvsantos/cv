"""Gera figuras ilustrativas para Aula 10 – ANOVA Fatorial.
Estilo: infografico didatico com paleta UEFS.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse, Patch
from matplotlib.lines import Line2D
import numpy as np
import os

# ── Paleta UEFS ──
AZUL = '#2135A6'
AZUL_PROF = '#27368C'
AZUL_APOIO = '#586BA6'
FUNDO = '#F2F2F2'
CONTRASTE = '#0D0D0D'
VERM = '#C62828'
VERM_CLARO = '#E74C3C'
AMARELO = '#F39C12'
VERDE = '#2ECC71'
VERDE_ESC = '#1B7A3D'
BRANCO = '#FFFFFF'
LARANJA = '#E67E22'

OUT = os.path.dirname(os.path.abspath(__file__))


def estilo_base(ax, remover_eixos=False):
    """Aplica estilo limpo."""
    if remover_eixos:
        ax.axis('off')
    else:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    return ax


# ═══════════════════════════════════════════════════════════════
# FIG 1 – Conceito: ANOVA Uma Via vs Fatorial (infografico)
# ═══════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

# ── Painel A: ANOVA Uma Via ──
ax = estilo_base(axes[0])
np.random.seed(42)
sem_cob = np.random.normal(22, 3.5, 15)
parcial = np.random.normal(15, 3.0, 15)
densa = np.random.normal(8, 2.5, 15)

dados_a = [sem_cob, parcial, densa]
cores_a = [VERM_CLARO, AMARELO, VERDE]
nomes_a = ['Sem\ncobertura', 'Cobertura\nparcial', 'Cobertura\ndensa']

parts = ax.violinplot(dados_a, positions=[1, 2, 3], showmeans=False,
                      showmedians=False, showextrema=False)
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(cores_a[i])
    pc.set_alpha(0.2)

bp = ax.boxplot(dados_a, positions=[1, 2, 3], widths=0.3, patch_artist=True,
                medianprops=dict(color=BRANCO, linewidth=2),
                whiskerprops=dict(color=CONTRASTE, linewidth=1.2),
                capprops=dict(color=CONTRASTE, linewidth=1.2),
                flierprops=dict(marker='o', markerfacecolor=CONTRASTE, markersize=3))
for i, box in enumerate(bp['boxes']):
    box.set_facecolor(cores_a[i])
    box.set_alpha(0.8)
    box.set_edgecolor(CONTRASTE)

ax.set_xticks([1, 2, 3])
ax.set_xticklabels(nomes_a, fontsize=10, fontweight='bold')
ax.set_ylabel('Perda de solo (t/ha/ano)', fontsize=11, fontweight='bold')
ax.set_title('ANOVA Uma Via\n1 Fator: Cobertura vegetal', fontsize=12,
             fontweight='bold', color=AZUL, pad=10)

ax.annotate('Um unico fator\n3 niveis', xy=(2, 3), fontsize=10,
            fontweight='bold', color=AZUL_APOIO, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8EAF6',
                      edgecolor=AZUL_APOIO, alpha=0.9))

# ── Painel B: ANOVA Fatorial ──
ax = estilo_base(axes[1])
x = np.array([1, 2, 3])
taboa = np.array([4.2, 6.1, 7.8])
ouricuri = np.array([3.8, 8.5, 10.2])

ax.fill_between(x, taboa - 0.8, taboa + 0.8, color=AZUL, alpha=0.1)
ax.fill_between(x, ouricuri - 1.0, ouricuri + 1.0, color=VERM_CLARO, alpha=0.1)

ax.plot(x, taboa, 'o-', color=AZUL, linewidth=3, markersize=12, label='Taboa',
        markerfacecolor=AZUL, markeredgecolor=BRANCO, markeredgewidth=2, zorder=5)
ax.plot(x, ouricuri, 's--', color=VERM_CLARO, linewidth=3, markersize=12, label='Ouricuri',
        markerfacecolor=VERM_CLARO, markeredgecolor=BRANCO, markeredgewidth=2, zorder=5)

ax.set_xticks(x)
ax.set_xticklabels(['Sem\nresina', '1x\nresina', '2x\nresina'], fontsize=10, fontweight='bold')
ax.set_ylabel('Resistencia a tracao (kN/m)', fontsize=11, fontweight='bold')
ax.set_title('ANOVA Fatorial\n2 Fatores: Fibra x Resina', fontsize=12,
             fontweight='bold', color=AZUL, pad=10)
ax.legend(fontsize=10, loc='upper left', framealpha=0.9)

# Seta mostrando interacao
ax.annotate('Interacao!\nOuricuri ganha\nmais com resina',
            xy=(2.5, 9.3), xytext=(1.3, 10.5),
            fontsize=9, fontweight='bold', color=VERM,
            arrowprops=dict(arrowstyle='->', color=VERM, lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE',
                      edgecolor=VERM, alpha=0.9))

ax.annotate('Dois fatores\ncruzados', xy=(1, 5), fontsize=10,
            fontweight='bold', color=AZUL_APOIO, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8EAF6',
                      edgecolor=AZUL_APOIO, alpha=0.9))

fig.suptitle('Da ANOVA Uma Via a Fatorial: por que cruzar fatores?',
             fontsize=14, fontweight='bold', color=AZUL_PROF, y=1.02)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_anova_fatorial_conceito.png'),
            dpi=200, bbox_inches='tight', facecolor=BRANCO)
plt.close()
print('ok fig_anova_fatorial_conceito.png')


# ═══════════════════════════════════════════════════════════════
# FIG 2 – Estrutura Fatorial (grid ilustrativo com destaque)
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 5.5))
estilo_base(ax, remover_eixos=True)
ax.set_xlim(-1, 13)
ax.set_ylim(-1.5, 8)

# Fundo
rect_bg = FancyBboxPatch((-0.5, -1), 13, 8.5, boxstyle="round,pad=0.3",
                          facecolor=FUNDO, edgecolor=AZUL_APOIO,
                          linewidth=1.5, alpha=0.4)
ax.add_patch(rect_bg)

# Titulo coluna
ax.text(6.5, 7, 'Fator B: Dosagem de Resina', ha='center',
        fontsize=14, fontweight='bold', color=AZUL)

col_labels = ['Sem Resina', '1x Resina', '2x Resina']
col_x = [3, 6.5, 10]
for cx, lbl in zip(col_x, col_labels):
    ax.text(cx, 6.2, lbl, ha='center', fontsize=11, fontweight='bold', color=AZUL_APOIO)

# Titulo linha
ax.text(-0.3, 3.5, 'Fator A:\nFibra', ha='center', va='center',
        fontsize=13, fontweight='bold', color=AZUL)

# Celulas
fibras = ['Taboa', 'Ouricuri']
row_y = [4.5, 1.8]
cores_fibra = [AZUL_APOIO, VERM_CLARO]
cores_cell = [['#C5CEE8', '#9FB3E8', '#7A8FD8'],
              ['#F8C4C4', '#F09898', '#E87070']]

for i, (fibra, fy, cor_f) in enumerate(zip(fibras, row_y, cores_fibra)):
    ax.text(1.0, fy + 0.3, fibra, ha='center', va='center',
            fontsize=12, fontweight='bold', color=cor_f)

    for j, cx in enumerate(col_x):
        rect = FancyBboxPatch((cx - 1.3, fy - 0.7), 2.6, 1.6,
                               boxstyle="round,pad=0.12",
                               facecolor=cores_cell[i][j],
                               edgecolor=CONTRASTE, linewidth=2, alpha=0.85, zorder=5)
        ax.add_patch(rect)
        celula_num = i * 3 + j + 1
        ax.text(cx, fy + 0.15, f'Celula {celula_num}', ha='center', va='center',
                fontsize=10, fontweight='bold', color=CONTRASTE, zorder=6)
        ax.text(cx, fy - 0.25, 'n = 5', ha='center', va='center',
                fontsize=9, color=CONTRASTE, zorder=6, style='italic')

# Resumo
ax.text(6.5, -0.5, '2 x 3 = 6 celulas  |  N total = 30  |  Delineamento completamente cruzado',
        ha='center', fontsize=11, fontweight='bold', color=AZUL_PROF,
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#E8EAF6',
                  edgecolor=AZUL_PROF, alpha=0.9))

ax.set_title('Estrutura do Delineamento Fatorial 2 x 3',
             fontsize=14, fontweight='bold', color=AZUL, pad=15)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_estrutura_fatorial.png'),
            dpi=200, bbox_inches='tight', facecolor=BRANCO)
plt.close()
print('ok fig_estrutura_fatorial.png')


# ═══════════════════════════════════════════════════════════════
# FIG 3 – Interacao AUSENTE (linhas paralelas, didatico)
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 5))
estilo_base(ax)

x = np.array([1, 2, 3])
taboa = np.array([4.0, 6.0, 8.0])
ouricuri = np.array([6.0, 8.0, 10.0])

# Faixa de confianca
ax.fill_between(x, taboa - 0.6, taboa + 0.6, color=AZUL, alpha=0.08)
ax.fill_between(x, ouricuri - 0.6, ouricuri + 0.6, color=VERM_CLARO, alpha=0.08)

ax.plot(x, taboa, 'o-', color=AZUL, linewidth=3, markersize=14, label='Taboa',
        markerfacecolor=AZUL, markeredgecolor=BRANCO, markeredgewidth=2, zorder=5)
ax.plot(x, ouricuri, 's-', color=VERM_CLARO, linewidth=3, markersize=14, label='Ouricuri',
        markerfacecolor=VERM_CLARO, markeredgecolor=BRANCO, markeredgewidth=2, zorder=5)

# Anotacoes nos pontos
for xi, yt, yo in zip(x, taboa, ouricuri):
    ax.text(xi + 0.12, yt - 0.5, f'{yt:.0f}', fontsize=9, fontweight='bold', color=AZUL)
    ax.text(xi + 0.12, yo + 0.3, f'{yo:.0f}', fontsize=9, fontweight='bold', color=VERM_CLARO)

# Setas mostrando distancia constante
for xi in [1, 2, 3]:
    yt_v = taboa[xi - 1]
    yo_v = ouricuri[xi - 1]
    ax.annotate('', xy=(xi - 0.15, yo_v), xytext=(xi - 0.15, yt_v),
                arrowprops=dict(arrowstyle='<->', color=VERDE_ESC, lw=2))

ax.text(0.7, 5.0, 'Mesma\ndistancia', fontsize=9, fontweight='bold', color=VERDE_ESC,
        rotation=90, ha='center', va='center')

ax.set_xticks(x)
ax.set_xticklabels(['Sem resina', '1x resina', '2x resina'], fontsize=11, fontweight='bold')
ax.set_ylabel('Resistencia (kN/m)', fontsize=12, fontweight='bold')
ax.legend(fontsize=11, loc='upper left', framealpha=0.9)

ax.set_title('SEM Interacao: linhas PARALELAS\nO efeito da resina e igual para ambas as fibras',
             fontsize=13, fontweight='bold', color=VERDE_ESC, pad=12)

ax.text(0.98, 0.02, 'Delta sempre = 2,0 kN/m',
        transform=ax.transAxes, fontsize=9, color='gray',
        ha='right', va='bottom', style='italic')

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_interacao_ausente.png'),
            dpi=200, bbox_inches='tight', facecolor=BRANCO)
plt.close()
print('ok fig_interacao_ausente.png')


# ═══════════════════════════════════════════════════════════════
# FIG 4 – Interacao PRESENTE (linhas divergem, didatico)
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 5))
estilo_base(ax)

x = np.array([1, 2, 3])
taboa = np.array([4.2, 6.1, 7.8])
ouricuri = np.array([3.8, 8.5, 10.2])

ax.fill_between(x, taboa - 0.8, taboa + 0.8, color=AZUL, alpha=0.08)
ax.fill_between(x, ouricuri - 1.0, ouricuri + 1.0, color=VERM_CLARO, alpha=0.08)

ax.plot(x, taboa, 'o-', color=AZUL, linewidth=3, markersize=14, label='Taboa',
        markerfacecolor=AZUL, markeredgecolor=BRANCO, markeredgewidth=2, zorder=5)
ax.plot(x, ouricuri, 's--', color=VERM_CLARO, linewidth=3, markersize=14, label='Ouricuri',
        markerfacecolor=VERM_CLARO, markeredgecolor=BRANCO, markeredgewidth=2, zorder=5)

# Anotacoes nos pontos
for xi, yt, yo in zip(x, taboa, ouricuri):
    ax.text(xi + 0.12, yt - 0.5, f'{yt:.1f}', fontsize=9, fontweight='bold', color=AZUL)
    ax.text(xi + 0.12, yo + 0.3, f'{yo:.1f}', fontsize=9, fontweight='bold', color=VERM_CLARO)

# Setas mostrando distancia VARIAVEL
deltas = ouricuri - taboa
for i, xi in enumerate([1, 2, 3]):
    yt_v = taboa[i]
    yo_v = ouricuri[i]
    cor_delta = VERDE_ESC if abs(deltas[i]) < 1 else AMARELO if abs(deltas[i]) < 3 else VERM
    ax.annotate('', xy=(xi - 0.15, yo_v), xytext=(xi - 0.15, yt_v),
                arrowprops=dict(arrowstyle='<->', color=cor_delta, lw=2.5))
    ax.text(xi - 0.3, (yt_v + yo_v) / 2, f'{deltas[i]:+.1f}', fontsize=8,
            fontweight='bold', color=cor_delta, ha='center', va='center',
            rotation=90)

# Zona de cruzamento
ax.axvspan(0.8, 1.3, color='#FFF8E1', alpha=0.4, zorder=1)
ax.text(1.05, 2.8, 'Quase\niguais', fontsize=8, color=AMARELO, ha='center',
        fontweight='bold', style='italic')

# Anotacao principal
ax.annotate('Ouricuri ganha MAIS\ncom resina!\n(interacao ordinal)',
            xy=(2.8, 10), xytext=(1.5, 11),
            fontsize=10, fontweight='bold', color=VERM,
            arrowprops=dict(arrowstyle='->', color=VERM, lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE',
                      edgecolor=VERM, alpha=0.9))

ax.set_xticks(x)
ax.set_xticklabels(['Sem resina', '1x resina', '2x resina'], fontsize=11, fontweight='bold')
ax.set_ylabel('Resistencia (kN/m)', fontsize=12, fontweight='bold')
ax.legend(fontsize=11, loc='lower right', framealpha=0.9)
ax.set_ylim(2, 12.5)

ax.set_title('COM Interacao: linhas DIVERGEM\nO efeito da resina DEPENDE do tipo de fibra',
             fontsize=13, fontweight='bold', color=VERM, pad=12)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_interacao_presente.png'),
            dpi=200, bbox_inches='tight', facecolor=BRANCO)
plt.close()
print('ok fig_interacao_presente.png')


# ═══════════════════════════════════════════════════════════════
# FIG 5 – Exemplo fatorial: violin+box+jitter com significancia
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(11, 5.5))
estilo_base(ax)

np.random.seed(7)
celulas = {
    'Taboa\nSem': (np.random.normal(4.2, 0.8, 8), AZUL_APOIO),
    'Taboa\n1x': (np.random.normal(6.1, 0.9, 8), AZUL),
    'Taboa\n2x': (np.random.normal(7.8, 1.1, 8), AZUL_PROF),
    'Ouricuri\nSem': (np.random.normal(3.8, 0.7, 8), '#F8C4C4'),
    'Ouricuri\n1x': (np.random.normal(8.5, 1.2, 8), VERM_CLARO),
    'Ouricuri\n2x': (np.random.normal(10.2, 1.4, 8), VERM),
}

posicoes = [1, 2, 3, 4.5, 5.5, 6.5]
dados_list = [v[0] for v in celulas.values()]
cores_list = [v[1] for v in celulas.values()]
nomes_list = list(celulas.keys())

# Violin
parts = ax.violinplot(dados_list, positions=posicoes, showmeans=False,
                      showmedians=False, showextrema=False)
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(cores_list[i])
    pc.set_alpha(0.2)

# Boxplot
bp = ax.boxplot(dados_list, positions=posicoes, widths=0.35, patch_artist=True,
                medianprops=dict(color=BRANCO, linewidth=2.5),
                whiskerprops=dict(color=CONTRASTE, linewidth=1.2),
                capprops=dict(color=CONTRASTE, linewidth=1.2),
                flierprops=dict(marker='o', markerfacecolor=CONTRASTE, markersize=3))
for i, box in enumerate(bp['boxes']):
    box.set_facecolor(cores_list[i])
    box.set_alpha(0.8)
    box.set_edgecolor(CONTRASTE)
    box.set_linewidth(1.5)

# Jitter
for i, (data, pos) in enumerate(zip(dados_list, posicoes)):
    jit = np.random.uniform(-0.08, 0.08, len(data))
    ax.scatter([pos + j for j in jit], data, color=BRANCO,
               edgecolors=CONTRASTE, s=35, zorder=5, linewidth=1)

# Medias anotadas
for i, (data, pos, cor) in enumerate(zip(dados_list, posicoes, cores_list)):
    m = np.mean(data)
    ax.text(pos, -0.3, f'{m:.1f}', ha='center', fontsize=8,
            fontweight='bold', color=cor)

# Separador visual
ax.axvline(3.75, color='gray', linestyle=':', linewidth=1, alpha=0.5)
ax.text(2, 13.5, 'TABOA', fontsize=12, fontweight='bold', color=AZUL,
        ha='center', bbox=dict(facecolor='#E8EAF6', edgecolor=AZUL, alpha=0.7,
                               boxstyle='round,pad=0.3'))
ax.text(5.5, 13.5, 'OURICURI', fontsize=12, fontweight='bold', color=VERM,
        ha='center', bbox=dict(facecolor='#FFEBEE', edgecolor=VERM, alpha=0.7,
                               boxstyle='round,pad=0.3'))

# Barras de significancia
def sig_bar(ax, x1, x2, y, text, color=AZUL):
    ax.plot([x1, x1, x2, x2], [y, y + 0.3, y + 0.3, y], color=color, linewidth=1.5)
    ax.text((x1 + x2) / 2, y + 0.4, text, ha='center', fontsize=8,
            fontweight='bold', color=color)

sig_bar(ax, 1, 3, 11, 'p < 0,001 ***', AZUL_PROF)
sig_bar(ax, 4.5, 6.5, 12.2, 'p < 0,001 ***', VERM)

ax.set_xticks(posicoes)
ax.set_xticklabels(nomes_list, fontsize=9, fontweight='bold')
ax.set_ylabel('Resistencia a tracao (kN/m)', fontsize=12, fontweight='bold')
ax.set_title('ANOVA Fatorial 2 x 3 — Geotexteis Naturais\nFibra (Taboa vs Ouricuri) x Dosagem de Resina',
             fontsize=13, fontweight='bold', color=AZUL, pad=12)
ax.set_ylim(-1, 14.5)

ax.text(0.98, 0.02, 'Dados ilustrativos — 8 amostras por celula',
        transform=ax.transAxes, fontsize=8, color='gray',
        ha='right', va='bottom', style='italic')

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_exemplo_fatorial.png'),
            dpi=200, bbox_inches='tight', facecolor=BRANCO)
plt.close()
print('ok fig_exemplo_fatorial.png')


# ═══════════════════════════════════════════════════════════════
# FIG 6 – Eta parcial ao quadrado (escala visual com zonas)
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 5))
estilo_base(ax, remover_eixos=True)
ax.set_xlim(-0.5, 11)
ax.set_ylim(-2.5, 7)

# Escala de fundo
faixas = [
    (0, 1.0, '< 0,01\nNenhum', '#E8EAF6', CONTRASTE),
    (1.0, 3.0, '0,01 - 0,06\nPequeno', '#C5CAE9', CONTRASTE),
    (3.0, 5.5, '0,06 - 0,14\nMedio', '#7986CB', BRANCO),
    (5.5, 10.0, '>= 0,14\nGrande', '#3949AB', BRANCO),
]

for x0, x1, lbl, cor, txt_cor in faixas:
    rect = FancyBboxPatch((x0, 4.5), x1 - x0, 1.5,
                           boxstyle="round,pad=0.05", facecolor=cor,
                           edgecolor=AZUL, linewidth=1.5, zorder=3)
    ax.add_patch(rect)
    ax.text((x0 + x1) / 2, 5.25, lbl, ha='center', va='center',
            fontsize=10, fontweight='bold', color=txt_cor, zorder=4)

# Seta direcional
ax.annotate('', xy=(10.2, 5.25), xytext=(-0.2, 5.25),
            arrowprops=dict(arrowstyle='->', color=CONTRASTE, lw=1.5, linestyle='--'))
ax.text(-0.4, 6.3, 'Efeito\nfraco', fontsize=9, color='gray',
        ha='center', fontweight='bold')
ax.text(10.3, 6.3, 'Efeito\nforte', fontsize=9, color='gray',
        ha='center', fontweight='bold')

# Marcadores dos tres efeitos do exemplo
efeitos = [
    ('Fibra (A)', 0.34, AZUL_APOIO, 2.5),
    ('Resina (B)', 0.79, AZUL, 1.0),
    ('A x B', 0.26, AZUL_PROF, -0.5),
]

for nome, eta, cor, y_pos in efeitos:
    # Posicao na escala (0 a 10 mapeando 0 a 1)
    x_pos = eta * 10
    # Marcador triangular
    ax.annotate(f'{nome}\neta2p = {eta:.2f}',
                xy=(x_pos, 4.4), xytext=(x_pos, y_pos),
                fontsize=11, fontweight='bold', color=cor, ha='center',
                arrowprops=dict(arrowstyle='->', color=cor, lw=2.5),
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BRANCO,
                          edgecolor=cor, linewidth=2, alpha=0.95))

# Classificacao dos efeitos
ax.text(3.4, -1.8, 'Todos os tres efeitos sao GRANDES (> 0,14) neste exemplo',
        fontsize=10, fontweight='bold', color=AZUL_PROF, ha='left', style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8EAF6',
                  edgecolor=AZUL_PROF, alpha=0.8))

# Destaque para resina
ax.text(8.2, 2.0, 'Resina explica\n79% da variancia!',
        fontsize=10, fontweight='bold', color=VERM, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE',
                  edgecolor=VERM, alpha=0.9))

ax.set_title('Eta Parcial ao Quadrado (eta2p) — Tamanho de Efeito na ANOVA Fatorial (Cohen, 1988)',
             fontsize=13, fontweight='bold', color=AZUL, pad=15)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_eta_parcial.png'),
            dpi=200, bbox_inches='tight', facecolor=BRANCO)
plt.close()
print('ok fig_eta_parcial.png')


print('\n=== Todas as 6 figuras da ANOVA Fatorial geradas! ===')
