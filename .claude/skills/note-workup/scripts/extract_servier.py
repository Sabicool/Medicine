"""Cut one shape group out of a Servier Medical Art .pptx kit as a transparent vector PDF.

    python3 extract_servier.py KIT.pptx SLIDE --list
    python3 extract_servier.py KIT.pptx SLIDE GROUP_NAME OUT.pdf

Keeps only that group on that slide, hides the master/layout decoration, makes
the slide exactly the group's size, then exports through Keynote (which must be
installed; macOS asks once to let the terminal control it).

--list prints each top-level shape on the slide with its position and size in
points; groups are illustrations, text boxes and lines are labels, and pics are
embedded bitmaps (not vector).
"""
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

def top_level_shapes(tree: str):
    """(start, end, kind, name) of each direct child shape of <p:spTree>."""
    body_start = tree.index("<p:spTree>") + len("<p:spTree>")
    body_end = tree.rindex("</p:spTree>")
    i, out = body_start, []
    while i < body_end:
        m = re.compile(r"<p:(grpSp|sp|pic|cxnSp|graphicFrame)>").search(tree, i, body_end)
        if not m:
            break
        kind = m[1]
        depth, j = 0, m.start()
        tag = re.compile(rf"<(/?)p:{kind}>")
        while True:
            t = tag.search(tree, j)
            depth += -1 if t[1] else 1
            j = t.end()
            if depth == 0:
                break
        name = re.search(r'<p:cNvPr id="\d+" name="([^"]*)"', tree[m.start():j])[1]
        out.append((m.start(), j, kind, name))
        i = j
    return out


def main():
    kit, slide = Path(sys.argv[1]), int(sys.argv[2])
    with zipfile.ZipFile(kit) as z:
        files = {n: z.read(n) for n in z.namelist()}
    path = f"ppt/slides/slide{slide}.xml"
    xml = files[path].decode()
    shapes = top_level_shapes(xml)
    if sys.argv[3] == "--list":
        for s, e, kind, name in shapes:
            off = re.search(r'<a:off x="(-?\d+)" y="(-?\d+)"/><a:ext cx="(\d+)" cy="(\d+)"/>', xml[s:e])
            print(kind, repr(name), [int(v) // 12700 for v in off.groups()] if off else "")
        return
    group, out = sys.argv[3], Path(sys.argv[4]).resolve()
    s, e, _, _ = next(sh for sh in shapes if sh[3] == group)
    shape = xml[s:e]
    off = re.search(r'<a:off x="(-?\d+)" y="(-?\d+)"/><a:ext cx="(\d+)" cy="(\d+)"/>', shape)
    cx, cy = int(off[3]), int(off[4])
    pad = 12700 * 2  # 2 pt so strokes on the edge aren't clipped
    shape = shape.replace(off[0], f'<a:off x="{pad}" y="{pad}"/><a:ext cx="{cx}" cy="{cy}"/>', 1)
    head = xml[: xml.index("<p:spTree>") + len("<p:spTree>")]
    tree_head = xml[len(head) : shapes[0][0]] if shapes else ""
    xml = head + tree_head + shape + xml[xml.rindex("</p:spTree>") :]
    # No master shapes, transparent background
    xml = re.sub(r"<p:sld ", '<p:sld showMasterSp="0" ', xml, count=1)
    xml = re.sub(r"<p:bg>.*?</p:bg>", "", xml, flags=re.S)
    xml = xml.replace("<p:cSld>", "<p:cSld><p:bg><p:bgPr><a:noFill/><a:effectLst/></p:bgPr></p:bg>", 1)
    files[path] = xml.encode()

    pres = files["ppt/presentation.xml"].decode()
    rels = files["ppt/_rels/presentation.xml.rels"].decode()
    rid = re.search(rf'Id="(rId\d+)"[^>]*Target="slides/slide{slide}.xml"', rels)
    rid = rid[1] if rid else re.search(rf'Target="slides/slide{slide}.xml"[^>]*Id="(rId\d+)"', rels)[1]
    pres = re.sub(r"<p:sldIdLst>.*?</p:sldIdLst>",
                  lambda m: "<p:sldIdLst>" + re.search(rf'<p:sldId [^>]*r:id="{rid}"/>', m[0])[0] + "</p:sldIdLst>",
                  pres, flags=re.S)
    pres = re.sub(r'<p:sldSz cx="\d+" cy="\d+"', f'<p:sldSz cx="{cx + 2 * pad}" cy="{cy + 2 * pad}"', pres)
    files["ppt/presentation.xml"] = pres.encode()

    with tempfile.TemporaryDirectory() as tmp:
        pptx = Path(tmp) / "one.pptx"
        with zipfile.ZipFile(pptx, "w", zipfile.ZIP_DEFLATED) as z:
            for n, data in files.items():
                z.writestr(n, data)
        pdf = Path(tmp) / "one.pdf"
        subprocess.run(["osascript", "-e", f'''
tell application "Keynote"
  set d to open POSIX file "{pptx}"
  export d to POSIX file "{pdf}" as PDF
  close d saving no
end tell'''], check=True)
        shutil.copy(pdf, out)
    print(out)


if __name__ == "__main__":
    main()
