# Excepción registrada

[↑ Glosario](../../README.md) · [← Excepción](./excepcion.md) · [Exclusión →](./exclusion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Apartamiento deliberado del camino, con su motivo, dueño y fecha de revisión.

Definición de trabajo de [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md).

## Por qué importa

La clase donde se define, [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), existe con este propósito: la clase existe para que puedas tratar la infraestructura como un producto con usuarios: los equipos que despliegan servicios.

## Cómo funciona

Según [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md):

Limita las decisiones que no aportan, y deja libres las que sí. Si un equipo debe apartarse, puede hacerlo con una excepción registrada. Si el camino se convierte en obligación sin salida, deja de ser una oferta y se vuelve un cuello de botella.

## Ejemplo

Ejemplo de [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) (sección «Preguntas frecuentes»):

Limita las decisiones que no aportan, y deja libres las que sí. Si un equipo debe apartarse, puede hacerlo con una excepción registrada. Si el camino se convierte en obligación sin salida, deja de ser una oferta y se vuelve un cuello de botella.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md)) son:

- **Los equipos no usan el camino** — causa: es más difícil que lo manual o no cubre su caso. Corrección: medir pasos y excepciones y mejorarlo.
- **El equipo de plataforma está saturado de solicitudes** — causa: baja adopción y servicios hechos a mano. Corrección: reducir pasos del camino y atender primero las excepciones.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md)) son: Las definiciones son operativas para la plataforma de entregas. Cada autor y cada herramienta usan estos términos con matices y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna persona ni plataforma: los pasos, las tasas de error, los tiempos, las solicitudes y los descriptores son supuestos del autor, y el verificador se evaluó con los defectos que yo mismo escribí. La siguiente clase pone todo a prueba en un taller: desplegar y destruir un entorno de forma segura.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Fecha de revisión](../f/fecha-de-revision.md), [Revisión](../r/revision.md), [Camino dorado](../c/camino-dorado.md), [Carga cognitiva](../c/carga-cognitiva.md), [Plataforma interna](../p/plataforma-interna.md), [Política como código](../p/politica-como-codigo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md).

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

[↑ Glosario](../../README.md) · [← Excepción](./excepcion.md) · [Exclusión →](./exclusion.md)
