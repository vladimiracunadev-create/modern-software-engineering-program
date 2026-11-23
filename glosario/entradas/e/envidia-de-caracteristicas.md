# Envidia de características

[↑ Glosario](../../README.md) · [← Envenenamiento](./envenenamiento.md) · [Envoltorio de enteros →](./envoltorio-de-enteros.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Método que usa más datos de otro objeto que de su propia clase.

Definición de trabajo de [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md).

## Por qué importa

En [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), el tema «Envidia de características y acoplamiento» importa porque señala responsabilidades mal ubicadas, con excepciones legítimas.

## Cómo funciona

Según [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md):

Un método tiene envidia de características cuando usa más datos de otro objeto que los de su propia clase: probablemente pertenece al otro objeto. El indicador es sencillo de medir y tiene excepciones por oficio: serializadores, formateadores, visitantes y adaptadores existen para leer los campos de otros. La excepción no invalida el indicador; obliga a mirar el papel del método. Mover un método sin ese examen empeora la ubicación de las responsabilidades.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md):

El equipo no reduce el reporte a cero: lo clasifica. Para cada una de las doce funciones señaladas anota tres cosas en una tabla: si es lógica o datos, cuántas veces cambió en el último año según `git log` y quién la toca.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md)) son:

- **El tablero baja a cero y el código no mejora** — causa: se optimizó la métrica y no el costo del cambio. Corrección: priorizar por historia de cambios y contexto.
- **Una plantilla o tabla de datos se parte en trozos** — causa: la regla de largo no distingue datos de lógica. Corrección: excluir literales de datos de la regla.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md)) son: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final. Se ejecutaron tres análisis con código de ejemplo, un repositorio fijado por commit y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún proyecto de producción ni se validó ningún detector contra un conjunto etiquetado por varias personas; los umbrales, los parámetros de la simulación y las etiquetas son del autor. La siguiente clase ejecuta los tratamientos de forma segura apoyada en pruebas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md), [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Objeto](../o/objeto.md), [Complejidad ciclomática](../c/complejidad-ciclomatica.md), [Duplicación accidental](../d/duplicacion-accidental.md), [Falsa alarma](../f/falsa-alarma.md), [Olor de código](../o/olor-de-codigo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «CodeSmell»](https://martinfowler.com/bliki/CodeSmell.html) — qué es un olor de código; autoridad: Martin Fowler.
- [Fowler, «Refactoring»](https://martinfowler.com/books/refactoring.html) — catálogo de olores y de refactorizaciones; autoridad: Martin Fowler.
- [Sjøberg et al. (IEEE TSE, 2013)](https://doi.org/10.1109/TSE.2012.89) — olores y esfuerzo de mantenimiento; autoridad: IEEE Transactions on Software Engineering.
- [Yamashita y Moonen, «Do code smells reflect important maintainability aspects?» (ICSM, 2012)](https://doi.org/10.1109/ICSM.2012.6405287) — olores y aspectos de mantenibilidad percibidos; autoridad: IEEE ICSM.
- [McCabe, «A Complexity Measure» (IEEE TSE, 1976)](https://doi.org/10.1109/TSE.1976.233837) — complejidad ciclomática; autoridad: IEEE Transactions on Software Engineering.

---

[↑ Glosario](../../README.md) · [← Envenenamiento](./envenenamiento.md) · [Envoltorio de enteros →](./envoltorio-de-enteros.md)
