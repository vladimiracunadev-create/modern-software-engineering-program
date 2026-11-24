# Calentamiento

[↑ Glosario](../../README.md) · [← Caducidad de la evidencia](./caducidad-de-la-evidencia.md) · [Calibración →](./calibracion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

El **calentamiento** (*warm-up*) es el periodo en que una instancia nueva llena sus cachés y abre sus conexiones antes de rendir con normalidad. Es el sentido de [SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) (health, readiness y apagado ordenado). [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md) lo usa en mediciones: el conjunto de ejecuciones iniciales cuyo tiempo difiere del régimen estable por cachés frías o carga de módulos. En ambos, lo común es que las primeras operaciones son más lentas que las siguientes.

## Por qué importa

Una instancia recién arrancada con caché fría atiende peor que una caliente, y el criterio de disponibilidad lo reconoce o lo ignora. Si lo ignora, el balanceador manda tráfico completo a una instancia que no está lista y aparecen errores o lentitud. En mediciones ([SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md)), si no se descarta el calentamiento el benchmark mide el arranque y no el comportamiento estable.

## Cómo funciona

Una instancia nueva tiene la caché vacía, conexiones sin abrir y código sin compilar. [SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) ofrece tres estrategias para decidir cuándo recibe tráfico completo:

1. **Recibir tráfico desde el arranque:** simple, con solicitudes lentas al principio.
2. **Esperar un tiempo fijo:** predecible, pero ignora la velocidad real de calentamiento.
3. **Declararse lista al alcanzar un umbral de aciertos de caché:** adaptable, pero exige instrumentar.

El calentamiento **traslada el costo**: mientras una instancia se calienta, las otras absorben más tráfico. Por eso conecta con la disponibilidad (readiness): una instancia puede estar viva y aun así no estar lista.

En [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md), el mismo fenómeno obliga a diseñar la medición: ejecuciones de descarte iniciales y análisis solo del régimen estable.

## Ejemplo

El caso conductor de [SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) deja la plataforma de entregas con tres sondeos de propósito distinto, calentamiento declarado y apagado ordenado. Cambiar una sola decisión, el plazo de gracia de 30 a 10 segundos, obliga a revisar qué artefactos se tocan. Ilustración propia: si una instancia necesita 80 % de aciertos de caché para rendir, se marca lista al superarlo y no a los 30 segundos fijos.

## Errores y confusiones comunes

- **Instancia recién arrancada que responde con errores:** recibe tráfico sin estar lista; corrección, sondeo de disponibilidad y de arranque ([SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md)).
- **Reinicio de todas las instancias cuando cae la base de datos:** el sondeo de vida consulta una dependencia externa; la vida debe ser local.
- **Confundirlo con arranque en frío:** aquel es crear el entorno; el calentamiento es lo que sigue.

## Límites y cuándo no aplica

La curva lineal de calentamiento de la clase es un supuesto: las cachés reales se calientan según la popularidad de las claves ([SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md)). Con una aplicación sin caché relevante, la espera no aporta. Y el término de medición ([SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md)) no es de operación: no se resuelve con sondeos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](./conjunto.md), [Instancia](../i/instancia.md), [Módulo](../m/modulo.md), [Benchmark](../b/benchmark.md), [Cascada de reinicios](./cascada-de-reinicios.md), [Drenaje](../d/drenaje.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (15 clases más lo mencionan; las que más):

[SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-454](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md), [SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md), [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md), [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md), [SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md).

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

[↑ Glosario](../../README.md) · [← Caducidad de la evidencia](./caducidad-de-la-evidencia.md) · [Calibración →](./calibracion.md)
