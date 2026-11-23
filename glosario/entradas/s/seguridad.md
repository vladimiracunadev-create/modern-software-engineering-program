# Seguridad

[↑ Glosario](../../README.md) · [← Seguimiento de cambios](./seguimiento-de-cambios.md) · [Selección de campos →](./seleccion-de-campos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Propiedad de un sistema de resistir acciones deliberadas de personas que buscan usarlo de forma no autorizada.

Definición de trabajo de [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md).

## Por qué importa

En [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), el tema «Safety y seguridad» importa porque una evita daño por fallo; la otra por ataque; comparten defensas y también chocan.

## Cómo funciona

Según [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md):

La *safety* protege a las personas y al entorno de los fallos del sistema: una ventilación que no arranca, un actuador que no se detiene. La *seguridad* (security) protege al sistema de acciones deliberadas: alguien que apaga el extractor. Comparten mecanismos (validar entradas, mínimo privilegio, actualizaciones) y a veces chocan: una actualización remota mejora la seguridad y es un riesgo de safety si puede dejar el dispositivo inservible (`SE-271`). Un análisis serio trata ambas con el mismo método: peligros, causas, defensas y comprobaciones.

Según [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md):

Los que haga falta para llevar la probabilidad de fallo peligroso por debajo de lo que el peligro tolera, con un análisis de causa común. Una norma de seguridad funcional fija el objetivo; esta clase solo muestra el mecanismo.

## Ejemplo

Ejemplo de [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) (sección «Preguntas frecuentes»):

Los que haga falta para llevar la probabilidad de fallo peligroso por debajo de lo que el peligro tolera, con un análisis de causa común. Una norma de seguridad funcional fija el objetivo; esta clase solo muestra el mecanismo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md)) son:

- **«Tenemos tres sensores» y fallan los tres** — causa: causa común. Corrección: diversidad de principio, alimentación y software; analizar la causa común.
- **El dispositivo se reinicia en operaciones largas** — causa: plazo del temporizador demasiado corto. Corrección: fijarlo con la distribución de las operaciones y partir las largas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No es un cálculo de integridad de seguridad. ([SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Propiedad](../p/propiedad.md), [Causa común](../c/causa-comun.md), [Estado seguro](../e/estado-seguro.md), [Safety](./safety.md), [Temporizador de vigilancia](../t/temporizador-de-vigilancia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (611 clases más lo mencionan; las que más):

[SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md), [SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «security».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ETSI EN 303 645](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/) — requisitos de ciberseguridad para IoT de consumo, incluido el periodo de soporte; autoridad: ETSI.
- [NISTIR 8259A: IoT Device Cybersecurity Capability Core Baseline](https://csrc.nist.gov/pubs/ir/8259/a/final) — capacidades básicas de un dispositivo IoT; autoridad: NIST.
- [OWASP, Internet of Things Project](https://owasp.org/www-project-internet-of-things/) — riesgos frecuentes en IoT; autoridad: OWASP.
- [Hsueh, Tsai e Iyer, «Fault injection techniques and tools» (IEEE Computer, 1997)](https://doi.org/10.1109/2.585157) — inyección de fallos; autoridad: IEEE Computer.
- [Python: `datetime`](https://docs.python.org/3/library/datetime.html) — cálculo de la fecha de desbordamiento; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Seguimiento de cambios](./seguimiento-de-cambios.md) · [Selección de campos →](./seleccion-de-campos.md)
