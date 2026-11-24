# Postmortem sin culpa

## Definición

Un **postmortem sin culpa** (*blameless postmortem*) es la revisión posterior a un incidente que parte de que cada persona actuó con la mejor información y las herramientas disponibles, y que busca los factores del sistema que hicieron posible el fallo. Es la definición de `SE-501`; `SE-611` lo resume como el análisis de un incidente centrado en el sistema y no en las personas. El **postmortem** es el documento que reconstruye el incidente para aprender de él; **sin culpa** es el principio con que se hace.

## Por qué importa

Decide si la organización aprende o esconde información. `SE-501` da la razón práctica: si nombrar una acción propia tiene consecuencias personales, la información se esconde, y sin información el análisis es mentira. Cambia además dónde se buscan las correcciones: no en «tener más cuidado», sino en el diseño, las señales y los procesos.

## Cómo funciona

El análisis pregunta *por qué esa acción tenía sentido en ese momento*, *qué señales faltaban* y *qué hacía fácil equivocarse*. No elimina la responsabilidad: la **desplaza del individuo al sistema** que dejó un camino fácil hacia el fallo.

`SE-501` señala un obstáculo cognitivo, el **sesgo de retrospectiva**: quien conoce el desenlace lo ve como previsible y juzga la decisión con información que entonces no existía. Una forma de contrarrestarlo es reconstruir la línea de tiempo con las señales que la persona realmente veía.

Lo que convierte el documento en mejora son las **acciones verificables**: cada una con propietario, fecha y forma de comprobar que se hizo, con seguimiento semanal. Sin eso, el postmortem es literatura.

## Ejemplo

Una persona ejecutó un comando de limpieza en el entorno equivocado. Un postmortem con culpa concluye «error humano; se le recuerda el procedimiento». Uno sin culpa pregunta: ¿por qué el terminal de producción y el de pruebas se veían iguales?, ¿por qué el comando no pedía confirmación?, ¿por qué la persona tenía permiso de borrado en producción sin segundo aprobador? Las acciones resultantes son cambios del sistema: color y nombre distintos del entorno, confirmación y permisos más estrechos, cada una con propietario y fecha. (Ilustración propia; las clases tratan incidentes sintéticos con tiempo virtual.)

## Errores y confusiones comunes

- **El postmortem culpa a una persona.** Se detuvo en «error humano»; corrección de `SE-501`: preguntar por qué la acción tenía sentido y qué la facilitó.
- **El incidente se repite.** Las acciones carecen de propietario, fecha o verificación; hay que hacerlas verificables y darles seguimiento.
- **Creer que «sin culpa» es «sin responsabilidad».** Se mantiene la responsabilidad, pero del sistema y de quien lo diseña o decide.
- **Escribirlo solo para cumplir.** Si nadie lee ni actúa sobre él, no cumple su función.

## Límites y cuándo no aplica

Las definiciones de `SE-501` son operativas para la API de entregas y sus experimentos usan tiempo virtual y semillas fijas. El enfoque sin culpa no ampara la negligencia deliberada ni el ocultamiento: si alguien incumple a propósito una regla, es otro asunto, y se trata con otros mecanismos. Funciona solo si hay cultura que lo sostenga: un documento que declara «sin culpa» mientras la gestión penaliza a quien habla destruye la confianza que pretendía crear. En `SE-611` la idea se extiende a incidentes de modelos, donde además hay que reconstruir datos y versiones.
