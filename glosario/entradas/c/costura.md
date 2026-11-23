# Costura

[↑ Glosario](../../README.md) · [← Costo por solución aceptada](./costo-por-solucion-aceptada.md) · [Cota →](./cota.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Lugar donde puede alterarse el comportamiento de un programa sin editar el código en ese lugar.

Definición de trabajo de [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-422 — Pruebas unitarias y diseño testable](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md): Punto del código donde se puede reemplazar una dependencia sin editar la unidad.

## Por qué importa

En [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md), el tema «Costuras y su costo» importa porque sin costura, cada prueba paga la dependencia más lenta.

## Cómo funciona

Según [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md):

Una **costura** es un lugar donde se puede alterar el comportamiento sin modificar el código en ese lugar. Feathers distingue tres clases. En una **costura de objeto** el comportamiento depende de un objeto o función que se puede sustituir (se pasa como argumento, se hereda, se reemplaza en una prueba); es la más usada. En una **costura de enlace** se cambia lo que se enlaza (otra biblioteca o módulo con el mismo nombre en el entorno de prueba). En una **costura de preprocesamiento** se transforma el texto antes de compilar, y casi no existe en Python. Sin costura, probar una función que lee la asistencia de una base de datos obliga a levantar la base en cada prueba.

Según [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md):

Escenario hipotético, construido para la clase y sin datos reales. Antes de refactorizar `nota_final`, el equipo añade un parámetro `leer_asistencia` con la consulta real como valor por defecto (costura de objeto sin cambio de comportamiento), genera 1 000 entradas con semilla fija y 14 casos de borde, guarda las salidas actuales en un archivo y escribe una prueba que las exige. Mide 18 líneas de 18 cubiertas y 12 mutantes de 12 detectados con el conjunto combinado. Al caracterizar descubre que la nota de un alumno con una parte ausente se calcula con peso 0,3 y 0,3 sobre un total de 0,6, un comportamiento que parece un defecto; consulta con el área académica y se decide conservarlo hasta la siguiente revisión del reglamento, con la anotación en la prueba.

## Ejemplo

Ejemplo de [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. Antes de refactorizar `nota_final`, el equipo añade un parámetro `leer_asistencia` con la consulta real como valor por defecto (costura de objeto sin cambio de comportamiento), genera 1 000 entradas con semilla fija y 14 casos de borde, guarda las salidas actuales en un archivo y escribe una prueba que las exige. Mide 18 líneas de 18 cubiertas y 12 mutantes de 12 detectados con el conjunto combinado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La suite tarda minutos** — causa: cada prueba paga la dependencia lenta. Corrección: crear una costura y sustituir la dependencia. ([SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **costura** es un lugar donde se puede alterar el comportamiento sin modificar el código en ese lugar. ([SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md))
- Traslada el análisis a otro dominio (por ejemplo, una función que calcula el precio de una reserva con descuentos): cambia la función y las dependencias y conserva el procedimiento de crear una costura, registrar un maestro dorado, medir cobertura y mutantes, normalizar la variación y decidir qué hacer con cada comportamiento sospechoso. ([SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](../d/dependencia.md), [Frontera](../f/frontera.md), [Maestro dorado](../m/maestro-dorado.md), [Mutante equivalente](../m/mutante-equivalente.md), [No determinismo](../n/no-determinismo.md), [Prueba de caracterización](../p/prueba-de-caracterizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-422 — Pruebas unitarias y diseño testable](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md), [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md), [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md), [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «seam».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Feathers, «Working Effectively with Legacy Code»](https://www.pearson.com/en-us/subject-catalog/p/working-effectively-with-legacy-code/P200000009466/9780131177055) — pruebas de caracterización y costuras; autoridad: libro de referencia (ISBN 9780131177055).
- [Jia y Harman, «An Analysis and Survey of the Development of Mutation Testing»](https://doi.org/10.1109/TSE.2010.62) — pruebas de mutación; autoridad: IEEE Transactions on Software Engineering, 2011.
- [Python: sys.settrace](https://docs.python.org/3/library/sys.html#sys.settrace) — medición de líneas ejecutadas; autoridad: documentación de Python.
- [Python: PYTHONHASHSEED](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED) — origen del orden variable de los conjuntos; autoridad: documentación de Python.
- [Python: unittest.mock](https://docs.python.org/3/library/unittest.mock.html) — sustitución de dependencias en pruebas; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Costo por solución aceptada](./costo-por-solucion-aceptada.md) · [Cota →](./cota.md)
