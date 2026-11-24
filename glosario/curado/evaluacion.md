# Evaluación

## Definición

En ingeniería con IA, una **evaluación** (*eval*) es un conjunto de casos con un criterio que mide la calidad de un componente. `SE-549` la define así. `SE-561` añade rigor operativo: un conjunto de tareas con criterio de éxito ejecutable y un procedimiento reproducible para medir un sistema; `SE-597` la usa como conjunto de casos con un criterio de calificación. No es sinónimo de «prueba unitaria»: la salida de un modelo no es única, así que se mide con ejemplos y criterios, no con una igualdad exacta.

## Por qué importa

Es el sustituto de la intuición. Sin evaluación, «el asistente mejoró» es una impresión; con ella, es un número con incertidumbre y una regla de decisión. Cambia la decisión de cuándo se puede cambiar un modelo, un prompt o una herramienta: se cambia si la evaluación lo permite, no si «parece mejor». `SE-549` la describe como una especificación: dice qué se espera, con ejemplos, sin exigir una salida única.

## Cómo funciona

Una evaluación bien hecha (`SE-549`) tiene tres partes:

1. **Casos:** entradas representativas, incluidas las difíciles.
2. **Criterio:** decide si una salida es aceptable; puede ser una aserción de código, una rúbrica aplicada por una persona o por un modelo evaluador.
3. **Regla de decisión:** un umbral y un margen.

`SE-549` ordena las técnicas por costo: primero pruebas de comportamiento comprobables con código, luego revisión humana y de modelos sobre trazas, por último experimentos A/B en producción. La base barata es la más frecuente y cada nivel se justifica por lo que el anterior no ve. `SE-561` agrega que, por el comportamiento no determinista, el resultado se resume con su incertidumbre y se repite.

## Ejemplo

`SE-549`: para el asistente de redacción, el equipo parte de treinta casos: veinte que fallaron antes o que el negocio considera críticos (avisos para una entrega con una hora de adelanto, textos en un tono que no alarme) y diez de un registro de producción. Mide la línea base ocho veces: media de 0,86 y desviación de 0,03. Fija el umbral en 0,80 (dos desviaciones por debajo) y una zona de duda entre 0,80 y 0,83 en la que repite la evaluación con cinco corridas por caso. Y añade una regla: cada fallo real en producción se convierte en un caso nuevo en menos de una semana. Así la evaluación crece con la realidad.

## Errores y confusiones comunes

- **El resultado público no se reproduce en tu equipo** (`SE-561`): distribución de tareas distinta o contaminación. Corrección: evaluación propia, con tareas reales y reservadas.
- **Evaluar solo con casos fáciles.** El umbral se cumple y los casos difíciles fallan sin que nadie lo vea.
- **Una sola corrida.** Con componentes no deterministas hace falta repetir y reportar dispersión.
- **Confundir la evaluación con un *benchmark* público.** Este mide otra distribución de tareas.

## Límites y cuándo no aplica

Una evaluación mide lo que sus casos cubren: no garantiza el comportamiento fuera de ellos. El criterio automático puede tener sesgo (`SE-597` hace explícito el del modelo juez) y una rúbrica humana, subjetividad. Comparar versiones exige emparejar casos y dimensionar su número según el efecto que se quiere detectar. Y los casos de una evaluación se contaminan si se usan también para afinar el sistema: la regla es reservar una parte sin tocarla.
