# VLAN

[↑ Glosario](../../README.md) · [← Vista lógica](./vista-logica.md) · [VM →](./vm.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Segmentación lógica de dominios de enlace sobre infraestructura compartida.

Definición de trabajo de [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md).

## Por qué importa

La clase donde se define, [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), existe con este propósito: la clase existe para explicar entrega local mediante tramas, direcciones de enlace y resolución de vecinos.

## Cómo funciona

Según [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md):

En IPv4, ARP resuelve una dirección de protocolo a una dirección de enlace en el dominio local. Para un destino remoto, el host resuelve la MAC de la puerta de enlace, no la del servidor. Una entrada vecina incompleta orienta el diagnóstico hacia enlace, VLAN o puerta de enlace.

Según [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md):

El conjunto de interfaces que reciben una trama enviada a la dirección de difusión (por ejemplo, una consulta ARP). Un enrutador separa dominios; un conmutador no, salvo que use VLAN. Acotarlos limita el ruido y el alcance de ciertos ataques.

## Ejemplo

Ejemplo de [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md) (sección «Preguntas frecuentes»):

El conjunto de interfaces que reciben una trama enviada a la dirección de difusión (por ejemplo, una consulta ARP). Un enrutador separa dominios; un conmutador no, salvo que use VLAN. Acotarlos limita el ruido y el alcance de ciertos ataques.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md)) son:

- **«Las transferencias grandes se cuelgan pero conectar funciona»** — causa: un tramo con MTU menor descarta paquetes con DF y los avisos ICMP se filtran. Corrección: probar PMTU, permitir ICMP «fragmentación necesaria» y ajustar el MSS.
- **Medir el rendimiento en loopback y extrapolarlo** — causa: el loopback no usa ningún medio. Corrección: medir sobre la interfaz y la ruta reales.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** es un modelo con direcciones de documentación (RFC 5737), no una captura de una red real, y no considera VLAN, puentes ni redes en malla. ([SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dominio](../d/dominio.md), [Enlace](../e/enlace.md), [Segmentación](../s/segmentacion.md), [Sobre](../s/sobre.md), [Alcance](../a/alcance.md), [ARP](../a/arp.md).
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

[↑ Glosario](../../README.md) · [← Vista lógica](./vista-logica.md) · [VM →](./vm.md)
