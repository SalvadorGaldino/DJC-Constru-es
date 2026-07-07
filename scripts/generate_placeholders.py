"""
Gera imagens provisórias para a DJC Construções.
Estilo consistente com a identidade visual do site (fundo escuro industrial + linhas douradas
de andaime), com aviso textual claro de que são placeholders — evita passar a impressão de
fotos reais de obras que não existem.
"""
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG  = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

DARK_1 = (10, 10, 10)
DARK_2 = (28, 28, 28)
GOLD   = (201, 168, 76)
MUTED  = (138, 138, 138)

def vertical_gradient(size, top, bottom):
    w, h = size
    base = Image.new("RGB", size, top)
    draw = ImageDraw.Draw(base)
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    return base

def add_scaffold_lines(img, seed, density=1.0):
    """Linhas verticais/horizontais douradas finas, opacidade baixa — mesmo motivo do hero do site."""
    w, h = img.size
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    rnd = random.Random(seed)
    n_vert = max(3, int(w / 140 * density))
    for i in range(n_vert):
        x = int(w * (i + 0.5) / n_vert + rnd.randint(-25, 25))
        alpha = rnd.randint(14, 26)
        draw.line([(x, 0), (x, h)], fill=(*GOLD, alpha), width=2)
    n_horiz = max(1, int(h / 180 * density))
    for i in range(n_horiz):
        y = int(h * (i + 0.5) / n_horiz + rnd.randint(-15, 15))
        alpha = rnd.randint(10, 18)
        draw.line([(0, y), (w, y)], fill=(*GOLD, alpha), width=2)
    return Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")

def add_vignette(img):
    w, h = img.size
    vig = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(vig)
    draw.ellipse([-w*0.25, -h*0.25, w*1.25, h*1.25], fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(w * 0.08))
    dark = Image.new("RGB", (w, h), DARK_1)
    return Image.composite(img, dark, vig)

def draw_building_icon(img, cx, cy, scale=1.0):
    """Ícone simples de prédio/construção, no mesmo espírito dos ícones SVG do site."""
    draw = ImageDraw.Draw(img, "RGBA")
    s = scale
    pts = [
        (cx - 90*s, cy + 70*s), (cx - 90*s, cy - 10*s), (cx*1 - 30*s, cy - 70*s),
        (cx + 30*s, cy - 10*s), (cx + 30*s, cy + 70*s),
    ]
    draw.line(pts, fill=(*GOLD, 140), width=int(5*s), joint="curve")
    draw.line([(cx - 30*s, cy + 70*s), (cx - 30*s, cy + 15*s), (cx + 30*s, cy + 15*s)], fill=(*GOLD, 140), width=int(5*s), joint="curve")
    return img

def centered_text(img, lines, y_center, main=True):
    draw = ImageDraw.Draw(img, "RGBA")
    w, h = img.size
    total_h = 0
    rendered = []
    for text, font_path, size, color in lines:
        font = ImageFont.truetype(font_path, size)
        bbox = draw.textbbox((0, 0), text, font=font)
        tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
        rendered.append((text, font, tw, th, color))
        total_h += th + 10
    y = y_center - total_h / 2
    for text, font, tw, th, color in rendered:
        draw.text((w/2 - tw/2, y), text, font=font, fill=color)
        y += th + 10
    return img

def make_placeholder(path, size, label, seed, sub="Imagem provisória — substituir por foto real"):
    w, h = size
    img = vertical_gradient(size, DARK_2, DARK_1)
    img = add_scaffold_lines(img, seed, density=1.2)
    img = add_vignette(img)
    icon_scale = min(w, h) / 420
    draw_building_icon(img, w/2, h/2 - min(w,h)*0.12, scale=icon_scale)
    lines = [
        (label.upper(), FONT_BOLD, max(18, int(min(w,h)*0.075)), (*GOLD, 235)),
        (sub, FONT_REG, max(11, int(min(w,h)*0.032)), (*MUTED, 220)),
    ]
    img = centered_text(img, lines, h/2 + min(w,h)*0.22)
    img.save(path, quality=87)
    print(f"OK  {path}  {size}")

# ---- Portfólio (obras) ----
make_placeholder("img/obra1.jpg", (600, 560), "Construção residencial", seed=1)
make_placeholder("img/obra2.jpg", (600, 280), "Reforma e acabamento", seed=2)
make_placeholder("img/obra3.jpg", (600, 280), "Estrutura e cobertura", seed=3)
make_placeholder("img/obra4.jpg", (1200, 280), "Área externa e piscina", seed=4)
make_placeholder("img/obra5.jpg", (600, 280), "Alvenaria estrutural", seed=5)

# ---- Sobre nós ----
make_placeholder("img/sobre.jpg", (600, 750), "Equipe DJC em obra", seed=6)

# ---- OG Image (preview de compartilhamento) ----
def make_og_image(path):
    w, h = 1200, 630
    img = vertical_gradient((w, h), DARK_2, DARK_1)
    img = add_scaffold_lines(img, seed=99, density=1.0)
    img = add_vignette(img)
    draw_building_icon(img, w/2, h/2 - 60, scale=1.6)
    lines = [
        ("DJC CONSTRUÇÕES", FONT_BOLD, 64, (*GOLD, 240)),
        ("Construindo com ética e qualidade", FONT_REG, 28, (245, 243, 238, 230)),
        ("Litoral do Paraná", FONT_REG, 22, (*MUTED, 220)),
    ]
    img = centered_text(img, lines, h/2 + 150)
    img.save(path, quality=90)
    print(f"OK  {path}  {(w,h)}")

make_og_image("img/og-image.jpg")
