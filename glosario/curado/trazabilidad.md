# Trazabilidad

## Definición

La **trazabilidad** es la capacidad de seguir un artefacto hacia su origen y hacia sus consecuencias. `SE-168` la toma de Gotel y Finkelstein: seguir un requisito hacia atrás, hasta de dónde viene, y hacia adelante, hasta lo que produjo (contratos, ejemplos, pruebas). `SE-060` la reduce al vínculo entre necesidad, regla, solución y evidencia; `SE-198` la aplica a los cambios de un repositorio (motivo, cambio, uso); y `SE-466` la exige en sistemas regulados como una relación verificable entre requisito, control, prueba y evidencia. El sentido común es el de un camino de ida y vuelta que alguien puede recorrer y comprobar.

## Por qué importa

Permite responder dos preguntas que se hacen siempre en el peor momento: «¿qué verifica este requisito?» y «¿por qué existe esto?». `SE-450` la presenta como lo que un regulador pedirá y como hallazgo útil antes de que lo pregunte: con 30 requisitos y 45 pruebas generados con semilla, 9 requisitos quedan sin ninguna prueba y 2 pruebas sin requisito. Sin trazabilidad, el análisis de impacto de un cambio es una conjetura.

## Cómo funciona

Para que sirva, la trazabilidad debe tener **cobertura en ambos sentidos** (`SE-168`): todo requisito tiene al menos un contrato, todo contrato tiene ejemplo y prueba, y todo ejemplo y prueba pertenece a algún contrato. `SE-450` los nombra como trazabilidad **hacia adelante** («¿qué prueba verifica este requisito?») y **hacia atrás** («¿de qué requisito o peligro viene esta prueba?»).

La causa de que muchos proyectos la abandonen es el mantenimiento: los enlaces que nadie mantiene se convierten en ruido y la trazabilidad cae en desuso. Por eso `SE-168` aconseja un costo de mantenimiento bajo (identificadores estables, comprobación en integración continua) y un alcance acotado: no todo se enlaza con todo. `SE-450` agrega que una trazabilidad construida al final suele fallar, y una mantenida junto al código, con un comprobador, cuesta menos.

En un repositorio, `SE-198` usa una **matriz de trazabilidad** que relaciona cambios con motivos y expone huérfanos en ambos sentidos: commits sin motivo e issues sin cambio. No exige que todo commit tenga issue, pero exige decidir cuáles pueden no tenerlo.

## Ejemplo

`SE-168` construye un paquete sintético de 41 artefactos (3 intenciones, 8 requisitos, 8 contratos, 12 ejemplos y 10 pruebas) y un validador que comprueba enlaces colgantes, tipos permitidos, requisitos y contratos sin descendiente, ciclos y huellas. Aplica 240 mutaciones de ocho tipos con semilla fija y el validador detecta todas las de forma (por ejemplo, 33 de 33 enlaces a un identificador inexistente y 32 de 32 requisitos sin contrato). No detecta un texto que cambia de sentido con el rastro intacto: prueba que los eslabones existen, no que digan la verdad.

En `SE-198`, sobre 60 cambios y 25 issues generados, el cierre `Fixes` de un commit integrado con *squash* se pierde: el único con squash no queda visible en `main` porque el commit de integración solo dice «Integra rama».

## Errores y confusiones comunes

- **Creer que un enlace garantiza que la prueba verifica el requisito.** La cobertura de enlaces mide que hay un enlace, no que la prueba compruebe el requisito; eso lo decide la revisión (`SE-450`).
- **Enlazar todo con todo.** Aumenta el costo de mantenimiento y acaba abandonada (`SE-168`).
- **Perder el vínculo al integrar.** Una integración con squash que descarta el cuerpo del mensaje borra la única referencia al issue (`SE-198`).
- **Construirla al final.** Se reconstruye de memoria y falla (`SE-450`).

## Límites y cuándo no aplica

El validador de `SE-168` comprueba forma y huellas sobre un paquete sintético; en uno real los enlaces los escribe una persona que puede enlazar mal, y un enlace válido puede apuntar al artefacto equivocado. En `SE-450` el comprobador solo verifica estructura, no si el argumento es convincente. Los números de `SE-198` son de un repositorio pequeño con una proporción de squash elegida por el autor: muestran el mecanismo, no cuántos vínculos pierde un proyecto real. Y no cubre los vínculos que viven en la descripción de una solicitud de integración, que el alojamiento puede conservar aparte.
