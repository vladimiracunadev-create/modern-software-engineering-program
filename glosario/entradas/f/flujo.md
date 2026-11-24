# Flujo

[↑ Glosario](../../README.md) · [← Fixture semántico común](./fixture-semantico-comun.md) · [Flujo asistido →](./flujo-asistido.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Un **flujo** (*stream*) es una secuencia de elementos procesada de uno en uno ([SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md)). El programa usa la palabra con matices:

- **En redes** ([SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md)): una secuencia ordenada de octetos sin fronteras de mensaje (TCP) o un canal lógico ordenado dentro de una conexión QUIC.
- **En programación** ([SE-067](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md), [SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md)): una secuencia de datos leída o escrita progresivamente, procesada por trozos sin retener el conjunto completo.
- **En estilos arquitectónicos** ([SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md)): el contrato de las tuberías y filtros.

## Por qué importa

La memoria de una versión en flujo no depende del volumen de entrada; la de un procesamiento por lotes crece con él ([SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md)). Con una entrada que se duplica, una versión por lotes puede quedarse sin memoria; una en flujo sigue funcionando. En redes, olvidar que un flujo de octetos no tiene fronteras de mensaje produce errores de lectura parcial.

## Cómo funciona

En el estilo de tuberías y filtros ([SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md)), un filtro recibe un flujo de elementos y emite otro. Si todos comparten esa forma, se conectan en cualquier orden que tenga sentido y cada uno se prueba con una lista pequeña. En el laboratorio, cada filtro es un generador de Python: `f_validate` deja pasar las filas válidas, `f_due` las que vencen en 72 horas o menos, `f_enrich` añade una etiqueta y `f_format` produce el texto; la cadena es `f_format(f_enrich(f_due(f_validate(filas))))`. El contrato uniforme compra reuso y sustitución de pasos sin editar los vecinos.

## Ejemplo

El equipo de *Avisos* migra un volcado nocturno a filtros y descubre dos cosas: el paso de ordenar por urgencia, añadido al final, retiene todo el lote y es el único que escala con el volumen; y una fila con código de curso nulo detenía toda la cadena de madrugada. Solución: ordenar solo dentro de cada curso (estado de tamaño acotado) y entregar el orden global como una consulta aparte. Ilustración:

```python
def f_due(filas):
    for f in filas:
        if f["horas"] <= 72: yield f
```

## Errores y confusiones comunes

- **Un paso que acumula todo el flujo.** Ordenar o agrupar sin límite rompe la promesa de memoria acotada ([SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md)).
- **Una fila inválida detiene todo.** Hace falta una política por elemento (descartar, registrar o apartar).
- **Suponer fronteras de mensaje en un flujo de octetos** ([SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md)).

## Límites y cuándo no aplica

El estilo comparte la forma (pasos encadenados) pero no necesariamente el contrato: en una canalización de integración continua, cada paso suele recibir artefactos completos, no un flujo de elementos ([SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md)). Los pasos con estado global (ordenar, agregar) obligan a retener datos y reintroducen el costo en memoria que el flujo evitaba.

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
