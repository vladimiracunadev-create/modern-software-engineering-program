# Durabilidad

## Definición

La **durabilidad** es la probabilidad de no perder un dato durante un periodo (`SE-440`, disponibilidad, durabilidad y recuperación). `SE-256` usa el término con un matiz de almacenamiento local: la propiedad de que una escritura confirmada sobreviva a una caída, cuyo costo crece con la frecuencia con que se fuerza la sincronización con el almacenamiento. En la «D» de ACID es la misma idea vista desde una transacción.

## Por qué importa

Se confunde con la disponibilidad y no es lo mismo. Un sistema puede estar caído una hora sin perder nada, o estar siempre disponible y perder el 0,01 % de los datos al año (`SE-440`). La decisión que cambia es dónde se invierte: copias, velocidad de reparación, diario de operaciones y claves de idempotencia.

## Cómo funciona

`SE-440` modela un objeto con N réplicas independientes que fallan con tasa anual λ y se reparan en R horas. Se pierde el objeto cuando fallan todas durante la ventana de reparación. La aproximación de primer orden es 8 760 · N · (λ/8 760)ᴺ · Rᴺ⁻¹. Dos conclusiones:

- La pérdida crece con λᴺ: tres réplicas hacen la tasa de pérdida proporcional al cubo de la tasa de fallo.
- Pero también crece con Rᴺ⁻¹: con tres copias, con el cuadrado del tiempo de reparación. Por eso el tiempo de reparación pesa más que el número de copias.

En el almacenamiento local de `SE-256`, la durabilidad de una escritura exige forzar la sincronización con el disco; hacerlo en cada escritura cuesta rendimiento, y hacerlo menos expone a perder lo reciente ante una caída. En `SE-600`, sin diario de operaciones y clave de idempotencia, un reinicio produce duplicados.

## Ejemplo

El equipo de `SE-440` escribe el presupuesto de fiabilidad: promete 99,5 % de disponibilidad mensual en el horario de entregas (unas 3,6 horas de caída al mes) y lo desglosa por capa, declarando una causa común de despliegue. Ilustración propia de durabilidad: si una réplica tarda 24 h en reconstruirse y otra falla en ese intervalo, el objeto sigue vivo con la tercera; si la reparación tarda dos semanas, la ventana de riesgo crece mucho.

## Errores y confusiones comunes

- **Equiparar durabilidad con disponibilidad.**
- **Contar réplicas como independientes** cuando comparten una causa común.
- **Creer que más copias bastan:** si la reparación es lenta, no.
- **Confirmar una escritura antes de que sea durable** en almacenamiento local (`SE-256`).

## Límites y cuándo no aplica

El modelo supone fallos independientes y tasas constantes; no cubre corrupción silenciosa ni errores humanos (borrar por error), que una copia replicada propaga. Las cifras de `SE-440` son del presupuesto ilustrativo de la clase. No sustituye las copias de seguridad ni las pruebas de restauración.
