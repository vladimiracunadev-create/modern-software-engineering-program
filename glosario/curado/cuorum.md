# Cuórum

## Definición

El **cuórum** es el número mínimo de réplicas que deben responder o participar para dar una operación por válida (`SE-355`, `SE-390`). En los sistemas sin líder fijo se expresa con tres números: N réplicas por dato, W confirmaciones para escribir y R consultas para leer; la condición `R + W > N` asegura que lectura y escritura se solapen.

## Por qué importa

Cuando un dato vive en varias réplicas, cada operación debe decidir cuántas consultar o confirmar. Pocas hacen el sistema rápido y disponible, pero pueden devolver datos viejos; muchas dan lecturas más actuales a costa de latencia y de tolerar menos caídas. La decisión que cambia es elegir (W, R) con un cálculo, no por defecto ni por «rapidez».

## Cómo funciona

`SE-355` lo explica así. Cada dato vive en N réplicas. Una escritura se confirma al llegar a W réplicas; una lectura consulta R réplicas y se queda con la versión más nueva. Si **R + W > N**, el conjunto de réplicas leídas y el de réplicas escritas siempre comparten al menos una, y por tanto la lectura ve la última escritura confirmada. Si no, puede no verla.

Valores de la clase: con N = 3, W = 2 y R = 2 se cumple la condición y se tolera la caída de una réplica; con W = 1 y R = 1 es el más rápido y el que más lecturas viejas devuelve. `SE-390` lo presenta como número mínimo de réplicas que deben participar y relaciona los errores típicos: una persona que no ve su propia escritura (lectura de una réplica atrasada, corregible con consistencia de sesión o lectura del cuórum) y un cuórum 1/1 elegido sin calcular lo que se pierde.

La propia clase advierte que el cuórum no garantiza consistencia fuerte en todos los casos: hay detalles de escrituras parciales y de relojes. Lo que da es una condición clara y medible.

## Ejemplo

Con N = 3, una escritura llega a las réplicas A y B (W = 2) mientras C está atrasada. Una lectura con R = 2 consulta B y C: B tiene la versión nueva, C la vieja; el lector toma la más nueva y ve la escritura. Con R = 1 podría consultar solo C y devolver un dato viejo. Cálculo directo de la condición de `SE-355`.

## Errores y confusiones comunes

- **Una persona no ve su propia escritura**: lectura de una réplica atrasada; consistencia de sesión o lectura del cuórum (`SE-390`).
- **El cuórum es 1/1 por «rapidez»**: no se calculó lo que se pierde; elegir (W, R) con `W + R > N` si importa lo último.
- **Creer que R + W > N garantiza consistencia fuerte**: no cubre escrituras parciales ni relojes.
- **Confundirlo con el quórum de un consenso con líder**: es una familia de mecanismos distinta, con líder y mayoría.

## Límites y cuándo no aplica

`SE-355` aclara que sus simulaciones no modelan fallos de nodos ni escrituras parciales ni miden latencia o costo de mover datos; el retardo exponencial y la lectura uniforme son supuestos del autor. Si lo importante es disponibilidad o latencia sobre frescura, puede bastar un cuórum bajo; si hay un líder único que ordena las escrituras, la replicación sigue otro modelo y la condición no es la misma.
