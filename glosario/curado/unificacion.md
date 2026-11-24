# Unificación

## Definición

La **unificación** es el mecanismo central de la programación lógica: dados dos términos, **busca una sustitución de variables que los haga idénticos** (`SE-078`). Si existe, los términos *unifican* y la sustitución resultante liga las variables; si no, fallan. No es una asignación ni una comparación: es una **resolución simultánea de ecuaciones entre estructuras**, y por eso una misma relación puede usarse como entrada y como salida. El término pertenece a la lógica y la demostración automática; el programa lo estudia en su forma de Prolog.

## Por qué importa

Quien viene de la programación imperativa interpreta `X = f(Y)` como «guardar en X el valor de `f(Y)`». En programación lógica no se guarda nada: se **afirma una igualdad** que el sistema resuelve. Entender la unificación explica por qué una misma regla sirve para verificar, calcular y generar; por qué un fallo hace retroceder la búsqueda; y por qué ciertos resultados sorprendentes (como estructuras infinitas) son posibles. La decisión que cambia es cómo se razona sobre un programa lógico: en términos de sustituciones y retroceso, no de variables que cambian de valor.

## Cómo funciona

El algoritmo compara dos términos y construye una sustitución:

- Una **variable** unifica con cualquier término, quedando ligada a él.
- Dos **constantes** unifican si son iguales.
- Dos **estructuras** (`f(a, b)` y `g(c)`) unifican si tienen el mismo **funtor** y la misma **aridad** y sus argumentos unifican uno a uno, acumulando la sustitución.
- Si algo no encaja, **falla**.

Una variable lógica no se reasigna: queda **vinculada dentro de una rama de búsqueda**. Cuando la búsqueda retrocede (por un fallo), esos vínculos se deshacen y se prueba otra alternativa. Existe una sutileza, la **comprobación de ocurrencia** (*occurs check*): al unificar `X` con `f(X)`, la sustitución correcta no existe, porque `X` sería un término infinito (`f(f(f(...)))`). Muchos sistemas la omiten por defecto por costo; `SE-078` observa que el resolvedor mínimo del curso la omite, y que SWI-Prolog ofrece `unify_with_occurs_check/2` para exigirla. Qué términos se admiten depende entonces del sistema, y no conviene extrapolar desde el pseudocódigo.

## Ejemplo

`SE-078` ejecutó tres casos:

```text
f(A, 2)  con  f(1, B)   -> éxito: A = 1, B = 2  (la misma relación sirve de entrada y de salida)
f(1)     con  f(2)      -> fallo: lo que hace retroceder la búsqueda
X        con  f(X)      -> aceptado sin comprobación de ocurrencia: estructura infinita
```

El primer caso muestra que la unificación liga variables **en ambos sentidos**: `A` recibe lo que está en el otro término y `B`, también. El segundo muestra que un fallo no es un error, sino una señal para explorar otra alternativa. El tercero, el peligro de omitir la comprobación: en un sistema con la comprobación, `X = f(X)` falla; sin ella, crea un ciclo. La clase implementó además un resolvedor mínimo en Python (unificación y retroceso, sin optimizaciones) para contar cuántas comparaciones de unificación hacía, y observar su costo.

## Errores y confusiones comunes

- **Pensar que `=` asigna.** Unifica; no hay mutación.
- **Ignorar la comprobación de ocurrencia.** Una variable puede quedar ligada a una estructura infinita.
- **Confundir fallo con error.** El fallo es parte del mecanismo de búsqueda.
- **Extrapolar desde un resolvedor de juguete.** Los sistemas reales difieren en qué admiten.

## Límites y cuándo no aplica

La unificación decide cuándo dos estructuras encajan; no resuelve por sí sola la eficiencia de la búsqueda (el orden de las reglas y el retroceso determinan el costo). Aplica a términos de primer orden; en lenguajes con tipos o en otros paradigmas se usan mecanismos distintos (la inferencia de tipos usa una forma de unificación, pero con otro propósito). Y el uso de la comprobación de ocurrencia es una decisión de cada sistema, con costo que debe valorarse.
