# AMFE

[↑ Glosario](../../README.md) · [← Amenazas y requisitos de seguridad](./amenazas-y-requisitos-de-seguridad.md) · [Amortizado →](./amortizado.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Análisis de modos de fallo y efectos; tabla de modos de fallo con su efecto, causa y valoración de gravedad, ocurrencia y detección.

Definición de trabajo de [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md).

## Por qué importa

En [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), el tema «AMFE y estabilidad» importa porque la puntuación ordinal es frágil; sirve para conversar.

## Cómo funciona

Según [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md):

El análisis de modos de fallo y efectos (AMFE, IEC 60812) lista cada modo de fallo con su efecto y le asigna gravedad, ocurrencia y capacidad de detección en escalas ordinales de 1 a 10; el producto es el número de prioridad de riesgo (NPR). Es un método para ordenar la conversación, no para medir. Las escalas son ordinales y su producto mezcla magnitudes distintas: un punto de desacuerdo entre dos evaluadoras reordena la lista. La prioridad debe revisarse mirando la gravedad por separado: un fallo de gravedad 10 merece atención aunque su NPR sea bajo.

Según [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md):

El equipo de la plataforma entrega el modelo de fallos del nodo con doce filas. Cada una dice: el fallo (deriva del sensor de CO₂, corte durante la escritura de la configuración, bit invertido en el bus), su efecto (ventilación que no arranca, nodo con configuración inválida), la defensa que lo ve (referencia con un segundo sensor, dos copias alternadas con suma, CRC de la trama de `SE-266`), el resultado de la inyección (100 de 100) y lo que queda sin cubrir (fallo simultáneo de ambos sensores por contaminación, fallo de la propia memoria). La prioridad se discute con el AMFE, y la gravedad se mira aparte: los modos con gravedad 9 o 10 se revisan aunque su NPR sea bajo.

## Ejemplo

Ejemplo de [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma entrega el modelo de fallos del nodo con doce filas. Cada una dice: el fallo (deriva del sensor de CO₂, corte durante la escritura de la configuración, bit invertido en el bus), su efecto (ventilación que no arranca, nodo con configuración inválida), la defensa que lo ve (referencia con un segundo sensor, dos copias alternadas con suma, CRC de la trama de `SE-266`), el resultado de la inyección (100 de 100) y lo que queda sin cubrir (fallo simultáneo de ambos sensores por contaminación, fallo de la propia memoria).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md)) son:

- **Lecturas plausibles y erróneas durante semanas** — causa: deriva lenta sin referencia independiente. Corrección: comparar con otro sensor o con un modelo del entorno.
- **Configuración inválida tras un corte** — causa: sobrescritura o una sola copia. Corrección: dos copias alternadas con suma y número de secuencia.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La figura no desautoriza el AMFE: dice que su orden fino es poco fiable y que sirve para elegir de qué hablar. ([SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modo de fallo](../m/modo-de-fallo.md), [Análisis](./analisis.md), [Efecto](../e/efecto.md), [Gravedad](../g/gravedad.md), [Fallo silencioso](../f/fallo-silencioso.md), [Inyección de fallos](../i/inyeccion-de-fallos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

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

[↑ Glosario](../../README.md) · [← Amenazas y requisitos de seguridad](./amenazas-y-requisitos-de-seguridad.md) · [Amortizado →](./amortizado.md)
