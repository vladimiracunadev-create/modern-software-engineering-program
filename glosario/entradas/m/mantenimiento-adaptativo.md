# Mantenimiento adaptativo

[↑ Glosario](../../README.md) · [← Mantenimiento](./mantenimiento.md) · [Mantenimiento correctivo →](./mantenimiento-correctivo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Modificación para que el sistema siga funcionando cuando cambia su entorno, sin que el sistema sea defectuoso.

Definición de trabajo de [SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md).

## Por qué importa

En [SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md), el tema «El mantenimiento adaptativo tiene fecha» importa porque una fecha impuesta convierte un trabajo diferible en una restricción.

## Cómo funciona

[SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones ordena su cartera de treinta y ocho solicitudes con la tipología. Resultan 9 correctivas (de las cuales 2 graves), 6 adaptativas, 17 perfectivas y 6 preventivas; 5 solicitudes quedan «ambiguas» y se resuelven preguntando a quien las pidió.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md)) son:

- **Todo se llama «urgente»** — causa: no se distingue origen y consecuencia. Corrección: clasificar por tipología y fecha, y ordenar por consecuencia.
- **Las incidencias aumentan aunque se corrige más** — causa: el correctivo apresurado alimenta la degradación. Corrección: reservar capacidad protegida para trabajo preventivo.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-517 — Mantenimiento correctivo, adaptativo y perfectivo](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se observó ningún equipo, sistema ni institución real; los coeficientes de la simulación de capacidad, los textos de las solicitudes, la proporción de ambiguas, las tasas de acierto de las revisoras y la distribución de duraciones son construcciones del autor, y el clasificador por palabras clave se escribió conociendo los textos que lo evalúan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Entorno](../e/entorno.md), [Kappa de Cohen](../k/kappa-de-cohen.md), [Mantenimiento correctivo](./mantenimiento-correctivo.md), [Mantenimiento perfectivo](./mantenimiento-perfectivo.md), [Mantenimiento preventivo](./mantenimiento-preventivo.md).
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

[↑ Glosario](../../README.md) · [← Mantenimiento](./mantenimiento.md) · [Mantenimiento correctivo →](./mantenimiento-correctivo.md)
