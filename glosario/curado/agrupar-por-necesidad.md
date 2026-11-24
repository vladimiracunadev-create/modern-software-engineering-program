# Agrupar por necesidad

## Definición

**Agrupar por necesidad** es asignar peticiones distintas a la necesidad de fondo que expresan, con un criterio explícito y revisable. Es el paso del taller de `SE-131` que convierte un backlog de frases literales («agregar botón exportar», «descargar mis notas», «modo oscuro») en una lista más corta de necesidades que se pueden investigar. No es una clasificación por palabras parecidas: es un juicio sobre qué quiere conseguir la persona.

## Por qué importa

Cambia lo que se cuenta al priorizar. Si cada petición pesa uno, las necesidades repetidas con palabras distintas parecen casos aislados y las prioridades se distorsionan. `SE-131` muestra dieciséis peticiones del backlog que se reducen a unas seis necesidades: exportar, seguimiento docente, accesibilidad visual, recordar fechas, ayuda humana y no perder el trabajo. Contar necesidades, y no peticiones, evita construir tres variantes de la misma solución.

## Cómo funciona

El mecanismo parte de descomponer cada petición (observación, inferencia, solución) y preguntarse qué necesidad la explica. «Letra más grande», «más contraste» y «modo oscuro» comparten la accesibilidad visual aunque sus soluciones difieran. Luego se asigna cada petición a una necesidad y se registra la asignación junto con la petición original textual, para poder rehacerla.

La clase insiste en que es un **juicio de investigación**: lo hizo una persona, y otra podría separar «seguimiento docente» en dos. Por eso la agrupación no se da por válida hasta contrastarla con entrevistas, y por eso el criterio queda escrito. Una asignación sin criterio no se puede discutir; una asignación con criterio se puede corregir cuando aparece evidencia nueva.

## Ejemplo

En la plataforma de entregas, el archivo del taller de `SE-131` conserva la petición original sin sobrescribir, quién la hizo y cuándo, su descomposición, el problema reformulado, la guía de preguntas, la rúbrica aplicada por dos personas y las peticiones del backlog con su necesidad asignada. El contrato es que la petición original no se modifica y que el problema reformulado indica qué observación lo confirmaría. Así, si una entrevista muestra que «descargar mis notas» era en realidad «seguimiento docente», se reasigna sin perder el rastro.

## Errores y confusiones comunes

- **El backlog crece con peticiones que parecen distintas y resultan iguales.** Causa: no se agruparon por necesidad; corrección de `SE-131`: agrupar con criterio explícito y contar necesidades.
- **Agrupar por solución.** Juntar «exportar a PDF» con «exportar a Word» solo agrupa formatos; la necesidad puede ser «entregar la evidencia a quien la exige».
- **Tomar la agrupación como un hecho.** Es una hipótesis hasta contrastarla con personas.
- **Perder la petición original.** Sin ella no se puede auditar el criterio.

## Límites y cuándo no aplica

Las definiciones de `SE-131` son operativas para la plataforma de entregas y se probaron con peticiones sintéticas de una sola persona que etiquetó; los umbrales se afinaron con pocos ejemplos. Con un backlog muy pequeño la agrupación aporta poco. Y no sustituye la investigación: agrupar ordena lo que ya se recogió, pero no revela necesidades que nadie pidió. Para eso están las entrevistas y la observación del trabajo real.
