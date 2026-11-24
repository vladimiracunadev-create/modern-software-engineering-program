# Contrato de datos

## Definición

Un **contrato de datos** es un acuerdo versionado entre un productor y sus consumidores sobre el esquema, la semántica, la calidad y el servicio de un conjunto de datos (`SE-366`). `SE-343` lo usa en un sentido algo más acotado: el esquema y las garantías de calidad y frescura que el productor ofrece. Es la contraparte, para los datos, del contrato de una interfaz.

## Por qué importa

Los consumidores de datos (informes, modelos, otros equipos) dependen de campos que el productor puede cambiar sin saberlo. Sin un acuerdo explícito, un cambio incompatible rompe aguas abajo, y el productor se entera después. La decisión que cambia es quién es responsable de qué: el productor se compromete a lo que publica y a cómo lo cambia; el consumidor sabe en qué puede confiar.

## Cómo funciona

El contrato tiene cuatro partes, siguiendo la definición de `SE-366`:

- **Esquema**: campos, tipos y obligatoriedad.
- **Semántica**: qué significa cada campo. Un cambio de significado sin cambio de tipo es el más difícil de detectar (cambio semántico).
- **Calidad**: reglas que los datos cumplen, como unicidad o rangos.
- **Servicio**: garantías como la frescura, es decir, cuánto retraso máximo tiene el dato.

Está **versionado**: los cambios se rigen por reglas de promoción y de compatibilidad (hacia atrás y hacia adelante). La clase `SE-366` lo trabaja con un verificador y un registro de esquemas, que comparan una versión propuesta con la vigente y rechazan cambios incompatibles. La causa de que funcione es que convierte una convención informal en algo comprobable de forma automática antes de publicar.

Un detalle de alcance: `SE-366` usa el término dentro de otro tema, sin una sección propia; el mecanismo completo (registro, compatibilidad) es el de esa clase. El paso siguiente, `SE-367`, construye el linaje y el catálogo que dicen quién consume cada campo, pieza necesaria para saber a quién afecta un cambio.

## Ejemplo

El productor publica `entregas` v1 con `nota` entero y frescura máxima de una hora. Quiere cambiar `nota` a decimal. El verificador compara con la versión vigente y marca el cambio como incompatible para consumidores que esperan entero; el productor debe publicar v2 y dar un plazo de convivencia. Escenario construido en la línea de `SE-366`.

## Errores y confusiones comunes

- **Reducirlo al esquema**: sin semántica ni calidad, un cambio de significado pasa inadvertido.
- **No versionarlo**: no hay forma de cambiar sin romper.
- **Confundirlo con la documentación**: un contrato se comprueba automáticamente; una documentación se lee.
- **Creer que lo cumple quien consume**: obliga al productor.

## Límites y cuándo no aplica

`SE-366` declara que sus esquemas, reglas de promoción y registros son construcciones del autor y que el verificador es una simplificación: no cubre tipos anidados, enumeraciones ni uniones. No se ejecutó un registro de esquemas real ni se midió el costo de un cambio incompatible en una organización. Para datos con un único productor y consumidor dentro del mismo equipo, el costo formal puede ser mayor que el beneficio.
