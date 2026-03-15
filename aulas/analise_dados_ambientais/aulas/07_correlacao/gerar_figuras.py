#!/usr/bin/env python3
"""Gera figuras matplotlib para a aula de Correlacao."""
import os
import math
import random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

AZUL = "#2135A6"
AZUL_PROF = "#27368C"
AZUL_APOIO = "#586BA6"
FUNDO = "#F2F2F2"
CONTRASTE = "#0D0D0D"
DEST = os.path.dirname(os.path.abspath(__file__))

random.seed(42)
np.random.seed(42)


def fig_01_tipos_correlacao():
    """Scatter plots mostrando diferentes tipos de correlacao."""
    fig, axes = plt.subplots(2, 3, figsize=(12.8, 7.2), facecolor=FUNDO)
    fig.suptitle("Tipos de Correlacao", fontsize=16, fontweight="bold", color=CONTRASTE)

    configs = [
        ("Positiva Forte\nr = 0,85", 0.85, AZUL),
        ("Positiva Fraca\nr = 0,25", 0.25, AZUL_APOIO),
        ("Nula\nr = 0,02", 0.02, "#888888"),
        ("Negativa Forte\nr = -0,85", -0.85, "#C0392B"),
        ("Negativa Fraca\nr = -0,25", -0.25, "#E74C3C"),
        ("Nao-Linear\nr = 0,05", None, "#8E44AD"),
    ]
    for ax, (title, r_val, color) in zip(axes.flat, configs):
        ax.set_facecolor("white")
        n = 80
        if r_val is not None:
            x = np.random.randn(n)
            y = r_val * x + math.sqrt(1 - r_val**2) * np.random.randn(n)
            ax.scatter(x, y, c=color, alpha=0.6, s=20, edgecolors="none")
            if abs(r_val) > 0.1:
                z = np.polyfit(x, y, 1)
                xline = np.linspace(x.min(), x.max(), 50)
                ax.plot(xline, np.polyval(z, xline), color=color, lw=2)
        else:
            x = np.linspace(-3, 3, n)
            y = x**2 + 0.5 * np.random.randn(n)
            ax.scatter(x, y, c=color, alpha=0.6, s=20, edgecolors="none")
            z = np.polyfit(x, y, 2)
            xline = np.linspace(-3, 3, 100)
            ax.plot(xline, np.polyval(z, xline), color=color, lw=2)
        ax.set_title(title, fontsize=10, fontweight="bold")
        ax.tick_params(labelsize=8)

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    path = os.path.join(DEST, "fig_01_tipos_correlacao.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_02_tamanho_efeito():
    """r vs r-quadrado (variancia compartilhada)."""
    fig, ax = plt.subplots(figsize=(12.8, 7.2), facecolor=FUNDO)
    ax.set_facecolor("white")

    r_vals = [0.10, 0.30, 0.50, 0.60, 0.70, 0.90, 1.00]
    r2_vals = [r**2 * 100 for r in r_vals]
    colors = plt.cm.RdYlGn(np.linspace(0.15, 0.85, len(r_vals)))

    bars = ax.bar([f"r = {r:.2f}" for r in r_vals], r2_vals, color=colors, edgecolor="white", width=0.6)
    for bar, r2 in zip(bars, r2_vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
                f"{r2:.1f}%", ha="center", fontsize=11, fontweight="bold")

    ax.set_ylabel("Variancia Compartilhada (r2, %)", fontsize=12)
    ax.set_xlabel("Coeficiente de Correlacao (r)", fontsize=12)
    ax.set_title("Tamanho de Efeito: r vs r2", fontsize=14, fontweight="bold")
    ax.set_ylim(0, 115)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    path = os.path.join(DEST, "fig_02_tamanho_efeito.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_03_escala_correlacao():
    """Escala visual de -1 a +1 com faixas de magnitude."""
    fig, ax = plt.subplots(figsize=(12.8, 4.0), facecolor=FUNDO)
    ax.set_facecolor(FUNDO)

    faixas = [
        (-1.0, -0.80, "#1A237E", "Muito Forte (-)"),
        (-0.80, -0.70, "#283593", "Forte (-)"),
        (-0.70, -0.40, "#3949AB", "Moderada (-)"),
        (-0.40, -0.10, "#7986CB", "Fraca (-)"),
        (-0.10, 0.10, "#E0E0E0", "Desprezivel"),
        (0.10, 0.40, "#FFAB91", "Fraca (+)"),
        (0.40, 0.70, "#FF7043", "Moderada (+)"),
        (0.70, 0.80, "#E64A19", "Forte (+)"),
        (0.80, 1.0, "#BF360C", "Muito Forte (+)"),
    ]

    for start, end, color, label in faixas:
        ax.barh(0, end - start, left=start, height=0.5, color=color, edgecolor="white", lw=0.5)
        mid = (start + end) / 2
        text_color = "white" if abs(mid) > 0.3 else CONTRASTE
        ax.text(mid, 0, label, ha="center", va="center", fontsize=7.5,
                fontweight="bold", color=text_color, rotation=0)

    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-0.5, 0.5)
    ax.set_xlabel("Coeficiente de Correlacao (r)", fontsize=12)
    ax.set_title("Escala de Magnitude da Correlacao (Cohen, 1992)", fontsize=14, fontweight="bold")
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    for val in [-1, -0.8, -0.7, -0.4, -0.1, 0.1, 0.4, 0.7, 0.8, 1.0]:
        ax.axvline(val, color="white", lw=1, ymin=0.2, ymax=0.8)
        ax.text(val, -0.35, f"{val:.1f}", ha="center", fontsize=8, color="#555")

    plt.tight_layout()
    path = os.path.join(DEST, "fig_03_escala_correlacao.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_04_correlacao_espuria():
    """Exemplo de correlacao espuria com variavel confundidora."""
    fig, axes = plt.subplots(1, 3, figsize=(12.8, 4.5), facecolor=FUNDO)

    # Dados simulados: temperatura -> praia e sorvete
    n = 60
    temp = np.random.uniform(15, 40, n)
    praia = 0.8 * temp + np.random.randn(n) * 3
    sorvete = 0.7 * temp + np.random.randn(n) * 4

    # Plot 1: praia vs sorvete (parece correlacao)
    ax1 = axes[0]
    ax1.set_facecolor("white")
    ax1.scatter(praia, sorvete, c=AZUL, alpha=0.6, s=20)
    z = np.polyfit(praia, sorvete, 1)
    xl = np.linspace(praia.min(), praia.max(), 50)
    ax1.plot(xl, np.polyval(z, xl), color="#C0392B", lw=2)
    r = np.corrcoef(praia, sorvete)[0, 1]
    ax1.set_title(f"Correlacao Espuria\nr = {r:.2f}", fontsize=10, fontweight="bold")
    ax1.set_xlabel("Frequencia na Praia", fontsize=9)
    ax1.set_ylabel("Consumo de Sorvete", fontsize=9)

    # Plot 2: Separado por temperatura
    ax2 = axes[1]
    ax2.set_facecolor("white")
    mask_quente = temp > 27.5
    ax2.scatter(praia[mask_quente], sorvete[mask_quente], c="#C0392B", alpha=0.6, s=20, label="Quente (>27C)")
    ax2.scatter(praia[~mask_quente], sorvete[~mask_quente], c=AZUL, alpha=0.6, s=20, label="Frio (<27C)")
    ax2.set_title("Controlando Temperatura", fontsize=10, fontweight="bold")
    ax2.set_xlabel("Frequencia na Praia", fontsize=9)
    ax2.legend(fontsize=8)

    # Plot 3: Diagrama causal
    ax3 = axes[2]
    ax3.set_facecolor(FUNDO)
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 10)
    ax3.axis("off")
    # Caixas
    for x, y, txt, cor in [(5, 9, "TEMPERATURA\n(Confundidora)", "#E74C3C"),
                           (1, 3, "Praia", AZUL),
                           (9, 3, "Sorvete", AZUL_APOIO)]:
        ax3.add_patch(plt.Rectangle((x - 1.8, y - 1), 3.6, 2, facecolor=cor,
                                    edgecolor="white", alpha=0.9, lw=2, zorder=2))
        ax3.text(x, y, txt, ha="center", va="center", fontsize=9,
                 fontweight="bold", color="white", zorder=3)
    # Setas
    ax3.annotate("", xy=(1.5, 4.2), xytext=(4, 7.8),
                 arrowprops=dict(arrowstyle="->", lw=2, color="#E74C3C"))
    ax3.annotate("", xy=(8.5, 4.2), xytext=(6, 7.8),
                 arrowprops=dict(arrowstyle="->", lw=2, color="#E74C3C"))
    ax3.annotate("", xy=(7, 3), xytext=(3, 3),
                 arrowprops=dict(arrowstyle="->", lw=2, color="#888", linestyle="dashed"))
    ax3.text(5, 2, "Espuria!", ha="center", fontsize=10, style="italic", color="#888")
    ax3.set_title("Variavel Confundidora", fontsize=10, fontweight="bold")

    plt.tight_layout()
    path = os.path.join(DEST, "fig_04_correlacao_espuria.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


if __name__ == "__main__":
    print("=== Gerando figuras: Correlacao ===")
    fig_01_tipos_correlacao()
    fig_02_tamanho_efeito()
    fig_03_escala_correlacao()
    fig_04_correlacao_espuria()
    print("=== Concluido ===")
