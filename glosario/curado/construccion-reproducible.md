# Construcción reproducible

## Definición

Una **construcción reproducible** es aquella que, con el mismo código fuente y las mismas herramientas, produce artefactos idénticos bit a bit. Es el sentido de `SE-527`; `SE-212` y `SE-408` lo repiten con otras palabras («los mismos bytes a partir de las mismas fuentes»). Se distingue de una construcción meramente «repetible» (que funciona cada vez) en que el resultado debe poder compararse byte a byte.

## Por qué importa

Cambia lo que una huella puede afirmar. Según `SE-527`, cuando la construcción no es reproducible no se puede verificar que lo que se despliega es lo que se probó, ni comparar dos artefactos para ver si cambió algo. `SE-212` lo aplica a la documentación: si la construcción varía, no se puede comparar lo revisado con lo publicado. La reproducibilidad es la condición para que una huella publicada signifique algo.

## Cómo funciona

`SE-527` identifica tres causas habituales de no reproducibilidad:

- **Fechas** incrustadas: la fecha de modificación de los archivos fuente o el momento de la construcción.
- **Orden** en que se leen o se empaquetan los archivos, que depende del sistema.
- **Rutas absolutas** del equipo que construye.

La corrección es eliminar cada dependencia ambiental: fijar o normalizar las marcas de tiempo, ordenar de forma determinista la entrada y evitar rutas absolutas en el resultado. El verificador es simple: construir dos veces (idealmente en equipos distintos) y comparar las huellas. Si coinciden, el proceso es reproducible respecto a esa entrada; si no, la diferencia señala la causa.

## Ejemplo

La documentación de la plataforma de entregas (`SE-212`) se construye en cada pull request con comprobadores de enlaces y de Markdown, y con una construcción reproducible cuya huella se publica junto a la página. La revisión humana mira exactitud, tarea de la audiencia y tipo de página; la huella permite comprobar después que lo publicado es lo revisado.

## Errores y confusiones comunes

- **Confundirla con una construcción automatizada.** Automatizar no garantiza bytes idénticos.
- **Ignorar el orden del sistema de archivos.** El mismo árbol se empaqueta distinto en dos equipos.
- **Esperar reproducibilidad con herramientas sin fijar.** «Las mismas herramientas» incluye versiones.
- **La suite sale roja y verde sin cambios.** Es inestabilidad de pruebas, no de construcción; corrección de `SE-527`: cuarentena con dueño y plazo, y corregir la causa.

## Límites y cuándo no aplica

Según `SE-527`, no es un fin en sí misma: es la condición para que una huella signifique algo. Si nadie compara huellas, la reproducibilidad no aporta nada. Tampoco garantiza que el artefacto sea correcto ni seguro: dos construcciones idénticas pueden ser idénticamente defectuosas. Y lograrla en proyectos con muchas dependencias puede ser costoso; en ese caso se prioriza por riesgo, empezando por lo que se despliega.
