# Proxy de inyección

[↑ Glosario](../../README.md) · [← Proxy](./proxy.md) · [Proyección →](./proyeccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Intermediario en la conexión que altera lo que la atraviesa según el tóxico activo.

Definición de trabajo de [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md).

## Por qué importa

La clase donde se define, [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), existe con este propósito: en Kubernetes y en la nube la falla se declara como un recurso (un experimento con alcance, programación y condiciones de parada), y esa declaración, con sus privilegios, es lo que hay que gobernar.

## Cómo funciona

[SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el cliente de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md):

Supón, como caso hipotético y no como medición, que el equipo de la API de entregas rellena la tabla de criterios con su catálogo de doce fallas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md)) son:

- **La falla inyectada no produce ningún efecto** — causa: la herramienta actúa en otra capa. Corrección: elegir por capa antes que por catálogo.
- **La falla no se retira al terminar** — causa: reversión no probada o componente caído. Corrección: verificar el retiro y tener un segundo camino.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md)) son: Las definiciones son operativas para el cliente de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutó una medición real con sockets en una máquina Windows 11 con CPython 3.12.9, con 30 peticiones secuenciales por escenario y un proxy propio. No se ejecutó ninguna de las herramientas descritas, no se probó su rendimiento ni sus privilegios, y lo que se afirma de ellas procede de sus páginas oficiales, que cambian con las versiones.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Activo](../a/activo.md), [Intermediario](../i/intermediario.md), [Tóxico](../t/toxico.md), [Condición de parada](../c/condicion-de-parada.md), [Orquestador de caos](../o/orquestador-de-caos.md), [Plantilla de experimento](./plantilla-de-experimento.md).
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

[↑ Glosario](../../README.md) · [← Proxy](./proxy.md) · [Proyección →](./proyeccion.md)
