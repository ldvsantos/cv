"""
Gera figuras para os slides de Taxonomia de Bloom.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Paleta UEFS
CORES = ["#F2F2F2", "#C5CEE8", "#586BA6", "#27368C", "#2135A6", "#0D0D0D"]
CORES_TEXTO = ["#0D0D0D", "#0D0D0D", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"]

NIVEIS = [
    "1. LEMBRAR",
    "2. ENTENDER",
    "3. APLICAR",
    "4. ANALISAR",
    "5. AVALIAR",
    "6. CRIAR",
]

DESCRICOES = [
    "Recuperar informação",
    "Construir significado",
    "Usar em situação conhecida",
    "Decompor e identificar relações",
    "Julgar com critérios",
    "Gerar algo novo",
]


def fig_piramide_bloom():
    """Pirâmide triangular com 6 faixas horizontais."""
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_aspect("equal")
    ax.axis("off")

    n = len(NIVEIS)
    h_total = 6.0
    h_faixa = h_total / n
    base_max = 9.0
    cx = 5.0

    for i in range(n):
        y_bot = i * h_faixa + 0.5
        y_top = y_bot + h_faixa

        frac_bot = 1.0 - (i / n)
        frac_top = 1.0 - ((i + 1) / n)
        w_bot = base_max * frac_bot
        w_top = base_max * frac_top

        verts = [
            (cx - w_bot / 2, y_bot),
            (cx + w_bot / 2, y_bot),
            (cx + w_top / 2, y_top),
            (cx - w_top / 2, y_top),
        ]
        poly = patches.Polygon(verts, closed=True,
                               facecolor=CORES[i], edgecolor="white",
                               linewidth=2)
        ax.add_patch(poly)

        y_mid = (y_bot + y_top) / 2
        ax.text(cx, y_mid + 0.08, NIVEIS[i],
                ha="center", va="center", fontsize=13, fontweight="bold",
                color=CORES_TEXTO[i])
        ax.text(cx, y_mid - 0.22, DESCRICOES[i],
                ha="center", va="center", fontsize=9, fontstyle="italic",
                color=CORES_TEXTO[i], alpha=0.85)

    # setas laterais
    ax.annotate("", xy=(0.3, 6.3), xytext=(0.3, 0.5),
                arrowprops=dict(arrowstyle="->", lw=2, color="#586BA6"))
    ax.text(0.15, 3.5, "Complexidade", ha="center", va="center",
            fontsize=10, rotation=90, color="#586BA6", fontweight="bold")

    ax.annotate("", xy=(9.7, 0.5), xytext=(9.7, 6.3),
                arrowprops=dict(arrowstyle="->", lw=2, color="#27368C"))
    ax.text(9.85, 3.5, "Frequência de uso", ha="center", va="center",
            fontsize=10, rotation=270, color="#27368C", fontweight="bold")

    # rótulos LOTS / HOTS
    ax.text(cx, 0.15, "LOTS — Habilidades de Ordem Inferior",
            ha="center", va="center", fontsize=8, color="#888888")
    ax.text(cx, 6.7, "HOTS — Habilidades de Ordem Superior",
            ha="center", va="center", fontsize=8, color="#888888")

    fig.tight_layout()
    fig.savefig("fig_piramide_bloom.png", dpi=200, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    print("✓ fig_piramide_bloom.png")


def fig_bloom_verbos():
    """Tabela visual de verbos por nível em formato compacto."""
    verbos = {
        "Lembrar":  ["Listar", "Definir", "Citar", "Identificar"],
        "Entender": ["Explicar", "Comparar", "Resumir", "Classificar"],
        "Aplicar":  ["Calcular", "Executar", "Resolver", "Demonstrar"],
        "Analisar": ["Investigar", "Diferenciar", "Decompor", "Organizar"],
        "Avaliar":  ["Validar", "Julgar", "Argumentar", "Recomendar"],
        "Criar":    ["Propor", "Projetar", "Formular", "Desenvolver"],
    }

    fig, ax = plt.subplots(figsize=(11, 5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.5)
    ax.axis("off")

    cols = list(verbos.keys())
    w = 1.8
    gap = 0.15
    x_start = 0.3

    for j, nivel in enumerate(cols):
        x = x_start + j * (w + gap)
        # cabeçalho
        rect = patches.FancyBboxPatch((x, 5.3), w, 0.8,
                                       boxstyle="round,pad=0.1",
                                       facecolor=CORES[j], edgecolor="white",
                                       linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + w / 2, 5.7, nivel.upper(), ha="center", va="center",
                fontsize=9, fontweight="bold", color=CORES_TEXTO[j])

        # verbos
        for k, verbo in enumerate(verbos[nivel]):
            y = 4.6 - k * 0.9
            rect_v = patches.FancyBboxPatch((x, y), w, 0.7,
                                             boxstyle="round,pad=0.08",
                                             facecolor="#F7F7FA",
                                             edgecolor=CORES[j],
                                             linewidth=1)
            ax.add_patch(rect_v)
            ax.text(x + w / 2, y + 0.35, verbo, ha="center", va="center",
                    fontsize=8.5, color="#222222")

    fig.tight_layout()
    fig.savefig("fig_bloom_verbos.png", dpi=200, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    print("✓ fig_bloom_verbos.png")


def fig_bloom_analises():
    """Mapeamento visual: Nível → Técnica Estatística."""
    mapping = [
        ("Lembrar\nEntender", "Descritiva\nFrequências\nTabelas"),
        ("Aplicar", "Teste T\nANOVA\nCorrelação"),
        ("Analisar", "Regressão Múltipla\nANCOVA\nFatorial"),
        ("Avaliar", "Metanálise\nAFC / TRI\nComparação Modelos"),
        ("Criar", "Machine Learning\nLógica Fuzzy\nNovo Instrumento"),
    ]

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 4)
    ax.axis("off")

    cores_map = [CORES[0], CORES[2], CORES[3], CORES[4], CORES[5]]
    cores_txt = [CORES_TEXTO[0], CORES_TEXTO[2], CORES_TEXTO[3],
                 CORES_TEXTO[4], CORES_TEXTO[5]]

    w = 2.0
    gap = 0.5
    x_start = 0.3

    for j, (nivel, tecnica) in enumerate(mapping):
        x = x_start + j * (w + gap)

        # box nível
        rect = patches.FancyBboxPatch((x, 2.3), w, 1.3,
                                       boxstyle="round,pad=0.12",
                                       facecolor=cores_map[j],
                                       edgecolor="white", linewidth=2)
        ax.add_patch(rect)
        ax.text(x + w / 2, 2.95, nivel, ha="center", va="center",
                fontsize=8.5, fontweight="bold", color=cores_txt[j])

        # seta
        ax.annotate("", xy=(x + w / 2, 1.7), xytext=(x + w / 2, 2.25),
                    arrowprops=dict(arrowstyle="->", lw=1.5, color="#586BA6"))

        # box técnica
        rect2 = patches.FancyBboxPatch((x, 0.3), w, 1.4,
                                        boxstyle="round,pad=0.12",
                                        facecolor="#F2F2F2",
                                        edgecolor=cores_map[j],
                                        linewidth=1.5)
        ax.add_patch(rect2)
        ax.text(x + w / 2, 1.0, tecnica, ha="center", va="center",
                fontsize=7.5, color="#222222")

    fig.tight_layout()
    fig.savefig("fig_bloom_analises.png", dpi=200, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    print("✓ fig_bloom_analises.png")


if __name__ == "__main__":
    fig_piramide_bloom()
    fig_bloom_verbos()
    fig_bloom_analises()
    print("\nTodas as figuras geradas com sucesso!")
