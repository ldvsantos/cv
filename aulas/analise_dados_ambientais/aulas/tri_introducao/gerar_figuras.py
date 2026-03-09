#!/usr/bin/env python3
"""Gera figuras matplotlib para a aula de Introducao a TRI."""
import os
import math
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


def _logistic(theta, a=1.0, b=0.0, c=0.0):
    """Curva Caracteristica do Item (CCI) - modelo 3PL."""
    return c + (1 - c) / (1 + np.exp(-a * (theta - b)))


def fig_01_cci_basica():
    """Curva Caracteristica do Item basica (1PL)."""
    fig, ax = plt.subplots(figsize=(12.8, 7.2), facecolor=FUNDO)
    ax.set_facecolor("white")

    theta = np.linspace(-4, 4, 500)
    p = _logistic(theta, a=1.0, b=0.0)

    ax.plot(theta, p, color=AZUL, lw=3)

    # Anotacoes
    ax.axhline(0.5, color="#888", lw=1, linestyle=":", alpha=0.7)
    ax.axvline(0, color="#888", lw=1, linestyle=":", alpha=0.7)
    ax.plot(0, 0.5, "o", color="#E74C3C", markersize=12, zorder=5)

    ax.annotate("b = 0.0\n(dificuldade)", xy=(0, 0.5), xytext=(1.5, 0.3),
                fontsize=12, arrowprops=dict(arrowstyle="->", color="#E74C3C"),
                color="#E74C3C", fontweight="bold")

    # Regioes
    ax.fill_between(theta[theta < -1.5], p[theta < -1.5], alpha=0.08, color="#E74C3C")
    ax.fill_between(theta[theta > 1.5], p[theta > 1.5], alpha=0.08, color="#27AE60")
    ax.text(-3, 0.15, "Baixa\nhabilidade", fontsize=10, color="#E74C3C", ha="center")
    ax.text(3, 0.85, "Alta\nhabilidade", fontsize=10, color="#27AE60", ha="center")

    ax.set_xlabel("Habilidade (theta)", fontsize=13)
    ax.set_ylabel("P(acerto)", fontsize=13)
    ax.set_title("Curva Caracteristica do Item (CCI) - Modelo 1PL", fontsize=14, fontweight="bold")
    ax.set_ylim(-0.05, 1.05)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    path = os.path.join(DEST, "fig_01_cci_basica.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_02_discriminacao():
    """Comparacao de diferentes discriminacoes (parametro a)."""
    fig, ax = plt.subplots(figsize=(12.8, 7.2), facecolor=FUNDO)
    ax.set_facecolor("white")

    theta = np.linspace(-4, 4, 500)
    params = [
        (0.3, "a = 0.3 (baixa)", "#E74C3C", "--"),
        (1.0, "a = 1.0 (moderada)", AZUL_APOIO, "-"),
        (2.0, "a = 2.0 (alta)", AZUL, "-"),
        (3.0, "a = 3.0 (muito alta)", AZUL_PROF, "-"),
    ]

    for a_val, label, color, ls in params:
        p = _logistic(theta, a=a_val, b=0.0)
        ax.plot(theta, p, color=color, lw=2.5, linestyle=ls, label=label)

    ax.axhline(0.5, color="#888", lw=0.8, linestyle=":", alpha=0.5)
    ax.set_xlabel("Habilidade (theta)", fontsize=13)
    ax.set_ylabel("P(acerto)", fontsize=13)
    ax.set_title("Efeito da Discriminacao (parametro a)", fontsize=14, fontweight="bold")
    ax.legend(fontsize=11, loc="upper left")
    ax.set_ylim(-0.05, 1.05)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.text(0.98, 0.3, "Maior a =\ncurva mais\ningreme", transform=ax.transAxes,
            fontsize=11, ha="right", color=AZUL_PROF, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor=FUNDO, edgecolor=AZUL))

    plt.tight_layout()
    path = os.path.join(DEST, "fig_02_discriminacao.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_03_dificuldade():
    """Efeito da dificuldade (parametro b): deslocamento horizontal."""
    fig, ax = plt.subplots(figsize=(12.8, 7.2), facecolor=FUNDO)
    ax.set_facecolor("white")

    theta = np.linspace(-4, 4, 500)
    diffs = [(-2.0, "#27AE60", "b=-2 (facil)"),
             (-0.5, AZUL_APOIO, "b=-0.5"),
             (0.5, AZUL, "b=+0.5"),
             (2.0, "#E74C3C", "b=+2 (dificil)")]

    for b_val, color, label in diffs:
        p = _logistic(theta, a=1.5, b=b_val)
        ax.plot(theta, p, color=color, lw=2.5, label=label)
        ax.plot(b_val, 0.5, "o", color=color, markersize=8, zorder=5)

    ax.axhline(0.5, color="#888", lw=0.8, linestyle=":", alpha=0.5)

    # Anotacoes efeito teto/chao
    ax.annotate("Efeito teto\n(muito facil)", xy=(-3, 0.95), fontsize=10,
                color="#27AE60", fontweight="bold")
    ax.annotate("Efeito chao\n(muito dificil)", xy=(2.5, 0.08), fontsize=10,
                color="#E74C3C", fontweight="bold")

    ax.set_xlabel("Habilidade (theta)", fontsize=13)
    ax.set_ylabel("P(acerto)", fontsize=13)
    ax.set_title("Efeito da Dificuldade (parametro b)", fontsize=14, fontweight="bold")
    ax.legend(fontsize=11, loc="center left")
    ax.set_ylim(-0.05, 1.05)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    path = os.path.join(DEST, "fig_03_dificuldade.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_04_1pl_vs_2pl():
    """Comparacao lado a lado 1PL vs 2PL."""
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.5), facecolor=FUNDO)

    theta = np.linspace(-4, 4, 500)
    items_b = [-1.5, -0.5, 0.5, 1.5]
    colors = ["#27AE60", AZUL_APOIO, AZUL, "#E74C3C"]

    # 1PL: todas as curvas com mesmo a=1
    ax = axes[0]
    ax.set_facecolor("white")
    for b, c in zip(items_b, colors):
        p = _logistic(theta, a=1.0, b=b)
        ax.plot(theta, p, color=c, lw=2, label=f"b={b}")
    ax.set_title("Modelo 1PL (Rasch)\na fixo = 1.0", fontsize=11, fontweight="bold")
    ax.legend(fontsize=9, loc="upper left")
    ax.set_xlabel("theta", fontsize=11)
    ax.set_ylabel("P(acerto)", fontsize=11)
    ax.axhline(0.5, color="#888", lw=0.8, linestyle=":", alpha=0.5)
    ax.set_ylim(-0.05, 1.05)

    # 2PL: curvas com a variavel
    ax = axes[1]
    ax.set_facecolor("white")
    items_a = [0.5, 1.2, 2.0, 0.8]
    for b, a, c in zip(items_b, items_a, colors):
        p = _logistic(theta, a=a, b=b)
        ax.plot(theta, p, color=c, lw=2, label=f"a={a}, b={b}")
    ax.set_title("Modelo 2PL\na variavel", fontsize=11, fontweight="bold")
    ax.legend(fontsize=9, loc="upper left")
    ax.set_xlabel("theta", fontsize=11)
    ax.set_ylabel("P(acerto)", fontsize=11)
    ax.axhline(0.5, color="#888", lw=0.8, linestyle=":", alpha=0.5)
    ax.set_ylim(-0.05, 1.05)

    for a in axes:
        a.spines["top"].set_visible(False)
        a.spines["right"].set_visible(False)

    plt.suptitle("Comparacao: 1PL (Rasch) vs 2PL", fontsize=13, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    path = os.path.join(DEST, "fig_04_1pl_vs_2pl.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_05_tri_vs_tct():
    """Diagrama conceitual TRI vs TCT."""
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.5), facecolor=FUNDO)

    # TCT: escore depende do teste
    ax = axes[0]
    ax.set_facecolor("white")
    testes = ["Teste Facil", "Teste Medio", "Teste Dificil"]
    escores = [85, 65, 40]
    bars = ax.bar(testes, escores, color=[AZUL_APOIO, AZUL, AZUL_PROF], edgecolor="white", width=0.5)
    for bar, e in zip(bars, escores):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f"{e}%", ha="center", fontsize=12, fontweight="bold")
    ax.set_ylabel("Escore (%)", fontsize=11)
    ax.set_title("TCT: Escore depende\ndo teste", fontsize=11, fontweight="bold", color="#E74C3C")
    ax.set_ylim(0, 100)
    ax.axhline(65, color="#888", lw=0.8, linestyle="--", alpha=0.5)
    ax.text(2.4, 67, "Mesmo aluno!", fontsize=9, color="#888")

    # TRI: theta invariante
    ax = axes[1]
    ax.set_facecolor("white")
    testes2 = ["Teste Facil", "Teste Medio", "Teste Dificil"]
    thetas = [1.2, 1.18, 1.22]
    bars = ax.bar(testes2, thetas, color=["#27AE60", "#27AE60", "#27AE60"], edgecolor="white", width=0.5)
    for bar, t in zip(bars, thetas):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.03,
                f"theta={t:.2f}", ha="center", fontsize=12, fontweight="bold")
    ax.set_ylabel("Habilidade (theta)", fontsize=11)
    ax.set_title("TRI: theta invariante\nao teste", fontsize=11, fontweight="bold", color="#27AE60")
    ax.set_ylim(0, 2)
    ax.axhline(1.2, color="#888", lw=0.8, linestyle="--", alpha=0.5)

    for a in axes:
        a.spines["top"].set_visible(False)
        a.spines["right"].set_visible(False)

    plt.suptitle("TCT vs TRI: Invariancia da Medida", fontsize=13, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    path = os.path.join(DEST, "fig_05_tri_vs_tct.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_06_politomico():
    """Curvas de categorias para item politomico (Likert 5 pontos)."""
    fig, ax = plt.subplots(figsize=(12.8, 7.2), facecolor=FUNDO)
    ax.set_facecolor("white")

    theta = np.linspace(-4, 4, 500)
    # Thresholds para 5 categorias (4 limiares)
    thresholds = [-2.5, -0.8, 0.8, 2.5]
    a = 1.5
    colors = ["#E74C3C", "#E67E22", AZUL_APOIO, AZUL, "#27AE60"]
    labels = ["Discordo\ntotalmente", "Discordo", "Neutro", "Concordo", "Concordo\ntotalmente"]

    # Calcular P de cada categoria via GRM
    n_cat = len(thresholds) + 1
    p_star = np.zeros((n_cat + 1, len(theta)))
    p_star[0, :] = 1.0  # P*(0) = 1
    p_star[n_cat, :] = 0.0  # P*(K) = 0
    for k, bk in enumerate(thresholds):
        p_star[k + 1, :] = _logistic(theta, a=a, b=bk)

    for k in range(n_cat):
        pk = p_star[k, :] - p_star[k + 1, :]
        ax.plot(theta, pk, color=colors[k], lw=2.5, label=labels[k])
        # Preencher levemente
        ax.fill_between(theta, pk, alpha=0.06, color=colors[k])

    ax.set_xlabel("Habilidade (theta)", fontsize=13)
    ax.set_ylabel("P(categoria k)", fontsize=13)
    ax.set_title("Curvas de Categorias - Item Politomico (Likert 5 pontos)", fontsize=14, fontweight="bold")
    ax.legend(fontsize=9, loc="upper right", ncol=2)
    ax.set_ylim(-0.02, 1.02)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    path = os.path.join(DEST, "fig_06_politomico.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


if __name__ == "__main__":
    print("=== Gerando figuras: TRI Introducao ===")
    fig_01_cci_basica()
    fig_02_discriminacao()
    fig_03_dificuldade()
    fig_04_1pl_vs_2pl()
    fig_05_tri_vs_tct()
    fig_06_politomico()
    print("=== Concluido ===")
