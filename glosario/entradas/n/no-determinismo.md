# No determinismo

[↑ Glosario](../../README.md) · [← No asociatividad](./no-asociatividad.md) · [No verificable →](./no-verificable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Dependencia de la salida de factores distintos de la entrada, como el orden de un conjunto, el reloj o el azar.

Definición de trabajo de [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md).

## Por qué importa

En [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md), el tema «Fuentes de no determinismo» importa porque una salida que varía entre ejecuciones invalida la comparación.

## Cómo funciona

[SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md):

Escenario hipotético, construido para la clase y sin datos reales. Antes de refactorizar `nota_final`, el equipo añade un parámetro `leer_asistencia` con la consulta real como valor por defecto (costura de objeto sin cambio de comportamiento), genera 1 000 entradas con semilla fija y 14 casos de borde, guarda las salidas actuales en un archivo y escribe una prueba que las exige. Mide 18 líneas de 18 cubiertas y 12 mutantes de 12 detectados con el conjunto combinado.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md)) son:

- **La prueba pasa y producción cambia** — causa: los ejemplos no cubren los bordes de decisión. Corrección: añadir casos de borde y medir mutantes.
- **La prueba falla de forma intermitente** — causa: orden de un conjunto, reloj o azar. Corrección: repetir con condiciones distintas y normalizar la fuente.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): las cifras de cobertura, mutantes y órdenes fueron idénticas y los tiempos de reloj de la costura difieren por diseño.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Dependencia](../d/dependencia.md), [Costura](../c/costura.md), [Maestro dorado](../m/maestro-dorado.md), [Prueba de caracterización](../p/prueba-de-caracterizacion.md), [Variante defectuosa](../v/variante-defectuosa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md), [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md), [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md), [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), [SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-346](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md), [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Feathers, «Working Effectively with Legacy Code»](https://www.pearson.com/en-us/subject-catalog/p/working-effectively-with-legacy-code/P200000009466/9780131177055) — pruebas de caracterización y costuras; autoridad: libro de referencia (ISBN 9780131177055).
- [Jia y Harman, «An Analysis and Survey of the Development of Mutation Testing»](https://doi.org/10.1109/TSE.2010.62) — pruebas de mutación; autoridad: IEEE Transactions on Software Engineering, 2011.
- [Python: sys.settrace](https://docs.python.org/3/library/sys.html#sys.settrace) — medición de líneas ejecutadas; autoridad: documentación de Python.
- [Python: PYTHONHASHSEED](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED) — origen del orden variable de los conjuntos; autoridad: documentación de Python.
- [Python: unittest.mock](https://docs.python.org/3/library/unittest.mock.html) — sustitución de dependencias en pruebas; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← No asociatividad](./no-asociatividad.md) · [No verificable →](./no-verificable.md)
