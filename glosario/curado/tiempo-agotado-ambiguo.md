# Tiempo agotado ambiguo

## Definición

Un **tiempo agotado ambiguo** es la ausencia de respuesta que no permite saber si la operación se ejecutó (`SE-389`). Cuando el cliente espera y no recibe nada, no puede distinguir entre varias historias posibles, y la decisión de qué hacer a continuación se toma a ciegas.

## Por qué importa

Es la raíz de muchos duplicados y de muchas pérdidas en sistemas distribuidos. Reintentar «por si acaso» puede ejecutar dos veces una acción que ya ocurrió; no reintentar puede dejar sin hacer una que nunca llegó. La decisión que cambia es que los reintentos solo se hacen sobre operaciones que lo toleran, y que de las demás se consulta el estado.

## Cómo funciona

`SE-389` enumera las tres historias que caben cuando no hay respuesta:

1. La petición se perdió y **no se ejecutó**.
2. Se ejecutó y **la respuesta se perdió**.
3. Se ejecutó y **la respuesta llegará tarde**.

Desde fuera son idénticas. La clase no las distingue, las reparte: con pérdidas simétricas, **más de la mitad** de los tiempos agotados corresponde a una operación ya ejecutada. Por eso reintentar sin precaución es peligroso.

La consecuencia de diseño: reintentar es seguro solo si la operación es **idempotente** o va con una **clave de idempotencia** que permita al servidor reconocer el duplicado (`SE-392`). Si no lo es, el cliente debe **consultar el estado** en lugar de repetir. Esto conecta con el detector de fallos, que tiene la misma incertidumbre a nivel de nodo (¿caído o lento?), con el presupuesto de reintentos, que acota el efecto de insistir, y con el timeout, que decide cuánto esperar antes de declarar la ambigüedad.

## Ejemplo

Un cliente envía el cobro de una inscripción y el tiempo se agota. Si reintenta sin clave de idempotencia, puede cobrar dos veces. Con una clave de idempotencia, el servidor reconoce el segundo envío como duplicado y devuelve el resultado del primero. Alternativamente, el cliente consulta si la inscripción ya figura como pagada antes de repetir. Resolución descrita en `SE-389`.

## Errores y confusiones comunes

- **Registros duplicados tras una lentitud**: reintento de una operación ya ejecutada; se corrige con clave de idempotencia o consulta del estado.
- **El servicio de abajo cae cuando el de arriba se recupera**: reintentos multiplicados por varias capas; se corrige reintentando en una sola capa con presupuesto.
- **Interpretar el timeout como fallo seguro**: solo dice que no hubo respuesta a tiempo.
- **Suponer que «no hubo respuesta» equivale a «no se ejecutó»**.

## Límites y cuándo no aplica

`SE-389` indica que no midió ninguna red ni servicio real: las probabilidades, la distribución lognormal y los parámetros de reintentos son construcciones del autor. La cifra de «más de la mitad» depende del supuesto de pérdidas simétricas. En operaciones puramente de lectura, o idempotentes por naturaleza, la ambigüedad no causa daño y reintentar es seguro.
