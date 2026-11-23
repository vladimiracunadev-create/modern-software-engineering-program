# Request ID

[↑ Glosario](../../README.md) · [← Reproyección](./reproyeccion.md) · [Requirements Engineer / Business Systems Analyst →](./requirements-engineer-business-systems-analyst.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Identificador de correlación de una operación.

Definición de trabajo de [SE-047 — Taller: seguir una petición de extremo a extremo](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md).

## Por qué importa

La clase donde se define, [SE-047 — Taller: seguir una petición de extremo a extremo](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md), existe con este propósito: la clase existe para reconstruir una petición extremo a extremo correlacionando DNS, transporte, TLS y HTTP.

## Cómo funciona

Según [SE-047 — Taller: seguir una petición de extremo a extremo](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md):

Nombre DNS, IP, MAC, socket, certificado, Host, request ID y usuario nombran entidades diferentes. El taller conecta cada identificador solo donde es válido. Una IP compartida por CDN no identifica un backend ni una persona.

Según [SE-047 — Taller: seguir una petición de extremo a extremo](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md):

La petición observable de extremo a extremo ejecuta una traza sintética cada cinco minutos desde dos redes. Ante fallo, guarda solo metadatos y los vincula a logs por request ID. El taller compara caso sano y degradado, calcula la primera divergencia y evita concluir desde diferencias posteriores que son consecuencias.

## Ejemplo

Ejemplo de [SE-047 — Taller: seguir una petición de extremo a extremo](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md) (sección «Ejemplo profesional»):

La petición observable de extremo a extremo ejecuta una traza sintética cada cinco minutos desde dos redes. Ante fallo, guarda solo metadatos y los vincula a logs por request ID. El taller compara caso sano y degradado, calcula la primera divergencia y evita concluir desde diferencias posteriores que son consecuencias.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-047 — Taller: seguir una petición de extremo a extremo](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md)) son:

- **Informe con una lista de errores sin ordenar** — causa: no se identificó la primera divergencia. Corrección: comparar con el caso sano y señalar la primera fase que difiere.
- **Eventos de componentes que no se pueden unir** — causa: falta un identificador propagado. Corrección: generar el ID en el borde, propagarlo y registrarlo en cada capa.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El laboratorio genera un `request_id`, lo propaga en una cabecera y lo registra en cada evento; la fase `correlation` del caso sano comprueba que el mismo valor aparece en cliente y servidor. ([SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Correlación](../c/correlacion.md), [Operación](../o/operacion.md).
- **Ver también:** [Identificador de correlación](../i/identificador-de-correlacion.md), [Alcance](../a/alcance.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md), [Incertidumbre](../i/incertidumbre.md), [Primera divergencia](../p/primera-divergencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-047 — Taller: seguir una petición de extremo a extremo](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md), [SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), [SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 1122 — Requirements for Internet Hosts: Communication Layers](https://www.rfc-editor.org/rfc/rfc1122) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Reproyección](./reproyeccion.md) · [Requirements Engineer / Business Systems Analyst →](./requirements-engineer-business-systems-analyst.md)
