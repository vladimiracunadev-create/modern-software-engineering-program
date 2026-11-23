# Estado seguro

[↑ Glosario](../../README.md) · [← Estado local, compartido y persistente](./estado-local-compartido-y-persistente.md) · [Estado vacío →](./estado-vacio.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Estado en que un sistema con un fallo causa el menor daño posible, definido de antemano.

Definición de trabajo de [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md).

## Por qué importa

En [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), el tema «Estado seguro» importa porque cada fallo debe llevar a un estado de menor daño definido de antemano.

## Cómo funciona

Según [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), en la sección «Estado seguro»:

Un fallo detectado debe llevar a un estado definido de antemano cuyo daño sea menor: el extractor encendido si no se sabe el nivel de CO₂, la puerta desbloqueada o bloqueada según el riesgo, el actuador parado. El estado seguro no siempre es «apagado». Se decide por peligro y se documenta, porque quien programa bajo presión elige el estado que facilita probar. Y debe probarse: forzar el fallo (`SE-275`) y comprobar que se alcanza.

## Ejemplo

Ejemplo de [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma escribe el análisis de peligros del nodo con cuatro filas. Peligro: el extractor no arranca con CO₂ alto. Defensa: dos sensores de principios distintos con comparación, estado seguro «extractor encendido» si discrepan, y prueba por inyección de fallos. Peligro: el firmware se cuelga. Defensa: temporizador de vigilancia con plazo de 5 s, alimentado solo tras una comprobación de salud, y operaciones largas partidas en pasos de 200 ms. Peligro: un contador de tiempo da la vuelta. Defensa: toda comparación de tiempos usa resta sin signo, y una prueba simula el arranque a 49 días. Peligro: un atacante apaga el extractor.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md)) son:

- **«Tenemos tres sensores» y fallan los tres** — causa: causa común. Corrección: diversidad de principio, alimentación y software; analizar la causa común.
- **El dispositivo se reinicia en operaciones largas** — causa: plazo del temporizador demasiado corto. Corrección: fijarlo con la distribución de las operaciones y partir las largas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún sensor, temporizador ni microcontrolador y no se hizo ningún análisis de seguridad funcional: las probabilidades, los tiempos lognormales y los contadores son construcciones del autor. La siguiente clase convierte estos peligros en un taller de modelado de fallos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Daño](../d/dano.md), [Estado](./estado.md), [Causa común](../c/causa-comun.md), [Safety](../s/safety.md), [Seguridad](../s/seguridad.md), [Temporizador de vigilancia](../t/temporizador-de-vigilancia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md), [SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md).

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

[↑ Glosario](../../README.md) · [← Estado local, compartido y persistente](./estado-local-compartido-y-persistente.md) · [Estado vacío →](./estado-vacio.md)
