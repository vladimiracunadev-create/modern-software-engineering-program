# Referencia independiente

[↑ Glosario](../../README.md) · [← Referencia externa única](./referencia-externa-unica.md) · [Reflexión →](./reflexion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Fuente de comparación que no comparte el mecanismo de fallo del dato que se verifica.

Definición de trabajo de [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md).

## Por qué importa

En [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), el tema «Plausibilidad y referencia» importa porque las comprobaciones locales dejan pasar lo lento; una referencia independiente lo ve.

## Cómo funciona

Según [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md):

Las comprobaciones de plausibilidad miran el propio dato: rango, variación máxima entre lecturas, valor congelado, ausencia, dispersión. Detectan fallos bruscos. Un fallo lento (una deriva de offset creciente) pasa todas, porque cada lectura se parece a la anterior. Para verlo hace falta una **referencia independiente**: un segundo sensor de otro principio, un modelo del entorno o una comparación con un valor esperado. Cada comprobación añadida cubre una clase de fallo y deja otras: lo importante es saber cuáles.

Según [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** semanas después de una instalación, el CO₂ medido está 400 ppm por debajo del real y nadie lo vio. **Hipótesis rivales:** (a) el sensor falló de golpe y una comprobación lo perdió; (b) el algoritmo de calibración tiene un error; (c) una deriva lenta pasa todas las comprobaciones locales. **Prueba:** inyecta una deriva de 0,02 por muestra; con todas las comprobaciones locales se detectan 0 de 100. **Conclusión:** la causa es la ausencia de referencia independiente. **Regresión:** añade una comparación con un segundo sensor de otro principio, inyecta 100 derivas y comprueba que se detectan. No cambies a la vez la referencia y los umbrales.

## Ejemplo

Ejemplo de [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md) (sección «Caso conductor»):

El nodo ambiental de una sala de estudio continúa como caso conductor de la [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md). El taller deja el undécimo artefacto: el modelo de fallos del nodo con inyección, enumeración de cortes, AMFE y lo que queda sin cubrir. `SE-276` los reúne en un dispositivo simulado completo. Cambia después una sola defensa, la referencia independiente, y observa qué fallos dejan de verse.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Lecturas plausibles y erróneas durante semanas** — causa: deriva lenta sin referencia independiente. Corrección: comparar con otro sensor o con un modelo del entorno. ([SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Para verlo hace falta una **referencia independiente**: un segundo sensor de otro principio, un modelo del entorno o una comparación con un valor esperado. ([SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Mecanismo](../m/mecanismo.md), [AMFE](../a/amfe.md), [Fallo silencioso](../f/fallo-silencioso.md), [Inyección de fallos](../i/inyeccion-de-fallos.md), [Número de prioridad de riesgo](../n/numero-de-prioridad-de-riesgo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-275 — Taller: modelar fallos físicos y digitales](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md), [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), [SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md), [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md).

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

[↑ Glosario](../../README.md) · [← Referencia externa única](./referencia-externa-unica.md) · [Reflexión →](./reflexion.md)
