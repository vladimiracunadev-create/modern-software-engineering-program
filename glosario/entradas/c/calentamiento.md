# Calentamiento

[↑ Glosario](../../README.md) · [← Caducidad de la evidencia](./caducidad-de-la-evidencia.md) · [Calibración →](./calibracion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Periodo en que una instancia nueva llena sus cachés y conexiones antes de rendir con normalidad.

Definición de trabajo de [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-437 — Perfiles, benchmarks y errores de medición](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md): Conjunto de ejecuciones iniciales cuyo tiempo difiere del régimen estable por cachés frías o carga de módulos.

## Por qué importa

En [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md), el tema «Calentamiento» importa porque una instancia con caché fría atiende peor que una caliente; el criterio de disponibilidad lo reconoce o lo ignora.

## Cómo funciona

Según [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md), en la sección «Calentamiento»:

Una instancia nueva tiene la caché fría, conexiones sin abrir y código sin compilar; sus primeras solicitudes son más lentas. Hay tres estrategias: recibir tráfico desde el arranque (simple, con solicitudes lentas), esperar un tiempo fijo (predecible, ignora la velocidad real) o declararse lista al alcanzar un umbral de aciertos (adaptable, exige instrumentar). El calentamiento traslada el costo: las otras instancias absorben más tráfico mientras tanto.

## Ejemplo

Ejemplo de [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) (sección «Caso conductor»):

La plataforma de entregas queda con un comportamiento operable: tres sondeos con propósito distinto, calentamiento declarado y apagado ordenado. Recupera `SE-247`: los trabajos largos vuelven a la cola al apagar. La clase siguiente aplica todo lo aprendido a una API deliberadamente defectuosa. Cambia después una sola decisión, el plazo de gracia de 30 a 10 s, y revisa qué artefactos hay que tocar.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md)) son:

- **Todas las instancias se reinician cuando cae la base de datos** — causa: el sondeo de vida consulta una dependencia externa. Corrección: vida local; dependencias en disponibilidad.
- **Una instancia recién arrancada responde con errores** — causa: recibe tráfico sin estar lista. Corrección: sondeo de disponibilidad y de arranque.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** la curva lineal de calentamiento es un supuesto: las cachés reales se calientan según la popularidad de las claves. ([SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md))
- Traslada el experimento a otro de los dominios persistentes (por ejemplo, un servicio de pagos ficticio): cambia las dependencias y conserva el procedimiento de separar los sondeos, medir el drenaje y elegir el criterio de calentamiento. ([SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md))

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
