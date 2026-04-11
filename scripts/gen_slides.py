"""
Gerador de 5 slides profissionais 1920x1080 — Claude Code Deck
Design: dark gradient + orange stripe + cyan/purple text + glassmorphism
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, os, sys

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "_mapas", "slides")
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1920, 1080

# ── Paleta ────────────────────────────────────────────────────────────────────
BG_TOP       = (8, 8, 20)
BG_BOT       = (18, 6, 36)
ORANGE       = (255, 120, 30)
ORANGE_GLOW  = (255, 160, 60, 60)
CYAN         = (0, 230, 255)
PURPLE       = (180, 80, 255)
WHITE        = (255, 255, 255)
GLASS_FILL   = (255, 255, 255, 18)
GLASS_BORDER = (255, 255, 255, 50)
GLASS_DARK   = (20, 10, 40, 160)

# ── Helpers ───────────────────────────────────────────────────────────────────
def load_font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/seguisb.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def gradient_bg(draw):
    for y in range(H):
        t = y / H
        r = int(BG_TOP[0] + (BG_BOT[0] - BG_TOP[0]) * t)
        g = int(BG_TOP[1] + (BG_BOT[1] - BG_TOP[1]) * t)
        b = int(BG_TOP[2] + (BG_BOT[2] - BG_TOP[2]) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

def orange_stripe(img, y=120, thickness=4):
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    # glow blur
    for i in range(20, 0, -1):
        alpha = int(80 * (1 - i / 20))
        d.rectangle([0, y - i, W, y + thickness + i], fill=(*ORANGE, alpha))
    d.rectangle([0, y, W, y + thickness], fill=(*ORANGE, 230))
    img = Image.alpha_composite(img.convert("RGBA"), ov)
    return img

def glass_rect(img, x1, y1, x2, y2, radius=20):
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=GLASS_DARK)
    d.rounded_rectangle([x1, y1, x2, y2], radius=radius, outline=GLASS_BORDER, width=1)
    img = Image.alpha_composite(img.convert("RGBA"), ov)
    return img

def centered_text(draw, text, y, font, color, shadow=True):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2
    if shadow:
        draw.text((x + 2, y + 2), text, font=font, fill=(0, 0, 0, 120))
    draw.text((x, y), text, font=font, fill=color)
    return bbox[3] - bbox[1]

def gradient_text(img, text, y, size, bold=False):
    """Render text with cyan-to-purple horizontal gradient."""
    font = load_font(size, bold)
    tmp = Image.new("RGBA", img.size, (0, 0, 0, 0))
    td = ImageDraw.Draw(tmp)
    bbox = td.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (W - tw) // 2
    # draw char by char with gradient color
    cx = x
    for ch in text:
        cb = td.textbbox((0, 0), ch, font=font)
        cw = cb[2] - cb[0]
        t = (cx - x) / max(tw, 1)
        r = int(CYAN[0] + (PURPLE[0] - CYAN[0]) * t)
        g = int(CYAN[1] + (PURPLE[1] - CYAN[1]) * t)
        b = int(CYAN[2] + (PURPLE[2] - CYAN[2]) * t)
        td.text((cx, y), ch, font=font, fill=(r, g, b, 255))
        cx += cw
    img = Image.alpha_composite(img.convert("RGBA"), tmp)
    return img, th

def noise_bg(img, intensity=8):
    """Add subtle noise for depth."""
    import random
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    pix = ov.load()
    for _ in range(W * H // 40):
        x = random.randint(0, W - 1)
        y = random.randint(0, H - 1)
        v = random.randint(0, intensity)
        pix[x, y] = (v, v, v, v)
    return Image.alpha_composite(img.convert("RGBA"), ov)

def dot_grid(img, spacing=60, color=(255,255,255,12)):
    ov = Image.new("RGBA", img.size, (0,0,0,0))
    d = ImageDraw.Draw(ov)
    for x in range(0, W, spacing):
        for y in range(0, H, spacing):
            d.ellipse([x-1,y-1,x+1,y+1], fill=color)
    return Image.alpha_composite(img.convert("RGBA"), ov)

def corner_accents(img):
    ov = Image.new("RGBA", img.size, (0,0,0,0))
    d = ImageDraw.Draw(ov)
    # top-left
    d.line([(60,60),(160,60)], fill=(*ORANGE, 200), width=3)
    d.line([(60,60),(60,160)], fill=(*ORANGE, 200), width=3)
    # top-right
    d.line([(W-160,60),(W-60,60)], fill=(*ORANGE, 200), width=3)
    d.line([(W-60,60),(W-60,160)], fill=(*ORANGE, 200), width=3)
    # bottom-left
    d.line([(60,H-60),(160,H-60)], fill=(*ORANGE, 200), width=3)
    d.line([(60,H-160),(60,H-60)], fill=(*ORANGE, 200), width=3)
    # bottom-right
    d.line([(W-160,H-60),(W-60,H-60)], fill=(*ORANGE, 200), width=3)
    d.line([(W-60,H-160),(W-60,H-60)], fill=(*ORANGE, 200), width=3)
    return Image.alpha_composite(img.convert("RGBA"), ov)

def pill_tag(img, text, x, y, font_size=24):
    font = load_font(font_size)
    tmp_d = ImageDraw.Draw(Image.new("RGBA", (1,1)))
    bb = tmp_d.textbbox((0,0), text, font=font)
    tw, th = bb[2]-bb[0], bb[3]-bb[1]
    pad = 16
    ov = Image.new("RGBA", img.size, (0,0,0,0))
    d = ImageDraw.Draw(ov)
    d.rounded_rectangle([x, y, x+tw+pad*2, y+th+pad], radius=20,
                         fill=(*ORANGE, 200))
    d.text((x+pad, y+pad//2), text, font=font, fill=(0,0,0,230))
    return Image.alpha_composite(img.convert("RGBA"), ov)

def progress_bar(img, pct, y=H-40, height=4):
    ov = Image.new("RGBA", img.size, (0,0,0,0))
    d = ImageDraw.Draw(ov)
    margin = 80
    full_w = W - margin*2
    d.rectangle([margin, y, margin+full_w, y+height], fill=(255,255,255,20))
    bar_w = int(full_w * pct)
    for i in range(bar_w):
        t = i / max(bar_w, 1)
        r = int(CYAN[0] + (ORANGE[0] - CYAN[0]) * t)
        g = int(CYAN[1] + (ORANGE[1] - CYAN[1]) * t)
        b = int(CYAN[2] + (ORANGE[2] - CYAN[2]) * t)
        d.rectangle([margin+i, y, margin+i+1, y+height], fill=(r,g,b,220))
    return Image.alpha_composite(img.convert("RGBA"), ov)

def footer(img, slide_num, total=5, label="ForYou Code · Jarvis"):
    font = load_font(22)
    ov = Image.new("RGBA", img.size, (0,0,0,0))
    d = ImageDraw.Draw(ov)
    d.text((80, H-50), label, font=font, fill=(255,255,255,90))
    num_text = f"{slide_num}/{total}"
    bb = d.textbbox((0,0), num_text, font=font)
    d.text((W-80-(bb[2]-bb[0]), H-50), num_text, font=font, fill=(255,255,255,90))
    img = Image.alpha_composite(img.convert("RGBA"), ov)
    return img

# ── Base frame ────────────────────────────────────────────────────────────────
def base_frame(slide_num, total=5):
    img = Image.new("RGBA", (W, H), BG_TOP)
    draw = ImageDraw.Draw(img)
    gradient_bg(draw)
    img = dot_grid(img)
    img = orange_stripe(img, y=120)
    img = corner_accents(img)
    img = progress_bar(img, slide_num / total)
    img = footer(img, slide_num)
    return img

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 1 — Claude Code (Title)
# ═══════════════════════════════════════════════════════════════════════════════
def slide_01():
    img = base_frame(1)

    # large glass card
    img = glass_rect(img, 260, 280, W-260, 800, radius=32)

    draw = ImageDraw.Draw(img)

    # super-title tag
    img = pill_tag(img, "Claude Code  →  Claude Code CLI",
                   W//2 - 220, 310, font_size=28)

    # main gradient title
    img, _ = gradient_text(img, "Claude Code", 400, 120, bold=True)

    draw = ImageDraw.Draw(img)
    sub_font = load_font(38)
    centered_text(draw, "Terminal agêntico para engenharia de software", 555, sub_font, (220, 220, 240))

    # three pills
    tags = ["Automação", "Refatoração", "Agentes IA"]
    colors = [CYAN, ORANGE, PURPLE]
    total_w = len(tags) * 220
    sx = (W - total_w) // 2
    for i, (tag, col) in enumerate(zip(tags, colors)):
        ov = Image.new("RGBA", img.size, (0,0,0,0))
        d = ImageDraw.Draw(ov)
        font = load_font(28, bold=True)
        bb = d.textbbox((0,0), tag, font=font)
        tw = bb[2]-bb[0]
        px, py = sx + i*220, 650
        pw, ph = tw+40, 48
        d.rounded_rectangle([px, py, px+pw, py+ph], radius=24,
                             fill=(*col, 40), outline=(*col, 180), width=2)
        d.text((px+20, py+10), tag, font=font, fill=col)
        img = Image.alpha_composite(img.convert("RGBA"), ov)

    # bottom line
    draw = ImageDraw.Draw(img)
    small = load_font(26)
    centered_text(draw, "Anthropic · 2025", 740, small, (180, 160, 220, 180), shadow=False)

    img.convert("RGB").save(os.path.join(OUT_DIR, "slide_01.png"), quality=95)
    print("✓ slide_01.png")

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 2 — Recursos Principais
# ═══════════════════════════════════════════════════════════════════════════════
def slide_02():
    img = base_frame(2)
    img = glass_rect(img, 100, 180, W-100, 960, radius=28)

    draw = ImageDraw.Draw(img)
    title_font = load_font(72, bold=True)
    centered_text(draw, "Recursos Principais", 200, title_font, WHITE)

    features = [
        ("⚡", "Edição cirúrgica",  "Lê, entende e edita com precisão cirúrgica"),
        ("🤖", "Agentes autônomos", "Executa tarefas complexas sem supervisão constante"),
        ("🔍", "Busca inteligente", "Grep, glob e análise semântica integrados"),
        ("🔄", "Git nativo",        "Status, diff, commit e PR com RTK savings 80 %"),
    ]

    cols = 2
    card_w, card_h = 780, 220
    margin_x = (W - cols * card_w - 40) // 2

    for i, (icon, title, desc) in enumerate(features):
        col_i = i % cols
        row_i = i // cols
        cx = margin_x + col_i * (card_w + 40)
        cy = 330 + row_i * (card_h + 30)

        img = glass_rect(img, cx, cy, cx+card_w, cy+card_h, radius=20)
        draw = ImageDraw.Draw(img)

        icon_font = load_font(48)
        draw.text((cx+30, cy+30), icon, font=icon_font, fill=WHITE)

        tf = load_font(36, bold=True)
        draw.text((cx+110, cy+35), title, font=tf, fill=CYAN)

        df = load_font(26)
        draw.text((cx+110, cy+85), desc, font=df, fill=(200, 200, 220))

    img.convert("RGB").save(os.path.join(OUT_DIR, "slide_02.png"), quality=95)
    print("✓ slide_02.png")

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 3 — Stack & Integrações
# ═══════════════════════════════════════════════════════════════════════════════
def slide_03():
    img = base_frame(3)

    draw = ImageDraw.Draw(img)
    title_font = load_font(72, bold=True)
    centered_text(draw, "Stack & Integrações", 160, title_font, WHITE)

    items = [
        ("Supabase",    CYAN,   "PostgreSQL · Auth · Realtime"),
        ("Vercel",      WHITE,  "Deploy · Serverless · Edge"),
        ("Cloudflare",  ORANGE, "CDN · DNS · Workers"),
        ("Lovable",     PURPLE, "UI preview · Git sync"),
        ("Antigravity", CYAN,   "Motor principal · Agentes E2E"),
        ("GitHub",      WHITE,  "Repos · Actions · PRs"),
    ]

    cols = 3
    card_w, card_h = 520, 170
    gap_x = (W - cols * card_w - 40*(cols-1)) // 2
    gap_y = 40

    for i, (name, col, desc) in enumerate(items):
        ci = i % cols
        ri = i // cols
        x = gap_x + ci * (card_w + 40)
        y = 290 + ri * (card_h + gap_y)

        img = glass_rect(img, x, y, x+card_w, y+card_h, radius=16)
        draw = ImageDraw.Draw(img)

        # color bar left
        ov = Image.new("RGBA", img.size, (0,0,0,0))
        d = ImageDraw.Draw(ov)
        d.rounded_rectangle([x, y, x+6, y+card_h], radius=3, fill=(*col, 220))
        img = Image.alpha_composite(img.convert("RGBA"), ov)
        draw = ImageDraw.Draw(img)

        nf = load_font(36, bold=True)
        draw.text((x+30, y+30), name, font=nf, fill=col)
        df = load_font(24)
        draw.text((x+30, y+85), desc, font=df, fill=(190, 190, 220))

    img.convert("RGB").save(os.path.join(OUT_DIR, "slide_03.png"), quality=95)
    print("✓ slide_03.png")

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 4 — Fluxo de Trabalho
# ═══════════════════════════════════════════════════════════════════════════════
def slide_04():
    img = base_frame(4)
    img = glass_rect(img, 80, 180, W-80, 940, radius=28)

    draw = ImageDraw.Draw(img)
    title_font = load_font(72, bold=True)
    centered_text(draw, "Fluxo de Trabalho", 200, title_font, WHITE)

    steps = [
        ("1", "Prompt",     "Descreva a tarefa em linguagem natural", CYAN),
        ("2", "Análise",    "Claude lê o código e planeja a solução",  PURPLE),
        ("3", "Execução",   "Edições precisas com ferramentas nativas", ORANGE),
        ("4", "Validação",  "Testes, lint e git automatizados",         CYAN),
        ("5", "Deploy",     "Push → Vercel · PR automático no GitHub",  PURPLE),
    ]

    step_h = 110
    start_y = 330

    for i, (num, title, desc, col) in enumerate(steps):
        y = start_y + i * (step_h + 12)
        img = glass_rect(img, 160, y, W-160, y+step_h, radius=16)

        # number badge
        ov = Image.new("RGBA", img.size, (0,0,0,0))
        d = ImageDraw.Draw(ov)
        d.ellipse([180, y+20, 240, y+80], fill=(*col, 200))
        nf = load_font(32, bold=True)
        d.text((200, y+28), num, font=nf, fill=(0,0,0,230))

        tf = load_font(34, bold=True)
        d.text((270, y+18), title, font=tf, fill=col)
        df = load_font(26)
        d.text((270, y+60), desc, font=df, fill=(200, 200, 225))

        # arrow between steps
        if i < len(steps) - 1:
            ax = W // 2
            ay = y + step_h + 6
            d.polygon([(ax-8, ay), (ax+8, ay), (ax, ay+12)], fill=(255,255,255,60))

        img = Image.alpha_composite(img.convert("RGBA"), ov)

    img.convert("RGB").save(os.path.join(OUT_DIR, "slide_04.png"), quality=95)
    print("✓ slide_04.png")

# ═══════════════════════════════════════════════════════════════════════════════
# SLIDE 5 — CTA / Começar Agora
# ═══════════════════════════════════════════════════════════════════════════════
def slide_05():
    img = base_frame(5)

    # large glow circle center
    ov = Image.new("RGBA", (W, H), (0,0,0,0))
    d = ImageDraw.Draw(ov)
    cx, cy, r = W//2, H//2, 320
    for ri in range(r, 0, -4):
        alpha = int(30 * (1 - ri / r))
        d.ellipse([cx-ri, cy-ri, cx+ri, cy+ri], fill=(*PURPLE, alpha))
    img = Image.alpha_composite(img.convert("RGBA"), ov)

    img = glass_rect(img, 340, 260, W-340, 820, radius=40)

    draw = ImageDraw.Draw(img)
    small_font = load_font(30)
    centered_text(draw, "Pronto para automatizar tudo?", 290, small_font, (200,180,240,200), shadow=False)

    img, _ = gradient_text(img, "Comece Agora", 360, 110, bold=True)

    draw = ImageDraw.Draw(img)
    body = load_font(32)
    centered_text(draw, "npm install -g @anthropic-ai/claude-code", 520, body, ORANGE)

    # three stat boxes
    stats = [("80 %", "Savings Git"), ("99 %", "Savings Tests"), ("24/7", "Autonomia")]
    bw, bh = 300, 130
    total_w = len(stats) * bw + 40 * (len(stats)-1)
    sx = (W - total_w) // 2

    for i, (val, lbl) in enumerate(stats):
        bx = sx + i*(bw+40)
        by = 650
        img = glass_rect(img, bx, by, bx+bw, by+bh, radius=18)
        draw = ImageDraw.Draw(img)
        vf = load_font(48, bold=True)
        bb = draw.textbbox((0,0), val, font=vf)
        draw.text((bx + (bw-(bb[2]-bb[0]))//2, by+12), val, font=vf, fill=CYAN)
        lf = load_font(22)
        bb2 = draw.textbbox((0,0), lbl, font=lf)
        draw.text((bx + (bw-(bb2[2]-bb2[0]))//2, by+70), lbl, font=lf, fill=(200,200,220))

    # footer cta
    cf = load_font(26)
    centered_text(draw, "claude.ai/code · ForYou Code · 2025", 810, cf, (180,160,220,160), shadow=False)

    img.convert("RGB").save(os.path.join(OUT_DIR, "slide_05.png"), quality=95)
    print("✓ slide_05.png")

# ── Run ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    slide_01()
    slide_02()
    slide_03()
    slide_04()
    slide_05()
    print("\nDone → _mapas/slides/")
