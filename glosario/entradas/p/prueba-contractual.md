# Prueba contractual

[↑ Glosario](../../README.md) · [← Prueba basada en requisitos](./prueba-basada-en-requisitos.md) · [Prueba de arquitectura →](./prueba-de-arquitectura.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Prueba que verifica que un proveedor cumple lo que un contrato afirma.

Definición de trabajo de [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md).

## Por qué importa

La clase donde se define, [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md), existe con este propósito: la clase existe para convertir una especificación en algo que se ejecuta contra el sistema, y para decidir qué tipo de prueba protege a quién: las pruebas del proveedor, los contratos dirigidos por el consumidor, las propiedades con reducción de contraejemplos y los dobles de prueba.

## Cómo funciona

[SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md):

En la plataforma, cada consumidor mantiene su contrato en su repositorio y lo publica en una carpeta compartida con su versión. El proveedor ejecuta todos los contratos publicados en integración continua antes de cada cambio y falla con el nombre del consumidor y del campo. Una carpeta de propiedades ejecuta la deduplicación y la regla de penalización con entradas generadas y reduce los contraejemplos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md)) son:

- **Las pruebas del consumidor pasan y la integración falla** — causa: el doble no se verifica contra el proveedor. Corrección: verificar cada doble contra el proveedor real de forma periódica.
- **El proveedor despliega un cambio que rompe a un cliente** — causa: solo prueba su propio esquema, generado desde su código. Corrección: ejecutar contratos de consumidor antes de cada cambio.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): matriz y reducción idénticas, latencias distintas y variables entre ejecuciones. No se usó Pact ni Hypothesis, los consumidores y los cambios son construcciones del autor y el servidor es local, sin red. La siguiente clase reúne lo anterior en un taller de extremo a extremo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrato](../c/contrato.md), [Contrato de consumidor](../c/contrato-de-consumidor.md), [Contrato dirigido por el consumidor](../c/contrato-dirigido-por-el-consumidor.md), [Doble de prueba](../d/doble-de-prueba.md), [Propiedad](./propiedad.md), [Reducción](../r/reduccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), [SE-068](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md), [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler: Consumer-Driven Contracts](https://martinfowler.com/articles/consumerDrivenContracts.html) — contratos que expresan lo que cada consumidor usa; autoridad: martinfowler.com.
- [Pact documentation](https://docs.pact.io/) — implementación del enfoque dirigido por el consumidor; autoridad: proyecto Pact.
- [Claessen y Hughes, «QuickCheck» (ICFP, 2000)](https://doi.org/10.1145/351240.351266) — pruebas basadas en propiedades y reducción; autoridad: ACM SIGPLAN ICFP.
- [Hypothesis documentation](https://hypothesis.readthedocs.io/en/latest/) — biblioteca de pruebas de propiedades para Python con reducción; autoridad: proyecto Hypothesis.
- [Python: `doctest`](https://docs.python.org/3/library/doctest.html) — ejemplos ejecutables dentro de la documentación; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Prueba basada en requisitos](./prueba-basada-en-requisitos.md) · [Prueba de arquitectura →](./prueba-de-arquitectura.md)
