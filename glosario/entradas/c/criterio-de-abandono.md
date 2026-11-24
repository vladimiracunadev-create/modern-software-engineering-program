# Criterio de abandono

[↑ Glosario](../../README.md) · [← Crisis del software](./crisis-del-software.md) · [Criterio de aborto →](./criterio-de-aborto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Un **criterio de abandono** es una condición medible, fijada de antemano, que obliga a detener una iniciativa ([SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md)).

## Por qué importa

Una reescritura sin forma de pararla se convierte en compromiso irreversible por inercia. [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md) propone que la conclusión de un análisis no sea «reescribir» ni «evolucionar» sino una **opción con salida**: se decide con indicadores, y se acuerda de antemano cuándo se corta.

## Cómo funciona

Si se elige reescribir, se hace de forma incremental ([SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md)) para que cada rebanada entregue valor y pueda detenerse; se fijan criterios de abandono, como el porcentaje de alcance cubierto o la desviación acumulada del presupuesto; y se define quién tiene autoridad para parar, sin que parar se considere un fracaso personal. Si se elige evolucionar, se fijan indicadores (costo por cambio, tiempo de ciclo, incidencias) que revisan la decisión si no mejoran en un plazo.

## Ejemplo

[SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md) (escenario hipotético): el equipo convierte las propuestas en parámetros. Del historial de la empresa obtiene que la última reescritura costó 1,8 veces su presupuesto y duró 1,5 veces lo previsto; mide el crecimiento del costo del módulo (9 % anual) y la deriva por peticiones al módulo antiguo; ejecuta una simulación con análisis de sensibilidad. Un criterio sería, por ejemplo, abandonar si el gasto acumulado excede una proporción fijada del presupuesto antes de cubrir cierto alcance.

## Errores y confusiones comunes

**No hay forma de parar la reescritura.** Sin criterios de abandono ni dueño; fijar criterios y quién puede aplicarlos.

## Límites y cuándo no aplica

Un criterio solo sirve si se mide con datos reales y alguien con autoridad lo aplica. Cifras como las de la clase son del escenario, no valores universales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](./condicion.md), [Análisis de sensibilidad](../a/analisis-de-sensibilidad.md), [Costo acumulado](./costo-acumulado.md), [Deriva del alcance](../d/deriva-del-alcance.md), [Horizonte de equilibrio](../h/horizonte-de-equilibrio.md), [Sensibilidad](../s/sensibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), [SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md), [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-142](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Spolsky, «Things You Should Never Do, Part I»](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) — argumento contra reescribir desde cero; autoridad: ensayo de un autor reconocido, de opinión.
- [Brooks, «No Silver Bullet»](https://doi.org/10.1109/MC.1987.1663532) — complejidad esencial y accidental; autoridad: IEEE Computer, 1987.
- [Lehman, «Programs, life cycles, and laws of software evolution»](https://doi.org/10.1109/PROC.1980.11805) — evolución de sistemas en uso; autoridad: Proceedings of the IEEE, 1980.
- [Fowler, «TechnicalDebt»](https://martinfowler.com/bliki/TechnicalDebt.html) — principal e intereses; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Crisis del software](./crisis-del-software.md) · [Criterio de aborto →](./criterio-de-aborto.md)
