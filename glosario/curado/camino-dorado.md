# Camino dorado

## Definición

Un **camino dorado** (o camino pavimentado) es la forma recomendada, soportada y automatizada de realizar una tarea frecuente, como crear un servicio nuevo, con las guardas ya incorporadas (`SE-406`). `SE-489` precisa lo que no es: no es obligatorio. Es una vía fácil y respaldada, no una prohibición de salirse.

## Por qué importa

Sin camino dorado, cada equipo debe recordar por su cuenta los límites de recursos, el usuario sin privilegios, la etiqueta de dueño, las sondas de salud y las imágenes con versión fija; olvidar una guarda es solo cuestión de tiempo. La decisión que cambia es dónde se pone la seguridad y la consistencia: no en documentos que alguien debe leer, sino en el camino que la gente ya recorre. `SE-406` lo resume: el camino más fácil debe ser también el correcto.

## Cómo funciona

El mecanismo es económico antes que técnico. Si lo correcto exige más pasos que lo incorrecto, la gente elige lo incorrecto; por eso el camino automatiza lo correcto y baja su costo por debajo de la alternativa manual. Incluye las guardas por defecto, de modo que un servicio creado por el camino nace conforme.

Como no es una obligación, quien tenga una necesidad distinta puede apartarse, asumiendo el costo de mantener lo suyo. Esa salida no se prohíbe; se registra (el programa lo relaciona con la excepción registrada) para que el equipo de plataforma vea qué casos el camino no cubre.

`SE-489` añade cómo saber si funciona: se mide, no se supone. Dos indicadores bastan para empezar: la **cobertura** (qué parte de las tareas pasa por el camino) y el **costo de empezar** (pasos para llegar a algo funcionando). Un camino con baja cobertura o con costo alto de arranque es un camino que nadie usa.

## Ejemplo

Una plataforma ofrece una plantilla que, al crear un servicio, genera el despliegue con límites de recursos, usuario sin privilegios, etiqueta de dueño, sondas de salud e imágenes fijadas. Un equipo con un requisito especial se aparta, documenta la excepción y mantiene su propia configuración. Ilustración del mecanismo de `SE-406`.

## Errores y confusiones comunes

- **Nadie usa el camino dorado** (`SE-489`): causa, cobertura baja o costo de empezar alto; corrección, medir ambos y ampliar la cobertura o simplificar el inicio.
- **Volverlo obligatorio**: pasa a ser un estándar impuesto y pierde la señal que da la excepción.
- **Confundirlo con una plantilla pasiva**: sin soporte y automatización no es un camino, es un ejemplo.
- **Medir solo cuántos servicios tiene la plataforma** en vez de cuántos equipos lo eligen.

## Límites y cuándo no aplica

Vale para tareas frecuentes y parecidas entre equipos; para un caso único, construir el camino cuesta más de lo que ahorra. Un camino que cubre mal los casos reales se vuelve un proyecto de infraestructura con su propia agenda, como advierte `SE-406` de las plataformas sin usuarios identificados. Y las guardas incorporadas envejecen: requieren mantenimiento.
