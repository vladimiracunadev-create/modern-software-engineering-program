# Modelo iterativo

[↑ Glosario](../../README.md) · [← Modelo incremental](./modelo-incremental.md) · [Modelo predictivo →](./modelo-predictivo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Organización del trabajo en ciclos que repiten construir, mostrar y aprender para revisar la dirección.

Definición de trabajo de [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md).

## Por qué importa

En [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md), el tema «Modelo iterativo» importa porque repite ciclos para descubrir qué construir; paga una sobrecarga por ciclo a cambio de errores más baratos.

## Cómo funciona

Según [SE-181 — Modelos predictivos, iterativos e incrementales](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md), en la sección «Modelo iterativo»:

Iterar es repetir un ciclo completo de construir, mostrar y aprender, con la intención de revisar lo hecho. Boehm lo organizó alrededor del riesgo: cada vuelta ataca primero lo que más puede hacer fracasar el proyecto. El mecanismo económico es sencillo: el coste de rehacer una pieza malentendida crece con lo construido encima, de modo que descubrirlo después de cuatro piezas cuesta menos que después de cuarenta. La contrapartida es una sobrecarga por ciclo (preparar la demostración, reunir a las usuarias, decidir), de modo que existe un intervalo intermedio de menor esfuerzo total y no uno de «cuanto más corto, mejor».

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
