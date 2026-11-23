# Flujo

[↑ Glosario](../../README.md) · [← Fixture semántico común](./fixture-semantico-comun.md) · [Flujo asistido →](./flujo-asistido.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Secuencia de elementos procesada de uno en uno.

Definición de trabajo de [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md): Secuencia ordenada de octetos sin fronteras de mensaje.
- En [SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md): Canal lógico ordenado dentro de una conexión QUIC.
- En [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md): Secuencia de datos leída o escrita progresivamente.
- En [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md): Secuencia de datos procesada por trozos sin retener el conjunto completo.

## Por qué importa

En [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md), el tema «Flujo frente a lotes» importa porque decide si la memoria depende o no del volumen.

## Cómo funciona

Según [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md):

Un filtro recibe un flujo de elementos y emite otro. Si todos los filtros comparten esa forma, se conectan en cualquier orden que tenga sentido y cada uno se prueba con una lista pequeña. En el laboratorio, cada filtro es un generador de Python: `f_validate` deja pasar las filas válidas, `f_due` las que vencen en 72 horas o menos, `f_enrich` añade una etiqueta y `f_format` produce el texto del aviso. La cadena completa es la composición `f_format(f_enrich(f_due(f_validate(filas))))`. El contrato uniforme es la propiedad que el estilo compra: reuso y sustitución de pasos sin editar los vecinos.

Según [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md):

El equipo de *Avisos* migra el volcado nocturno a una cadena de filtros. Al ponerla en producción descubre dos cosas. La primera: el paso de ordenar los avisos por urgencia, que alguien añadió al final «para que salgan ordenados», retiene todo el lote y es el único que escala con el volumen. Tras discutirlo se decide ordenar solo dentro de cada curso (un filtro con estado, pero de tamaño acotado por el número de entregas de un curso) y entregar el orden global como una consulta aparte. La segunda: una fila con un código de curso nulo detenía la cadena entera a las tres de la mañana.

## Ejemplo

Ejemplo de [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* migra el volcado nocturno a una cadena de filtros. Al ponerla en producción descubre dos cosas. La primera: el paso de ordenar los avisos por urgencia, que alguien añadió al final «para que salgan ordenados», retiene todo el lote y es el único que escala con el volumen. Tras discutirlo se decide ordenar solo dentro de cada curso (un filtro con estado, pero de tamaño acotado por el número de entregas de un curso) y entregar el orden global como una consulta aparte. La segunda: una fila con un código de curso nulo detenía la cadena entera a las tres de la mañana.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La memoria de la versión en flujo no depende del volumen de entrada; la de los lotes crece con él, y por eso el millón de la matrícula la rompió. ([SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md))
- Comparte la forma (pasos encadenados) pero no necesariamente el contrato: en una canalización de CI cada paso suele recibir artefactos completos, no un flujo de elementos. ([SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-039](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Frontera](./frontera.md), [Secuencia](../s/secuencia.md), [Trozo](../t/trozo.md), [Alcance](../a/alcance.md), [Contrato](../c/contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (198 clases más lo mencionan; las que más):

[SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md), [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md), [SE-080](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md), [SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md), [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md), [SE-550](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «stream».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 768 — User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9000 — QUIC](https://www.rfc-editor.org/rfc/rfc9000) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [Python Tutorial — Input and Output](https://docs.python.org/3/tutorial/inputoutput.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python `json` documentation](https://docs.python.org/3/library/json.html) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Fixture semántico común](./fixture-semantico-comun.md) · [Flujo asistido →](./flujo-asistido.md)
