"""Gera figuras didáticas para Aula 6 - ANOVA Fatorial."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
import os

AZUL = '#2135A6'
AZUL_APOIO = '#586BA6'
AZUL_PROF = '#27368C'
CONTRASTE = '#0D0D0D'
OUT = os.path.dirname(os.path.abspath(__file__))

# --- Fig 1: Conceito ANOVA Fatorial (Uma Via vs Fatorial) ---
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# ANOVA Uma Via
np.random.seed(42)
g1 = np.random.normal(20, 4, 15)
g2 = np.random.normal(25, 4, 15)
g3 = np.random.normal(30, 4, 15)
bp1 = axes[0].boxplot([g1, g2, g3], patch_artist=True, labels=['Sem cob.', 'Parcial', 'Densa'], widths=0.5)
cores = ['#E74C3C', '#F39C12', '#2ECC71']
for b, c in zip(bp1['boxes'], cores):
    b.set_facecolor(c)
    b.set_alpha(0.7)
axes[0].set_title('ANOVA Uma Via\n(1 Fator: Cobertura)', fontsize=11, fontweight='bold', color=AZUL)
axes[0].set_ylabel('Perda de solo (t/ha)', fontsize=10, fontweight='bold')
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)

# ANOVA Fatorial
x = np.array([1, 2, 3])
taboa = np.array([4.2, 6.1, 7.8])
ouricuri = np.array([3.8, 8.5, 10.2])
axes[1].plot(x, taboa, 'o-', color=AZUL, linewidth=2.5, markersize=10, label='Taboa')
axes[1].plot(x, ouricuri, 's--', color='#E74C3C', linewidth=2.5, markersize=10, label='Ouricuri')
axes[1].set_xticks(x)
axes[1].set_xticklabels(['Sem\nresina', '1x\nresina', '2x\nresina'], fontsize=9)
axes[1].set_title('ANOVA Fatorial\n(2 Fatores: Fibra x Resina)', fontsize=11, fontweight='bold', color=AZUL)
axes[1].set_ylabel('Resistencia (kN/m)', fontsize=10, fontweight='bold')
axes[1].legend(fontsize=9)
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_anova_fatorial_conceito.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_anova_fatorial_conceito.png')

# --- Fig 2: Estrutura fatorial (grid de células) ---
fig, ax = plt.subplots(figsize=(8, 4))
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)

# Headers
ax.text(5.5, 5.5, 'Fator B: Dosagem de Resina', ha='center', fontsize=13, fontweight='bold', color=AZUL)
for j, lbl in enumerate(['Sem Resina', '1x Resina', '2x Resina']):
    ax.text(3 + j * 2.3, 4.8, lbl, ha='center', fontsize=10, fontweight='bold', color=AZUL_APOIO)

ax.text(0.8, 3.2, 'Fator A:\nFibra', ha='center', va='center', fontsize=12, fontweight='bold', color=AZUL, rotation=0)

fibras = ['Taboa', 'Ouricuri']
cores_celula = ['#C5CEE8', '#9FA8DA']
for i, (fibra, cor) in enumerate(zip(fibras, cores_celula)):
    ax.text(1.8, 3.8 - i * 1.8, fibra, ha='center', va='center', fontsize=10, fontweight='bold', color=CONTRASTE)
    for j in range(3):
        rect = FancyBboxPatch((2.5 + j * 2.3, 3.2 - i * 1.8), 1.8, 1.2,
                              boxstyle="round,pad=0.1", facecolor=cor, edgecolor=AZUL, linewidth=1.5, alpha=0.8)
        ax.add_patch(rect)
        celula_num = i * 3 + j + 1
        ax.text(3.4 + j * 2.3, 3.8 - i * 1.8, f'Celula {celula_num}\nn = 5',
                ha='center', va='center', fontsize=9, fontweight='bold', color=CONTRASTE)

ax.text(5.5, 0.5, '2 x 3 = 6 celulas   |   N total = 30', ha='center', fontsize=11, fontweight='bold', color=AZUL_PROF)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_estrutura_fatorial.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_estrutura_fatorial.png')

# --- Fig 3: Interação ausente (linhas paralelas) ---
fig, ax = plt.subplots(figsize=(6, 4))
x = np.array([1, 2, 3])
taboa = np.array([4.0, 6.0, 8.0])
ouricuri = np.array([6.0, 8.0, 10.0])

ax.plot(x, taboa, 'o-', color=AZUL, linewidth=2.5, markersize=10, label='Taboa')
ax.plot(x, ouricuri, 's-', color='#E74C3C', linewidth=2.5, markersize=10, label='Ouricuri')
ax.set_xticks(x)
ax.set_xticklabels(['Sem resina', '1x resina', '2x resina'], fontsize=10)
ax.set_ylabel('Resistencia (kN/m)', fontsize=11, fontweight='bold')
ax.set_title('Sem Interacao\n(linhas paralelas)', fontsize=12, fontweight='bold', color='#1B5E20')
ax.legend(fontsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_interacao_ausente.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_interacao_ausente.png')

# --- Fig 4: Interação presente (linhas cruzam) ---
fig, ax = plt.subplots(figsize=(6, 4))
x = np.array([1, 2, 3])
taboa = np.array([4.2, 6.1, 7.8])
ouricuri = np.array([3.8, 8.5, 10.2])

ax.plot(x, taboa, 'o-', color=AZUL, linewidth=2.5, markersize=10, label='Taboa')
ax.plot(x, ouricuri, 's-', color='#E74C3C', linewidth=2.5, markersize=10, label='Ouricuri')
ax.set_xticks(x)
ax.set_xticklabels(['Sem resina', '1x resina', '2x resina'], fontsize=10)
ax.set_ylabel('Resistencia (kN/m)', fontsize=11, fontweight='bold')
ax.set_title('Com Interacao\n(linhas divergem/cruzam)', fontsize=12, fontweight='bold', color='#C62828')
ax.legend(fontsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Anotação
ax.annotate('Ouricuri ganha\nmais com resina', xy=(2.5, 9.3), fontsize=9, fontweight='bold',
            color='#C62828', ha='center',
            arrowprops=dict(arrowstyle='->', color='#C62828', lw=1.5),
            xytext=(1.5, 10.5))

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_interacao_presente.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_interacao_presente.png')

# --- Fig 5: Exemplo fatorial boxplot (2x3) ---
fig, ax = plt.subplots(figsize=(8, 4.5))
np.random.seed(7)
dados = {
    'Taboa\nSem': np.random.normal(4.2, 0.8, 5),
    'Taboa\n1x': np.random.normal(6.1, 0.9, 5),
    'Taboa\n2x': np.random.normal(7.8, 1.1, 5),
    'Ouricuri\nSem': np.random.normal(3.8, 0.7, 5),
    'Ouricuri\n1x': np.random.normal(8.5, 1.2, 5),
    'Ouricuri\n2x': np.random.normal(10.2, 1.4, 5),
}

bp = ax.boxplot(list(dados.values()), patch_artist=True, labels=list(dados.keys()), widths=0.5,
                medianprops=dict(color='white', linewidth=2))
cores = [AZUL_APOIO, AZUL_APOIO, AZUL_APOIO, '#C0392B', '#C0392B', '#C0392B']
for b, c in zip(bp['boxes'], cores):
    b.set_facecolor(c)
    b.set_alpha(0.75)

ax.set_ylabel('Resistencia a tracao (kN/m)', fontsize=11, fontweight='bold')
ax.set_title('ANOVA Fatorial 2x3 — Geotexteis Naturais', fontsize=12, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Legenda manual
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=AZUL_APOIO, alpha=0.75, label='Taboa'),
                   Patch(facecolor='#C0392B', alpha=0.75, label='Ouricuri')]
ax.legend(handles=legend_elements, fontsize=10)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_exemplo_fatorial.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_exemplo_fatorial.png')

# --- Fig 6: Eta parcial ao quadrado ---
fig, ax = plt.subplots(figsize=(7, 4))
fontes = ['Fibra (A)', 'Resina (B)', 'A x B']
eta_vals = [0.34, 0.79, 0.26]
cores = [AZUL_APOIO, AZUL, AZUL_PROF]

bars = ax.barh(fontes, eta_vals, color=cores, edgecolor='white', height=0.5, alpha=0.85)
for bar, val in zip(bars, eta_vals):
    ax.text(val + 0.02, bar.get_y() + bar.get_height()/2, f'{val:.2f}', va='center', fontsize=12, fontweight='bold', color=CONTRASTE)

ax.set_xlabel('Eta parcial ao quadrado (η²p)', fontsize=12, fontweight='bold')
ax.set_title('Tamanho de Efeito — ANOVA Fatorial', fontsize=13, fontweight='bold', color=AZUL)
ax.axvline(0.14, color='#E74C3C', linestyle='--', linewidth=1.5, label='Limiar "grande" (0,14)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=9)
ax.set_xlim(0, 1.0)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_eta_parcial.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_eta_parcial.png')

print('\n=== Todas as figuras da ANOVA Fatorial geradas! ===')
