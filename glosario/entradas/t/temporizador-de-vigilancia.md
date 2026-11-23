# Temporizador de vigilancia

[↑ Glosario](../../README.md) · [← Template Method](./template-method.md) · [Tenant →](./tenant.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Temporizador que reinicia el sistema si el firmware no lo reinicia periódicamente.

Definición de trabajo de [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md).

## Por qué importa

En [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), el tema «Temporizador de vigilancia» importa porque recupera de cuelgues a cambio de reinicios falsos si el plazo es corto.

## Cómo funciona

Según [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), en la sección «Temporizador de vigilancia»:

Un temporizador de vigilancia (watchdog) reinicia el dispositivo si el firmware no lo «alimenta» a tiempo. Recupera de cuelgues y de bucles infinitos. Su plazo es un intercambio: corto, recupera rápido y reinicia sin motivo durante operaciones largas legítimas; largo, casi no se equivoca y deja al dispositivo colgado mucho tiempo. Por eso se fija con la distribución del tiempo de las operaciones más largas y no con la intuición, y la alimentación se hace solo cuando varias comprobaciones de salud pasan, no desde una interrupción que sigue viva aunque el programa principal esté colgado.

## Ejemplo

Ejemplo de [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma escribe el análisis de peligros del nodo con cuatro filas. Peligro: el extractor no arranca con CO₂ alto. Defensa: dos sensores de principios distintos con comparación, estado seguro «extractor encendido» si discrepan, y prueba por inyección de fallos. Peligro: el firmware se cuelga. Defensa: temporizador de vigilancia con plazo de 5 s, alimentado solo tras una comprobación de salud, y operaciones largas partidas en pasos de 200 ms. Peligro: un contador de tiempo da la vuelta. Defensa: toda comparación de tiempos usa resta sin signo, y una prueba simula el arranque a 49 días. Peligro: un atacante apaga el extractor.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md)) son:

- **«Tenemos tres sensores» y fallan los tres** — causa: causa común. Corrección: diversidad de principio, alimentación y software; analizar la causa común.
- **El dispositivo se reinicia en operaciones largas** — causa: plazo del temporizador demasiado corto. Corrección: fijarlo con la distribución de las operaciones y partir las largas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un temporizador de vigilancia (watchdog) reinicia el dispositivo si el firmware no lo «alimenta» a tiempo. ([SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Firmware](../f/firmware.md), [Causa común](../c/causa-comun.md), [Estado seguro](../e/estado-seguro.md), [Safety](../s/safety.md), [Seguridad](../s/seguridad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «watchdog».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ETSI EN 303 645](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/) — requisitos de ciberseguridad para IoT de consumo, incluido el periodo de soporte; autoridad: ETSI.
- [NISTIR 8259A: IoT Device Cybersecurity Capability Core Baseline](https://csrc.nist.gov/pubs/ir/8259/a/final) — capacidades básicas de un dispositivo IoT; autoridad: NIST.
- [OWASP, Internet of Things Project](https://owasp.org/www-project-internet-of-things/) — riesgos frecuentes en IoT; autoridad: OWASP.
- [Hsueh, Tsai e Iyer, «Fault injection techniques and tools» (IEEE Computer, 1997)](https://doi.org/10.1109/2.585157) — inyección de fallos; autoridad: IEEE Computer.
- [Python: `datetime`](https://docs.python.org/3/library/datetime.html) — cálculo de la fecha de desbordamiento; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Template Method](./template-method.md) · [Tenant →](./tenant.md)
