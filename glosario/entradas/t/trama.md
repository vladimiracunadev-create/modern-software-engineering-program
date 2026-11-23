# Trama

[↑ Glosario](../../README.md) · [← Tráfico norte-sur y este-oeste](./trafico-norte-sur-y-este-oeste.md) · [Tramo revisable →](./tramo-revisable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Unidad transmitida por un protocolo de enlace.

Definición de trabajo de [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md).

## Por qué importa

La clase donde se define, [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), existe con este propósito: la clase existe para explicar entrega local mediante tramas, direcciones de enlace y resolución de vecinos.

## Cómo funciona

Según [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md):

Una interfaz transmite tramas dentro de un enlace. La dirección MAC identifica una interfaz en ese alcance, no una identidad global de la persona ni una ruta por Internet. Switches aprenden asociaciones entre direcciones y puertos; ese aprendizaje expira y puede cambiar al mover un equipo.

Según [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md):

En la capa de IP suelen exponer 1500, pero Wi-Fi agrega capas propias de acceso al medio, retransmisión y agregación de tramas que Ethernet cableado no tiene. El MTU igual no implica comportamiento igual: la variación de latencia y la pérdida visible difieren.

## Ejemplo

Ejemplo de [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md) (sección «Preguntas frecuentes»):

En la capa de IP suelen exponer 1500, pero Wi-Fi agrega capas propias de acceso al medio, retransmisión y agregación de tramas que Ethernet cableado no tiene. El MTU igual no implica comportamiento igual: la variación de latencia y la pérdida visible difieren.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md)) son:

- **«Las transferencias grandes se cuelgan pero conectar funciona»** — causa: un tramo con MTU menor descarta paquetes con DF y los avisos ICMP se filtran. Corrección: probar PMTU, permitir ICMP «fragmentación necesaria» y ajustar el MSS.
- **Medir el rendimiento en loopback y extrapolarlo** — causa: el loopback no usa ningún medio. Corrección: medir sobre la interfaz y la ruta reales.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una trama Ethernet II tiene una cabecera de 14 bytes (direcciones de destino y origen y el tipo), una carga útil de hasta 1500 bytes —el *MTU* habitual— y 4 bytes de verificación (FCS), de modo que la trama completa mide hasta 1518 bytes. ([SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Enlace](../e/enlace.md), [Alcance](../a/alcance.md), [ARP](../a/arp.md), [Código de autenticación de mensaje](../c/codigo-de-autenticacion-de-mensaje.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md), [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 826 — An Ethernet Address Resolution Protocol](https://www.rfc-editor.org/rfc/rfc826) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 894 — IP Datagrams over Ethernet Networks](https://www.rfc-editor.org/rfc/rfc894) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 1122 — Requirements for Internet Hosts: Communication Layers](https://www.rfc-editor.org/rfc/rfc1122) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Tráfico norte-sur y este-oeste](./trafico-norte-sur-y-este-oeste.md) · [Tramo revisable →](./tramo-revisable.md)
