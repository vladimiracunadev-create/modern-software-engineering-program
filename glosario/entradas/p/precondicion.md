# Precondición

[↑ Glosario](../../README.md) · [← Precisión](./precision.md) · [Precondición y postcondición →](./precondicion-y-postcondicion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Condición que debe cumplirse al invocar una operación; su incumplimiento es un defecto del cliente.

Definición de trabajo de [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-052 — Invariantes, precondiciones y poscondiciones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md): Propiedad requerida al iniciar una operación.
- En [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md): Lo que debe cumplirse al llamar a una rutina; responsabilidad de quien llama.
- En [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md): Condición sobre el estado del recurso que debe cumplirse para que una solicitud se aplique.

## Por qué importa

En [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md), el tema «Precondiciones» importa porque fijan qué debe cumplir quien llama; una violación es un defecto del cliente, no del proveedor.

En [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md), el tema «Precondiciones» importa porque la producción exige observabilidad, aborto y reversión probados.

## Cómo funciona

Según [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md), en la sección «Precondiciones»:

Una precondición dice qué debe ser cierto al llamar a una operación: `calificar` exige que la calificación no esté publicada; `dar_prórroga` exige horas positivas. El punto conceptual es el reparto de culpa: si la precondición falla, el defecto es del cliente, y el proveedor no tiene por qué comportarse bien. Esa precisión evita código defensivo repetido en cada capa y obliga a decidir quién valida la entrada. Una precondición demasiado débil traslada al proveedor casos que debería rechazar; una demasiado fuerte hace inutilizable la operación.

Según [SE-052 — Invariantes, precondiciones y poscondiciones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md), en la sección «Precondición»:

La precondición describe estados de entrada que una operación acepta. No es una esperanza escondida. `destino autorizado` y `presupuesto > costo_estimado` permiten decidir antes de ejecutar. Si el consumidor puede violarla, la interfaz debe validar y producir un error observable.

## Ejemplo

Ejemplo de [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) (sección «Ejemplo mínimo»):

El fragmento declara una precondición y una postcondición para la prórroga. Antes de ejecutarlo, predice cuál de las dos llamadas falla.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una subclase rompe a los clientes de la base pese a compilar** — causa: reforzó una precondición o debilitó una postcondición. Corrección: aplicar la regla: aceptar al menos lo mismo, garantizar al menos lo mismo. ([SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md))
- **Una precondición validada en tres capas distintas** — causa: no se acordó quién valida la entrada. Corrección: decidir un responsable y expresar el resto como afirmaciones internas. ([SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md))
- **La función falla sin decir quién se equivocó** — causa: contrato implícito. Corrección: escribir precondición, invariante y poscondición. ([SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El punto conceptual es el reparto de culpa: si la precondición falla, el defecto es del cliente, y el proveedor no tiene por qué comportarse bien. ([SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md))
- No: la validación trata con entradas de fuera del sistema (formularios, mensajes) y debe responder con un error amable; la precondición expresa lo que un componente interno da por hecho. ([SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Condición](../c/condicion.md), [Estado](../e/estado.md), [Operación](../o/operacion.md), [Propiedad](./propiedad.md), [Composición](../c/composicion.md), [Contrato ejecutable](../c/contrato-ejecutable.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-052 — Invariantes, precondiciones y poscondiciones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-159 — Contratos, invariantes y diseño por contrato](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.
- [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (32 clases más lo mencionan; las que más):

[SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md), [SE-089](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-089-grafos-y-recorridos/README.md), [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), [SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md), [SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-051](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Precondiciones».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Hoare, «An axiomatic basis for computer programming» (CACM, 1969)](https://doi.org/10.1145/363235.363259) — tripleta precondición–instrucción–postcondición; autoridad: Communications of the ACM.
- [Meyer, «Applying design by contract» (IEEE Computer, 1992)](https://doi.org/10.1109/2.161279) — formulación del diseño por contrato; autoridad: IEEE Computer.
- [Liskov y Wing, «A behavioral notion of subtyping» (TOPLAS, 1994)](https://doi.org/10.1145/197320.197383) — subtipado conductual y reglas de sustitución; autoridad: ACM TOPLAS.
- [Eiffel: Design by Contract](https://www.eiffel.com/values/design-by-contract/) — descripción del mecanismo en el lenguaje que lo introdujo; autoridad: Eiffel Software.
- [Python: sentencia `assert`](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) — semántica de `assert` y su desactivación; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Precisión](./precision.md) · [Precondición y postcondición →](./precondicion-y-postcondicion.md)
