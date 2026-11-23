# Driver arquitectónico

[↑ Glosario](../../README.md) · [← Drenaje](./drenaje.md) · [Dry-run →](./dry-run.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Fuerza de negocio, de contexto o técnica que condiciona la estructura del sistema y que debe poder escribirse como una frase verificable.

Definición de trabajo de [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md).

## Por qué importa

La clase donde se define, [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), existe con este propósito: la clase existe para que conviertas «necesitamos una buena arquitectura» en drivers, restricciones y escenarios de calidad que se puedan medir, y para que sepas qué decisiones fuerzan y cuáles solo reflejan una preferencia.

## Cómo funciona

[SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

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
- **Ver también:** [Contextos](../c/contextos.md), [Estructura](../e/estructura.md), [Fuerza](../f/fuerza.md), [Causa común](../c/causa-comun.md), [Dominancia](./dominancia.md), [Escenario de calidad](../e/escenario-de-calidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-325 — Drivers, restricciones y atributos de arquitectura](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

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

[↑ Glosario](../../README.md) · [← Drenaje](./drenaje.md) · [Dry-run →](./dry-run.md)
