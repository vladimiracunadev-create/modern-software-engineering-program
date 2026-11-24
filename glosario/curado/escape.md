# Escape

## Definición

Un **escape** es un defecto que supera las puertas del proceso y se descubre después de dar el trabajo por terminado. Es el sentido de `SE-189` (defecto descubierto tras dar un incremento por terminado) y de `SE-188`. En `SE-432` el matiz es el más grave: un defecto que llega a producción sin ser detectado. No es lo mismo que un defecto encontrado durante el desarrollo: lo que define al escape es que el proceso lo dejó pasar.

## Por qué importa

Cambia qué se mide para saber si el proceso de calidad funciona. Cuántos defectos se encuentran no dice nada sobre cuántos se escapan; los escapes sí miden lo que las comprobaciones no vieron. Por eso la definición de terminado se revisa con los escapes del periodo (`SE-188`), y las estrategias de prueba por riesgo se evalúan por la pérdida que causan, no solo por su número (`SE-432`).

## Cómo funciona

Si cada comprobación detectara defectos al azar y de forma independiente, añadir otra reduciría los escapes de forma multiplicativa. `SE-188` muestra que no es así: las comprobaciones miran cosas parecidas, los defectos «fáciles» los ve cualquiera y los «difíciles» se escapan a todas. Esa **correlación** hace que la segunda y la tercera comprobación aporten mucho menos de lo esperado y, a partir de cierto punto, nada. En el ejemplo de la clase, cuando las comprobaciones ven exactamente lo mismo (correlación 1,0) los escapes se quedan en 4 500 aunque haya cuatro. Añadir comprobaciones que miran lo mismo no protege.

La consecuencia práctica es medir qué ve cada comprobación, retirar las redundantes y añadir las que ven algo distinto. `SE-432` añade una precisión sobre cómo evaluar: contar escapes ignora su impacto; hay que medir pérdida y percentil 95. Y `SE-189` advierte contra premiar una métrica que se infla, como la velocidad, mientras el plazo no cambia: se sigue el rendimiento y los escapes.

## Ejemplo

El equipo de la plataforma de entregas reduce su definición de terminado de catorce casillas a tres niveles, cada casilla con la razón registrada, es decir, qué escape evitó. El fragmento de `SE-188` calcula los escapes esperados de dos comprobaciones independientes y de dos que ven lo mismo, y pide predecir cuál deja pasar menos defectos antes de ejecutarlo.

## Errores y confusiones comunes

- **Más casillas y los escapes no bajan.** Comprobaciones correlacionadas; medir qué ve cada una.
- **Evaluar la estrategia solo por número de escapes.** Ignora el impacto; medir pérdida y percentil 95 (`SE-432`).
- **Premiar una métrica que se infla.** La velocidad sube y el plazo no cambia (`SE-189`).
- **Confundir escape con defecto encontrado tarde en desarrollo.** El escape cruza la puerta de «terminado».

## Límites y cuándo no aplica

El escape solo se cuenta cuando se descubre: los que aún no se han visto no aparecen, de modo que la cifra es un mínimo. Las cifras de `SE-188` son de un modelo con parámetros elegidos por la clase. Y reducir escapes tiene un costo; el nivel de comprobación debe ajustarse al riesgo del tipo de cambio.
