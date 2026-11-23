# Contrato de consumidor

[↑ Glosario](../../README.md) · [← Contrato de comparación](./contrato-de-comparacion.md) · [Contrato de datos →](./contrato-de-datos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Prueba escrita por un consumidor que fija lo que espera de la respuesta de un proveedor.

Definición de trabajo de [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md).

## Por qué importa

En [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), el tema «Contratos de consumidor» importa porque dicen qué usa cada uno y detectan lo que importa.

## Cómo funciona

Según [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), en la sección «Contratos de consumidor»:

En un contrato dirigido por el consumidor, cada consumidor declara qué usa del proveedor (qué campos lee, qué tipos espera) y esa declaración se ejecuta como prueba contra el proveedor antes de publicar un cambio. Detecta lo que importa a quien consume y no alarma por lo que nadie usa. Su límite es que solo cubre a los consumidores que escribieron contrato y a lo que declararon; un consumidor que lee un campo que no declaró queda fuera. La ley de Hyrum dice que habrá más usos de los declarados.

## Ejemplo

Ejemplo de [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) (sección «Caso conductor»):

La plataforma de entregas es el caso conductor de la [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md). Esta clase deja cinco contratos de consumidor, una propiedad con reducción y una comprobación de dobles contra el proveedor real. `SE-167` los integrará en un taller que convierte una intención en un contrato comprobable de extremo a extremo, y `SE-168` los empaquetará con su trazabilidad. Cambia después una sola decisión, retirar el campo `links`, y revisa qué consumidores, ejemplos y pruebas se ven afectados.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un cambio «compatible» rompe a un consumidor** — causa: el verificador comprueba solo la firma. Corrección: añadir contratos de consumidor. ([SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md))
- **El proveedor despliega un cambio que rompe a un cliente** — causa: solo prueba su propio esquema, generado desde su código. Corrección: ejecutar contratos de consumidor antes de cada cambio. ([SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un esquema escrito a mano y compartido con los consumidores es una barrera mejor, y un contrato de consumidor es otra distinta: protege a quien consume, no a quien produce. ([SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espera](../e/espera.md), [Ampliar, migrar y contraer](../a/ampliar-migrar-y-contraer.md), [Compatibilidad hacia atrás](./compatibilidad-hacia-atras.md), [Contrato dirigido por el consumidor](./contrato-dirigido-por-el-consumidor.md), [Doble de prueba](../d/doble-de-prueba.md), [Lector tolerante](../l/lector-tolerante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md), [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Contratos de consumidor».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Semantic Versioning 2.0.0](https://semver.org/) — versionado para comunicar compatibilidad; autoridad: sus autores.
- [Hyrum's Law](https://www.hyrumslaw.com/) — usos no documentados de una interfaz; autoridad: Hyrum Wright.
- [Pact: documentación](https://docs.pact.io/) — pruebas de contrato dirigidas por el consumidor; autoridad: proyecto Pact.
- [Fowler, «Tolerant Reader»](https://martinfowler.com/bliki/TolerantReader.html) — lectores que toleran campos que no conocen; autoridad: Martin Fowler.
- [Fowler, «Parallel Change»](https://martinfowler.com/bliki/ParallelChange.html) — ampliar, migrar y contraer; autoridad: Martin Fowler.

---

[↑ Glosario](../../README.md) · [← Contrato de comparación](./contrato-de-comparacion.md) · [Contrato de datos →](./contrato-de-datos.md)
