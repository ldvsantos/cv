"""
Gera a capa para "Propriedade Intelectual e Inovação no Agronegócio"
Tema: Inovação, patentes, redes de conhecimento, tons de roxo/índigo.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math

W, H = 1357, 1888
DPI = 150

BG_TOP = (25, 10, 40)
BG_BOT = (10, 5, 15)
ACCENT = (180, 120, 255)
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

np.random.seed(77)
# Hexágonos concêntricos brilhantes (Inovação / Patentes / Moléculas)
cx, cy = W//2, 800
for r in range(150, 600, 80):
    pts = []
    for i in range(6):
        ang = math.pi/3 * i - math.pi/2
        pts.append((cx + r*math.cos(ang), cy + r*math.sin(ang)))
    td.polygon(pts, outline=(ACCENT[0], ACCENT[1], ACCENT[2], 50), width=3)
    for p in pts:
        td.ellipse([p[0]-6, p[1]-6, p[0]+6, p[1]+6], fill=ACCENT+(150,))

# Linhas de transferência (tech transfer)
for _ in range(50):
    x1 = np.random.randint(50, W-50)
    y1 = np.random.randint(400, 1200)
    x2 = x1 + np.random.randint(-200, 200)
    y2 = y1 + np.random.randint(100, 300)
    td.line([(x1, y1), (x2, y2)], fill=(200, 150, 255, 30), width=1)

img = Image.alpha_composite(img, theme_img.filter(ImageFilter.GaussianBlur(radius=0.5)))

ov = Image.new("RGBA", (W, H), (0,0,0,0))
ImageDraw.Draw(ov).rectangle([0,0, W, 280], fill=(15, 5, 25, 200))
ImageDraw.Draw(ov).rectangle([0,1300, W, H], fill=(5, 0, 10, 220))
img = Image.alpha_composite(img, ov)

draw = ImageDraw.Draw(img)
def c_text(draw, txt, y, f, fill):
    w = f.getbbox(txt)[2] - f.getbbox(txt)[0]
    draw.text(((W-w)//2, y), txt, font=f, fill=fill)

c_text(draw, "PROPRIEDADE INTELECTUAL", 75, get_font("calibri", 92, True), WHITE)
c_text(draw, "E INOVAÇÃO", 180, get_font("calibri", 110, True), ACCENT)
draw.line([(W//2 - 250, 310), (W//2 + 250, 310)], fill=ACCENT+(150,), width=2)

sub_bg = Image.new("RGBA", (W, 140), (0,0,0,0))
ImageDraw.Draw(sub_bg).rounded_rectangle([W//2-500, 5, W//2+500, 135], radius=10, fill=(20,10,30, 180))
img.paste(Image.alpha_composite(Image.new("RGBA", (W, 140), (0,0,0,0)), sub_bg), (0, 340), sub_bg)
draw = ImageDraw.Draw(img)
c_text(draw, "Fundamentos, Proteção e Transferência", 355, get_font("calibri", 46), (230,220,255))
c_text(draw, "de Tecnologia no Agro", 410, get_font("calibri", 46), (230,220,255))

draw.line([(W//2 - 350, 1420), (W//2 + 350, 1420)], fill=ACCENT+(120,), width=2)
c_text(draw, "Luiz Diego Vidal Santos", 1470, get_font("calibri", 54, True), WHITE)
c_text(draw, "Universidade Estadual de Feira de Santana", 1545, get_font("calibri", 36), (190,180,210))
c_text(draw, "2026  •  CC BY-NC-SA 4.0", 1610, get_font("calibri", 30), (190,180,210))

out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "img", "capa_pi.png"))
final = Image.new("RGB", img.size, (0,0,0))
final.paste(img, mask=img.split()[3])
final.save(out, "PNG", dpi=(DPI, DPI))
print(f"Salvo: {out}")
