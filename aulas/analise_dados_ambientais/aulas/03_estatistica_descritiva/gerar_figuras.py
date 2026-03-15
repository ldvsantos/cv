"""Gera figuras didáticas para Aula 2 - Estatística Descritiva."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

AZUL = '#2135A6'
AZUL_APOIO = '#586BA6'
CONTRASTE = '#0D0D0D'
OUT = os.path.dirname(os.path.abspath(__file__))

# --- Fig 1: Tendência central (dotplot com média, mediana, moda) ---
fig, ax = plt.subplots(figsize=(8, 3.5))
np.random.seed(42)
dados = np.array([3, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9, 12])
for v in np.unique(dados):
    count = np.sum(dados == v)
    ax.scatter([v]*count, np.arange(1, count+1)*0.3, color=AZUL_APOIO, s=100, zorder=5, edgecolors='white', linewidth=1.5)
media = np.mean(dados)
mediana = np.median(dados)
from scipy.stats import mode as sp_mode
moda_result = sp_mode(dados, keepdims=True)
moda = moda_result.mode[0]
ax.axvline(media, color='#E74C3C', linewidth=2, linestyle='--', label=f'Media = {media:.1f}')
ax.axvline(mediana, color='#2ECC71', linewidth=2, linestyle='-', label=f'Mediana = {mediana:.1f}')
ax.axvline(moda, color='#F39C12', linewidth=2, linestyle=':', label=f'Moda = {moda}')
ax.set_xlabel('Valor', fontsize=12, fontweight='bold')
ax.set_title('Medidas de Tendencia Central', fontsize=13, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=9)
ax.set_yticks([])
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_tendencia_central.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_tendencia_central.png')

# --- Fig 2: Dispersão (desvios em torno da média) ---
fig, ax = plt.subplots(figsize=(8, 4))
np.random.seed(7)
dados = np.array([12, 14, 15, 16, 17, 18, 19, 20, 22, 25])
media = np.mean(dados)
ax.scatter(range(1, len(dados)+1), dados, color=AZUL_APOIO, s=80, zorder=5, edgecolors='white', linewidth=1.5)
ax.axhline(media, color='#E74C3C', linewidth=2, linestyle='--', label=f'Media = {media:.1f}')
for i, d in enumerate(dados):
    cor = '#2ECC71' if d >= media else '#E74C3C'
    ax.plot([i+1, i+1], [media, d], color=cor, linewidth=1.5, alpha=0.7)
ax.set_xlabel('Observacao', fontsize=12, fontweight='bold')
ax.set_ylabel('Valor', fontsize=12, fontweight='bold')
ax.set_title('Desvios em Torno da Media', fontsize=13, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_dispersao_desvios.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_dispersao_desvios.png')

# --- Fig 3: Curva normal / escore Z ---
fig, ax = plt.subplots(figsize=(8, 4))
x = np.linspace(-4, 4, 500)
y = (1/np.sqrt(2*np.pi)) * np.exp(-x**2/2)
ax.plot(x, y, color=AZUL, linewidth=2.5)
ax.fill_between(x, y, where=(x >= -1) & (x <= 1), alpha=0.3, color=AZUL_APOIO, label='68,3% (+-1 DP)')
ax.fill_between(x, y, where=((x >= -2) & (x < -1)) | ((x > 1) & (x <= 2)), alpha=0.15, color='#27368C', label='95,4% (+-2 DP)')
ax.set_title('Distribuicao Normal e Escores Z', fontsize=13, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('Escore Z (desvios-padrao)', fontsize=11)
ax.set_yticks([])
ax.legend(fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_curva_normal_z.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_curva_normal_z.png')

# --- Fig 4: Intervalo de confiança ---
fig, ax = plt.subplots(figsize=(7, 4))
np.random.seed(42)
medias = [np.mean(np.random.normal(50, 10, 30)) for _ in range(20)]
erros = [1.96 * 10 / np.sqrt(30)] * 20
for i, (m, e) in enumerate(zip(medias, erros)):
    cor = '#2ECC71' if (50 - e <= m <= 50 + e) else '#E74C3C'
    ax.errorbar(m, i, xerr=e, fmt='o', color=cor, capsize=4, markersize=5)
ax.axvline(50, color=AZUL, linewidth=2, linestyle='--', label='Media pop. = 50')
ax.set_xlabel('Valor', fontsize=12, fontweight='bold')
ax.set_ylabel('Amostra', fontsize=12, fontweight='bold')
ax.set_title('Intervalo de Confianca (95%)', fontsize=13, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_intervalo_confianca.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_intervalo_confianca.png')

print('\n=== Todas as figuras da Aula 2 geradas! ===')
