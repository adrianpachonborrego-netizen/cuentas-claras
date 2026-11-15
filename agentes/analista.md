# 📊 Planta 5 · Analista (cada 48 h)

Objetivo: medir qué funciona y mover el edificio hacia ello, igual que el chico del reto, que lo mide cada 48 horas y no cada semana.

## Pasos
1. Lee `datos/metricas.csv` (lo rellena Adrián: fecha, clics_google, impresiones, ventas, ingresos_eur, pagina_top, notas).
2. Si no hay datos nuevos desde el último informe, escribe en el informe «Sin datos nuevos: Adrián, apunta las métricas» y termina.
3. Calcula con Python:
   - Variación de clics, ventas e ingresos frente al periodo anterior.
   - Conversión = ventas / clics.
   - Ingreso medio por venta.
4. Decide como mucho **3 acciones** concretas para las próximas 48 h. Por ejemplo:
   - Subir a P1 en `plan/temas.md` temas parecidos a la página que más clics trae.
   - Si hay clics pero 0 ventas: proponer un cambio en la caja de producto (texto, precio o posición) en 1 o 2 guías.
   - Si una plantilla vende: pedir a la fábrica una versión ampliada o un pack (en `plan/ideas-productos.md`).
   Aplica tú los cambios de prioridad y de texto. Los de precio solo se proponen, porque Adrián los cambia en Payhip.
5. Escribe `datos/informes/AAAA-MM-DD.md`: 5 líneas de resumen, una tabla con las cifras y las 3 acciones.
6. `python3 build.py` si tocaste contenido. Commit `analista: informe AAAA-MM-DD` y push.

Nunca inventes cifras. Si falta un dato, dilo.
