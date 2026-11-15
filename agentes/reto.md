# 🎬 Planta 6 · Reto diario (TikTok / YouTube Shorts)

Objetivo: cada día, un vídeo vertical del reto «Intentando vivir de mis plantillas», con las **cifras reales**, como el de ericbuilds. El reto es el escaparate: cada vídeo es un anuncio gratis y la gente vuelve al día siguiente para ver si se cumple.

## Pasos
1. Lee `reto/config.json`, `datos/ventas-diarias.csv` (lo rellena Adrián cada noche) y el JSON del día anterior en `reto/dias/`.
2. Calcula con Python:
   - `dia` = días desde `inicio` + 1.
   - `ventas_ayer` e `ingresos_ayer` = la fila de ayer (Payhip + Etsy). **Si falta la fila de ayer, NO te la inventes**: pon `ventas_ayer` = null y en el vídeo usa la frase «Hoy no hay cifras: mañana, doble recuento» (o deja el día sin vídeo y avisa a Adrián).
   - `total` = suma de todos los ingresos desde `inicio`.
   - Fase actual y `racha`: días seguidos (hasta ayer) con ventas ≥ objetivo de la fase. Cuando la racha llega a `racha_meta`, se pasa a la fase siguiente y la racha vuelve a 0.
3. Rellena `hoy` con 3 cosas **reales** que hayan pasado en el edificio en las últimas 24 h (mira `git log --since="1 day ago"`: guías publicadas, producto nuevo, cambios del analista, Etsy, Pinterest). Frases de menos de 40 caracteres.
4. Escribe una `pregunta` que invite a comentar («¿Cuántas ventas crees que hago hoy?», «¿Llegará la racha a 3?»…). Cámbiala cada día.
5. Guarda `reto/dias/AAAA-MM-DD.json` y genera el vídeo: `python3 reto/hacer_reto.py reto/dias/AAAA-MM-DD.json /tmp/reto.mp4`. Extrae 3 fotogramas con ffmpeg y míralos con Read; si algo se ve mal, corrígelo.
6. Commit del JSON (el MP4 no se sube al repo) y push.
7. Entrega a Adrián con SendUserFile el MP4 y la portada, más:
   - **Descripción** (estilo ericbuilds): «Día X de 30. Ayer cerré con N ventas y Y €… Qué estoy haciendo: … Llevo Z €. El objetivo: … ¿Cuántas crees que hago hoy? Comenta tu número.»
   - **Hashtags:** #reto30dias #ganardineroporinternet #emprendimiento #buildinpublic #finanzaspersonales
   - Recordatorio: subirlo con un **sonido en tendencia** (el vídeo no tiene audio a propósito) y la misma descripción en YouTube Shorts.

Nunca exageres ni inventes cifras: el reto funciona porque es real.
