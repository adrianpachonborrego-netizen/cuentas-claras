#!/usr/bin/env python3
"""Genera la web estática de Cuentas Claras en la carpeta docs/ (GitHub Pages).

Uso:  python3 build.py
Necesita: pip install markdown   (en la mayoría de sistemas ya está)

- contenido/articulos/*.md  -> docs/blog/<slug>.html
- contenido/paginas/*.html  -> docs/<ruta indicada en 'ruta'>
- productos.json            -> cajas de producto y fichas
- config.json               -> nombre y URL de la web
Atajo dentro de un artículo:  [[producto:ID]]  inserta la caja de compra del producto.
"""
import json, re, shutil, html
from pathlib import Path
from datetime import date
import markdown

ROOT = Path(__file__).parent
OUT = ROOT / "docs"
CFG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
PRODUCTOS = {p["id"]: p for p in json.loads((ROOT / "productos.json").read_text(encoding="utf-8"))}
SITE = CFG["url"].rstrip("/")
BASE = CFG.get("base_path", "").rstrip("/")  # p. ej. "/cuentas-claras" si no hay dominio propio


def front_matter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
    if not m:
        raise ValueError("Falta el bloque --- de cabecera")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, m.group(2)


def url(path):
    return f"{BASE}/{path.lstrip('/')}"


def caja_producto(pid):
    p = PRODUCTOS.get(pid)
    if not p or not p.get("activo", True):
        return ""
    incluye = "".join(f"<li>{html.escape(i)}</li>" for i in p["incluye"])
    tachado = f"<s>{p['precio_tachado']}</s>" if p.get("precio_tachado") else ""
    img = f'<img src="{url(p["imagen"])}" alt="{html.escape(p["nombre"])}" loading="lazy" style="border-radius:10px;margin-bottom:14px;border:1px solid #e3e8ee">' if p.get("imagen") else ""
    return f"""
<div class="offer">
  {img}<span class="tag">{"Plantilla gratis" if p.get("gratis") else "Plantilla lista para usar"}</span>
  <h3>{html.escape(p['nombre'])}</h3>
  <p>{html.escape(p['gancho'])}</p>
  <ul>{incluye}</ul>
  <div class="price">{p['precio']}{tachado}</div>
  <p class="small">{"Gratis · solo te pide el email para enviártela" if p.get("gratis") else "Descarga inmediata · Excel, Google Sheets y LibreOffice · Pago seguro"}</p>
  <a class="btn big" href="{p['url_pago']}" data-payhip>{"Descargar gratis" if p.get("gratis") else "Descargar ahora"}</a>
  <p class="small" style="margin-top:10px"><a href="{url(p['pagina'])}">Ver todo lo que incluye</a></p>
</div>"""


def layout(title, description, body, path, extra_head=""):
    canonical = f"{SITE}{url(path)}"
    verif = f'<meta name="google-site-verification" content="{CFG["google_verificacion"]}">' if CFG.get("google_verificacion") else ""
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<link rel="stylesheet" href="{url('assets/style.css')}">
{verif}
{extra_head}
</head>
<body>
<header class="site"><div class="wrap wide">
  <a class="logo" href="{url('')}">Cuentas<span>Claras</span></a>
  <nav class="main"><a href="{url('herramientas/')}">Calculadoras</a><a href="{url('plantillas/')}">Plantillas</a><a href="{url('blog/')}">Guías</a></nav>
</div></header>
<main><div class="wrap">
{body}
</div></main>
<footer class="site"><div class="wrap wide">
  <p>© {date.today().year} {CFG['nombre']} · Información general, no es asesoramiento financiero personalizado.</p>
  <p><a href="{url('aviso-legal.html')}">Aviso legal</a><a href="{url('privacidad.html')}">Privacidad</a><a href="{url('cookies.html')}">Cookies</a><a href="{url('contacto.html')}">Contacto</a></p>
