# Escalada

## Definición

En el trabajo con agentes, la **escalada** es la entrega de la tarea a una persona con la evidencia necesaria. `SE-581` la define así y `SE-588` precisa que se entrega *con la traza*. Es la salida honesta de un agente que no pudo resolver algo: en lugar de seguir intentándolo o de declarar un éxito falso, devuelve el control con el contexto para que alguien decida.

## Por qué importa

Cambia qué significa fallar bien. `SE-581` lo resume: la mejora no estuvo en resolver más, sino en **fallar mejor**. Un informe que solo dice «tope alcanzado» obliga a reconstruir qué pasó; una escalada con evidencia deja la mañana empezando con una lista que se puede leer y actuar.

## Cómo funciona

Una escalada es la acción asociada a una condición de parada que no es convergencia. Lo que la hace útil es lo que lleva consigo. En `SE-581`, el detector con cambio de plan y escalada entrega, para cada tarea sin resolver:

- el **objetivo** original,
- los **tres últimos intentos**,
- el **último error**.

Con eso la persona no repite lo ya intentado. La causa de su valor es el costo de contexto: una tarea entregada sin traza cuesta casi lo mismo que empezarla de nuevo; con traza, se retoma en el punto de fallo. En `SE-588` la escalada aparece también como parte de la respuesta a la pregunta «cómo se detiene»: junto con la parada, es uno de los controles que un comité querrá ver.

## Ejemplo

El caso de `SE-581`: un asistente ejecuta cuarenta tareas de mantenimiento durante la noche con un tope de 30 vueltas. Por la mañana, once terminaron en el tope y el informe dice solo «tope alcanzado». Revisando las trazas, nueve repetían el mismo error desde la vuelta cinco. Se añade el detector con cambio de plan y escalada. La noche siguiente, el número de tareas sin resolver es parecido, pero el gasto baja y la lista de la mañana se puede leer. Es una simulación con datos sintéticos, no una medición de un agente real.

## Errores y confusiones comunes

- **Informar solo «tope alcanzado».** Es parar sin escalar: se pierde la información que permite decidir.
- **Seguir hasta agotar el presupuesto.** Nueve de las once tareas de la clase repetían el mismo error desde la vuelta cinco: seguir no aportaba nada.
- **Entregar la traza completa sin resumen.** La evidencia útil es la mínima para decidir (objetivo, últimos intentos, último error), no todo el registro.
- **Escalar tarde.** La escalada debe dispararse por sin progreso o repetición, no solo por el tope.

## Límites y cuándo no aplica

En `SE-581` se simularon cinco reglas sobre 4 000 tareas sintéticas con parámetros del autor y semilla 497; no se midió ningún agente real, ni el costo en dinero, ni el efecto de cambiar de plan en un modelo concreto. `SE-588` declara también lo que un informe de este tipo no cubre: un adversario adaptativo, procesos hijos y red fuera del confinamiento, y la productividad. La escalada supone que hay una persona disponible y con autoridad; si nadie recibe el aviso, es una parada con otro nombre.
