# Carga cognitiva

[↑ Glosario](../../README.md) · [← Carga analítica](./carga-analitica.md) · [Carga cognitiva de un equipo →](./carga-cognitiva-de-un-equipo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Esfuerzo mental que un equipo dedica a recordar y decidir cosas ajenas a su trabajo principal.

Definición de trabajo de [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md): Cantidad de cosas que un equipo debe conocer y mantener para hacer su trabajo.
- En [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md): Cantidad de contexto que un equipo debe mantener para operar y cambiar lo que posee.

## Por qué importa

En [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), el tema «Carga cognitiva y soporte» importa porque el tiempo de los equipos y la cola de soporte limitan la escala.

## Cómo funciona

Según [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md):

El libro Team Topologies y el documento de plataformas de la CNCF coinciden en un punto: una plataforma interna existe para reducir la carga cognitiva de los equipos que construyen producto, ofreciéndoles capacidades listas para usar en autoservicio. Tratarla como producto significa tener usuarios identificados, entender qué les cuesta y medir si lo que se ofrece lo reduce. Sin eso se vuelve un proyecto de infraestructura con su propia agenda. Una plataforma se vuelve costosa de mantener cuando ofrece mucho y se usa poco, y se vuelve inútil cuando no ofrece lo que el equipo necesita justo cuando lo necesita.

Según [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md):

El documento de la CNCF define una plataforma interna como una colección de capacidades —aprovisionamiento, canalizaciones, observabilidad, seguridad— ofrecidas a los equipos de producto con un enfoque de producto: se conocen sus necesidades, se fijan interfaces, se mide su uso y se retira lo que no sirve. Team Topologies aporta el criterio de diseño: el trabajo de los equipos de producto tiene una **carga cognitiva** limitada, y la plataforma existe para reducirla, no para sumar otra cosa que aprender. De ello se deduce que la plataforma compite con las alternativas que los equipos tienen a mano (construirlo ellos, usar un servicio externo, copiar la solución de otro equipo) y que su éxito no es lo que ofrece sino lo que los equipos eligen.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md):

El equipo de plataforma de la plataforma de entregas escribe la historia de su usuario principal: un equipo de producto que necesita un servicio nuevo en producción en un día, de forma segura. Reduce los 23 pasos a 5: una plantilla crea el repositorio, la cuenta y la red; otra, el despliegue con límites y sondas; otra, las alarmas; el equipo escribe el código y revisa un plan.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md)) son:

- **Los equipos no usan el camino** — causa: es más difícil que lo manual o no cubre su caso. Corrección: medir pasos y excepciones y mejorarlo.
- **El equipo de plataforma está saturado de solicitudes** — causa: baja adopción y servicios hechos a mano. Corrección: reducir pasos del camino y atender primero las excepciones.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Team Topologies aporta el criterio de diseño: el trabajo de los equipos de producto tiene una **carga cognitiva** limitada, y la plataforma existe para reducirla, no para sumar otra cosa que aprender. ([SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](./contextos.md), [Principal](../p/principal.md), [Trabajo](../t/trabajo.md), [Autoservicio](../a/autoservicio.md), [Camino dorado](./camino-dorado.md), [Catálogo de servicios](./catalogo-de-servicios.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.
- [SE-530 — Diseño de equipos y ownership](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md), [SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md), [SE-009](../../../classes/part-00-ingenieria-de-software-como-profesion/se-009-sostenibilidad-inclusion-y-responsabilidad-social/README.md), [SE-070](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md), [SE-106](../../../classes/part-08-entornos-herramientas-y-depuracion/se-106-ergonomia-accesibilidad-y-productividad-del-entorno/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Team Topologies](https://teamtopologies.com/) — equipos de plataforma y carga cognitiva; autoridad: sitio de los autores del libro.
- [Team Topologies, conceptos clave](https://teamtopologies.com/key-concepts) — tipos de equipo, interacción y carga cognitiva; autoridad: autores del marco.
- [CNCF Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/) — qué es una plataforma interna y qué ofrece; autoridad: CNCF TAG App Delivery.
- [DORA](https://dora.dev/) — investigación sobre desempeño de entrega de software; autoridad: programa de investigación DORA.
- [Backstage: What is Backstage?](https://backstage.io/docs/overview/what-is-backstage/) — portal de desarrollo con catálogo y plantillas; autoridad: documentación del proyecto.

---

[↑ Glosario](../../README.md) · [← Carga analítica](./carga-analitica.md) · [Carga cognitiva de un equipo →](./carga-cognitiva-de-un-equipo.md)
