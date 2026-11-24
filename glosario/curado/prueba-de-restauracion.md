# Prueba de restauración

## Definición

La **prueba de restauración** es el ejercicio que restaura una copia en un entorno aislado y verifica su contenido y su tiempo (`SE-357`). Es la única prueba de la hipótesis de que se puede volver: una copia que nunca se restauró es una suposición.

## Por qué importa

Hacer copias de seguridad es fácil; recuperar es lo que cuenta. Las copias pueden estar incompletas, corruptas, inconsistentes o simplemente ser inutilizables con los procedimientos que el equipo conoce. La decisión que cambia es qué se considera «respaldado»: no lo que tiene una copia, sino lo que se ha restaurado con éxito, y en qué tiempo.

## Cómo funciona

`SE-357` define el procedimiento: restaurar una copia reciente en un entorno aislado, ejecutar la verificación, medir el tiempo y registrar quién lo hizo y qué falló. Dos reglas de frecuencia:

- **Periódica**: una copia no ensayada en el último trimestre se considera **no verificada**.
- **Tras cada cambio** que afecte al respaldo: una migración, un cambio de proveedor.

La verificación debe ser **de negocio**, no solo estructural: una copia ingenua tomada con la base en uso puede restaurarse «con éxito» y tener datos erróneos, porque cada página es válida pero el conjunto no corresponde a ningún instante. Por eso la clase combina la prueba de restauración con la copia consistente: la primera prueba el camino de vuelta, la segunda garantiza el contenido.

También hay que ensayar el **caso inverso**: qué pasa cuando la última copia está dañada y hay que usar la anterior, y cuántos datos más se pierden. Eso conecta con el objetivo de punto de recuperación: la restauración mide el tiempo realmente necesario (que alimenta el RTO) y revela cuánta información se pierde (el RPO real).

## Ejemplo

Cada trimestre, el equipo restaura la copia más reciente en un entorno aislado, ejecuta consultas de verificación de negocio (totales, conteos, relaciones), mide cuánto tarda y anota quién lo hizo y qué falló. En una prueba descubren que el procedimiento depende de una clave que solo conocía una persona. Lo corrigen antes de necesitarlo. Ilustración del procedimiento de `SE-357`.

## Errores y confusiones comunes

- **La restauración termina bien y los datos son erróneos**: copia ingenua con la base en uso; se corrige con la API de copia consistente y verificación de negocio.
- **Se pierden horas de trabajo tras un borrado accidental**: solo copia diaria y sin registro de cambios; se corrige archivando el registro para recuperar a un instante.
- **Comprobar solo que el archivo existe o que el motor arranca**.
- **No registrar quién y cómo**: el conocimiento queda en una persona.

## Límites y cuándo no aplica

`SE-357` aclara que sus experimentos usan bases pequeñas de SQLite y datos sintéticos; no se midió el tiempo de restauración con volumen real ni se probó cifrado, almacenamiento remoto, otro motor o datos de producción. Una restauración probada en un entorno aislado no garantiza el tiempo en una emergencia real (con otro volumen, otra red y menos calma). Y verifica un momento: la copia de hoy, no las futuras.
