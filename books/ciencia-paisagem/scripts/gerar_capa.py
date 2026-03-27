"""
Gera a capa moderna do livro "Ciência da Paisagem"
com curvas topográficas estilizadas e tipografia limpa.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math

# ── Dimensões (mesma da capa original) ──────────────────────
W, H = 1357, 1888
DPI = 150

# ── Paleta ──────────────────────────────────────────────────
BG_TOP    = (15, 52, 40)       # verde-escuro profundo
BG_BOT    = (8, 35, 50)        # azul-petróleo escuro
ACCENT    = (72, 180, 120)     # verde-claro vibrante
ACCENT2   = (45, 140, 100)     # verde intermediário
LINE_CLR  = (50, 120, 85, 55)  # curvas topográficas (com alpha)
LINE_HI   = (90, 200, 140, 80) # curvas de destaque
WHITE     = (255, 255, 255)
LIGHT     = (220, 235, 225)
SUBTLE    = (180, 210, 190)
SEPARATOR = (72, 180, 120, 160)

# ── Fontes (Windows) ────────────────────────────────────────
def get_font(name, size, bold=False):
    """Tenta carregar fonte do sistema Windows."""
    candidates = []
    if bold:
        candidates = [
            f"C:/Windows/Fonts/{name}bd.ttf",
            f"C:/Windows/Fonts/{name}-Bold.ttf",
            f"C:/Windows/Fonts/{name}b.ttf",
        ]
    candidates += [
        f"C:/Windows/Fonts/{name}.ttf",
        f"C:/Windows/Fonts/{name}-Regular.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    # fallback
    return ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size)


# ── Criação da imagem base com a Foto "Paisagem Resiliente" ─────────
bg_img_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "img", "paisagem_resiliente.jpg")

if os.path.exists(bg_img_path):
    bg_img = Image.open(bg_img_path).convert("RGBA")
    
    # Redimensionar a imagem para cobrir a capa inteira (zoom fill)
    bg_w, bg_h = bg_img.size
    aspect_capa = W / H
    aspect_bg = bg_w / bg_h
    
    if aspect_bg > aspect_capa:
        # A imagem é mais larga que a capa, cropar nas laterais
        new_h = H
        new_w = int(aspect_bg * H)
        bg_img = bg_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        # Cortar do centro
        offset = (new_w - W) // 2
        bg_img = bg_img.crop((offset, 0, offset + W, H))
    else:
        # A imagem é mais alta que a capa, cropar em cima/embaixo
        new_w = W
        new_h = int(W / aspect_bg)
        bg_img = bg_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        # Cortar do centro (um pouco mais para baixo para focar na árvore/cabras)
        offset = (new_h - H) // 2
        bg_img = bg_img.crop((0, offset, W, offset + H))
        
    img = bg_img
    draw = ImageDraw.Draw(img)
else:
    # Se não achar a imagem, faz o fundo com gradiente como antes
    img = Image.new("RGBA", (W, H), BG_TOP)
    draw = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        t2 = t * t * (3 - 2 * t)
        r = int(BG_TOP[0] + (BG_BOT[0] - BG_TOP[0]) * t2)
        g = int(BG_TOP[1] + (BG_BOT[1] - BG_TOP[1]) * t2)
        b = int(BG_TOP[2] + (BG_BOT[2] - BG_TOP[2]) * t2)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))


# ── Curvas topográficas (Perlin-like com seno composto) ─────
topo_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
topo_draw = ImageDraw.Draw(topo_layer)

np.random.seed(42)

# Gerar campo de elevação simplificado
def elevation(x, y):
    """Superfície pseudo-topográfica baseada em somas de senos."""
    val = 0
    # várias frequências
    val += 1.0 * math.sin(x * 0.004 + 0.3) * math.cos(y * 0.003 + 1.2)
    val += 0.6 * math.sin(x * 0.007 - 1.5) * math.sin(y * 0.006 + 0.8)
    val += 0.4 * math.cos(x * 0.012 + 2.1) * math.cos(y * 0.009 - 0.5)
    val += 0.25 * math.sin(x * 0.02 + y * 0.015)
    val += 0.15 * math.cos(x * 0.025 - y * 0.02 + 1.0)
    return val

# Zona das curvas: parte central da imagem (y de 280 a 1150)
TOPO_Y0, TOPO_Y1 = 280, 1150
n_levels = 18

# Calcular range de elevação na zona
samples_e = [elevation(x, y)
             for x in range(0, W, 20) for y in range(TOPO_Y0, TOPO_Y1, 20)]
e_min, e_max = min(samples_e), max(samples_e)
levels = np.linspace(e_min + 0.05, e_max - 0.05, n_levels)

# Marching-squares simplificado: para cada nível, rastrear iso-linhas
step = 4  # resolução do grid
for idx, level in enumerate(levels):
    is_highlight = (idx % 5 == 0)
    color = LINE_HI if is_highlight else LINE_CLR
    width = 2 if is_highlight else 1

    for y in range(TOPO_Y0, TOPO_Y1 - step, step):
        for x in range(0, W - step, step):
            # 4 cantos da célula
            e00 = elevation(x, y)
            e10 = elevation(x + step, y)
            e01 = elevation(x, y + step)
            e11 = elevation(x + step, y + step)

            # checar se o iso-nível cruza esta célula
            above = [(e00 >= level), (e10 >= level), (e01 >= level), (e11 >= level)]
            n_above = sum(above)
            if n_above == 0 or n_above == 4:
                continue

            # interpolar pontos de cruzamento nas bordas
            pts = []
            # borda superior (e00 → e10)
            if above[0] != above[1]:
                t = (level - e00) / (e10 - e00 + 1e-10)
                pts.append((x + t * step, y))
            # borda esquerda (e00 → e01)
            if above[0] != above[2]:
                t = (level - e00) / (e01 - e00 + 1e-10)
                pts.append((x, y + t * step))
            # borda inferior (e01 → e11)
            if above[2] != above[3]:
                t = (level - e01) / (e11 - e01 + 1e-10)
                pts.append((x + t * step, y + step))
            # borda direita (e10 → e11)
            if above[1] != above[3]:
                t = (level - e10) / (e11 - e10 + 1e-10)
                pts.append((x + step, y + t * step))

            if len(pts) >= 2:
                topo_draw.line([tuple(pts[0]), tuple(pts[1])],
                               fill=color, width=width)

# Aplicar blur suave nas curvas para visual orgânico
topo_layer = topo_layer.filter(ImageFilter.GaussianBlur(radius=1.2))
img = Image.alpha_composite(img, topo_layer)

# ── Faixa escurecida/fundo para o texto ficar legível ─────────────
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ov_draw = ImageDraw.Draw(overlay)

# Overlay geral muito sutil para escurecer a foto
ov_draw.rectangle([0, 0, W, H], fill=(10, 30, 20, 100))

# Faixa escura forte no topo (para o título principal)
for y in range(0, 450):
    alpha = int(220 * (1 - y / 450))
    ov_draw.line([(0, y), (W, y)], fill=(0, 20, 10, alpha))

# Faixa escura forte embaixo (para autor e informações)
for y in range(1200, H):
    t = (y - 1200) / (H - 1200)
    alpha = int(220 * t)
    ov_draw.line([(0, y), (W, y)], fill=(0, 15, 10, alpha))

img = Image.alpha_composite(img, overlay)

# ── Tipografia ──────────────────────────────────────────────
draw = ImageDraw.Draw(img)

# ---- Título principal ----
font_title1 = get_font("calibri", 92, bold=True)
font_title2 = get_font("calibri", 120, bold=True)
font_sub    = get_font("calibri", 46)
font_author = get_font("calibri", 54, bold=True)
font_info   = get_font("calibri", 36)
font_small  = get_font("calibri", 30)

# "ANÁLISE DA" — tracking amplo, letras espaçadas
title1 = "ANÁLISE DA"
title2 = "PAISAGEM"

def draw_spaced_text(draw, text, x_center, y, font, fill, spacing=8):
    """Desenha texto com espaçamento entre letras."""
    # Calcular largura total
    total_w = 0
    char_widths = []
    for ch in text:
        bbox = font.getbbox(ch)
        cw = bbox[2] - bbox[0]
        char_widths.append(cw)
        total_w += cw + spacing
    total_w -= spacing  # remover último espaçamento

    x_start = x_center - total_w // 2
    x = x_start
    for ch, cw in zip(text, char_widths):
        draw.text((x, y), ch, font=font, fill=fill)
        x += cw + spacing

# Título
draw_spaced_text(draw, title1, W // 2, 80, font_title1, WHITE, spacing=14)
draw_spaced_text(draw, title2, W // 2, 175, font_title2, ACCENT, spacing=18)

# Linha decorativa fina
line_y = 320
line_w = 500
draw.line([(W//2 - line_w//2, line_y), (W//2 + line_w//2, line_y)],
          fill=ACCENT + (140,), width=2)

# ── Pequeno badge/tag no centro das curvas ──────────────────
# Subtítulo posicionado sobre as curvas com fundo sutil
sub_text = "Fundamentos, Métodos de Análise"
sub_text2 = "e Planejamento Territorial"

# Fundo semitransparente para subtítulo
sub_y = 360
sub_bg = Image.new("RGBA", (W, 130), (0, 0, 0, 0))
sub_bg_draw = ImageDraw.Draw(sub_bg)
sub_bg_draw.rounded_rectangle(
    [(W//2 - 480, 5), (W//2 + 480, 125)],
    radius=12, fill=(10, 40, 30, 140)
)
img.paste(Image.alpha_composite(
    Image.new("RGBA", (W, 130), (0, 0, 0, 0)), sub_bg),
    (0, sub_y), sub_bg)

draw = ImageDraw.Draw(img)  # recriar draw após paste

# Texto do subtítulo
bbox1 = font_sub.getbbox(sub_text)
bbox2 = font_sub.getbbox(sub_text2)
tw1 = bbox1[2] - bbox1[0]
tw2 = bbox2[2] - bbox2[0]
draw.text(((W - tw1) // 2, sub_y + 15), sub_text, font=font_sub, fill=LIGHT)
draw.text(((W - tw2) // 2, sub_y + 68), sub_text2, font=font_sub, fill=LIGHT)

# ── Mosaico de retângulos (grid temático de uso do solo) ────
mosaic_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
mos_draw = ImageDraw.Draw(mosaic_layer)

# Paleta de verdes para o mosaico (simula classes de uso do solo)
MOSAIC_COLORS = [
    (25, 80, 55),    # floresta densa
    (35, 100, 65),   # mata secundária
    (50, 130, 80),   # vegetação arbustiva
    (65, 155, 95),   # pastagem verde
    (40, 110, 70),   # reflorestamento
    (80, 170, 110),  # agricultura irrigada
    (55, 140, 85),   # cerrado
    (30, 90, 60),    # mata ciliar
    (70, 160, 100),  # campo limpo
    (45, 120, 75),   # transição
    (90, 185, 125),  # área verde urbana
    (20, 70, 48),    # sombra/relevo
]

np.random.seed(123)

# Parâmetros do grid
MOSAIC_Y0 = 540       # início do mosaico (abaixo do subtítulo)
MOSAIC_Y1 = 1200      # fim do mosaico (acima do autor)
MOSAIC_X0 = 60        # margem esquerda
MOSAIC_X1 = W - 60    # margem direita
COLS = 10
ROWS = 8
GAP = 5               # espaço entre retângulos
CORNER_R = 4          # raio dos cantos arredondados

cell_w = (MOSAIC_X1 - MOSAIC_X0 - GAP * (COLS - 1)) / COLS
cell_h = (MOSAIC_Y1 - MOSAIC_Y0 - GAP * (ROWS - 1)) / ROWS

for row in range(ROWS):
    for col in range(COLS):
        x0 = MOSAIC_X0 + col * (cell_w + GAP)
        y0 = MOSAIC_Y0 + row * (cell_h + GAP)
        x1 = x0 + cell_w
        y1 = y0 + cell_h

        # Cor baseada na elevação + variação aleatória
        cx, cy = int((x0 + x1) / 2), int((y0 + y1) / 2)
        elev = elevation(cx, cy)
        # Mapear elevação para índice de cor
        t_elev = (elev - e_min) / (e_max - e_min + 1e-10)
        idx = int(t_elev * (len(MOSAIC_COLORS) - 1))
        idx = max(0, min(len(MOSAIC_COLORS) - 1, idx))

        # Adicionar variação aleatória na luminosidade
        base = MOSAIC_COLORS[idx]
        variation = np.random.randint(-15, 16)
        color = tuple(max(10, min(255, c + variation)) for c in base)

        # Alpha variável: mais opaco no centro, mais transparente nas bordas
        dist_center_y = abs((y0 + y1) / 2 - (MOSAIC_Y0 + MOSAIC_Y1) / 2)
        max_dist_y = (MOSAIC_Y1 - MOSAIC_Y0) / 2
        alpha = int(200 - 80 * (dist_center_y / max_dist_y))
        alpha = max(80, min(220, alpha))

        mos_draw.rounded_rectangle(
            [(int(x0), int(y0)), (int(x1), int(y1))],
            radius=CORNER_R,
            fill=color + (alpha,)
        )

# Blur leve no mosaico para suavizar
mosaic_layer = mosaic_layer.filter(ImageFilter.GaussianBlur(radius=0.8))
img = Image.alpha_composite(img, mosaic_layer)
draw = ImageDraw.Draw(img)

# ── Seção inferior: autor ───────────────────────────────────
# Linha separadora
sep_y = 1420
draw.line([(W//2 - 350, sep_y), (W//2 + 350, sep_y)],
          fill=ACCENT + (120,), width=2)

# Nome do autor
author = "Luiz Diego Vidal Santos"
bbox_a = font_author.getbbox(author)
aw = bbox_a[2] - bbox_a[0]
draw.text(((W - aw) // 2, 1470), author, font=font_author, fill=WHITE)

# Afiliação
affil = "Universidade Estadual de Feira de Santana"
bbox_af = font_info.getbbox(affil)
afw = bbox_af[2] - bbox_af[0]
draw.text(((W - afw) // 2, 1545), affil, font=font_info, fill=SUBTLE)

# Ano e licença
year_lic = "2026  •  CC BY-NC-SA 4.0"
bbox_yl = font_small.getbbox(year_lic)
ylw = bbox_yl[2] - bbox_yl[0]
draw.text(((W - ylw) // 2, 1610), year_lic, font=font_small, fill=SUBTLE)

# ── Detalhes decorativos ────────────────────────────────────
# Pequena barra vertical accent à esquerda do título
draw.rectangle([(80, 90), (86, 290)], fill=ACCENT + (100,))

# Ícone abstrato: hexágono pequeno no canto inferior
def draw_hexagon(draw, cx, cy, r, fill, width=2):
    pts = []
    for i in range(6):
        angle = math.pi / 3 * i - math.pi / 6
        pts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    draw.polygon(pts, outline=fill, fill=None)
    # segundo hexágono menor
    pts2 = []
    for i in range(6):
        angle = math.pi / 3 * i - math.pi / 6
        pts2.append((cx + r*0.6 * math.cos(angle), cy + r*0.6 * math.sin(angle)))
    draw.polygon(pts2, outline=fill, fill=None)

draw_hexagon(draw, W - 100, H - 100, 40, ACCENT + (60,))
draw_hexagon(draw, 100, H - 130, 30, ACCENT + (40,))

# ── Salvar ──────────────────────────────────────────────────
out_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                        "img", "capa_ciencia_paisagem.png")
# Converter para RGB antes de salvar
final = Image.new("RGB", img.size, (0, 0, 0))
final.paste(img, mask=img.split()[3])
final.save(out_path, "PNG", dpi=(DPI, DPI))
print(f"✓ Capa salva em: {out_path}")
print(f"  Tamanho: {final.size[0]}×{final.size[1]} px")
