"""Gera figuras didáticas para Aula 4 - Teste T de Student."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, t as t_dist
import os

AZUL = '#2135A6'
AZUL_APOIO = '#586BA6'
CONTRASTE = '#0D0D0D'
OUT = os.path.dirname(os.path.abspath(__file__))

# --- Fig 1: Tipos de Teste T ---
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# Amostra única
np.random.seed(42)
dados = np.random.normal(52, 8, 30)
axes[0].hist(dados, bins=10, color=AZUL_APOIO, edgecolor='white', alpha=0.8)
axes[0].axvline(50, color='#E74C3C', linewidth=2.5, linestyle='--', label='μ₀ = 50')
axes[0].axvline(np.mean(dados), color='#2ECC71', linewidth=2.5, label=f'x̄ = {np.mean(dados):.1f}')
axes[0].set_title('Amostra Unica', fontsize=12, fontweight='bold', color=AZUL)
axes[0].legend(fontsize=9)
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)

# Independente
g1 = np.random.normal(48, 7, 25)
g2 = np.random.normal(55, 7, 25)
bp = axes[1].boxplot([g1, g2], patch_artist=True, labels=['Grupo A', 'Grupo B'])
bp['boxes'][0].set_facecolor(AZUL_APOIO)
bp['boxes'][1].set_facecolor('#27368C')
for b in bp['boxes']:
    b.set_alpha(0.7)
axes[1].set_title('Independente', fontsize=12, fontweight='bold', color=AZUL)
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

# Pareado
antes = np.random.normal(45, 8, 15)
depois = antes + np.random.normal(5, 3, 15)
for i in range(len(antes)):
    axes[2].plot([1, 2], [antes[i], depois[i]], 'o-', color=AZUL_APOIO, alpha=0.5, markersize=5)
axes[2].set_xlim(0.5, 2.5)
axes[2].set_xticks([1, 2])
axes[2].set_xticklabels(['Antes', 'Depois'], fontsize=11, fontweight='bold')
axes[2].set_title('Pareado (Dependente)', fontsize=12, fontweight='bold', color=AZUL)
axes[2].spines['top'].set_visible(False)
axes[2].spines['right'].set_visible(False)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_tipos_teste_t.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_tipos_teste_t.png')

# --- Fig 2: Amostra única ---
fig, ax = plt.subplots(figsize=(7, 4))
x = np.linspace(-4, 4, 500)
y = t_dist.pdf(x, 29)
ax.plot(x, y, color=AZUL, linewidth=2.5)
t_crit = t_dist.ppf(0.975, 29)
ax.fill_between(x, y, where=(x >= t_crit), alpha=0.4, color='#E74C3C', label=f'Rejeicao (t > {t_crit:.2f})')
ax.fill_between(x, y, where=(x <= -t_crit), alpha=0.4, color='#E74C3C')
ax.axvline(1.8, color='#2ECC71', linewidth=2.5, linestyle='--', label='t observado = 1,80')
ax.set_title('Teste T — Amostra Unica (gl = 29)', fontsize=12, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=9)
ax.set_yticks([])
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_amostra_unica.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_amostra_unica.png')

# --- Fig 3: Independente boxplot ---
fig, ax = plt.subplots(figsize=(6, 5))
np.random.seed(10)
controle = np.random.normal(35, 6, 20)
tratamento = np.random.normal(42, 6, 20)
bp = ax.boxplot([controle, tratamento], patch_artist=True, labels=['Controle', 'Bioengenharia'], widths=0.5)
bp['boxes'][0].set_facecolor(AZUL_APOIO)
bp['boxes'][1].set_facecolor('#27368C')
for b in bp['boxes']:
    b.set_alpha(0.7)
    b.set_edgecolor(CONTRASTE)
ax.set_ylabel('Resistencia ao cisalhamento (kPa)', fontsize=11, fontweight='bold')
ax.set_title('Teste T Independente — Solo com Vegetacao', fontsize=12, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Significância
y_max = max(controle.max(), tratamento.max()) + 3
ax.plot([1, 1, 2, 2], [y_max, y_max+1, y_max+1, y_max], color=CONTRASTE, linewidth=1.5)
ax.text(1.5, y_max+1.5, '* p < 0,05', ha='center', fontsize=11, fontweight='bold', color='#E74C3C')
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_independente_boxplot.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_independente_boxplot.png')

# --- Fig 4: Pareado ---
fig, ax = plt.subplots(figsize=(7, 4.5))
np.random.seed(7)
antes = np.random.normal(40, 8, 12)
depois = antes + np.random.normal(8, 4, 12)

for i in range(len(antes)):
    cor = '#2ECC71' if depois[i] > antes[i] else '#E74C3C'
    ax.plot([1, 2], [antes[i], depois[i]], 'o-', color=cor, alpha=0.6, markersize=7, linewidth=1.5)

ax.set_xlim(0.5, 2.5)
ax.set_xticks([1, 2])
ax.set_xticklabels(['Antes\n(solo exposto)', 'Depois\n(com vetiver)'], fontsize=11, fontweight='bold')
ax.set_ylabel('Cobertura vegetal (%)', fontsize=11, fontweight='bold')
ax.set_title('Teste T Pareado — Antes vs Depois', fontsize=12, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_dependente_pareado.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_dependente_pareado.png')

# --- Fig 5: Homocedasticidade ---
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
np.random.seed(21)

# Homocedástico
g1 = np.random.normal(50, 8, 40)
g2 = np.random.normal(55, 8, 40)
bp1 = axes[0].boxplot([g1, g2], patch_artist=True, labels=['Grupo A', 'Grupo B'], widths=0.5)
bp1['boxes'][0].set_facecolor(AZUL_APOIO)
bp1['boxes'][1].set_facecolor('#27368C')
for b in bp1['boxes']:
    b.set_alpha(0.7)
axes[0].set_title('Homocedastico\n(variancias iguais)', fontsize=11, fontweight='bold', color='#1B5E20')
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)

# Heterocedástico
g3 = np.random.normal(50, 5, 40)
g4 = np.random.normal(55, 18, 40)
bp2 = axes[1].boxplot([g3, g4], patch_artist=True, labels=['Grupo A', 'Grupo B'], widths=0.5)
bp2['boxes'][0].set_facecolor('#2ECC71')
bp2['boxes'][1].set_facecolor('#E74C3C')
for b in bp2['boxes']:
    b.set_alpha(0.7)
axes[1].set_title('Heterocedastico\n(variancias diferentes)', fontsize=11, fontweight='bold', color='#C62828')
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

fig.suptitle('Pressuposto de Homocedasticidade (Teste de Levene)', fontsize=13, fontweight='bold', color=AZUL, y=1.02)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_homoscedasticidade.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_homoscedasticidade.png')

# --- Fig 6: d de Cohen ---
fig, ax = plt.subplots(figsize=(8, 4))
x = np.linspace(-4, 8, 500)

for d, cor, lbl in [(0.2, '#2ECC71', 'Pequeno (d=0,2)'), (0.5, '#F39C12', 'Medio (d=0,5)'), (0.8, '#E74C3C', 'Grande (d=0,8)')]:
    y1 = norm.pdf(x, 0, 1)
    y2 = norm.pdf(x, d*2.5, 1)
    ax.plot(x, y1, color=AZUL, linewidth=1, alpha=0.3)
    ax.plot(x, y2, color=cor, linewidth=2, label=lbl)

ax.set_title('Tamanho de Efeito — d de Cohen', fontsize=13, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=10)
ax.set_yticks([])
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_cohen_d.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_cohen_d.png')

print('\n=== Todas as figuras da Aula 4 geradas! ===')
