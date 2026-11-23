# Safety

[↑ Glosario](../../README.md) · [← SaaS / Product Platform Engineer](./saas-product-platform-engineer.md) · [Safety-Critical Software Engineer →](./safety-critical-software-engineer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Propiedad de un sistema de no causar daño inaceptable a personas o al entorno ante fallos accidentales.

Definición de trabajo de [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md): Propiedad que excluye estados malos.

## Por qué importa

En [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), el tema «Safety y seguridad» importa porque una evita daño por fallo; la otra por ataque; comparten defensas y también chocan.

## Cómo funciona

Según [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md):

La *safety* protege a las personas y al entorno de los fallos del sistema: una ventilación que no arranca, un actuador que no se detiene. La *seguridad* (security) protege al sistema de acciones deliberadas: alguien que apaga el extractor. Comparten mecanismos (validar entradas, mínimo privilegio, actualizaciones) y a veces chocan: una actualización remota mejora la seguridad y es un riesgo de safety si puede dejar el dispositivo inservible (`SE-271`). Un análisis serio trata ambas con el mismo método: peligros, causas, defensas y comprobaciones.

Según [SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md):

Safety afirma que algo malo nunca ocurre: no ejecutar sin autorización. Liveness afirma que algo bueno eventualmente ocurre bajo supuestos: toda ejecución termina o se cancela. Probar safety no garantiza progreso; reintentar eternamente puede mantener invariantes y violar liveness.

## Ejemplo

Caso medido en la sección «Safety y seguridad» de [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md):

La *safety* protege a las personas y al entorno de los fallos del sistema: una ventilación que no arranca, un actuador que no se detiene. La *seguridad* (security) protege al sistema de acciones deliberadas: alguien que apaga el extractor. Comparten mecanismos (validar entradas, mínimo privilegio, actualizaciones) y a veces chocan: una actualización remota mejora la seguridad y es un riesgo de safety si puede dejar el dispositivo inservible (`SE-271`). Un análisis serio trata ambas con el mismo método: peligros, causas, defensas y comprobaciones.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md)) son:

- **«Tenemos tres sensores» y fallan los tres** — causa: causa común. Corrección: diversidad de principio, alimentación y software; analizar la causa común.
- **El dispositivo se reinicia en operaciones largas** — causa: plazo del temporizador demasiado corto. Corrección: fijarlo con la distribución de las operaciones y partir las largas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La *safety* protege a las personas y al entorno de los fallos del sistema: una ventilación que no arranca, un actuador que no se detiene. ([SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Daño](../d/dano.md), [Entorno](../e/entorno.md), [Estado](../e/estado.md), [Propiedad](../p/propiedad.md), [Causa común](../c/causa-comun.md), [Dominio](../d/dominio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md), [SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md), [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ETSI EN 303 645](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/) — requisitos de ciberseguridad para IoT de consumo, incluido el periodo de soporte; autoridad: ETSI.
- [NISTIR 8259A: IoT Device Cybersecurity Capability Core Baseline](https://csrc.nist.gov/pubs/ir/8259/a/final) — capacidades básicas de un dispositivo IoT; autoridad: NIST.
- [OWASP, Internet of Things Project](https://owasp.org/www-project-internet-of-things/) — riesgos frecuentes en IoT; autoridad: OWASP.
- [Hsueh, Tsai e Iyer, «Fault injection techniques and tools» (IEEE Computer, 1997)](https://doi.org/10.1109/2.585157) — inyección de fallos; autoridad: IEEE Computer.
- [Python: `datetime`](https://docs.python.org/3/library/datetime.html) — cálculo de la fecha de desbordamiento; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← SaaS / Product Platform Engineer](./saas-product-platform-engineer.md) · [Safety-Critical Software Engineer →](./safety-critical-software-engineer.md)
