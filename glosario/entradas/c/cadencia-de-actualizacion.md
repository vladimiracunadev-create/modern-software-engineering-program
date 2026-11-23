# Cadencia de actualización

[↑ Glosario](../../README.md) · [← Cadena de respuesta](./cadena-de-respuesta.md) · [Caducidad →](./caducidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Intervalo anunciado en el que se informa del estado, haya o no novedades.

Definición de trabajo de [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md).

## Por qué importa

La clase donde se define, [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), existe con este propósito: la clase existe para que coordines una respuesta en la que participan varias personas: quién decide, quién opera, quién comunica y quién escribe; cómo se declara y se clasifica un incidente; cada cuánto se informa y a quién; y cómo se miden los tiempos sin engañarse con un promedio.

## Cómo funciona

Según [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), en la sección «Cadencia de actualizaciones»:

Se simulan 1 500 incidentes de duración lognormal (mediana de 90 minutos). Las preguntas de las partes interesadas llegan con una tasa que crece con la antigüedad de la última noticia (0,05 por minuto, multiplicada por 1 + antigüedad/15 minutos). Cada pregunta cuesta 3 minutos de quien dirige y cada actualización, 4.

**Cómo leer la figura.** Cada barra es una política de actualizaciones de estado y su largo los minutos que la persona al mando gasta por incidente respondiendo preguntas; entre paréntesis van las preguntas que recibe. Sin cadencia recibe más preguntas y gasta más tiempo; actualizar cada 30 minutos es lo que menos gasta y actualizar cada 5 minutos, con 21,1 actualizaciones por incidente, sube el gasto a 102,9 minutos, más que no actualizar. **Dónde deja de valer:** la tasa de preguntas que crece con la antigüedad y los costes de 3 y 4 minutos son supuestos del autor; no se midió ningún incidente.

## Ejemplo

Caso medido en la sección «Cadencia de actualizaciones» de [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md):

Se simulan 1 500 incidentes de duración lognormal (mediana de 90 minutos). Las preguntas de las partes interesadas llegan con una tasa que crece con la antigüedad de la última noticia (0,05 por minuto, multiplicada por 1 + antigüedad/15 minutos). Cada pregunta cuesta 3 minutos de quien dirige y cada actualización, 4.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md)) son:

- **Veinte personas opinan y nadie decide** — causa: sin comandante ni roles. Corrección: asignar roles al declarar el incidente.
- **Quien arregla contesta preguntas** — causa: sin comunicaciones y sin cadencia. Corrección: rol de comunicaciones y actualizaciones periódicas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos. No se observó ningún incidente ni equipo real; los tiempos por tramo, el ruido de percepción de la severidad, la tasa de preguntas, los costes de 3 y 4 minutos y la independencia entre tramos son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Intervalo](../i/intervalo.md), [Comandante del incidente](./comandante-del-incidente.md), [Incidente](../i/incidente.md), [Kappa de Cohen](../k/kappa-de-cohen.md), [Severidad](../s/severidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Managing Incidents](https://sre.google/sre-book/managing-incidents/) — roles y gestión de incidentes; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE Workbook: Incident Response](https://sre.google/workbook/incident-response/) — casos de respuesta y ensayo de roles; autoridad: Google, SRE Workbook.
- [PagerDuty Incident Response](https://response.pagerduty.com/) — roles y comunicación; autoridad: documentación pública de PagerDuty.
- [Atlassian Incident Management Handbook](https://www.atlassian.com/incident-management/handbook) — ciclo de vida y comunicación; autoridad: documentación pública de Atlassian.
- [Cohen, «A coefficient of agreement for nominal scales»](https://doi.org/10.1177/001316446002000104) — kappa de Cohen; autoridad: Educational and Psychological Measurement, 1960.

---

[↑ Glosario](../../README.md) · [← Cadena de respuesta](./cadena-de-respuesta.md) · [Caducidad →](./caducidad.md)
