# Mutante superviviente

[↑ Glosario](../../README.md) · [← Mutante equivalente](./mutante-equivalente.md) · [N+1 →](../n/n-mas-1.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Variante defectuosa que pasa todos los ejemplos del conjunto.

Definición de trabajo de [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md).

## Por qué importa

La clase donde se define, [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md), existe con este propósito: el taller existe para recorrer, de principio a fin y con una sola regla, el camino que las seis clases anteriores desarmaron: de una intención en prosa a un contrato con cláusulas completas, ejemplos que separan variantes, un revisor mecánico y una decisión humana sobre lo que ningún revisor ve.

## Cómo funciona

[SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md):

En el taller, cada grupo recibe la intención de la secretaría y produce un archivo de contrato con cláusulas, ejemplos y errores. El archivo pasa tres revisiones automáticas: forma de las cláusulas (con su exactitud declarada), coherencia interna (rangos, ejemplos, errores, invariantes) y supervivencia de mutantes de la regla de referencia (con el bucle de contraejemplos).

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md)) son:

- **El linter acepta cláusulas vacías o rechaza buenas** — causa: se evaluó solo con los casos de ajuste. Corrección: evaluar con cláusulas nuevas y declarar la exactitud medida.
- **Se añaden ejemplos sin que bajen los supervivientes** — causa: los ejemplos son típicos y no separan mutantes. Corrección: añadir el contraejemplo más pequeño de un mutante vivo.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El linter se ajustó con ocho cláusulas y se probó con seis, los mutantes y las mutaciones del contrato son construcciones del autor y no se trabajó con ninguna secretaría ni persona real. La siguiente clase empaqueta todos los artefactos con su trazabilidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Variante defectuosa](../v/variante-defectuosa.md), [Conjunto](../c/conjunto.md), [Variante](../v/variante.md), [Bucle de contraejemplos](../b/bucle-de-contraejemplos.md), [Cláusula completa](../c/clausula-completa.md), [Decisión humana abierta](../d/decision-humana-abierta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md), [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md).

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

[↑ Glosario](../../README.md) · [← Mutante equivalente](./mutante-equivalente.md) · [N+1 →](../n/n-mas-1.md)
