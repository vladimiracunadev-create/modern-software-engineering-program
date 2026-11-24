# Formatter

## Definición

Un **formatter** (formateador) es una herramienta que **transforma la presentación del código fuente bajo reglas deterministas**: sangrías, espacios, saltos de línea, orden de importaciones, comillas. Dada la misma entrada y la misma configuración produce siempre la misma salida. En `SE-100` se presenta junto al compilador, el *linter* y el análisis estático, con un papel acotado: reducir las discusiones de estilo, sin juzgar el contenido. Que sea determinista es lo que lo distingue de una guía de estilo que se aplica a mano.

## Por qué importa

Sin un formateador común, los cambios de código arrastran ruido: sangrías distintas, líneas reflujadas, estilos que dependen de cada editor, y las revisiones se llenan de comentarios de estilo. Con uno, el formato deja de ser tema de conversación y los *diffs* muestran solo cambios de significado. La decisión que cambia es quién decide el estilo: la herramienta, con una configuración versionada, en lugar de cada persona o de cada revisión. También permite **reproducir el formato en integración continua**, de modo que un cambio mal formateado se detecte automáticamente.

## Cómo funciona

El formateador analiza el código a un árbol sintáctico (o a una representación que conserva el significado) y lo **vuelve a imprimir** con sus reglas, descartando el formato original. Por eso el resultado no depende de cómo estaba escrito, y por eso es idempotente: formatear lo ya formateado no cambia nada. Dos usos típicos:

- **Escribir:** se ejecuta al guardar o antes de confirmar un cambio.
- **Comprobar:** en integración continua se ejecuta en modo de verificación, que falla si algún archivo cambiaría.

Dos precauciones se desprenden de `SE-100`. Primero, un formateador **no mejora nombres, cohesión ni corrección**: ordena la apariencia, no el diseño. Segundo, hay que **versionarlo**: un cambio en las reglas de una versión nueva reformatea muchos archivos y produce *diffs* masivos sin cambio de comportamiento; fijar versión y configuración en el repositorio lo evita y permite que el editor y la integración continua den el mismo resultado.

## Ejemplo

Un proyecto fija la herramienta y su versión, y verifica en integración continua:

```bash
python -m black --check src tests     # falla si algún archivo cambiaría
python -m black src tests             # reformatea
```

Si dos personas escriben el mismo código con estilos diferentes, tras formatear ambas versiones son idénticas y la revisión se concentra en la lógica. Si la herramienta se actualiza sin fijar versión, un cambio de regla puede reescribir cientos de líneas en un solo cambio; fijar la versión convierte esa actualización en una decisión explícita, con su propio cambio dedicado.

## Errores y confusiones comunes

- **Creer que el formateador mejora el código.** Solo ordena la presentación.
- **No fijar versión.** Los cambios de regla producen diffs masivos y discrepancias entre editor e integración continua.
- **Confundirlo con el linter.** El linter detecta patrones sospechosos (variables sin uso, comparaciones erróneas); el formateador no juzga. A veces se solapan (orden de importaciones), pero son herramientas distintas.
- **Mezclar reformateos y cambios funcionales.** Dificulta la revisión; el reformateo masivo va en su propio cambio.

## Límites y cuándo no aplica

La señal estática no sustituye experimentación y puede ser ruidosa durante la exploración (`SE-100`): formatear a cada paso un cuaderno de pruebas puede estorbar. El formateador impone un estilo único, que a veces resulta menos legible en un caso concreto (una tabla alineada a mano); la mayoría de las herramientas permiten desactivarlo por bloque. Y en equipos con una guía de estilo ya aplicada y poco cambio, el beneficio marginal es menor.
