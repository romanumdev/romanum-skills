"""Turn generated art pieces drawn on a flat key colour into transparent, trimmed PNGs.

Image tools often can't output real transparency, so the extraction brief asks for each outlined piece on a flat
chroma colour (pure cyan #00FFFF by default, or magenta #FF00FF when the piece contains cyan) and each glow effect on
flat black. This script keys those backgrounds out:
- Chroma pieces: alpha from how far a pixel lifts the key's bright channels above its dark ones, compared with the key
  sampled from the image border. Pieces with a thick dark outline have none of that lift, so along an outline this
  gives the true mix of outline and key. Pixels far from the key stay solid. The key is then unmixed from the
  semi-transparent edge pixels, and key spill left in a thin band along the edge is removed, so no fringe remains.
- Black pieces (lightning, smoke, sparkles): alpha from brightness, colour unpremultiplied, which keeps soft glows.
Each result is trimmed to its content with padding and scaled so its longer side fits the given size.

Usage:
  python key_assets.py RAW_DIR OUT_DIR PIECES_JSON

PIECES_JSON maps file names to [background, longest side], for example:
  {"prop-ghost.png": ["chroma", 768], "fx-smoke-puff.png": ["black", 384]}
Requires NumPy and Pillow.
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image


def border_colour(rgb):
    edge = np.concatenate([rgb[0], rgb[-1], rgb[:, 0], rgb[:, -1]])
    return np.median(edge, axis=0)


def grow(mask, pixels):
    """The mask grown by a few pixels in every direction."""
    out = mask.copy()
    for _ in range(pixels):
        out = out | np.roll(out, 1, 0) | np.roll(out, -1, 0) | np.roll(out, 1, 1) | np.roll(out, -1, 1)
    return out


def key_chroma(rgb):
    key = border_colour(rgb)
    high = key > 128  # cyan: green and blue; magenta: red and blue
    if high.all() or not high.any():
        raise ValueError(f"border colour {key.round()} isn't a chroma key")
    distance = np.sqrt(((rgb - key) ** 2).sum(axis=2))
    key_lift = key[high].min() - key[~high].max()
    lift = rgb[..., high].min(axis=2) - rgb[..., ~high].max(axis=2)
    alpha = np.clip(1 - lift / key_lift, 0, 1)
    alpha = np.clip((alpha - 0.05) / 0.95, 0, 1)  # the background's small variations
    alpha[distance > 200] = 1  # clearly part of the piece
    alpha[distance < 15] = 0
    # Unmix the key from partly transparent pixels: observed = a * piece + (1 - a) * key.
    a = alpha[..., None]
    safe = np.where(a > 0.02, a, 1)
    piece = np.clip((rgb - (1 - a) * key) / safe, 0, 255)
    # Take out key spill left along the edge.
    band = grow(alpha < 0.5, 3)
    spill = np.clip(piece[..., high].min(axis=2) - piece[..., ~high].max(axis=2), 0, None)
    for channel in np.nonzero(high)[0]:
        piece[..., channel] -= np.where(band, spill, 0)
    piece = np.where(a > 0.02, np.clip(piece, 0, 255), 0)
    return piece, alpha


def key_black(rgb):
    key = border_colour(rgb)
    lifted = np.clip(rgb - key, 0, 255)
    alpha = np.clip(lifted.max(axis=2) / 255.0, 0, 1)
    alpha = np.clip((alpha - 0.03) / 0.97, 0, 1)  # drops the generator's faint noise floor
    a = alpha[..., None]
    piece = np.clip(lifted / np.where(a > 0.02, a, 1), 0, 255)
    piece = np.where(a > 0.02, piece, 0)
    return piece, alpha


def trim(img, pad_ratio=0.04):
    alpha = np.array(img.getchannel("A"))
    ys, xs = np.nonzero(alpha > 8)
    if len(xs) == 0:
        return img
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    pad = int(max(x1 - x0, y1 - y0) * pad_ratio) + 4
    box = (max(0, x0 - pad), max(0, y0 - pad), min(img.width, x1 + pad), min(img.height, y1 + pad))
    return img.crop(box)


def main(raw_dir, out_dir, pieces_json):
    raw, out = Path(raw_dir), Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    pieces = json.loads(Path(pieces_json).read_text())
    report = []
    for name, (background, longest) in pieces.items():
        source = raw / name
        if not source.exists():
            report.append(f"{name}: missing raw image")
            continue
        rgb = np.asarray(Image.open(source).convert("RGB")).astype(np.float64)
        piece, alpha = (key_black if background == "black" else key_chroma)(rgb)
        rgba = np.dstack([piece, alpha * 255]).round().astype(np.uint8)
        img = trim(Image.fromarray(rgba, "RGBA"))
        scale = longest / max(img.size)
        if scale < 1:
            img = img.resize((max(1, round(img.width * scale)), max(1, round(img.height * scale))), Image.LANCZOS)
        img.save(out / name)
        a = np.array(img.getchannel("A"))
        report.append(f"{name}: {img.size[0]}x{img.size[1]}, {background} key, opaque {np.mean(a > 250):.0%}, clear {np.mean(a < 5):.0%}")
    print("\n".join(report))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
