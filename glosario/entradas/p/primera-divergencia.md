# Primera divergencia

[↑ Glosario](../../README.md) · [← Primer éxito](./primer-exito.md) · [Primera respuesta / resolución →](./primera-respuesta-resolucion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

La **primera divergencia** es el primer punto donde un caso sano y uno afectado dejan de coincidir ([SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md), [SE-058](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md)). [SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md) precisa el método: se comparan trazas sana y afectada desde el mismo inicio y se localiza el primer estado distinto, no el último error. Es una técnica de diagnóstico, no un tipo de fallo.

## Por qué importa

El último error visible suele ser consecuencia, no causa. Buscar desde el final lleva a arreglar síntomas; buscar desde el primer punto en que algo difiere reduce las hipótesis causales. [SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md) lo resume: las diferencias posteriores pueden ser consecuencias y no deben optimizarse primero. Cambia el orden en que se investiga y qué se corrige.

## Cómo funciona

El procedimiento ([SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md), [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md)):

1. Obtener una traza del caso **sano** y otra del **afectado**, con el mismo inicio y condiciones comparables.
2. Alinearlas paso a paso desde el principio.
3. Señalar la **primera fase o estado** donde difieren.
4. Formular hipótesis solo sobre ese punto y sus causas inmediatas.

La causa de que funcione es la causalidad temporal: lo que ocurre antes de la divergencia es idéntico en ambos casos, así que no puede explicar la diferencia; lo que ocurre después puede ser un efecto en cascada. En el laboratorio de [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md), cada fila de la figura va de un escenario a su primera divergencia respecto del caso sano y a su resultado (correcto, fallido o recuperado). [SE-058](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md) la usa para comparar dos recorridos de un algoritmo.

## Ejemplo

Traza sana: resolución DNS, conexión TCP, handshake TLS, petición, respuesta. Traza afectada: resolución DNS, conexión TCP, fallo del handshake TLS. La primera divergencia está en el handshake; el error final «no se pudo cargar la página» es solo el último eslabón. Ilustración:

```python
for i, (a, b) in enumerate(zip(traza_sana, traza_afectada)):
    if a != b:
        print("primera divergencia en el paso", i, a, b); break
```

## Errores y confusiones comunes

- **Informe con una lista de errores sin ordenar.** Causa: no se identificó la primera divergencia; corrección: comparar con el caso sano y señalar la primera fase que difiere ([SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md)).
- **Optimizar las diferencias posteriores** ([SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md)).
- **Comparar trazas con condiciones distintas.** La divergencia puede deberse a la entrada, no al fallo.

## Límites y cuándo no aplica

Requiere un caso sano comparable: si no existe, hay que construirlo o usar una referencia. En sistemas no deterministas, dos trazas sanas ya pueden diferir, y hay que descartar esas diferencias antes. Y el laboratorio de [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md) modela DNS, TLS y pérdida de forma determinista: demuestra el método, no el comportamiento de una red real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Evento](../e/evento.md), [Traza](../t/traza.md), [Alcance](../a/alcance.md), [Diagnóstico](../d/diagnostico.md), [Dominio](../d/dominio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-047 — Taller: seguir una petición de extremo a extremo](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-058 — Resolución sistemática y registro de hipótesis](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-105 — Reproducción de errores y reducción de casos](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

**También se usa en** (26 clases más lo mencionan; las que más):

[SE-098](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md), [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md), [SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), [SE-039](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md), [SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md), [SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md), [SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md), [SE-043](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Language Server Protocol 3.18](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/) — Mensajes, capacidades y sincronización entre editor y servidor; autoridad: Microsoft.
- [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) — Breakpoints, frames, variables y negociación de capacidades; autoridad: Microsoft.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Pdb, cprofile, timeit, tracemalloc y límites instrumentales; autoridad: Python Software Foundation.
- [Python venv](https://docs.python.org/3/library/venv.html) — Aislamiento de intérprete, scripts y entorno virtual; autoridad: Python Software Foundation.
- [Development Container Specification](https://containers.dev/implementors/spec/) — Configuración reproducible de herramientas y ciclo de vida del contenedor; autoridad: Dev Container Specification maintainers.

---

[↑ Glosario](../../README.md) · [← Primer éxito](./primer-exito.md) · [Primera respuesta / resolución →](./primera-respuesta-resolucion.md)
