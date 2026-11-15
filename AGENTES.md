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
| 4 | 🏭 Fábrica de productos | Domingos y miércoles (11:17), 2 productos por semana | Crea una plantilla de Excel nueva y su ficha | `agentes/fabrica.md` |
| 3 | ✅ Editor-verificador | Cada día (13:23) | Comprueba datos, cuentas y calidad; publica o devuelve | `agentes/editor.md` |
| 2 | ✍️ Redactor | Cada día (8:41) | Escribe 1 guía nueva del plan | `agentes/redactor.md` |
| 1 | 🔎 Investigador | Lunes (9:13) | Busca 7 temas nuevos que la gente busca en Google | `agentes/investigador.md` |
| 7 | 📌 Pinterest | Sábados (10:23) | Prepara 7 pines y el CSV de subida masiva | `agentes/pinterest.md` |
| 6 | 🎬 Reto diario | Cada día (9:07) | Vídeo del reto con las cifras reales para TikTok/Shorts | `agentes/reto.md` |
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

## La meta
Fase 1: **2 ventas al día durante 7 días seguidos**. Después 3, 4 y 5 (ver `reto/config.json`). Todos los agentes trabajan para eso.

## Canales de venta
- **Web + Google** (Payhip) · **Etsy** (misma plantilla, ficha en `marketing/etsy.md`) · **TikTok/Shorts** (reto diario) · **Pinterest** (pines a la web)

## Lo que haces tú (10 min cada 2 días)

0. **Cada noche (30 s):** añade una línea a `datos/ventas-diarias.csv` con las ventas de Payhip y Etsy del día (o pégaselas a Claude).
1. **Cada mañana:** sube el vídeo del reto a TikTok y Shorts con un sonido en tendencia.
1. **Payhip / Etsy:** apunta las ventas y los ingresos.
2. **Google Search Console** → Rendimiento: apunta clics, impresiones y la página con más clics.
3. Añade una línea a `datos/metricas.csv` (o pégame los números en el chat y la añado yo).
4. Cuando la fábrica cree un producto: súbelo a Payhip, copia el enlace en `productos.json` y pon `"activo": true`.

## Reglas de seguridad del edificio

- Ningún agente borra artículos publicados. Solo puede marcarlos para revisión.
- Los productos de pago **nunca** van en este repositorio (es público). Van en el repo privado `cuentas-claras-productos`.
- Todo dato (porcentajes, leyes, impuestos, tipos de interés) se comprueba en una fuente oficial o fiable y se cita. Si no se puede comprobar, no se publica.

## Arranque de cada agente (sesión nueva)

1. Si `adrianpachonborrego-netizen/cuentas-claras` no está en la sesión, añádelo con acceso de escritura y clónalo (`git clone --depth 1`). La fábrica también clona `adrianpachonborrego-netizen/cuentas-claras-productos`.
2. `pip install markdown` si hace falta.
3. Lee `AGENTES.md` y `agentes/guia-estilo.md`, y después tu archivo de `agentes/`.
4. Haz los commits en `main` con `git -c push.negotiate=true push origin HEAD:main`. Si el push falla porque hay cambios nuevos, haz `git pull --rebase` y vuelve a intentarlo una vez.
