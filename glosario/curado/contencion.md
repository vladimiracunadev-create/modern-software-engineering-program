# Contención

## Definición

En el sentido principal del programa, **contención** es la fracción del tiempo que las tareas pasan esperando un cerrojo (`SE-386`, memoria compartida, locks y condiciones de carrera). El término es ambiguo y otras clases lo usan de otra manera: en `SE-287` y `SE-588`, *contener* es lograr que un comportamiento no alcance lo que no debería (tiempo, memoria, archivos, entorno, red) o no produzca su efecto dañino. Esta entrada desarrolla sobre todo el primer sentido y señala el segundo para no confundirlos.

## Por qué importa

Un cerrojo demasiado grueso serializa el servicio: aunque haya muchos hilos, trabajan de uno en uno. Medir la contención dice si dividir un cerrojo vale la pena antes de hacerlo, porque dividir multiplica cerrojos y riesgo de interbloqueo.

## Cómo funciona

`SE-386` separa dos ideas:

- **Granularidad:** cuánto dato protege un cerrojo. Uno global es fácil de razonar y serializa todo; uno por curso deja avanzar cursos distintos a la vez, pero multiplica los cerrojos y el riesgo de interbloqueo si una operación toca varios.
- **Contención:** la fracción del tiempo que las tareas pasan esperando. Depende de cuántas tareas compiten y de cómo se reparten las claves.

El matiz importante es el reparto: si unos pocos cursos concentran las entregas del cierre de plazo, dividir por curso ayuda menos de lo que sugiere el número de cerrojos, porque casi toda la espera se concentra en tres.

## Ejemplo

El panel de la docente en `SE-386` no añade un cerrojo global. Primero separa dos casos: el contador de entregas pasa a una operación atómica de la base (`UPDATE curso SET entregas = entregas + 1`), que no necesita cerrojo en el programa; el cupo de la tarea (leer, comprobar, descontar) se protege con una transacción que bloquea esa fila. Para las rutas que tocan curso y estudiante fija un orden, curso antes que estudiante, verificado por una prueba. Mide cuántas peticiones del cierre caen en los tres cursos más populares y decide no partir más por curso.

## Errores y confusiones comunes

- **Pensar que más cerrojos siempre baja la espera:** con claves concentradas no lo hace.
- **Añadir un cerrojo donde basta una operación atómica de la base.**
- **Dividir sin ordenar los cerrojos**, lo que invita al interbloqueo.
- **Confundirlo con el sentido de seguridad** de `SE-287`/`SE-588` (contención de un efecto dañino), que no tiene que ver con cerrojos.

## Límites y cuándo no aplica

La contención se mide, no se supone: sin medición del reparto de claves la decisión es una conjetura. Con poca concurrencia o secciones críticas muy cortas, el costo de la espera no justifica un diseño más fino. Y este sentido no cubre la contención en red o en disco, que son otros recursos compartidos con otras causas.
