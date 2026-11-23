# Comandante del incidente

[↑ Glosario](../../README.md) · [← Color, texto y movimiento](./color-texto-y-movimiento.md) · [Comando →](./comando.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Persona que decide y prioriza durante el incidente sin operar.

Definición de trabajo de [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md).

## Por qué importa

La clase donde se define, [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), existe con este propósito: la clase existe para que coordines una respuesta en la que participan varias personas: quién decide, quién opera, quién comunica y quién escribe; cómo se declara y se clasifica un incidente; cada cuánto se informa y a quién; y cómo se miden los tiempos sin engañarse con un promedio.

## Cómo funciona

[SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo escribe el protocolo de incidentes de la API de entregas. Severidades: 1 (más del 10 % de las entregas falla o hay pérdida de datos), 2 (entre 1 % y 10 %), 3 (degradación sin pérdida visible), 4 (sin impacto externo). Las severidades 1 y 2 abren un canal propio con cuatro roles: comando, operaciones, comunicaciones y escriba, con suplentes asignados por rotación.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md)) son:

- **Veinte personas opinan y nadie decide** — causa: sin comandante ni roles. Corrección: asignar roles al declarar el incidente.
- **Quien arregla contesta preguntas** — causa: sin comunicaciones y sin cadencia. Corrección: rol de comunicaciones y actualizaciones periódicas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos. No se observó ningún incidente ni equipo real; los tiempos por tramo, el ruido de percepción de la severidad, la tasa de preguntas, los costes de 3 y 4 minutos y la independencia entre tramos son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Incidente](../i/incidente.md), [Cadencia de actualización](./cadencia-de-actualizacion.md), [Kappa de Cohen](../k/kappa-de-cohen.md), [Severidad](../s/severidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-500 — Gestión de incidentes y comunicación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

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

[↑ Glosario](../../README.md) · [← Color, texto y movimiento](./color-texto-y-movimiento.md) · [Comando →](./comando.md)
