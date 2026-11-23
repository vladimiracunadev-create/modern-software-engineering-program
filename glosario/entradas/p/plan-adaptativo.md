# Plan adaptativo

[↑ Glosario](../../README.md) · [← Plan](./plan.md) · [Plan de ejecución →](./plan-de-ejecucion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Plan que declara sus supuestos, sus señales y las reglas con que se revisa, y que cambia por evidencia y no por presión.

Definición de trabajo de [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md).

## Por qué importa

La clase donde se define, [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md), existe con este propósito: el proyecto entrega un plan que cambia con la evidencia sin cambiar por capricho: dice qué se prometió, bajo qué supuestos, qué señales vigila, qué regla dispara la replanificación y qué barreras no se negocian, y demuestra con una simulación qué ganan y qué cuestan esas reglas.

## Cómo funciona

Según [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md):

Un plan adaptativo hace dos cosas distintas. Una es ordenar el trabajo por valor para que, si el tiempo se agota, lo entregado sea lo más valioso (`SE-186`). Otra es prometer según el pronóstico: comprometer solo el alcance que el rendimiento reciente respalda, de modo que lo prometido se cumpla. Combinarlas es lo habitual, pero conviene medirlas por separado, porque cada una resuelve un problema distinto —el valor entregado y la fiabilidad de lo prometido— y confundirlas lleva a atribuir a una lo que hizo la otra.

Según [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md):

Compara con el plan de la semana 9: el rendimiento se reduce a la mitad, el disparador se activa en la semana 13 y el equipo, en vez de discutir si «es real», ejecuta el protocolo: recorta funciones de menor valor, conserva las cuatro barreras y registra la decisión. Un plan adaptativo es adecuado cuando el cambio de plan ya estaba previsto en sus reglas; es una excusa cuando se cambia sin regla, o una promesa vacía cuando nadie la activa.

## Ejemplo

Ejemplo de [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md) (sección «Ejemplo profesional»):

Compara con el plan de la semana 9: el rendimiento se reduce a la mitad, el disparador se activa en la semana 13 y el equipo, en vez de discutir si «es real», ejecuta el protocolo: recorta funciones de menor valor, conserva las cuatro barreras y registra la decisión. Un plan adaptativo es adecuado cuando el cambio de plan ya estaba previsto en sus reglas; es una excusa cuando se cambia sin regla, o una promesa vacía cuando nadie la activa.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md)) son:

- **Nadie reacciona a la alarma de replanificación** — causa: regla sin ventana que alarma casi siempre. Corrección: exigir avisos seguidos, ampliar la ventana y medir las falsas alarmas.
- **El plan se rehace cada semana** — causa: se replanifica por cada oscilación. Corrección: replanificar solo cuando se cumple una regla fijada de antemano.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se planificó ningún proyecto real ni se observó una replanificación: el rendimiento gamma, la caída del rendimiento, el valor lognormal, las reglas de alcance y las doscientas mutaciones son construcciones del autor, y el validador se afinó con los mismos casos que lo evalúan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](../e/evidencia.md), [Plan](./plan.md), [Regla](../r/regla.md), [Supuestos](../s/supuestos.md), [Disparador](../d/disparador.md), [Falsa alarma](../f/falsa-alarma.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), [SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md).

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Principios del Manifiesto Ágil](https://agilemanifesto.org/principles.html) — aceptar cambios y reflexionar a intervalos regulares; autoridad: autores del manifiesto.
- [Flyvbjerg, «From Nobel Prize to project management: getting risks right» (Project Management Journal, 2006)](https://doi.org/10.1177/875697280603700302) — optimismo en la planificación y clases de referencia; autoridad: Project Management Journal.
- [DORA: investigación](https://dora.dev/research/) — métricas de entrega y estabilidad; autoridad: DORA (Google Cloud).
- [Efron, «Bootstrap methods: another look at the jackknife» (The Annals of Statistics, 1979)](https://doi.org/10.1214/aos/1176344552) — remuestreo usado para el pronóstico; autoridad: The Annals of Statistics.
- [Nygard, «Documenting architecture decisions» (2011)](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — registro de las decisiones de replanificación; autoridad: autor de la práctica.

---

[↑ Glosario](../../README.md) · [← Plan](./plan.md) · [Plan de ejecución →](./plan-de-ejecucion.md)
