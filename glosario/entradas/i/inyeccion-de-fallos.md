# Inyección de fallos

[↑ Glosario](../../README.md) · [← Inyección de fallas](./inyeccion-de-fallas.md) · [Inyección de prompt →](./inyeccion-de-prompt.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

La **inyección de fallos** es la introducción deliberada de un fallo en un sistema, o en su modelo, para observar si es detectado y cómo responde el sistema. [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md) la aplica a fallos físicos y digitales en simulación; [SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) la usa con latencia, error, caída o carga; [SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md) la usa para provocar una condición de error en una automatización frágil. El núcleo es el mismo: provocar a propósito lo que «puede pasar» para verlo pasar.

## Por qué importa

Mide si una defensa funciona en lugar de suponerlo. [SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md) lo dice con precisión: convierte «puede pasar» en «pasa y lo vemos». Y [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md) da el valor práctico: cambia «creemos que lo detecta» por «lo detecta en N de 100 casos», y el resultado informa qué defensa añadir.

## Cómo funciona

[SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md) ejemplifica fallos físicos y digitales: congelar la lectura de un sensor, añadir una deriva, invertir un bit, cortar la energía a mitad de una escritura. Hsueh y colaboradores, citados por la clase, clasifican las técnicas según el nivel en que se inyecta: hardware, software o simulación. La clase elige simulación porque es reproducible y barato.

[SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) añade que **cada tipo de fallo ataca una defensa distinta**: la latencia añadida prueba los *timeouts* y los reintentos; los errores prueban el manejo de fallos y el circuit breaker; la caída de una dependencia prueba la degradación; la carga prueba los límites y la contención. El procedimiento general es:

1. Definir una hipótesis de comportamiento esperado.
2. Inyectar un fallo concreto, de alcance acotado.
3. Observar la respuesta con las métricas definidas.
4. Comparar con la hipótesis y corregir la defensa o el supuesto.

## Ejemplo

En [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), el nodo ambiental recibe un sensor de CO₂ congelado y se mide cuántas veces de 100 lo detecta el comparador de dos sensores. Ilustración propia: en una automatización que descarga archivos, se simula que la segunda descarga devuelve un error 500 para comprobar que la ejecución se detiene y deja un estado recuperable, no a medias.

## Errores y confusiones comunes

- **Inyectar sin hipótesis ni medición,** que no enseña nada.
- **Confundirla con una prueba de carga:** la carga es un tipo de fallo entre varios.
- **Inyectar en producción sin acotar el alcance** ni poder detenerla.
- **Considerar probada una defensa por un solo caso.**

## Límites y cuándo no aplica

Solo prueba los fallos que alguien imaginó inyectar. La simulación de [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md) no sustituye a la inyección en hardware real, que descubre fallos que el modelo no recoge. En sistemas sin un comportamiento esperado definido, no hay con qué comparar.

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
