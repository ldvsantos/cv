"""Gera figuras didáticas para Aula 1 - Introdução e Etimologia Estatística."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

AZUL = '#2135A6'
AZUL_APOIO = '#586BA6'
CONTRASTE = '#0D0D0D'
OUT = os.path.dirname(os.path.abspath(__file__))

# --- Fig 1: População vs Amostra ---
fig, ax = plt.subplots(figsize=(7, 4))
np.random.seed(42)
pop_x = np.random.normal(0, 3, 300)
pop_y = np.random.normal(0, 3, 300)
ax.scatter(pop_x, pop_y, color=AZUL_APOIO, alpha=0.2, s=30, label='Populacao')
idx = np.random.choice(300, 30, replace=False)
ax.scatter(pop_x[idx], pop_y[idx], color='#E74C3C', s=60, edgecolors='white', linewidth=1.5, zorder=5, label='Amostra (n=30)')
ax.set_title('Populacao vs Amostra', fontsize=13, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=10)
ax.set_xlabel('Variavel X', fontsize=11)
ax.set_ylabel('Variavel Y', fontsize=11)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_populacao_amostra.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_populacao_amostra.png')

# --- Fig 2: Escalas de medida ---
fig, axes = plt.subplots(1, 4, figsize=(10, 3))
titles = ['Nominal', 'Ordinal', 'Intervalar', 'Razao']
examples = ['Cor do solo\n(Vermelho, Amarelo,\nBruno)', 'Grau de erosao\n(Baixo, Medio,\nAlto)', 'Temperatura\n(20C, 25C, 30C)', 'Peso\n(0 kg, 50 kg,\n100 kg)']
colors = ['#E8EAF6', '#C5CAE9', '#9FA8DA', '#5C6BC0']
for ax, t, ex, c in zip(axes, titles, examples, colors):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.add_patch(plt.Rectangle((0.05, 0.05), 0.9, 0.9, facecolor=c, edgecolor=AZUL, linewidth=2, transform=ax.transAxes))
    text_color = 'white' if c == '#5C6BC0' else CONTRASTE
    ax.text(0.5, 0.7, t, ha='center', va='center', fontsize=12, fontweight='bold', color=text_color, transform=ax.transAxes)
    ax.text(0.5, 0.3, ex, ha='center', va='center', fontsize=8, color=text_color, transform=ax.transAxes)
    ax.axis('off')
fig.suptitle('Escalas de Medida', fontsize=13, fontweight='bold', color=AZUL)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_escalas_medida.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_escalas_medida.png')

# --- Fig 3: Histograma de frequências ---
fig, ax = plt.subplots(figsize=(7, 4))
np.random.seed(10)
dados = np.random.normal(25, 5, 200)
ax.hist(dados, bins=15, color=AZUL_APOIO, edgecolor='white', alpha=0.85)
ax.axvline(np.mean(dados), color='#E74C3C', linewidth=2, linestyle='--', label=f'Media = {np.mean(dados):.1f}')
ax.set_xlabel('Temperatura (C)', fontsize=12, fontweight='bold')
ax.set_ylabel('Frequencia', fontsize=12, fontweight='bold')
ax.set_title('Histograma de Frequencias', fontsize=13, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_histograma_freq.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_histograma_freq.png')

print('\n=== Todas as figuras da Aula 1 geradas! ===')
