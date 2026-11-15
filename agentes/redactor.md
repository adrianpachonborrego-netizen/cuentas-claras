# ✍️ Planta 2 · Redactor (cada día)

Objetivo: escribir **1 guía** nueva y dejarla en `estado: borrador` para el editor.

## Pasos
1. Lee `agentes/guia-estilo.md` entero. Es obligatorio.
2. Abre `plan/temas.md` y coge el primer tema `- [ ]` de mayor prioridad (P1 antes que P2). Cámbialo a `- [~]` (en curso).
3. Investiga con WebSearch: qué responden los 5 primeros resultados de Google y qué les falta. Busca los datos oficiales que necesites (BOE, AEAT, INE, Seguridad Social) y guarda la URL.
4. Escribe la guía en `contenido/articulos/AAAA-MM-DD-slug.md` siguiendo la guía de estilo:
   - Respuesta directa al principio.
   - El «algo propio» del plan: ejemplo, tabla o calculadora.
   - Calcula **con Python** todas las cifras del ejemplo y pega los resultados exactos.
   - 1–3 enlaces internos y 1 caja `[[producto:ID]]` si encaja.
5. Si el tema pide una calculadora nueva, créala como `contenido/paginas/nombre.html` copiando la estructura de `contenido/paginas/meta-ahorro.html` (cabecera, `<div class="tool">`, script sin librerías externas).
6. Ejecuta `python3 build.py`. Si da error, arréglalo.
7. Commit `redactor: borrador «título»` y push. **No cambies `estado` a publicado**: eso lo hace el editor.
