# Camino dorado

[↑ Glosario](../../README.md) · [← Camino crítico](./camino-critico.md) · [Camino feliz →](./camino-feliz.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Forma recomendada, soportada y automatizada de realizar una tarea frecuente, con las guardas incorporadas.

Definición de trabajo de [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md): Forma recomendada y soportada de realizar una tarea común, no obligatoria.

## Por qué importa

En [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), el tema «Camino dorado» importa porque quita pasos y decisiones, no libertad.

En [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), el tema «Camino dorado» importa porque los valores por defecto ahorran decisiones; deben cubrir y ser fáciles de empezar.

## Cómo funciona

Según [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), en la sección «Camino dorado»:

Un camino dorado, o camino pavimentado, es la forma recomendada, soportada y automatizada de hacer algo frecuente, como crear un servicio nuevo. Incorpora las guardas que de otro modo cada equipo debería recordar: límites de recursos, un usuario sin privilegios, una etiqueta de dueño, sondas de salud, imágenes con versión fija. No es una obligación: quien tenga una necesidad distinta puede apartarse, asumiendo el costo de mantener lo suyo. Lo que lo hace valioso no es la libertad sino el costo: el camino más fácil es también el correcto. Si lo correcto exige más pasos que lo incorrecto, la gente elige lo incorrecto.

## Ejemplo

Ejemplo de [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) (sección «Caso conductor»):

La plataforma de entregas es el caso conductor de la [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md). Esta clase deja el décimo artefacto: el camino dorado y su verificador. `SE-407` pone todo a prueba en un taller: desplegar y destruir un entorno de forma segura. Cambia una regla, por ejemplo exige dos réplicas en todos los entornos, y mira cuántos servicios dejan de cumplir.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Nadie usa el camino dorado** — causa: cobertura baja o costo de empezar alto. Corrección: medir ambos; ampliar la cobertura o simplificar el inicio. ([SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un camino dorado, o camino pavimentado, es la forma recomendada, soportada y automatizada de hacer algo frecuente, como crear un servicio nuevo. ([SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Guarda](../g/guarda.md), [Tarea](../t/tarea.md), [Autoservicio](../a/autoservicio.md), [Carga cognitiva](./carga-cognitiva.md), [Catálogo de servicios](./catalogo-de-servicios.md), [Excepción registrada](../e/excepcion-registrada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-407](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md), [SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md), [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [CNCF Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/) — qué es una plataforma interna y qué ofrece; autoridad: CNCF TAG App Delivery.
- [Team Topologies](https://teamtopologies.com/) — equipos de plataforma y carga cognitiva; autoridad: sitio de los autores del libro.
- [DORA](https://dora.dev/) — investigación sobre desempeño de entrega de software; autoridad: programa de investigación DORA.
- [Backstage: What is Backstage?](https://backstage.io/docs/overview/what-is-backstage/) — portal de desarrollo con catálogo y plantillas; autoridad: documentación del proyecto.
- [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/) — políticas como código; autoridad: documentación del proyecto.

---

[↑ Glosario](../../README.md) · [← Camino crítico](./camino-critico.md) · [Camino feliz →](./camino-feliz.md)
