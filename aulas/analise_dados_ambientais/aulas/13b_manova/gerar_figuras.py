"""Gera figuras para a aula MANOVA."""
import os
import numpy as np
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

OUT = os.path.dirname(os.path.abspath(__file__))

AZUL = "#2135A6"
AZUL_PROF = "#27368C"
AZUL_APOIO = "#586BA6"
FUNDO = "#F2F2F2"
PRETO = "#0D0D0D"
CORES = ["#2135A6", "#27368C", "#586BA6", "#7B8EC9", "#C5CEE8"]


plt.rcParams.update({
    "figure.facecolor": FUNDO,
    "axes.facecolor": FUNDO,
    "axes.edgecolor": PRETO,
    "axes.labelcolor": PRETO,
    "xtick.color": PRETO,
    "ytick.color": PRETO,
    "text.color": PRETO,
    "font.family": "sans-serif",
    "font.size": 12,
})


def fig_manova_conceito():
    """ANOVA vs MANOVA: comparacao conceitual."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

    np.random.seed(42)

    # --- ANOVA: 1 VD ---
    g1 = np.random.normal(5, 1, 20)
    g2 = np.random.normal(6.5, 1, 20)
    g3 = np.random.normal(5.8, 1, 20)
    for g, label, cor in zip([g1, g2, g3], ["Taboa", "Ouricuri", "Junco"],
                             [AZUL, AZUL_PROF, AZUL_APOIO]):
        axes[0].hist(g, bins=8, alpha=0.5, color=cor, label=label, edgecolor="white")
    axes[0].set_xlabel("Resistencia a tracao (kN/m)", fontsize=11)
    axes[0].set_ylabel("Frequencia", fontsize=11)
    axes[0].set_title("ANOVA: 1 VD", fontsize=13, fontweight="bold")
    axes[0].legend(fontsize=9)
    axes[0].grid(axis="y", alpha=0.3)

    # --- MANOVA: 2 VDs ---
    cov = [[1, 0.5], [0.5, 1]]
    d1 = np.random.multivariate_normal([5, 4], cov, 25)
    d2 = np.random.multivariate_normal([7, 6], cov, 25)
    d3 = np.random.multivariate_normal([6, 7.5], cov, 25)
    for d, label, cor in zip([d1, d2, d3], ["Taboa", "Ouricuri", "Junco"],
                             [AZUL, AZUL_PROF, AZUL_APOIO]):
        axes[1].scatter(d[:, 0], d[:, 1], c=cor, s=40, alpha=0.7, label=label, edgecolors="white")
        # Centroide
        cx, cy = d.mean(axis=0)
        axes[1].plot(cx, cy, "X", color=cor, markersize=14, markeredgecolor="white", markeredgewidth=2)

    axes[1].set_xlabel("Resistencia a tracao", fontsize=11)
    axes[1].set_ylabel("Resistencia a puncao", fontsize=11)
    axes[1].set_title("MANOVA: 2 VDs simultaneas", fontsize=13, fontweight="bold")
    axes[1].legend(fontsize=9)
    axes[1].grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_manova_conceito.png"), dpi=180)
    plt.close(fig)
    print("  OK fig_manova_conceito.png")


def fig_combinacao_linear():
    """Mostra como projecao linear separa grupos melhor."""
    np.random.seed(10)
    cov = [[1, 0.6], [0.6, 1]]
    d1 = np.random.multivariate_normal([4, 5], cov, 30)
    d2 = np.random.multivariate_normal([5.5, 5.5], cov, 30)
    d3 = np.random.multivariate_normal([5, 7], cov, 30)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

    # Scatter 2D
    for d, label, cor in zip([d1, d2, d3], ["Taboa", "Ouricuri", "Junco"],
                             [AZUL, AZUL_PROF, AZUL_APOIO]):
        axes[0].scatter(d[:, 0], d[:, 1], c=cor, s=35, alpha=0.6, label=label, edgecolors="white")
    axes[0].set_xlabel("VD1: Tracao", fontsize=11)
    axes[0].set_ylabel("VD2: Puncao", fontsize=11)
    axes[0].set_title("Espaco original (2 VDs)", fontsize=13, fontweight="bold")
    axes[0].legend(fontsize=9)
    axes[0].grid(alpha=0.3)

    # Projecao na melhor direcao (simulada como combinacao linear)
    # Direcao discriminante aproximada
    w = np.array([0.5, 0.87])  # normalizado
    for d, label, cor in zip([d1, d2, d3], ["Taboa", "Ouricuri", "Junco"],
                             [AZUL, AZUL_PROF, AZUL_APOIO]):
        proj = d @ w
        axes[1].hist(proj, bins=10, alpha=0.5, color=cor, label=label, edgecolor="white")

    axes[1].set_xlabel("Combinacao linear (0,5 VD1 + 0,87 VD2)", fontsize=10)
    axes[1].set_ylabel("Frequencia", fontsize=11)
    axes[1].set_title("Projecao discriminante", fontsize=13, fontweight="bold")
    axes[1].legend(fontsize=9)
    axes[1].grid(axis="y", alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_combinacao_linear.png"), dpi=180)
    plt.close(fig)
    print("  OK fig_combinacao_linear.png")


def fig_pressupostos_manova():
    """Normalidade multivariada e homogeneidade de covariancias."""
    np.random.seed(55)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

    # Normalidade multivariada via QQ-plot de distancias de Mahalanobis
    cov = [[1, 0.4], [0.4, 1]]
    data = np.random.multivariate_normal([0, 0], cov, 50)
    mean = data.mean(axis=0)
    cov_inv = np.linalg.inv(np.cov(data.T))
    d2 = np.array([((x - mean) @ cov_inv @ (x - mean)) for x in data])
    d2_sorted = np.sort(d2)
    n = len(d2)
    # Chi-squared quantiles approximation (using inverse CDF via numpy percentile)
    expected = np.array([_chi2_ppf((i + 0.5) / n, 2) for i in range(n)])

    axes[0].scatter(expected, d2_sorted, c=AZUL, s=25, zorder=3)
    max_val = max(expected.max(), d2_sorted.max())
    axes[0].plot([0, max_val], [0, max_val], color="#D32F2F", linewidth=2, ls="--")
    axes[0].set_xlabel("Quantis chi-quadrado (gl=2)", fontsize=11)
    axes[0].set_ylabel("Distancias de Mahalanobis", fontsize=11)
    axes[0].set_title("Normalidade multivariada\n(QQ-plot Mahalanobis)", fontsize=12, fontweight="bold")
    axes[0].grid(alpha=0.3)

    # Homogeneidade de covariancias - elipses
    cov1 = [[1, 0.4], [0.4, 1]]
    cov2 = [[1.1, 0.35], [0.35, 0.9]]
    cov3 = [[0.9, 0.45], [0.45, 1.1]]
    means = [[3, 3], [6, 3], [4.5, 6]]
    for cov_m, m, label, cor in zip([cov1, cov2, cov3], means,
                                     ["Taboa", "Ouricuri", "Junco"],
                                     [AZUL, AZUL_PROF, AZUL_APOIO]):
        vals, vecs = np.linalg.eigh(cov_m)
        angle = np.degrees(np.arctan2(vecs[1, 1], vecs[0, 1]))
        w, h = 2 * 2 * np.sqrt(vals)
        ell = Ellipse(xy=m, width=w, height=h, angle=angle,
                      facecolor=cor, alpha=0.25, edgecolor=cor, linewidth=2)
        axes[1].add_patch(ell)
        axes[1].plot(m[0], m[1], "o", color=cor, markersize=10, label=label)

    axes[1].set_xlim(-1, 10)
    axes[1].set_ylim(-1, 10)
    axes[1].set_aspect("equal")
    axes[1].set_xlabel("VD1", fontsize=11)
    axes[1].set_ylabel("VD2", fontsize=11)
    axes[1].set_title("Homogeneidade de covariancias\n(elipses semelhantes)", fontsize=12, fontweight="bold")
    axes[1].legend(fontsize=9)
    axes[1].grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_pressupostos_manova.png"), dpi=180)
    plt.close(fig)
    print("  OK fig_pressupostos_manova.png")


def _chi2_ppf(p, k):
    """Approximate chi-squared inverse CDF (Wilson-Hilferty)."""
    if p <= 0:
        return 0.0
    if p >= 1:
        return k * 10.0
    z = _norm_ppf_simple(p)
    x = k * (1 - 2.0 / (9.0 * k) + z * math.sqrt(2.0 / (9.0 * k))) ** 3
    return max(x, 0.0)


def _norm_ppf_simple(p):
    """Inverse normal CDF (Abramowitz & Stegun rational approx)."""
    if p <= 0:
        return -6.0
    if p >= 1:
        return 6.0
    if p == 0.5:
        return 0.0
    if p > 0.5:
        return -_norm_ppf_simple(1 - p)
    t = math.sqrt(-2.0 * math.log(p))
    c0, c1, c2 = 2.515517, 0.802853, 0.010328
    d1, d2, d3 = 1.432788, 0.189269, 0.001308
    return -(t - (c0 + c1 * t + c2 * t ** 2) / (1 + d1 * t + d2 * t ** 2 + d3 * t ** 3))


def fig_exemplo_manova():
    """Grafico de barras agrupadas com 3 grupos e 3 VDs."""
    np.random.seed(99)
    grupos = ["Taboa", "Ouricuri", "Junco"]
    vds = ["Tracao\n(kN/m)", "Puncao\n(kN)", "Rigidez\n(kN/m)"]
    medias = np.array([
        [4.2, 3.8, 5.1],
        [5.5, 4.1, 4.8],
        [4.8, 5.2, 4.5],
    ])
    se = np.array([
        [0.4, 0.3, 0.5],
        [0.5, 0.4, 0.4],
        [0.3, 0.5, 0.3],
    ])

    x = np.arange(len(vds))
    width = 0.25

    fig, ax = plt.subplots(figsize=(9, 5))
    for i, (grupo, cor) in enumerate(zip(grupos, [AZUL, AZUL_PROF, AZUL_APOIO])):
        ax.bar(x + i * width, medias[i], width, yerr=se[i], color=cor,
               alpha=0.8, label=grupo, capsize=4, edgecolor="white")

    ax.set_xticks(x + width)
    ax.set_xticklabels(vds, fontsize=12)
    ax.set_ylabel("Valor medio", fontsize=12)
    ax.set_title("MANOVA: 3 VDs x 3 Grupos", fontsize=14, fontweight="bold")
    ax.legend(fontsize=11)
    ax.grid(axis="y", alpha=0.3)
    ax.set_ylim(0, 7)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_exemplo_manova.png"), dpi=180)
    plt.close(fig)
    print("  OK fig_exemplo_manova.png")


if __name__ == "__main__":
    print("Gerando figuras - MANOVA")
    fig_manova_conceito()
    fig_combinacao_linear()
    fig_pressupostos_manova()
    fig_exemplo_manova()
    print("Concluido!")
