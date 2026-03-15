"""Gera figuras didáticas para Aula 5 - ANOVA de Uma Via."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle
from scipy.stats import f as f_dist
import os

AZUL = '#2135A6'
AZUL_APOIO = '#586BA6'
CONTRASTE = '#0D0D0D'
OUT = os.path.dirname(os.path.abspath(__file__))

# --- Fig 1: Por que ANOVA? (Erro Tipo I acumulado) ---
fig, ax = plt.subplots(figsize=(8, 4))
n_groups = np.arange(2, 11)
n_comp = n_groups * (n_groups - 1) / 2
erro_acum = 1 - (1 - 0.05)**n_comp

ax.bar(n_groups, erro_acum * 100, color=AZUL_APOIO, edgecolor='white', linewidth=1.5, alpha=0.85)
ax.axhline(5, color='#E74C3C', linestyle='--', linewidth=2, label='Limite aceitavel (5%)')
for i, (ng, ea) in enumerate(zip(n_groups, erro_acum)):
    ax.text(ng, ea * 100 + 1.5, f'{ea*100:.0f}%', ha='center', fontsize=9, fontweight='bold', color=CONTRASTE)

ax.set_xlabel('Numero de Grupos', fontsize=12, fontweight='bold')
ax.set_ylabel('Risco de Erro Tipo I (%)', fontsize=12, fontweight='bold')
ax.set_title('Por que usar ANOVA?\nErro Tipo I acumulado com multiplos Testes T', fontsize=12, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=10)
ax.set_ylim(0, 105)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_erro_tipo1_acumulado.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_erro_tipo1_acumulado.png')

# --- Fig 2: Variância Between vs Within ---
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
np.random.seed(42)

g1a = np.random.normal(10, 1.5, 15)
g2a = np.random.normal(20, 1.5, 15)
g3a = np.random.normal(30, 1.5, 15)

for i, (g, cor) in enumerate([(g1a, '#2135A6'), (g2a, '#586BA6'), (g3a, '#27368C')]):
    jitter = np.random.uniform(-0.15, 0.15, len(g))
    axes[0].scatter([i+1+j for j in jitter], g, color=cor, alpha=0.7, s=40, edgecolors='white')
    axes[0].plot([i+0.7, i+1.3], [np.mean(g), np.mean(g)], color=cor, linewidth=3)

axes[0].set_title('F Alto\n(Between >> Within)', fontsize=11, fontweight='bold', color='#1B5E20')
axes[0].set_xticks([1, 2, 3])
axes[0].set_xticklabels(['Grupo 1', 'Grupo 2', 'Grupo 3'])
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)
axes[0].set_ylabel('Valor', fontsize=11, fontweight='bold')

g1b = np.random.normal(20, 8, 15)
g2b = np.random.normal(21, 8, 15)
g3b = np.random.normal(22, 8, 15)

for i, (g, cor) in enumerate([(g1b, '#2135A6'), (g2b, '#586BA6'), (g3b, '#27368C')]):
    jitter = np.random.uniform(-0.15, 0.15, len(g))
    axes[1].scatter([i+1+j for j in jitter], g, color=cor, alpha=0.7, s=40, edgecolors='white')
    axes[1].plot([i+0.7, i+1.3], [np.mean(g), np.mean(g)], color=cor, linewidth=3)

axes[1].set_title('F Baixo\n(Between ~ Within)', fontsize=11, fontweight='bold', color='#C62828')
axes[1].set_xticks([1, 2, 3])
axes[1].set_xticklabels(['Grupo 1', 'Grupo 2', 'Grupo 3'])
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

fig.suptitle('Logica da ANOVA: Variancia Entre vs Dentro dos Grupos', fontsize=13, fontweight='bold', color=AZUL, y=1.02)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_between_within.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_between_within.png')

# --- Fig 3: Exemplo prático - perda de solo por cobertura (boxplot 3 grupos) ---
fig, ax = plt.subplots(figsize=(7, 4.5))
np.random.seed(7)
sem_cob = np.array([18.5, 22.1, 19.8, 25.3, 20.7, 23.4, 21.0])
parc_cob = np.array([12.3, 14.5, 11.2, 13.8, 15.1, 12.7, 13.0])
densa_cob = np.array([5.8, 7.2, 4.9, 6.5, 8.1, 5.3, 6.0])

bp = ax.boxplot([sem_cob, parc_cob, densa_cob],
                tick_labels=['Sem\ncobertura', 'Cobertura\nparcial', 'Cobertura\ndensa'],
                patch_artist=True, widths=0.5,
                medianprops=dict(color='white', linewidth=2),
                whiskerprops=dict(color=CONTRASTE),
                capprops=dict(color=CONTRASTE))

cores = ['#E74C3C', '#F39C12', '#2ECC71']
for box, cor in zip(bp['boxes'], cores):
    box.set_facecolor(cor)
    box.set_alpha(0.8)

for i, (data, xpos) in enumerate([(sem_cob, 1), (parc_cob, 2), (densa_cob, 3)]):
    jitter = np.random.uniform(-0.08, 0.08, len(data))
    ax.scatter([xpos + j for j in jitter], data, color='white', edgecolors=CONTRASTE, s=35, zorder=5, linewidth=1)

ax.set_ylabel('Perda de solo (t/ha)', fontsize=12, fontweight='bold')
ax.set_title('ANOVA Uma Via — Perda de Solo\npor Tipo de Cobertura Vegetal', fontsize=12, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for i, (d, cor) in enumerate([(sem_cob, '#E74C3C'), (parc_cob, '#F39C12'), (densa_cob, '#2ECC71')]):
    ax.text(i+1, max(d)+2, f'M={np.mean(d):.1f}', ha='center', fontsize=9, fontweight='bold', color=cor)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_anova_boxplot.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_anova_boxplot.png')

# --- Fig 4: Post-hoc visual (quais grupos diferem) ---
fig, ax = plt.subplots(figsize=(7, 4))
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)

positions = [(2, 3), (5, 3), (8, 3)]
labels = ['Sem\ncobertura', 'Cobertura\nparcial', 'Cobertura\ndensa']
colors = ['#E74C3C', '#F39C12', '#2ECC71']
medias = ['M=21,5', 'M=13,2', 'M=6,3']

for (x, y), lbl, cor, med in zip(positions, labels, colors, medias):
    circle = Circle((x, y), 1.1, facecolor=cor, edgecolor=CONTRASTE, linewidth=2, alpha=0.8)
    ax.add_patch(circle)
    ax.text(x, y+0.2, lbl, ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    ax.text(x, y-0.5, med, ha='center', va='center', fontsize=9, color='white')

ax.annotate('', xy=(3.2, 4.0), xytext=(1.8, 4.0), arrowprops=dict(arrowstyle='<->', color=AZUL, lw=2.5))
ax.text(2.5, 4.5, 'p < 0,05 *', ha='center', fontsize=10, fontweight='bold', color=AZUL)

ax.annotate('', xy=(6.8, 4.0), xytext=(5.2, 4.0), arrowprops=dict(arrowstyle='<->', color=AZUL, lw=2.5))
ax.text(6.0, 4.5, 'p < 0,05 *', ha='center', fontsize=10, fontweight='bold', color=AZUL)

ax.annotate('', xy=(7.5, 1.5), xytext=(2.5, 1.5), arrowprops=dict(arrowstyle='<->', color='#C62828', lw=2.5))
ax.text(5.0, 0.8, 'p < 0,001 ***', ha='center', fontsize=10, fontweight='bold', color='#C62828')

ax.set_title('Post-hoc: Quais Grupos Diferem Entre Si?', fontsize=13, fontweight='bold', color=AZUL, pad=15)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_posthoc_visual.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_posthoc_visual.png')

# --- Fig 5: Distribuição F ---
fig, ax = plt.subplots(figsize=(7, 3.5))
x = np.linspace(0.01, 8, 500)
y = f_dist.pdf(x, 2, 6)
f_crit = f_dist.ppf(0.95, 2, 6)

ax.plot(x, y, color=AZUL, linewidth=2.5)
ax.fill_between(x, y, where=(x <= f_crit), alpha=0.15, color=AZUL, label='Regiao de nao rejeicao')
ax.fill_between(x, y, where=(x >= f_crit), alpha=0.4, color='#E74C3C', label=f'Regiao critica (F > {f_crit:.2f})')
ax.axvline(f_crit, color='#E74C3C', linestyle='--', linewidth=2)
ax.axvline(3.97, color='#2ECC71', linestyle='-', linewidth=2.5, label='F calculado = 3,97')

ax.set_xlabel('Estatistica F', fontsize=11, fontweight='bold')
ax.set_ylabel('Densidade', fontsize=11)
ax.set_title('Distribuicao F (gl1=2, gl2=6)', fontsize=12, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=9, loc='upper right')
ax.set_xlim(0, 8)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_distribuicao_f.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_distribuicao_f.png')

# --- Fig 6: Tamanho de efeito omega² ---
fig, ax = plt.subplots(figsize=(8, 2.5))
ax.axis('off')

faixas = [
    (0, 0.01, 'Nenhum\n(< 0,01)', '#E8EAF6'),
    (0.01, 0.06, 'Pequeno\n(0,01-0,06)', '#C5CAE9'),
    (0.06, 0.14, 'Medio\n(0,06-0,14)', '#9FA8DA'),
    (0.14, 0.30, 'Grande\n(>= 0,14)', '#5C6BC0'),
]

total_w = 8
for x0_frac, x1_frac, lbl, cor in faixas:
    x0 = 1 + x0_frac / 0.30 * total_w
    x1 = 1 + x1_frac / 0.30 * total_w
    rect = FancyBboxPatch((x0, 0.8), x1 - x0, 1.2, boxstyle="round,pad=0.05", facecolor=cor, edgecolor=AZUL, linewidth=1.5)
    ax.add_patch(rect)
    text_color = 'white' if cor == '#5C6BC0' else CONTRASTE
    ax.text((x0 + x1) / 2, 1.4, lbl, ha='center', va='center', fontsize=9, fontweight='bold', color=text_color)

ax.set_xlim(0.5, 10)
ax.set_ylim(0, 3)
ax.set_title('Omega quadrado (Field, 2013) — Tamanho de Efeito ANOVA', fontsize=12, fontweight='bold', color=AZUL, pad=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_omega2.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_omega2.png')

print('\n=== Todas as figuras da Aula 5 geradas! ===')
