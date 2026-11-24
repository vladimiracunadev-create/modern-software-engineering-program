# Contradicción

## Definición

En ingeniería de requisitos, una **contradicción** es una relación entre requisitos que no pueden cumplirse todos a la vez, directamente o a través de otros. Es el sentido de `SE-154`, que la sitúa junto a la ambigüedad y la incompletitud como los tres defectos clásicos de una especificación. `SE-560` usa la misma idea para instrucciones dadas a un modelo: las reglas contradictorias provocan elecciones arbitrarias entre ellas.

## Por qué importa

Cambia cuándo se descubre que algo no se puede construir. Requisitos incompatibles hacen imposible cumplirlos todos, y quien implementa acabará eligiendo uno en silencio. Detectarlo al especificar cuesta una pregunta; detectarlo con el sistema construido cuesta un rediseño o una excepción permanente.

## Cómo funciona

`SE-154` distingue dos formas. La **contradicción directa** («guardar» frente a «no guardar») es rara y se ve a simple vista. La frecuente es la **indirecta**: requiere varias premisas para aparecer, y un conjunto puede ser inconsistente sin que ningún par lo sea. Por eso la revisión por pares, que compara requisitos de dos en dos, no encuentra las contradicciones más costosas.

La detección sistemática traduce los requisitos a una forma donde se pueda decidir si existe algún estado que los cumpla todos. Si no existe, se buscan **subconjuntos mínimos incompatibles**: los requisitos más pequeños que, juntos, no pueden satisfacerse. Eso señala qué conjunto de personas debe decidir. El hallazgo se registra como defecto con tipo, técnica y responsable, no como una observación suelta.

## Ejemplo

En `SE-154` el inventario de defectos muestra tres casos para comparar: una ambigüedad que desaparece al añadir un ejemplo, una contradicción que solo aparece tras un cambio hecho en `SE-153`, y una celda abierta que resultó imposible por una regla de la interfaz. El inventario es útil cuando cada defecto tiene tipo, técnica y responsable; es peligroso cuando se reduce a observaciones sin dueño.

## Errores y confusiones comunes

- **Revisar de dos en dos y declarar el conjunto consistente.** Hay contradicciones de orden tres o más; buscar subconjuntos mínimos incompatibles sobre las condiciones (`SE-154`).
- **Confundir contradicción con ambigüedad.** Una contradicción persiste aunque cada requisito sea claro; una ambigüedad desaparece al precisarlo.
- **Resolverla eligiendo al azar.** Debe decidir quien tiene autoridad sobre ambos requisitos.
- **Pensar que solo existe entre requisitos funcionales.** También ocurre entre atributos de calidad.

## Límites y cuándo no aplica

La detección formal exige expresar los requisitos con precisión suficiente; con texto libre solo se encuentran contradicciones evidentes. Un conjunto consistente no es un conjunto correcto: puede ser consistente y no resolver el problema. En requisitos de calidad la incompatibilidad suele ser un compromiso a negociar más que una contradicción lógica. Y los ejemplos de `SE-154` usan identificadores y requisitos ilustrativos.
