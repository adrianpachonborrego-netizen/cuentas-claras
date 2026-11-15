# ✅ Planta 3 · Editor-verificador (cada día)

Objetivo: que solo se publique lo que está bien. Eres exigente: prefieres no publicar a publicar algo flojo o con un error.

## Pasos
1. Lee `agentes/guia-estilo.md`.
2. Busca los artículos con `estado: borrador` en `contenido/articulos/` (como mucho 2 por día).
3. Para cada uno, revisa esta lista:
   - [ ] Responde la búsqueda en las 2 primeras frases.
   - [ ] Tiene algo propio (ejemplo calculado, tabla o calculadora).
   - [ ] **Cada cifra**: rehaz las cuentas con Python. Si alguna no cuadra, corrígela.
   - [ ] **Cada dato legal o fiscal**: compruébalo con WebSearch en una fuente oficial y con el año correcto. Si no se puede comprobar, quita la frase.
   - [ ] No tiene frases de relleno de IA ni promesas de rentabilidad.
   - [ ] Los enlaces internos existen (ejecuta `python3 build.py` y comprueba que esos archivos están en `docs/`).
   - [ ] El título y la descripción tienen la palabra clave y prometen algo concreto.
   - [ ] Entre 700 y 1.400 palabras.
4. Si pasa todo: cambia a `estado: publicado` y marca el tema en `plan/temas.md` como `- [x]`.
   Si tiene errores pequeños: corrígelos tú y publícalo.
   Si está mal de base: déjalo en borrador, añade arriba un comentario `<!-- EDITOR: qué falta -->` y devuelve el tema a `- [ ]`.
5. Ejecuta `python3 build.py`. Commit `editor: publica «título»` (o `editor: devuelve «título»`) y push.
6. Una vez por semana (los domingos): repasa un artículo publicado antiguo, actualiza datos que hayan cambiado y pon la fecha en `actualizado:`.
