# Tóxico

[↑ Glosario](../../README.md) · [← Tormenta de reintentos](./tormenta-de-reintentos.md) · [Trabajador →](./trabajador.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Alteración configurable de una conexión (latencia, corte, límite de datos, pérdida) que el proxy aplica en una dirección.

Definición de trabajo de [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md).

## Por qué importa

La clase donde se define, [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), existe con este propósito: en Kubernetes y en la nube la falla se declara como un recurso (un experimento con alcance, programación y condiciones de parada), y esa declaración, con sus privilegios, es lo que hay que gobernar.

## Cómo funciona

Según [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md):

Toxiproxy es un proxy TCP escrito en Go que se interpone entre un cliente y su dependencia y se controla con una API HTTP. La aplicación no se modifica: solo apunta a la dirección del proxy en lugar de la del servicio, y desde la prueba se activan, modifican y retiran **tóxicos** que alteran lo que atraviesa la conexión. Según su documentación, los tóxicos disponibles incluyen `latency` (retraso, con variación opcional), `bandwidth` (límite de KB por segundo), `slow_close` (retrasa el cierre del socket), `timeout` (detiene todos los datos y cierra la conexión pasado un tiempo, o la deja abierta y descarta los datos si el tiempo es 0), `reset_peer` (simula un reinicio de conexión), `slicer` (fragmenta los datos), `limit_data` (cierra tras transmitir cierto volumen) y `packet_loss` (descarta fragmentos al azar).

## Ejemplo

Ejemplo de [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md) (sección «Ejemplo mínimo»):

El fragmento mide el tiempo que tarda un cliente con espera de 300 ms en una petición local contra un servidor que responde de inmediato. Antes de ejecutarlo, predice cuánto tarda y si el tiempo cambia al pasar por un proxy sin tóxico.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md)) son:

- **La falla inyectada no produce ningún efecto** — causa: la herramienta actúa en otra capa. Corrección: elegir por capa antes que por catálogo.
- **La falla no se retira al terminar** — causa: reversión no probada o componente caído. Corrección: verificar el retiro y tener un segundo camino.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La aplicación no se modifica: solo apunta a la dirección del proxy en lugar de la del servicio, y desde la prueba se activan, modifican y retiran **tóxicos** que alteran lo que atraviesa la conexión. ([SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Corte](../c/corte.md), [Latencia](../l/latencia.md), [Límite](../l/limite.md), [Proxy](../p/proxy.md), [Condición de parada](../c/condicion-de-parada.md), [Orquestador de caos](../o/orquestador-de-caos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md).

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

[↑ Glosario](../../README.md) · [← Tormenta de reintentos](./tormenta-de-reintentos.md) · [Trabajador →](./trabajador.md)
