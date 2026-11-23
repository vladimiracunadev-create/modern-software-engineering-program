# Camino crítico

[↑ Glosario](../../README.md) · [← Camino a producción](./camino-a-produccion.md) · [Camino dorado →](./camino-dorado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Secuencia de elementos dependientes de mayor duración; define la duración mínima de la entrega si las duraciones fueran las supuestas.

Definición de trabajo de [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md): Cadena de dependencias de mayor duración acumulada, que fija la duración mínima.
- En [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md): Cadena de requisitos dependientes de mayor duración acumulada, que fija el mínimo de tiempo con recursos ilimitados.
- En [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md): Cadena de dependencias cuya suma de duraciones fija el tiempo mínimo de aplicar el conjunto.
- En [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md): Secuencia de llamadas de la que depende la respuesta al usuario.

## Por qué importa

En [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), el tema «Camino crítico» importa porque identifica qué retrasos retrasan la entrega; no cuántas veces ocurrirá.

## Cómo funciona

Según [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), en la sección «Camino crítico»:

El camino crítico es la secuencia de elementos dependientes más larga: cualquier retraso en uno de ellos retrasa la entrega. Calcularlo con duraciones típicas es útil para saber dónde mirar, y engañoso si se toma como duración esperada. Con duraciones inciertas, otros caminos casi tan largos también pueden convertirse en críticos en una parte de las ejecuciones. La noción útil es la probabilidad de que un elemento sea crítico, y no su etiqueta determinista.

## Ejemplo

Ejemplo de [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la duración de una red pequeña con camino crítico de 6 días. Antes de ejecutarlo, predice cuánto vale la duración si el elemento C tarda 1 día más.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Todo el equipo espera a la misma entrega externa** — causa: el camino crítico pasa por una dependencia. Corrección: dividir el trabajo para que avance sin ella, con un contrato o un doble. ([SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md))
- **La canalización no baja de un mínimo al añadir ejecutores** — causa: el camino crítico ya está alcanzado. Corrección: calcular el camino crítico y acortar su eslabón más largo. ([SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md))
- **El plan supone que todo es secuencial** — causa: las dependencias no están declaradas. Corrección: escribir el grafo y calcular el camino crítico. ([SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El camino crítico es la secuencia de elementos dependientes más larga: cualquier retraso en uno de ellos retrasa la entrega. ([SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md))
- **comprometer el plazo del camino crítico determinista en una red ancha**. ([SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](./conjunto.md), [Dependencia](../d/dependencia.md), [Recurso](../r/recurso.md), [Secuencia](../s/secuencia.md), [Contenido de una especificación](./contenido-de-una-especificacion.md), [Decisión de entrega](../d/decision-de-entrega.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-402 — Infraestructura como código y estado](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md).

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md).

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

[↑ Glosario](../../README.md) · [← Camino a producción](./camino-a-produccion.md) · [Camino dorado →](./camino-dorado.md)
