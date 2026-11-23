# Retraso de detección

[↑ Glosario](../../README.md) · [← Retorno](./retorno.md) · [Retraso de etiquetas →](./retraso-de-etiquetas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Tiempo entre el cambio real y la activación del disparador.

Definición de trabajo de [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md).

## Por qué importa

La clase donde se define, [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md), existe con este propósito: el proyecto entrega un plan que cambia con la evidencia sin cambiar por capricho: dice qué se prometió, bajo qué supuestos, qué señales vigila, qué regla dispara la replanificación y qué barreras no se negocian, y demuestra con una simulación qué ganan y qué cuestan esas reglas.

## Cómo funciona

[SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md):

El equipo de la plataforma de entregas entrega el plan con ocho secciones. El objetivo es «lanzar la recuperación de borradores con la regla de penalización verificada en 22 semanas». Los supuestos son cuatro, con responsable y fecha. El rango comunicado es «entre 18 y 23 semanas con 85 % de confianza», calculado con 12 semanas de historia y calibrado como en `SE-191`.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md)) son:

- **Nadie reacciona a la alarma de replanificación** — causa: regla sin ventana que alarma casi siempre. Corrección: exigir avisos seguidos, ampliar la ventana y medir las falsas alarmas.
- **El plan se rehace cada semana** — causa: se replanifica por cada oscilación. Corrección: replanificar solo cuando se cumple una regla fijada de antemano.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se planificó ningún proyecto real ni se observó una replanificación: el rendimiento gamma, la caída del rendimiento, el valor lognormal, las reglas de alcance y las doscientas mutaciones son construcciones del autor, y el validador se afinó con los mismos casos que lo evalúan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Activación](../a/activacion.md), [Disparador](../d/disparador.md), [Falsa alarma](../f/falsa-alarma.md), [Guardrail](../g/guardrail.md), [Guardrail o barrera](../g/guardrail-o-barrera.md), [Plan adaptativo](../p/plan-adaptativo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md).

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

[↑ Glosario](../../README.md) · [← Retorno](./retorno.md) · [Retraso de etiquetas →](./retraso-de-etiquetas.md)
