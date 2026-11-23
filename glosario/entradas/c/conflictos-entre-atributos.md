# Conflictos entre atributos

[↑ Glosario](../../README.md) · [← Conflicto textual](./conflicto-textual.md) · [Conformidad →](./conformidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Casi toda táctica mejora un atributo y empeora otro: replicar mejora la disponibilidad y complica la consistencia; guardar en caché mejora la latencia y complica la frescura; separar en servicios mejora la autonomía y añade latencia de red y operación. Por eso un conjunto de requisitos casi siempre no tiene una solución que gane en todo: tiene una frontera de alternativas que no se dominan entre sí. La decisión consiste en elegir un punto de esa frontera y escribir lo que se sacrificó.

Explicación de la sección «Conflictos entre atributos» de [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md).

## Por qué importa

En [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), el tema «Conflictos entre atributos» importa porque mejorar uno cuesta otro; hay que elegir cuál sacrificar.

En [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), el tema «Conflictos entre atributos» importa porque mejorar uno suele empeorar otro; decidirlo antes evita sorpresas en producción.

## Cómo funciona

Según [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), en la sección «Conflictos entre atributos»:

Casi toda táctica mejora un atributo y empeora otro: replicar mejora la disponibilidad y complica la consistencia; guardar en caché mejora la latencia y complica la frescura; separar en servicios mejora la autonomía y añade latencia de red y operación. Por eso un conjunto de requisitos casi siempre no tiene una solución que gane en todo: tiene una frontera de alternativas que no se dominan entre sí. La decisión consiste en elegir un punto de esa frontera y escribir lo que se sacrificó. Si la decisión no nombra lo sacrificado, aún no se ha tomado.

Según [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), en la sección «Conflictos entre atributos»:

Los atributos compiten por los mismos recursos. Más validación de las entregas mejora la seguridad y la fiabilidad y añade latencia; más réplicas mejoran la disponibilidad y cuestan consistencia o dinero; cifrar mejora la confidencialidad y obliga a gestionar claves; una interfaz más sencilla puede resultar menos flexible. Un **árbol de utilidad** ordena los escenarios por importancia para el negocio y por dificultad técnica, y obliga a escribir cuál se sacrifica cuando chocan. Decidirlo antes tiene un valor concreto: durante un incidente nadie debería descubrir, discutiendo, que la disponibilidad y la consistencia no podían ser ambas prioridad uno. La decisión debe quedar escrita con su fecha, su dueño y la condición que la revisaría.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md):

El equipo de la plataforma abre `drivers.md` con cuatro drivers (el pico de entrega no debe perder archivos; el servicio se apoya en seis personas; las notas deben ser consistentes; el servicio debe estar disponible en periodo de entregas), tres restricciones (infraestructura de la universidad, datos en el país, Python como lenguaje) y cinco escenarios medibles.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md)) son:

- **La discusión de arquitectura no termina** — causa: no hay escenarios con medida que comparar. Corrección: escribir escenarios con las seis partes y priorizarlos.
- **Se elige «microservicios» y el rendimiento no mejora** — causa: la causa del rendimiento era la capacidad o un cuello de botella, no la partición. Corrección: medir la capacidad contra el pico antes de cambiar la estructura.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna plataforma, base de datos ni red: los tiempos de servicio, las llegadas, las disponibilidades, la causa común y los candidatos son construcciones del autor. La siguiente clase mira el mismo sistema desde varias vistas y comprueba que no se contradigan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Característica de calidad](./caracteristica-de-calidad.md), [Causa común](./causa-comun.md), [Dominancia](../d/dominancia.md), [Driver arquitectónico](../d/driver-arquitectonico.md), [Escenario de calidad](../e/escenario-de-calidad.md), [Indicador](../i/indicador.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — modelo de calidad del producto de software; autoridad: ISO.
- [SEI, «The Architecture Tradeoff Analysis Method»](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) — escenarios de calidad y árbol de utilidad; autoridad: Software Engineering Institute (Carnegie Mellon).
- [Google SRE, «Embracing Risk»](https://sre.google/sre-book/embracing-risk/) — disponibilidad como objetivo con coste; autoridad: Google SRE.
- [Python: `heapq`](https://docs.python.org/3/library/heapq.html) — cola de prioridad usada en la simulación; autoridad: documentación de Python.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Conflicto textual](./conflicto-textual.md) · [Conformidad →](./conformidad.md)
