# Cláusula completa

[↑ Glosario](../../README.md) · [← Clase de seguridad del software](./clase-de-seguridad-del-software.md) · [Clausura transitiva →](./clausura-transitiva.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Afirmación de un contrato con actor, modal, resultado observable y límite.

Definición de trabajo de [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md).

## Por qué importa

La clase donde se define, [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md), existe con este propósito: el taller existe para recorrer, de principio a fin y con una sola regla, el camino que las seis clases anteriores desarmaron: de una intención en prosa a un contrato con cláusulas completas, ejemplos que separan variantes, un revisor mecánico y una decisión humana sobre lo que ningún revisor ve.

## Cómo funciona

Según [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md):

La regla tiene cuatro expresiones regulares (actor reconocido, modal, observable y límite) y una cláusula es «completa» si cumple las cuatro. Se ajustó con ocho cláusulas escritas por el autor, cuatro completas y cuatro incompletas, y acertó **8 de 8**: 4 aceptadas y 4 rechazadas correctamente. La prueba real son seis cláusulas nuevas que la regla no conocía. Resultado: **5 de 6**. Rechazó una cláusula completa («Ninguna estudiante podrá entregar después del cierre, excepto con una prórroga aprobada por escrito»), porque ni «estudiante» sin artículo, ni «después del cierre», ni «excepto» estaban en sus listas. Las otras cinco (dos aceptadas y tres rechazadas correctas) coincidieron con el juicio del autor.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md):

En el taller, cada grupo recibe la intención de la secretaría y produce un archivo de contrato con cláusulas, ejemplos y errores. El archivo pasa tres revisiones automáticas: forma de las cláusulas (con su exactitud declarada), coherencia interna (rangos, ejemplos, errores, invariantes) y supervivencia de mutantes de la regla de referencia (con el bucle de contraejemplos).

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md)) son:

- **El linter acepta cláusulas vacías o rechaza buenas** — causa: se evaluó solo con los casos de ajuste. Corrección: evaluar con cláusulas nuevas y declarar la exactitud medida.
- **Se añaden ejemplos sin que bajen los supervivientes** — causa: los ejemplos son típicos y no separan mutantes. Corrección: añadir el contraejemplo más pequeño de un mutante vivo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Rechazó una cláusula completa («Ninguna estudiante podrá entregar después del cierre, excepto con una prórroga aprobada por escrito»), porque ni «estudiante» sin artículo, ni «después del cierre», ni «excepto» estaban en sus listas. ([SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Actor](../a/actor.md), [Afirmación](../a/afirmacion.md), [Contrato](./contrato.md), [Límite](../l/limite.md), [Bucle de contraejemplos](../b/bucle-de-contraejemplos.md), [Decisión humana abierta](../d/decision-humana-abierta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Jia y Harman, «An analysis and survey of the development of mutation testing» (IEEE TSE, 2011)](https://doi.org/10.1109/TSE.2010.62) — mutación y mutantes equivalentes; autoridad: IEEE Transactions on Software Engineering.
- [Meyer, «On formalism in specifications» (IEEE Software, 1985)](https://doi.org/10.1109/MS.1985.229776) — defectos de las especificaciones en lenguaje natural; autoridad: IEEE Software.
- [Hall, «Seven myths of formal methods» (IEEE Software, 1990)](https://doi.org/10.1109/52.57887) — qué aportan y qué no los métodos formales; autoridad: IEEE Software.
- [Cucumber: Better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/) — redacción de escenarios declarativos y breves; autoridad: proyecto Cucumber.
- [Fowler: Consumer-Driven Contracts](https://martinfowler.com/articles/consumerDrivenContracts.html) — contratos expresados por el consumidor; autoridad: martinfowler.com.

---

[↑ Glosario](../../README.md) · [← Clase de seguridad del software](./clase-de-seguridad-del-software.md) · [Clausura transitiva →](./clausura-transitiva.md)
