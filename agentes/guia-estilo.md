# Guía de estilo común (todos los agentes la leen primero)

## Público
Gente normal en España, de 18 a 40 años: primer sueldo, estudiantes, gente que va justa, gente que quiere ahorrar para algo. No saben de finanzas y no quieren sermones.

## Tono
- Tú a tú, claro y directo, como un amigo que sabe de números.
- Frases cortas. Párrafos de 2–4 líneas como mucho.
- Ejemplos con euros reales y situaciones de España: piso compartido, abono transporte, paga extra, Hacienda, Bizum.
- Nada de «en el mundo actual», «es importante destacar», «en conclusión», «sumérgete», «desbloquea» ni frases de relleno típicas de IA.

## Cada guía DEBE tener (si no, el editor la devuelve)
1. **Respuesta en las 2 primeras frases.** El lector sabe al momento si está en el sitio correcto.
2. **Algo propio que no esté en otras webs**: un ejemplo calculado paso a paso, una tabla comparativa hecha por nosotros o un enlace a una de nuestras calculadoras.
3. **Al menos un enlace interno** a una calculadora o a otra guía (rutas relativas: `../herramientas/x.html`, `otra-guia.html`).
4. **Una sola caja de producto** `[[producto:ID]]`, al final o tras el ejemplo, y solo si de verdad ayuda con ese problema.
5. **Entre 700 y 1.400 palabras.** Mejor corta y útil que larga y vacía.
6. **Datos comprobados.** Leyes, impuestos, SMI, IPC, tipos de interés: fuente oficial (BOE, Agencia Tributaria, Seguridad Social, INE, Banco de España) en un enlace dentro del texto, con el año. Si no se puede comprobar, se quita.
7. **Cuentas correctas.** Toda suma, porcentaje y resultado se calcula con Python antes de publicar.

## Formato del archivo
`contenido/articulos/AAAA-MM-DD-slug.md` con esta cabecera exacta:

```
---
titulo: Título con la palabra clave al principio (máx. 65 caracteres si se puede)
descripcion: 140-160 caracteres que prometan algo concreto
slug: palabras-clave-con-guiones
fecha: AAAA-MM-DD
actualizado: AAAA-MM-DD
lectura: minutos
palabra_clave: la búsqueda principal
producto: id-del-producto
estado: borrador
---
```
Titulares con `##` y `###`. Tablas en markdown. Avisos con `<div class="note" markdown="1">…</div>`.

## Prohibido
- Prometer rentabilidades, decir «invierte en X» o recomendar productos financieros concretos.
- Inventar estadísticas, estudios, testimonios o reseñas.
- Copiar textos de otras webs.
- Temas de salud, apuestas, criptomonedas especulativas o «hazte rico rápido».
- Publicar más de 2 guías al día.
