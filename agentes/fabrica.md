# 🏭 Planta 4 · Fábrica de productos (domingos alternos)

Objetivo: crear **1 producto digital nuevo** (normalmente una plantilla de Excel) que resuelva un problema que ya traen las guías.

## Pasos
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
