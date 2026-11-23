# NAT

[↑ Glosario](../../README.md) · [← Narrativa y verificación](./narrativa-y-verificacion.md) · [Navegación facetada →](./navegacion-facetada.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Traducción de direcciones entre dominios.

Definición de trabajo de [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md).

## Por qué importa

La clase donde se define, [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md), existe con este propósito: la clase existe para decidir entrega directa o por gateway usando prefijos, rutas y traducción de direcciones.

## Cómo funciona

Según [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md):

RFC 1918 reserva bloques sin significado global. NAT modifica direcciones y, en NAPT, puertos, manteniendo estado temporal. Conserva escaso espacio público y permite topologías privadas, pero no es una política de autorización ni cifrado; rompe parte de la transparencia extremo a extremo.

Según [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md):

No. Es una dirección no enrutable en Internet, pero dentro de la red privada es alcanzable por cualquier equipo, y el NAT no es un cortafuegos. La seguridad se obtiene con filtrado y autenticación, no por el rango de la dirección.

## Ejemplo

Ejemplo de [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md) (sección «Preguntas frecuentes»):

No. Es una dirección no enrutable en Internet, pero dentro de la red privada es alcanzable por cualquier equipo, y el NAT no es un cortafuegos. La seguridad se obtiene con filtrado y autenticación, no por el rango de la dirección.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md)) son:

- **Un equipo alcanza Internet pero no a un vecino** — causa: máscara mal configurada: el vecino parece estar en otra red. Corrección: comparar prefijo y dirección con `ipaddress` y corregir la máscara.
- **Suponer que `is_private` equivale a «de mi red»** — causa: la misma dirección privada existe en muchas redes. Corrección: identificar equipos con nombres y credenciales, no con la dirección.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La ausencia de NAT no implica exposición automática: el filtrado y las rutas siguen gobernando alcanzabilidad. ([SE-039](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dominio](../d/dominio.md), [Traducción](../t/traduccion.md), [Alcance](../a/alcance.md), [CIDR](../c/cidr.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md).
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

[↑ Glosario](../../README.md) · [← Narrativa y verificación](./narrativa-y-verificacion.md) · [Navegación facetada →](./navegacion-facetada.md)
