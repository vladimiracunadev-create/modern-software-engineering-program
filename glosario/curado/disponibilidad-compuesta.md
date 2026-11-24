# Disponibilidad compuesta

## Definición

La **disponibilidad compuesta** es la disponibilidad de un sistema que depende de varios componentes, calculada combinando las de cada uno. En serie (hacen falta todos) es el producto de las disponibilidades; en paralelo (basta uno) la indisponibilidad es el producto de las indisponibilidades. `SE-419` y `SE-535` la enuncian para la cadena en serie y `SE-405` desarrolla el cálculo completo.

## Por qué importa

La disponibilidad que se promete al cliente no es la de un componente sino la del conjunto. Sumar componentes fiables en serie reduce el total; duplicar un componente lo mejora, pero solo bajo condiciones. La decisión que cambia es dónde se invierte para subir la disponibilidad y qué se comprueba antes de creer una cifra de «nueves».

## Cómo funciona

`SE-405` da los tres cálculos que hay que distinguir:

1. **Paralelo con conmutación perfecta**: si dos componentes fallan de forma independiente y cualquiera basta, la indisponibilidad es el producto. Dos proveedores de 99,95 % dan 1 − 0,0005² = 99,99997 %.
2. **Serie**: si el servicio necesita a ambos a la vez, como una réplica síncrona, la disponibilidad es el producto de las disponibilidades: baja a 99,90 %.
3. **Techo de un componente compartido**: un componente en serie con el par, como el DNS que decide el destino, impone su propio techo: 99,95 % × 99,99997 % ≈ 99,95 %.

La lección de la clase es que la ganancia de un segundo proveedor existe solo si **la conmutación funciona, los fallos son independientes y nada común queda en el camino**. Los tres supuestos son las condiciones; fallar cualquiera anula el beneficio calculado. `SE-419` y `SE-535` aplican la misma aritmética a la cadena de dependencias de un producto y a un sistema que depende en serie de varios componentes.

## Ejemplo

Una plataforma usa dos proveedores de 99,95 % en paralelo y cree llegar a 99,99997 %. Pero ambos se resuelven por el mismo DNS, que está en serie con el par: el techo vuelve a ser 99,95 %. Además, si la conmutación nunca se ensayó y falla la mitad de las veces, el valor real queda lejos del calculado. Cálculo de `SE-405` con proveedores ficticios.

## Errores y confusiones comunes

- **Dos proveedores y la misma caída anual**: un componente compartido en serie; se corrige dibujando las dependencias y eliminando o duplicando el común.
- **La conmutación falla cuando se necesita**: nunca se ensayó; se ensaya con regularidad y se mide su acierto.
- **Multiplicar disponibilidades de componentes correlacionados**: asume independencia que puede no existir.
- **Creer en el SLA de un proveedor como disponibilidad propia**: el crédito de servicio compensa, no restituye.

## Límites y cuándo no aplica

`SE-405` precisa que sus proveedores son ficticios y que no se midió ningún enlace real: la disponibilidad, la independencia, las probabilidades de oferta y el precio de salida son supuestos del autor. El modelo de producto asume independencia; los fallos correlacionados (un mismo despliegue, una misma región) empeoran el resultado. No describe degradación parcial ni latencia, solo si el servicio está arriba o abajo.
