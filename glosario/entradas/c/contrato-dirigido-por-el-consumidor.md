# Contrato dirigido por el consumidor

[↑ Glosario](../../README.md) · [← Contrato del consumidor](./contrato-del-consumidor.md) · [Contrato ejecutable →](./contrato-ejecutable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Contrato escrito por quien consume, que expresa solo lo que usa.

Definición de trabajo de [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md).

## Por qué importa

En [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md), el tema «Contratos dirigidos por el consumidor» importa porque avisan solo a quien depende de lo que cambia.

## Cómo funciona

Según [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md), en la sección «Contratos dirigidos por el consumidor»:

Un contrato dirigido por el consumidor lista lo que el consumidor lee: qué campos, con qué tipo y qué valores. El proveedor ejecuta los contratos de todos sus consumidores contra cada cambio. Lo bueno es que avisa a quien depende de lo que cambió y no a los demás: quitar un campo que nadie lee no genera una alarma. Lo malo es que exige que cada consumidor declare su uso con honestidad: un contrato incompleto produce falsa seguridad.

Según [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md), en la sección «Contratos dirigidos por el consumidor»:

En el enfoque de Fowler, cada consumidor expresa en una prueba qué espera de la respuesta del proveedor: los campos que usa y sus tipos, no los que el proveedor devuelve. El proveedor reúne esos contratos y los ejecuta antes de cada cambio; si alguno falla, sabe qué consumidor se rompería y por qué. Su virtud es que traslada el conocimiento del uso al lugar donde se decide el cambio. Su coste es organizativo: alguien debe publicar, versionar y mantener los contratos de los consumidores.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md):

El equipo del servicio de notas mantiene en su repositorio una carpeta `contratos/` con un archivo por consumidor (`panel.json`, `exportador.json`, `avisos.json`) que lista los campos, tipos y valores que ese consumidor usa y, desde un incidente, el orden de la lista. La integración continua del servicio ejecuta los tres contratos contra su respuesta en cada propuesta de cambio y falla con el nombre del consumidor afectado. Los equipos de los consumidores abren un contrato nuevo cuando empiezan a usar un campo, y retiran las cláusulas que dejaron de usar.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md)) son:

- **El consumidor falla en producción y sus pruebas pasan** — causa: el doble refleja una versión antigua del proveedor. Corrección: verificar el doble contra el proveedor con el mismo contrato.
- **El proveedor recibe alarmas por cambios que nadie usa** — causa: comparación de esquema completo. Corrección: contratos por consumidor.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con un proveedor y un consumidor sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. No se usó red, servidor HTTP ni herramienta de contratos; los ocho cambios, los tres consumidores y el grafo de siete interfaces son del autor. La verificación del contrato es un verificador mínimo y su exactitud real es desconocida.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md), [SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrato](./contrato.md), [Cambio compatible](./cambio-compatible.md), [Contrato de consumidor](./contrato-de-consumidor.md), [Doble de prueba](../d/doble-de-prueba.md), [Interfaz](../i/interfaz.md), [Propiedad](../p/propiedad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-166 — Especificaciones ejecutables y pruebas contractuales](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), [SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md).

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

[↑ Glosario](../../README.md) · [← Contrato del consumidor](./contrato-del-consumidor.md) · [Contrato ejecutable →](./contrato-ejecutable.md)
