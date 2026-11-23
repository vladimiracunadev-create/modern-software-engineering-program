# Interruptor de función

[↑ Glosario](../../README.md) · [← Interruptor de circuito](./interruptor-de-circuito.md) · [Interruptor del experimento →](./interruptor-del-experimento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Mecanismo que permite integrar y desplegar trabajo incompleto sin que sea visible o activo para las usuarias.

Definición de trabajo de [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md).

## Por qué importa

La clase donde se define, [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), existe con este propósito: la clase existe para que planifiques una entrega sabiendo qué la retrasa de verdad: los caminos que convergen, las dependencias que no controlas y el orden en que se hace el trabajo, y para que sepas qué puedes cambiar de cada una.

## Cómo funciona

[SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md):

El equipo de la plataforma de entregas dibuja la red de la entrega: 15 elementos propios y cuatro dependencias externas. Calcula el camino crítico (10 días con medianas) y lo contrasta con la simulación que, como en la red de ancho 3 de la clase, da una media cercana a 14 y un percentil 85 cercano a 16: comunica «entre 12 y 16 días».

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md)) son:

- **El plan cumple todas las fechas parciales y falla la final** — causa: se sumaron fechas de caminos paralelos. Corrección: simular la red y comunicar un rango.
- **Siempre hay una dependencia «casi lista» que llega tarde** — causa: no se pidió fecha de aviso ni alternativa. Corrección: acordar con cada proveedor una fecha de aviso y un doble.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se analizó ningún proyecto real: la forma de las redes, las duraciones, los riesgos de las dependencias y los valores son construcciones del autor. La siguiente clase convierte estas incertidumbres en riesgos, supuestos, problemas y decisiones con responsable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-185](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Activo](../a/activo.md), [Mecanismo](../m/mecanismo.md), [Trabajo](../t/trabajo.md), [Camino crítico](../c/camino-critico.md), [Dependencia](../d/dependencia.md), [Dependencia externa](../d/dependencia-externa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Malcolm et al., «Application of a technique for research and development program evaluation» (Operations Research, 1959)](https://doi.org/10.1287/opre.7.5.646) — PERT y la incertidumbre en redes de actividades; autoridad: Operations Research.
- [Fowler, «Feature toggles»](https://martinfowler.com/articles/feature-toggles.html) — integrar trabajo incompleto sin exponerlo; autoridad: martinfowler.com.
- [The Scrum Guide](https://scrumguides.org/scrum-guide.html) — planificación y entrega de incrementos utilizables; autoridad: Scrum.org y Scrum Inc. (autores de la guía).
- [Boehm, «Software risk management: principles and practices» (IEEE Software, 1991)](https://doi.org/10.1109/52.62930) — identificar y priorizar riesgos de proyecto, incluidas las dependencias; autoridad: IEEE Software.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — gestión de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Interruptor de circuito](./interruptor-de-circuito.md) · [Interruptor del experimento →](./interruptor-del-experimento.md)
