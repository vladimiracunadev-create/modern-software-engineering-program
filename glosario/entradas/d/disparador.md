# Disparador

[↑ Glosario](../../README.md) · [← Diseño responsive](./diseno-responsive.md) · [Disparador de revisión →](./disparador-de-revision.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Condición medible sobre una señal, con umbral, ventana y responsable, que obliga a revisar el plan.

Definición de trabajo de [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md): Código que el motor ejecuta antes o después de un cambio y que puede rechazarlo.

## Por qué importa

En [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md), el tema «Disparadores» importa porque convierten una señal en una acción con responsable; sin umbral no son reglas.

## Cómo funciona

Según [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md), en la sección «Disparadores»:

Un disparador es una condición medible sobre una señal que obliga a revisar el plan: «el percentil 85 del pronóstico supera la fecha comprometida dos semanas seguidas». Tiene cuatro partes: la señal, el umbral, la ventana (cuántas observaciones o cuánto tiempo) y la acción con su responsable. Sin ventana, cualquier oscilación lo activa; sin responsable, nadie lo atiende; sin acción, es una alarma sin protocolo. Los disparadores se acuerdan al planificar, no cuando ya hay presión, y se revisan con las falsas alarmas que produjeron.

## Ejemplo

Ejemplo de [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma de entregas entrega el plan con ocho secciones. El objetivo es «lanzar la recuperación de borradores con la regla de penalización verificada en 22 semanas». Los supuestos son cuatro, con responsable y fecha. El rango comunicado es «entre 18 y 23 semanas con 85 % de confianza», calculado con 12 semanas de historia y calibrado como en `SE-191`. El disparador es «percentil 85 del pronóstico sobre el plazo durante dos semanas seguidas, con ventana de ocho semanas», elegido por tener unas 34 % de falsas alarmas y cinco semanas de retraso, que el equipo acepta con eso a la vista.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md)) son:

- **Nadie reacciona a la alarma de replanificación** — causa: regla sin ventana que alarma casi siempre. Corrección: exigir avisos seguidos, ampliar la ventana y medir las falsas alarmas.
- **El plan se rehace cada semana** — causa: se replanifica por cada oscilación. Corrección: replanificar solo cuando se cumple una regla fijada de antemano.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Los disparadores se acuerdan al planificar, no cuando ya hay presión, y se revisan con las falsas alarmas que produjeron. ([SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md))
- **un disparador sin ventana que alarma casi siempre y termina ignorado**. ([SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Motor](../m/motor.md), [Plan](../p/plan.md), [Señal](../s/senal.md), [Clave foránea](../c/clave-foranea.md), [Falsa alarma](../f/falsa-alarma.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-192 — Proyecto: plan adaptativo con evidencia y guardrails](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (31 clases más lo mencionan; las que más):

[SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md), [SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Disparadores».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SQLite: disparadores](https://www.sqlite.org/lang_createtrigger.html) — rechazo de operaciones con `RAISE`; autoridad: documentación oficial de SQLite.
- [Principios del Manifiesto Ágil](https://agilemanifesto.org/principles.html) — aceptar cambios y reflexionar a intervalos regulares; autoridad: autores del manifiesto.
- [Flyvbjerg, «From Nobel Prize to project management: getting risks right» (Project Management Journal, 2006)](https://doi.org/10.1177/875697280603700302) — optimismo en la planificación y clases de referencia; autoridad: Project Management Journal.
- [DORA: investigación](https://dora.dev/research/) — métricas de entrega y estabilidad; autoridad: DORA (Google Cloud).
- [Efron, «Bootstrap methods: another look at the jackknife» (The Annals of Statistics, 1979)](https://doi.org/10.1214/aos/1176344552) — remuestreo usado para el pronóstico; autoridad: The Annals of Statistics.

---

[↑ Glosario](../../README.md) · [← Diseño responsive](./diseno-responsive.md) · [Disparador de revisión →](./disparador-de-revision.md)
