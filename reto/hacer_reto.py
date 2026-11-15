#!/usr/bin/env python3
"""Vídeo diario del reto «Vivir de mis plantillas» (1080x1920, ~20 s, sin voz).

Uso:  python3 reto/hacer_reto.py reto/dias/AAAA-MM-DD.json  [salida.mp4]

El JSON del día:
{
  "dia": 3, "total_dias": 30,
  "ventas_ayer": 1, "ingresos_ayer": 4.99, "total": 9.98,
  "objetivo_ventas_dia": 2, "racha": 0, "racha_meta": 7,
  "hoy": ["Subí la plantilla a Etsy", "Nueva guía: cuesta de enero", "Probé otra portada"],
  "pregunta": "¿Cuántas ventas crees que hago hoy?"
}
Sin audio a propósito: en TikTok/Shorts se le pone un sonido en tendencia al subirlo.
Necesita: Pillow y ffmpeg.
"""
import json, math, subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
BG = (246, 243, 236); INK = (22, 32, 44); MUTED = (91, 104, 118)
GREEN = (31, 111, 92); BLUE = (37, 74, 200); YEL = (242, 184, 75); LINE = (222, 228, 234)

FONT_DIRS = ["/usr/share/fonts/opentype/inter/", "/usr/share/fonts/truetype/dejavu/"]


def font(name, size):
    for d, n in [(FONT_DIRS[0], name), (FONT_DIRS[1], "DejaVuSans-Bold.ttf")]:
        p = os.path.join(d, n)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


F_BIG = lambda s: font("InterDisplay-Black.otf", s)
F_BOLD = lambda s: font("Inter-Bold.otf", s)
F_MED = lambda s: font("Inter-Medium.otf", s)


def eur(v):
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") + " €"


