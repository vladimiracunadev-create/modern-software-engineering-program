# Sonda de resiliencia

[↑ Glosario](../../README.md) · [← Sonda de preparación](./sonda-de-preparacion.md) · [Sonda sintética →](./sonda-sintetica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Comprobación automática del estado del sistema durante un experimento.

Definición de trabajo de [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md).

## Por qué importa

La clase donde se define, [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), existe con este propósito: en Kubernetes y en la nube la falla se declara como un recurso (un experimento con alcance, programación y condiciones de parada), y esa declaración, con sus privilegios, es lo que hay que gobernar.

## Cómo funciona

Según [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md):

LitmusChaos es otro marco nativo de la nube, un proyecto incubado de la CNCF, que adopta un enfoque «nativo de Kubernetes» para declarar la intención del caos con recursos personalizados. Distingue el **experimento de caos** (la unidad fundamental), el centro de caos (`ChaosCenter`) como plano de control, un repositorio de experimentos (`ChaosHub`) y las **sondas de resiliencia** (*resilience probes*) que comprueban de forma automática el estado del sistema durante el experimento. Esa última idea, la comprobación continua integrada al experimento, es el equivalente operativo del estado estable de `SE-505` y de la condición de aborto de `SE-506`.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md):

Supón, como caso hipotético y no como medición, que el equipo de la API de entregas rellena la tabla de criterios con su catálogo de doce fallas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md)) son:

- **La falla inyectada no produce ningún efecto** — causa: la herramienta actúa en otra capa. Corrección: elegir por capa antes que por catálogo.
- **La falla no se retira al terminar** — causa: reversión no probada o componente caído. Corrección: verificar el retiro y tener un segundo camino.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Distingue el **experimento de caos** (la unidad fundamental), el centro de caos (`ChaosCenter`) como plano de control, un repositorio de experimentos (`ChaosHub`) y las **sondas de resiliencia** (*resilience probes*) que comprueban de forma automática el estado del sistema durante el experimento. ([SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Comprobación automática](../c/comprobacion-automatica.md), [Estado](../e/estado.md), [Condición de parada](../c/condicion-de-parada.md), [Orquestador de caos](../o/orquestador-de-caos.md), [Plantilla de experimento](../p/plantilla-de-experimento.md), [Proxy de inyección](../p/proxy-de-inyeccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Toxiproxy](https://github.com/Shopify/toxiproxy) — proxy TCP de inyección, tóxicos y API HTTP; autoridad: repositorio oficial de Shopify.
- [Chaos Mesh](https://chaos-mesh.org/docs/) — plataforma de caos para Kubernetes; autoridad: documentación del proyecto Chaos Mesh.
- [LitmusChaos](https://docs.litmuschaos.io/docs/introduction/what-is-litmus) — marco de caos nativo de Kubernetes; autoridad: documentación del proyecto LitmusChaos (CNCF).
- [Azure Chaos Studio](https://learn.microsoft.com/en-us/azure/chaos-studio/chaos-studio-overview) — espacios de trabajo y escenarios; autoridad: documentación de Microsoft.
- [Netflix Chaos Monkey](https://github.com/Netflix/chaosmonkey) — descripción y requisitos actuales; autoridad: repositorio oficial de Netflix.

---

[↑ Glosario](../../README.md) · [← Sonda de preparación](./sonda-de-preparacion.md) · [Sonda sintética →](./sonda-sintetica.md)
