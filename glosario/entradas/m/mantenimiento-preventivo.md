# Mantenimiento preventivo

[↑ Glosario](../../README.md) · [← Mantenimiento perfectivo](./mantenimiento-perfectivo.md) · [Mantenimiento y deterioro →](./mantenimiento-y-deterioro.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Modificación para que el sistema conserve la capacidad de cambiar, sin cambiar su comportamiento visible.

Definición de trabajo de [SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md).

## Por qué importa

La clase donde se define, [SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md), existe con este propósito: la clase existe para que dejes de tratar el mantenimiento como «lo que queda después de construir» y lo trates como el modo de vida normal de un sistema que sigue en uso.

## Cómo funciona

Según [SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md):

Refactorizar es una técnica; el mantenimiento preventivo es la categoría de trabajo que la usa. Puede incluir refactorizar, pero también documentar un formato, eliminar dependencias sin uso o añadir pruebas, todo lo que protege la capacidad de cambiar sin cambiar el comportamiento visible.

## Ejemplo

Ejemplo de [SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md) (sección «Preguntas frecuentes»):

Refactorizar es una técnica; el mantenimiento preventivo es la categoría de trabajo que la usa. Puede incluir refactorizar, pero también documentar un formato, eliminar dependencias sin uso o añadir pruebas, todo lo que protege la capacidad de cambiar sin cambiar el comportamiento visible.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md)) son:

- **Todo se llama «urgente»** — causa: no se distingue origen y consecuencia. Corrección: clasificar por tipología y fecha, y ordenar por consecuencia.
- **Las incidencias aumentan aunque se corrige más** — causa: el correctivo apresurado alimenta la degradación. Corrección: reservar capacidad protegida para trabajo preventivo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se observó ningún equipo, sistema ni institución real; los coeficientes de la simulación de capacidad, los textos de las solicitudes, la proporción de ambiguas, las tasas de acierto de las revisoras y la distribución de duraciones son construcciones del autor, y el clasificador por palabras clave se escribió conociendo los textos que lo evalúan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Kappa de Cohen](../k/kappa-de-cohen.md), [Mantenimiento adaptativo](./mantenimiento-adaptativo.md), [Mantenimiento correctivo](./mantenimiento-correctivo.md), [Mantenimiento perfectivo](./mantenimiento-perfectivo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — mantenimiento del software y sus categorías; autoridad: IEEE Computer Society.
- [Lehman, «Programs, life cycles, and laws of software evolution»](https://doi.org/10.1109/PROC.1980.11805) — leyes de evolución del software; autoridad: Proceedings of the IEEE, 1980.
- [Fowler, «TechnicalDebt»](https://martinfowler.com/bliki/TechnicalDebt.html) — la metáfora de la deuda y sus intereses; autoridad: autor del texto.
- [Python: random](https://docs.python.org/3/library/random.html) — generador con semilla para reproducir las simulaciones; autoridad: documentación de Python.
- [Python: statistics](https://docs.python.org/3/library/statistics.html) — mediana y cuantiles usados en los resultados; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Mantenimiento perfectivo](./mantenimiento-perfectivo.md) · [Mantenimiento y deterioro →](./mantenimiento-y-deterioro.md)
