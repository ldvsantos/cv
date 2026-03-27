"""
Gera a capa para "Geotecnologias e SIG"
Tema: Mundo digital, matriz, radares, grids espaciais, tons de azul e cyan.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math

W, H = 1357, 1888
DPI = 150

BG_TOP = (10, 20, 35)
BG_BOT = (5, 10, 15)
ACCENT = (60, 180, 240)
WHITE = (255, 255, 255)

def get_font(name, size, bold=False):
    cands = [
        f"C:/Windows/Fonts/{name}bd.ttf" if bold else f"C:/Windows/Fonts/{name}.ttf",
        "C:/Windows/Fonts/arial.ttf"
    ]
    for path in cands:
        if os.path.exists(path): return ImageFont.truetype(path, size)
    return ImageFont.load_default()

img = Image.new("RGBA", (W, H), BG_TOP)
draw = ImageDraw.Draw(img)
for y in range(H):
    t = y / H
    r = int(BG_TOP[0] + (BG_BOT[0] - BG_TOP[0]) * t)
    g = int(BG_TOP[1] + (BG_BOT[1] - BG_TOP[1]) * t)
    b = int(BG_TOP[2] + (BG_BOT[2] - BG_TOP[2]) * t)
    draw.line([(0, y), (W, y)], fill=(r,g,b,255))

# Tema Gráfico: Grid de mapa / UI SIG
theme_img = Image.new("RGBA", (W, H), (0,0,0,0))
td = ImageDraw.Draw(theme_img)

# Grid
grid_step = 80
for x in range(0, W, grid_step):
    td.line([(x, 0), (x, H)], fill=(ACCENT[0], ACCENT[1], ACCENT[2], 15), width=1)
for y in range(0, H, grid_step):
    td.line([(0, y), (W, y)], fill=(ACCENT[0], ACCENT[1], ACCENT[2], 15), width=1)

# Nós de conexão / Polígonos de geoprocessamento
np.random.seed(99)
pts = []
for _ in range(30):
    px = np.random.randint(100, W-100)
    py = np.random.randint(400, 1200)
    # alinhar ao grid
    px = (px // grid_step) * grid_step
    py = (py // grid_step) * grid_step
    pts.append((px, py))
    td.ellipse([px-4, py-4, px+4, py+4], fill=ACCENT+(180,))
    td.ellipse([px-10, py-10, px+10, py+10], outline=ACCENT+(80,), width=1)

for i in range(len(pts)):
    for j in range(i+1, len(pts)):
        if math.dist(pts[i], pts[j]) < 250:
            td.line([pts[i], pts[j]], fill=ACCENT+(60,), width=2)
            
# Um polígono central grande simulando um lote/bacia
poly_pts = [pts[i] for i in [0, 2, 5, 8, 1, 0] if i < len(pts)]
if len(poly_pts) > 2:
    td.polygon(poly_pts, fill=(ACCENT[0], ACCENT[1], ACCENT[2], 25))

img = Image.alpha_composite(img, theme_img)

ov = Image.new("RGBA", (W, H), (0,0,0,0))
ImageDraw.Draw(ov).rectangle([0,0, W, 280], fill=(5, 10, 20, 200))
ImageDraw.Draw(ov).rectangle([0,1300, W, H], fill=(5, 5, 10, 220))
img = Image.alpha_composite(img, ov)

draw = ImageDraw.Draw(img)
def c_text(draw, txt, y, f, fill):
    w = f.getbbox(txt)[2] - f.getbbox(txt)[0]
    draw.text(((W-w)//2, y), txt, font=f, fill=fill)

c_text(draw, "GEOTECNOLOGIAS", 75, get_font("calibri", 110, True), WHITE)
c_text(draw, "E SIG", 180, get_font("calibri", 110, True), ACCENT)
draw.line([(W//2 - 250, 310), (W//2 + 250, 310)], fill=ACCENT+(150,), width=2)

sub_bg = Image.new("RGBA", (W, 140), (0,0,0,0))
ImageDraw.Draw(sub_bg).rounded_rectangle([W//2-480, 5, W//2+480, 135], radius=8, fill=(10,30,40, 190))
img.paste(Image.alpha_composite(Image.new("RGBA", (W, 140), (0,0,0,0)), sub_bg), (0, 340), sub_bg)
draw = ImageDraw.Draw(img)
c_text(draw, "Fundamentos, Análise Espacial e", 355, get_font("calibri", 46), (220,240,255))
c_text(draw, "Aplicações Ambientais", 410, get_font("calibri", 46), (220,240,255))

draw.line([(W//2 - 350, 1420), (W//2 + 350, 1420)], fill=ACCENT+(120,), width=2)
c_text(draw, "Luiz Diego Vidal Santos", 1470, get_font("calibri", 54, True), WHITE)
c_text(draw, "Universidade Estadual de Feira de Santana", 1545, get_font("calibri", 36), (180,200,210))
c_text(draw, "2026  •  CC BY-NC-SA 4.0", 1610, get_font("calibri", 30), (180,200,210))

out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "img", "capa_geotecnologias_sig.png"))
final = Image.new("RGB", img.size, (0,0,0))
final.paste(img, mask=img.split()[3])
final.save(out, "PNG", dpi=(DPI, DPI))
print(f"Salvo: {out}")
