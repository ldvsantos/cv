import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math, random

# ── Configurações Globais ──────────────────────────────────
W, H = 1357, 1888
DPI = 150
WHITE = (255, 255, 255)
LIGHT = (220, 235, 225)
SUBTLE = (180, 210, 190)

def get_font(name, size, bold=False):
    candidates = []
    if bold:
        candidates = [
            f"C:/Windows/Fonts/{name}bd.ttf",
            f"C:/Windows/Fonts/{name}-Bold.ttf",
            f"C:/Windows/Fonts/{name}b.ttf",
        ]
    candidates += [f"C:/Windows/Fonts/{name}.ttf"]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size)

font_title   = get_font("calibri", 110, bold=True)
font_title_s = get_font("calibri", 92, bold=True)
font_sub     = get_font("calibri", 46)
font_author  = get_font("calibri", 54, bold=True)
font_info    = get_font("calibri", 36)
font_small   = get_font("calibri", 30)

def draw_spaced_text(draw, text, x_center, y, font, fill, spacing=8):
    total_w = 0
    char_widths = []
    for ch in text:
        bbox = font.getbbox(ch)
        cw = bbox[2] - bbox[0]
        char_widths.append(cw)
        total_w += cw + spacing
    total_w -= spacing
    x = x_center - total_w // 2
    for ch, cw in zip(text, char_widths):
        draw.text((x, y), ch, font=font, fill=fill)
        x += cw + spacing

def hexagon(draw, cx, cy, r, fill):
    pts = []
    for i in range(6):
        angle = math.pi / 3 * i - math.pi / 6
        pts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    draw.polygon(pts, outline=fill, fill=None)
    pts2 = []
    for i in range(6):
        angle = math.pi / 3 * i - math.pi / 6
        pts2.append((cx + r*0.6 * math.cos(angle), cy + r*0.6 * math.sin(angle)))
    draw.polygon(pts2, outline=fill, fill=None)

BOOKS = [
    {
        "id": "bioengenharia",
        "folder": "bioengenharia-solos",
        "file": "capa_bioengenharia_de_solos.png",
        "title": ["BIOENGENHARIA", "DE SOLOS"],
        "sub": ["Fundamentos, Técnicas e Soluções", "Baseadas na Natureza"],
        "bg_top": (45, 25, 10),
        "bg_bot": (20, 35, 15),
        "accent": (140, 190, 80),
        "theme": "roots"
    },
    {
        "id": "branding",
        "folder": "branding-agro",
        "file": "capa_branding.png",
        "title": ["GESTÃO DE BRANDING", "NO AGRO"],
        "sub": ["Estratégias de Marca para o", "Agronegócio Brasileiro"],
        "bg_top": (40, 15, 15),
        "bg_bot": (10, 10, 10),
        "accent": (240, 160, 50),
        "theme": "growth"
    },
    {
        "id": "geotec",
        "folder": "geotecnologias-sig",
        "file": "capa_geotecnologias_sig.png",
        "title": ["GEOTECNOLOGIAS", "E SIG"],
        "sub": ["Fundamentos, Análise Espacial e", "Aplicações Ambientais"],
        "bg_top": (10, 25, 45),
        "bg_bot": (5, 10, 20),
        "accent": (60, 180, 220),
        "theme": "digital_grid"
    },
    {
        "id": "pi",
        "folder": "pi",
        "file": "capa_pi.png",
        "title": ["PROPRIEDADE INTELECTUAL", "E INOVAÇÃO"],
        "sub": ["Fundamentos, Proteção e Transferência", "de Tecnologia no Agro"],
        "bg_top": (25, 10, 35),
        "bg_bot": (10, 5, 15),
        "accent": (160, 100, 240),
        "theme": "network"
    },
    {
        "id": "analise",
        "folder": "analise_dados",
        "file": "capa_analise_dados_ambientais.png",
        "title": ["ANÁLISE DE DADOS", "AMBIENTAIS"],
        "sub": ["Estatística, Modelagem e", "Métodos Quantitativos"],
        "bg_top": (20, 20, 20),
        "bg_bot": (5, 15, 25),
        "accent": (220, 80, 120),
        "theme": "scatter"
    }
]

def render_bg_effect(theme, bg_layer, accent):
    draw = ImageDraw.Draw(bg_layer)
    np.random.seed(42)
    
    if theme == "roots":
        # Wavy vertical lines converging like roots
        for _ in range(40):
            x_start = np.random.randint(-200, W+200)
            pts = []
            x = x_start
            for y in range(300, 1200, 30):
                x += math.sin(y*0.01 + x_start) * 20
                pts.append((x, y))
            if len(pts)>1:
                draw.line(pts, fill=accent+(40,), width=random.choice([1, 2, 4]))
                
    elif theme == "growth":
        # Fields/sun rays, arcs and dynamic polygons overlaying
        for _ in range(15):
            r = np.random.randint(200, 900)
            cx, cy = W/2, 1300
            draw.arc([cx-r, cy-r, cx+r, cy+r], 180, 360, fill=accent+(30,), width=3)
            
    elif theme == "digital_grid":
        # Tech nodes / SIG radar circles
        for x in range(100, W, 120):
            for y in range(400, 1200, 120):
                if random.random() > 0.4:
                    draw.point((x, y), fill=accent+(100,))
                    draw.ellipse([x-2, y-2, x+2, y+2], fill=accent+(60,))
                if random.random() > 0.8:
                    draw.line([(x,y), (x+120, y)], fill=accent+(30,), width=1)
                if random.random() > 0.8:
                    draw.line([(x,y), (x, y+120)], fill=accent+(30,), width=1)
                    
    elif theme == "network":
        # Nodes and brain-like networks
        nodes = [(random.randint(100, W-100), random.randint(400, 1100)) for _ in range(50)]
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                dist = math.dist(nodes[i], nodes[j])
                if dist < 200:
                    draw.line([nodes[i], nodes[j]], fill=accent+(int(60 - dist*0.3),), width=2)
            draw.ellipse([nodes[i][0]-4, nodes[i][1]-4, nodes[i][0]+4, nodes[i][1]+4], fill=accent+(150,))
            
    elif theme == "scatter":
        # Data points / scatter plot
        for _ in range(300):
            x = np.random.normal(W/2, 350)
            y = np.random.normal(800, 200)
            r = random.uniform(2, 8)
            draw.ellipse([x-r, y-r, x+r, y+r], fill=accent+(random.randint(40,150),))


