"""Gera figuras ilustrativas para Aula 09 – ANOVA de Uma Via.
Estilo: infográfico didático com paleta UEFS.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Ellipse
from matplotlib.lines import Line2D
import numpy as np
from scipy.stats import f as f_dist
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
# FIG 1 – Erro Tipo I Acumulado (Infográfico com alertas)
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 5))
estilo_base(ax)

n_groups = np.arange(2, 9)
n_comp = n_groups * (n_groups - 1) / 2
erro_acum = 1 - (1 - 0.05)**n_comp

cores_barra = [VERDE if e < 0.10 else AMARELO if e < 0.20 else VERM_CLARO for e in erro_acum]
bars = ax.bar(n_groups, erro_acum * 100, color=cores_barra, edgecolor='white',
              linewidth=2, alpha=0.9, width=0.65, zorder=3)

# Linha limite
ax.axhline(5, color=VERM, linestyle='--', linewidth=2.5, zorder=2)
ax.text(8.2, 5, 'Limite\naceitavel\n(5%)', fontsize=9, color=VERM,
        fontweight='bold', va='center', ha='left')

# Zonas de fundo
ax.axhspan(0, 10, color='#E8F5E9', alpha=0.4, zorder=1)
ax.axhspan(10, 25, color='#FFF8E1', alpha=0.4, zorder=1)
ax.axhspan(25, 55, color='#FFEBEE', alpha=0.4, zorder=1)

# Anotacoes
for bar, ng, ea in zip(bars, n_groups, erro_acum):
    pct = f'{ea*100:.0f}%'
    y = bar.get_height()
    simbolo = 'ok' if ea < 0.10 else '!' if ea < 0.20 else 'X'
    ax.text(ng, y + 1.8, f'{simbolo} {pct}', ha='center', fontsize=10,
            fontweight='bold', color=CONTRASTE)

# Seta didatica
ax.annotate('Risco dispara\ncom comparacoes\nmultiplas!',
            xy=(7, erro_acum[-1]*100), xytext=(5.5, 48),
            fontsize=10, fontweight='bold', color=VERM,
            arrowprops=dict(arrowstyle='->', color=VERM, lw=2),
            ha='center')

ax.set_xlabel('Numero de grupos comparados', fontsize=12, fontweight='bold')
ax.set_ylabel('Risco de Erro Tipo I (%)', fontsize=12, fontweight='bold')
ax.set_title('Por que NAO usar varios Testes T?\nO erro acumulado cresce a cada comparacao',
             fontsize=13, fontweight='bold', color=AZUL, pad=12)
ax.set_ylim(0, 55)
ax.set_xticks(n_groups)
ax.set_xticklabels([f'{n} grupos\n({int(c)} testes)' for n, c in zip(n_groups, n_comp)], fontsize=9)

leg = [
    Line2D([0], [0], marker='s', color='w', markerfacecolor=VERDE, markersize=12, label='Risco aceitavel (< 10%)'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor=AMARELO, markersize=12, label='Risco moderado (10-25%)'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor=VERM_CLARO, markersize=12, label='Risco alto (> 25%)'),
]
ax.legend(handles=leg, fontsize=9, loc='upper left', framealpha=0.9)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_erro_tipo1_acumulado.png'), dpi=200, bbox_inches='tight', facecolor=BRANCO)
plt.close()
print('ok fig_erro_tipo1_acumulado.png')


# ═══════════════════════════════════════════════════════════════
# FIG 2 – Variancia Between vs Within (Diagrama conceitual)
# ═══════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
np.random.seed(42)

def draw_cluster(ax, cx, cy, n=12, spread=0.8, color='#2135A6', label=''):
    xs = np.random.normal(cx, spread, n)
    ys = np.random.normal(cy, spread, n)
    ax.scatter(xs, ys, color=color, s=60, alpha=0.7, edgecolors='white', linewidth=1, zorder=5)
    ell = Ellipse((cx, cy), width=spread*4.5, height=spread*4.5,
                  fill=False, edgecolor=color, linewidth=2, linestyle='--', alpha=0.6, zorder=4)
    ax.add_patch(ell)
    ax.text(cx, cy - spread*2.8, label, ha='center', fontsize=10, fontweight='bold', color=color)

# Painel A: F alto
ax = estilo_base(axes[0])
ax.set_xlim(-2, 18)
ax.set_ylim(-4, 12)
ax.set_aspect('equal')

draw_cluster(ax, 2, 7, spread=0.9, color='#2135A6', label='Sem cobertura')
draw_cluster(ax, 8, 4, spread=0.9, color=AZUL_APOIO, label='Cob. parcial')
draw_cluster(ax, 14, 1, spread=0.9, color=AZUL_PROF, label='Cob. densa')

ax.annotate('', xy=(5, 6), xytext=(3.5, 7), arrowprops=dict(arrowstyle='<->', color=VERDE_ESC, lw=2.5))
ax.annotate('', xy=(11, 2.5), xytext=(9, 4), arrowprops=dict(arrowstyle='<->', color=VERDE_ESC, lw=2.5))

ax.set_title('F alto: Grupos BEM separados\n(Variancia ENTRE >> DENTRO)', fontsize=11,
             fontweight='bold', color=VERDE_ESC, pad=10)

# Painel B: F baixo
ax = estilo_base(axes[1])
ax.set_xlim(-2, 18)
ax.set_ylim(-4, 12)
ax.set_aspect('equal')

draw_cluster(ax, 7, 5, n=12, spread=2.5, color='#2135A6', label='Sem cobertura')
draw_cluster(ax, 8.5, 4.5, n=12, spread=2.5, color=AZUL_APOIO, label='Cob. parcial')
draw_cluster(ax, 10, 4, n=12, spread=2.5, color=AZUL_PROF, label='Cob. densa')

ax.set_title('F baixo: Grupos MISTURADOS\n(Variancia ENTRE = DENTRO)', fontsize=11,
             fontweight='bold', color=VERM, pad=10)

fig.suptitle('Logica da ANOVA: Como a Estatistica F ve os dados',
             fontsize=14, fontweight='bold', color=AZUL, y=1.03)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_between_within.png'), dpi=200, bbox_inches='tight', facecolor=BRANCO)
plt.close()
print('ok fig_between_within.png')


# ═══════════════════════════════════════════════════════════════
# FIG 3 – Boxplot contextualizado (solo + cobertura vegetal)
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 5.5))
estilo_base(ax)

np.random.seed(7)
sem_cob = np.array([18.5, 22.1, 19.8, 25.3, 20.7, 23.4, 21.0, 24.2])
parc_cob = np.array([12.3, 14.5, 11.2, 13.8, 15.1, 12.7, 13.0, 14.8])
densa_cob = np.array([5.8, 7.2, 4.9, 6.5, 8.1, 5.3, 6.0, 7.5])

cores = [VERM_CLARO, AMARELO, VERDE]
dados = [sem_cob, parc_cob, densa_cob]
nomes = ['Sem\ncobertura', 'Cobertura\nparcial', 'Cobertura\ndensa']

parts = ax.violinplot(dados, positions=[1, 2, 3], showmeans=False, showmedians=False, showextrema=False)
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(cores[i])
    pc.set_alpha(0.25)

bp = ax.boxplot(dados, positions=[1, 2, 3], widths=0.3, patch_artist=True,
                medianprops=dict(color=BRANCO, linewidth=2.5),
                whiskerprops=dict(color=CONTRASTE, linewidth=1.5),
                capprops=dict(color=CONTRASTE, linewidth=1.5),
                flierprops=dict(marker='o', markerfacecolor=CONTRASTE, markersize=4))

for i, (box, cor) in enumerate(zip(bp['boxes'], cores)):
    box.set_facecolor(cor)
    box.set_alpha(0.85)
    box.set_edgecolor(CONTRASTE)
    box.set_linewidth(1.5)

for i, (data, cor) in enumerate(zip(dados, cores)):
    jitter = np.random.uniform(-0.08, 0.08, len(data))
    ax.scatter([i+1 + j for j in jitter], data, color=BRANCO, edgecolors=CONTRASTE,
               s=45, zorder=5, linewidth=1.2)

for i, (d, cor) in enumerate(zip(dados, cores)):
    m = np.mean(d)
    ax.plot([i+0.65, i+1.35], [m, m], color=cor, linewidth=1, linestyle=':', alpha=0.6)
    ax.text(i+1.4, m, f'media = {m:.1f}', fontsize=9, fontweight='bold', color=cor, va='center')

def sig_bar(ax, x1, x2, y, text, color=AZUL):
    ax.plot([x1, x1, x2, x2], [y, y+0.5, y+0.5, y], color=color, linewidth=1.5)
    ax.text((x1+x2)/2, y+0.7, text, ha='center', fontsize=9, fontweight='bold', color=color)

sig_bar(ax, 1, 2, 27, 'p < 0,01 **')
sig_bar(ax, 1, 3, 29.5, 'p < 0,001 ***', VERM)
sig_bar(ax, 2, 3, 25, 'p < 0,05 *', AZUL_APOIO)

ax.set_ylabel('Perda de solo (t/ha/ano)', fontsize=12, fontweight='bold')
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(nomes, fontsize=11, fontweight='bold')
ax.set_title('ANOVA Uma Via - Perda de Solo por Tipo de Cobertura Vegetal',
             fontsize=13, fontweight='bold', color=AZUL, pad=12)
ax.set_ylim(2, 33)

ax.text(0.98, 0.02, 'Dados ilustrativos - 8 parcelas/grupo',
        transform=ax.transAxes, fontsize=8, color='gray', ha='right', va='bottom', style='italic')

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_anova_boxplot.png'), dpi=200, bbox_inches='tight', facecolor=BRANCO)
plt.close()
print('ok fig_anova_boxplot.png')


# ═══════════════════════════════════════════════════════════════
# FIG 4 – Distribuicao F (didatica com zonas e decisao)
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 4.5))
estilo_base(ax)

x = np.linspace(0.01, 10, 800)
y = f_dist.pdf(x, 2, 6)
f_crit = f_dist.ppf(0.95, 2, 6)
f_calc = 3.97

ax.fill_between(x, y, where=(x <= f_crit), alpha=0.12, color=AZUL, zorder=2)
ax.fill_between(x, y, where=(x >= f_crit), alpha=0.35, color=VERM_CLARO, zorder=2)
ax.plot(x, y, color=AZUL, linewidth=3, zorder=3)

ax.axvline(f_crit, color=VERM, linestyle='--', linewidth=2.5, zorder=4)
ax.axvline(f_calc, color=VERDE, linestyle='-', linewidth=3, zorder=4)

ax.annotate(f'F critico = {f_crit:.2f}\n(alfa = 0,05)',
            xy=(f_crit, f_dist.pdf(f_crit, 2, 6) + 0.01),
            xytext=(f_crit + 1.5, 0.35),
            fontsize=10, fontweight='bold', color=VERM,
            arrowprops=dict(arrowstyle='->', color=VERM, lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=VERM, alpha=0.9))

ax.annotate(f'F calculado = {f_calc}\n(nosso resultado)',
            xy=(f_calc, f_dist.pdf(f_calc, 2, 6) + 0.01),
            xytext=(f_calc - 2.5, 0.42),
            fontsize=10, fontweight='bold', color=VERDE_ESC,
            arrowprops=dict(arrowstyle='->', color=VERDE_ESC, lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9', edgecolor=VERDE_ESC, alpha=0.9))

ax.text(2, 0.02, 'Nao rejeita H0\n(sem evidencia)', ha='center', fontsize=9,
        color=AZUL, fontweight='bold', style='italic')
ax.text(7.5, 0.02, 'Rejeita H0\n(diferenca\nsignificativa)', ha='center', fontsize=9,
        color=VERM, fontweight='bold', style='italic')

ax.text(0.98, 0.95, f'F calc ({f_calc}) < F crit ({f_crit:.2f})\n-> NAO rejeitamos H0',
        transform=ax.transAxes, fontsize=10, fontweight='bold', color=AZUL_PROF,
        ha='right', va='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#E8EAF6', edgecolor=AZUL, alpha=0.9))

ax.set_xlabel('Estatistica F', fontsize=12, fontweight='bold')
ax.set_ylabel('Densidade', fontsize=11)
ax.set_title('Distribuicao F (gl1 = 2, gl2 = 6) - Decisao Estatistica',
             fontsize=13, fontweight='bold', color=AZUL, pad=12)
ax.set_xlim(0, 10)
ax.set_ylim(0, 0.55)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_distribuicao_f.png'), dpi=200, bbox_inches='tight', facecolor=BRANCO)
plt.close()
print('ok fig_distribuicao_f.png')


# ═══════════════════════════════════════════════════════════════
# FIG 5 – Post-hoc (diagrama de comparacoes par a par)
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 5.5))
estilo_base(ax, remover_eixos=True)
ax.set_xlim(-1, 13)
ax.set_ylim(-2, 10)
ax.set_aspect('equal')

rect_bg = FancyBboxPatch((-0.5, -1.5), 13, 11, boxstyle="round,pad=0.3",
                          facecolor=FUNDO, edgecolor=AZUL_APOIO, linewidth=1.5, alpha=0.4)
ax.add_patch(rect_bg)

grupos = [
    (2, 4, 'Sem\ncobertura', VERM_CLARO, 'media = 21,5 t/ha'),
    (6, 4, 'Cobertura\nparcial', AMARELO, 'media = 13,2 t/ha'),
    (10, 4, 'Cobertura\ndensa', VERDE, 'media = 6,3 t/ha'),
]

for cx, cy, lbl, cor, media in grupos:
    caixa = FancyBboxPatch((cx-1.3, cy-1.2), 2.6, 2.8,
                            boxstyle="round,pad=0.15", facecolor=cor,
                            edgecolor=CONTRASTE, linewidth=2, alpha=0.85, zorder=5)
    ax.add_patch(caixa)
    ax.text(cx, cy+0.5, lbl, ha='center', va='center', fontsize=11,
            fontweight='bold', color=BRANCO, zorder=6)
    ax.text(cx, cy-0.5, media, ha='center', va='center', fontsize=9,
            color=BRANCO, zorder=6, style='italic')

def arco_comp(ax, x1, x2, y_base, y_top, texto, cor, lw=2.5):
    mid = (x1 + x2) / 2
    ax.annotate('', xy=(x2, y_base), xytext=(x1, y_base),
                arrowprops=dict(arrowstyle='<->', connectionstyle='arc3,rad=-0.3',
                                color=cor, lw=lw))
    ax.text(mid, y_top, texto, ha='center', fontsize=10, fontweight='bold', color=cor,
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BRANCO, edgecolor=cor, alpha=0.9))

arco_comp(ax, 2, 6, 7.0, 8.2, 'p < 0,01 **', AZUL)
arco_comp(ax, 6, 10, 7.0, 8.2, 'p < 0,05 *', AZUL_APOIO)

ax.annotate('', xy=(10, 2.5), xytext=(2, 2.5),
            arrowprops=dict(arrowstyle='<->', connectionstyle='arc3,rad=0.25',
                            color=VERM, lw=3))
ax.text(6, 0.5, 'p < 0,001 ***', ha='center', fontsize=11, fontweight='bold', color=VERM,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=VERM, alpha=0.9))

ax.set_title('Testes Post-hoc: Quais grupos diferem entre si?',
             fontsize=14, fontweight='bold', color=AZUL, pad=15)

ax.text(6, -1.3, 'Post-hoc realizado apenas quando F e significativo (p < 0,05)',
        ha='center', fontsize=9, color='gray', style='italic')

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_posthoc_visual.png'), dpi=200, bbox_inches='tight', facecolor=BRANCO)
plt.close()
print('ok fig_posthoc_visual.png')


# ═══════════════════════════════════════════════════════════════
# FIG 6 – Tamanho de efeito omega2 (termometro visual)
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 4))
estilo_base(ax, remover_eixos=True)
ax.set_xlim(-0.5, 11)
ax.set_ylim(-1, 5)

faixas = [
    (0, 2.0, '< 0,01\nNenhum', '#E8EAF6', CONTRASTE),
    (2.0, 4.5, '0,01 - 0,06\nPequeno', '#C5CAE9', CONTRASTE),
    (4.5, 7.0, '0,06 - 0,14\nMedio', '#7986CB', BRANCO),
    (7.0, 10.0, '>= 0,14\nGrande', '#3949AB', BRANCO),
]

for x0, x1, lbl, cor, txt_cor in faixas:
    rect = FancyBboxPatch((x0, 1.5), x1-x0, 1.8,
                           boxstyle="round,pad=0.05", facecolor=cor,
                           edgecolor=AZUL, linewidth=1.5, zorder=3)
    ax.add_patch(rect)
    ax.text((x0+x1)/2, 2.4, lbl, ha='center', va='center', fontsize=10,
            fontweight='bold', color=txt_cor, zorder=4)

exemplo_x = 6.0
ax.annotate('omega2 = 0,12\n(nosso exemplo)',
            xy=(exemplo_x, 1.4), xytext=(exemplo_x, -0.3),
            fontsize=11, fontweight='bold', color=AZUL_PROF, ha='center',
            arrowprops=dict(arrowstyle='->', color=AZUL_PROF, lw=2.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8EAF6', edgecolor=AZUL_PROF))

ax.annotate('', xy=(10.2, 2.4), xytext=(-0.2, 2.4),
            arrowprops=dict(arrowstyle='->', color=CONTRASTE, lw=1.5, linestyle='--'))
ax.text(-0.3, 3.8, 'Efeito\nfraco', fontsize=9, color='gray', ha='center', fontweight='bold')
ax.text(10.3, 3.8, 'Efeito\nforte', fontsize=9, color='gray', ha='center', fontweight='bold')

ax.set_title('omega2 (Omega ao Quadrado) - Tamanho de Efeito na ANOVA (Field, 2013)',
             fontsize=13, fontweight='bold', color=AZUL, pad=15)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_omega2.png'), dpi=200, bbox_inches='tight', facecolor=BRANCO)
plt.close()
print('ok fig_omega2.png')


print('\n=== Todas as 6 figuras geradas! ===')
