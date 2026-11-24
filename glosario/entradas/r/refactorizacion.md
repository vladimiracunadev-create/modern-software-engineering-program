# Refactorización

[↑ Glosario](../../README.md) · [← Refactor](./refactor.md) · [Referencia →](./referencia.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

La **refactorización** es un **cambio de la estructura interna del código que no altera su comportamiento observable** ([SE-070](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md), [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md)). Martin Fowler la define así y la apoya en pruebas que comprueban que el comportamiento se conserva ([SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md)). Dos palabras son decisivas: *estructura interna*, porque lo que cambia es cómo está organizado el código (nombres, funciones, clases), y *observable*, porque lo que debe permanecer es lo que perciben quienes lo usan (resultados, errores, efectos). Un cambio que corrige un defecto o añade una función **no es** una refactorización, aunque se haga en el mismo archivo.

## Por qué importa

El código que se entiende mal se cambia con miedo y se rompe con facilidad. Refactorizar es la forma de pagar deuda técnica de manera segura: se mejora la legibilidad y la estructura para que el próximo cambio sea barato. La decisión que cambia es cómo se organiza el trabajo: **un cambio por propósito**. Si una refactorización y un arreglo van en el mismo cambio, no se puede saber, al aparecer un fallo, cuál de los dos lo causó; [SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md) lo documenta como error frecuente y su corrección es un cambio por propósito, cada uno con su revisión.

## Cómo funciona

La seguridad de una refactorización descansa en tres prácticas:

- **Pasos pequeños.** Cada paso (renombrar, extraer una función, mover un método) es tan pequeño que, si algo se rompe, la causa se localiza en el último.
- **Pruebas que fijan el comportamiento antes.** Cuando no hay pruebas, se escriben **pruebas de caracterización** ([SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md)) que registran lo que el código **hace**, no lo que debería hacer; sirven de red de seguridad.
- **Comparación diferencial.** La versión original y la refactorizada se ejecutan sobre muchas entradas, incluidas las fronteras, y se comparan los resultados.

Con asistentes automáticos, [SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md) advierte de que la parte que se pierde es la **comprobación**: el asistente devuelve una versión más corta o más clara con total seguridad y el comportamiento puede haber cambiado en un caso (el orden, un valor límite, una nota igual a cero). «Parece igual» no es «se comprobó». Por eso la clase propone un procedimiento verificable: comparación diferencial con miles de entradas generadas con fronteras, ejecución de pruebas de caracterización y un *diff* acotado, sin cambios de estilo mezclados.

## Ejemplo

Un cálculo con una condición anidada se refactoriza extrayendo una función, sin cambiar su resultado:

```python
# antes
def total(items):
    t = 0
    for i in items:
        if i["activo"] and i["precio"] > 0:
            t += i["precio"] * i["cantidad"]
    return t

# después (misma conducta, mejor estructura)
def _vale(item): return item["activo"] and item["precio"] > 0
def total(items):
    return sum(i["precio"] * i["cantidad"] for i in items if _vale(i))

# comprobación diferencial
for caso in generar_casos(5000):
    assert total_antes(caso) == total_despues(caso)
```

El generador incluye listas vacías, precios cero y cantidades extremas, que son los lugares donde las refactorizaciones suelen cambiar la conducta.

## Errores y confusiones comunes

- **Mezclar refactorización y arreglo.** Se pierde la capacidad de localizar la causa de un fallo.
- **Comprobar solo con ejemplos.** La refactorización cambia el orden o un valor límite sin que nadie lo note; se usa comparación diferencial con generador enriquecido.
- **Llamar refactorización a cualquier reescritura.** Si cambia el comportamiento, es otra cosa.
- **Confiar en la pulcritud de la salida de un asistente.** Hay que comprobar.

## Límites y cuándo no aplica

Las pruebas de caracterización fijan lo que el código hace, incluidos sus errores: pueden consagrar un defecto ([SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md)). La refactorización sin ninguna red de pruebas es una apuesta, y en código sin pruebas el primer paso es construirlas. Y si el comportamiento observable incluye rendimiento o uso de memoria, «no cambia el comportamiento» exige medirlos también; una estructura distinta puede cambiar el costo sin cambiar el resultado.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Estructura](../e/estructura.md), [Abstracción](../a/abstraccion.md), [Caracterización](../c/caracterizacion.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Duplicación de conocimiento](../d/duplicacion-de-conocimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-559 — Revisión, refactorización y explicación asistidas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (21 clases más lo mencionan; las que más):

[SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md), [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md), [SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md), [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «Refactoring»](https://refactoring.com/) — definición y práctica de la refactorización; autoridad: autor del texto.
- [Bacchelli y Bird](https://doi.org/10.1109/ICSE.2013.6606617) — revisión de código moderna: expectativas, resultados y desafíos; autoridad: ICSE 2013.
- [Google: Engineering Practices, code review](https://google.github.io/eng-practices/review/) — guía pública de revisión; autoridad: documentación de Google.
- [Claessen y Hughes, «QuickCheck»](https://doi.org/10.1145/351240.351266) — pruebas de propiedades con entradas aleatorias; autoridad: ICFP 2000.
- [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) — biblioteca de pruebas de propiedades para Python; autoridad: documentación del proyecto.

---

[↑ Glosario](../../README.md) · [← Refactor](./refactor.md) · [Referencia →](./referencia.md)
