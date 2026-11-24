# Disparador

[↑ Glosario](../../README.md) · [← Diseño responsive](./diseno-responsive.md) · [Disparador de revisión →](./disparador-de-revision.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Un **disparador** es una condición medible sobre una señal, con umbral, ventana y responsable, que obliga a revisar el plan ([SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md)). [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md) usa la palabra en otro sentido, de bases de datos: código que el motor ejecuta antes o después de un cambio y que puede rechazarlo (*trigger*). Esta entrada desarrolla el primero y señala el segundo.

## Por qué importa

Convierte una señal en una acción con responsable. Un plan sin disparadores se revisa por costumbre o por pánico; con ellos, se revisa cuando una regla acordada de antemano lo exige. Cambia la gestión del plan: se pasa de reaccionar a cada oscilación a replanificar solo cuando hay una razón escrita.

## Cómo funciona

[SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md) da un ejemplo: «el percentil 85 del pronóstico supera la fecha comprometida dos semanas seguidas». Un disparador tiene **cuatro partes**:

- la **señal** (qué se mide, aquí el percentil 85 del pronóstico);
- el **umbral** (cuándo es preocupante, aquí superar la fecha comprometida);
- la **ventana** (cuántas observaciones o cuánto tiempo, aquí dos semanas seguidas);
- la **acción con su responsable** (revisar el plan, y quién).

La clase explica por qué cada parte es necesaria: sin ventana, cualquier oscilación lo activa; sin responsable, nadie lo atiende; sin acción, es una alarma sin protocolo. La ventana es lo que controla las **falsas alarmas**: si cada semana hay una probabilidad independiente de 5 % de activarse sin motivo, en 20 semanas la probabilidad de al menos una falsa alarma es 1 − 0,95²⁰ ≈ 64 %, más de la mitad. Una regla sin ventana que alarma casi siempre acaba ignorada.

En el plan de la plataforma de entregas, el objetivo es «lanzar la recuperación de borradores con la regla de penalización verificada en 22 semanas», los supuestos son cuatro con responsable y fecha, el rango comunicado es «entre 18 y 23 semanas con 85 % de confianza», y el disparador es el anterior. En [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), el sentido de base de datos comparte la idea de condición que ejecuta una acción, pero la ejecuta el motor automáticamente.

## Ejemplo

Disparador: «si el rendimiento de las últimas cuatro semanas baja por debajo de cierto valor, el responsable del plan convoca una revisión en 48 horas». Señal: rendimiento semanal; umbral: valor fijado; ventana: cuatro semanas; acción: convocar revisión; responsable: quien lleva el plan. Si baja una semana, no hace nada; si baja cuatro seguidas, se revisa. (Estructura ilustrativa derivada de [SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md).)

## Errores y confusiones comunes

- **Nadie reacciona a la alarma de replanificación**: la regla no tiene ventana y alarma casi siempre; corrección: exigir avisos seguidos, ampliar la ventana y medir falsas alarmas.
- **El plan se rehace cada semana**: se replanifica por cada oscilación.
- **Disparador sin responsable.**
- **Confundirlo con un trigger de base de datos.**

## Límites y cuándo no aplica

Un disparador solo detecta lo que se midió; una causa no medida no lo activa. Las ventanas largas retrasan la reacción: equilibrar falsas alarmas y detección tardía es una decisión de riesgo. Y los umbrales deben revisarse con la experiencia del proyecto.

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
