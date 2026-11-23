# MTU

[↑ Glosario](../../README.md) · [← MSB/LSB](./msb-lsb.md) · [Muerte por aserción →](./muerte-por-asercion.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Máximo tamaño de unidad que un enlace puede transportar sin tratamiento adicional.

Definición de trabajo de [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md).

## Por qué importa

La clase donde se define, [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md), existe con este propósito: la clase existe para decidir entrega directa o por gateway usando prefijos, rutas y traducción de direcciones.

## Cómo funciona

Según [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md):

Una ruta puede transportar paquetes pequeños y fallar con tamaños mayores. IPv6 exige que el origen gestione Path MTU; filtrar indiscriminadamente ICMPv6 rompe funciones esenciales. Además, que el trayecto de ida exista no garantiza una ruta de retorno ni políticas simétricas.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md):

La petición observable de extremo a extremo conserva un inventario redactado de dirección, prefijo, gateway y ruta elegida. Cuando la VPN anuncia `10.0.0.0/8` y la red local usa `10.20.30.0/24`, verifica la coincidencia más específica y documenta el conflicto. La solución puede ser renumerar, dividir rutas o cambiar política; desactivar todo el túnel solo oculta el diseño.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md)) son:

- **Un equipo alcanza Internet pero no a un vecino** — causa: máscara mal configurada: el vecino parece estar en otra red. Corrección: comparar prefijo y dirección con `ipaddress` y corregir la máscara.
- **Suponer que `is_private` equivale a «de mi red»** — causa: la misma dirección privada existe en muchas redes. Corrección: identificar equipos con nombres y credenciales, no con la dirección.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- ¿el destino está en una red conectada?, ¿cuál es la ruta más específica?, ¿qué traducción aplica el NAT? y ¿cabe el paquete en el MTU de la ruta? ([SE-039](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Enlace](../e/enlace.md), [Alcance](../a/alcance.md), [CIDR](../c/cidr.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md), [NAT](../n/nat.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 8200 — Internet Protocol, Version 6](https://www.rfc-editor.org/rfc/rfc8200) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 1918 — Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 3022 — Traditional IP Network Address Translator](https://www.rfc-editor.org/rfc/rfc3022) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 1122 — Requirements for Internet Hosts: Communication Layers](https://www.rfc-editor.org/rfc/rfc1122) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← MSB/LSB](./msb-lsb.md) · [Muerte por aserción →](./muerte-por-asercion.md)
