# Costura

[↑ Glosario](../../README.md) · [← Costo por solución aceptada](./costo-por-solucion-aceptada.md) · [Cota →](./cota.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Una **costura** (*seam*, de Feathers) es un lugar donde puede alterarse el comportamiento de un programa sin editar el código en ese lugar ([SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md)). En [SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md) se usa en un sentido práctico: el punto del código donde se puede reemplazar una dependencia sin editar la unidad.

## Por qué importa

Es lo que permite probar y refactorizar código heredado: sin costura, probar una función exige ejecutar su dependencia lenta o real. [SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md) lo muestra con un síntoma concreto: la suite tarda minutos porque cada prueba paga la dependencia lenta; la corrección es crear una costura y sustituirla.

## Cómo funciona

Feathers distingue tres clases. En una **costura de objeto**, el comportamiento depende de un objeto o función que se puede sustituir (se pasa como argumento, se hereda, se reemplaza en una prueba); es la más usada. En una **costura de enlace** se cambia lo que se enlaza (otra biblioteca o módulo con el mismo nombre en el entorno de prueba). En una **costura de preprocesamiento** se transforma el texto antes de compilar.

## Ejemplo

[SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md) (escenario hipotético): antes de refactorizar `nota_final`, el equipo añade un parámetro `leer_asistencia` con la consulta real como valor por defecto, una costura de objeto sin cambio de comportamiento. Luego genera 1 000 entradas con semilla fija y 14 casos de borde, guarda las salidas actuales y escribe una prueba que las exige.

```python
def nota_final(alumno, leer_asistencia=consultar_asistencia):
    return calcular(alumno, leer_asistencia(alumno))
```

## Errores y confusiones comunes

**La suite tarda minutos.** Cada prueba paga la dependencia lenta; crear una costura y sustituirla.

## Límites y cuándo no aplica

Una costura no mejora el diseño por sí sola: es un medio para fijar el comportamiento antes de refactorizar. Y no todos los lenguajes ofrecen las tres clases.

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
