# Gemelo simulado

[↑ Glosario](../../README.md) · [← Gateway](./gateway.md) · [Generación →](./generacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Modelo ejecutable de un dispositivo o una flota usado para comparar decisiones sin hardware.

Definición de trabajo de [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md).

## Por qué importa

La clase donde se define, [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), existe con este propósito: el proyecto entrega un dispositivo simulado que se puede operar y actualizar: un paquete que reúne identidad, versiones, reversión, reintentos, despliegue por etapas, umbrales y un responsable, un validador que dice qué cubre y qué no, y una simulación de un mes y de una flota que muestra qué aporta cada defensa.

## Cómo funciona

[SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md):

El equipo de la plataforma entrega el paquete de los 200 nodos con nueve secciones. La identidad es una clave derivada por dispositivo desde un secreto maestro que nunca está en el nodo. El firmware tiene dos ranuras con reversión a los 60 s. Las claves se rotan cada doce meses con una lista de revocación. Los umbrales son de 5 a 40 °C con variación máxima de 3 °C por muestra y una referencia independiente de CO₂.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md)) son:

- **El paquete pasa el validador y falla en la flota** — causa: validador de forma sin reglas de sentido. Corrección: añadir reglas de sentido y una revisión humana.
- **Nadie sabe qué hacer ante un nodo mudo** — causa: sin procedimiento operativo. Corrección: escribir los procedimientos de los incidentes frecuentes.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se simuló ningún componente real ni se actualizó un dispositivo: las probabilidades de cuelgue, de corte y de fallo, el informe y la reparación del 90 % y las 200 mutaciones son construcciones del autor, y el validador se afinó con los mismos casos que lo evalúan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dispositivo](../d/dispositivo.md), [Modelo](../m/modelo.md), [Operabilidad](../o/operabilidad.md), [Paquete del dispositivo](../p/paquete-del-dispositivo.md), [Reversión automática](../r/reversion-automatica.md), [Validador de forma](../v/validador-de-forma.md).
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

[↑ Glosario](../../README.md) · [← Gateway](./gateway.md) · [Generación →](./generacion.md)
