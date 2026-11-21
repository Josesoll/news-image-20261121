#!/usr/bin/env python3
"""Deterministic front-page generator for news-image-20261121.

Renders entry.png (1024x1024) summing up Saturday 21 November 2026.
All stories were first reported / happened on 21 Nov 2026 (see README).
No randomness except a fixed-seed star field; output is byte-stable
for a given Pillow/font environment.
"""
import random
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (248, 244, 233)
INK = (18, 18, 18)
RED = (178, 24, 24)
NAVY = (13, 24, 48)
GOLD = (245, 178, 44)
ORANGE = (255, 122, 26)
WHITE = (255, 255, 255)
GREY = (90, 86, 78)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

def f(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

def centered(draw, y, text, font, fill=INK):
    w_ = draw.textlength(text, font=font)
    draw.text(((W - w_) / 2, y), text, font=font, fill=fill)
    return y + font.size + 6

def burst(draw, cx, cy, r, fill):
    pts = []
    for i in range(16):
        ang = i * 3.14159265 / 8
        rr = r if i % 2 == 0 else r * 0.38
        import math
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    draw.polygon(pts, fill=fill)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
M = 48  # margin

# --- Masthead ---
d.line([(M, 36), (W - M, 36)], fill=INK, width=3)
centered(d, 46, "THE  WORLD  TODAY", f(SERIF_B, 74))
d.rectangle([M, 138, W - M, 184], fill=INK)
centered(d, 146, "SATURDAY  21  NOVEMBER  2026", f(SANS_B, 30), fill=WHITE)
centered(d, 190, "RIYADH  •  UKRAINE  •  ANTALYA  •  GENEVA  •  FLORIDA  •  EUROPE", f(SANS_B, 17), fill=RED)

# --- Lead visual: night sky, interceptors over a skyline ---
vx0, vy0, vx1, vy1 = M, 224, W - M, 400
d.rectangle([vx0, vy0, vx1, vy1], fill=NAVY)
rng = random.Random(21)
for _ in range(90):
    x = rng.randint(vx0 + 8, vx1 - 8); y = rng.randint(vy0 + 8, vy0 + 120)
    d.ellipse([x, y, x + 3, y + 3], fill=(210, 220, 240))
# incoming missile trails (orange, descending)
for (x0, y0, x1, y1) in [(180, 238, 330, 356), (430, 232, 520, 330), (760, 236, 660, 344), (880, 244, 790, 330)]:
    d.line([(x0, y0), (x1, y1)], fill=ORANGE, width=7)
    d.line([(x0, y0), (x1, y1)], fill=GOLD, width=3)
    burst(d, x1, y1, 26, GOLD)
    burst(d, x1, y1, 13, (255, 240, 190))
# interceptor arcs (white, rising)
for (x0, y0, x1, y1) in [(240, 390, 330, 356), (560, 390, 520, 330), (700, 390, 660, 344), (840, 390, 790, 330)]:
    d.line([(x0, y0), ((x0 + x1) // 2, (y0 + y1) // 2 - 34), (x1, y1)], fill=WHITE, width=4)
# skyline
for (x, h, w_) in [(60, 52, 70), (140, 84, 54), (205, 40, 90), (305, 66, 48), (365, 96, 58),
                   (435, 44, 84), (530, 72, 52), (595, 38, 88), (695, 88, 56), (762, 48, 76),
                   (850, 68, 54), (915, 42, 52)]:
    d.rectangle([x, vy1 - h, x + w_, vy1], fill=(5, 10, 22))
d.rectangle([vx0, vy0, vx1, vy1], outline=INK, width=3)
# labels inside visual
for (x, txt) in [(vx0 + 16, "RIYADH — BEFORE DAWN"), (vx1 - 292, "UKRAINE — OVERNIGHT")]:
    tw = d.textlength(txt, font=f(SANS_B, 17))
    d.rectangle([x, vy0 + 14, x + tw + 20, vy0 + 46], fill=RED)
    d.text((x + 10, vy0 + 20), txt, font=f(SANS_B, 17), fill=WHITE)

# --- Lead headline + deck ---
y = 414
for line in ["MISSILES OVER RIYADH,", "RAIN OF FIRE ON UKRAINE"]:
    centered(d, y, line, f(SERIF_B, 52)); y += 58
deck = ("Saudi defences destroy three Houthi ballistic missiles over the capital before dawn — "
        "while Russia fires 148 drones and 3 ballistic missiles at Ukraine overnight.")
for line in wrap(d, deck, f(SANS, 22), W - 2 * M - 24):
    centered(d, y, line, f(SANS, 22)); y += 28
y += 2
centered(d, y, "Kryvyi Rih toll, Saturday: a boy of 7 and a paramedic killed, about 60 wounded — AP",
         f(SERIF_I, 19), fill=GREY)
y += 34
d.line([(M, y), (W - M, y)], fill=RED, width=4)
y += 14

# --- Secondary grid 2 x 2 ---
stories = [
    ("CLIMATE  •  ANTALYA", "COP31 TALKS RUN\nINTO OVERTIME",
     "Nearly 200 nations fail to agree on Saturday. “Fossil fuels” vanish from the draft deal as 1.5°C overshoot is conceded."),
    ("AI WEAPONS  •  GENEVA", "NO BAN ON\nKILLER ROBOTS",
     "128 nations end UN talks Saturday with only a pledge to keep talking until 2028 — no binding rules on autonomous weapons."),
    ("STORM  •  FLORIDA", "FLORIDA UNDER\nRECORD WATER",
     "St. Johns River stays near record levels Saturday after 24 inches of rain on the Space Coast. The flood storm heads north."),
    ("EUROPE  •  SATURDAY", "GEN Z MARCHES\nROLL ON IN EUROPE",
     "Youth protests continue into Saturday — transport strike in Italy, marches in France and Spain — over living costs and war spending."),
]
colw = (W - 2 * M - 20) // 2
rowh = 158
for i, (kicker, head, deck_) in enumerate(stories):
    cx = M + (i % 2) * (colw + 20)
    cy = y + (i // 2) * (rowh + 12)
    d.text((cx, cy), kicker, font=f(SANS_B, 16), fill=RED)
    hy = cy + 24
    for line in head.split("\n"):
        d.text((cx, hy), line, font=f(SERIF_B, 29), fill=INK); hy += 34
    for line in wrap(d, deck_, f(SANS, 17), colw - 6)[:3]:
        d.text((cx, hy), line, font=f(SANS, 17), fill=(45, 43, 40)); hy += 21
    if i % 2 == 0:
        d.line([(cx + colw + 10, cy + 4), (cx + colw + 10, cy + rowh)], fill=(190, 182, 164), width=2)
    if i < 2:
        d.line([(cx, cy + rowh + 4), (cx + colw, cy + rowh + 4)], fill=(190, 182, 164), width=2)

# --- Footer ---
fy = H - 44
d.line([(M, fy - 10), (W - M, fy - 10)], fill=INK, width=2)
centered(d, fy, "Every story on this page happened or was first reported on Saturday 21 November 2026  •  Reuters • AP • AFP • Al Jazeera",
         f(SANS, 15), fill=GREY)

img.save("entry.png", format="PNG", optimize=True)
print("wrote entry.png", img.size)
