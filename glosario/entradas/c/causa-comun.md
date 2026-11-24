# Causa común

[↑ Glosario](../../README.md) · [← Catálogo de servicios](./catalogo-de-servicios.md) · [Causa y evidencia →](./causa-y-evidencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Una **causa común** es un solo evento o condición que degrada varios canales que se suponían independientes. El programa lo usa con el mismo núcleo en varias clases: [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) (riesgo y seguridad funcional) la presenta como lo que rompe el producto de probabilidades; [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), como origen único de fallos de varios componentes redundantes; [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), como evento único que provoca el fallo simultáneo; [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), como fallo por algo compartido (despliegue, configuración, dependencia); [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md), como origen compartido que hace que los fallos dejen de ser independientes.

## Por qué importa

La redundancia solo ayuda si los canales fallan por separado. Si dos réplicas comparten fuente de energía, versión de software o configuración, su probabilidad conjunta de fallar no es el producto de las individuales. [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md) dice que la causa común limita lo que gana la redundancia. Cambia la decisión de diseño: en lugar de añadir una réplica más, se pregunta qué comparten las existentes.

## Cómo funciona

Si dos canales fallan cada uno con probabilidad *p* de forma independiente, ambos fallan con *p²*. Con causa común, una fracción de los fallos afecta a los dos a la vez y esa fracción domina. [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md) lo modela con el parámetro β, la fracción de causa común. Con λ = 2 × 10⁻⁶ por hora, intervalo de prueba de un año y β = 0,05, el laboratorio da 8,76 × 10⁻³ para 1oo1, 5,30 × 10⁻⁴ para 1oo2 y 7,15 × 10⁻⁴ para 2oo3. Con pruebas cada cinco años: 4,38 × 10⁻², 4,50 × 10⁻³ y 9,12 × 10⁻³. Notación: «1oo2» son dos canales donde basta uno para cortar; «2oo3», tres donde cortan si dos coinciden.

[SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) indica buscar al menos una causa común al construir un árbol de fallos; [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) propone diversidad de principio, de alimentación y de software; [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md) y [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), enumerar lo que comparten las réplicas y aislarlo.

## Ejemplo

[SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md): «tenemos tres sensores» y fallan los tres, porque compartían principio de medida o alimentación. [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md): el sistema cae más de lo que da la cuenta porque las capas comparten algo. Ilustración propia: dos servidores en zonas distintas, pero ambos con el mismo despliegue defectuoso, fallan juntos.

## Errores y confusiones comunes

- **Multiplicar probabilidades de componentes sin verificar independencia.**
- **Contar réplicas como protección cuando comparten dependencia** ([SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md)).
- **Confundirla con falla en cascada:** la cascada propaga de un componente a otro; la causa común afecta a varios simultáneamente por un origen compartido.

## Límites y cuándo no aplica

El valor de β es una estimación, no una constante medible fácilmente; los números de [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md) son un laboratorio con parámetros elegidos, no datos de un sistema. Y el análisis solo encuentra las causas comunes que alguien se pregunta; una no imaginada sigue ahí. Si los canales son realmente diversos y aislados, el modelo independiente es una aproximación razonable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa](./capa.md), [Componente](./componente.md), [Condición](./condicion.md), [Dependencia](../d/dependencia.md), [Espacio de nombres](../e/espacio-de-nombres.md), [Estado seguro](../e/estado-seguro.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-274 — Safety, seguridad y vida útil prolongada](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.
- [SE-446 — IEC 61508 y niveles de integridad de seguridad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.
- [SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md), [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md), [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md), [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md).

**Aparece en los casos de estudio:** [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

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

[↑ Glosario](../../README.md) · [← Catálogo de servicios](./catalogo-de-servicios.md) · [Causa y evidencia →](./causa-y-evidencia.md)
