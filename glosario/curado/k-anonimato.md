# K-anonimato

## Definición

Un conjunto de datos cumple **k-anonimato** cuando cada combinación de **cuasi-identificadores** (atributos que no identifican por sí solos, como ciudad, plan o año de nacimiento, pero que juntos pueden señalar a una persona) aparece en al menos *k* registros. Dicho de otro modo, ninguna persona es distinguible de al menos otras *k − 1* por esos atributos. El programa usa el sentido de Sweeney (2002), tal como lo presentan `SE-369` y `SE-463`; `SE-137`, `SE-226` y `SE-488` lo aplican a telemetría y a entornos de vista previa con datos reducidos.

## Por qué importa

Quitar el nombre y el identificador de una tabla no la anonimiza: `SE-369` muestra que un agregado liberado con atributos que, juntos, identifican puede señalar a una persona aunque cada atributo sea inocuo. El k-anonimato convierte esa intuición en una medida que se puede calcular antes de publicar, compartir telemetría o poblar un entorno de pruebas, y obliga a decidir cuánta utilidad se sacrifica a cambio de privacidad.

## Cómo funciona

El mecanismo es contar y generalizar. Se eligen los cuasi-identificadores, se agrupan los registros por cada combinación y se mide el tamaño del grupo más pequeño: ese es el *k* real del conjunto. Si es menor que el objetivo, se actúa sobre los atributos (`SE-463`):

1. **Generalizar:** reducir la precisión (año a década o a tramos de cinco años, comuna a región) o quitar atributos.
2. **Suprimir:** eliminar los registros raros que quedan en grupos pequeños.
3. Volver a medir hasta que el grupo más pequeño alcance *k*.

Cada paso reduce la unicidad y también la utilidad. Con *k* de 5, `SE-369` agrupa 5 000 personas por ciudad (6 grupos, ninguno pequeño), por ciudad y plan (18 grupos, ninguno pequeño) y por ciudad, plan y año de nacimiento (1 004 grupos, de los cuales 441 tienen menos de 5 personas y dejan a 1 310 personas expuestas); al generalizar el año a década, quedan 108 grupos y ninguno pequeño. La causa es combinatoria: cada atributo que se añade multiplica los grupos y deja menos personas en cada uno.

## Ejemplo

En `SE-463`, el conjunto del experimento se generaliza con tramos de cinco años, macrozona y sin género: queda en 12 grupos con un *k* mínimo de 63. Es una protección fuerte, y el precio es que el conjunto sirve para contar por macrozona y poco más. Los datos son sintéticos de la clase, y el ejemplo ilustra el compromiso, no una recomendación de qué *k* usar.

## Errores y confusiones comunes

- **Creer que sin nombre ya es anónimo.** El problema son los atributos en conjunto (cuasi-identificadores), no el identificador directo.
- **Confundir k-anonimato con seudonimización.** Seudonimizar sustituye el identificador por otro reversible con una clave; el k-anonimato actúa sobre la combinación de atributos. Son técnicas distintas.
- **Fijar el *k* sin decidir los cuasi-identificadores.** El valor de *k* solo tiene sentido respecto de los atributos elegidos: un atributo olvidado deshace la garantía.
- **Medir una sola vez.** Cada versión nueva de los datos puede cambiar los grupos; hay que volver a medir al publicar.

## Límites y cuándo no aplica

`SE-369` lo llama condición necesaria y no suficiente. `SE-463` precisa tres límites: no protege cuando todos los miembros de un grupo comparten el valor del atributo sensible (si las 63 personas de un grupo abandonaron el servicio, saber el grupo revela el abandono); no protege frente a quien conoce un dato más; y no resiste que se publiquen varias versiones del mismo conjunto, porque se pueden cruzar. Tampoco es una garantía legal: la minimización y los plazos de retención dependen de la norma aplicable, que las clases citan de fuentes oficiales.
