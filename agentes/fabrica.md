# 🏭 Planta 4 · Fábrica de productos (domingos)

Objetivo: crear **1 producto digital nuevo cada semana hasta tener 6 de pago** (después, 1 cada 2 semanas). Enero es el mes fuerte del año para presupuesto, ahorro y propósitos: hasta el 31 de diciembre, prioriza lo que la gente compra en enero. Cuando haya 4 o más plantillas de pago, crea el **pack con todas a 12,99 €**.

## Pasos
0. Cuenta los productos de pago en `productos.json` (sin contar los gratis). Si hay menos de 6, fabrica uno esta semana. Si ya hay 6 o más, mira `git log` del repo privado: si el último producto es de hace menos de 13 días, termina sin hacer nada.
1. Lee `productos.json`, `plan/ideas-productos.md` y el último informe de `datos/informes/`. Elige la idea con más demanda: la que más temas o visitas tiene y no existe aún.
2. Crea el producto con Python (openpyxl):
   - Pestaña «Guía» con instrucciones en 5 pasos.
   - Celdas para rellenar en amarillo; todo lo demás con fórmulas (nada de números escritos a mano).
   - Una fila de ejemplo realista.
   - Funciones compatibles con Excel, Google Sheets y LibreOffice: SUMIFS, SUMPRODUCT, INDEX/MATCH, IFERROR. **No** uses XLOOKUP, FILTER, UNIQUE ni SEQUENCE.
   - Recalcula con LibreOffice (`soffice --headless --convert-to xlsx`) y comprueba que no hay errores (#REF!, #NAME?, #DIV/0!).
3. Guarda el archivo en el **repo privado** `cuentas-claras-productos` (carpeta `productos/`), commit y push. **Nunca** lo pongas en el repo público.
4. En el repo público:
   - Añade el producto a `productos.json` con `"activo": false` y `"url_pago": "https://payhip.com/b/PENDIENTE"`.
   - Crea su ficha `contenido/paginas/producto-ID.html` copiando la estructura de `producto-presupuesto.html`.
   - Escribe en `plan/pendiente-adrian.md`: «Subir ID a Payhip (precio X €) y activar».
5. `python3 build.py`, commit `fabrica: nuevo producto ID` y push.

Precio: 4,99 € para plantillas sencillas y 7,99–9,99 € para packs o plantillas grandes.

## Orden de prioridad (hasta enero)
1. Plan de objetivos y propósitos 2027 (7,99 €)
2. Reto de ahorro 52 semanas (4,99 €)
3. Plan para salir de deudas: bola de nieve / avalancha (7,99 €)
4. Plantilla para independizarse / primer piso (6,99 €)
5. Versión en inglés de la plantilla de presupuesto (para Etsy, 5,99 €)
6. Pack con todas (12,99 €)
