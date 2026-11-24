# Camino crítico

[↑ Glosario](../../README.md) · [← Camino a producción](./camino-a-produccion.md) · [Camino dorado →](./camino-dorado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

El **camino crítico** es la secuencia de elementos dependientes de mayor duración acumulada: fija la duración mínima de la entrega si las duraciones fueran las supuestas. Es el sentido de [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md). Las clases lo reutilizan con el mismo núcleo en otros grafos: la cadena de requisitos dependientes ([SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md)), la cadena de jobs de una canalización ([SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md)), la cadena de dependencias al aplicar infraestructura como código ([SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md)) y, en [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), la secuencia de llamadas de la que depende la respuesta al usuario.

## Por qué importa

Dice dónde mirar. Cualquier retraso en un elemento del camino crítico retrasa la entrega; un retraso fuera de él, dentro de su holgura, no. Cambia la decisión de dónde poner a la gente, qué dependencia externa atacar primero y qué optimizar: acelerar un eslabón que no es crítico no acorta nada.

## Cómo funciona

El cálculo es el recorrido del grafo de dependencias sumando duraciones y quedándose con la cadena más larga; la suma es la duración mínima con recursos ilimitados ([SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md)). La consecuencia práctica es que añadir recursos tiene un piso: en una canalización, añadir ejecutores no baja de un mínimo porque el camino crítico ya está alcanzado ([SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md)); hay que acortar su eslabón más largo.

[SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) añade el matiz decisivo: calcularlo con duraciones típicas sirve para saber dónde mirar, y engaña si se toma como duración esperada. Con duraciones inciertas, otros caminos casi tan largos también se vuelven críticos en una parte de las ejecuciones. La noción útil es la **probabilidad de que un elemento sea crítico**, no su etiqueta determinista. En una red ancha, comprometer el plazo del camino crítico determinista subestima el riesgo.

## Ejemplo

[SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) incluye un fragmento que calcula la duración de una red pequeña cuyo camino crítico es de 6 días, y pide predecir antes de ejecutar cuánto vale la duración si el elemento C tarda un día más. La respuesta depende de si C está en el camino crítico: si lo está, la entrega se mueve un día; si tiene holgura, puede no moverse. El ejercicio entrena justo esa lectura.

## Errores y confusiones comunes

- **Todo el equipo espera la misma entrega externa.** El camino crítico pasa por una dependencia; corrección de [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md): dividir el trabajo para que avance sin ella, con un contrato o un doble.
- **El plan supone que todo es secuencial.** Las dependencias no están declaradas; escribir el grafo y calcular ([SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md)).
- **Esperar que más recursos acorten siempre.** No bajan del camino crítico ([SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md)).
- **Tratarlo como duración esperada.** Es un mínimo bajo supuestos, no un pronóstico.

## Límites y cuándo no aplica

Presupone que las dependencias están completas y que las duraciones son las supuestas; con incertidumbre alta, o redes anchas con muchos caminos casi iguales, la etiqueta determinista pierde valor y conviene simular y hablar de probabilidad de ser crítico. Tampoco modela restricciones de recursos compartidos: el cálculo habla de recursos ilimitados. Y no dice nada sobre la calidad o el valor de lo que se entrega, solo sobre el tiempo.

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
