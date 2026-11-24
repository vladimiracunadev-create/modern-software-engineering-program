# Paquete del dispositivo

[↑ Glosario](../../README.md) · [← Paquete de migración](./paquete-de-migracion.md) · [Paquete diagnóstico →](./paquete-diagnostico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

El **paquete del dispositivo** es un documento que reúne las decisiones de identidad, versiones, reversión, claves, umbrales, reintentos, despliegue, vigilancia, responsabilidad y revisión de un dispositivo. Es el artefacto de [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md) (proyecto: dispositivo simulado operable y actualizable). No es un paquete de software ni un instalador: es la documentación de decisiones que hace revisable al dispositivo.

## Por qué importa

Reúne decisiones dispersas en un lugar revisable. En un dispositivo que vivirá años, esas decisiones se toman en clases, piezas de código y conversaciones distintas; si no se reúnen, nadie ve el conjunto ni detecta las que se contradicen. [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md) precisa que no sustituye al código: lo hace revisable.

## Cómo funciona

El paquete tiene **nueve secciones**, que responden:

1. Cómo se **identifica** el dispositivo.
2. Qué **versión** corre y cómo **vuelve atrás**.
3. Cómo **rota sus claves**.
4. Qué **umbrales** usa.
5. Cómo **reintenta**.
6. Cómo se **despliega** una versión.
7. Cuál es el plazo de su **temporizador de vigilancia**.
8. **Quién responde** por él.
9. **Cuándo se revisa.**

La clase lo apoya en dos fuentes: NISTIR 8259A, que enumera capacidades que un dispositivo debe ofrecer, y los registros breves de decisión de Nygard. Tiene un **validador** que comprueba la forma, y una **simulación** que prueba que las decisiones funcionan juntas.

## Ejemplo

El nodo ambiental de una sala de estudio cierra en [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md) su caso conductor de la [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md). El proyecto deja el duodécimo artefacto: el paquete del dispositivo operable y actualizable, con su validador, su simulación y sus límites, que reúne los once anteriores. Cambiar una sola decisión, el tamaño de la primera etapa del despliegue, muestra qué fallos dejan de detectarse.

## Errores y confusiones comunes

- **Un paquete que pasa el validador y falla en la flota:** el validador comprueba forma; hacen falta reglas de sentido y revisión humana ([SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md)).
- **Escribirlo una vez y no revisarlo:** la novena sección existe por eso.
- **Tratarlo como sustituto del código o de las pruebas.**
- **Confundirlo con la operabilidad:** esta es la propiedad; el paquete es el documento que la hace revisable.

## Límites y cuándo no aplica

Es un documento sobre un dispositivo *simulado*: no demuestra que un dispositivo físico cumpla lo escrito. Para productos sin dispositivos desplegables a largo plazo, algunas secciones pierden sentido. Su valor depende de que lo escrito se mantenga al día con el código.

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
