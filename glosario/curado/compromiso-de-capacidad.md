# Compromiso de capacidad

## Definición

Un **compromiso de capacidad** es un acuerdo de pagar por una cantidad de capacidad durante un periodo, se use o no (SE-140). SE-404 lo formula como el acuerdo de pagar una cantidad de capacidad por un plazo a cambio de un precio unitario menor. En la nube corresponde a las instancias o planes reservados y a los compromisos de gasto.

## Por qué importa

Cambia el costo de la parte estable de la demanda y expone a un riesgo si la demanda cae. Comprometer ahorra si la demanda se mantiene por encima de lo comprometido; cuesta si baja, porque se paga igual. Es una decisión de costos con incertidumbre, no una oferta que convenga aceptar por defecto.

## Cómo funciona

El proveedor cobra menos por unidad a cambio de certeza: sabe que cierta cantidad se pagará. SE-140 lo describe como **una opción vendida al proveedor**: el cliente cede flexibilidad y obtiene un precio menor. Ahorra si la demanda se mantiene por encima de lo comprometido y cuesta si cae.

El nivel que conviene comprometer está **cerca de la demanda esperada**; SE-404 afina: cerca de la **mediana** de la demanda, no del promedio ni del máximo, y precisa la lógica de asimetría: comprometer de más cuesta más que no comprometer, porque lo comprometido se paga siempre, mientras que lo que queda bajo demanda solo se paga si se usa. Se compromete la parte de la demanda que casi siempre está presente (la base) y el resto se deja bajo demanda. FinOps incluye esta optimización de tarifas como una de sus prácticas.

El riesgo se mide, no se intuye: con el **percentil alto del costo** y con **escenarios de caída persistente** de la demanda. Si el compromiso es por tres años y la demanda cae a la mitad en el segundo, el ahorro unitario puede ser menor que el costo de la capacidad ociosa.

Se complementa con el costo por resultado y la atribución del gasto: un compromiso compartido entre equipos exige una regla de reparto, y cada centro no debe pagar más que su costo solo.

## Ejemplo

Con cifras ilustrativas: la demanda diaria de cómputo fluctúa entre 40 y 100 unidades con mediana 60. El proveedor ofrece 30 % de descuento por comprometer. Comprometer 60 (la mediana) cubre la base casi siempre y el resto se paga bajo demanda; comprometer 100 (el máximo) paga 40 unidades ociosas la mayor parte del tiempo y puede costar más que no comprometer. Si la demanda cae a 45 de forma persistente, incluso el compromiso de 60 deja capacidad ociosa. (Valores de ejemplo para mostrar la lógica de SE-140 y SE-404.)

## Errores y confusiones comunes

- **Comprometer el máximo** o el promedio en vez de la base estable.
- **No simular una caída persistente**: el ahorro se convierte en pérdida.
- **Olvidar que se paga se use o no.**
- **Confundirlo con un descuento por volumen**: aquí hay plazo y obligación de pago.

## Límites y cuándo no aplica

Con demanda muy variable o incierta, no hay base estable que comprometer. Si la arquitectura puede cambiar de proveedor o de tipo de recurso, el compromiso limita esa libertad. Para proyectos de vida corta el plazo del compromiso puede superar la vida del proyecto.
