# Plataforma interna

[↑ Glosario](../../README.md) · [← Plataforma efectiva](./plataforma-efectiva.md) · [Plataforma mínima →](./plataforma-minima.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Conjunto de capacidades de infraestructura y entrega que un equipo ofrece como producto a otros equipos de la organización.

Definición de trabajo de [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md): Conjunto de capacidades que un equipo ofrece como producto a otros equipos de la organización.

## Por qué importa

La clase donde se define, [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), existe con este propósito: la clase existe para que puedas tratar la infraestructura como un producto con usuarios: los equipos que despliegan servicios.

## Cómo funciona

Según [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md):

El libro Team Topologies y el documento de plataformas de la CNCF coinciden en un punto: una plataforma interna existe para reducir la carga cognitiva de los equipos que construyen producto, ofreciéndoles capacidades listas para usar en autoservicio. Tratarla como producto significa tener usuarios identificados, entender qué les cuesta y medir si lo que se ofrece lo reduce. Sin eso se vuelve un proyecto de infraestructura con su propia agenda. Una plataforma se vuelve costosa de mantener cuando ofrece mucho y se usa poco, y se vuelve inútil cuando no ofrece lo que el equipo necesita justo cuando lo necesita.

Según [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md):

Traslada el análisis a otro dominio (por ejemplo, la plataforma interna de una tienda con equipos de catálogo, pagos y logística): cambia los servicios y conserva el procedimiento de contar pasos y probabilidades de error, simular la cola de soporte, escribir un verificador con mutaciones y declarar lo que no ve. La transferencia está lograda cuando puedes decir qué quitarías primero del camino de otro equipo, no cuando las plantillas se parecen.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md):

El equipo de plataforma de la plataforma de entregas escribe la historia de su usuario principal: un equipo de producto que necesita un servicio nuevo en producción en un día, de forma segura. Reduce los 23 pasos a 5: una plantilla crea el repositorio, la cuenta y la red; otra, el despliegue con límites y sondas; otra, las alarmas; el equipo escribe el código y revisa un plan.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md)) son:

- **Los equipos no usan el camino** — causa: es más difícil que lo manual o no cubre su caso. Corrección: medir pasos y excepciones y mejorarlo.
- **El equipo de plataforma está saturado de solicitudes** — causa: baja adopción y servicios hechos a mano. Corrección: reducir pasos del camino y atender primero las excepciones.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Traslada el análisis a otro dominio (por ejemplo, la plataforma interna de una tienda con equipos de catálogo, pagos y logística): cambia los servicios y conserva el procedimiento de contar pasos y probabilidades de error, simular la cola de soporte, escribir un verificador con mutaciones y declarar lo que no ve. ([SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md))
- El documento de la CNCF define una plataforma interna como una colección de capacidades —aprovisionamiento, canalizaciones, observabilidad, seguridad— ofrecidas a los equipos de producto con un enfoque de producto: se conocen sus necesidades, se fijan interfaces, se mide su uso y se retira lo que no sirve. ([SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Conjunto](../c/conjunto.md), [Organización](../o/organizacion.md), [Producto](./producto.md), [Autoservicio](../a/autoservicio.md), [Camino dorado](../c/camino-dorado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-537](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md), [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md), [SE-407](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md), [SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md), [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md).

**Aparece en los casos de estudio:** [Mercado Libre](../../../casos/exito/mercado-libre.md), [Spotify](../../../casos/exito/spotify.md).

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

[↑ Glosario](../../README.md) · [← Plataforma efectiva](./plataforma-efectiva.md) · [Plataforma mínima →](./plataforma-minima.md)
