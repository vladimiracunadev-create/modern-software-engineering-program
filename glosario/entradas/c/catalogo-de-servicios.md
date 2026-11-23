# Catálogo de servicios

[↑ Glosario](../../README.md) · [← Catálogo de patrones de un sistema](./catalogo-de-patrones-de-un-sistema.md) · [Causa común →](./causa-comun.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Inventario de servicios con sus dueños, ciclo de vida y documentación.

Definición de trabajo de [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md).

## Por qué importa

En [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), el tema «Catálogo de servicios» importa porque sin dueño verificado no hay quién responda en un incidente.

## Cómo funciona

[SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md):

El equipo de plataforma de la API de entregas decide tratar sus capacidades como un producto. Para cada una (servicio nuevo, entorno de vista previa, base de datos, cola, alertas) escribe un dueño, una medida de éxito y una fecha de revisión. Para el camino dorado fija una meta de cobertura del 80 % de lo que piden los equipos (medida preguntando a ocho equipos) y un tiempo de empezar de menos de cuatro horas medido desde la solicitud hasta el primer despliegue.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md)) son:

- **Nadie usa el camino dorado** — causa: cobertura baja o costo de empezar alto. Corrección: medir ambos; ampliar la cobertura o simplificar el inicio.
- **La adopción sube y nadie está contento** — causa: se obligó a usarlo. Corrección: medir satisfacción y preguntar a quien no adoptó.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md)) son: Las definiciones son operativas para la plataforma de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ciclo de vida](./ciclo-de-vida.md), [Ciclo](./ciclo.md), [Inventario](../i/inventario.md), [Servicio](../s/servicio.md), [Autoservicio](../a/autoservicio.md), [Camino dorado](./camino-dorado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [CNCF: Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/) — plataformas internas como producto; autoridad: CNCF TAG App Delivery.
- [CNCF: modelo de madurez de la ingeniería de plataformas](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) — dimensiones de madurez; autoridad: CNCF TAG App Delivery.
- [Backstage: catálogo de software](https://backstage.io/docs/features/software-catalog/) — catálogo basado en metadatos; autoridad: documentación de Backstage.

---

[↑ Glosario](../../README.md) · [← Catálogo de patrones de un sistema](./catalogo-de-patrones-de-un-sistema.md) · [Causa común →](./causa-comun.md)
