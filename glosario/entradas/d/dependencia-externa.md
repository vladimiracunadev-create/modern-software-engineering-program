# Dependencia externa

[↑ Glosario](../../README.md) · [← Dependencia directa y transitiva](./dependencia-directa-y-transitiva.md) · [Dependencia funcional →](./dependencia-funcional.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Dependencia cuya fecha y calidad controla alguien ajeno al equipo.

Definición de trabajo de [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md).

## Por qué importa

En [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), el tema «Dependencias externas» importa porque cada una añade una probabilidad de espera; con varias, esperar es lo normal.

## Cómo funciona

Según [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), en la sección «Dependencias externas»:

Una dependencia externa es un elemento que no controlas: la entrega de otro equipo, una aprobación, un proveedor. Cada una tiene su propia probabilidad de llegar tarde y un retraso cuando lo hace. La probabilidad de que todas lleguen a tiempo es el producto de las individuales; con diez dependencias de 90 % de fiabilidad, es 35 %. El plan debe tratar la espera como el caso normal: pedir fechas de aviso, tener trabajo útil que hacer mientras se espera y reducir el número de dependencias en el camino crítico.

## Ejemplo

Ejemplo de [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma de entregas dibuja la red de la entrega: 15 elementos propios y cuatro dependencias externas. Calcula el camino crítico (10 días con medianas) y lo contrasta con la simulación que, como en la red de ancho 3 de la clase, da una media cercana a 14 y un percentil 85 cercano a 16: comunica «entre 12 y 16 días». De las cuatro dependencias externas, dos están en el camino crítico; para cada una acuerdan una fecha de aviso y una alternativa (un doble para identidad hasta que llegue la real; un interruptor para notificaciones).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md)) son:

- **El plan cumple todas las fechas parciales y falla la final** — causa: se sumaron fechas de caminos paralelos. Corrección: simular la red y comunicar un rango.
- **Siempre hay una dependencia «casi lista» que llega tarde** — causa: no se pidió fecha de aviso ni alternativa. Corrección: acordar con cada proveedor una fecha de aviso y un doble.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una dependencia externa es un elemento que no controlas: la entrega de otro equipo, una aprobación, un proveedor. ([SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-185](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](./dependencia.md), [Camino crítico](../c/camino-critico.md), [Holgura](../h/holgura.md), [Interruptor de función](../i/interruptor-de-funcion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

**También se usa en** (66 clases más lo mencionan; las que más):

[SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md), [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), [SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md), [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), [SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md), [SE-068](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md), [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Dependencias externas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Malcolm et al., «Application of a technique for research and development program evaluation» (Operations Research, 1959)](https://doi.org/10.1287/opre.7.5.646) — PERT y la incertidumbre en redes de actividades; autoridad: Operations Research.
- [Fowler, «Feature toggles»](https://martinfowler.com/articles/feature-toggles.html) — integrar trabajo incompleto sin exponerlo; autoridad: martinfowler.com.
- [The Scrum Guide](https://scrumguides.org/scrum-guide.html) — planificación y entrega de incrementos utilizables; autoridad: Scrum.org y Scrum Inc. (autores de la guía).
- [Boehm, «Software risk management: principles and practices» (IEEE Software, 1991)](https://doi.org/10.1109/52.62930) — identificar y priorizar riesgos de proyecto, incluidas las dependencias; autoridad: IEEE Software.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — gestión de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Dependencia directa y transitiva](./dependencia-directa-y-transitiva.md) · [Dependencia funcional →](./dependencia-funcional.md)
