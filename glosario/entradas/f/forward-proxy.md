# Forward proxy

[↑ Glosario](../../README.md) · [← Formatter](./formatter.md) · [FPR →](./fpr.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Intermediario que actúa por clientes hacia destinos.

Definición de trabajo de [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md).

## Por qué importa

La clase donde se define, [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md), existe con este propósito: la clase existe para mapear cómo proxy, balanceador, gateway y CDN cambian conexiones, metadatos y caché.

## Cómo funciona

Según [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md):

El cliente elige o recibe política para un forward proxy que actúa hacia destinos. Un reverse proxy recibe en nombre del origen y selecciona servicios internos. La misma tecnología puede cumplir ambos roles; lo que importa es quién la configura, a qué lado representa y qué autoridad tiene.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md):

La petición observable de extremo a extremo asigna un identificador de correlación en el primer componente confiable y lo propaga. El origen indica si la respuesta vino de caché y qué backend atendió sin exponer topología sensible al público. Los timeouts decrecen hacia dentro para que el gateway pueda responder antes del deadline del cliente.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md)) son:

- **El origen registra IP falsas** — causa: confía en `X-Forwarded-For` que viene del cliente. Corrección: sobrescribir en el borde y aceptar conexiones solo del proxy.
- **Tráfico a un origen caído tras detectarlo** — causa: sin comprobaciones de salud o con intervalos largos. Corrección: comprobaciones activas y pasivas y reintento hacia otro origen.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md)) son: Estas definiciones son operativas: precisan el uso dentro de la petición observable de extremo a extremo y deben leerse junto a las fuentes. No convierten un término histórico o dependiente de implementación en una garantía universal. No cubre configuración de un proveedor concreto ni DDoS. Más intermediarios aportan control y también estados de fallo. La siguiente clase estudia conexiones persistentes y comunicación en tiempo real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-043](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Intermediario](../i/intermediario.md), [Alcance](../a/alcance.md), [Balanceador](../b/balanceador.md), [CDN](../c/cdn.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9111 — HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 7239 — Forwarded HTTP Extension](https://www.rfc-editor.org/rfc/rfc7239) — estandariza metadatos reenviados y documenta sus consideraciones de seguridad y privacidad.

---

[↑ Glosario](../../README.md) · [← Formatter](./formatter.md) · [FPR →](./fpr.md)