# Gerar para todos
base_dir = os.path.dirname(os.path.abspath(__file__))

for b in BOOKS:
    # ── Fundo
    img = Image.new("RGBA", (W, H), b["bg_top"])
    draw = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        t2 = t*t*(3 - 2*t)
        ro = int(b["bg_top"][0] + (b["bg_bot"][0] - b["bg_top"][0]) * t2)
        go = int(b["bg_top"][1] + (b["bg_bot"][1] - b["bg_top"][1]) * t2)
        bo = int(b["bg_top"][2] + (b["bg_bot"][2] - b["bg_top"][2]) * t2)
        draw.line([(0, y), (W, y)], fill=(ro, go, bo, 255))
        
    # ── Tema
    theme_layer = Image.new("RGBA", (W, H), (0,0,0,0))
    render_bg_effect(b["theme"], theme_layer, b["accent"])
    theme_layer = theme_layer.filter(ImageFilter.GaussianBlur(radius=1.5))
    img = Image.alpha_composite(img, theme_layer)
    
    # ── Vinhetas (escurecer bordas superior/inferior)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    for y in range(0, 270):
        ov_draw.line([(0, y), (W, y)], fill=(0, 0, 0, int(90 * (1 - y/270))))
    for y in range(1200, H):
        ov_draw.line([(0, y), (W, y)], fill=(0, 0, 0, int(70 * (y - 1200)/(H - 1200))))
    img = Image.alpha_composite(img, overlay)
    
    draw = ImageDraw.Draw(img)
    
    # ── Titulo
    y_t = 80
    for i, t_line in enumerate(b["title"]):
        fnt = font_title if len(t_line) < 15 else font_title_s
        draw_spaced_text(draw, t_line, W//2, y_t, fnt, WHITE if i == 0 else b["accent"], spacing=14)
        y_t += 95
        
    line_y = 320
    draw.line([(W//2 - 250, line_y), (W//2 + 250, line_y)], fill=b["accent"] + (140,), width=2)
    
    # ── Subtítulo
    sub_y = 360
    sub_bg = Image.new("RGBA", (W, 130), (0, 0, 0, 0))
    ImageDraw.Draw(sub_bg).rounded_rectangle([(W//2 - 480, 5), (W//2 + 480, 125)], radius=12, fill=(10, 20, 20, 140))
    img.paste(Image.alpha_composite(Image.new("RGBA", (W, 130), (0,0,0,0)), sub_bg), (0, sub_y), sub_bg)
    
    draw = ImageDraw.Draw(img)
    y_sub = sub_y + 15
    for s_line in b["sub"]:
        bbox = font_sub.getbbox(s_line)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw)//2, y_sub), s_line, font=font_sub, fill=LIGHT)
        y_sub += 53
        
    # ── Autor (Base)
    sep_y = 1420
    draw.line([(W//2 - 350, sep_y), (W//2 + 350, sep_y)], fill=b["accent"] + (120,), width=2)
    author = "Luiz Diego Vidal Santos"
    bbox_a = font_author.getbbox(author)
    draw.text(((W - (bbox_a[2] - bbox_a[0])) // 2, 1470), author, font=font_author, fill=WHITE)
    affil = "Universidade Estadual de Feira de Santana"
    bbox_af = font_info.getbbox(affil)
    draw.text(((W - (bbox_af[2] - bbox_af[0])) // 2, 1545), affil, font=font_info, fill=SUBTLE)
    year_lic = "2026  •  CC BY-NC-SA 4.0"
    bbox_yl = font_small.getbbox(year_lic)
    draw.text(((W - (bbox_yl[2] - bbox_yl[0])) // 2, 1610), year_lic, font=font_small, fill=SUBTLE)
    
    # Detalhes
    draw.rectangle([(80, 90), (86, 290)], fill=b["accent"] + (100,))
    hexagon(draw, W - 100, H - 100, 40, b["accent"] + (60,))
    hexagon(draw, 100, H - 130, 30, b["accent"] + (40,))
    
    # ── Salvar
    out_dir = os.path.join(base_dir, b["folder"], "img")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, b["file"])
    
    final = Image.new("RGB", img.size, (0, 0, 0))
    final.paste(img, mask=img.split()[3])
    final.save(out_path, "PNG", dpi=(DPI, DPI))
    print(f"✓ {b['id']} -> {out_path}")

print("Todas as capas geradas com sucesso.")
