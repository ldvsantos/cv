"""Gera figuras didáticas para Aula ANCOVA."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

AZUL = '#2135A6'
AZUL_APOIO = '#586BA6'
AZUL_PROF = '#27368C'
CONTRASTE = '#0D0D0D'
OUT = os.path.dirname(os.path.abspath(__file__))

# --- Fig 1: Conceito ANCOVA (dispersão com fator + covariável) ---
fig, ax = plt.subplots(figsize=(7, 4.5))
np.random.seed(42)

# 3 grupos com covariável (precipitação) influenciando VD (erosão)
for lbl, cor, base_erosao, marker in [('Sem cobertura', '#E74C3C', 18, 'o'),
                                       ('Parcial', '#F39C12', 12, 's'),
                                       ('Densa', '#2ECC71', 6, '^')]:
    precip = np.random.uniform(40, 120, 10)
    erosao = base_erosao + 0.08 * precip + np.random.normal(0, 2, 10)
    ax.scatter(precip, erosao, color=cor, marker=marker, s=60, alpha=0.8, edgecolors='white', label=lbl)

ax.set_xlabel('Precipitacao acumulada (mm)', fontsize=11, fontweight='bold')
ax.set_ylabel('Perda de solo (t/ha)', fontsize=11, fontweight='bold')
ax.set_title('ANCOVA: Fator (Cobertura) + Covariavel (Precipitacao)', fontsize=12, fontweight='bold', color=AZUL)
ax.legend(fontsize=9, title='Cobertura', title_fontsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_ancova_conceito.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_ancova_conceito.png')

# --- Fig 2: Efeito da covariável (com vs sem controle) ---
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
np.random.seed(42)

# Sem controle (ANOVA simples) - boxplot
sem = np.random.normal(20, 6, 10)
parc = np.random.normal(14, 6, 10)
densa = np.random.normal(8, 6, 10)

bp = axes[0].boxplot([sem, parc, densa], patch_artist=True,
                      labels=['Sem', 'Parcial', 'Densa'], widths=0.5)
cores = ['#E74C3C', '#F39C12', '#2ECC71']
for b, c in zip(bp['boxes'], cores):
    b.set_facecolor(c)
    b.set_alpha(0.7)
axes[0].set_title('ANOVA (sem covariavel)\nF = 8,2; p = 0,002', fontsize=11, fontweight='bold', color=AZUL_APOIO)
axes[0].set_ylabel('Perda de solo (t/ha)', fontsize=10, fontweight='bold')
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)

# Com controle (ANCOVA) - boxplot com barras de erro menores
sem_adj = np.random.normal(19, 3, 10)
parc_adj = np.random.normal(13, 3, 10)
densa_adj = np.random.normal(7, 3, 10)

bp2 = axes[1].boxplot([sem_adj, parc_adj, densa_adj], patch_artist=True,
                       labels=['Sem', 'Parcial', 'Densa'], widths=0.5)
for b, c in zip(bp2['boxes'], cores):
    b.set_facecolor(c)
    b.set_alpha(0.7)
axes[1].set_title('ANCOVA (ajustada por chuva)\nF = 15,7; p < 0,001', fontsize=11, fontweight='bold', color=AZUL)
axes[1].set_ylabel('Perda de solo ajustada (t/ha)', fontsize=10, fontweight='bold')
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

fig.suptitle('Efeito de Controlar a Covariavel', fontsize=13, fontweight='bold', color=AZUL, y=1.02)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_covariavel_efeito.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_covariavel_efeito.png')

# --- Fig 3: Médias ajustadas vs brutas ---
fig, ax = plt.subplots(figsize=(7, 4))
grupos = ['Sem cobertura', 'Parcial', 'Densa']
medias_brutas = [20.5, 14.2, 8.1]
medias_ajust = [19.0, 13.5, 9.3]

x = np.arange(len(grupos))
w = 0.35
b1 = ax.bar(x - w/2, medias_brutas, w, color=AZUL_APOIO, alpha=0.7, label='Medias brutas', edgecolor='white')
b2 = ax.bar(x + w/2, medias_ajust, w, color=AZUL, alpha=0.85, label='Medias ajustadas', edgecolor='white')

for bar, val in zip(b1, medias_brutas):
    ax.text(bar.get_x() + bar.get_width()/2, val + 0.5, f'{val}', ha='center', fontsize=9, fontweight='bold', color=AZUL_APOIO)
for bar, val in zip(b2, medias_ajust):
    ax.text(bar.get_x() + bar.get_width()/2, val + 0.5, f'{val}', ha='center', fontsize=9, fontweight='bold', color=AZUL)

ax.set_xticks(x)
ax.set_xticklabels(grupos, fontsize=10, fontweight='bold')
ax.set_ylabel('Perda de solo (t/ha)', fontsize=11, fontweight='bold')
ax.set_title('Medias Brutas vs Ajustadas (EMMs)', fontsize=12, fontweight='bold', color=AZUL)
ax.legend(fontsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_medias_ajustadas.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_medias_ajustadas.png')

# --- Fig 4: Pressupostos ANCOVA (homogeneidade de inclinações) ---
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
np.random.seed(21)

# Retas paralelas (OK)
for lbl, cor, intercept in [('Sem', '#E74C3C', 15), ('Parcial', '#F39C12', 10), ('Densa', '#2ECC71', 5)]:
    x_cov = np.random.uniform(40, 120, 10)
    y_vd = intercept + 0.1 * x_cov + np.random.normal(0, 1.5, 10)
    axes[0].scatter(x_cov, y_vd, color=cor, alpha=0.7, s=40, edgecolors='white')
    # Reta de regressão
    z = np.polyfit(x_cov, y_vd, 1)
    x_fit = np.linspace(35, 125, 50)
    axes[0].plot(x_fit, z[0]*x_fit + z[1], color=cor, linewidth=2, alpha=0.8)

axes[0].set_title('Retas Paralelas (OK)\nHomogeneidade assumida', fontsize=11, fontweight='bold', color='#1B5E20')
axes[0].set_xlabel('Covariavel', fontsize=10, fontweight='bold')
axes[0].set_ylabel('VD', fontsize=10, fontweight='bold')
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)

# Retas não paralelas (VIOLAÇÃO)
slopes = [0.05, 0.12, 0.25]
for (lbl, cor, intercept), slope in zip([('Sem', '#E74C3C', 15), ('Parcial', '#F39C12', 10), ('Densa', '#2ECC71', 5)], slopes):
    x_cov = np.random.uniform(40, 120, 10)
    y_vd = intercept + slope * x_cov + np.random.normal(0, 1.5, 10)
    axes[1].scatter(x_cov, y_vd, color=cor, alpha=0.7, s=40, edgecolors='white')
    z = np.polyfit(x_cov, y_vd, 1)
    x_fit = np.linspace(35, 125, 50)
    axes[1].plot(x_fit, z[0]*x_fit + z[1], color=cor, linewidth=2, alpha=0.8)

axes[1].set_title('Retas Nao Paralelas (VIOLACAO)\nInteracao Fator x Covariavel', fontsize=11, fontweight='bold', color='#C62828')
axes[1].set_xlabel('Covariavel', fontsize=10, fontweight='bold')
axes[1].set_ylabel('VD', fontsize=10, fontweight='bold')
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_pressupostos_ancova.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_pressupostos_ancova.png')

# --- Fig 5: Exemplo ANCOVA (scatter com retas paralelas ajustadas) ---
fig, ax = plt.subplots(figsize=(7, 4.5))
np.random.seed(7)

for lbl, cor, intercept, marker in [('Sem cobertura', '#E74C3C', 16, 'o'),
                                     ('Parcial', '#F39C12', 10, 's'),
                                     ('Densa', '#2ECC71', 4, '^')]:
    precip = np.random.uniform(40, 120, 10)
    erosao = intercept + 0.08 * precip + np.random.normal(0, 1.5, 10)
    ax.scatter(precip, erosao, color=cor, marker=marker, s=60, alpha=0.8, edgecolors='white', label=lbl)
    x_fit = np.linspace(35, 125, 50)
    ax.plot(x_fit, intercept + 0.08 * x_fit, color=cor, linewidth=2, alpha=0.7)

# Linha vertical na média da covariável
ax.axvline(80, color=AZUL, linestyle=':', linewidth=2, alpha=0.5, label='Media da cov.')
ax.set_xlabel('Precipitacao (mm)', fontsize=11, fontweight='bold')
ax.set_ylabel('Perda de solo (t/ha)', fontsize=11, fontweight='bold')
ax.set_title('ANCOVA — Retas Paralelas Ajustadas', fontsize=12, fontweight='bold', color=AZUL)
ax.legend(fontsize=9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_exemplo_ancova.png'), dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('fig_exemplo_ancova.png')

print('\n=== Todas as figuras da ANCOVA geradas! ===')
