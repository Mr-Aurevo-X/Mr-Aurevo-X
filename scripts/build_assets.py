#!/usr/bin/env python3
"""Build Camo-safe PNG assets for the GitHub profile README."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

BG = (5, 8, 7)
PANEL = (7, 20, 16)
PANEL2 = (7, 24, 32)
LIME = (57, 255, 20)
CYAN = (0, 240, 255)
MUTED = (183, 255, 224)
DIM = (125, 255, 192)
STROKE = (18, 53, 43)
GRID = (12, 42, 34)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        r"C:\Windows\Fonts\consolab.ttf" if bold else r"C:\Windows\Fonts\consola.ttf",
        r"C:\Windows\Fonts\CascadiaMono.ttf",
        r"C:\Windows\Fonts\lucon.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def rounded_rect(draw: ImageDraw.ImageDraw, box, fill, outline=None, width=2, radius=16):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_grid(img: Image.Image, step: int = 40, color=GRID):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    for x in range(0, w, step):
        draw.line([(x, 0), (x, h)], fill=color)
    for y in range(0, h, step):
        draw.line([(0, y), (w, y)], fill=color)


def build_banner() -> None:
    w, h = 1200, 320
    img = Image.new("RGB", (w, h), BG)
    draw_grid(img)
    draw = ImageDraw.Draw(img)
    rounded_rect(draw, (2, 2, w - 3, h - 3), fill=None, outline=STROKE, width=2, radius=18)

    # rain-ish columns
    f_rain = font(13)
    rain = [
        (48, 40, "01??10CODE01??10", LIME),
        (160, 70, "CURSOR_AI_RUN", CYAN),
        (290, 50, "BUILD·TEST·SHIP", LIME),
        (980, 60, "ATELIER_ONLINE", CYAN),
        (1080, 100, "QA_OK", LIME),
    ]
    for x, y, text, color in rain:
        draw.text((x, y), text, fill=color, font=f_rain)

    f_title = font(42, bold=True)
    f_sub = font(20)
    f_tag = font(14)
    draw.text((48, 110), "MR-AUREVO-X", fill=LIME, font=f_title)
    draw.text((48, 168), "AI-RUN WORKSHOP  //  Cursor builds · Human QA", fill=MUTED, font=f_sub)
    draw.text((48, 210), ">_ terminal profile · Windows tools factory", fill=CYAN, font=f_tag)

    # neon bar
    draw.rounded_rectangle((48, 250, 420, 258), radius=4, fill=LIME)
    draw.rounded_rectangle((430, 250, 620, 258), radius=4, fill=CYAN)

    # status chip
    rounded_rect(draw, (980, 40, 1150, 78), fill=PANEL, outline=LIME, width=2, radius=10)
    draw.ellipse((998, 52, 1014, 68), fill=LIME)
    draw.text((1024, 50), "ONLINE", fill=LIME, font=font(16, bold=True))

    img.save(ASSETS / "banner.png", optimize=True)
    print("wrote banner.png")


def build_typing() -> None:
    w, h = 900, 60
    img = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(img)
    rounded_rect(draw, (1, 1, w - 2, h - 2), fill=BG, outline=LIME, width=2, radius=10)
    f = font(20)
    draw.text((22, 18), ">_", fill=LIME, font=f)
    draw.text((54, 18), "Built by Cursor AI · Ideas & QA by Mr-Aurevo-X", fill=MUTED, font=f)
    draw.rectangle((860, 18, 872, 42), fill=CYAN)
    img.save(ASSETS / "typing.png", optimize=True)
    print("wrote typing.png")


def build_ai_core() -> None:
    w, h = 900, 180
    img = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(img)
    rounded_rect(draw, (1, 1, w - 2, h - 2), fill=BG, outline=STROKE, width=2, radius=14)
    draw.text((28, 20), "PROTOCOL // OWNERSHIP_MATRIX", fill=DIM, font=font(14))

    rounded_rect(draw, (28, 56, 428, 152), fill=PANEL, outline=LIME, width=2, radius=10)
    draw.text((48, 72), "CURSOR AI", fill=LIME, font=font(16, bold=True))
    draw.text((48, 100), "builds · refactors · ships", fill=MUTED, font=font(15))
    draw.text((48, 124), "operates the workshop 24/7", fill=CYAN, font=font(15))

    rounded_rect(draw, (472, 56, 872, 152), fill=PANEL2, outline=CYAN, width=2, radius=10)
    draw.text((492, 72), "MR-AUREVO-X", fill=CYAN, font=font(16, bold=True))
    draw.text((492, 100), "ideas · product vision", fill=MUTED, font=font(15))
    draw.text((492, 124), "tests · QA · green light", fill=LIME, font=font(15))

    # bridge
    draw.rounded_rectangle((420, 98, 480, 108), radius=3, fill=LIME)

    img.save(ASSETS / "ai-core.png", optimize=True)
    print("wrote ai-core.png")


def build_status_card() -> None:
    w, h = 900, 220
    img = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(img)
    rounded_rect(draw, (2, 2, w - 3, h - 3), fill=BG, outline=LIME, width=2, radius=16)
    draw_grid(img, step=36)
    # re-draw frame over grid edge
    rounded_rect(draw, (2, 2, w - 3, h - 3), fill=None, outline=LIME, width=2, radius=16)

    # header
    draw.text((32, 28), "ATELIER STATUS", fill=MUTED, font=font(18, bold=True))
    rounded_rect(draw, (720, 24, 868, 56), fill=PANEL, outline=LIME, width=2, radius=10)
    draw.ellipse((738, 34, 754, 50), fill=LIME)
    draw.text((766, 32), "ONLINE", fill=LIME, font=font(15, bold=True))

    # divider
    draw.line([(32, 72), (868, 72)], fill=STROKE, width=2)

    rows = [
        ("OPERATOR", "Cursor AI", LIME),
        ("HUMAN", "Mr-Aurevo-X  ·  ideas + tests", CYAN),
        ("MODE", "AI-OPERATED WORKSHOP", LIME),
        ("OUTPUT", "Windows tools  ·  cleaners  ·  audits", CYAN),
    ]
    f_lab = font(15, bold=True)
    f_val = font(15)
    y = 92
    for label, value, color in rows:
        draw.text((32, y), label, fill=DIM, font=f_lab)
        draw.text((220, y), value, fill=color, font=f_val)
        y += 30

    img.save(ASSETS / "status-card.png", optimize=True)
    print("wrote status-card.png")


def build_manifesto_card() -> None:
    w, h = 900, 260
    img = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(img)
    rounded_rect(draw, (2, 2, w - 3, h - 3), fill=BG, outline=CYAN, width=2, radius=16)

    draw.text((32, 26), "MANIFESTO", fill=MUTED, font=font(16, bold=True))
    rounded_rect(draw, (740, 22, 868, 52), fill=PANEL2, outline=CYAN, width=2, radius=10)
    draw.text((760, 30), "TERMINAL", fill=CYAN, font=font(13, bold=True))

    draw.line([(32, 64), (868, 64)], fill=STROKE, width=2)

    f_big = font(18, bold=True)
    f_body = font(16)
    draw.text((32, 86), "THIS PROFILE IS A TERMINAL.", fill=LIME, font=f_big)
    draw.text((32, 118), "The workshop is AI-operated.", fill=MUTED, font=f_body)
    draw.text((32, 146), "Mr-Aurevo-X brings the spark -- Cursor forges the steel.", fill=MUTED, font=f_body)

    draw.line([(32, 180), (868, 180)], fill=(0, 80, 90), width=1)

    draw.text((32, 198), "FR : Idées humaines. Code machine. Tests sur vrai PC.", fill=CYAN, font=font(15))
    draw.text((32, 224), "EN : Human ideas. Machine code. Real-device QA.", fill=CYAN, font=font(15))

    img.save(ASSETS / "manifesto-card.png", optimize=True)
    print("wrote manifesto-card.png")


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    build_banner()
    build_typing()
    build_ai_core()
    build_status_card()
    build_manifesto_card()


if __name__ == "__main__":
    main()
