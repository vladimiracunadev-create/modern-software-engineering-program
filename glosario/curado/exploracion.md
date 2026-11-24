# Exploración

## Definición

La **exploración** (pruebas exploratorias) es la actividad simultánea de aprendizaje, diseño y ejecución de pruebas con una misión (`SE-429`).

## Por qué importa

Encuentra lo que nadie previó y que un guion escrito no puede encontrar. Pero solo es profesional si deja rastro: sin misión ni registro, «exploramos» no significa nada.

## Cómo funciona

Una sesión de exploración es un bloque de tiempo acotado (por ejemplo, 60 a 90 minutos) con una misión: «explorar la subida de archivos buscando pérdidas de datos». La misión limita el alcance sin escribir los pasos; el registro anota qué se hizo, qué se encontró y qué dudas surgieron. Lo que la distingue de «jugar» es que existe una misión y un registro; lo que la distingue de una prueba escrita es que los pasos se deciden sobre la marcha. Se prepara con una lista de sondas, que no la sustituye.

## Ejemplo

`SE-429`: un guion aleatorio de 60 acciones no halla ninguno de los 12 defectos y el equipo concluye que la aplicación «está bien»; ejecutar 480 acciones o dirigirse con sondas cambia la conclusión. La falta de hallazgos no prueba ausencia de defectos.

## Errores y confusiones comunes

- **«Exploramos» y nadie sabe qué se hizo.** Sin misión ni registro; misión acotada y notas de sesión.
- **La herramienta de accesibilidad pasa y una persona no puede usar la página.** Solo se probó lo que una regla decide; revisión manual con tecnologías de apoyo.

## Límites y cuándo no aplica

Depende de la habilidad de quien explora y no es repetible como una prueba automática; los defectos encontrados deben convertirse en pruebas de regresión.
