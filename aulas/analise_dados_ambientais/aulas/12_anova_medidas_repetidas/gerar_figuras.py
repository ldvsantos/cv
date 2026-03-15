"""Gera figuras para a aula de ANOVA de Medidas Repetidas."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import math


def _norm_ppf(p):
    """Inverse normal CDF (rational approximation, Abramowitz & Stegun)."""
    if p <= 0:
        return -6.0
    if p >= 1:
        return 6.0
    if p == 0.5:
        return 0.0
    if p > 0.5:
        return -_norm_ppf(1 - p)
    t = math.sqrt(-2.0 * math.log(p))
    c0, c1, c2 = 2.515517, 0.802853, 0.010328
    d1, d2, d3 = 1.432788, 0.189269, 0.001308
    return -(t - (c0 + c1 * t + c2 * t**2) / (1 + d1 * t + d2 * t**2 + d3 * t**3))

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


def fig_mr_conceito():
    """Spaghetti plot mostrando medidas repetidas em 3 condições."""
    np.random.seed(42)
    n_sujeitos = 8
    condicoes = ["Sem resina", "1× resina", "2× resina"]
    dados = np.array([
        [7, 6, 8],
        [4, 9, 9],
        [6, 5, 6],
        [8, 7, 7],
        [9, 4, 4],
        [8, 8, 5],
        [5, 10, 8],
        [6, 8, 7],
    ])

    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(condicoes))

    for i in range(n_sujeitos):
        ax.plot(x, dados[i], "o-", color=CORES[i % len(CORES)],
                alpha=0.6, linewidth=1.5, markersize=6,
                label=f"Amostra {i+1}")

    medias = dados.mean(axis=0)
    ax.plot(x, medias, "s-", color="#D32F2F", linewidth=3, markersize=10,
            label="Média", zorder=5)

    ax.set_xticks(x)
    ax.set_xticklabels(condicoes, fontsize=13)
    ax.set_ylabel("Resistência (kPa)", fontsize=13)
    ax.set_title("ANOVA-MR: mesmas amostras em 3 condições", fontsize=14, fontweight="bold")
    ax.legend(fontsize=9, ncol=3, loc="upper right")
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_mr_conceito.png"), dpi=180)
    plt.close(fig)
    print("  OK fig_mr_conceito.png")


def fig_esfericidade():
    """Ilustra esfericidade: variâncias das diferenças iguais vs. desiguais."""
    np.random.seed(7)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))

    # Caso 1: esfericidade assumida (variâncias semelhantes)
    diffs_ok = [
        np.random.normal(0, 1.0, 30),
        np.random.normal(0, 1.1, 30),
        np.random.normal(0, 0.9, 30),
    ]
    labels1 = ["T1−T2", "T1−T3", "T2−T3"]
    bp1 = axes[0].boxplot(diffs_ok, tick_labels=labels1, patch_artist=True,
                          medianprops=dict(color=PRETO, linewidth=2))
    for patch, c in zip(bp1["boxes"], [AZUL, AZUL_PROF, AZUL_APOIO]):
        patch.set_facecolor(c)
        patch.set_alpha(0.6)
    axes[0].set_title("Esfericidade assumida ✓", fontsize=13, fontweight="bold", color="#2E7D32")
    axes[0].set_ylabel("Diferenças", fontsize=12)
    axes[0].axhline(0, color="grey", ls="--", alpha=0.5)
    axes[0].grid(axis="y", alpha=0.3)

    # Caso 2: esfericidade violada (variâncias muito diferentes)
    diffs_bad = [
        np.random.normal(0, 0.5, 30),
        np.random.normal(0, 3.0, 30),
        np.random.normal(0, 1.2, 30),
    ]
    labels2 = ["T1−T2", "T1−T3", "T2−T3"]
    bp2 = axes[1].boxplot(diffs_bad, tick_labels=labels2, patch_artist=True,
                          medianprops=dict(color=PRETO, linewidth=2))
    for patch, c in zip(bp2["boxes"], [AZUL, AZUL_PROF, AZUL_APOIO]):
        patch.set_facecolor(c)
        patch.set_alpha(0.6)
    axes[1].set_title("Esfericidade violada ✗", fontsize=13, fontweight="bold", color="#D32F2F")
    axes[1].axhline(0, color="grey", ls="--", alpha=0.5)
    axes[1].grid(axis="y", alpha=0.3)

    fig.suptitle("Variância das diferenças entre pares de condições", fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_esfericidade.png"), dpi=180, bbox_inches="tight")
    plt.close(fig)
    print("  OK fig_esfericidade.png")


def fig_residuos_normalidade():
    """QQ-plot de resíduos para ANOVA-MR (sem scipy)."""
    np.random.seed(21)
    residuos = np.random.normal(0, 1, 50)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))

    # Histograma dos resíduos
    axes[0].hist(residuos, bins=12, color=AZUL, alpha=0.7, edgecolor="white")
    axes[0].axvline(0, color="#D32F2F", ls="--", linewidth=2)
    axes[0].set_xlabel("Resíduos", fontsize=12)
    axes[0].set_ylabel("Frequência", fontsize=12)
    axes[0].set_title("Distribuição dos Resíduos", fontsize=13, fontweight="bold")
    axes[0].grid(axis="y", alpha=0.3)

    # QQ-plot manual (sem scipy)
    n = len(residuos)
    sorted_res = np.sort(residuos)
    probs = (np.arange(1, n + 1) - 0.5) / n
    theoretical = np.array([_norm_ppf(p) for p in probs])

    axes[1].scatter(theoretical, sorted_res, c=AZUL, s=30, zorder=3)
    # Fit line
    slope = np.std(sorted_res)
    intercept = np.mean(sorted_res)
    line_x = np.array([theoretical.min(), theoretical.max()])
    line_y = intercept + slope * line_x
    axes[1].plot(line_x, line_y, color="#D32F2F", linewidth=2, zorder=2)
    axes[1].set_title("QQ-Plot dos Resíduos", fontsize=13, fontweight="bold")
    axes[1].set_xlabel("Quantis teóricos", fontsize=12)
    axes[1].set_ylabel("Quantis observados", fontsize=12)
    axes[1].grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_residuos_normalidade.png"), dpi=180)
    plt.close(fig)
    print("  OK fig_residuos_normalidade.png")


def fig_fatorial_mr():
    """Visualização de delineamento Fatorial de Medidas Repetidas."""
    np.random.seed(35)
    tempos = ["60 dias", "120 dias", "180 dias"]
    x = np.arange(len(tempos))

    # Dois tipos de geotêxtil (fator entre-sujeitos) medidos ao longo do tempo (fator intra)
    media_taboa = [92, 78, 60]
    media_ouricuri = [88, 72, 55]
    se = 3

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.errorbar(x, media_taboa, yerr=se, fmt="o-", color=AZUL,
                linewidth=2.5, markersize=9, capsize=5, label="Taboa (entre)")
    ax.errorbar(x, media_ouricuri, yerr=se, fmt="s--", color=AZUL_APOIO,
                linewidth=2.5, markersize=9, capsize=5, label="Ouricuri (entre)")

    ax.set_xticks(x)
    ax.set_xticklabels(tempos, fontsize=13)
    ax.set_ylabel("Resistência residual (%)", fontsize=13)
    ax.set_title("ANOVA Fatorial-MR: Tipo × Tempo", fontsize=14, fontweight="bold")
    ax.set_ylim(40, 105)
    ax.legend(fontsize=12)
    ax.grid(axis="y", alpha=0.3)

    # Anotações
    ax.annotate("Fator intra-sujeitos\n(Tempo)", xy=(1, 45), fontsize=10,
                ha="center", color=AZUL_PROF, fontstyle="italic")
    ax.annotate("", xy=(0, 43), xytext=(2, 43),
                arrowprops=dict(arrowstyle="<->", color=AZUL_PROF, lw=1.5))

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_fatorial_mr.png"), dpi=180)
    plt.close(fig)
    print("  OK fig_fatorial_mr.png")


if __name__ == "__main__":
    print("Gerando figuras — ANOVA de Medidas Repetidas")
    fig_mr_conceito()
    fig_esfericidade()
    fig_residuos_normalidade()
    fig_fatorial_mr()
    print("Concluído!")
