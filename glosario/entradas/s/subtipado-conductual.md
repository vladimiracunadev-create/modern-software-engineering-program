# Subtipado conductual

[↑ Glosario](../../README.md) · [← Subproblemas superpuestos](./subproblemas-superpuestos.md) · [Sucesos concurrentes →](./sucesos-concurrentes.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Relación por la que una subclase puede sustituir a su base aceptando al menos lo mismo y garantizando al menos lo mismo.

Definición de trabajo de [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md).

## Por qué importa

En [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md), el tema «Subtipado conductual» importa porque un cambio de contrato es seguro solo si acepta más y garantiza más.

## Cómo funciona

Según [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md), en la sección «Subtipado conductual»:

Liskov y Wing formalizan cuándo una subclase puede sustituir a su base sin romper a los clientes: **precondición igual o más débil** (acepta al menos lo mismo), **postcondición igual o más fuerte** (garantiza al menos lo mismo) e **invariante preservado**. La herencia sintáctica no basta: una subclase `CalificacionEstricta` que exige `1 ≤ horas ≤ 48` donde la base acepta `0 ≤ horas ≤ 72` compila, hereda y rompe llamadas válidas. El criterio sirve también para versionar servicios: es el mismo principio de «aceptar más, devolver más» que reaparece en `SE-164`.

## Ejemplo

Caso medido en la sección «Subtipado conductual» de [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md):

Liskov y Wing formalizan cuándo una subclase puede sustituir a su base sin romper a los clientes: **precondición igual o más débil** (acepta al menos lo mismo), **postcondición igual o más fuerte** (garantiza al menos lo mismo) e **invariante preservado**. La herencia sintáctica no basta: una subclase `CalificacionEstricta` que exige `1 ≤ horas ≤ 48` donde la base acepta `0 ≤ horas ≤ 72` compila, hereda y rompe llamadas válidas. El criterio sirve también para versionar servicios: es el mismo principio de «aceptar más, devolver más» que reaparece en `SE-164`.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md)) son:

- **El invariante falla lejos de donde se corrompió el estado** — causa: se comprueba al final o cada muchas operaciones. Corrección: comprobar en la frontera de cada operación pública, al menos en pruebas.
- **Una subclase rompe a los clientes de la base pese a compilar** — causa: reforzó una precondición o debilitó una postcondición. Corrección: aplicar la regla: aceptar al menos lo mismo, garantizar al menos lo mismo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos salvo los tiempos. No se usó ninguna biblioteca de contratos, los nueve defectos y la probabilidad de reparación son supuestos del autor y no se midió a ningún equipo. La siguiente clase pregunta qué estructura y qué comportamiento tienen las entidades cuyos contratos se acaban de escribir.

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
