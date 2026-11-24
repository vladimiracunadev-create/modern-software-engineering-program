# Prueba de integración

## Definición

Una **prueba de integración** ejecuta dos o más piezas reales juntas y comprueba el acuerdo entre ellas (`SE-423`).

## Por qué importa

Los componentes se comunican por interfaces (una respuesta JSON, una tabla compartida, una cola) y cada uno asume algo sobre la otra parte: nombres, tipos, valores posibles, orden, cuántos elementos por página. Un defecto de integración es una asunción que ya no se cumple. Ninguna prueba de una sola parte lo ve, porque cada una se comprueba contra su propia versión de la asunción.

## Cómo funciona

La prueba ejecuta las piezas reales y verifica que la asunción de una coincide con el comportamiento de la otra. Se complementa con **contratos por consumidor**: el proveedor ejecuta en su integración continua un archivo por consumidor que lista los campos, tipos y valores que ese consumidor usa, y falla con el nombre del consumidor afectado.

## Ejemplo

`SE-423`: el servicio de notas guarda una carpeta `contratos/` con `panel.json`, `exportador.json` y `avisos.json`; su integración continua ejecuta los tres en cada propuesta de cambio. Los consumidores abren un contrato cuando empiezan a usar un campo y retiran cláusulas que dejaron de usar. Las pruebas de integración del panel lo ejecutan contra la respuesta real del servicio con una base sembrada.

## Errores y confusiones comunes

- **El consumidor falla en producción y sus pruebas pasan.** El doble refleja una versión antigua del proveedor; verificarlo con el mismo contrato.
- **El proveedor recibe alarmas por cambios que nadie usa.** Comparación de esquema completo; contratos por consumidor.

## Límites y cuándo no aplica

Las pruebas de integración siguen siendo necesarias para lo que el contrato no dice: transacciones, ordenamiento, efectos. Son más lentas y frágiles que las unitarias; se reserva su uso para las interfaces.
