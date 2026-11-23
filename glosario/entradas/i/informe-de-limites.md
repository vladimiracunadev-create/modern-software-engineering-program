# Informe de límites

[↑ Glosario](../../README.md) · [← Informe de entrega](./informe-de-entrega.md) · [Informe y decisión →](./informe-y-decision.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Apartado que declara lo que se hizo, lo que no y lo que ningún validador detecta.

Definición de trabajo de [SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-588 — Proyecto: harness mínimo gobernado y evaluado](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md): Declaración de lo no probado, lo no cubierto y lo no medido.

## Por qué importa

En [SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md), el tema «Informe de límites» importa porque decir qué no se probó es parte de la evidencia.

## Cómo funciona

[SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el cliente de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md):

Supón, como caso hipotético y no como medición, que el equipo entrega su paquete y lo revisa otra persona del equipo vecino. Encuentra que una especificación usa una métrica que se emite con otro nombre, que una ventana cae en la semana de evaluaciones de una universidad cliente y que la política no dice quién activa el interruptor general un domingo. Ninguna de las tres la ve el validador, y las tres entran en `limites.md` como clases de error de revisión humana.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El paquete no lo entiende nadie más** — causa: falta el informe de límites y el catálogo. Corrección: revisión por otra persona sin ayuda. ([SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md)) son: Las definiciones son operativas para el cliente de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas. Se ejecutaron dos experimentos con semilla fija y tiempo virtual en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md), [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contención](../c/contencion.md), [Escalada](../e/escalada.md), [Escenario adverso](../e/escenario-adverso.md), [Especificación del experimento](../e/especificacion-del-experimento.md), [Harness gobernado](../h/harness-gobernado.md), [Huella](../h/huella.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.
- [SE-588 — Proyecto: harness mínimo gobernado y evaluado](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Principles of Chaos Engineering](https://principlesofchaos.org/) — método en cuatro pasos y experimentos continuos; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Netflix: ChAP: Chaos Automation Platform](https://netflixtechblog.com/chap-chaos-automation-platform-53e6d528371f) — programa automatizado con control, experimento e interruptor; autoridad: blog de ingeniería de Netflix.
- [AWS Fault Injection Service: experiment templates](https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html) — acciones, objetivos y condiciones de parada de una plantilla; autoridad: documentación de Amazon Web Services.
- [Basiri et al., Chaos Engineering](https://arxiv.org/abs/1702.05843) — principios y enfoque de experimentación; autoridad: IEEE Software 33(3), 2016.
- [Google SRE: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — repetibilidad de las pruebas; autoridad: libro de ingeniería de confiabilidad de Google.

---

[↑ Glosario](../../README.md) · [← Informe de entrega](./informe-de-entrega.md) · [Informe y decisión →](./informe-y-decision.md)
