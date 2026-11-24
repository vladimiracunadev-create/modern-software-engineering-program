# Análisis

## Definición

En ingeniería de requisitos, **análisis** es el tratamiento del conjunto recogido para encontrar duplicados, conflictos, dependencias y huecos, y convertirlos en decisiones o preguntas. Es el sentido de `SE-145`, que lo sitúa tras la elicitación y antes de la especificación y la validación. «Análisis» tiene otros usos en el programa (análisis de impacto, estático, de datos); aquí se trata únicamente de lo que se hace con los requisitos ya recogidos.

## Por qué importa

Decide cuándo se descubren los conflictos: antes de comprometer diseño o después. Cada persona consultada ve su parte; solo quien trata lo recogido como conjunto ve que dos partes chocan. `SE-145` lo ilustra con una simulación en la que hablar con todo el mundo cubre apenas el 77 % de lo necesario: recoger más no sustituye a analizar. Un conflicto hallado al analizar cuesta una conversación; hallado en producción cuesta un rediseño.

## Cómo funciona

Analizar es tratar lo recogido como un conjunto, no como una lista. `SE-145` enumera cuatro búsquedas:

- **Duplicados:** dos personas piden lo mismo con palabras distintas.
- **Conflictos:** dos personas piden cosas incompatibles.
- **Dependencias:** un requisito solo tiene sentido si otro existe.
- **Huecos:** una situación que nadie contempló.

El producto del análisis no es un texto más pulido sino una lista de preguntas pendientes con responsable. La clase da el modelo: «Auditoría exige 730 días y Privacidad 365; ¿quién decide?». La pregunta nombra a las partes y obliga a que alguien con autoridad resuelva. Y la regla de cierre es práctica: un análisis que no produce preguntas probablemente no analizó nada.

## Ejemplo

En la plataforma de entregas de `SE-145`, los requisitos recogidos de docentes, estudiantes, secretaría y auditoría se cruzan. Retención de datos aparece con dos plazos incompatibles; la solución no la elige quien analiza, sino que se registra como pregunta dirigida a quien tiene la decisión. Mientras no se resuelva, el requisito queda marcado como en conflicto, no como aprobado con un valor arbitrario.

## Errores y confusiones comunes

- **Confundir elicitar con analizar.** Hablar con el cliente es una técnica de elicitación; el análisis empieza cuando lo recogido se trata como conjunto (`SE-145`).
- **Pulir la redacción en lugar de buscar conflictos.** Mejorar el texto no resuelve la contradicción de fondo.
- **Resolver el conflicto en silencio.** Elegir un valor sin que decida quien corresponde oculta el problema.
- **Mezclar requisito y solución.** Dos equipos discuten una frase una hora porque mezcla ambas cosas; la corrección es separar necesidad, requisito y supuesto y registrar el origen de cada uno.

## Límites y cuándo no aplica

El análisis solo encuentra lo que está en el conjunto: si la elicitación no recogió el conocimiento tácito (por ejemplo, porque solo se entrevistó a quien paga), el análisis no puede inventarlo, y la especificación saldrá «completa» pero decepcionará a quienes la usan. Tampoco decide por sí mismo: produce preguntas, no resoluciones. En proyectos muy pequeños puede hacerse en una conversación; la disciplina que importa es dejar escritas las preguntas y quién las responde.