def ease(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def centered(d, y, text, f, fill=INK):
    w = d.textlength(text, font=f)
    d.text(((W - w) / 2, y), text, font=f, fill=fill)


def card(d, x0, y0, x1, y1, r=36, fill=(255, 255, 255)):
    d.rounded_rectangle((x0 + 14, y0 + 14, x1 + 14, y1 + 14), r, fill=INK)
    d.rounded_rectangle((x0, y0, x1, y1), r, fill=fill, outline=INK, width=6)


def header(d, dia, total, etiqueta):
    centered(d, 230, f"Día {dia} de {total} · {etiqueta}", F_BOLD(44), MUTED)
    seg = (W - 160) / total
    for i in range(total):
        c = INK if i < dia - 1 else (BLUE if i == dia - 1 else LINE)
        d.rectangle((80 + i * seg + 3, 300, 80 + (i + 1) * seg - 3, 314), fill=c)


def pill(d, cx, y, text, f, fg=GREEN, bg=(255, 255, 255)):
    w = d.textlength(text, font=f) + 70
    d.rounded_rectangle((cx - w / 2 + 6, y + 6, cx + w / 2 + 6, y + 86), 22, fill=INK)
    d.rounded_rectangle((cx - w / 2, y, cx + w / 2, y + 80), 22, fill=bg, outline=INK, width=4)
    centered(d, y + 14, text, f, fg)


def escenas(D):
    dia, tot = D["dia"], D["total_dias"]

    def e1(t):  # gancho
        im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
        header(d, dia, tot, "EL RETO")
        k = ease(t / 0.5)
        centered(d, 520, "DÍA", F_BIG(200), INK)
        centered(d, 740, f"{dia}", F_BIG(int(380 * (0.6 + 0.4 * k))), BLUE)
        centered(d, 1180, f"DE {tot}", F_BIG(120), INK)
        if t > 0.6:
            pill(d, W / 2, 1420, "Intentando vivir de mis plantillas", F_BOLD(44))
        return im

    def e2(t):  # ayer
        im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
        header(d, dia, tot, "AYER")
        centered(d, 450, "AYER, AL CERRAR", F_BIG(100))
        card(d, 90, 640, W - 104, 1140)
        k = ease(t / 1.2)
        v = round(D["ventas_ayer"] * k)
        e = D["ingresos_ayer"] * k
        d.text((170, 700), f"{v}", font=F_BIG(300), fill=INK)
        d.text((170, 1040), "VENTAS", font=F_BOLD(40), fill=MUTED)
        txt = eur(e); f = F_BIG(120)
        d.text((W - 160 - d.textlength(txt, font=f), 780), txt, font=f, fill=GREEN)
        d.text((W - 160 - d.textlength("INGRESOS", font=F_BOLD(40)), 1040), "INGRESOS", font=F_BOLD(40), fill=MUTED)
        if t > 1.4 and D["ventas_ayer"] >= D["objetivo_ventas_dia"]:
            pill(d, W / 2, 1290, "Objetivo del día cumplido", F_BOLD(46))
        elif t > 1.4:
            pill(d, W / 2, 1290, f"Objetivo: {D['objetivo_ventas_dia']} al día", F_BOLD(46), fg=BLUE)
        return im

    def e3(t):  # total
        im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
        header(d, dia, tot, "EL RECUENTO")
        centered(d, 560, "LLEVO EN TOTAL" if dia <= 2 else f"LLEVO EN {dia - 1} DÍAS", F_BOLD(60), MUTED)
        k = ease(t / 1.3)
        centered(d, 700, eur(D["total"] * k), F_BIG(180), GREEN)
        centered(d, 950, "ventas de plantillas · todo real", F_MED(46), MUTED)
        return im

    def e4(t):  # racha
        im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
        header(d, dia, tot, "LA META")
        centered(d, 450, "LA META", F_BIG(120))
        centered(d, 620, f"{D['objetivo_ventas_dia']} ventas al día,", F_BOLD(66))
        centered(d, 710, f"{D['racha_meta']} días seguidos", F_BOLD(66))
        n = D["racha_meta"]; r = 58; gap = (W - 2 * 120) / n
        for i in range(n):
            cx = 120 + gap * (i + 0.5); cy = 1000
            on = i < D["racha"] and t > 0.3 + i * 0.12
            d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GREEN if on else (255, 255, 255), outline=INK, width=5)
            if on:
                d.line((cx - 24, cy + 2, cx - 6, cy + 22, cx + 26, cy - 18), fill=(255, 255, 255), width=10)
        centered(d, 1140, f"Racha: {D['racha']} / {n}", F_BIG(80), BLUE)
        return im

    def e5(t):  # qué hago
        im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
        header(d, dia, tot, "QUÉ HAGO")
        centered(d, 450, "¿QUÉ ESTOY HACIENDO?", F_BIG(84))
        f = F_BOLD(50)
        lineas = []
        for item in D["hoy"]:
            words, cur, out = item.split(), "", []
            for w_ in words:
                if d.textlength((cur + " " + w_).strip(), font=f) > W - 340:
                    out.append(cur); cur = w_
                else:
                    cur = (cur + " " + w_).strip()
            out.append(cur); lineas.append(out[:2])
        alto = sum(70 * len(l) + 60 for l in lineas)
        card(d, 80, 620, W - 94, 620 + alto + 40)
        y = 660
        for i, ls in enumerate(lineas):
            if t > 0.25 + i * 0.6:
                d.ellipse((130, y + 4, 190, y + 64), fill=BLUE)
                d.text((148, y + 6), str(i + 1), font=F_BOLD(44), fill=(255, 255, 255))
                for j, l in enumerate(ls):
                    d.text((220, y + j * 70), l, font=f, fill=INK)
            y += 70 * len(ls) + 60
        return im

    def e6(t):  # cierre
        im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
        header(d, dia, tot, "MAÑANA")
        f = F_BIG(84); words, cur, ls = D["pregunta"].upper().split(), "", []
        for w_ in words:
            if d.textlength((cur + " " + w_).strip(), font=f) > W - 140:
                ls.append(cur); cur = w_
            else:
                cur = (cur + " " + w_).strip()
        ls.append(cur)
        for j, l in enumerate(ls[:3]):
            centered(d, 520 + j * 105, l, f)
        pill(d, W / 2, 900, "Comenta tu número", F_BOLD(52), fg=BLUE)
        centered(d, 1150, f"Mañana, día {dia + 1} →", F_BIG(100), INK)
        return im

    return [(e1, 2.6), (e2, 3.6), (e3, 2.8), (e4, 3.4), (e5, 1.0 + 0.6 * len(D["hoy"]) + 1.6), (e6, 3.0)]


def main():
    D = json.load(open(sys.argv[1], encoding="utf-8"))
    out = sys.argv[2] if len(sys.argv) > 2 else sys.argv[1].replace(".json", ".mp4")
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    for fn, dur in escenas(D):
        n = int(dur * FPS)
        for i in range(n):
            ff.stdin.write(fn(i / FPS).tobytes())
    ff.stdin.close(); ff.wait()
    # portada para elegir en TikTok/Shorts
    escenas(D)[0][0](2.0).save(out.replace(".mp4", "_portada.jpg"), quality=90)
    print("OK", out)


if __name__ == "__main__":
    main()
