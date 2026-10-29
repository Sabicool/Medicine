"""Where an art PDF's outline is, to line arrows up with an organ's edges.

    python3 -I outline.py servier-liver.pdf              left/right edge at each height
    python3 -I outline.py servier-liver.pdf --grid g.png  the art with a 10% grid over it

Fractions run 0 to 1: x from the left, y from the BOTTOM (as in TikZ). For a
node of width W and height H centred at the origin, (fx, fy) is at
((fx - 0.5) * W, (fy - 0.5) * H). Needs poppler (pdftoppm); --grid needs ImageMagick.
"""
import argparse
import subprocess
import tempfile
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--rows", type=int, default=25, help="heights to report (default 25)")
    ap.add_argument("--grid", metavar="PNG", help="write the art with a 10%% grid instead")
    args = ap.parse_args()

    with tempfile.TemporaryDirectory() as tmp:
        if args.grid:
            png = Path(tmp) / "art.png"
            subprocess.run(["pdftoppm", "-r", "150", "-png", "-singlefile", args.pdf, str(png.with_suffix(""))], check=True)
            w, h = map(int, subprocess.run(["magick", "identify", "-format", "%w %h", str(png)],
                                           capture_output=True, text=True, check=True).stdout.split())
            draw = []
            for i in range(1, 10):
                x, y = w * i // 10, h * i // 10
                draw += ["-draw", f"line {x},0 {x},{h}", "-draw", f"line 0,{y} {w},{y}",
                         "-draw", f"text {x + 2},12 '.{i}'", "-draw", f"text 2,{y - 2} '.{10 - i}'"]
            subprocess.run(["magick", str(png), "-stroke", "#00a0ff", "-fill", "#00a0ff", "-pointsize", "11",
                            *draw, args.grid], check=True)
            print(args.grid)
            return

        ppm = Path(tmp) / "art"
        subprocess.run(["pdftoppm", "-r", "100", "-singlefile", args.pdf, str(ppm)], check=True)
        data = ppm.with_suffix(".ppm").read_bytes()
        _, size, _, pixels = data.split(b"\n", 3)
        w, h = map(int, size.split())
        step = max(1, h // args.rows)
        print("   y    left  right")
        for r in range(0, h, step):
            row = pixels[r * w * 3:(r + 1) * w * 3]
            ink = [i for i in range(w) if min(row[3 * i:3 * i + 3]) < 200]
            if ink:
                print(f"{1 - r / h:5.2f}  {ink[0] / w:5.3f}  {ink[-1] / w:5.3f}")


if __name__ == "__main__":
    main()
