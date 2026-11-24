# Subtipado conductual

[↑ Glosario](../../README.md) · [← Subproblemas superpuestos](./subproblemas-superpuestos.md) · [Sucesos concurrentes →](./sucesos-concurrentes.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

El **subtipado conductual** es la relación por la cual una subclase puede sustituir a su base sin romper a los clientes: acepta al menos lo mismo y garantiza al menos lo mismo ([SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md)). Es la formalización de Liskov y Wing del principio de sustitución. Se llama conductual porque se refiere al comportamiento prometido, no a la forma de las firmas.

## Por qué importa

La herencia sintáctica no basta. Una subclase puede compilar, heredar todos los métodos y aun así romper llamadas válidas de los clientes de la base. El subtipado conductual da el criterio para decidir si un cambio de contrato es seguro, y por eso también sirve para versionar servicios: es el mismo principio que la compatibilidad hacia atrás.

## Cómo funciona

[SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) enuncia tres condiciones:

- **Precondición igual o más débil**: la subclase acepta al menos lo mismo que la base.
- **Postcondición igual o más fuerte**: garantiza al menos lo mismo.
- **Invariante preservado**: no rompe lo que la clase base mantiene siempre cierto.

La razón es la perspectiva del cliente. Quien escribió código contra la base confía en dos cosas: que lo que le pasa se acepta (si cumple la precondición) y que lo que recibe cumple la postcondición. Una subclase que **exige más** (precondición más fuerte) rechaza llamadas que el cliente tenía derecho a hacer; una que **promete menos** (postcondición más débil) entrega algo con lo que el cliente no contaba.

La clase da el contraejemplo: una subclase `CalificacionEstricta` que exige `1 ≤ horas ≤ 48` donde la base acepta `0 ≤ horas ≤ 72`. Compila, hereda y rompe llamadas válidas (con 0 horas o con 60). El criterio vale también para versionar servicios: una nueva versión es sustituible por la anterior si acepta más (o igual) y garantiza más (o igual).

Sobre el invariante, [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) señala un fallo frecuente: el invariante falla lejos de donde se corrompió el estado porque se comprobó al final o cada muchas operaciones; la corrección es comprobarlo en la frontera de cada operación pública, al menos en pruebas.

## Ejemplo

Base: `calificar(horas)` acepta `0 ≤ horas ≤ 72` y garantiza que la nota queda en `[0, 100]`. Subclase correcta: acepta `0 ≤ horas ≤ 96` (más débil) y garantiza nota en `[0, 100]` con además un mensaje (más fuerte). Subclase incorrecta: acepta `1 ≤ horas ≤ 48` (más fuerte) y puede devolver nota `None` en un caso (postcondición más débil). El código de un cliente que llama con 0 horas fallará con la segunda. (Ejemplo derivado del de [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md).)

## Errores y confusiones comunes

- **Una subclase rompe a los clientes pese a compilar**: reforzó una precondición o debilitó una postcondición.
- **Creer que si el compilador lo acepta es sustituible.**
- **Invariantes comprobados tarde.**
- **Confundir subtipado con herencia de implementación**: se puede heredar código sin ser subtipo.

## Límites y cuándo no aplica

Solo es verificable si los contratos están escritos; con contratos implícitos, el criterio es una guía de revisión. No resuelve el acoplamiento por herencia ni sustituye otras razones para preferir composición. Para propiedades no funcionales (rendimiento, tiempo) la sustituibilidad también puede romperse sin violar pre y postcondiciones formales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Relación](../r/relacion.md), [Contrato ejecutable](../c/contrato-ejecutable.md), [Invariante](../i/invariante.md), [Invariante de clase](../i/invariante-de-clase.md), [Postcondición](../p/postcondicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Liskov y Wing, «A behavioral notion of subtyping» (TOPLAS, 1994)](https://doi.org/10.1145/197320.197383) — subtipado conductual y reglas de sustitución; autoridad: ACM TOPLAS.
- [Meyer, «Applying design by contract» (IEEE Computer, 1992)](https://doi.org/10.1109/2.161279) — formulación del diseño por contrato; autoridad: IEEE Computer.
- [Hoare, «An axiomatic basis for computer programming» (CACM, 1969)](https://doi.org/10.1145/363235.363259) — tripleta precondición–instrucción–postcondición; autoridad: Communications of the ACM.
- [Eiffel: Design by Contract](https://www.eiffel.com/values/design-by-contract/) — descripción del mecanismo en el lenguaje que lo introdujo; autoridad: Eiffel Software.
- [Python: sentencia `assert`](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) — semántica de `assert` y su desactivación; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Subproblemas superpuestos](./subproblemas-superpuestos.md) · [Sucesos concurrentes →](./sucesos-concurrentes.md)
