# Oportunidades

## Definición

Una **oportunidad** es un problema o necesidad con alcance estimado, consecuencia cuantificable y una ventana en la que actuar tiene sentido (SE-121). No todo problema lo es: se vuelve una cuando alcanza a suficientes personas, con suficiente consecuencia y con una posibilidad razonable de actuar. Es el primer artefacto del descubrimiento de producto en la plataforma de entregas.

## Por qué importa

Permite comparar problemas con números en lugar de con voces. Sin tamaño, frecuencia y ventana, una queja ruidosa compite con una necesidad silenciosa y gana la que se oye más. Cambia la decisión de qué investigar o construir primero: se prioriza por tamaño estimado, y el rango señala qué factor conviene afinar antes de invertir.

## Cómo funciona

SE-121 estima la oportunidad con tres factores: **cuántas personas** la sufren, **con qué frecuencia** y **qué costo** tiene cada ocurrencia. El resultado se expresa como **rango**, porque cada factor es incierto: un número único (400 horas al mes) transmite una precisión que no existe; un rango (de unas 190 a unas 1.700) muestra cuánto del tamaño es conocimiento y cuánto suposición. Además, el rango indica qué factor es más sensible: es el que conviene investigar primero.

La clase construye el primer artefacto con tickets sintéticos: agrupa por causa (la más frecuente es la expiración de sesión), formula un enunciado de problema y estima el rango. Un detalle importante es contar por **causa**, no por frase: varias redacciones de una misma causa quedan dispersas si se cuenta el texto. La corrección es etiquetar la causa por ticket, con quién y cuándo, y conservar el texto original. Y otro: no aceptar la petición original como requisito; se reformula como necesidad («necesito… para…») antes de proponer opciones, o la reunión discute la solución durante una hora sin acordar el problema.

## Ejemplo

Con los tickets de la plataforma, la causa más frecuente es la expiración de sesión durante la entrega. Si afecta a entre 300 y 1.000 estudiantes al mes, con una a tres ocurrencias por persona y un costo de 10 a 20 minutos cada una, el producto de los extremos da un rango de decenas a cientos de horas: ancho, pero suficiente para decir que merece investigarse frente a un problema de decenas de minutos. (Cifras de ejemplo en la línea del método de SE-121; los datos de la clase son sintéticos.)

## Errores y confusiones comunes

- **Priorizar una falla que, al arreglarla, no reduce los tickets**: se contó la frase y no la causa.
- **Discutir la solución sin acordar el problema**: se aceptó la petición como requisito.
- **Dar una cifra única con falsa precisión.**
- **Confundir oportunidad con idea de producto**: la oportunidad es el problema con tamaño; la idea es una respuesta posible.

## Límites y cuándo no aplica

El rango depende de datos de calidad variable (tickets sintéticos en la clase, que ilustran el método y no miden un producto real). Una oportunidad grande puede carecer de ventana de acción (no hay forma razonable de resolverla ahora). Y el tamaño no es el único criterio: riesgos, dependencias y estrategia también cuentan al decidir.
