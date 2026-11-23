# CDN

[↑ Glosario](../../README.md) · [← Causa, corrección y seguimiento](./causa-correccion-y-seguimiento.md) · [Celda →](./celda.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Red de borde que distribuye y puede almacenar contenido.

Definición de trabajo de [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md).

## Por qué importa

La clase donde se define, [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md), existe con este propósito: la clase existe para mapear cómo proxy, balanceador, gateway y CDN cambian conexiones, metadatos y caché.

## Cómo funciona

Según [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md):

Una CDN acerca caché y cómputo al consumidor. El punto de presencia puede responder sin contactar al origen, revalidar o fallar por política regional. `Age`, `Via`, identificadores de caché y logs de borde ayudan, pero son específicos del proveedor y no reemplazan un modelo.

## Ejemplo

Caso medido en la sección «Qué se ve y qué queda oculto detrás de una CDN» de [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md):

Una red de entrega de contenido pone intermediarios entre el cliente y el origen. Desde el cliente se observaron: `Server: cloudflare`, `Age: 3521` (la copia tenía casi una hora), `alt-svc: h3`, un certificado de 90 días emitido por una CA intermedia propia del proveedor y un RTT medio de 146 ms *hasta el nodo que respondió*. No se pudo observar: qué servidor de origen existe y dónde está, si el tramo entre la CDN y el origen va cifrado, en qué nodo de borde cayó la petición ni cuándo fue la última validación con el origen.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md)) son:

- **El origen registra IP falsas** — causa: confía en `X-Forwarded-For` que viene del cliente. Corrección: sobrescribir en el borde y aceptar conexiones solo del proxy.
- **Tráfico a un origen caído tras detectarlo** — causa: sin comprobaciones de salud o con intervalos largos. Corrección: comprobaciones activas y pasivas y reintento hacia otro origen.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No se pudo observar: qué servidor de origen existe y dónde está, si el tramo entre la CDN y el origen va cifrado, en qué nodo de borde cayó la petición ni cuándo fue la última validación con el origen. ([SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-043](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Borde](../b/borde.md), [Alcance](../a/alcance.md), [Balanceador](../b/balanceador.md), [Diagnóstico](../d/diagnostico.md), [Forward proxy](../f/forward-proxy.md), [Garantía](../g/garantia.md).
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

[↑ Glosario](../../README.md) · [← Causa, corrección y seguimiento](./causa-correccion-y-seguimiento.md) · [Celda →](./celda.md)
