# Gravedad de los datos

## Definición

La **gravedad de los datos** es la tendencia de las aplicaciones a ubicarse donde están los datos, por el costo y el tiempo de moverlos (`SE-405`). Mover código es barato; mover datos no. Cuanto más pesan los datos, más condicionan dónde vive todo lo demás.

## Por qué importa

Las decisiones de proveedor, de nube o de regiones se toman a menudo pensando en el cómputo, y los datos se mueven después. La gravedad hace que esa secuencia sea cara: salir de un proveedor, o ejecutar en otro, depende más del volumen de datos que del código. La decisión que cambia es cuándo se decide la portabilidad: al diseñar, no el día que se quiere salir.

## Cómo funciona

`SE-405` identifica tres componentes del costo de mover datos:

- **Tiempo**: tarda según el tamaño y el ancho de banda.
- **Dinero**: cuesta según la tarifa de salida del proveedor.
- **Atracción**: siguen atrayendo a las aplicaciones que los usan, porque ejecutar lejos de ellos añade latencia y más tráfico de salida.

El tercer componente es el que da nombre a la metáfora: una aplicación lejos de los datos paga latencia en cada consulta y tráfico de salida en cada transferencia; esa presión empuja a poner la aplicación junto a los datos, y entonces más aplicaciones se acercan, y los datos pesan aún más. La consecuencia práctica es una forma de dependencia (un acoplamiento al proveedor) que no aparece en el código, sino en el volumen.

La respuesta que enseña la clase es de diseño: formatos abiertos y exportaciones periódicas, de modo que la portabilidad de los datos exista antes de necesitarla. Eso mantiene abierta la opción de moverlos y limita el poder de negociación del proveedor, aunque no elimina el costo de transferencia.

## Ejemplo

Una plataforma guarda el histórico de entregas en un servicio de un proveedor. Al querer ejecutar un análisis en otro proveedor, calcula el tiempo de transferencia según el ancho de banda y la tarifa de salida, y comprueba que la copia tarda días y cuesta más que el cómputo del análisis. Una exportación periódica en formato abierto habría permitido hacerlo con menos fricción. Razonamiento ilustrativo según `SE-405`, con cifras de proveedores ficticios.

## Errores y confusiones comunes

- **Asumir portabilidad porque el código es portable**: los datos no lo son al mismo ritmo.
- **Decidir la nube sin estimar volumen y tarifa de salida**.
- **Confundirla con el acoplamiento del código al proveedor**: es un efecto distinto, que se mide en terabytes y euros.
- **Posponer la exportación**: el costo de mover sube con el volumen.

## Límites y cuándo no aplica

`SE-405` indica que sus proveedores son ficticios y que la disponibilidad, la independencia de fallos y el precio de salida son supuestos del autor; no hay medición de enlaces reales. Con volúmenes pequeños, mover los datos es barato y la gravedad es despreciable. Y la gravedad es una tendencia, no una ley: se puede reducir con replicación, formatos abiertos y arquitecturas pensadas para ejecutar cerca de los datos.
