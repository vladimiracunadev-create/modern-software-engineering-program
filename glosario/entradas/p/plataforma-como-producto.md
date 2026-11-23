# Plataforma como producto

[↑ Glosario](../../README.md) · [← Plataforma](./plataforma.md) · [Plataforma de datos gobernada →](./plataforma-de-datos-gobernada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

El libro Team Topologies y el documento de plataformas de la CNCF coinciden en un punto: una plataforma interna existe para reducir la carga cognitiva de los equipos que construyen producto, ofreciéndoles capacidades listas para usar en autoservicio. Tratarla como producto significa tener usuarios identificados, entender qué les cuesta y medir si lo que se ofrece lo reduce. Sin eso se vuelve un proyecto de infraestructura con su propia agenda.

Explicación de la sección «Plataforma como producto» de [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md).

## Por qué importa

En [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), el tema «Plataforma como producto» importa porque tiene usuarios, una oferta y una medida de valor.

En [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), el tema «Plataforma como producto» importa porque obliga a pensar en personas usuarias, adopción y retirada, no solo en construir.

## Cómo funciona

Según [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), en la sección «Plataforma como producto»:

El libro Team Topologies y el documento de plataformas de la CNCF coinciden en un punto: una plataforma interna existe para reducir la carga cognitiva de los equipos que construyen producto, ofreciéndoles capacidades listas para usar en autoservicio. Tratarla como producto significa tener usuarios identificados, entender qué les cuesta y medir si lo que se ofrece lo reduce. Sin eso se vuelve un proyecto de infraestructura con su propia agenda. Una plataforma se vuelve costosa de mantener cuando ofrece mucho y se usa poco, y se vuelve inútil cuando no ofrece lo que el equipo necesita justo cuando lo necesita.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md):

El equipo de plataforma de la plataforma de entregas escribe la historia de su usuario principal: un equipo de producto que necesita un servicio nuevo en producción en un día, de forma segura. Reduce los 23 pasos a 5: una plantilla crea el repositorio, la cuenta y la red; otra, el despliegue con límites y sondas; otra, las alarmas; el equipo escribe el código y revisa un plan.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md)) son:

- **Los equipos no usan el camino** — causa: es más difícil que lo manual o no cubre su caso. Corrección: medir pasos y excepciones y mejorarlo.
- **El equipo de plataforma está saturado de solicitudes** — causa: baja adopción y servicios hechos a mano. Corrección: reducir pasos del camino y atender primero las excepciones.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md)) son: Las definiciones son operativas para la plataforma de entregas. Cada autor y cada herramienta usan estos términos con matices y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna persona ni plataforma: los pasos, las tasas de error, los tiempos, las solicitudes y los descriptores son supuestos del autor, y el verificador se evaluó con los defectos que yo mismo escribí. La siguiente clase pone todo a prueba en un taller: desplegar y destruir un entorno de forma segura.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Autoservicio](../a/autoservicio.md), [Camino dorado](../c/camino-dorado.md), [Carga cognitiva](../c/carga-cognitiva.md), [Catálogo de servicios](../c/catalogo-de-servicios.md), [Excepción registrada](../e/excepcion-registrada.md), [Plataforma interna](./plataforma-interna.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

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

[↑ Glosario](../../README.md) · [← Plataforma](./plataforma.md) · [Plataforma de datos gobernada →](./plataforma-de-datos-gobernada.md)
