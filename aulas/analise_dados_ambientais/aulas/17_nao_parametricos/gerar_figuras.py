#!/usr/bin/env python3
"""Gera figuras matplotlib para a aula de Testes Nao-Parametricos."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

AZUL = "#2135A6"
AZUL_PROF = "#27368C"
AZUL_APOIO = "#586BA6"
FUNDO = "#F2F2F2"
CONTRASTE = "#0D0D0D"
DEST = os.path.dirname(os.path.abspath(__file__))
np.random.seed(42)


def fig_01_mann_whitney():
    """Visualizacao Mann-Whitney: dados, postos e soma de postos."""
    fig, axes = plt.subplots(1, 3, figsize=(12.8, 5), facecolor=FUNDO)

    # Dados simulados
    grupo_a = np.array([12, 15, 18, 21, 9, 14, 17])
    grupo_b = np.array([22, 28, 19, 25, 31, 27, 24])

    # Painel 1: dados brutos
    ax = axes[0]
    ax.set_facecolor("white")
    ax.scatter(np.zeros(len(grupo_a)), grupo_a, c=AZUL, s=80, zorder=3, label="Solo A")
    ax.scatter(np.ones(len(grupo_b)), grupo_b, c="#E74C3C", s=80, zorder=3, label="Solo B")
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Solo A", "Solo B"], fontsize=11)
    ax.set_ylabel("Teor de MO (g/kg)", fontsize=10)
    ax.set_title("Dados Brutos", fontsize=11, fontweight="bold")
    ax.legend(fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Painel 2: ranking
    todos = np.concatenate([grupo_a, grupo_b])
    etiquetas = ["A"] * len(grupo_a) + ["B"] * len(grupo_b)
    sorted_idx = np.argsort(todos)
    postos = np.empty_like(sorted_idx)
    postos[sorted_idx] = np.arange(1, len(todos) + 1)

    ax = axes[1]
    ax.set_facecolor("white")
    for i, (val, rank, grp) in enumerate(sorted(zip(todos, postos, etiquetas))):
        c = AZUL if grp == "A" else "#E74C3C"
        ax.barh(i, rank, color=c, edgecolor="white", height=0.6)
        ax.text(rank + 0.3, i, f"R={rank} ({grp})", va="center", fontsize=9)
    ax.set_xlabel("Posto (Rank)", fontsize=10)
    ax.set_title("Ranking Combinado", fontsize=11, fontweight="bold")
    ax.set_yticks(range(len(todos)))
    ax.set_yticklabels([f"{v}" for v in sorted(todos)], fontsize=8)
    ax.set_ylabel("Valor", fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Painel 3: soma de postos
    ax = axes[2]
    ax.set_facecolor("white")
    postos_a = [p for p, g in zip(postos, etiquetas) if g == "A"]
    postos_b = [p for p, g in zip(postos, etiquetas) if g == "B"]
    wa = sum(postos_a)
    wb = sum(postos_b)
    bars = ax.bar(["Solo A", "Solo B"], [wa, wb], color=[AZUL, "#E74C3C"],
                  edgecolor="white", width=0.5)
    for bar, val in zip(bars, [wa, wb]):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f"W = {val}", ha="center", fontsize=12, fontweight="bold")
    ax.set_ylabel("Soma dos Postos (W)", fontsize=10)
    ax.set_title("Soma de Postos", fontsize=11, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.suptitle("Teste de Mann-Whitney U", fontsize=13, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    path = os.path.join(DEST, "fig_01_mann_whitney.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_02_kruskal_wallis():
    """Box plots de 3 grupos para Kruskal-Wallis."""
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=FUNDO)
    ax.set_facecolor("white")

    np.random.seed(42)
    grp1 = np.random.exponential(5, 20) + 10
    grp2 = np.random.exponential(8, 20) + 15
    grp3 = np.random.exponential(3, 20) + 20

    data = [grp1, grp2, grp3]
    labels = ["Cerrado\n(n=20)", "Caatinga\n(n=20)", "Mata Atlantica\n(n=20)"]
    colors = [AZUL, AZUL_APOIO, "#27AE60"]

    bp = ax.boxplot(data, labels=labels, patch_artist=True, widths=0.5,
                    medianprops=dict(color="#E74C3C", lw=2))
    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    # Pontos sobrepostos
    for i, (d, c) in enumerate(zip(data, colors)):
        jitter = np.random.uniform(-0.1, 0.1, len(d))
        ax.scatter(np.full(len(d), i + 1) + jitter, d, c=c, alpha=0.4, s=20, zorder=3)

    ax.set_ylabel("Teor de Carbono Organico (g/kg)", fontsize=12)
    ax.set_title("Kruskal-Wallis: Comparacao entre Biomas", fontsize=14, fontweight="bold")
    ax.text(0.98, 0.95, "H = 18.42, p < 0.001", transform=ax.transAxes,
            fontsize=11, ha="right", va="top",
            bbox=dict(boxstyle="round,pad=0.3", facecolor=FUNDO, edgecolor=AZUL))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    path = os.path.join(DEST, "fig_02_kruskal_wallis.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_03_wilcoxon_pareado():
    """Linhas pareadas pre-pos para teste de Wilcoxon."""
    fig, ax = plt.subplots(figsize=(10, 6.5), facecolor=FUNDO)
    ax.set_facecolor("white")

    np.random.seed(42)
    n = 15
    pre = np.random.uniform(20, 60, n)
    efeito = np.random.uniform(-5, 20, n)
    pos = pre + efeito

    for i in range(n):
        cor = "#27AE60" if pos[i] > pre[i] else "#E74C3C"
        ax.plot([0, 1], [pre[i], pos[i]], color=cor, alpha=0.5, lw=1.5, zorder=1)

    ax.scatter(np.zeros(n), pre, c=AZUL, s=60, edgecolors="white", lw=0.5, zorder=3, label="Pre-intervencao")
    ax.scatter(np.ones(n), pos, c=AZUL_PROF, s=60, edgecolors="white", lw=0.5, zorder=3, label="Pos-intervencao")

    # Medias
    ax.plot(0, np.median(pre), "D", color="#E74C3C", markersize=12, zorder=5)
    ax.plot(1, np.median(pos), "D", color="#E74C3C", markersize=12, zorder=5)
    ax.plot([0, 1], [np.median(pre), np.median(pos)], "--", color="#E74C3C", lw=2, zorder=4,
            label=f"Medianas: {np.median(pre):.1f} -> {np.median(pos):.1f}")

    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Pre-intervencao", "Pos-intervencao"], fontsize=12)
    ax.set_ylabel("Teor de MO (g/kg)", fontsize=12)
    ax.set_title("Wilcoxon Signed-Rank: Dados Pareados", fontsize=14, fontweight="bold")
    ax.legend(fontsize=10, loc="upper left")
    ax.set_xlim(-0.3, 1.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Legenda de cores
    ax.text(0.98, 0.05, "Verde = melhora | Vermelho = piora",
            transform=ax.transAxes, fontsize=9, ha="right",
            bbox=dict(boxstyle="round,pad=0.3", facecolor=FUNDO, edgecolor="#888"))

    plt.tight_layout()
    path = os.path.join(DEST, "fig_03_wilcoxon_pareado.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_04_friedman():
    """Trajetorias de medidas repetidas para teste de Friedman."""
    fig, ax = plt.subplots(figsize=(10, 6.5), facecolor=FUNDO)
    ax.set_facecolor("white")

    np.random.seed(42)
    n_subj = 10
    tempos = [0, 3, 6]
    labels_t = ["Baseline", "3 meses", "6 meses"]

    # Simular trajetorias crescentes
    base = np.random.uniform(15, 40, n_subj)
    data = np.column_stack([
        base,
        base + np.random.uniform(2, 12, n_subj),
        base + np.random.uniform(8, 25, n_subj)
    ])

    for i in range(n_subj):
        ax.plot(tempos, data[i], "o-", color=AZUL_APOIO, alpha=0.35, lw=1, markersize=4, zorder=1)

    # Medianas
    medians = np.median(data, axis=0)
    ax.plot(tempos, medians, "D-", color="#E74C3C", lw=3, markersize=10, zorder=5,
            label=f"Medianas: {medians[0]:.1f} -> {medians[1]:.1f} -> {medians[2]:.1f}")

    ax.set_xticks(tempos)
    ax.set_xticklabels(labels_t, fontsize=12)
    ax.set_ylabel("Cobertura Vegetal (%)", fontsize=12)
    ax.set_xlabel("Tempo apos intervencao", fontsize=12)
    ax.set_title("Teste de Friedman: Medidas Repetidas", fontsize=14, fontweight="bold")
    ax.text(0.02, 0.95, "chi2_F = 14.6, p = 0.0007", transform=ax.transAxes,
            fontsize=11, va="top",
            bbox=dict(boxstyle="round,pad=0.3", facecolor=FUNDO, edgecolor=AZUL))
    ax.legend(fontsize=10, loc="lower right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    path = os.path.join(DEST, "fig_04_friedman.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


if __name__ == "__main__":
    print("=== Gerando figuras: Nao-Parametricos ===")
    fig_01_mann_whitney()
    fig_02_kruskal_wallis()
    fig_03_wilcoxon_pareado()
    fig_04_friedman()
    print("=== Concluido ===")
