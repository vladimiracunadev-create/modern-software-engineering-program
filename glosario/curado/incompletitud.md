# Incompletitud

## Definición

La **incompletitud** de un conjunto de requisitos es la ausencia de un comportamiento para una situación que el sistema podrá encontrar (SE-154). Un conjunto es incompleto si omite una situación que debería contemplar. Es uno de los tipos de defecto de especificación, junto con la ambigüedad y la contradicción.

## Por qué importa

Lo no dicho se decide en el código por quien programa. Cuando la especificación calla, la persona que implementa elige un comportamiento, a menudo sin saber que lo está decidiendo y sin consultar a nadie. Cambia el momento y la persona que decide: lo que debió ser una decisión de producto queda como una suposición de programación.

## Cómo funciona

SE-154 propone una técnica concreta para hacer visible la incompletitud: las **tablas estado–evento**. Si hay 6 estados y 7 eventos, hay 42 combinaciones, y cada una debe tener un comportamiento (una transición, «se ignora» o «es imposible») o una pregunta abierta. Una celda vacía es un hueco. El ejemplo de la clase: no saber qué pasa si una estudiante retira una entrega en revisión es un hueco que alguien llenará en el código sin preguntar.

La técnica funciona porque convierte «pensar en todo» en un recorrido finito y mecánico: en lugar de preguntar «¿qué se me olvida?», se enumeran las combinaciones y se pregunta por cada una. Lo mismo vale para condiciones: n condiciones binarias dan 2ⁿ combinaciones (tabla de decisión). Cada celda debe resolverse como acción, decisión pendiente con responsable o imposibilidad justificada.

La incompletitud es difícil de ver sin esa enumeración porque es ausencia: la lectura revisa lo que está escrito y las ausencias no se ven. Por eso se combina con otras técnicas de detección y con la validación con quienes usan el sistema. Cada técnica encuentra el defecto para el que fue diseñada; la enumeración de combinaciones encuentra huecos, y no encuentra contradicciones ni ambigüedades.

## Ejemplo

Estados de una entrega: borrador, enviada, en revisión, calificada, devuelta, retirada (6). Eventos: enviar, editar, retirar, calificar, devolver, reabrir, vencer plazo (7). La celda (en revisión, retirar) está vacía. Se plantea la pregunta: ¿se permite retirar una entrega en revisión? Respuesta del responsable: «sí, con aviso al docente» o «no». Cualquier respuesta es mejor que dejar que el código decida. (Caso de SE-154 con una enumeración ilustrativa.)

## Errores y confusiones comunes

- **Dos equipos implementan la misma frase de maneras distintas**: ambigüedad, no incompletitud.
- **Contradicción** de orden tres no vista en revisión por pares.
- **Llenar las celdas vacías con «lo obvio»** sin preguntar.
- **Creer que una especificación larga es completa.**

## Límites y cuándo no aplica

La enumeración solo cubre las dimensiones que se eligieron (estados y eventos); una situación fuera de ese modelo sigue sin verse. Con muchos estados y eventos, la tabla es enorme y se reduce con agrupaciones. Una especificación nunca es totalmente completa: se declara qué queda abierto.
