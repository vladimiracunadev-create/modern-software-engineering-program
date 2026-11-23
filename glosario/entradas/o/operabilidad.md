# Operabilidad

[↑ Glosario](../../README.md) · [← OpenAPI](./openapi.md) · [Operación →](./operacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Capacidad de un dispositivo de ser mantenido durante su vida útil por personas que no lo construyeron.

Definición de trabajo de [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md).

## Por qué importa

En [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), el tema «Operabilidad» importa porque un dispositivo operable tolera cortes, cuelgues y actualizaciones sin visita.

## Cómo funciona

Según [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), en la sección «Operabilidad»:

Un dispositivo es operable si una persona que no lo construyó puede mantenerlo vivo durante años: sabe cómo se actualiza, qué pasa cuando falla, cómo se retira una clave y cómo se detecta que dejó de enviar. Operabilidad es el conjunto de las defensas de la parte vistas desde quien las usa. Sin ella, cada incidente exige a quien lo construyó.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md):

El equipo de la plataforma entrega el paquete de los 200 nodos con nueve secciones. La identidad es una clave derivada por dispositivo desde un secreto maestro que nunca está en el nodo. El firmware tiene dos ranuras con reversión a los 60 s. Las claves se rotan cada doce meses con una lista de revocación. Los umbrales son de 5 a 40 °C con variación máxima de 3 °C por muestra y una referencia independiente de CO₂.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md)) son:

- **El paquete pasa el validador y falla en la flota** — causa: validador de forma sin reglas de sentido. Corrección: añadir reglas de sentido y una revisión humana.
- **Nadie sabe qué hacer ante un nodo mudo** — causa: sin procedimiento operativo. Corrección: escribir los procedimientos de los incidentes frecuentes.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se simuló ningún componente real ni se actualizó un dispositivo: las probabilidades de cuelgue, de corte y de fallo, el informe y la reparación del 90 % y las 200 mutaciones son construcciones del autor, y el validador se afinó con los mismos casos que lo evalúan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Dispositivo](../d/dispositivo.md), [Gemelo simulado](../g/gemelo-simulado.md), [Paquete del dispositivo](../p/paquete-del-dispositivo.md), [Reversión automática](../r/reversion-automatica.md), [Validador de forma](../v/validador-de-forma.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-276 — Proyecto: dispositivo simulado operable y actualizable](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-228](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md), [SE-173](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md), [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), [SE-258](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md).

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

[↑ Glosario](../../README.md) · [← OpenAPI](./openapi.md) · [Operación →](./operacion.md)