</div></footer>
</body>
</html>"""


def write(path, content):
    f = OUT / path
    if path.endswith("/") or path == "":
        f = f / "index.html"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(content, encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "assets", OUT / "assets")
    urls = []

    # Artículos
    articulos = []
    for f in sorted((ROOT / "contenido/articulos").glob("*.md")):
        meta, body = front_matter(f.read_text(encoding="utf-8"))
        if meta.get("estado", "publicado") != "publicado":
            continue
        body = re.sub(r"\[\[producto:([\w-]+)\]\]", lambda m: caja_producto(m.group(1)), body)
        body_html = markdown.markdown(body, extensions=["tables", "toc", "md_in_html"])
        slug = meta["slug"]
        path = f"blog/{slug}.html"
        fecha = meta.get("fecha", str(date.today()))
        ld = {"@context": "https://schema.org", "@type": "Article", "headline": meta["titulo"],
              "description": meta["descripcion"], "datePublished": fecha,
              "dateModified": meta.get("actualizado", fecha),
              "author": {"@type": "Organization", "name": CFG["nombre"]}}
        head = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
        page = (f'<div class="crumbs"><a href="{url("")}">Inicio</a> › <a href="{url("blog/")}">Guías</a></div>'
                f'<h1>{html.escape(meta["titulo"])}</h1>'
                f'<div class="meta">Actualizado: {meta.get("actualizado", fecha)} · {meta.get("lectura", "5")} min de lectura</div>'
                f'{body_html}')
        write(path, layout(meta["titulo"] + " | " + CFG["nombre"], meta["descripcion"], page, path, head))
        articulos.append((fecha, meta, path))
        urls.append((path, meta.get("actualizado", fecha)))
    articulos.sort(key=lambda x: x[0], reverse=True)

    # Páginas (herramientas, plantillas, legales)
    paginas = []
    for f in sorted((ROOT / "contenido/paginas").glob("*.html")):
        meta, body = front_matter(f.read_text(encoding="utf-8"))
        body = re.sub(r"\[\[producto:([\w-]+)\]\]", lambda m: caja_producto(m.group(1)), body)
        path = meta["ruta"]
        write(path, layout(meta["titulo"] + " | " + CFG["nombre"], meta["descripcion"], body, path))
        paginas.append((meta, path))
        if meta.get("indexar", "si") == "si":
            urls.append((path, meta.get("actualizado", str(date.today()))))

    def tarjetas(items):
        return '<div class="grid">' + "".join(
            f'<a class="card" href="{url(p)}"><span class="tag">{html.escape(m.get("seccion", ""))}</span>'
            f'<h3>{html.escape(m["titulo"])}</h3><p>{html.escape(m["descripcion"])}</p></a>' for m, p in items) + "</div>"

    herramientas = [(m, p) for m, p in paginas if m.get("seccion") == "Calculadora"]
    plantillas = [(m, p) for m, p in paginas if m.get("seccion") == "Plantilla"]
    guias = [(m | {"seccion": "Guía"}, p) for _, m, p in articulos]

    write("herramientas/", layout("Calculadoras de finanzas personales | " + CFG["nombre"],
          "Calculadoras gratis para organizar tu dinero: presupuesto 50/30/20, interés compuesto y más.",
          "<h1>Calculadoras gratis</h1><p class='lead'>Haz las cuentas en segundos, sin registrarte.</p>" + tarjetas(herramientas), "herramientas/"))
    write("plantillas/", layout("Plantillas de Excel para tus finanzas | " + CFG["nombre"],
          "Plantillas de Excel y Google Sheets listas para usar: presupuesto, ahorro, gastos y más.",
          "<h1>Plantillas listas para usar</h1><p class='lead'>Abre, rellena y listo. Funcionan en Excel, Google Sheets y LibreOffice.</p>" + tarjetas(plantillas), "plantillas/"))
    write("blog/", layout("Guías de ahorro y finanzas personales | " + CFG["nombre"],
          "Guías prácticas para ahorrar, hacer un presupuesto y ordenar tu dinero en España.",
          "<h1>Guías</h1><p class='lead'>Paso a paso, con ejemplos en euros.</p>" + tarjetas(guias), "blog/"))
    urls += [("herramientas/", str(date.today())), ("plantillas/", str(date.today())), ("blog/", str(date.today()))]

    portada = f"""
<section class="hero">
  <h1>Pon orden en tu dinero, sin complicarte.</h1>
  <p class="lead">Calculadoras gratis, guías claras y plantillas de Excel listas para usar. Pensado para gente normal en España.</p>
  <a class="btn" href="{url('herramientas/regla-50-30-20.html')}">Calcula tu presupuesto gratis</a>
</section>
<h2>Calculadoras</h2>{tarjetas(herramientas)}
<h2>Plantillas</h2>{tarjetas(plantillas)}
<h2>Últimas guías</h2>{tarjetas(guias[:6])}"""
    write("", layout(CFG["nombre"] + " · Presupuesto, ahorro y plantillas de Excel", CFG["descripcion"], portada, ""))
    urls.insert(0, ("", str(date.today())))

    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p, d in urls:
        sitemap.append(f"  <url><loc>{SITE}{url(p)}</loc><lastmod>{d}</lastmod></url>")
    sitemap.append("</urlset>")
    (OUT / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}{url('sitemap.xml')}\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("")
    write("404.html", layout("Página no encontrada", "Esta página no existe.",
          f"<h1>Esta página no existe</h1><p><a href='{url('')}'>Volver al inicio</a></p>", "404.html"))
    if CFG.get("dominio"):
        (OUT / "CNAME").write_text(CFG["dominio"])
    print(f"OK: {len(articulos)} artículos, {len(paginas)} páginas, {len(urls)} URLs en el sitemap")


if __name__ == "__main__":
    main()
