#!/usr/bin/env python3
"""Gera figuras matplotlib para a aula de Regressao."""
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


def fig_01_regressao_linear():
    """Scatter com reta de regressao, residuos e IC."""
    fig, ax = plt.subplots(figsize=(12.8, 7.2), facecolor=FUNDO)
    ax.set_facecolor("white")

    n = 40
    x = np.random.uniform(5, 50, n)
    y = 2.5 * x + 15 + np.random.randn(n) * 12

    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    xline = np.linspace(3, 52, 100)
    yline = p(xline)

    # Residuos
    y_pred = p(x)
    for xi, yi, yp in zip(x, y, y_pred):
        ax.plot([xi, xi], [yi, yp], color="#E74C3C", alpha=0.3, lw=1, zorder=1)

    ax.scatter(x, y, c=AZUL, s=40, alpha=0.8, edgecolors="white", lw=0.5, zorder=3)
    ax.plot(xline, yline, color="#C0392B", lw=2.5, label=f"Y = {z[0]:.2f}X + {z[1]:.1f}", zorder=2)

    # IC approximado
    residuals = y - y_pred
    se = np.std(residuals)
    ax.fill_between(xline, yline - 1.96 * se, yline + 1.96 * se,
                    alpha=0.12, color=AZUL, label="IC 95%")

    # Anotar B0 e Bx
    ax.annotate(f"B0 = {z[1]:.1f}\n(Intercepto)", xy=(3, p(3)),
                xytext=(8, p(3) + 25), fontsize=10,
                arrowprops=dict(arrowstyle="->", color=AZUL_APOIO), color=AZUL_PROF)
    ax.annotate(f"Bx = {z[0]:.2f}\n(Inclinacao)", xy=(30, p(30)),
                xytext=(35, p(30) - 30), fontsize=10,
                arrowprops=dict(arrowstyle="->", color=AZUL_APOIO), color=AZUL_PROF)

    # R2
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r2 = 1 - ss_res / ss_tot
    ax.text(0.02, 0.95, f"R2 = {r2:.3f}", transform=ax.transAxes,
            fontsize=14, fontweight="bold", va="top",
            bbox=dict(boxstyle="round,pad=0.3", facecolor=FUNDO, edgecolor=AZUL))

    ax.set_xlabel("Investimento em Propaganda (mil R$)", fontsize=12)
    ax.set_ylabel("Vendas (unidades)", fontsize=12)
    ax.set_title("Regressao Linear Simples", fontsize=14, fontweight="bold")
    ax.legend(fontsize=10, loc="lower right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    path = os.path.join(DEST, "fig_01_regressao_linear.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_02_diagnosticos():
    """Painel 2x2 de diagnosticos de regressao."""
    fig, axes = plt.subplots(2, 2, figsize=(12.8, 7.2), facecolor=FUNDO)

    n = 60
    x = np.random.uniform(5, 50, n)
    y = 2.5 * x + 15 + np.random.randn(n) * 12
    z = np.polyfit(x, y, 1)
    y_pred = np.polyval(z, x)
    residuals = y - y_pred
    std_res = (residuals - np.mean(residuals)) / np.std(residuals)

    # 1. Y real vs Y predito
    ax = axes[0, 0]
    ax.set_facecolor("white")
    ax.scatter(y_pred, y, c=AZUL, alpha=0.6, s=25)
    lims = [min(y.min(), y_pred.min()), max(y.max(), y_pred.max())]
    ax.plot(lims, lims, "--", color="#C0392B", lw=1.5)
    ax.set_xlabel("Y Predito", fontsize=9)
    ax.set_ylabel("Y Observado", fontsize=9)
    ax.set_title("Y Observado vs Predito", fontsize=10, fontweight="bold")

    # 2. Q-Q plot (sem scipy)
    ax = axes[0, 1]
    ax.set_facecolor("white")
    sorted_res = np.sort(std_res)
    n_pts = len(sorted_res)
    theoretical = []
    for i in range(n_pts):
        p_val = (i + 0.5) / n_pts
        # Abramowitz & Stegun approx for inverse normal
        if p_val < 0.5:
            t = math.sqrt(-2.0 * math.log(p_val))
        else:
            t = math.sqrt(-2.0 * math.log(1.0 - p_val))
        c0, c1, c2 = 2.515517, 0.802853, 0.010328
        d1, d2, d3 = 1.432788, 0.189269, 0.001308
        z_val = t - (c0 + c1 * t + c2 * t**2) / (1 + d1 * t + d2 * t**2 + d3 * t**3)
        if p_val < 0.5:
            z_val = -z_val
        theoretical.append(z_val)
    ax.scatter(theoretical, sorted_res, c=AZUL, alpha=0.6, s=25)
    ax.plot([-3, 3], [-3, 3], "--", color="#C0392B", lw=1.5)
    ax.set_xlabel("Quantis Teoricos", fontsize=9)
    ax.set_ylabel("Quantis Amostrais", fontsize=9)
    ax.set_title("Q-Q Plot dos Residuos", fontsize=10, fontweight="bold")

    # 3. Residuos vs Fitted
    ax = axes[1, 0]
    ax.set_facecolor("white")
    ax.scatter(y_pred, std_res, c=AZUL, alpha=0.6, s=25)
    ax.axhline(0, color="#C0392B", lw=1.5, linestyle="--")
    ax.axhline(2, color="#888", lw=0.8, linestyle=":")
    ax.axhline(-2, color="#888", lw=0.8, linestyle=":")
    ax.set_xlabel("Y Predito (Fitted)", fontsize=9)
    ax.set_ylabel("Residuos Padronizados", fontsize=9)
    ax.set_title("Residuos vs Fitted", fontsize=10, fontweight="bold")

    # 4. Histograma residuos
    ax = axes[1, 1]
    ax.set_facecolor("white")
    ax.hist(std_res, bins=12, color=AZUL, alpha=0.7, edgecolor="white")
    ax.axvline(0, color="#C0392B", lw=1.5, linestyle="--")
    ax.set_xlabel("Residuos Padronizados", fontsize=9)
    ax.set_ylabel("Frequencia", fontsize=9)
    ax.set_title("Distribuicao dos Residuos", fontsize=10, fontweight="bold")

    plt.suptitle("Diagnosticos da Regressao", fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.94])
    path = os.path.join(DEST, "fig_02_diagnosticos_regressao.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_03_curva_logistica():
    """Curva sigmoide da regressao logistica."""
    fig, ax = plt.subplots(figsize=(12.8, 7.2), facecolor=FUNDO)
    ax.set_facecolor("white")

    x = np.linspace(-6, 6, 300)
    b0, b1 = 0, 1.2
    p = 1 / (1 + np.exp(-(b0 + b1 * x)))

    ax.plot(x, p, color=AZUL, lw=3, label="P(Y=1) = 1 / (1 + e^-(B0+B1X))")
    ax.axhline(0.5, color="#C0392B", lw=1.5, linestyle="--", alpha=0.7, label="P = 0,5 (ponto de corte)")
    ax.axhline(0, color="#888", lw=0.5)
    ax.axhline(1, color="#888", lw=0.5)

    # Dados dicotomicos simulados
    n = 80
    x_data = np.random.uniform(-5, 5, n)
    p_data = 1 / (1 + np.exp(-(b0 + b1 * x_data)))
    y_data = (np.random.random(n) < p_data).astype(float)
    jitter = np.random.uniform(-0.03, 0.03, n)
    ax.scatter(x_data, y_data + jitter, c=[AZUL if y == 1 else "#C0392B" for y in y_data],
               alpha=0.4, s=25, edgecolors="none", zorder=2)

    # Ponto de inflexao
    ax.plot(0, 0.5, "o", color="#E74C3C", markersize=10, zorder=5)
    ax.annotate("Ponto de inflexao\n(X=0, P=0.5)", xy=(0, 0.5), xytext=(2, 0.3),
                fontsize=11, arrowprops=dict(arrowstyle="->", color="#E74C3C"),
                color="#E74C3C", fontweight="bold")

    ax.set_xlabel("Variavel Preditora (X)", fontsize=12)
    ax.set_ylabel("Probabilidade P(Y=1)", fontsize=12)
    ax.set_title("Curva Logistica (Sigmoid)", fontsize=14, fontweight="bold")
    ax.legend(fontsize=10, loc="upper left")
    ax.set_ylim(-0.08, 1.08)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    path = os.path.join(DEST, "fig_03_curva_logistica.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_04_curva_roc():
    """Curva ROC com AUC."""
    fig, ax = plt.subplots(figsize=(8, 7.2), facecolor=FUNDO)
    ax.set_facecolor("white")

    # Simular curva ROC
    n = 200
    np.random.seed(42)
    y_true = np.concatenate([np.ones(100), np.zeros(100)])
    scores = np.concatenate([np.random.beta(5, 2, 100), np.random.beta(2, 5, 100)])

    thresholds = np.linspace(0, 1, 500)
    tpr_list = []
    fpr_list = []
    for t in thresholds:
        pred = (scores >= t).astype(float)
        tp = np.sum((pred == 1) & (y_true == 1))
        fp = np.sum((pred == 1) & (y_true == 0))
        fn = np.sum((pred == 0) & (y_true == 1))
        tn = np.sum((pred == 0) & (y_true == 0))
        tpr_list.append(tp / (tp + fn) if (tp + fn) > 0 else 0)
        fpr_list.append(fp / (fp + tn) if (fp + tn) > 0 else 0)

    fpr = np.array(fpr_list)
    tpr = np.array(tpr_list)
    # Sort by fpr
    idx = np.argsort(fpr)
    fpr = fpr[idx]
    tpr = tpr[idx]
    auc = np.trapz(tpr, fpr)

    ax.fill_between(fpr, tpr, alpha=0.15, color=AZUL)
    ax.plot(fpr, tpr, color=AZUL, lw=3, label=f"Modelo (AUC = {auc:.3f})")
    ax.plot([0, 1], [0, 1], "--", color="#888", lw=1.5, label="Acaso (AUC = 0,500)")

    ax.set_xlabel("1 - Especificidade (Taxa Falso Positivo)", fontsize=12)
    ax.set_ylabel("Sensibilidade (Taxa Verdadeiro Positivo)", fontsize=12)
    ax.set_title("Curva ROC", fontsize=14, fontweight="bold")
    ax.legend(fontsize=11, loc="lower right")
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.02)
    ax.set_aspect("equal")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    path = os.path.join(DEST, "fig_04_curva_roc.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


def fig_05_vif_multicolinearidade():
    """Grafico de barras de VIF."""
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=FUNDO)
    ax.set_facecolor("white")

    vars_names = ["Temperatura", "Precipitacao", "Umidade\nRelativa", "Cobertura\nVegetal", "Declividade"]
    vif_vals = [2.3, 1.8, 14.5, 3.1, 1.2]
    colors = ["#27AE60" if v < 10 else "#E74C3C" for v in vif_vals]

    bars = ax.barh(vars_names, vif_vals, color=colors, edgecolor="white", height=0.5)
    ax.axvline(10, color="#E74C3C", lw=2, linestyle="--", label="Limite VIF = 10")

    for bar, v in zip(bars, vif_vals):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                f"{v:.1f}", va="center", fontsize=11, fontweight="bold")

    ax.set_xlabel("VIF (Variance Inflation Factor)", fontsize=12)
    ax.set_title("Diagnostico de Multicolinearidade", fontsize=14, fontweight="bold")
    ax.legend(fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    path = os.path.join(DEST, "fig_05_vif_multicolinearidade.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [OK] {os.path.basename(path)}")


if __name__ == "__main__":
    print("=== Gerando figuras: Regressao ===")
    fig_01_regressao_linear()
    fig_02_diagnosticos()
    fig_03_curva_logistica()
    fig_04_curva_roc()
    fig_05_vif_multicolinearidade()
    print("=== Concluido ===")
