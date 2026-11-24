# Estado seguro

[↑ Glosario](../../README.md) · [← Estado local, compartido y persistente](./estado-local-compartido-y-persistente.md) · [Estado vacío →](./estado-vacio.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Un **estado seguro** (*safe state*) es aquel en que un sistema con un fallo causa el menor daño posible, y que se define de antemano. Es el sentido de [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) (safety, seguridad y vida útil prolongada). El adjetivo no significa «seguro» en el sentido de ciberseguridad: se refiere a seguridad funcional (*safety*), es decir, a no causar daño a personas o al entorno cuando algo falla.

## Por qué importa

Un fallo detectado debe llevar a un lugar conocido, no a un comportamiento improvisado. [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) advierte la razón: quien programa bajo presión elige el estado que facilita probar, no el que minimiza el daño. Definirlo de antemano, por peligro, lo convierte en una decisión de diseño revisable.

## Cómo funciona

El mecanismo, según [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md):

1. **Identificar el peligro** (qué daño puede ocurrir).
2. **Definir el estado de menor daño** para ese peligro: el extractor encendido si no se sabe el nivel de CO₂, la puerta desbloqueada o bloqueada según el riesgo, el actuador parado. El estado seguro **no siempre es «apagado»**: depende del peligro.
3. **Documentarlo.**
4. **Probarlo:** forzar el fallo ([SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), inyección de fallos) y comprobar que se alcanza.

Se combina con detección de fallos (sensores diversos con comparación, temporizador de vigilancia) y con un análisis de peligros por escrito.

## Ejemplo

El análisis de peligros del nodo de [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) tiene cuatro filas. Primera: el extractor no arranca con CO₂ alto; defensa: dos sensores de principios distintos con comparación, estado seguro «extractor encendido» si discrepan, y prueba por inyección de fallos. Segunda: el firmware se cuelga; defensa: temporizador de vigilancia con plazo de 5 s, alimentado solo tras una comprobación de salud. Tercera: un contador de tiempo da la vuelta; defensa: restas sin signo y una prueba que simula el arranque a 49 días. Cuarta: un atacante apaga el extractor.

## Errores y confusiones comunes

- **Equiparar estado seguro con «apagado».** Apagar un extractor con CO₂ alto es el peligro.
- **Elegir el estado que facilita probar** en vez del que reduce el daño.
- **No probar el camino al estado seguro:** un estado seguro nunca alcanzado en pruebas es una suposición.
- **Confundirlo con seguridad informática,** que protege contra atacantes (aunque el cuarto peligro de la clase une ambas).

## Límites y cuándo no aplica

No existe un estado seguro único válido siempre: algunos sistemas (un avión en vuelo) no pueden «parar». El análisis se limita a los peligros identificados. Los números de [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) son un caso didáctico del nodo ambiental, no una certificación de seguridad funcional.

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
