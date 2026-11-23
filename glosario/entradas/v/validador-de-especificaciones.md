# Validador de especificaciones

[↑ Glosario](../../README.md) · [← Validación por capas](./validacion-por-capas.md) · [Validador de estructura →](./validador-de-estructura.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Programa que comprueba la forma y el contenido de una especificación antes de ejecutarla.

Definición de trabajo de [SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md).

## Por qué importa

La clase donde se define, [SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md), existe con este propósito: la clase existe para que reúnas la [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md) en un **programa de experimentos con evidencia**: un catálogo de fallas, especificaciones de experimento validadas, resultados con control y huella reproducible, y una declaración de lo que nada de eso demuestra.

## Cómo funciona

[SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el cliente de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md):

Supón, como caso hipotético y no como medición, que el equipo entrega su paquete y lo revisa otra persona del equipo vecino. Encuentra que una especificación usa una métrica que se emite con otro nombre, que una ventana cae en la semana de evaluaciones de una universidad cliente y que la política no dice quién activa el interruptor general un domingo. Ninguna de las tres la ve el validador, y las tres entran en `limites.md` como clases de error de revisión humana.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md)) son:

- **El experimento confirma siempre** — causa: la métrica no se mueve con la falla. Corrección: comprobar que la señal responde a una falla conocida.
- **El aborto nunca se activa** — causa: umbral más laxo que el estado estable o métrica ciega. Corrección: validar el umbral relativo y la existencia de la métrica.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md)) son: Las definiciones son operativas para el cliente de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas. Se ejecutaron dos experimentos con semilla fija y tiempo virtual en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md), [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contenido de una especificación](../c/contenido-de-una-especificacion.md), [Especificación](../e/especificacion.md), [Especificación del experimento](../e/especificacion-del-experimento.md), [Huella](../h/huella.md), [Informe de límites](../i/informe-de-limites.md), [Mutación](../m/mutacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

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

[↑ Glosario](../../README.md) · [← Validación por capas](./validacion-por-capas.md) · [Validador de estructura →](./validador-de-estructura.md)
