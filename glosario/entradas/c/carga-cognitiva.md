# Carga cognitiva

[↑ Glosario](../../README.md) · [← Carga analítica](./carga-analitica.md) · [Carga cognitiva de un equipo →](./carga-cognitiva-de-un-equipo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

La **carga cognitiva** es el esfuerzo mental que un equipo dedica a recordar y decidir cosas ajenas a su trabajo principal ([SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md)). [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) la formula como la cantidad de cosas que un equipo debe conocer y mantener para hacer su trabajo, y [SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md) como la cantidad de contexto que debe mantener para operar y cambiar lo que posee. El programa la toma de *Team Topologies*.

## Por qué importa

La capacidad de un equipo es finita. Cada herramienta de despliegue, política de seguridad o convención de infraestructura que debe recordar compite con el producto. La decisión profesional que cambia es qué se ofrece a los equipos: una plataforma interna se justifica si **reduce** esa carga, y no por lo mucho que ofrece. [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) lo dice así: la plataforma existe para reducirla, no para sumar otra cosa que aprender.

## Cómo funciona

El trabajo de un equipo de producto tiene una carga cognitiva limitada; lo que excede ese límite se hace peor o se olvida. La respuesta que enseña el programa es mover capacidades repetidas (aprovisionamiento, canalizaciones, observabilidad, seguridad) a una plataforma ofrecida en autoservicio, con enfoque de producto: usuarios identificados, necesidades entendidas, interfaces fijadas, uso medido y retiro de lo que no sirve (documento de plataformas de la CNCF, que [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) cita).

De ahí se deduce algo contraintuitivo: la plataforma compite con las alternativas que los equipos tienen a mano (construirlo ellos, usar un servicio externo, copiar la solución de otro equipo), y su éxito se mide por lo que los equipos **eligen**, no por lo que ofrece. Se vuelve costosa cuando ofrece mucho y se usa poco, e inútil cuando no ofrece lo necesario en el momento justo ([SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md)).

[SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md) aplica la idea al tamaño de lo que un equipo posee: si debe mantener demasiado contexto para operar y cambiar sus sistemas, la propiedad está mal dimensionada.

## Ejemplo

Un equipo debe crear un servicio nuevo y recordar límites de recursos, usuario sin privilegios, etiqueta de dueño y sondas de salud. Con un camino dorado, esas guardas vienen incorporadas y el equipo solo piensa en su lógica. La carga baja porque deja de recordar lo que la plataforma ya hace. Ilustración de [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md).

## Errores y confusiones comunes

- **Los equipos no usan el camino**: es más difícil que lo manual o no cubre su caso; se corrige midiendo pasos y excepciones.
- **Plataforma saturada de solicitudes**: baja adopción y servicios hechos a mano; reducir pasos y atender primero las excepciones.
- **Medir la plataforma por funciones ofrecidas** en vez de por reducción real de esfuerzo.
- **Confundirla con carga de trabajo**: el número de tareas no es lo mismo que cuánto contexto hay que sostener a la vez.

## Límites y cuándo no aplica

El programa no da una unidad ni una medida estándar de carga cognitiva: es un criterio de diseño, no una métrica con umbral. Se estima con proxies (pasos, excepciones, tiempo de arranque) que hay que elegir y justificar. No sustituye la conversación con los equipos sobre qué les cuesta.

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
