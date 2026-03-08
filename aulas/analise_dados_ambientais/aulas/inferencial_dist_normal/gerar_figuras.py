"""Gera figuras didáticas para Aula 3 - Estatística Inferencial e Distribuição Normal."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skewnorm, norm
import os

AZUL = '#2135A6'
AZUL_APOIO = '#586BA6'
CONTRASTE = '#0D0D0D'
OUT = os.path.dirname(os.path.abspath(__file__))

# --- Fig 1: Erros Tipo I e Tipo II ---
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
x = np.linspace(-4, 4, 500)
y = norm.pdf(x, 0, 1)

# Tipo I
axes[0].plot(x, y, color=AZUL, linewidth=2.5)
axes[0].fill_between(x, y, where=(x >= 1.96), alpha=0.4, color='#E74C3C', label='Erro Tipo I (alfa)')
axes[0].fill_between(x, y, where=(x <= -1.96), alpha=0.4, color='#E74C3C')
axes[0].set_title('Erro Tipo I (Falso Positivo)', fontsize=11, fontweight='bold', color='#C62828')
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)
axes[0].legend(fontsize=9)
axes[0].set_yticks([])

# Tipo II
y2 = norm.pdf(x, 2, 1)
axes[1].plot(x, y, color=AZUL, linewidth=2.5, label='H0 verdadeira')
axes[1].plot(x, y2, color='#2ECC71', linewidth=2.5, label='H1 verdadeira')
axes[1].fill_between(x, y2, where=(x <= 1.96), alpha=0.3, color='#F39C12', label='Erro Tipo II (beta)')
axes[1].set_title('Erro Tipo II (Falso Negativo)', fontsize=11, fontweight='bold', color='#E65100')
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)
axes[1].legend(fontsize=8)
axes[1].set_yticks([])

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_erros_tipo.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_erros_tipo.png')

# --- Fig 2: Influência de N no valor-p ---
fig, ax = plt.subplots(figsize=(7, 4))
np.random.seed(42)
ns = [5, 10, 20, 30, 50, 100, 200, 500]
from scipy.stats import ttest_ind
p_vals = []
for n in ns:
    ps = []
    for _ in range(500):
        g1 = np.random.normal(50, 10, n)
        g2 = np.random.normal(52, 10, n)
        _, p = ttest_ind(g1, g2)
        ps.append(p)
    p_vals.append(np.mean(ps))

ax.plot(ns, p_vals, 'o-', color=AZUL, linewidth=2, markersize=8)
ax.axhline(0.05, color='#E74C3C', linestyle='--', linewidth=2, label='p = 0,05')
ax.set_xlabel('Tamanho da amostra (N)', fontsize=12, fontweight='bold')
ax.set_ylabel('p-valor medio', fontsize=12, fontweight='bold')
ax.set_title('Influencia do Tamanho Amostral no p-valor', fontsize=13, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_influencia_n_p.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_influencia_n_p.png')

# --- Fig 3: Curva normal - exemplo vetiver ---
fig, ax = plt.subplots(figsize=(7, 4))
x = np.linspace(0, 60, 500)
mu, sigma = 30, 8
y = norm.pdf(x, mu, sigma)
ax.plot(x, y, color=AZUL, linewidth=2.5)
ax.fill_between(x, y, where=(x >= mu-sigma) & (x <= mu+sigma), alpha=0.3, color=AZUL_APOIO)
ax.fill_between(x, y, where=(x >= mu-2*sigma) & (x <= mu+2*sigma) & ~((x >= mu-sigma) & (x <= mu+sigma)), alpha=0.15, color='#27368C')
ax.axvline(mu, color='#E74C3C', linestyle='--', linewidth=2, label=f'Media = {mu} cm')
ax.set_xlabel('Comprimento radicular (cm)', fontsize=12, fontweight='bold')
ax.set_title('Curva Normal — Comprimento Radicular do Vetiver', fontsize=12, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=10)
ax.set_yticks([])
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_curva_normal_vetiver.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_curva_normal_vetiver.png')

# --- Fig 4: Assimetria ---
fig, axes = plt.subplots(1, 3, figsize=(10, 3.5))
x = np.linspace(-5, 10, 500)

axes[0].plot(x, skewnorm.pdf(x, -5, 1, 2), color=AZUL, linewidth=2.5)
axes[0].set_title('Assimetria Negativa', fontsize=11, fontweight='bold', color=AZUL)
axes[0].set_yticks([])
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)

axes[1].plot(x, norm.pdf(x, 2, 1.5), color='#2ECC71', linewidth=2.5)
axes[1].set_title('Simetrica (Normal)', fontsize=11, fontweight='bold', color='#1B5E20')
axes[1].set_yticks([])
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

axes[2].plot(x, skewnorm.pdf(x, 5, 1, 2), color='#E74C3C', linewidth=2.5)
axes[2].set_title('Assimetria Positiva', fontsize=11, fontweight='bold', color='#C62828')
axes[2].set_yticks([])
axes[2].spines['top'].set_visible(False)
axes[2].spines['right'].set_visible(False)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_assimetria.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_assimetria.png')

# --- Fig 5: Curtose ---
fig, ax = plt.subplots(figsize=(7, 4))
x = np.linspace(-6, 6, 500)
from scipy.stats import t as t_dist

ax.plot(x, norm.pdf(x), color=AZUL, linewidth=2.5, label='Mesocurtica (Normal)')
ax.plot(x, t_dist.pdf(x, 3), color='#E74C3C', linewidth=2, linestyle='--', label='Leptocurtica (caudas pesadas)')
ax.plot(x, norm.pdf(x, 0, 1.8)*1.8, color='#2ECC71', linewidth=2, linestyle=':', label='Platicurtica (achatada)')
ax.set_title('Tipos de Curtose', fontsize=13, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=9)
ax.set_yticks([])
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_curtose.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_curtose.png')

# --- Fig 6: Relação N x tamanho de efeito ---
fig, ax = plt.subplots(figsize=(7, 4))
ns = np.arange(10, 210, 5)
effects = {'Pequeno (d=0,2)': 0.2, 'Medio (d=0,5)': 0.5, 'Grande (d=0,8)': 0.8}
colors = ['#2ECC71', '#F39C12', '#E74C3C']
for (lbl, d), cor in zip(effects.items(), colors):
    from scipy.stats import norm as norm_dist
    power = []
    for n in ns:
        se = np.sqrt(2/n)
        z_crit = 1.96
        z_beta = d/se - z_crit
        pw = norm_dist.cdf(z_beta)
        power.append(pw)
    ax.plot(ns, power, color=cor, linewidth=2, label=lbl)

ax.axhline(0.8, color=AZUL, linestyle='--', linewidth=1.5, alpha=0.7, label='Poder = 80%')
ax.set_xlabel('Tamanho amostral (N por grupo)', fontsize=12, fontweight='bold')
ax.set_ylabel('Poder estatistico', fontsize=12, fontweight='bold')
ax.set_title('Relacao entre N e Poder por Tamanho de Efeito', fontsize=12, fontweight='bold', color=AZUL)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_relacao_n_efeito.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_relacao_n_efeito.png')

# --- Fig 7: Testes de normalidade visual ---
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
np.random.seed(42)
dados_norm = np.random.normal(50, 10, 100)
dados_nnorm = np.concatenate([np.random.normal(30, 5, 50), np.random.normal(70, 5, 50)])

axes[0].hist(dados_norm, bins=15, color=AZUL_APOIO, edgecolor='white', alpha=0.85, density=True)
x_fit = np.linspace(20, 80, 100)
axes[0].plot(x_fit, norm.pdf(x_fit, np.mean(dados_norm), np.std(dados_norm)), color='#E74C3C', linewidth=2)
axes[0].set_title('Dados Normais\n(Shapiro-Wilk p > 0,05)', fontsize=11, fontweight='bold', color='#1B5E20')
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)

axes[1].hist(dados_nnorm, bins=15, color='#F39C12', edgecolor='white', alpha=0.85, density=True)
x_fit2 = np.linspace(10, 90, 100)
axes[1].plot(x_fit2, norm.pdf(x_fit2, np.mean(dados_nnorm), np.std(dados_nnorm)), color='#E74C3C', linewidth=2)
axes[1].set_title('Dados Nao Normais\n(Shapiro-Wilk p < 0,05)', fontsize=11, fontweight='bold', color='#C62828')
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_testes_normalidade.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_testes_normalidade.png')

print('\n=== Todas as figuras da Aula 3 geradas! ===')
