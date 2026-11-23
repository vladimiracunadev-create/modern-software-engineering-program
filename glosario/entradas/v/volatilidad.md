# Volatilidad

[↑ Glosario](../../README.md) · [← Vocabulario controlado](./vocabulario-controlado.md) · [Volumen →](./volumen.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Proporción de lo planificado que cambia o se revela mal entendido antes de entregarse.

Definición de trabajo de [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md).

## Por qué importa

En [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md), el tema «Volatilidad» importa porque es la variable que decide el cruce: cuánto de lo planificado cambiará antes de entregarse.

## Cómo funciona

Según [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md):

La volatilidad es la proporción de lo planificado que cambiará o se revelará mal entendido antes de entregarse. No se conoce al inicio, pero se puede estimar con proyectos anteriores y se puede reducir con prototipos. El coste de cambiar, en cambio, es una propiedad del sistema: en uno con pruebas automáticas, integración continua y despliegue frecuente, rehacer cuesta poco; en uno con hardware o contratos cerrados, cuesta mucho. Un modelo se elige por el producto de ambos: volatilidad alta con cambio barato favorece ciclos cortos; volatilidad baja con cambio caro favorece planificar más.

Según [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md):

Traslada el experimento a otro dominio (por ejemplo, la migración de un sistema de reservas con comportamiento conocido): cambia la volatilidad y el coste de cambiar, y conserva el procedimiento de medir esfuerzo por intervalo y valor ante un corte. La transferencia está lograda cuando puedes explicar qué parte del método dependía del dominio y cuál no, no cuando el código se parece.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md):

El equipo de la plataforma de entregas divide el lanzamiento en tres bloques. La integración con el sistema de calificaciones de la secretaría tiene fecha fija y proveedor externo: se planifica de forma predictiva, con un contrato de interfaz acordado de antemano. La experiencia de entrega y recuperación del borrador tiene alta incertidumbre sobre lo que las estudiantes necesitan: se construye en ciclos de dos semanas con revisión de las usuarias.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un plan predictivo se rehace por completo a mitad de camino** — causa: volatilidad subestimada al elegir el modelo. Corrección: estimar la volatilidad con proyectos previos y planificar revisiones. ([SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Lo que enseña no es el número sino la forma: el coste del modelo predictivo crece linealmente con la volatilidad y el del iterativo apenas. ([SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Intervalo de retroalimentación](../i/intervalo-de-retroalimentacion.md), [Modelo incremental](../m/modelo-incremental.md), [Modelo iterativo](../m/modelo-iterativo.md), [Modelo predictivo](../m/modelo-predictivo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Boehm, «A spiral model of software development and enhancement» (IEEE Computer, 1988)](https://doi.org/10.1109/2.59) — modelo de proceso guiado por riesgo; autoridad: IEEE Computer.
- [Larman y Basili, «Iterative and incremental developments: a brief history» (IEEE Computer, 2003)](https://doi.org/10.1109/MC.2003.1204375) — historia de las prácticas iterativas e incrementales; autoridad: IEEE Computer.
- [Flyvbjerg, «From Nobel Prize to project management: getting risks right» (Project Management Journal, 2006)](https://doi.org/10.1177/875697280603700302) — sesgo de optimismo en la planificación de proyectos; autoridad: Project Management Journal.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — procesos de ingeniería de software; autoridad: IEEE Computer Society.
- [Manifiesto por el Desarrollo Ágil de Software](https://agilemanifesto.org/) — valores que motivan las prácticas iterativas actuales; autoridad: autores del manifiesto.

---

[↑ Glosario](../../README.md) · [← Vocabulario controlado](./vocabulario-controlado.md) · [Volumen →](./volumen.md)
