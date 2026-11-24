# Inyección de fallas

## Definición

La **inyección de fallas** es introducir a propósito una falla controlada para comprobar que el sistema la detecta y se recupera (`SE-611`). `SE-384` la usa en el sentido más concreto de provocar caídas, duplicados, retrasos y mensajes inválidos para comprobar las invariantes de un flujo. Es la técnica de base de la ingeniería del caos.

## Por qué importa

Un diseño que *declara* resiliencia (hay tiempos de espera, reintentos y cortacircuitos) no es lo mismo que una resiliencia *demostrada*, el comportamiento observado cuando alguien provocó la falla. La decisión que cambia es cómo se gana confianza: no por la lectura del diseño, sino por haber visto al sistema fallar y recuperarse en condiciones controladas.

## Cómo funciona

El mecanismo es el de un experimento: se define qué se espera (el estado estable o las invariantes), se provoca una falla acotada y se observa si lo esperado se mantiene. En `SE-384`, las fallas provocadas son caídas del consumidor, duplicados, retrasos y mensajes inválidos; lo que se comprueba son las cinco invariantes del flujo (una calificación por entrega, un aviso como máximo, etc.). Si una invariante se viola, se sabe qué mecanismo falta.

`SE-611` fija las precondiciones. Ensayar con inyección de fallas en un sistema que **no tiene aún monitores ni runbook** produce un incidente en lugar de un ensayo: primero el diseño y las pruebas por separado. Y en producción real las fallas necesitan **límites**: un segmento, una fracción, una hora acordada, y un acuerdo previo con quien está de guardia. Esos límites son los mismos que usa la ingeniería del caos: alcance acotado, grupo de control, condición de aborto.

La clase además es honesta con su alcance: el taller usa un modelo y datos sintéticos en una máquina de escritorio, y no sustituye un ensayo de recuperación completo con la infraestructura real (`SE-502`).

## Ejemplo

Un equipo quiere comprobar que un mensaje inválido no detiene el flujo. Inyecta un mensaje mal formado entre mil válidos y observa: los demás se procesan y el inválido termina en la cola de mensajes fallidos, visible y con alarma. Si el flujo se detuviera, la prueba habría revelado la falta de esa cola. Escenario basado en `SE-384`.

## Errores y confusiones comunes

- **Inyectar sin monitores ni runbook**: produce un incidente real en vez de un ensayo (`SE-611`).
- **Inyectar sin límites** en producción: segmento, fracción y hora acordada son parte del diseño.
- **Confundirla con una prueba de carga**: busca fallos, no capacidad.
- **Considerar el ensayo sintético un ensayo de recuperación completo**.

## Límites y cuándo no aplica

No se hace en sistemas que no pueden ya observarse ni recuperarse, ni sin permiso de quienes operan. Un ensayo con modelo sintético demuestra la lógica del diseño, no el comportamiento de la infraestructura real. Y lo que se prueba es solo lo que se inyectó: una recuperación comprobada para una falla no implica que lo sea para otra.
