# Blue-green

[↑ Glosario](../../README.md) · [← Bloqueo del estado](./bloqueo-del-estado.md) · [BM25 →](./bm25.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Despliegue con dos entornos completos entre los que se cambia el tráfico.

Definición de trabajo de [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md).

## Por qué importa

La clase donde se define, [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md), existe con este propósito: la clase existe para que decidas cómo llevar una versión nueva a producción de forma que un defecto dañe a pocas personas, se detecte pronto y se pueda deshacer.

## Cómo funciona

Según [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md):

Un despliegue **por oleadas** (*rolling*) reemplaza servidores en lotes: el riesgo se reparte en el tiempo, pero ambas versiones conviven y el retroceso es otra oleada. **Blue-green** mantiene dos entornos completos; el tráfico se dirige a uno, y el otro recibe la versión nueva y se prueba sin usuarios; el cambio es instantáneo y el retroceso, volver a dirigir el tráfico, pero el cambio expone a todas las personas a la vez y el coste es doble infraestructura. **Canary** dirige una fracción pequeña del tráfico a la versión nueva y compara con la anterior en paralelo; reduce el número de personas expuestas al defecto y obtiene evidencia con tráfico real.

Según [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md):

Responden preguntas distintas. Blue-green da un cambio y un retroceso instantáneos y permite probar el entorno nuevo sin usuarios; no limita la exposición una vez hecho el cambio. Canary limita la exposición y obtiene evidencia con tráfico real. Se combinan: se prueba el entorno verde, se envía una fracción pequeña y se promueve por fases.

## Ejemplo

Ejemplo de [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) (sección «Preguntas frecuentes»):

Responden preguntas distintas. Blue-green da un cambio y un retroceso instantáneos y permite probar el entorno nuevo sin usuarios; no limita la exposición una vez hecho el cambio. Canary limita la exposición y obtiene evidencia con tráfico real. Se combinan: se prueba el entorno verde, se envía una fracción pequeña y se promueve por fases.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md)) son:

- **El despliegue se revierte sin defecto** — causa: umbral de decisión única evaluado repetidamente. Corrección: umbral mayor, mínimo de muestra o prueba secuencial.
- **Un defecto pequeño no se detecta** — causa: canario y ventana insuficientes. Corrección: definir el defecto mínimo relevante y dimensionar para él.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Blue-green** mantiene dos entornos completos; el tráfico se dirige a uno, y el otro recibe la versión nueva y se prueba sin usuarios; el cambio es instantáneo y el retroceso, volver a dirigir el tráfico, pero el cambio expone a todas las personas a la vez y el coste es doble infraestructura. ([SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md))
- Blue-green da un cambio y un retroceso instantáneos y permite probar el entorno nuevo sin usuarios; no limita la exposición una vez hecho el cambio. ([SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Entorno](../e/entorno.md), [Escalón de tráfico](../e/escalon-de-trafico.md), [Expandir y contraer](../e/expandir-y-contraer.md), [Falsa alarma](../f/falsa-alarma.md), [Línea base](../l/linea-base.md), [Retroceso](../r/retroceso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md), [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «CanaryRelease»](https://martinfowler.com/bliki/CanaryRelease.html) — despliegue progresivo; autoridad: autor del texto.
- [Fowler, «BlueGreenDeployment»](https://martinfowler.com/bliki/BlueGreenDeployment.html) — dos entornos y cambio de tráfico; autoridad: autor del texto.
- [Google SRE Workbook: Canarying Releases](https://sre.google/workbook/canarying-releases/) — diseño de un canario; autoridad: Google, libro de ingeniería de confiabilidad.
- [Fowler, «ParallelChange»](https://martinfowler.com/bliki/ParallelChange.html) — expandir, migrar y contraer; autoridad: autor del texto.
- [Google SRE: Release Engineering](https://sre.google/sre-book/release-engineering/) — entrega y retroceso; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Bloqueo del estado](./bloqueo-del-estado.md) · [BM25 →](./bm25.md)
