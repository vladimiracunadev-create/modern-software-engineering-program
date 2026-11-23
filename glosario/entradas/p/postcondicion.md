# Postcondición

[↑ Glosario](../../README.md) · [← Poscondición](./poscondicion.md) · [Postmortem →](./postmortem.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Condición que la operación garantiza al terminar si se cumplió la precondición.

Definición de trabajo de [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md).

## Por qué importa

En [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md), el tema «Postcondiciones» importa porque fijan lo que el proveedor garantiza al terminar; sin ellas el cliente depende de lo observado.

## Cómo funciona

Según [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md), en la sección «Postcondiciones»:

La postcondición describe lo que el proveedor garantiza al volver: tras `calificar`, la nota está en el rango y el estado es «calificada». Meyer la presenta como el beneficio del cliente a cambio de cumplir la precondición. Sirve a la persona que lee (describe lo que puede suponerse) y al comprobador (detecta violaciones sin conocer el cálculo). Su límite es que solo afirma lo escrito: una operación que duplica una prórroga sin pasar del tope cumple todas las postcondiciones que nadie escribió.

## Ejemplo

Ejemplo de [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) (sección «Ejemplo mínimo»):

El fragmento declara una precondición y una postcondición para la prórroga. Antes de ejecutarlo, predice cuál de las dos llamadas falla.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una subclase rompe a los clientes de la base pese a compilar** — causa: reforzó una precondición o debilitó una postcondición. Corrección: aplicar la regla: aceptar al menos lo mismo, garantizar al menos lo mismo. ([SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Su límite es que solo afirma lo escrito: una operación que duplica una prórroga sin pasar del tope cumple todas las postcondiciones que nadie escribió. ([SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Operación](../o/operacion.md), [Precondición](./precondicion.md), [Contrato ejecutable](../c/contrato-ejecutable.md), [Invariante](../i/invariante.md), [Invariante de clase](../i/invariante-de-clase.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Postcondiciones».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Hoare, «An axiomatic basis for computer programming» (CACM, 1969)](https://doi.org/10.1145/363235.363259) — tripleta precondición–instrucción–postcondición; autoridad: Communications of the ACM.
- [Meyer, «Applying design by contract» (IEEE Computer, 1992)](https://doi.org/10.1109/2.161279) — formulación del diseño por contrato; autoridad: IEEE Computer.
- [Liskov y Wing, «A behavioral notion of subtyping» (TOPLAS, 1994)](https://doi.org/10.1145/197320.197383) — subtipado conductual y reglas de sustitución; autoridad: ACM TOPLAS.
- [Eiffel: Design by Contract](https://www.eiffel.com/values/design-by-contract/) — descripción del mecanismo en el lenguaje que lo introdujo; autoridad: Eiffel Software.
- [Python: sentencia `assert`](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) — semántica de `assert` y su desactivación; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Poscondición](./poscondicion.md) · [Postmortem →](./postmortem.md)
