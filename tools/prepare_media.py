"""Turn originals from the Box folder into web-sized JPEGs for docs/media.

Usage: python3 tools/prepare_media.py "<path to Build Photos>"
Needs Pillow and macOS sips (for HEIC). Each entry: output name, source file,
crop box as fractions (left, top, right, bottom) after rotation.
"""
import os, subprocess, sys, tempfile
from PIL import Image, ImageOps

SRC = sys.argv[1]
OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "media")
PHOTOS = [
    ("two-hands", "2026-09-12_Two_Hands_Comparison.jpeg", (0.0, 0.0, 1.0, 1.0)),
    # Side-by-side project cards: both crops come from the same photo, so light and scale match.
    ("hand-one", "2026-09-12_Two_Hands_Comparison.jpeg", (0.08, 0.20, 0.50, 0.98)),
    ("hand-two", "2026-09-12_Two_Hands_Comparison.jpeg", (0.47, 0.20, 0.89, 0.98)),
    ("first-hand", "IMG_0939.HEIC", (0.0, 0.25, 1.0, 0.9)),
    ("team-session", "IMG_2893.HEIC", (0.0, 0.0, 1.0, 1.0)),
    ("assembly", "IMG_4382.heic", (0.0, 0.0, 1.0, 1.0)),
    ("cad-and-parts", "IMG_2898.HEIC", (0.0, 0.0, 1.0, 1.0)),
    ("palm-channel", "IMG_0942.HEIC", (0.0, 0.2, 1.0, 0.95)),
    ("forming-bath", "IMG_0737.HEIC", (0.0, 0.1, 1.0, 0.85)),
    ("pla-gauntlet", "IMG_0945.HEIC", (0.0, 0.2, 1.0, 1.0)),
    ("fingertips", "80529383984__72D559A8-33E7-4E0C-81DD-16CFA34B3D6E.heic", (0.0, 0.1, 1.0, 0.85)),
    ("printer-bed", "IMG_4628.heic", (0.0, 0.2, 1.0, 0.85)),
]

os.makedirs(OUT, exist_ok=True)
with tempfile.TemporaryDirectory() as tmp:
    for name, src, crop in PHOTOS:
        path = os.path.join(SRC, src)
        if src.lower().endswith(".heic"):
            jpg = os.path.join(tmp, name + ".jpg")
            subprocess.run(["sips", "-s", "format", "jpeg", path, "--out", jpg], check=True, capture_output=True)
            path = jpg
        im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
        w, h = im.size
        im = im.crop((int(crop[0] * w), int(crop[1] * h), int(crop[2] * w), int(crop[3] * h)))
        for width in (1600, 800):
            copy = im.copy()
            copy.thumbnail((width, width))
            copy.save(os.path.join(OUT, f"{name}-{width}.jpg"), quality=78, optimize=True, progressive=True)
        print(name, im.size)

# Video: fingers closing, Jul 8 (IMG_4487.MOV). Run from the repo root:
# ffmpeg -ss 6 -t 5.2 -i "<Build Photos>/IMG_4487.MOV" -an -vf scale=-2:960 -c:v libx264 -crf 27 \
#   -preset slow -pix_fmt yuv420p -movflags +faststart docs/media/fingers-close.mp4
