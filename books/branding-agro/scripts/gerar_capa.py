"""
Gera a capa para "Gestão de Branding no Agro"
Tema: Conexão, mercado, cores quentes do campo (laranja, amarelo) e moderno.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math

W, H = 1357, 1888
DPI = 150

BG_TOP = (45, 15, 10)
BG_BOT = (15, 5, 5)
ACCENT = (240, 160, 50)
WHITE = (255, 255, 255)
SUBTLE = (200, 180, 170)

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

# Tema Gráfico: Círculos de influência e campos arados abstratos (branding/expansão)
theme_img = Image.new("RGBA", (W, H), (0,0,0,0))
td = ImageDraw.Draw(theme_img)

np.random.seed(33)
cx, cy = int(W*0.8), int(H*0.7)
for r in range(100, 1800, 80):
    w = max(1, int(15 - r/100))
    alpha = max(10, 120 - int(r/15))
    td.arc([cx-r, cy-r, cx+r, cy+r], 90, 360, fill=(ACCENT[0], ACCENT[1], ACCENT[2], alpha), width=w)

# raios estilo sol/mercado
for angle_deg in range(180, 360, 15):
    rad = math.radians(angle_deg)
    length = 2000
    x2 = cx + math.cos(rad) * length
    y2 = cy + math.sin(rad) * length
    td.line([(cx, cy), (int(x2), int(y2))], fill=(255,200,100, 15), width=2)

img = Image.alpha_composite(img, theme_img.filter(ImageFilter.GaussianBlur(radius=1.0)))

ov = Image.new("RGBA", (W, H), (0,0,0,0))
ImageDraw.Draw(ov).rectangle([0,0, W, 300], fill=(20, 5, 0, 180))
ImageDraw.Draw(ov).rectangle([0,1300, W, H], fill=(10, 5, 5, 200))
img = Image.alpha_composite(img, ov)

draw = ImageDraw.Draw(img)
f_t = get_font("calibri", 110, True)
f_st = get_font("calibri", 46)

def c_text(draw, txt, y, f, fill):
    w = f.getbbox(txt)[2] - f.getbbox(txt)[0]
    draw.text(((W-w)//2, y), txt, font=f, fill=fill)

# Textos
c_text(draw, "GESTÃO DE BRANDING", 75, f_t, WHITE)
c_text(draw, "NO AGRO", 180, f_t, ACCENT)

draw.line([(W//2 - 200, 310), (W//2 + 200, 310)], fill=ACCENT+(150,), width=2)

sub_bg = Image.new("RGBA", (W, 140), (0,0,0,0))
ImageDraw.Draw(sub_bg).rounded_rectangle([W//2-450, 5, W//2+450, 135], radius=15, fill=(40,20,10, 180))
img.paste(Image.alpha_composite(Image.new("RGBA", (W, 140), (0,0,0,0)), sub_bg), (0, 350), sub_bg)

draw = ImageDraw.Draw(img)
c_text(draw, "Estratégias de Marca para o", 365, f_st, (255,240,230))
c_text(draw, "Agronegócio Brasileiro", 420, f_st, (255,240,230))

draw.line([(W//2 - 350, 1420), (W//2 + 350, 1420)], fill=ACCENT+(120,), width=2)
c_text(draw, "Luiz Diego Vidal Santos", 1470, get_font("calibri", 54, True), WHITE)
c_text(draw, "Universidade Estadual de Feira de Santana", 1545, get_font("calibri", 36), SUBTLE)
c_text(draw, "2026  •  CC BY-NC-SA 4.0", 1610, get_font("calibri", 30), SUBTLE)

out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "img", "capa_branding.png"))
final = Image.new("RGB", img.size, (0,0,0))
final.paste(img, mask=img.split()[3])
final.save(out, "PNG", dpi=(DPI, DPI))
print(f"Salvo: {out}")
