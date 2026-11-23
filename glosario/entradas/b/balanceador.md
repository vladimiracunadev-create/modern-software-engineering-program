# Balanceador

[↑ Glosario](../../README.md) · [← Balance y rotaciones](./balance-y-rotaciones.md) · [Balanceo de carga →](./balanceo-de-carga.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Selector de un destino entre instancias elegibles.

Definición de trabajo de [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md).

## Por qué importa

La clase donde se define, [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md), existe con este propósito: la clase existe para mapear cómo proxy, balanceador, gateway y CDN cambian conexiones, metadatos y caché.

## Cómo funciona

Según [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md):

Un balanceador reparte peticiones entre varios orígenes y debe saber cuáles están sanos. En una simulación local con dos orígenes, A y B, 20 peticiones en turno rotatorio se repartieron 10 y 10. Al detener A, las 20 siguientes terminaron en B gracias a un reintento hacia el otro origen, y se detectaron 10 fallos de conexión. La *rapidez* de detección dependió de cómo falla la conexión: 0,35 ms en Linux (rechazo inmediato) frente a 499,9 ms en Windows (la prueba esperó el timeout de 0,5 s). Sin comprobaciones de salud, un balanceador seguiría enviando tráfico al origen caído; con ellas, lo saca de rotación y lo reincorpora al recuperarse.

Según [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md):

Un proxy inverso recibe peticiones y las reenvía a uno o más orígenes; un balanceador es un proxy (u otro dispositivo) cuyo propósito es repartir carga y conmutar ante fallas. En la práctica suelen ser el mismo componente con distintas funciones.

## Ejemplo

Ejemplo de [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md) (sección «Ejemplo mínimo»):

Dibuja cliente → proxy → balanceador → dos backends. Marca en cada enlace quién inicia conexión, dónde termina TLS, qué Host se conserva y qué dirección ve el receptor.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md)) son:

- **El origen registra IP falsas** — causa: confía en `X-Forwarded-For` que viene del cliente. Corrección: sobrescribir en el borde y aceptar conexiones solo del proxy.
- **Tráfico a un origen caído tras detectarlo** — causa: sin comprobaciones de salud o con intervalos largos. Corrección: comprobaciones activas y pasivas y reintento hacia otro origen.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Sin comprobaciones de salud, un balanceador seguiría enviando tráfico al origen caído; con ellas, lo saca de rotación y lo reincorpora al recuperarse. ([SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-043](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Instancia](../i/instancia.md), [Alcance](../a/alcance.md), [CDN](../c/cdn.md), [Diagnóstico](../d/diagnostico.md), [Forward proxy](../f/forward-proxy.md), [Garantía](../g/garantia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-044 — Proxies, balanceadores, gateways y CDN](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (30 clases más lo mencionan; las que más):

[SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-043](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md), [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), [SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md), [SE-045](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md), [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Slack](../../../casos/exito/slack.md), [Shopify](../../../casos/exito/shopify.md), [Cloudflare](../../../casos/exito/cloudflare.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9111 — HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 7239 — Forwarded HTTP Extension](https://www.rfc-editor.org/rfc/rfc7239) — estandariza metadatos reenviados y documenta sus consideraciones de seguridad y privacidad.

---

[↑ Glosario](../../README.md) · [← Balance y rotaciones](./balance-y-rotaciones.md) · [Balanceo de carga →](./balanceo-de-carga.md)
