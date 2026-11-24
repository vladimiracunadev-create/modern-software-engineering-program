# Dependencia externa

[↑ Glosario](../../README.md) · [← Dependencia directa y transitiva](./dependencia-directa-y-transitiva.md) · [Dependencia funcional →](./dependencia-funcional.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Una **dependencia externa** es una dependencia cuya fecha y calidad controla alguien ajeno al equipo ([SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md)): la entrega de otro equipo, una aprobación, un proveedor. Se opone a la dependencia interna, que el equipo puede reordenar o acelerar.

## Por qué importa

Cada dependencia externa añade una probabilidad de espera, y con varias, esperar es lo normal. Un plan que supone que todas llegan a tiempo es optimista por construcción. Cambia cómo se planifica: la espera se trata como el caso habitual y se diseña el trabajo para seguir avanzando mientras llega.

## Cómo funciona

[SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) da la cuenta: la probabilidad de que **todas** las dependencias lleguen a tiempo es el **producto** de las individuales. Con diez dependencias de 90 % de fiabilidad cada una, la probabilidad conjunta es 0,9¹⁰ ≈ 35 %. Por eso un plan con muchas dependencias externas casi siempre se retrasa en alguna.

Dos prácticas lo mitigan. Primero, **pedir una fecha de aviso** a cada proveedor (cuándo sabrán si llegan tarde) y acordar una alternativa o un doble; la clase pide acordar con cada proveedor una fecha de aviso. Segundo, **tener trabajo útil que hacer mientras se espera**, dividiendo el trabajo para que avance sin la dependencia, con un contrato de interfaz acordado de antemano o un doble.

En el análisis de la red, las dependencias externas que están en el **camino crítico** son las que más importan: un retraso allí retrasa la entrega. En el ejemplo de [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), el equipo de la plataforma dibuja la red de la entrega con 15 elementos propios y cuatro dependencias externas; calcula el camino crítico (10 días con medianas) y lo contrasta con la simulación, que da una media cercana a 14 y un percentil 85 cercano a 16: comunica «entre 12 y 16 días». De las cuatro externas, dos están en el camino crítico, y para cada una acuerdan una fecha de aviso.

## Ejemplo

Un plan necesita la API de calificaciones de secretaría, una aprobación legal y la nueva versión de una biblioteca. Con 90 %, 80 % y 95 % de probabilidad de llegar a tiempo, la probabilidad conjunta es 0,9 × 0,8 × 0,95 ≈ 68 %. Si además dos están en el camino crítico, el plazo prometido debe incluir ese riesgo. (Cifras ilustrativas con el cálculo de [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md).)

## Errores y confusiones comunes

- **El plan cumple las fechas parciales y falla la final**: se sumaron fechas de caminos paralelos; corrección: simular la red y comunicar un rango.
- **Siempre hay una dependencia «casi lista» que llega tarde**: no se pidió fecha de aviso ni alternativa; corrección: acordar fecha de aviso y un doble.
- **Suponer independencia entre dependencias** cuando comparten un proveedor.
- **No tener trabajo alternativo mientras se espera.**

## Límites y cuándo no aplica

La cuenta supone independencia entre dependencias; si dos dependen del mismo proveedor, el riesgo se correlaciona. Las probabilidades individuales son estimaciones. Las dependencias externas contractuales (con penalizaciones) se gestionan de otro modo que las informales.

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
