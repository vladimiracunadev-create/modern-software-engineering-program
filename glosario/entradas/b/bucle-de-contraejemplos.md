# Bucle de contraejemplos

[↑ Glosario](../../README.md) · [← Brief como contrato de evidencia](./brief-como-contrato-de-evidencia.md) · [Bucle de eventos y cola →](./bucle-de-eventos-y-cola.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Procedimiento que añade el ejemplo más pequeño que distingue a la regla de un mutante superviviente y repite.

Definición de trabajo de [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md).

## Por qué importa

La clase donde se define, [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md), existe con este propósito: el taller existe para recorrer, de principio a fin y con una sola regla, el camino que las seis clases anteriores desarmaron: de una intención en prosa a un contrato con cláusulas completas, ejemplos que separan variantes, un revisor mecánico y una decisión humana sobre lo que ningún revisor ve.

## Cómo funciona

Según [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md):

Un ejemplo vale por lo que separa. El bucle de contraejemplos parte de los ejemplos de la intención, busca una variante defectuosa que todavía pasa, encuentra el ejemplo más pequeño que la distingue de la regla y lo añade; repite hasta que solo sobreviven variantes que ningún ejemplo puede separar (las equivalentes). Es el mismo principio de la verificación guiada por contraejemplos, aplicado a los ejemplos del contrato. Su límite es que no sabe si una variante superviviente es equivalente: detenerse es una decisión humana.

Según [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md):

En el taller, cada grupo recibe la intención de la secretaría y produce un archivo de contrato con cláusulas, ejemplos y errores. El archivo pasa tres revisiones automáticas: forma de las cláusulas (con su exactitud declarada), coherencia interna (rangos, ejemplos, errores, invariantes) y supervivencia de mutantes de la regla de referencia (con el bucle de contraejemplos). Una cuarta revisión, humana, lee lo que las tres no ven: una persona de la secretaría firma cada cláusula que cambie lo que se debe a una estudiante y el contrato registra las decisiones abiertas con responsable y fecha.

## Ejemplo

Ejemplo de [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md) (sección «Ejemplo profesional»):

En el taller, cada grupo recibe la intención de la secretaría y produce un archivo de contrato con cláusulas, ejemplos y errores. El archivo pasa tres revisiones automáticas: forma de las cláusulas (con su exactitud declarada), coherencia interna (rangos, ejemplos, errores, invariantes) y supervivencia de mutantes de la regla de referencia (con el bucle de contraejemplos). Una cuarta revisión, humana, lee lo que las tres no ven: una persona de la secretaría firma cada cláusula que cambie lo que se debe a una estudiante y el contrato registra las decisiones abiertas con responsable y fecha.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md)) son:

- **El linter acepta cláusulas vacías o rechaza buenas** — causa: se evaluó solo con los casos de ajuste. Corrección: evaluar con cláusulas nuevas y declarar la exactitud medida.
- **Se añaden ejemplos sin que bajen los supervivientes** — causa: los ejemplos son típicos y no separan mutantes. Corrección: añadir el contraejemplo más pequeño de un mutante vivo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El bucle de contraejemplos parte de los ejemplos de la intención, busca una variante defectuosa que todavía pasa, encuentra el ejemplo más pequeño que la distingue de la regla y lo añade; repite hasta que solo sobreviven variantes que ningún ejemplo puede separar (las equivalentes). ([SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Mutante superviviente](../m/mutante-superviviente.md), [Variante defectuosa](../v/variante-defectuosa.md), [Regla](../r/regla.md), [Cláusula completa](../c/clausula-completa.md), [Decisión humana abierta](../d/decision-humana-abierta.md), [Revisor de coherencia](../r/revisor-de-coherencia.md).
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

[↑ Glosario](../../README.md) · [← Brief como contrato de evidencia](./brief-como-contrato-de-evidencia.md) · [Bucle de eventos y cola →](./bucle-de-eventos-y-cola.md)
