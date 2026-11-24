# Hipótesis falsable

## Definición

Una **hipótesis falsable** es una afirmación sobre el mundo, con un umbral y una regla de decisión fijados antes de observar, que algún resultado posible refutaría (SE-124). SE-505 la usa en ingeniería del caos: la afirmación de que el estado estable se mantendrá bajo una condición, con una regla que dice qué observación la refuta.

## Por qué importa

Una hipótesis que ninguna observación puede contradecir no orienta ninguna decisión. La falsabilidad distingue una hipótesis de una esperanza. Cambia cómo se diseña una prueba de producto o un experimento: antes de mirar los datos se decide qué resultado haría cambiar de rumbo.

## Cómo funciona

SE-124 contrasta dos frases. «Los estudiantes valoran la confirmación de entrega» **no puede fallar**: cualquier resultado se interpreta a favor. «Al menos 6 de cada 10 estudiantes que ven la confirmación no repiten la entrega en 48 horas» **sí puede fallar**: si menos de 6 de cada 10 no repiten, queda refutada. Tiene un **umbral** (6 de 10), una **medida observable** (no repetir en 48 horas) y una **ventana**.

Se completa con la **regla de decisión**: qué se hará si el resultado queda por debajo, por encima o en medio (por ejemplo, construir, descartar o seguir probando). Fijar umbral y regla **antes de observar** evita ajustar el criterio a lo que salió. Y se combina con la incertidumbre: con 4 de 20 y con 40 de 200 la tasa observada es la misma (20 %), pero la certeza no; la clase pide predecir el resultado de ambos con la regla fijada, y la muestra grande es la que permite concluir.

Hay dos errores típicos con su causa. Un piloto que «confirma» la idea y la ampliación no la confirma: la conclusión se sacó de una muestra pequeña sin fijar umbral ni confianza; se corrige declarando de antemano el tamaño, el umbral y la probabilidad exigida, y calculando la posterior. Y el equipo que mide el alcance durante semanas sin avanzar: contrastó el supuesto más cómodo y no el más sensible; se corrige calculando la oscilación de cada supuesto y contrastando primero el de mayor sensibilidad e incertidumbre.

En ingeniería del caos (SE-505), la hipótesis dice que el estado estable se mantiene bajo una condición (una falla inyectada) y la regla define qué observación (una métrica fuera de rango) la refuta.

## Ejemplo

Hipótesis: «Con la confirmación de entrega visible, al menos el 60 % de las estudiantes no repite la entrega en 48 horas». Regla: con 200 observaciones, si el intervalo del 95 % queda por encima de 55 %, se construye; si queda por debajo de 55 %, se descarta; si lo atraviesa, se amplía la muestra. (Ilustración construida con el estilo de SE-124.)

## Errores y confusiones comunes

- **Hipótesis que no puede fallar.**
- **Fijar el umbral después de ver los datos.**
- **Piloto pequeño tomado como confirmación.**
- **Contrastar lo cómodo y no lo sensible.**

## Límites y cuándo no aplica

Falsar una hipótesis no prueba su contraria ni dice por qué falló. En fases muy exploratorias, antes de saber qué medir, conviene primero investigar y luego formular. Un umbral mal elegido hace la hipótesis trivial o inalcanzable.
