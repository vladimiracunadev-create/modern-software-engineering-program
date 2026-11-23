# Punto de captura

[↑ Glosario](../../README.md) · [← Punto ciego](./punto-ciego.md) · [Punto de código →](./punto-de-codigo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Ubicación e interfaz desde la que se observa tráfico.

Definición de trabajo de [SE-046 — Captura, medición y diagnóstico de tráfico](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md).

## Por qué importa

La clase donde se define, [SE-046 — Captura, medición y diagnóstico de tráfico](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md), existe con este propósito: la clase existe para capturar y medir tráfico con una pregunta previa y distinguir ausencia de evidencia de evidencia de ausencia.

## Cómo funciona

[SE-046 — Captura, medición y diagnóstico de tráfico](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Estas definiciones son operativas: precisan el uso dentro de la petición observable de extremo a extremo y deben leerse junto a las fuentes. No convierten un término histórico o dependiente de implementación en una garantía universal.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-046 — Captura, medición y diagnóstico de tráfico](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md):

La petición observable de extremo a extremo define un presupuesto de 800 ms: 100 DNS, 100 conexión/TLS, 400 procesamiento y 200 transferencia. La traza de incidente usa un ID, zona horaria, reloj monotónico local y ventana de dos minutos. Solo si la fase rompe presupuesto se solicita evidencia más invasiva.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-046 — Captura, medición y diagnóstico de tráfico](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md)) son:

- **Concluir una mejora con una sola medición** — causa: se ignora la variación entre ejecuciones. Corrección: repetir y comparar medianas y rangos.
- **Reportar solo el mejor valor** — causa: sesgo de selección. Corrección: conservar todas las muestras y resumir con mediana y rango.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-046 — Captura, medición y diagnóstico de tráfico](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md)) son: Estas definiciones son operativas: precisan el uso dentro de la petición observable de extremo a extremo y deben leerse junto a las fuentes. No convierten un término histórico o dependiente de implementación en una garantía universal. Cifrado impide leer payload y eso es una propiedad deseable. Capturas no sustituyen telemetría de aplicación. La siguiente clase integra las señales siguiendo una petición completa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-045](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Interfaz](../i/interfaz.md), [Alcance](../a/alcance.md), [Correlación](../c/correlacion.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md), [Latencia](../l/latencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-046 — Captura, medición y diagnóstico de tráfico](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 1122 — Requirements for Internet Hosts: Communication Layers](https://www.rfc-editor.org/rfc/rfc1122) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Punto ciego](./punto-ciego.md) · [Punto de código →](./punto-de-codigo.md)
