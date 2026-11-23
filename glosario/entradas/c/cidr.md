# CIDR

[↑ Glosario](../../README.md) · [← Ciclo de vida](./ciclo-de-vida.md) · [Cifra etiquetada →](./cifra-etiquetada.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Notación y asignación basada en prefijos de longitud variable.

Definición de trabajo de [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md).

## Por qué importa

La clase donde se define, [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md), existe con este propósito: la clase existe para decidir entrega directa o por gateway usando prefijos, rutas y traducción de direcciones.

## Cómo funciona

[SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Estas definiciones son operativas: precisan el uso dentro de la petición observable de extremo a extremo y deben leerse junto a las fuentes. No convierten un término histórico o dependiente de implementación en una garantía universal.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md):

La petición observable de extremo a extremo conserva un inventario redactado de dirección, prefijo, gateway y ruta elegida. Cuando la VPN anuncia `10.0.0.0/8` y la red local usa `10.20.30.0/24`, verifica la coincidencia más específica y documenta el conflicto. La solución puede ser renumerar, dividir rutas o cambiar política; desactivar todo el túnel solo oculta el diseño.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md)) son:

- **Un equipo alcanza Internet pero no a un vecino** — causa: máscara mal configurada: el vecino parece estar en otra red. Corrección: comparar prefijo y dirección con `ipaddress` y corregir la máscara.
- **Suponer que `is_private` equivale a «de mi red»** — causa: la misma dirección privada existe en muchas redes. Corrección: identificar equipos con nombres y credenciales, no con la dirección.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md)) son: Estas definiciones son operativas: precisan el uso dentro de la petición observable de extremo a extremo y deben leerse junto a las fuentes. No convierten un término histórico o dependiente de implementación en una garantía universal. No cubre protocolos de enrutamiento entre organizaciones ni diseño avanzado de direcciones. NAT puede variar por implementación. La siguiente clase estudia el contrato de transporte sobre IP.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Prefijo](../p/prefijo.md), [Alcance](../a/alcance.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md), [MTU](../m/mtu.md), [NAT](../n/nat.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-368](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 8200 — Internet Protocol, Version 6](https://www.rfc-editor.org/rfc/rfc8200) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 1918 — Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 3022 — Traditional IP Network Address Translator](https://www.rfc-editor.org/rfc/rfc3022) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 1122 — Requirements for Internet Hosts: Communication Layers](https://www.rfc-editor.org/rfc/rfc1122) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Ciclo de vida](./ciclo-de-vida.md) · [Cifra etiquetada →](./cifra-etiquetada.md)
