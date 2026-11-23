# Drenaje

[↑ Glosario](../../README.md) · [← Drenado](./drenado.md) · [Driver arquitectónico →](./driver-arquitectonico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Espera controlada a que terminen las solicitudes en curso antes de salir.

Definición de trabajo de [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md): Terminar el trabajo en curso y devolver el pendiente antes de salir.

## Por qué importa

La clase donde se define, [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md), existe con este propósito: la clase existe para que distingas tres preguntas que un orquestador hace al servicio —¿sigues vivo?, ¿puedes atender?, ¿ya arrancaste?—, diseñes sondeos que no conviertan la caída de una dependencia en un ciclo de reinicios, calientes una instancia antes de darle tráfico y apagues el proceso sin cortar las solicitudes en curso.

## Cómo funciona

Según [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md):

Cuando el orquestador quiere retirar una instancia envía una señal de terminación y espera un plazo de gracia antes de forzar la salida. El servicio debe, en orden: dejar de declararse disponible para que le retiren el tráfico, dejar de aceptar conexiones nuevas, esperar las solicitudes en curso hasta un máximo, interrumpir o devolver a la cola los trabajos largos y salir. Si el plazo de gracia es menor que la solicitud más larga esperable, el drenaje no basta.

Según [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md):

Traslada el experimento a otro de los dominios persistentes (por ejemplo, un servicio de pagos ficticio): cambia las dependencias y conserva el procedimiento de separar los sondeos, medir el drenaje y elegir el criterio de calentamiento. La transferencia está lograda cuando explicas qué dependía de la plataforma de entregas y cuál es el patrón de los tres sondeos.

## Ejemplo

Caso medido en la sección «Apagado abrupto o con drenaje en un servidor local real» de [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md):

Se levanta un `ThreadingHTTPServer` cuyo manejador tarda 200 ms (diez pausas de 20 ms) y 30 clientes envían una solicitud a la vez. A los 80 ms se detiene el servidor de dos maneras. **Abrupto:** se activa una bandera que corta las conexiones en curso sin responder (el efecto visto desde el cliente de un proceso que muere). **Con drenaje:** `shutdown()` deja de aceptar conexiones y `server_close()` espera a los hilos en curso.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Estudiantes pierden una subida al desplegar** — causa: terminación sin drenaje. Corrección: retirar, dejar de aceptar y esperar con plazo. ([SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md))
- **El drenaje no termina nunca** — causa: no hay plazo máximo ni trabajos que se devuelvan a la cola. Corrección: plazo acotado y devolver los trabajos largos. ([SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si el plazo de gracia es menor que la solicitud más larga esperable, el drenaje no basta. ([SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md))
- Traslada el experimento a otro de los dominios persistentes (por ejemplo, un servicio de pagos ficticio): cambia las dependencias y conserva el procedimiento de separar los sondeos, medir el drenaje y elegir el criterio de calentamiento. ([SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Trabajo](../t/trabajo.md).
- **Ver también:** [Trabajo en curso](../t/trabajo-en-curso.md), [Espera](../e/espera.md), [Artefacto inmutable](../a/artefacto-inmutable.md), [Calentamiento](../c/calentamiento.md), [Cascada de reinicios](../c/cascada-de-reinicios.md), [Concurrencia](../c/concurrencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-345 — 12-factor y aplicaciones nativas de la nube](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md).

**Aparece en los casos de estudio:** [Slack](../../../casos/exito/slack.md).

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

[↑ Glosario](../../README.md) · [← Drenado](./drenado.md) · [Driver arquitectónico →](./driver-arquitectonico.md)
