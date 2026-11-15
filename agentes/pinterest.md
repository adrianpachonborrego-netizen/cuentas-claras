# 📌 Planta 7 · Pinterest (sábados)

Objetivo: dejar preparados **7 pines** para la semana siguiente (1 al día), que lleven a guías, calculadoras y plantillas de la web.

## Pasos
1. Lee `agentes/guia-estilo.md`, la lista de páginas publicadas (`docs/sitemap.xml`), `productos.json` y el último informe del analista.
2. Elige 7 destinos: unos 4 guías o calculadoras (gratis, atraen) y 2–3 a plantillas de pago. Prioriza lo que el analista diga que funciona y lo de temporada. Puedes repetir destino con otro enfoque.
3. Escribe `marketing/pines/AAAA-MM-DD.json` (fecha del lunes siguiente) siguiendo el formato de `marketing/pines/2026-11-16.json`:
   - `titulo`: promesa clara (máx. ~45 caracteres); `subtitulo`; `lista` de 3–4 puntos cortos (máx. 30 caracteres cada uno).
   - `descripcion`: 150–300 caracteres, con palabras clave naturales.
   - `fecha`: un pin al día a las 19:00 (hora de Madrid), de lunes a domingo.
   - `estilo`: alterna 0, 1, 2 y 3. `cta`: «Descárgala en Cuentas Claras →» si enlaza a una plantilla de pago.
4. Ejecuta `python3 marketing/hacer_pines.py marketing/pines/AAAA-MM-DD.json` y mira 2–3 imágenes con Read (que no se corte texto).
5. `python3 build.py`, commit y push (las imágenes tienen que estar publicadas para que Pinterest las lea por URL).
6. Haz un ZIP con las 7 imágenes de `assets/pins/AAAA-MM-DD/` y envíaselo a Adrián con SendUserFile (también el CSV, por si un día Pinterest le deja subirlo en bloque). Su Pinterest NO tiene subida por CSV: sube las 7 imágenes a la vez en Crear Pin y rellena cada borrador a mano. Por eso, en tu mensaje final escribe para cada pin, listo para copiar: número de imagen y fecha, **Título**, **Descripción** y **Enlace COMPLETO** (https://… entero, sin abreviar). Tablero: «Ahorro y presupuesto»; publicar más tarde a las 19:00.
