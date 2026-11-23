# Sondeo de vida

[↑ Glosario](../../README.md) · [← Sondeo de disponibilidad](./sondeo-de-disponibilidad.md) · [Sorpresa →](./sorpresa.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Comprobación de que el proceso no está bloqueado; su fallo provoca un reinicio.

Definición de trabajo de [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md).

## Por qué importa

En [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md), el tema «Dependencias y cascadas» importa porque un sondeo de vida que consulta una dependencia convierte su caída en una caída del servicio.

## Cómo funciona

Según [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md):

El sondeo de **vida** responde «¿está el proceso atascado?» y su fallo provoca un **reinicio**: debe depender solo del propio proceso (por ejemplo, que el bucle de eventos responda). El de **disponibilidad** responde «¿puede atender solicitudes ahora?», incluye las dependencias necesarias y su fallo **retira** la instancia del reparto sin reiniciarla. El de **arranque** da tiempo a una instancia lenta de iniciarse sin que el de vida la mate. Confundirlos produce tanto reinicios innecesarios como instancias rotas que siguen recibiendo tráfico.

Según [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md):

Reproduce el fallo de la clase: **un sondeo de vida que depende de la base de datos**. Haz que el sondeo `/salud/viva` abra una conexión a la base de datos y apágala 120 s. **Síntoma:** todas las instancias se reinician en minutos y el servicio tarda más en volver que la propia base de datos. **Hipótesis rivales:** (a) las instancias tienen un fallo propio; (b) el sondeo falla por la dependencia. **Prueba:** ejecuta el sondeo a mano contra la instancia con la base de datos caída y contra una con la base de datos sana, y observa el mismo proceso sano con resultados distintos. **Causa:** la vida depende de algo externo. **Corrección:** vida local y disponibilidad con dependencias.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md):

La plataforma expone tres sondeos: `/salud/viva` (local, sin dependencias, usado para reiniciar), `/salud/lista` (comprueba base de datos, cola y que la caché alcance el 60 % de aciertos, usado para retirar del reparto) y `/salud/arranque` (permite hasta 60 s de inicio). Al recibir la señal de terminación, la instancia se declara no lista, deja de aceptar conexiones, espera hasta 25 s a las solicitudes en curso, devuelve a la cola los trabajos largos y sale con código 0. El plazo de gracia del orquestador es 30 s.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Todas las instancias se reinician cuando cae la base de datos** — causa: el sondeo de vida consulta una dependencia externa. Corrección: vida local; dependencias en disponibilidad. ([SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El sondeo de **vida** responde «¿está el proceso atascado?» y su fallo provoca un **reinicio**: debe depender solo del propio proceso (por ejemplo, que el bucle de eventos responda). ([SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md))
- **un sondeo de vida que depende de la base de datos**. ([SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Proceso](../p/proceso.md), [Calentamiento](../c/calentamiento.md), [Cascada de reinicios](../c/cascada-de-reinicios.md), [Drenaje](../d/drenaje.md), [Orquestador](../o/orquestador.md), [Plazo de gracia](../p/plazo-de-gracia.md).
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

[↑ Glosario](../../README.md) · [← Sondeo de disponibilidad](./sondeo-de-disponibilidad.md) · [Sorpresa →](./sorpresa.md)
