# Temporizador de vigilancia

[↑ Glosario](../../README.md) · [← Template Method](./template-method.md) · [Tenant →](./tenant.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Un **temporizador de vigilancia** (*watchdog*) es un temporizador que reinicia el sistema si el firmware no lo reinicia periódicamente. Es el sentido de [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) (safety, seguridad y vida útil prolongada). El firmware «lo alimenta» (reinicia su cuenta) mientras funciona; si deja de hacerlo, el temporizador vence y fuerza un reinicio.

## Por qué importa

Recupera de cuelgues y de bucles infinitos sin intervención humana, algo esencial en dispositivos desplegados sin acceso. A cambio, su plazo es un intercambio de riesgos: corto, recupera rápido pero reinicia sin motivo durante operaciones largas legítimas; largo, casi no se equivoca y deja al dispositivo colgado mucho tiempo.

## Cómo funciona

[SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) da dos reglas de diseño:

1. **El plazo se fija con la distribución del tiempo de las operaciones más largas,** no con la intuición.
2. **La alimentación se hace solo cuando varias comprobaciones de salud pasan,** no desde una interrupción que sigue viva aunque el programa principal esté colgado.

La segunda regla es la que más se incumple: si una interrupción de temporizador alimenta el watchdog automáticamente, el sistema puede estar colgado y el watchdog nunca vencer. La alimentación debe depender de pruebas de que las tareas importantes avanzaron.

Se combina con el **estado seguro**: qué hace el dispositivo mientras reinicia y al arrancar.

## Ejemplo

El análisis de peligros del nodo en [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) incluye: peligro, el firmware se cuelga; defensa, temporizador de vigilancia con plazo de 5 s, alimentado solo tras una comprobación de salud, y operaciones largas partidas en pasos de 200 ms. Así, una operación legítima nunca excede el plazo, y un bucle infinito lo vence en 5 segundos. Los otros peligros de la misma tabla (un contador que da la vuelta, un atacante que apaga el extractor) se tratan con otras defensas.

## Errores y confusiones comunes

- **Alimentarlo desde una interrupción,** que hace que nunca venza ante un cuelgue del bucle principal.
- **Plazo corto que reinicia durante operaciones largas legítimas.**
- **Usarlo como sustituto de corregir el defecto:** reiniciar oculta el síntoma.
- **No registrar los reinicios:** pierde la señal de que algo falla.

## Límites y cuándo no aplica

No arregla fallos que sobreviven al reinicio (datos corruptos, hardware dañado). Un reinicio puede ser peligroso en el estado físico del sistema (un actuador a mitad de movimiento), por eso el estado seguro debe estar definido. Los plazos de la clase son los de un nodo ambiental simulado.

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
