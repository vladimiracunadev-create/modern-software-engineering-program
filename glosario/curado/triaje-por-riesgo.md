# Triaje por riesgo

## Definición

El **triaje por riesgo** es el orden de lectura de un cambio según el riesgo esperado de cada parte, y no según su orden de aparición (SE-196). Es una técnica de revisión de código: la revisora decide por dónde empezar y cuánta atención dar a cada archivo en función de cuánto cuesta equivocarse en él.

## Por qué importa

Los archivos de un cambio no tienen el mismo riesgo: una migración de datos, la autenticación o la configuración son más caras de equivocar que la documentación. Una revisora que lee en el orden del diff gasta su atención en lo que viene primero y puede agotarla antes de llegar a lo crítico. Cambia el reparto de la atención donde es más probable un defecto de alto costo.

## Cómo funciona

El triaje ordena la lectura por **riesgo esperado**: qué tocó cada archivo, cuánto cambió y cuánto cuesta equivocarse. Es una heurística con supuestos (qué tipos de archivo son riesgosos) que deben **declararse y revisarse con los defectos reales que se escapen**. La plantilla del pull request ayuda: pide qué cambia, por qué, cómo se probó y qué archivos merecen más atención.

SE-196 demuestra el efecto con una prueba: con un presupuesto de lectura del 30 % en el orden de aparición, la revisora no alcanza la migración; con triaje por riesgo, la lee primero. La razón es que la atención es un recurso finito y el orden decide en qué se gasta.

El triaje se combina con automatización: un flujo de integración continua ejecuta formato, pruebas, análisis estático y búsqueda de secretos **antes** de asignar revisora, de modo que lo mecánico no ocupa atención humana. El archivo de propietarios (CODEOWNERS, SE-199) añade como revisor obligatorio al equipo dueño de las migraciones cuando un PR toca `migraciones/`. La revisora abre primero los archivos de riesgo alto, lee la descripción y, tras las correcciones, usa `range-diff` para ver solo lo que cambió.

## Ejemplo

Un PR toca cinco archivos: un cambio de texto en la documentación, una prueba, una migración que altera una columna de notas, la configuración del plazo y un comentario. Con triaje, el orden de lectura es migración, configuración, prueba, texto y comentario. Si el presupuesto de atención se acaba, lo que queda sin leer es lo de menor riesgo. (Ilustración construida con el criterio de SE-196.)

## Errores y confusiones comunes

- **Comentarios de estilo mientras se escapan defectos**: la lectura sigue el orden del diff; corrección: ordenar por riesgo y automatizar el estilo.
- **Releer todo tras cada corrección**: la rama se reescribió sin mostrar lo cambiado; corrección: `range-diff` o commits de corrección.
- **Clasificar el riesgo por tamaño**: un cambio de una línea en autenticación puede ser más riesgoso que cien líneas de documentación.
- **No actualizar los supuestos** tras defectos que se escapan.

## Límites y cuándo no aplica

El triaje depende de que los supuestos de riesgo sean razonables; si una categoría considerada inocua esconde defectos, la lectura se desvía. En cambios pequeños, el orden da igual. No sustituye la lectura completa cuando el cambio es crítico: ordena la atención, no la reduce por debajo de lo necesario.
