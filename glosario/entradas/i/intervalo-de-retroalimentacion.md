# Intervalo de retroalimentación

[↑ Glosario](../../README.md) · [← Intervalo de confianza de Wilson](./intervalo-de-confianza-de-wilson.md) · [Intervalo de Wilson →](./intervalo-de-wilson.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Cantidad de trabajo construido entre dos momentos en que se contrasta con quien lo usará.

Definición de trabajo de [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md).

## Por qué importa

La clase donde se define, [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md), existe con este propósito: la clase existe para que elijas un modelo de proceso por lo que cuesta equivocarse y por cuándo te enteras, no por la moda: un plan predictivo, un ciclo iterativo y una entrega incremental responden a tres preguntas distintas y se pueden combinar.

## Cómo funciona

Según [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** el lanzamiento llega a la semana 14 de 12 porque el equipo rehace una quinta parte de las piezas. **Hipótesis rivales:** (a) el equipo estimó mal el esfuerzo de construir; (b) el equipo construyó con calidad insuficiente; (c) los malentendidos se descubrieron tarde. **Prueba:** separa el esfuerzo de construcción del de retrabajo y calcula cuántas piezas rehechas se habían construido antes de la primera demostración. **Conclusión:** la causa es el intervalo de retroalimentación, no la estimación. **Regresión:** fija un punto de contraste con las usuarias cada cuatro piezas y registra el retrabajo de la siguiente ejecución. No cambies a la vez el intervalo y el alcance.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md):

El equipo de la plataforma de entregas divide el lanzamiento en tres bloques. La integración con el sistema de calificaciones de la secretaría tiene fecha fija y proveedor externo: se planifica de forma predictiva, con un contrato de interfaz acordado de antemano. La experiencia de entrega y recuperación del borrador tiene alta incertidumbre sobre lo que las estudiantes necesitan: se construye en ciclos de dos semanas con revisión de las usuarias.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md)) son:

- **El proyecto «ágil» no libera nada utilizable hasta el último mes** — causa: se iteró sin entregar incrementos. Corrección: definir qué puede usar una persona al final de cada ciclo y liberarlo.
- **Los ciclos tienen tanta ceremonia que no queda tiempo para construir** — causa: sobrecoste por ciclo no medido. Corrección: medir las horas por ciclo y ajustar el intervalo hasta el mínimo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Conclusión:** la causa es el intervalo de retroalimentación, no la estimación. ([SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Trabajo](../t/trabajo.md), [Modelo incremental](../m/modelo-incremental.md), [Modelo iterativo](../m/modelo-iterativo.md), [Modelo predictivo](../m/modelo-predictivo.md), [Volatilidad](../v/volatilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-182](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md).

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

[↑ Glosario](../../README.md) · [← Intervalo de confianza de Wilson](./intervalo-de-confianza-de-wilson.md) · [Intervalo de Wilson →](./intervalo-de-wilson.md)
