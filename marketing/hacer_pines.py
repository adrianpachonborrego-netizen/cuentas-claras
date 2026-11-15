#!/usr/bin/env python3
"""Genera pines de Pinterest (1000x1500) y el CSV de subida masiva.

Uso:  python3 marketing/hacer_pines.py marketing/pines/AAAA-MM-DD.json
Guarda las imágenes en assets/pins/AAAA-MM-DD/ (build.py las publica con la web, así
Pinterest puede leerlas por URL) y el CSV en marketing/pines/AAAA-MM-DD.csv.

JSON: {"tablero": "Ahorro y presupuesto", "pines": [
  {"titulo": "...", "subtitulo": "...", "lista": ["...","...","..."], "link": "blog/x.html",
   "descripcion": "...", "keywords": "ahorro, presupuesto", "fecha": "2026-11-17T18:00:00", "estilo": 0, "cta": "opcional"}
]}
"""
import json, os, sys, csv
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = json.load(open(os.path.join(ROOT, "config.json"), encoding="utf-8"))
SITE = CFG["url"].rstrip("/") + CFG.get("base_path", "")
W, H = 1000, 1500
ESTILOS = [((246, 243, 236), (31, 111, 92), (22, 32, 44)), ((31, 111, 92), (242, 184, 75), (255, 255, 255)),
           ((255, 244, 214), (37, 74, 200), (22, 32, 44)), ((22, 32, 44), (242, 184, 75), (255, 255, 255))]


def font(n, s):
    for p in [f"/usr/share/fonts/opentype/inter/{n}", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, s)
    return ImageFont.load_default()


def wrap(d, text, f, maxw):
    out, cur = [], ""
    for w in text.split():
        if d.textlength((cur + " " + w).strip(), font=f) > maxw:
            out.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    out.append(cur)
    return out


def pin(p, path):
    bg, acc, ink = ESTILOS[p.get("estilo", 0) % len(ESTILOS)]
    im = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 18), fill=acc)
    y = 120
    fb = font("InterDisplay-Black.otf", 96)
    for l in wrap(d, p["titulo"], fb, W - 140)[:4]:
        d.text((70, y), l, font=fb, fill=ink); y += 110
    y += 20
    fs = font("Inter-SemiBold.otf", 44)
    for l in wrap(d, p.get("subtitulo", ""), fs, W - 140)[:3]:
        d.text((70, y), l, font=fs, fill=acc if bg != (246, 243, 236) else (75, 88, 102)); y += 58
    y += 50
    fl = font("Inter-Bold.otf", 46)
    for i, item in enumerate(p.get("lista", [])[:5]):
        if y + 120 > H - 230:
            break
        d.rounded_rectangle((70, y, W - 70, y + 120), 24, fill=(255, 255, 255) if bg != (22, 32, 44) else (40, 52, 66))
        d.ellipse((100, y + 30, 160, y + 90), fill=acc)
        d.text((119, y + 34), str(i + 1), font=font("Inter-Bold.otf", 40), fill=bg if bg != (255, 244, 214) else (255, 255, 255))
        ls = wrap(d, item, fl, W - 300)[:2]
        ty = y + (60 - 28 * len(ls)) + 4
        for l in ls:
            d.text((190, ty), l, font=fl, fill=(255, 255, 255) if bg == (22, 32, 44) else (22, 32, 44)); ty += 54
        y += 140
    d.rounded_rectangle((70, H - 190, W - 70, H - 90), 50, fill=acc)
    fc = font("Inter-Bold.otf", 44); t = p.get("cta", "Gratis en Cuentas Claras →")
    d.text(((W - d.textlength(t, font=fc)) / 2, H - 167), t, font=fc, fill=bg if acc != (242, 184, 75) else (22, 32, 44))
    im.save(path, quality=88)


def main():
    src = sys.argv[1]
    D = json.load(open(src, encoding="utf-8"))
    tag = os.path.splitext(os.path.basename(src))[0]
    os.makedirs(os.path.join(ROOT, "assets", "pins", tag), exist_ok=True)
    rows = []
    for i, p in enumerate(D["pines"]):
        name = f"pin-{i+1}.jpg"
        pin(p, os.path.join(ROOT, "assets", "pins", tag, name))  # build.py copia assets/ a docs/
        rows.append({"Title": p["titulo"][:100], "Media URL": f"{SITE}/assets/pins/{tag}/{name}",
                     "Pinterest board": D["tablero"], "Thumbnail": "", "Description": p["descripcion"][:500],
                     "Link": f"{SITE}/{p['link']}", "Publish date": p.get("fecha", ""), "Keywords": p.get("keywords", "")})
    csvp = os.path.join(ROOT, "marketing", "pines", f"{tag}.csv")
    with open(csvp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("OK", len(rows), "pines →", csvp)


if __name__ == "__main__":
    main()
