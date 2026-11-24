# Perfil de operaciones

## Definición

Un **perfil de operaciones** es, en el taller de `SE-095`, la descripción de **qué operaciones hará un programa sobre una estructura de datos y con qué frecuencia**, expresada en **porcentajes y ráfagas** de insertar, extraer, buscar, recorrer y borrar, y completada con el **tamaño, la distribución de los datos y el SLO**. No confundir con el *perfil* de un perfilador (que mide una ejecución real); aquí es la **especificación de la carga** que sirve para elegir y comparar estructuras antes de medir.

## Por qué importa

«La mejor estructura» no existe sin una carga. Una lista es excelente para añadir y recorrer, mala para buscar; un `set` es excelente para buscar y malo para mantener el orden. Elegir sin declarar la carga es elegir por costumbre. La decisión que cambia es qué se escribe antes de medir: el perfil de operaciones, para que cualquier otro equipo pueda leer la recomendación y comprobar si su carga se parece. `SE-095` documenta el síntoma: la recomendación no convence a otro equipo porque no declara la carga ni el tamaño.

## Cómo funciona

El perfil incluye:

- **Mezcla de operaciones:** por ejemplo, 70 % buscar, 20 % insertar, 10 % borrar; y si las operaciones llegan en **ráfagas** (muchas inserciones seguidas, luego muchas consultas) o intercaladas.
- **Tamaño:** cuántos elementos y cuánto crecen. Lo que es barato con 100 elementos puede ser inviable con 10 millones.
- **Distribución de los datos:** claves ordenadas, repetidas, aleatorias; determina si aparecen peores casos.
- **SLO:** el objetivo de latencia o de capacidad que da sentido a «suficientemente rápido».

Hay una precaución explícita: **un porcentaje bajo puede dominar el impacto** si la operación es muy costosa o bloquea el flujo. Un 1 % de borrados que cuestan `O(n)` cada uno puede pesar más que el 99 % de búsquedas baratas. Por eso el perfil no solo cuenta frecuencias: pondera por costo y por efecto en el flujo.

## Ejemplo

El perfil del taller de `SE-095` para la biblioteca de estructuras y algoritmos, al elegir cómo almacenar casos con prioridad (ilustración, números inventados):

```text
operaciones:  insertar 40 %, extraer el de mayor prioridad 40 %, buscar por id 15 %,
              borrar por id 5 %.  Ráfagas: inserciones por lotes de 500 cada hora.
tamaño:       10^5 casos en régimen, 10^6 en picos.
distribución: prioridades con muchos empates; ids crecientes.
SLO:          extraer en p99 < 5 ms.
```

Con este perfil, la lista ordenada penaliza las inserciones, el montículo favorece insertar y extraer, y los ids crecientes hacen preocupante un árbol de búsqueda sin balance. La recomendación se escribe junto con la medición que la invalidaría.

## Errores y confusiones comunes

- **Elegir sin perfil.** La recomendación no es reproducible por otros.
- **Ignorar el tamaño.** Un resultado a pequeña escala no se extrapola.
- **Contar solo frecuencias.** Una operación rara pero costosa o bloqueante puede dominar.
- **Datos de prueba que no se parecen a los reales.** Ocultan peores casos.

## Límites y cuándo no aplica

El taller cubre cargas sintéticas y una plataforma (`SE-095`): el perfil es una declaración de la carga **esperada**, y si el uso real cambia, la elección debe revisarse. Para colecciones pequeñas y poco usadas, declarar un perfil formal es excesivo. El perfil tampoco sustituye medir, ya que dos estructuras con igual cota asintótica pueden diferir mucho en la práctica.
