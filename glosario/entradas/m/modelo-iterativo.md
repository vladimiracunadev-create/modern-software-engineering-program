# Modelo iterativo

[↑ Glosario](../../README.md) · [← Modelo incremental](./modelo-incremental.md) · [Modelo predictivo →](./modelo-predictivo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

El **modelo iterativo** organiza el trabajo en ciclos que repiten construir, mostrar y aprender, con la intención de revisar la dirección ([SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md)). Cada ciclo produce algo que se muestra a quienes lo usarán y alimenta el siguiente. Se contrasta con el modelo predictivo (planificar todo, construir, entregar) y se distingue del incremental, que se centra en entregar el producto en partes.

## Por qué importa

Cambia cómo se descubre lo que hay que construir. Cuando hay incertidumbre sobre lo que las personas necesitan, descubrir un malentendido pronto es mucho más barato que descubrirlo tarde. A cambio se paga una sobrecarga por ciclo. [SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md) enseña a elegir el ritmo y a aplicar el enfoque donde la incertidumbre lo justifica.

## Cómo funciona

Iterar es repetir un ciclo completo de construir, mostrar y aprender. [SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md) cita a Boehm, que organizó el modelo alrededor del **riesgo**: cada vuelta ataca primero lo que más puede hacer fracasar el proyecto. El mecanismo económico es sencillo: el coste de rehacer una pieza malentendida crece con lo construido encima, de modo que descubrirlo después de cuatro piezas cuesta menos que después de cuarenta.

La contrapartida es una **sobrecarga por ciclo** (preparar la demostración, reunir a las usuarias, decidir). Con ciclos muy cortos domina la sobrecarga; con ciclos muy largos domina el coste de errores tardíos. Existe, entonces, un intervalo intermedio de menor esfuerzo total; la clase lo explora con un modelo y propone medir las horas por ciclo para ajustar el intervalo hasta el mínimo. Un segundo criterio es el tipo de trabajo: lo que tiene fecha fija, proveedor externo y requisitos conocidos se planifica de forma predictiva; lo que tiene alta incertidumbre se construye en ciclos.

## Ejemplo

[SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md) divide el lanzamiento de la plataforma de entregas en tres bloques. La integración con el sistema de calificaciones de la secretaría tiene fecha fija y proveedor externo: se planifica de forma predictiva, con un contrato de interfaz acordado de antemano. La experiencia de entrega y recuperación del borrador tiene alta incertidumbre sobre lo que las estudiantes necesitan: se construye en ciclos de dos semanas con revisión de las usuarias. Un mismo proyecto mezcla ambos enfoques según la incertidumbre de cada parte.

## Errores y confusiones comunes

- **Proyecto «ágil» que no libera nada utilizable hasta el último mes**: se iteró sin entregar incrementos; corrección: definir qué puede usar una persona al final de cada ciclo y liberarlo.
- **Ceremonia que consume el ciclo**: sobrecoste no medido; corrección: medir horas por ciclo y ajustar.
- **Confundir iterar con repetir lo mismo**: cada ciclo debe cambiar algo por lo aprendido.
- **Confundir iterativo con incremental**: iterar revisa la dirección; el incremento añade partes.

## Límites y cuándo no aplica

No conviene cuando la revisión no puede ocurrir (no hay usuarias accesibles para mostrar), cuando el costo de cada ciclo es muy alto (hardware que se fabrica) o cuando los requisitos son estables y conocidos. Iterar sin mostrar ni aprender es solo reordenar el trabajo. Las cifras del modelo de [SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md) son hipótesis del autor, no mediciones de equipos reales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ciclo](../c/ciclo.md), [Organización](../o/organizacion.md), [Trabajo](../t/trabajo.md), [Intervalo de retroalimentación](../i/intervalo-de-retroalimentacion.md), [Modelo incremental](./modelo-incremental.md), [Modelo predictivo](./modelo-predictivo.md).
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

[↑ Glosario](../../README.md) · [← Modelo incremental](./modelo-incremental.md) · [Modelo predictivo →](./modelo-predictivo.md)
