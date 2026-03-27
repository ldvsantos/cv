"""
Gera a capa para "Análise de Dados Ambientais"
Tema: Dispersão de dados, estatística, modelagem, tons escuros e magenta/cyan.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math, random

W, H = 1357, 1888
DPI = 150

BG_TOP = (20, 20, 25)
BG_BOT = (5, 10, 15)
ACCENT = (220, 50, 110)
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

theme_img = Image.new("RGBA", (W, H), (0,0,0,0))
td = ImageDraw.Draw(theme_img)

np.random.seed(42)
# Gráfico de dispersão (Scatter plot estilizado)
points = []
for _ in range(400):
    x = np.random.normal(W/2, 350)
    y = np.random.normal(800, 300)
    if 50 < x < W-50 and 300 < y < 1200:
        r_pt = random.uniform(2, 9)
        alpha = random.randint(50, 200)
        td.ellipse([x-r_pt, y-r_pt, x+r_pt, y+r_pt], fill=ACCENT+(alpha,))
        points.append((x, y))

# Linha de tendência pseudo-estatística
pts_sorted = sorted(points, key=lambda p: p[0])
if pts_sorted:
    trend_pts = []
    for x_step in range(100, W-100, 100):
        # media de Y local
        local_y = [p[1] for p in pts_sorted if abs(p[0] - x_step) < 150]
        if local_y:
            trend_pts.append((x_step, sum(local_y)/len(local_y)))
    
    if len(trend_pts) > 2:
        for i in range(len(trend_pts)-1):
            td.line([trend_pts[i], trend_pts[i+1]], fill=(100, 200, 255, 150), width=4)

img = Image.alpha_composite(img, theme_img.filter(ImageFilter.GaussianBlur(radius=0.7)))

ov = Image.new("RGBA", (W, H), (0,0,0,0))
ImageDraw.Draw(ov).rectangle([0,0, W, 280], fill=(10, 10, 15, 200))
ImageDraw.Draw(ov).rectangle([0,1300, W, H], fill=(5, 5, 5, 220))
img = Image.alpha_composite(img, ov)

draw = ImageDraw.Draw(img)
def c_text(draw, txt, y, f, fill):
    w = f.getbbox(txt)[2] - f.getbbox(txt)[0]
    draw.text(((W-w)//2, y), txt, font=f, fill=fill)

c_text(draw, "ANÁLISE DE DADOS", 75, get_font("calibri", 110, True), WHITE)
c_text(draw, "AMBIENTAIS", 180, get_font("calibri", 110, True), ACCENT)
draw.line([(W//2 - 250, 310), (W//2 + 250, 310)], fill=ACCENT+(150,), width=2)

sub_bg = Image.new("RGBA", (W, 140), (0,0,0,0))
ImageDraw.Draw(sub_bg).rounded_rectangle([W//2-480, 5, W//2+480, 135], radius=10, fill=(25,10,20, 180))
img.paste(Image.alpha_composite(Image.new("RGBA", (W, 140), (0,0,0,0)), sub_bg), (0, 340), sub_bg)
draw = ImageDraw.Draw(img)
c_text(draw, "Estatística, Modelagem e", 355, get_font("calibri", 46), (255,220,230))
c_text(draw, "Métodos Quantitativos", 410, get_font("calibri", 46), (255,220,230))

draw.line([(W//2 - 350, 1420), (W//2 + 350, 1420)], fill=ACCENT+(120,), width=2)
c_text(draw, "Luiz Diego Vidal Santos", 1470, get_font("calibri", 54, True), WHITE)
c_text(draw, "Universidade Estadual de Feira de Santana", 1545, get_font("calibri", 36), (190,190,200))
c_text(draw, "2026  •  CC BY-NC-SA 4.0", 1610, get_font("calibri", 30), (190,190,200))

out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "img", "capa_analise_dados_ambientais.png"))
final = Image.new("RGB", img.size, (0,0,0))
final.paste(img, mask=img.split()[3])
final.save(out, "PNG", dpi=(DPI, DPI))
print(f"Salvo: {out}")
