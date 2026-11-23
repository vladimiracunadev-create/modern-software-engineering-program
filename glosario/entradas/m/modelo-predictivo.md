# Modelo predictivo

[↑ Glosario](../../README.md) · [← Modelo iterativo](./modelo-iterativo.md) · [Modelo sintáctico y semántico →](./modelo-sintactico-y-semantico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Organización del trabajo en fases con alcance, coste y plazo comprometidos al inicio, y retroalimentación concentrada hacia el final.

Definición de trabajo de [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md).

## Por qué importa

En [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md), el tema «Modelo predictivo» importa porque compromete alcance, coste y plazo al inicio; es eficiente cuando lo desconocido es poco.

## Cómo funciona

Según [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md), en la sección «Modelo predictivo»:

En un modelo predictivo se analiza, diseña, construye, prueba y entrega en fases con alcance fijado al inicio. Su fuerza es la coordinación: todos saben qué se hará y las dependencias se resuelven en el papel. Su debilidad es el momento en que se descubre un malentendido, que ocurre cuando alguien usa lo construido, y entonces todo lo hecho sobre ese malentendido se rehace. El modelo no es ingenuo ni obsoleto: funciona bien donde los requisitos son estables y la validación es temprana por otras vías, por ejemplo cuando se reconstruye un sistema cuyo comportamiento ya se conoce. Falla cuando el desconocimiento es el problema, no la ejecución.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md):

El equipo de la plataforma de entregas divide el lanzamiento en tres bloques. La integración con el sistema de calificaciones de la secretaría tiene fecha fija y proveedor externo: se planifica de forma predictiva, con un contrato de interfaz acordado de antemano. La experiencia de entrega y recuperación del borrador tiene alta incertidumbre sobre lo que las estudiantes necesitan: se construye en ciclos de dos semanas con revisión de las usuarias.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md)) son:

- **El proyecto «ágil» no libera nada utilizable hasta el último mes** — causa: se iteró sin entregar incrementos. Corrección: definir qué puede usar una persona al final de cada ciclo y liberarlo.
- **Los ciclos tienen tanta ceremonia que no queda tiempo para construir** — causa: sobrecoste por ciclo no medido. Corrección: medir las horas por ciclo y ajustar el intervalo hasta el mínimo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Lo que enseña no es el número sino la forma: el coste del modelo predictivo crece linealmente con la volatilidad y el del iterativo apenas. ([SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Organización](../o/organizacion.md), [Plazo](../p/plazo.md), [Retroalimentación](../r/retroalimentacion.md), [Intervalo de retroalimentación](../i/intervalo-de-retroalimentacion.md), [Modelo incremental](./modelo-incremental.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), [SE-182](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md).

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

[↑ Glosario](../../README.md) · [← Modelo iterativo](./modelo-iterativo.md) · [Modelo sintáctico y semántico →](./modelo-sintactico-y-semantico.md)
