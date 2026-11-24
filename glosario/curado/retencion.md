# Retención

## Definición

La **retención** es el plazo durante el cual se conserva cada tipo de dato (`SE-358`). El programa lo usa con matices cercanos: plazo máximo de conservación (`SE-369`), plazo con su costo en TB-mes (`SE-370`), tiempo con su fundamento (`SE-525`) y, en construcción y releases, la política que decide qué artefactos se conservan y cuánto tiempo (`SE-470`).

## Por qué importa

Conservar datos para siempre «por si acaso» tiene costos: almacenamiento, riesgo en una filtración y a veces falta de base legal para seguir guardándolos. Borrar demasiado pronto destruye lo que debía conservarse. La decisión que cambia es que el plazo de cada tipo de dato se fija con una justificación, no por inercia.

## Cómo funciona

`SE-358` fija cuatro reglas:

1. El plazo depende de la **finalidad** y de las **obligaciones aplicables**, y lo decide la institución con asesoría, no el equipo técnico solo.
2. Una retención sin ejecución es un deseo: hace falta un **trabajo programado de purga**, una **medida de cuánto hay vencido** y un plazo para cada copia.
3. Un registro de accesos conservado «por si acaso» crece sin límite, aumenta el daño de una filtración y puede dejar de tener base para conservarse.
4. El plazo también cubre los **respaldos**: una copia con datos vencidos los conserva hasta que ella misma expira.

`SE-525` añade matiz de modernización: un corte único de retención borra actas que debían conservarse; la corrección son reglas por tipo con fundamento y retención legal, y una tabla de retención con proceso de borrado verificado. `SE-370` pone el costo (TB-mes) como parte de la decisión, y `SE-470` aplica la idea a artefactos: la retención de los artefactos se justifica con la profundidad de los retrocesos que se quieran poder hacer.

Lo que se compra con retención es frente a la compactación: retener descarta por antigüedad, compactar conserva el último valor por clave.

## Ejemplo

La tabla de eventos crece sin parar porque nadie purga. Se define: eventos de depuración, 30 días; registros de acceso, un plazo fijado con asesoría; actas, retención legal. Un trabajo programado borra lo vencido, mide cuánto queda fuera de plazo y alerta si crece. Los respaldos tienen su propio plazo para que los datos vencidos no sobrevivan en ellos. Aplicación de `SE-358`.

## Errores y confusiones comunes

- **La tabla de eventos crece sin parar**: retención sin purga programada; se corrige con un trabajo de purga y medida de lo vencido.
- **Se borran actas que debían conservarse**: corte único de retención; se corrige con reglas por tipo con fundamento.
- **Se guardan datos personales de hace diez años**: no hay retención ni disposición.
- **Olvidar las copias**: el dato vencido sigue vivo en los respaldos.

## Límites y cuándo no aplica

Los plazos concretos son decisiones de cada institución y de la normativa que le aplique; las clases no fijan cifras generales. Retención y borrado deben coordinarse con las obligaciones de conservación (legales o contractuales), que pueden pedir lo contrario de reducir. En un entorno desechable de pruebas sin datos reales, la política formal es innecesaria.
