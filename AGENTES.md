# 🏢 El edificio de agentes de Cuentas Claras

Una web de finanzas personales en español que se escribe, se revisa, crea productos y se mejora sola.
Tú (Adrián) solo haces 3 cosas: **subir los productos nuevos a Payhip**, **apuntar las métricas** y **mirar el informe**.

## Cómo funciona el dinero

Google trae visitas → la persona lee una guía o usa una calculadora gratis → ve la plantilla que le resuelve el problema → la compra en Payhip (4,99–9,99 €).
Sin anuncios. Las calculadoras y los ejemplos propios son lo que hace que Google nos posicione y no nos trate como «contenido IA en masa».

## Las plantas

| Planta | Agente | Cuándo trabaja | Qué hace | Instrucciones |
|---|---|---|---|---|
| 5 | 📊 Analista | Cada 48 h (21:07) | Lee las métricas, decide qué funciona y reordena las prioridades | `agentes/analista.md` |
| 4 | 🏭 Fábrica de productos | Domingos alternos (11:17) | Crea una plantilla de Excel nueva y su ficha | `agentes/fabrica.md` |
| 3 | ✅ Editor-verificador | Cada día (13:23) | Comprueba datos, cuentas y calidad; publica o devuelve | `agentes/editor.md` |
| 2 | ✍️ Redactor | Cada día (8:41) | Escribe 1 guía nueva del plan | `agentes/redactor.md` |
| 1 | 🔎 Investigador | Lunes (9:13) | Busca 7 temas nuevos que la gente busca en Google | `agentes/investigador.md` |
| 0 | 📘 Reglas comunes | — | Estilo, tono, formato y lo que nunca se hace | `agentes/guia-estilo.md` |

**Ritmo: 1 guía al día, no una por hora.** Desde 2024 Google penaliza el «scaled content abuse» (muchas páginas hechas con IA sin valor). Es mejor 1 guía buena con ejemplo propio que 24 genéricas.

## Archivos que comparten los agentes

- `plan/temas.md`: cola de temas. El investigador añade, el redactor coge el primero pendiente y el analista reordena.
- `contenido/articulos/*.md`: las guías (`estado: borrador` → `estado: publicado`).
- `contenido/paginas/*.html`: calculadoras, fichas de producto y páginas legales.
- `productos.json`: catálogo. Un producto con `"activo": false` no se muestra.
- `datos/metricas.csv`: **lo rellenas tú** cada 2 días (Search Console + Payhip).
- `datos/informes/`: informes del analista, para que los leas.
- `build.py`: genera la web en `docs/` (GitHub Pages).

## Lo que haces tú (10 min cada 2 días)

1. **Payhip** → Dashboard: apunta las ventas y los ingresos.
2. **Google Search Console** → Rendimiento: apunta clics, impresiones y la página con más clics.
3. Añade una línea a `datos/metricas.csv` (o pégame los números en el chat y la añado yo).
4. Cuando la fábrica cree un producto: súbelo a Payhip, copia el enlace en `productos.json` y pon `"activo": true`.

## Reglas de seguridad del edificio

- Ningún agente borra artículos publicados. Solo puede marcarlos para revisión.
- Los productos de pago **nunca** van en este repositorio (es público). Van en el repo privado `cuentas-claras-productos`.
- Todo dato (porcentajes, leyes, impuestos, tipos de interés) se comprueba en una fuente oficial o fiable y se cita. Si no se puede comprobar, no se publica.
