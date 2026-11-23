# SSRF

[↑ Glosario](../../README.md) · [← Srcset](./srcset.md) · [Stack frame y alcance →](./stack-frame-y-alcance.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Abuso que induce a un servidor a solicitar destinos no autorizados.

Definición de trabajo de [SE-048 — Proyecto: servicio observable y tolerante a fallos de red](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md).

## Por qué importa

La clase donde se define, [SE-048 — Proyecto: servicio observable y tolerante a fallos de red](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), existe con este propósito: la clase existe para construir un servicio observable que trate timeout, reintento e idempotencia como decisiones de producto.

## Cómo funciona

Según [SE-048 — Proyecto: servicio observable y tolerante a fallos de red](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md):

La petición observable de extremo a extremo acepta solo esquemas y destinos permitidos, rechaza direcciones locales o metadatos cuando opera como servicio compartido y limita redirecciones. La validación evita convertir la herramienta en SSRF. El informe redacta credenciales, query sensible y direcciones privadas.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-048 — Proyecto: servicio observable y tolerante a fallos de red](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md):

El proyecto entrega un servidor local y CLI de consulta. Un entorno simulado ofrece DNS demorado, puerto cerrado, TLS autofirmado, 503 transitorio y caché. El tablero muestra tasa de éxito y p95 por fase; el runbook explica detección, mitigación, recuperación y límite de cada automatismo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-048 — Proyecto: servicio observable y tolerante a fallos de red](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md)) son:

- **El servicio se satura más al fallar** — causa: reintentos inmediatos y sincronizados de muchos clientes. Corrección: retroceso exponencial con jitter y tope de intentos.
- **Peticiones duplicadas tras un timeout** — causa: se reintentan operaciones no idempotentes. Corrección: claves de idempotencia o consulta previa del estado.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-048 — Proyecto: servicio observable y tolerante a fallos de red](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md)) son: Estas definiciones son operativas: precisan el uso dentro de la petición observable de extremo a extremo y deben leerse junto a las fuentes. No convierten un término histórico o dependiente de implementación en una garantía universal. El proyecto demuestra diseño y diagnóstico en laboratorio; no certifica disponibilidad productiva ni sustituye monitoreo externo. Sus resultados alimentan la [Parte 4](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), donde el mismo incidente se formaliza como problema, invariantes y algoritmo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Backoff](../b/backoff.md), [Circuit breaker](../c/circuit-breaker.md), [Deadline](../d/deadline.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-048 — Proyecto: servicio observable y tolerante a fallos de red](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-039](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md), [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9111 — HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9000 — QUIC](https://www.rfc-editor.org/rfc/rfc9000) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Srcset](./srcset.md) · [Stack frame y alcance →](./stack-frame-y-alcance.md)
