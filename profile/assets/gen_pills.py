"""Generate the link pills for the org profile header.

shields.io's pinned simple-icons subset has no LinkedIn mark, which left that
one badge as bare text next to logo-bearing ones. These are self-hosted so
every pill carries its real logo.
"""
import os

from gen_stack import CHARCOAL, CREAM, FONT, TERRACOTTA, fetch_icon

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

H = 28
ICON = 14
PAD_X = 10
GAP = 6
FONT_SIZE = 11
CHAR_W = 6.1  # approximate advance for 11px medium Helvetica


def build(label, slug, out_name, bg=CHARCOAL):
    text_w = len(label) * CHAR_W
    width = int(PAD_X + ICON + GAP + text_w + PAD_X)

    paths, (bx, by, bw, bh) = fetch_icon(slug)
    scale = ICON / max(bw, bh)
    gx = PAD_X - bx * scale
    gy = (H - bh * scale) / 2.0 - by * scale
    glyphs = "".join('<path d="%s" fill="%s"/>' % (d, CREAM) for d in paths)

    svg = (
        '<svg width="%d" height="%d" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg">'
        '<rect width="%d" height="%d" rx="6" fill="%s"/>'
        '<g transform="translate(%.2f,%.2f) scale(%.4f)">%s</g>'
        '<text x="%d" y="%.1f" font-family="%s" font-weight="500" font-size="%d" '
        'fill="%s">%s</text>'
        "</svg>\n"
        % (
            width, H, width, H,
            width, H, bg,
            gx, gy, scale, glyphs,
            PAD_X + ICON + GAP, H / 2.0 + FONT_SIZE * 0.35, FONT, FONT_SIZE,
            CREAM, label,
        )
    )
    with open(os.path.join(OUT_DIR, out_name), "w") as f:
        f.write(svg)
    print("wrote %s (%dx%d)" % (out_name, width, H))


if __name__ == "__main__":
    build("theaimerge.com", "googlechrome", "pill-website.svg", bg=TERRACOTTA)
    build("Newsletter", "substack", "pill-newsletter.svg")
    build("LinkedIn", "linkedin", "pill-linkedin.svg")
    build("YouTube", "youtube", "pill-youtube.svg")
