# Prueba de integración

[↑ Glosario](../../README.md) · [← Prueba de frontera](./prueba-de-frontera.md) · [Prueba de pico →](./prueba-de-pico.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Prueba que ejecuta dos o más piezas reales juntas y comprueba el acuerdo entre ellas.

Definición de trabajo de [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md).

## Por qué importa

La clase donde se define, [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md), existe con este propósito: la clase existe para que compruebes que las piezas de un sistema funcionan juntas sin levantar el sistema entero, y para que protejas el acuerdo entre un proveedor y sus consumidores con un contrato que cada parte pueda verificar.

## Cómo funciona

Según [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md):

Los componentes se comunican a través de interfaces: una respuesta JSON, una tabla compartida, una cola. Cada uno asume algo sobre la otra parte: nombres, tipos, valores posibles, orden, cuántos elementos aparecen por página. Un defecto de integración es una asunción que ya no se cumple. Ninguna prueba de una sola parte lo ve, porque cada una se comprueba contra su propia versión de la asunción. Las pruebas de integración ejecutan dos o más piezas reales juntas y comprueban que la asunción de una coincide con el comportamiento de la otra.

Según [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md):

El equipo del servicio de notas mantiene en su repositorio una carpeta `contratos/` con un archivo por consumidor (`panel.json`, `exportador.json`, `avisos.json`) que lista los campos, tipos y valores que ese consumidor usa y, desde un incidente, el orden de la lista. La integración continua del servicio ejecuta los tres contratos contra su respuesta en cada propuesta de cambio y falla con el nombre del consumidor afectado. Los equipos de los consumidores abren un contrato nuevo cuando empiezan a usar un campo, y retiran las cláusulas que dejaron de usar. Las pruebas de integración del panel ejecutan el panel contra la respuesta real del servicio con una base sembrada, una por interfaz del recorrido; los tres recorridos de extremo a extremo (`SE-424`) quedan para el comportamiento visible.

## Ejemplo

Ejemplo de [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) (sección «Ejemplo profesional»):

El equipo del servicio de notas mantiene en su repositorio una carpeta `contratos/` con un archivo por consumidor (`panel.json`, `exportador.json`, `avisos.json`) que lista los campos, tipos y valores que ese consumidor usa y, desde un incidente, el orden de la lista. La integración continua del servicio ejecuta los tres contratos contra su respuesta en cada propuesta de cambio y falla con el nombre del consumidor afectado. Los equipos de los consumidores abren un contrato nuevo cuando empiezan a usar un campo, y retiran las cláusulas que dejaron de usar.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md)) son:

- **El consumidor falla en producción y sus pruebas pasan** — causa: el doble refleja una versión antigua del proveedor. Corrección: verificar el doble contra el proveedor con el mismo contrato.
- **El proveedor recibe alarmas por cambios que nadie usa** — causa: comparación de esquema completo. Corrección: contratos por consumidor.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Las pruebas de integración siguen siendo necesarias para lo que el contrato no dice (transacciones, ordenamiento, efectos). ([SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md), [SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cambio compatible](../c/cambio-compatible.md), [Contrato](../c/contrato.md), [Contrato dirigido por el consumidor](../c/contrato-dirigido-por-el-consumidor.md), [Interfaz](../i/interfaz.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (23 clases más lo mencionan; las que más):

[SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md), [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md), [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md), [SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), [SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md), [SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md), [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Martin Fowler, «IntegrationTest»](https://martinfowler.com/bliki/IntegrationTest.html) — pruebas de integración; autoridad: autor del texto.
- [Martin Fowler, «ContractTest»](https://martinfowler.com/bliki/ContractTest.html) — pruebas de contrato; autoridad: autor del texto.
- [Ian Robinson, «Consumer-Driven Contracts»](https://martinfowler.com/articles/consumerDrivenContracts.html) — contratos por consumidor; autoridad: autor del texto.
- [Documentación de Pact](https://docs.pact.io/) — herramienta de contratos; autoridad: documentación oficial.
- [Especificación de JSON Schema](https://json-schema.org/specification) — descripción de documentos JSON; autoridad: especificación oficial.

---

[↑ Glosario](../../README.md) · [← Prueba de frontera](./prueba-de-frontera.md) · [Prueba de pico →](./prueba-de-pico.md)
