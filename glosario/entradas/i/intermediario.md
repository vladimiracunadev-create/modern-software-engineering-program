# Intermediario

[↑ Glosario](../../README.md) · [← Interferencia](./interferencia.md) · [Internacionalización →](./internacionalizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Componente que reenvía, transforma o almacena tráfico entre extremos.

Definición de trabajo de [SE-037 — Modelos OSI y TCP/IP como herramientas de diagnóstico](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md).

## Por qué importa

La clase donde se define, [SE-037 — Modelos OSI y TCP/IP como herramientas de diagnóstico](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md), existe con este propósito: la clase existe para usar OSI y TCP/IP como modelos de localización de fallos, no como descripción literal del recorrido.

## Cómo funciona

Según [SE-037 — Modelos OSI y TCP/IP como herramientas de diagnóstico](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md):

La abstracción por capas tiene fugas, y las observaciones reales lo muestran. La respuesta de `example.com` incluyó `Server: cloudflare` y `Age: 3521`: no respondió el origen del sitio sino un intermediario (una CDN) que termina TLS y sirve una copia con 3521 segundos de antigüedad. La cabecera `alt-svc: h3=":443"` ofrece HTTP/3 sobre QUIC (UDP): la siguiente conexión puede ni siquiera usar TCP. Y un `ping` que responde solo demuestra una respuesta ICMP bajo esa ruta y política: no valida DNS, puerto, TLS ni HTTP.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-037 — Modelos OSI y TCP/IP como herramientas de diagnóstico](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md):

La petición observable de extremo a extremo registra cuatro tiempos: resolución, conexión, negociación segura y primer byte. Si la resolución tarda 900 ms y las demás fases 20 ms, el equipo investiga el resolver antes de escalar al servicio. Si `curl --resolve` funciona, no «demuestra que Internet funciona»: aísla DNS conservando destino, TLS y HTTP.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Atribuir una respuesta al origen** — causa: un intermediario puede responder. Corrección: leer `Server`, `Via`, `Age` y comprobar quién respondió. ([SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La respuesta de `example.com` incluyó `Server: cloudflare` y `Age: 3521`: no respondió el origen del sitio sino un intermediario (una CDN) que termina TLS y sirve una copia con 3521 segundos de antigüedad. ([SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Extremo](../e/extremo.md), [Alcance](../a/alcance.md), [Capa](../c/capa.md), [Diagnóstico](../d/diagnostico.md), [Encapsulación](../e/encapsulacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-037 — Modelos OSI y TCP/IP como herramientas de diagnóstico](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (13 clases más lo mencionan; las que más):

[SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md), [SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md), [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md), [SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md), [SE-045](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md), [SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 1122 — Requirements for Internet Hosts: Communication Layers](https://www.rfc-editor.org/rfc/rfc1122) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 8200 — Internet Protocol, Version 6](https://www.rfc-editor.org/rfc/rfc8200) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Interferencia](./interferencia.md) · [Internacionalización →](./internacionalizacion.md)
