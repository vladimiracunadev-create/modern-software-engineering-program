# Consecuencia negativa

[↑ Glosario](../../README.md) · [← Consecuencia](./consecuencia.md) · [Consenso →](./consenso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Costo o limitación que la decisión acepta, declarada por quien decide.

Definición de trabajo de [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md).

## Por qué importa

En [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md), el tema «Consecuencias negativas» importa porque revela lo que se acepta perder.

## Cómo funciona

Según [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md):

Se definieron once criterios que un analizador puede comprobar: siete secciones presentes (contexto, decisión, alternativas consideradas, consecuencias, reversibilidad, disparador de revisión y evidencia) y cuatro propiedades de contenido (al menos dos alternativas, cada una con su motivo de descarte; al menos una consecuencia negativa declarada; algún criterio medible, es decir, un número con su unidad; y un disparador de revisión con un número). Se aplicaron a tres registros de ejemplo. El ADR-A (monolito modular con extracción del módulo de avisos si el p99 supera 200 ms) cumplió 11 de 11. El ADR-B («Usar microservicios… porque son la mejor práctica») cumplió 3 de 11: tiene contexto, decisión y consecuencias, pero ninguna alternativa, ninguna consecuencia negativa, ningún número, reversibilidad, disparador ni evidencia.

Según [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md):

Un año después de la decisión, la persona nueva del equipo de *Avisos* propone separar el cálculo en un servicio. La líder abre el ADR y la conversación cambia: el disparador de p99 no se ha cumplido (el máximo del año es 171 ms), pero el número de equipos es ahora cinco, y el registro decía que con más de tres equipos la coordinación supera el umbral. La discusión deja de ser «monolito o servicios» y pasa a ser «la consecuencia negativa que aceptamos se materializó».

## Ejemplo

Ejemplo de [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md) (sección «Ejemplo profesional»):

Un año después de la decisión, la persona nueva del equipo de *Avisos* propone separar el cálculo en un servicio. La líder abre el ADR y la conversación cambia: el disparador de p99 no se ha cumplido (el máximo del año es 171 ms), pero el número de equipos es ahora cinco, y el registro decía que con más de tres equipos la coordinación supera el umbral. La discusión deja de ser «monolito o servicios» y pasa a ser «la consecuencia negativa que aceptamos se materializó».

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Lo importante es que la revisión incluya a alguien que no la propuso, que es quien encuentra las consecuencias negativas que faltan. ([SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](./costo.md), [ADR](../a/adr.md), [Deriva arquitectónica](../d/deriva-arquitectonica.md), [Disparador de revisión](../d/disparador-de-revision.md), [Evidencia](../e/evidencia.md), [Función de aptitud](../f/funcion-de-aptitud.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-513](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Consecuencias negativas».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Consecuencia](./consecuencia.md) · [Consenso →](./consenso.md)
