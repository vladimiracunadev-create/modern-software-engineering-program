# Modelo incremental

[↑ Glosario](../../README.md) · [← Modelo generativo](./modelo-generativo.md) · [Modelo iterativo →](./modelo-iterativo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Organización del trabajo en partes utilizables que se liberan en un orden elegido por valor y riesgo.

Definición de trabajo de [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md).

## Por qué importa

En [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md), el tema «Modelo incremental» importa porque libera partes utilizables en orden de valor; protege lo entregado si el proyecto se corta.

## Cómo funciona

Según [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md), en la sección «Modelo incremental»:

Un incremento es una parte que se puede usar, no una capa técnica sin valor propio. Construir incrementalmente significa ordenar el trabajo de manera que cada entrega sea utilizable y que las primeras aporten la mayor parte del valor. Su efecto más visible aparece cuando el proyecto se interrumpe: un recorte presupuestario, una reorganización o un cambio de prioridades. Con una liberación única el valor entregado es cero hasta el último día; con incrementos es el acumulado hasta el corte. Iterativo e incremental son ortogonales: se puede iterar sin liberar nada y se puede liberar por partes sin revisar la dirección.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md):

El equipo de la plataforma de entregas divide el lanzamiento en tres bloques. La integración con el sistema de calificaciones de la secretaría tiene fecha fija y proveedor externo: se planifica de forma predictiva, con un contrato de interfaz acordado de antemano. La experiencia de entrega y recuperación del borrador tiene alta incertidumbre sobre lo que las estudiantes necesitan: se construye en ciclos de dos semanas con revisión de las usuarias.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md)) son:

- **El proyecto «ágil» no libera nada utilizable hasta el último mes** — causa: se iteró sin entregar incrementos. Corrección: definir qué puede usar una persona al final de cada ciclo y liberarlo.
- **Los ciclos tienen tanta ceremonia que no queda tiempo para construir** — causa: sobrecoste por ciclo no medido. Corrección: medir las horas por ciclo y ajustar el intervalo hasta el mínimo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió a ningún equipo ni producto: los porcentajes de malentendidos, el coste por ciclo y los valores de las funciones son construcciones del autor. La siguiente clase pregunta qué principios sostienen esa elección cuando se quita la ceremonia.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Organización](../o/organizacion.md), [Riesgo](../r/riesgo.md), [Trabajo](../t/trabajo.md), [Valor](../v/valor.md), [Intervalo de retroalimentación](../i/intervalo-de-retroalimentacion.md), [Modelo iterativo](./modelo-iterativo.md).
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

[↑ Glosario](../../README.md) · [← Modelo generativo](./modelo-generativo.md) · [Modelo iterativo →](./modelo-iterativo.md)
