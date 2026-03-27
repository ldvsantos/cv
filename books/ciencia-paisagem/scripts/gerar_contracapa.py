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

# ---- Texto da Contracapa ----
font_bio = get_font("calibri", 48)

# Texto de sinopse/resumo
sinopse = [
    "Livro-texto sobre Análise da Paisagem,",
    "integrando ecologia da paisagem, métricas espaciais,",
    "sensoriamento remoto, geoprocessamento e",
    "planejamento territorial para a gestão",
    "sustentável de paisagens tropicais."
]

y_text = 400
for linha in sinopse:
    bbox = font_bio.getbbox(linha)
    tw = bbox[2] - bbox[0]
    # draw.text(((W - tw) // 2, y_text), linha, font=font_bio, fill=WHITE)
    y_text += 70

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
                        "img", "contracapa_ciencia_paisagem.png")
barcode_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                        "img", "978-65-02-02072-2.jpeg")

# Adicionar código de barras no canto inferior direito/centralizado
if os.path.exists(barcode_path):
    barcode = Image.open(barcode_path).convert("RGBA")
    # Redimensionar o código de barras pra ficar de bom tamanho
    bw, bh = barcode.size
    target_bw = 360 # largura do código de barras na capa
    target_bh = int(bh * target_bw / bw)
    barcode = barcode.resize((target_bw, target_bh), Image.Resampling.LANCZOS)
    
    # Criar um retângulo branco por trás do código de barras + texto para dar contraste
    pad = 30
    draw.rectangle([
        (W - target_bw - pad*3, H - target_bh - pad*4 - 100),
        (W - pad, H - pad - 50)
    ], fill=(255, 255, 255, 255))
    
    # Colar o barcode
    img.paste(barcode, (W - target_bw - pad*2, H - target_bh - pad*2 - 50), mask=barcode.split()[3] if len(barcode.split()) == 4 else None)
    
    # Escrever o ISBN acima do barcode
    font_isbn = get_font("calibri", 34, bold=True)
    isbn_text = "ISBN 978-65-02-02072-2"
    bbox_isbn = font_isbn.getbbox(isbn_text)
    tw_isbn = bbox_isbn[2] - bbox_isbn[0]
    draw.text((W - target_bw - pad*2 + (target_bw - tw_isbn)//2, H - target_bh - pad*2 - 110), isbn_text, font=font_isbn, fill=(20, 20, 20, 255))

# Converter para RGB antes de salvar
final = Image.new("RGB", img.size, (0, 0, 0))
final.paste(img, mask=img.split()[3])
final.save(out_path, "PNG", dpi=(DPI, DPI))
print(f"✓ Contracapa salva em: {out_path}")
print(f"  Tamanho: {final.size[0]}×{final.size[1]} px")
