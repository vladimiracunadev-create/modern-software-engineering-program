# Paquete del dispositivo

[↑ Glosario](../../README.md) · [← Paquete de migración](./paquete-de-migracion.md) · [Paquete diagnóstico →](./paquete-diagnostico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Documento que reúne las decisiones de identidad, versiones, reversión, claves, umbrales, reintentos, despliegue, vigilancia, responsabilidad y revisión de un dispositivo.

Definición de trabajo de [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md).

## Por qué importa

En [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), el tema «Paquete del dispositivo» importa porque reúne decisiones dispersas en un lugar revisable.

## Cómo funciona

Según [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), en la sección «Paquete del dispositivo»:

El paquete es un documento que dice, en nueve secciones, cómo se identifica el dispositivo, qué versión corre y cómo vuelve atrás, cómo rota sus claves, qué umbrales usa, cómo reintenta, cómo se despliega una versión, cuál es el plazo de su temporizador de vigilancia, quién responde por él y cuándo se revisa. No sustituye al código: lo hace revisable. Sigue el espíritu de NISTIR 8259A, que enumera capacidades que un dispositivo debe ofrecer, y de los registros breves de decisión de Nygard.

## Ejemplo

Ejemplo de [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md) (sección «Caso conductor»):

El nodo ambiental de una sala de estudio cierra aquí su caso conductor de la [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md). El proyecto deja el duodécimo artefacto: el paquete del dispositivo operable y actualizable, con su validador, su simulación y sus límites, que reúne los once anteriores. La [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md) deja el dispositivo y pasa a los dominios especializados, empezando por el software científico y la reproducibilidad. Cambia después una sola decisión, el tamaño de la primera etapa, y observa qué fallos dejan de detectarse.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md)) son:

- **El paquete pasa el validador y falla en la flota** — causa: validador de forma sin reglas de sentido. Corrección: añadir reglas de sentido y una revisión humana.
- **Nadie sabe qué hacer ante un nodo mudo** — causa: sin procedimiento operativo. Corrección: escribir los procedimientos de los incidentes frecuentes.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se simuló ningún componente real ni se actualizó un dispositivo: las probabilidades de cuelgue, de corte y de fallo, el informe y la reparación del 90 % y las 200 mutaciones son construcciones del autor, y el validador se afinó con los mismos casos que lo evalúan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dispositivo](../d/dispositivo.md), [Documento](../d/documento.md), [Reintentos](../r/reintentos.md), [Responsabilidad](../r/responsabilidad.md), [Gemelo simulado](../g/gemelo-simulado.md), [Operabilidad](../o/operabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Moran et al., RFC 9019: A Firmware Update Architecture for Internet of Things](https://www.rfc-editor.org/rfc/rfc9019) — requisitos de una arquitectura de actualización; autoridad: IETF.
- [NISTIR 8259A: IoT Device Cybersecurity Capability Core Baseline](https://csrc.nist.gov/pubs/ir/8259/a/final) — capacidades de un dispositivo IoT; autoridad: NIST.
- [ETSI EN 303 645](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/) — requisitos básicos de ciberseguridad para IoT de consumo; autoridad: ETSI.
- [Nygard, «Documenting architecture decisions» (2011)](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — registros breves de decisiones; autoridad: autor de la práctica.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Paquete de migración](./paquete-de-migracion.md) · [Paquete diagnóstico →](./paquete-diagnostico.md)
