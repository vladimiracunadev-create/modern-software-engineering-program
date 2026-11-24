# Punto de no retorno

## Definición

El **punto de no retorno** es el paso de una migración desde el cual volver atrás exige un respaldo anterior a él (`SE-354`). `SE-528` lo formula como el paso a partir del cual volver atrás es imposible o destruye datos. Todo cambio que pierde información tiene uno.

## Por qué importa

Una migración con varios pasos mezcla pasos reversibles y otros que no lo son. Si ese límite no se nombra, se cruza sin darse cuenta y la decisión de seguir adelante o de retroceder se toma bajo presión, con el sistema ya roto. La decisión que cambia es que el punto se identifica, se nombra y se prepara antes de ejecutar, con respaldo verificado y criterios de espera.

## Cómo funciona

`SE-354` lo ubica dentro del patrón expandir y contraer. Las fases de expandir y migrar son reversibles: se puede volver al código anterior sin perder datos. Contraer, es decir, quitar la columna o estructura vieja, no lo es: una vez eliminada, volver exige restaurar desde un respaldo anterior a ese paso (`SE-357`). Por eso la clase pide que el plan lo diga con todas las letras: «el paso 4 (quitar `nombre`) es el punto de no retorno; antes de él se toma un respaldo verificado y se espera una semana sin instancias viejas».

La clase observa el riesgo de ocultarlo: las migraciones que mezclan pasos reversibles e irreversibles en un solo despliegue esconden ese punto y obligan a decidir bajo presión. Separar los pasos en despliegues distintos hace que el punto sea un lugar concreto del calendario, con su preparación: respaldo verificado (con prueba de restauración), un periodo de espera sin versiones viejas y la decisión explícita de cruzarlo.

`SE-528` aplica la misma idea a la modernización de sistemas heredados: identificar el paso desde el cual el sistema antiguo ya no se puede reanudar y preparar el ensayo de vuelta atrás antes.

## Ejemplo

Para separar una columna `direccion` en varias, el plan descompone el cambio en fases compatibles. Las tres primeras (añadir columnas nuevas, escribir en ambas, migrar lecturas) son reversibles. La cuarta, quitar `direccion`, es el punto de no retorno: antes se toma un respaldo verificado y se espera una semana sin instancias de la versión vieja. Ejercicio de transferencia de `SE-354`.

## Errores y confusiones comunes

- **Errores en las instancias viejas durante un despliegue**: cambio incompatible hecho en un solo paso; se corrige expandiendo, migrando y contrayendo en despliegues separados.
- **El panel se congela al ejecutar una migración**: actualización de muchas filas en una transacción; se corrige con un relleno por lotes idempotente y reanudable.
- **No nombrar el punto**: se cruza sin decisión consciente.
- **Respaldo no verificado**: sin prueba de restauración no hay vuelta atrás real.

## Límites y cuándo no aplica

No toda migración lo tiene: un cambio solo aditivo y compatible puede revertirse siempre. El respaldo previo permite volver al estado anterior al paso, pero no recupera los cambios hechos después: los datos nuevos escritos tras cruzarlo se pierden al restaurar. Y la espera de una semana es el ejemplo de la clase, no una regla general: depende de cuánto tarde en salir de circulación la última instancia vieja.
