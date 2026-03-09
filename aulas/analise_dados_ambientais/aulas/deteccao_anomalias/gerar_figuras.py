#!/usr/bin/env python3
"""Gera figuras matplotlib para a aula de Deteccao de Anomalias."""
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


def fig_01_serie_temporal_anomalias():
    """Serie temporal de chuva com anomalias destacadas."""
    fig, ax = plt.subplots(figsize=(12.8, 5.5), facecolor=FUNDO)
    ax.set_facecolor("white")

    n = 365
    t = np.arange(n)
    # Padrao sazonal + ruido
    base = 60 + 40 * np.sin(2 * np.pi * t / 365) + np.random.randn(n) * 15
    base = np.maximum(base, 0)

    # Inserir anomalias
    anomalias = [45, 120, 210, 280, 340]
    for idx in anomalias:
        base[idx] = base[idx] + np.random.uniform(80, 140)

    normal = np.ones(n, dtype=bool)
    for idx in anomalias:
        normal[idx] = False

    ax.bar(t[normal], base[normal], color=AZUL, alpha=0.6, width=1, label="Normal")
    ax.bar(t[~normal], base[~normal], color="#E74C3C", alpha=0.9, width=1.5, label="Anomalia")

    # Limiar
    limiar = np.mean(base[normal]) + 2.5 * np.std(base[normal])
    ax.axhline(limiar, color="#E74C3C", lw=1.5, linestyle="--",
               label=f"Limiar (media + 2.5*sigma = {limiar:.0f} mm)")

    ax.set_xlabel("Dia do Ano", fontsize=12)
    ax.set_ylabel("Precipitacao (mm)", fontsize=12)
    ax.set_title("Serie Temporal de Precipitacao com Anomalias", fontsize=14, fontweight="bold")
    ax.legend(fontsize=10, loc="upper right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    path = os.path.join(DEST, "fig_01_serie_anomalias.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_02_decomposicao_stl():
    """Painel 4 linhas simulando decomposicao STL."""
    fig, axes = plt.subplots(4, 1, figsize=(12.8, 8), facecolor=FUNDO, sharex=True)

    n = 365
    t = np.arange(n)
    tendencia = 50 + 0.05 * t
    sazonal = 35 * np.sin(2 * np.pi * t / 365)
    residuo = np.random.randn(n) * 8
    y = tendencia + sazonal + residuo

    # Anomalias nos residuos
    anom_idx = [45, 120, 210, 280, 340]
    for idx in anom_idx:
        residuo[idx] += np.random.uniform(40, 70)
        y[idx] = tendencia[idx] + sazonal[idx] + residuo[idx]

    titles = ["Serie Original", "Tendencia", "Sazonalidade", "Residuos"]
    dados = [y, tendencia, sazonal, residuo]
    colors = [AZUL, AZUL_PROF, AZUL_APOIO, "#27AE60"]

    for ax, titulo, d, c in zip(axes, titles, dados, colors):
        ax.set_facecolor("white")
        ax.plot(t, d, color=c, lw=1)
        ax.set_ylabel(titulo, fontsize=9, fontweight="bold")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    # Marcar anomalias nos residuos
    limiar_r = np.mean(residuo) + 2.5 * np.std(residuo[:200])  # usando parte "limpa"
    axes[3].axhline(limiar_r, color="#E74C3C", lw=1, linestyle="--", alpha=0.7)
    axes[3].axhline(-limiar_r, color="#E74C3C", lw=1, linestyle="--", alpha=0.7)
    for idx in anom_idx:
        axes[3].plot(idx, residuo[idx], "o", color="#E74C3C", markersize=6, zorder=5)

    axes[-1].set_xlabel("Dia do Ano", fontsize=11)
    plt.suptitle("Decomposicao STL (Seasonal-Trend Decomposition)", fontsize=13, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    path = os.path.join(DEST, "fig_02_decomposicao_stl.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_03_iqr_boxplot():
    """Boxplot com limites IQR e anomalias classificadas."""
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=FUNDO)
    ax.set_facecolor("white")

    np.random.seed(42)
    dados = np.concatenate([np.random.normal(50, 12, 95), [120, 135, -10, 140, 0]])
    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)
    iqr = q3 - q1
    li = q1 - 1.5 * iqr
    ls = q3 + 1.5 * iqr

    normais = dados[(dados >= li) & (dados <= ls)]
    outliers = dados[(dados < li) | (dados > ls)]

    bp = ax.boxplot(dados, vert=True, patch_artist=True, widths=0.4,
                    boxprops=dict(facecolor=AZUL, alpha=0.4),
                    medianprops=dict(color="#E74C3C", lw=2),
                    flierprops=dict(marker="o", markerfacecolor="#E74C3C", markersize=8))

    # Anotar IQR
    ax.annotate(f"Q1 = {q1:.1f}", xy=(1.2, q1), fontsize=10, color=AZUL_PROF)
    ax.annotate(f"Q3 = {q3:.1f}", xy=(1.2, q3), fontsize=10, color=AZUL_PROF)
    ax.annotate(f"LI = {li:.1f}", xy=(1.2, li), fontsize=10, color="#E74C3C")
    ax.annotate(f"LS = {ls:.1f}", xy=(1.2, ls), fontsize=10, color="#E74C3C")

    ax.axhline(li, color="#E74C3C", lw=1, linestyle=":", alpha=0.7)
    ax.axhline(ls, color="#E74C3C", lw=1, linestyle=":", alpha=0.7)

    # Faixa IQR
    ax.axhspan(q1, q3, alpha=0.08, color=AZUL, label=f"IQR = {iqr:.1f}")

    ax.set_ylabel("Valor", fontsize=12)
    ax.set_title(f"Metodo IQR: {len(outliers)} outliers detectados", fontsize=14, fontweight="bold")
    ax.legend(fontsize=10, loc="upper left")
    ax.set_xticklabels(["Precipitacao (mm)"], fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    path = os.path.join(DEST, "fig_03_iqr_boxplot.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_04_isolation_forest():
    """Conceito visual do Isolation Forest: score histogram."""
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.5), facecolor=FUNDO)

    # Painel 1: scatter 2D tipo isolation
    ax = axes[0]
    ax.set_facecolor("white")
    np.random.seed(42)
    x_normal = np.random.normal(0, 1, 200)
    y_normal = np.random.normal(0, 1, 200)
    x_anom = np.random.uniform(-4, 4, 8)
    y_anom = np.random.uniform(-4, 4, 8)

    ax.scatter(x_normal, y_normal, c=AZUL, alpha=0.4, s=20, label="Normal")
    ax.scatter(x_anom, y_anom, c="#E74C3C", s=80, marker="x", lw=2, label="Anomalia", zorder=5)

    # Simular splits
    ax.axvline(2.5, color="#888", lw=0.8, linestyle="--", alpha=0.5)
    ax.axhline(-2.8, color="#888", lw=0.8, linestyle="--", alpha=0.5)
    ax.axvline(-3.2, color="#888", lw=0.8, linestyle="--", alpha=0.5)

    ax.set_xlabel("X1", fontsize=11)
    ax.set_ylabel("X2", fontsize=11)
    ax.set_title("Isolation Forest:\nAnomalia = poucos splits", fontsize=11, fontweight="bold")
    ax.legend(fontsize=9)

    # Painel 2: score histogram
    ax = axes[1]
    ax.set_facecolor("white")
    scores_normal = np.random.beta(2, 5, 200) * 0.4 + 0.3
    scores_anom = np.random.beta(5, 2, 15) * 0.3 + 0.65

    ax.hist(scores_normal, bins=20, color=AZUL, alpha=0.6, label="Normal", edgecolor="white")
    ax.hist(scores_anom, bins=8, color="#E74C3C", alpha=0.7, label="Anomalia", edgecolor="white")
    ax.axvline(0.6, color="#E74C3C", lw=2, linestyle="--", label="Limiar = 0.6")

    ax.set_xlabel("Anomaly Score", fontsize=11)
    ax.set_ylabel("Frequencia", fontsize=11)
    ax.set_title("Distribuicao dos Anomaly Scores", fontsize=11, fontweight="bold")
    ax.legend(fontsize=9)

    for a in axes:
        a.spines["top"].set_visible(False)
        a.spines["right"].set_visible(False)

    plt.suptitle("Isolation Forest", fontsize=13, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    path = os.path.join(DEST, "fig_04_isolation_forest.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_05_comparacao_metodos():
    """Comparacao lado-a-lado de metodos de deteccao."""
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=FUNDO)
    ax.set_facecolor("white")

    metodos = ["Z-Score", "IQR\n(Tukey)", "Desvio\nAbsoluto\nMediano", "Isolation\nForest", "STL +\nLimiar"]
    precisao = [72, 78, 81, 89, 85]
    recall = [68, 74, 79, 91, 87]

    x = np.arange(len(metodos))
    w = 0.3
    bars1 = ax.bar(x - w/2, precisao, w, label="Precisao (%)", color=AZUL, edgecolor="white")
    bars2 = ax.bar(x + w/2, recall, w, label="Recall (%)", color=AZUL_APOIO, edgecolor="white")

    for bar in bars1:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f"{int(bar.get_height())}", ha="center", fontsize=9, fontweight="bold")
    for bar in bars2:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f"{int(bar.get_height())}", ha="center", fontsize=9, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(metodos, fontsize=10)
    ax.set_ylabel("Desempenho (%)", fontsize=12)
    ax.set_title("Comparacao de Metodos de Deteccao de Anomalias", fontsize=14, fontweight="bold")
    ax.legend(fontsize=10)
    ax.set_ylim(0, 100)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    path = os.path.join(DEST, "fig_05_comparacao_metodos.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


if __name__ == "__main__":
    print("=== Gerando figuras: Deteccao de Anomalias ===")
    fig_01_serie_temporal_anomalias()
    fig_02_decomposicao_stl()
    fig_03_iqr_boxplot()
    fig_04_isolation_forest()
    fig_05_comparacao_metodos()
    print("=== Concluido ===")
