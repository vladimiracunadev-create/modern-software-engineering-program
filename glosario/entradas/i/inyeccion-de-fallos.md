# Inyección de fallos

[↑ Glosario](../../README.md) · [← Inyección de fallas](./inyeccion-de-fallas.md) · [Inyección de prompt →](./inyeccion-de-prompt.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Introducción deliberada de un fallo en un sistema o su modelo para observar si es detectado y cómo responde.

Definición de trabajo de [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md): Introducción deliberada de un fallo (latencia, error, caída, carga) para observar la respuesta del sistema.
- En [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md): Provocar deliberadamente una condición de error para observar cómo responde el sistema.

## Por qué importa

En [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), el tema «Inyección de fallos» importa porque mide si una defensa funciona en lugar de suponerlo.

En [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md), el tema «Inyección de fallos» importa porque cada tipo de fallo prueba una defensa distinta.

En [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md), el tema «Inyección de fallos» importa porque convierte «puede pasar» en «pasa y lo vemos».

## Cómo funciona

Según [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), en la sección «Inyección de fallos»:

Inyectar un fallo es provocarlo a propósito: congelar la lectura de un sensor, añadir una deriva, invertir un bit, cortar la energía a mitad de una escritura. Hsueh y colaboradores clasifican las técnicas según el nivel en que se inyecta (hardware, software, simulación). Aquí se inyecta en simulación porque es reproducible y barato. El valor es que convierte «creemos que lo detecta» en «lo detecta en N de 100 casos»; y el resultado informa qué defensa añadir.

Según [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md), en la sección «Inyección de fallos»:

Cada tipo de fallo ataca una defensa distinta. La **latencia añadida** (la base responde, pero más lenta) pone a prueba los timeouts, la cola y la capacidad: es el fallo más traicionero porque no produce errores sino colas. Los **errores intermitentes** ponen a prueba los reintentos, los respaldos y la idempotencia. La **caída total** pone a prueba el interruptor, el mamparo y la respuesta degradada. El **aumento de tráfico** pone a prueba el descarte de carga y la capacidad. Un plan que solo inyecte caídas totales (lo que se le ocurre a todo el mundo) ignora que los incidentes reales suelen ser degradaciones parciales. La inyección debe ser parecida a un evento real, controlada (se puede detener) y observable (se sabe cuándo empezó y cuándo terminó).

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md):

El equipo de la plataforma entrega el modelo de fallos del nodo con doce filas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se cree que la defensa funciona sin haberla probado** — causa: sin inyección de fallos. Corrección: inyectar y medir la detección por tipo. ([SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se inyectó ningún fallo en hardware ni se hizo un AMFE real: los seis tipos de fallo, la escritura byte a byte y las puntuaciones son construcciones del autor. La siguiente clase reúne todo en un dispositivo simulado operable y actualizable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Latencia](../l/latencia.md), [Modelo](../m/modelo.md), [AMFE](../a/amfe.md), [Bloqueo](../b/bloqueo.md), [Concurrencia](../c/concurrencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Hsueh, Tsai e Iyer, «Fault injection techniques and tools» (IEEE Computer, 1997)](https://doi.org/10.1109/2.585157) — técnicas de inyección de fallos; autoridad: IEEE Computer.
- [IEC 60812:2018, FMEA y FMECA](https://webstore.iec.ch/en/publication/26359) — análisis de modos de fallo y efectos; autoridad: IEC.
- [Gal y Toledo, «Algorithms and data structures for flash memories» (ACM Computing Surveys, 2005)](https://doi.org/10.1145/1089733.1089735) — escrituras en flash y recuperación tras cortes; autoridad: ACM Computing Surveys.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — análisis de fallos y verificación en ingeniería de sistemas; autoridad: NASA.
- [Python: `zlib`](https://docs.python.org/3/library/zlib.html) — `crc32` usado como suma de verificación; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Inyección de fallas](./inyeccion-de-fallas.md) · [Inyección de prompt →](./inyeccion-de-prompt.md)
