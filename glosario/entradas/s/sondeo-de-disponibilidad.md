# Sondeo de disponibilidad

[↑ Glosario](../../README.md) · [← Sondeo de arranque](./sondeo-de-arranque.md) · [Sondeo de vida →](./sondeo-de-vida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Comprobación de que la instancia puede atender solicitudes; su fallo la retira del reparto.

Definición de trabajo de [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md).

## Por qué importa

La clase donde se define, [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md), existe con este propósito: la clase existe para que distingas tres preguntas que un orquestador hace al servicio —¿sigues vivo?, ¿puedes atender?, ¿ya arrancaste?—, diseñes sondeos que no conviertan la caída de una dependencia en un ciclo de reinicios, calientes una instancia antes de darle tráfico y apagues el proceso sin cortar las solicitudes en curso.

## Cómo funciona

Según [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md):

Porque reiniciar la instancia no repara la base de datos y sí pierde cachés y conexiones; además todas las instancias fallarían a la vez. La base de datos pertenece al sondeo de disponibilidad, que retira sin reiniciar.

## Ejemplo

Ejemplo de [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) (sección «Preguntas frecuentes»):

Porque reiniciar la instancia no repara la base de datos y sí pierde cachés y conexiones; además todas las instancias fallarían a la vez. La base de datos pertenece al sondeo de disponibilidad, que retira sin reiniciar.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una instancia recién arrancada responde con errores** — causa: recibe tráfico sin estar lista. Corrección: sondeo de disponibilidad y de arranque. ([SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La base de datos pertenece al sondeo de disponibilidad, que retira sin reiniciar. ([SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Instancia](../i/instancia.md), [Calentamiento](../c/calentamiento.md), [Cascada de reinicios](../c/cascada-de-reinicios.md), [Drenaje](../d/drenaje.md), [Orquestador](../o/orquestador.md), [Plazo de gracia](../p/plazo-de-gracia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE Book: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — señales de monitorización; autoridad: Google.
- [Python: http.server](https://docs.python.org/3/library/http.server.html) — servidor local del experimento; autoridad: Python Software Foundation.
- [Python: threading](https://docs.python.org/3/library/threading.html) — hilos y su espera al cerrar; autoridad: Python Software Foundation.
- [Python: signal](https://docs.python.org/3/library/signal.html) — señales del sistema en Python; autoridad: Python Software Foundation.
- [W3C Trace Context](https://www.w3.org/TR/trace-context/) — propagación de la correlación entre servicios; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Sondeo de arranque](./sondeo-de-arranque.md) · [Sondeo de vida →](./sondeo-de-vida.md)
