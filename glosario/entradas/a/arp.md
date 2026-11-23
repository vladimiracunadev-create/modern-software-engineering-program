# ARP

[↑ Glosario](../../README.md) · [← Arista de valor](./arista-de-valor.md) · [Arquitectura →](./arquitectura.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Protocolo IPv4 de resolución entre dirección IP y dirección de enlace.

Definición de trabajo de [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md).

## Por qué importa

La clase donde se define, [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), existe con este propósito: la clase existe para explicar entrega local mediante tramas, direcciones de enlace y resolución de vecinos.

## Cómo funciona

Según [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md):

En IPv4, ARP resuelve una dirección de protocolo a una dirección de enlace en el dominio local. Para un destino remoto, el host resuelve la MAC de la puerta de enlace, no la del servidor. Una entrada vecina incompleta orienta el diagnóstico hacia enlace, VLAN o puerta de enlace.

Según [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md):

El conjunto de interfaces que reciben una trama enviada a la dirección de difusión (por ejemplo, una consulta ARP). Un enrutador separa dominios; un conmutador no, salvo que use VLAN. Acotarlos limita el ruido y el alcance de ciertos ataques.

## Ejemplo

Ejemplo de [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md) (sección «Ejemplo mínimo»):

Con una dirección local, máscara y destino remoto, determina cuál IP se consulta en la tabla de vecinos. Comprueba con `arp -a`, `ip neigh` o equivalente. Explica por qué no aparece la MAC del destino remoto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Suponer que ARP funciona entre subredes** — causa: ARP solo opera dentro del dominio de difusión. Corrección: revisar el gateway y la tabla de rutas. ([SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si el destino está en el mismo prefijo, resuelve con ARP la dirección de enlace (MAC) *del destino*; si está en otro, resuelve la del *gateway* y le entrega la trama con el paquete IP intacto. ([SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Enlace](../e/enlace.md), [Resolución](../r/resolucion.md), [Alcance](./alcance.md), [Código de autenticación de mensaje](../c/codigo-de-autenticacion-de-mensaje.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 826 — An Ethernet Address Resolution Protocol](https://www.rfc-editor.org/rfc/rfc826) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 894 — IP Datagrams over Ethernet Networks](https://www.rfc-editor.org/rfc/rfc894) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 1122 — Requirements for Internet Hosts: Communication Layers](https://www.rfc-editor.org/rfc/rfc1122) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Arista de valor](./arista-de-valor.md) · [Arquitectura →](./arquitectura.md)
