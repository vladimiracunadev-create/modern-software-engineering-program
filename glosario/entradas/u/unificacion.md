# Unificación

[↑ Glosario](../../README.md) · [← Unidad menor](./unidad-menor.md) · [Unión etiquetada →](./union-etiquetada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

La **unificación** es el mecanismo central de la programación lógica: dados dos términos, **busca una sustitución de variables que los haga idénticos** ([SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md)). Si existe, los términos *unifican* y la sustitución resultante liga las variables; si no, fallan. No es una asignación ni una comparación: es una **resolución simultánea de ecuaciones entre estructuras**, y por eso una misma relación puede usarse como entrada y como salida. El término pertenece a la lógica y la demostración automática; el programa lo estudia en su forma de Prolog.

## Por qué importa

Quien viene de la programación imperativa interpreta `X = f(Y)` como «guardar en X el valor de `f(Y)`». En programación lógica no se guarda nada: se **afirma una igualdad** que el sistema resuelve. Entender la unificación explica por qué una misma regla sirve para verificar, calcular y generar; por qué un fallo hace retroceder la búsqueda; y por qué ciertos resultados sorprendentes (como estructuras infinitas) son posibles. La decisión que cambia es cómo se razona sobre un programa lógico: en términos de sustituciones y retroceso, no de variables que cambian de valor.

## Cómo funciona

El algoritmo compara dos términos y construye una sustitución:

- Una **variable** unifica con cualquier término, quedando ligada a él.
- Dos **constantes** unifican si son iguales.
- Dos **estructuras** (`f(a, b)` y `g(c)`) unifican si tienen el mismo **funtor** y la misma **aridad** y sus argumentos unifican uno a uno, acumulando la sustitución.
- Si algo no encaja, **falla**.

Una variable lógica no se reasigna: queda **vinculada dentro de una rama de búsqueda**. Cuando la búsqueda retrocede (por un fallo), esos vínculos se deshacen y se prueba otra alternativa. Existe una sutileza, la **comprobación de ocurrencia** (*occurs check*): al unificar `X` con `f(X)`, la sustitución correcta no existe, porque `X` sería un término infinito (`f(f(f(...)))`). Muchos sistemas la omiten por defecto por costo; [SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md) observa que el resolvedor mínimo del curso la omite, y que SWI-Prolog ofrece `unify_with_occurs_check/2` para exigirla. Qué términos se admiten depende entonces del sistema, y no conviene extrapolar desde el pseudocódigo.

## Ejemplo

[SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md) ejecutó tres casos:

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

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Estructura](../e/estructura.md), [Sustitución](../s/sustitucion.md), [Negación y mundo cerrado](../n/negacion-y-mundo-cerrado.md), [Resolución y backtracking](../r/resolucion-y-backtracking.md), [Restricciones y explicación](../r/restricciones-y-explicacion.md), [Términos, hechos y consultas](../t/terminos-hechos-y-consultas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-078 — Programación lógica y resolución](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), [SE-076](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), [SE-079](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), [SE-080](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md), [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SWI-Prolog Reference Manual](https://www.swi-prolog.org/pldoc/man?section=intro) — Hechos, reglas, unificación, búsqueda y límites operacionales; autoridad: SWI-Prolog project.
- [Python Language Reference](https://docs.python.org/3/reference/) — Semántica de sentencias, funciones, clases, generadores y corrutinas; autoridad: Python Software Foundation.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — Ownership, enums, traits, errores y concurrencia sin carreras de datos; autoridad: Rust project.
- [ReactiveX Observable Contract](https://reactivex.io/documentation/contract.html) — Notificaciones, terminación, errores y control de flujo observable; autoridad: ReactiveX project.
- [Erlang System Documentation: Processes](https://www.erlang.org/doc/system/ref_man_processes.html) — Procesos, buzones, envío de mensajes, enlaces y monitores; autoridad: Erlang/OTP project.

---

[↑ Glosario](../../README.md) · [← Unidad menor](./unidad-menor.md) · [Unión etiquetada →](./union-etiquetada.md)
