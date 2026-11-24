# Modelo predictivo

[↑ Glosario](../../README.md) · [← Modelo iterativo](./modelo-iterativo.md) · [Modelo sintáctico y semántico →](./modelo-sintactico-y-semantico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

El **modelo predictivo** organiza el trabajo en fases (analizar, diseñar, construir, probar, entregar) con alcance, coste y plazo comprometidos al inicio, y retroalimentación concentrada hacia el final ([SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md)). También se le llama en cascada o plan-driven. No es un sinónimo de «malo» ni de «obsoleto».

## Por qué importa

Es eficiente cuando lo desconocido es poco. Comprometer alcance, coste y plazo desde el inicio facilita la coordinación, los contratos y la planificación de dependencias. Cambia la decisión de cómo organizar un proyecto: no se elige un modelo por moda sino por la cantidad de incertidumbre del trabajo.

## Cómo funciona

En un modelo predictivo se analiza, diseña, construye, prueba y entrega en fases, con el alcance fijado al inicio. Su **fuerza es la coordinación**: todos saben qué se hará y las dependencias se resuelven en el papel (proveedores, fechas, contratos). Su **debilidad** está en el momento en que se descubre un malentendido: ocurre cuando alguien usa lo construido, y entonces todo lo hecho sobre ese malentendido se rehace. El costo de rehacer crece con lo construido encima, de modo que descubrirlo al final es lo más caro.

[SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md) subraya que el modelo **no es ingenuo ni obsoleto**: funciona donde el trabajo es conocido, los requisitos estables, las interfaces con terceros están acordadas y cambiar es caro. Por eso en la plataforma de entregas la integración con el sistema de calificaciones de secretaría, con fecha fija y proveedor externo, se planifica de forma predictiva con un contrato de interfaz acordado de antemano, mientras que la experiencia de entrega (alta incertidumbre) se construye en ciclos.

La clase lo contrasta con los otros dos modelos con un análisis de costos: lo que enseña no es el número sino la **forma** del costo. En el predictivo, el costo de un error de requisito crece con el avance; en el iterativo, se paga una sobrecarga por ciclo a cambio de errores más baratos. La decisión depende de cuánto desconocido hay.

## Ejemplo

Un contrato de interfaz con un proveedor de calificaciones: formatos, campos, plazos y pruebas de aceptación acordados al inicio, con fecha de entrega fija. Se analiza, se diseña la interfaz, se construye y se prueba contra el entorno del proveedor, y se entrega en la fecha. Cambiar el formato a mitad de camino sería caro, y por eso el contrato lo fija. (Ilustración del caso de [SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md).)

## Errores y confusiones comunes

- **Usarlo cuando hay mucha incertidumbre**: el malentendido se descubre tarde.
- **Considerarlo anticuado por definición.**
- **Comprometer alcance, coste y plazo sin margen para riesgos.**
- **Confundir predictivo con planificar**: todo modelo planifica; difiere cuánto se compromete y cuándo se revisa.

## Límites y cuándo no aplica

No aplica bien a productos nuevos con usuarios que no saben qué necesitan, ni a entornos donde los requisitos cambian durante el desarrollo. Los números del análisis de costos de [SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md) son supuestos del autor. En la práctica casi todos los proyectos mezclan modelos según la parte del trabajo.

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
