# Integrador

[↑ Glosario](../../README.md) · [← Integración frecuente](./integracion-frecuente.md) · [Integridad referencial →](./integridad-referencial.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Quien fusiona las ramas y ejecuta la verificación.

Definición de trabajo de [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md).

## Por qué importa

En [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md), el tema «Integrador único» importa porque alguien decide el orden y resuelve los conflictos.

## Cómo funciona

Según [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md):

La fusión se hace de uno en uno por un integrador (una persona o un agente designado) con una regla fija: fusionar una rama, ejecutar el menú completo, y solo si pasa fusionar la siguiente. Si falla, se sabe qué rama lo rompió y el trabajo vuelve al coordinador con la traza. El integrador es también quien resuelve los conflictos, o quien decide devolver la rama a su autor: tener varios resolviendo conflictos con criterios distintos reproduce el problema original.

Según [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md):

El equipo prueba tres agentes en un refactor de módulos: uno sobre el paquete de fechas, otro sobre el de reportes y otro sobre las pruebas de integración. Define la propiedad por carpeta y un integrador. En la primera semana ocurren dos hechos. Dos veces un agente necesita un cambio en una carpeta ajena y lo pide al coordinador, que lo reparte; el costo es una espera. Una vez, la fusión de las carpetas de fechas y de reportes pasa limpia y el menú falla porque reportes usaba una función con una firma cambiada. El equipo mide que el trabajo tardó un poco menos que con un solo agente y que dedicó más tiempo a coordinar que a escribir.

## Ejemplo

Ejemplo de [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md) (sección «Ejemplo profesional»):

El equipo prueba tres agentes en un refactor de módulos: uno sobre el paquete de fechas, otro sobre el de reportes y otro sobre las pruebas de integración. Define la propiedad por carpeta y un integrador. En la primera semana ocurren dos hechos. Dos veces un agente necesita un cambio en una carpeta ajena y lo pide al coordinador, que lo reparte; el costo es una espera. Una vez, la fusión de las carpetas de fechas y de reportes pasa limpia y el menú falla porque reportes usaba una función con una firma cambiada.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La fusión se hace de uno en uno por un integrador (una persona o un agente designado) con una regla fija: fusionar una rama, ejecutar el menú completo, y solo si pasa fusionar la siguiente. ([SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Verificación](../v/verificacion.md).
- **Ver también:** [Árbol de trabajo](../a/arbol-de-trabajo.md), [Canal de coordinación](../c/canal-de-coordinacion.md), [Conflicto semántico](../c/conflicto-semantico.md), [Conflicto textual](../c/conflicto-textual.md), [Propiedad de archivos](../p/propiedad-de-archivos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (15 clases más lo mencionan; las que más):

[SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md), [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), [SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md), [SE-292](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md), [SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md).

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Integración frecuente](./integracion-frecuente.md) · [Integridad referencial →](./integridad-referencial.md)
