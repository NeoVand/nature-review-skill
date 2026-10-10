#!/usr/bin/env python3
"""Generate an explicitly synthetic scientific-figure review fixture (Pillow)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "validation" / "fixtures" / "figure-1.png"
out.parent.mkdir(parents=True, exist_ok=True)
im = Image.new("RGB", (1100, 760), "white")
d = ImageDraw.Draw(im)
# Pillow's bundled default font is portable; no host font lookup needed.
font = ImageFont.load_default(size=23)
small = ImageFont.load_default(size=19)
title = ImageFont.load_default(size=29)
d.text((35, 25), "SYNTHETIC REVIEW FIXTURE - not research data", fill="black", font=small)
d.text((80, 86), "a", fill="black", font=title)
d.text((175, 87), "Irrigation eliminates drought damage", fill="black", font=title)
left, bottom, top, right = 180, 610, 165, 970
def y(v):
    return bottom - (v - 95) / 16 * (bottom - top)
d.line((left, top, left, bottom, right, bottom), fill="black", width=3)
for val in (95, 99, 103, 107, 111):
    yy = y(val)
    d.line((left - 8, yy, left, yy), fill="black", width=2)
    d.text((120, yy - 12), str(val), fill="black", font=font)
d.text((23, 350), "Signal", fill="black", font=font)
for x, value, color, label in ((390, 100, "#cf302c", "Control"), (730, 108, "#30913e", "Irrigated")):
    d.rectangle((x-90, y(value), x+90, bottom), fill=color)
    # These are illustrative decorations, deliberately undefined by the caption.
    d.line((x, y(value-1), x, y(value+1)), fill="black", width=3)
    d.line((x-20, y(value+1), x+20, y(value+1)), fill="black", width=3)
    d.line((x-20, y(value-1), x+20, y(value-1)), fill="black", width=3)
    d.text((x-60, bottom+20), label, fill="black", font=font)
d.line((390, y(110), 730, y(110)), fill="black", width=2)
d.text((490, y(110)-30), "P < 0.001", fill="black", font=small)
d.text((175, 694), "Illustrative bars and error marks; raw data are not supplied.", fill="black", font=small)
im.save(out)
print(out)
