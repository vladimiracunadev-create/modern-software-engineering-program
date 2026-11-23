# Integración frecuente

[↑ Glosario](../../README.md) · [← Integración continua](./integracion-continua.md) · [Integrador →](./integrador.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Fusión de los cambios de cada persona en la línea principal en intervalos cortos, para que las diferencias se detecten mientras son pequeñas.

Definición de trabajo de [SE-182 — Agile como principios y no como ceremonia](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md).

## Por qué importa

En [SE-182 — Agile como principios y no como ceremonia](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md), el tema «Disciplina técnica» importa porque entregar seguido exige integración frecuente, pruebas y ramas cortas; sin ellas el ciclo corto se rompe.

## Cómo funciona

Según [SE-182 — Agile como principios y no como ceremonia](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md):

El manifiesto pide atención continua a la excelencia técnica por una razón económica: si cada entrega requiere dos semanas de estabilización, el ciclo corto es imposible. La integración frecuente, las pruebas automatizadas y las ramas cortas mantienen bajo el coste de cada ciclo. Una rama que vive diez días acumula cambios de varias personas que se solapan, y el conflicto no es una molestia sino una señal de que dos entendimientos del mismo código divergieron. Fowler describe el patrón «Flaccid Scrum»: un equipo adopta la gestión de proyectos y omite las prácticas técnicas, con lo que la velocidad inicial cae pronto por deuda acumulada.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-182 — Agile como principios y no como ceremonia](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md):

El equipo de la plataforma de entregas revisa sus prácticas con una tabla de cuatro columnas: principio, práctica, decisión que cambió la última vez y señal observable. La demostración quincenal ya no es interna: invita a dos profesoras y tres estudiantes distintas cada vez, con una versión desplegada que pueden usar. La retrospectiva exige que cada acción tenga persona responsable y una señal de comprobación. La reunión diaria se acorta a un tablero asíncrono porque nadie había cambiado una decisión gracias a ella en tres semanas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Las ramas viven semanas y la integración final se llama «cierre»** — causa: no hay integración frecuente. Corrección: limitar la vida de una rama a un día y esconder el trabajo incompleto tras un interruptor. ([SE-182](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md))
- **La velocidad cae tras seis meses de «buena gestión»** — causa: se adoptó la gestión sin prácticas técnicas. Corrección: añadir pruebas automáticas, integración frecuente y refactorización continuas. ([SE-182](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-182 — Agile como principios y no como ceremonia](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió a ningún equipo ni se observó una demostración real: el modelo de aprendizaje, las horas de ceremonia y los cambios en un archivo son construcciones del autor. La siguiente clase compara cuatro marcos concretos con este criterio.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Fusión](../f/fusion.md), [Intervalo](./intervalo.md), [Principal](../p/principal.md), [Ceremonia ritual](../c/ceremonia-ritual.md), [Práctica](../p/practica.md), [Principio ágil](../p/principio-agil.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-182 — Agile como principios y no como ceremonia](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), [SE-002](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md), [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «Continuous Integration»](https://martinfowler.com/articles/continuousIntegration.html) — integración frecuente y sus condiciones; autoridad: martinfowler.com.
- [Manifiesto por el Desarrollo Ágil de Software](https://agilemanifesto.org/) — valores declarados por sus autores; autoridad: autores del manifiesto.
- [Principios del Manifiesto Ágil](https://agilemanifesto.org/principles.html) — los doce principios; autoridad: autores del manifiesto.
- [Fowler, «The new methodology»](https://martinfowler.com/articles/newMethodology.html) — procesos adaptativos y disciplina técnica; autoridad: martinfowler.com.
- [Fowler, «Flaccid Scrum»](https://martinfowler.com/bliki/FlaccidScrum.html) — adopción de la gestión sin prácticas técnicas; autoridad: martinfowler.com.

---

[↑ Glosario](../../README.md) · [← Integración continua](./integracion-continua.md) · [Integrador →](./integrador.md)
