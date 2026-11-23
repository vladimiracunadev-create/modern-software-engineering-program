# Circuit breaker

[↑ Glosario](../../README.md) · [← Cifrado de sobre](./cifrado-de-sobre.md) · [Cita de proximidad →](./cita-de-proximidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Un **circuit breaker** (interruptor de circuito) es un componente que deja de llamar a una dependencia que está fallando de forma persistente y la vuelve a probar después de un tiempo. [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) lo define con ese comportamiento, [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md), que lo trata entre los patrones de resiliencia, como control que rechaza llamadas a una dependencia con fallos persistentes y [SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md) como control que limita llamadas a una dependencia degradada, dentro de un servicio tolerante a fallos de red. El nombre viene del interruptor eléctrico: corta el paso para proteger el resto del circuito.

## Por qué importa

Llamar a una dependencia caída tiene dos costos: cada llamada espera hasta su límite de tiempo y consume recursos del que llama, y la dependencia, si está sobrecargada, recibe más carga justo cuando necesita descanso. El interruptor convierte un fallo lento y contagioso en un rechazo inmediato y barato. Es una de las defensas con que [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) y [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) protegen al sistema de la degradación en cascada.

## Cómo funciona

Según [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md), el interruptor tiene tres estados:

1. **Cerrado:** las llamadas pasan. Se cuentan los fallos consecutivos.
2. **Abierto:** se supera un umbral de fallos y las llamadas se **rechazan al instante**, sin tocar la dependencia.
3. **Semiabierto:** tras un tiempo, se deja pasar una llamada de sondeo; si tiene éxito, el interruptor se cierra, y si falla, vuelve a abrirse.

La causa de su utilidad es el rechazo rápido: no gasta el tiempo de espera ni la carga en llamadas que van a fallar de todos modos, y le da a la dependencia tiempo para recuperarse. Lo que decide si funciona bien son sus parámetros: el umbral de fallos, el tiempo en estado abierto y qué se hace con la llamada rechazada (un valor por defecto, una respuesta degradada, un error rápido).

## Ejemplo

En el experimento de [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md), una dependencia está caída entre los 5 y los 12 segundos de una ventana de 20 s, con 100 peticiones por segundo (2 000 en total). **Sin** interruptor se hacen 2 000 llamadas al servicio, con 1 300 éxitos. **Con** interruptor (umbral de 5 fallos y 1 s en estado abierto) se hacen 1 307 llamadas, se rechazan 693 al instante y los éxitos son 1 296. El interruptor aparta 693 peticiones del servicio caído sin cambiar apenas los éxitos. Son datos simulados con parámetros del autor.

## Errores y confusiones comunes

- **Un umbral mal calibrado corta tráfico sano.** Si el umbral es muy bajo, unos pocos fallos aislados abren el interruptor y rechazan peticiones que habrían funcionado.
- **Tratar el interruptor como sustituto del límite de tiempo.** Son controles distintos: el límite de tiempo acota cada llamada ([SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md)), el interruptor deja de hacerlas.
- **No decidir qué responder cuando está abierto.** Un rechazo sin respuesta degradada solo traslada el fallo al usuario.

## Límites y cuándo no aplica

[SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) declara los límites de su experimento: la dependencia cae de golpe y se recupera de golpe, el tráfico es constante y el umbral es el del autor. Con fallos parciales, latencia creciente o varias instancias, calibrar un interruptor es mucho más delicado y exige medir la tasa de error y la latencia reales. El interruptor no corrige la dependencia ni garantiza disponibilidad: solo limita el daño de llamarla mientras falla. Y no tiene sentido si la dependencia es imprescindible y no existe ninguna alternativa degradada.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](./componente.md), [Control](./control.md), [Dependencia](../d/dependencia.md), [Alcance](../a/alcance.md), [Backoff](../b/backoff.md), [Backoff exponencial](../b/backoff-exponencial.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-048 — Proyecto: servicio observable y tolerante a fallos de red](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), [SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Azure Architecture: patrón Circuit Breaker](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) — estados y parámetros del interruptor; autoridad: documentación de Microsoft.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9111 — HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9000 — QUIC](https://www.rfc-editor.org/rfc/rfc9000) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Cifrado de sobre](./cifrado-de-sobre.md) · [Cita de proximidad →](./cita-de-proximidad.md)
