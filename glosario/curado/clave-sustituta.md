# Clave sustituta

## Definición

Una **clave sustituta** es un identificador generado por el modelo, distinto de la clave de negocio, que identifica una fila de forma estable y no tiene significado de negocio (`SE-349`, `SE-363`). Puede ser un entero secuencial, un identificador aleatorio o un hash. Se contrapone a la clave **natural**, que sale de los datos del dominio.

## Por qué importa

Toda fila necesita algo que la identifique y no cambie. El correo de un estudiante parece una buena clave hasta que alguien cambia de dirección: entonces hay que actualizar cada fila que lo referencia. La decisión que cambia es qué se usa para relacionar tablas: una identidad estable e interna, en vez de un dato del mundo que puede cambiar, repetirse o reutilizarse.

## Cómo funciona

`SE-349` explica por qué funciona: la clave sustituta no significa nada, y por eso no tiene motivo para cambiar. El dato natural puede modificarse sin tocar las referencias. El costo es doble: oculta duplicados si no se añade además una **restricción de unicidad** sobre el dato natural, y su elección entre entero y UUID, que parece estética, tiene costos medibles de espacio, de orden de inserción y de exposición (un entero secuencial revela cuántas entregas hay).

`SE-363` lleva la idea a la ingeniería de datos. La clave de negocio del sistema operacional puede cambiar, repetirse entre sistemas o reutilizarse. Una clave sustituta aísla las tablas analíticas de esos cambios y permite **varias versiones de la misma entidad**, una por fila de la dimensión con historia. Ese aislamiento tiene un costo operativo: cada carga debe resolver de clave de negocio a clave sustituta, y los hechos sin dimensión (huérfanos) necesitan una fila especial «desconocido» para no desaparecer en una unión interna.

## Ejemplo

Una tabla de estudiantes usa `id` entero como clave sustituta y mantiene el correo con una restricción de unicidad. Si el estudiante cambia de correo, se actualiza una sola fila. En un almacén analítico, la dimensión de estudiantes guarda una fila por versión del estudiante, cada una con su clave sustituta; un hecho cuyo estudiante no se encuentra apunta a la fila «desconocido» en lugar de perderse.

## Errores y confusiones comunes

- **Quitar la clave natural**: sin unicidad sobre el dato natural, la clave sustituta permite filas duplicadas que parecen distintas.
- **Elegir entre entero y UUID por estética**: tiene costos de espacio, orden de inserción y exposición.
- **Exponer el entero secuencial hacia fuera**: revela cuántos registros existen.
- **Perder hechos huérfanos**: sin fila «desconocido», una unión interna los descarta.

## Límites y cuándo no aplica

No siempre hace falta: cuando existe una clave natural verdaderamente estable y única, añadir una sustituta suma una columna y una resolución en cada carga sin un beneficio claro. En el modelado con historia, la clave sustituta es necesaria, pero no resuelve por sí sola la semántica de los cambios; esa decisión (qué versión corresponde a un hecho) es aparte. Y aporta estabilidad interna, no identidad ante terceros: otros sistemas seguirán usando la clave de negocio.
