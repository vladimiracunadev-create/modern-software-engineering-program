# Modelo de ingreso

## Definición

Un **modelo de ingreso** es la regla que convierte el uso o la presencia de un cliente en dinero: cobrar por alumno, un precio plano por centro, un nivel gratuito con conversión a pago (SE-133). Es una de las decisiones de un modelo de negocio y se distingue del precio concreto: el modelo dice *por qué unidad* y *bajo qué condiciones* se cobra.

## Por qué importa

El mismo uso produce ingresos muy distintos según el modelo. Elegirlo es elegir quién asume el riesgo y qué conducta se premia. Cambia decisiones de producto: qué funcionalidad se limita, a quién se vende, qué métrica se vigila y cuánto cuesta servir a cada cliente.

## Cómo funciona

SE-133 compara tres modelos de la plataforma de entregas con su mecanismo:

- **Por alumno**: el ingreso crece con el tamaño del centro y con el costo de servirlo; el riesgo de que el uso baje recae en quien vende, porque el ingreso baja con el uso.
- **Precio plano por centro**: simplifica la venta, pero subsidia a los grandes (pagan lo mismo que los pequeños aunque cuesten más de servir) y desconecta el ingreso del uso.
- **Nivel gratuito**: reduce la fricción de entrada y traslada el costo de servir a quienes pagan; solo funciona si una fracción suficiente convierte.

Ninguno es mejor en abstracto: cada uno reparte de otra manera el riesgo («¿quién paga si el uso baja?») y el incentivo («¿qué se premia?»). Por eso la clase dice que elegir modelo es elegir qué hipótesis se apuesta a sostener, y que el Business Model Canvas ayuda a nombrarla, no a probarla. La prueba viene de un modelo de viabilidad con supuestos explícitos: una fila por supuesto (nombre, unidad, mínimo, moda, máximo, fuente y estado: medido, derivado o suposición), de modo que cambiar una fila cambia la fecha del resultado y alguien puede recalcular con otros valores.

## Ejemplo

SE-133 muestra con un modelo de viabilidad por qué no basta un número: la hoja da «11 veces» (ingreso sobre costo) y la dirección pide más ventas sin preguntar nada, porque se informó la razón con valores centrales y sin intervalo; la corrección es informar p5, mediana y p95 con el supuesto que más contribuye. Y un plan que se equilibra en el mes 4 puede agotar la caja en el mes 8 si se miró el flujo mensual y no la caja acumulada: se calcula la caja mínima y se financia hasta ese punto.

## Errores y confusiones comunes

- **Informar la razón con valores centrales y sin intervalo.**
- **Mirar el flujo mensual y no la caja acumulada.**
- **Confundir modelo de ingreso con precio**: el precio puede cambiar sin cambiar el modelo.
- **Elegir un modelo copiando a otro sector** sin revisar quién paga el costo de servir.

## Límites y cuándo no aplica

El modelo depende de supuestos que el equipo no controla (disposición a pagar, tasa de conversión). Los rangos de SE-133 son del autor y su modelo no reemplaza datos reales; las cifras sirven para mostrar el razonamiento. En productos con un solo cliente grande o contrato a medida, el «modelo» es una negociación, no una regla general.
