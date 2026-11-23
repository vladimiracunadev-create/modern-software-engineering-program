# SLO

## Definición

Un **SLO** (*service level objective*, objetivo de nivel de servicio) es el valor objetivo de un indicador de nivel de servicio (SLI) durante una ventana de tiempo. `SE-252` lo define como el valor mínimo comprometido de un indicador en una ventana, `SE-419` como el valor objetivo de un SLI en una ventana y `SE-497` como el valor objetivo de un SLI durante una ventana de tiempo. Un ejemplo de `SE-252`: 99,5 % de solicitudes buenas en 30 días. Es una meta interna de fiabilidad: no es lo mismo que un SLA, que es un compromiso contractual.

## Por qué importa

El SLO convierte «el servicio debe ser fiable» en un número, con una ventana, que el equipo y el producto pueden discutir y verificar. De él se deriva el presupuesto de error, que permite decidir cuánto riesgo se puede asumir; `SE-419` muestra que operar un producto incluye guardias con alertas basadas en SLO, que despiertan por consumo de presupuesto y no por cada pico. Sin SLO, la fiabilidad se negocia con adjetivos.

## Cómo funciona

Un SLO se construye sobre un **SLI** y se completa con una ventana y una forma de contar. `SE-497` pide escribir tres decisiones que definen el SLI y que determinan lo que el SLO significa: qué es un evento «bueno» (estado y umbral de latencia), qué es un evento «válido» (qué se excluye) y dónde se mide. A partir de ahí:

- **El objetivo** fija el mínimo aceptable. Con 99,9 % en 30 días, la fracción tolerable es 0,1 %, equivalente a 43,2 minutos de caída total (`SE-497`).
- **El presupuesto de error** es 1 − objetivo y se gasta con incidentes, despliegues y mantenimientos (`SE-419`).
- **Las dependencias componen:** si el servicio depende en serie de otros, su SLO no puede superar el producto de los de sus dependencias (`SE-497`), y por eso hay que revisar la redundancia.
- **El SLA** se fija por debajo del SLO, con margen interno; si el SLA es más estricto que el SLO, se firmó sin margen (`SE-497`).

## Ejemplo

En `SE-497`, la API de entregas define el SLI como la proporción de peticiones con respuesta exitosa en menos de 1 s, con un SLO de 99,9 % en 30 días. El equipo escribe además el límite de la promesa: el SLO no cubre la red del cliente ni los mantenimientos anunciados, y las dependencias externas (almacenamiento y correo) tienen SLO propios, de modo que la disponibilidad compuesta esperada es 99,7 %; se acuerda con producto revisar el objetivo cada cierto tiempo. Son datos sintéticos de la clase.

## Errores y confusiones comunes

- **«El SLO se cumple y hay quejas».** Se mide donde no se ve el problema o se promedia una ventana larga; corrección (`SE-497`): medir cerca de la persona y añadir ventana corta o segmento.
- **Dos paneles con consumos opuestos.** Uno cuenta peticiones y otro minutos; hay que declarar la forma de contar en el SLO.
- **SLA más estricto que el SLO.** Se firmó sin margen interno; el SLA se fija por debajo del SLO.
- **SLO superior al de las dependencias.** Se ignoró la composición en serie; se calcula el producto y se revisa la redundancia.

## Límites y cuándo no aplica

El SLO es tan bueno como su SLI: un SLI de disponibilidad sin umbral de latencia da por buena una respuesta correcta pero lenta (`SE-497`). Las series de `SE-419` son inventadas para mostrar la lectura; en un sistema real el presupuesto se calcula con SLI por solicitud y se consume también por degradaciones parciales, no solo por caídas totales. Un SLA real excluye mantenimientos con aviso y define ventanas distintas (trimestral, anual), cosa que los ejemplos simplificados de la clase no modelan.
