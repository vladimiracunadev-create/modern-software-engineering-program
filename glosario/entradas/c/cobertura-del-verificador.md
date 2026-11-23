# Cobertura del verificador

[↑ Glosario](../../README.md) · [← Cobertura del cambio](./cobertura-del-cambio.md) · [Cobertura estructural →](./cobertura-estructural.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Fracción de los criterios de la especificación que el verificador puede evaluar.

Definición de trabajo de [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md).

## Por qué importa

La clase donde se define, [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), existe con este propósito: la clase existe para que dejes de aceptar «terminé» como una medida.

## Cómo funciona

Según [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md):

Un agente verifica con lo que ve. Si su verificador cubre el 100 % de los criterios, su declaración es fiable aunque pueda tardar en llegar. Si cubre una fracción, los criterios que no ve nunca se corrigen, porque nadie sabe que están abiertos, y el agente declara convergencia cuando su parte visible está limpia. La consecuencia es contraintuitiva: cuanto peor es el verificador, **antes** declara convergencia, porque tiene menos que corregir. La declaración propia crece con la ceguera. Por eso la cobertura del verificador debe medirse, y por eso conviene que los criterios existan antes de implementar y sean ejecutables por una parte distinta del agente.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* convierte los diecisiete criterios de su especificación en pruebas ejecutables antes de que el agente implemente la primera tarea. Fija las condiciones de parada: máximo de seis pasadas, detener si los abiertos no bajan en dos pasadas seguidas, detener si una pasada reabre más de dos criterios y presupuesto de cómputo de tres horas. Tras la primera ejecución, el verificador encuentra siete criterios abiertos; el agente corrige cinco y rompe uno.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md)) son:

- **El agente dice haber terminado y la revisión encuentra incumplimientos** — causa: verificador del propio agente o con cobertura parcial. Corrección: criterios ejecutables previos y publicar la cobertura.
- **El bucle no acaba nunca** — causa: no hay condiciones de parada. Corrección: máximo de pasadas, sin progreso, presupuesto y regresión.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos; no se invocó ningún modelo, no se ejecutó `/speckit.converge` ni se observó ningún equipo o sistema reales. Las tasas de corrección y regresión, la independencia entre criterios, la cobertura del verificador y las diez variantes defectuosas son construcciones del autor, y los criterios completos se escribieron conociendo las variantes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Especificación](../e/especificacion.md), [Verificador](../v/verificador.md), [Condición de parada](./condicion-de-parada.md), [Convergencia](./convergencia.md), [Regresión](../r/regresion.md), [Variante defectuosa](../v/variante-defectuosa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Spec Kit — referencia del proceso agentic](https://github.github.io/spec-kit/reference/agentic-sdd.html) — implementar por fases y converger solo añadiendo tareas; autoridad: GitHub y mantenedores de la comunidad.
- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — verdad del entorno y condiciones de parada en bucles de agente; autoridad: Anthropic, artículo de ingeniería.
- [Jia y Harman](https://doi.org/10.1109/TSE.2010.62) — prueba de mutación como medida de la detección; autoridad: IEEE Transactions on Software Engineering.
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) — medir y gestionar el riesgo de sistemas de IA; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Cobertura del cambio](./cobertura-del-cambio.md) · [Cobertura estructural →](./cobertura-estructural.md)
