# Reconstrucción independiente

## Definición

La **reconstrucción independiente** es la construcción de un artefacto desde la fuente por una parte distinta del constructor original, para comparar el resultado con el artefacto publicado. `SE-479` la usa en la cadena de suministro: se toma la fuente revisada, se construye con las entradas declaradas en un entorno que no es el del constructor y se compara la huella con la del release.

## Por qué importa

Un release firmado prueba *quién* lo publicó, no que corresponda al código que se revisó. Si el entorno de construcción se compromete, el binario puede incluir algo que la fuente no tiene. La reconstrucción independiente cambia la confianza: de «creo en el constructor» a «alguien más puede obtener el mismo artefacto desde la fuente que revisé». Detecta, por ejemplo, un release manipulado después de la revisión.

## Cómo funciona

`SE-479` compara tres reconstrucciones contra dos releases (uno legítimo y uno malicioso):

1. Reconstruir desde la **fuente revisada** y comparar con el release legítimo: coincide.
2. Reconstruir desde la fuente revisada y comparar con el release malicioso: **no coincide**; es la detección.
3. Reconstruir desde la **fuente maliciosa** y comparar con el release malicioso: coincide.

La tercera comparación es la advertencia de la clase: **reproducible no equivale a legítimo**. Que un build se reproduzca solo prueba que es determinista; si la fuente de partida es la comprometida, el resultado coincide igual. De ahí la condición de independencia: la fuente de comparación tiene que ser la *revisada*, obtenida por un camino distinto del de quien publicó el release.

Esto presupone un **build reproducible** (`SE-469`): mismas entradas y mismo proceso dan la misma huella. La comparación se hace sobre la huella del artefacto.

## Ejemplo

Se publica una versión 2.4.0 de una biblioteca. Una segunda parte clona la etiqueta revisada, usa las dependencias fijadas por su bloqueo, construye en su entorno y calcula la huella. Si coincide con la del release, la fuente revisada es la que se empaquetó. Si no coincide, hay una diferencia que explicar: o hay una entrada no declarada (la fecha de compilación, una ruta absoluta) o hay manipulación. La cifra de coincidencias de la clase viene de un modelo sintético con releases legítimo y malicioso, no de un compilador real.

## Errores y confusiones comunes

- **El verificador acepta un release de otro constructor.** Causa (`SE-479`): valores esperados tomados del documento que se verifica. Corrección: configuración independiente, fijada de antemano.
- **Un release antiguo pasa como el último.** No se comprobó la secuencia; hay que recordar la mayor secuencia vista y rechazar las menores.
- **Confiar en una reconstrucción desde la fuente equivocada.** Coincide, pero no valida nada.
- **No declarar todas las entradas.** Con entradas ocultas la coincidencia falla incluso en el caso legítimo.

## Límites y cuándo no aplica

Exige tres cosas (`SE-479`): que exista una «fuente revisada» independiente de la usada para el release, que el build sea reproducible y que las entradas estén declaradas. Un compilador real con entradas no declaradas haría que la coincidencia no ocurriera ni siquiera en el caso legítimo. Aun cuando funcione, solo prueba que el artefacto corresponde a la fuente; no que la fuente sea segura ni que las dependencias lo sean. Y exige a alguien con la capacidad de reconstruir: para proyectos sin esa tercera parte, la garantía no existe.
