# Revisor de coherencia

[↑ Glosario](../../README.md) · [← Revisiones a ignorar](./revisiones-a-ignorar.md) · [Revocación →](./revocacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Comprobación que verifica que las partes de un contrato (rangos, ejemplos, errores, invariantes) concuerdan entre sí.

Definición de trabajo de [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md).

## Por qué importa

La clase donde se define, [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md), existe con este propósito: el taller existe para recorrer, de principio a fin y con una sola regla, el camino que las seis clases anteriores desarmaron: de una intención en prosa a un contrato con cláusulas completas, ejemplos que separan variantes, un revisor mecánico y una decisión humana sobre lo que ningún revisor ve.

## Cómo funciona

Según [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md):

El contrato mismo tiene defectos posibles: un rango estrechado o ensanchado, un ejemplo de error eliminado, un error sin ejemplo, un invariante sin prueba, un mensaje que miente. Un revisor de coherencia interna detecta los que rompen la relación entre partes (ejemplos y rangos, errores y ejemplos, invariantes y pruebas) y no los que cambian el sentido sin romper la coherencia (un rango más permisivo, un invariante con la condición contraria, un mensaje distinto). Mutar el contrato y medir da el mapa de lo que debe revisar una persona.

## Ejemplo

Ejemplo de [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md) (sección «Caso conductor»):

La plataforma de entregas es el caso conductor de la [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md). Este taller deja un contrato de la regla de penalización con cláusulas revisadas, cinco ejemplos que separan las variantes distinguibles, un revisor de coherencia y una lista de decisiones humanas. `SE-168` lo empaquetará con el resto de artefactos de la parte, con enlaces entre intención, requisitos, contratos, ejemplos y pruebas. Cambia después una sola decisión, el tope del 50 % al 30 %, y revisa qué cláusulas, ejemplos y pruebas deben cambiar.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md)) son:

- **El linter acepta cláusulas vacías o rechaza buenas** — causa: se evaluó solo con los casos de ajuste. Corrección: evaluar con cláusulas nuevas y declarar la exactitud medida.
- **Se añaden ejemplos sin que bajen los supervivientes** — causa: los ejemplos son típicos y no separan mutantes. Corrección: añadir el contraejemplo más pequeño de un mutante vivo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un revisor de coherencia interna detecta los que rompen la relación entre partes (ejemplos y rangos, errores y ejemplos, invariantes y pruebas) y no los que cambian el sentido sin romper la coherencia (un rango más permisivo, un invariante con la condición contraria, un mensaje distinto). ([SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrato](../c/contrato.md), [Invariante](../i/invariante.md), [Rango](./rango.md), [Bucle de contraejemplos](../b/bucle-de-contraejemplos.md), [Cláusula completa](../c/clausula-completa.md), [Decisión humana abierta](../d/decision-humana-abierta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md).

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

[↑ Glosario](../../README.md) · [← Revisiones a ignorar](./revisiones-a-ignorar.md) · [Revocación →](./revocacion.md)
