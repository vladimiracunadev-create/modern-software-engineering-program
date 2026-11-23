# Prueba de caracterización

[↑ Glosario](../../README.md) · [← Prueba de arquitectura](./prueba-de-arquitectura.md) · [Prueba de carga →](./prueba-de-carga.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Prueba que fija el comportamiento actual de un código, sea o no el correcto, para detectar cambios no deseados.

Definición de trabajo de [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md): Prueba que fija lo que el código hace hoy, sin afirmar que sea lo correcto.
- En [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md): Prueba que documenta el comportamiento actual, correcto o no.
- En [SE-558 — Generación de pruebas, documentación y migraciones](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md): Prueba que fija el comportamiento actual, sea o no el correcto.

## Por qué importa

En [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md), el tema «Código heredado y pruebas de caracterización» importa porque permiten cambiar sin conocer la especificación, que no existe.

## Cómo funciona

Según [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md):

Una prueba normal expresa lo que el código debería hacer según una especificación. Una **prueba de caracterización** expresa lo que el código hace hoy: se ejecuta el código con una entrada, se observa la salida y se escribe como expectativa. Su valor es que sirve de red de seguridad: si después de un cambio la salida difiere, el cambio alteró un comportamiento, y entonces alguien decide si fue deseado. La técnica invierte el orden habitual (primero se observa, luego se afirma) porque en un sistema heredado la especificación es el propio sistema. El resultado puede incluir comportamientos que hoy parecen errores: se registran igual, porque otros sistemas pueden depender de ellos, y se marcan para decidir aparte.

Según [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md):

Un **maestro dorado** (también llamado prueba de caracterización o de aprobación) registra la salida del código **actual** para un conjunto de entradas y exige que el código nuevo produzca exactamente lo mismo. No dice que el comportamiento sea correcto; dice que **no cambió**. En el experimento se generan 5000 entradas con semilla fija (canal, urgencia, horas, adjuntos y tamaño del grupo) y se guarda la salida de la función antigua. El refactor produce **la misma salida en las 5000** (0 diferencias). La semilla es parte de la evidencia: sin ella, otra persona no puede repetir la comprobación.

## Ejemplo

Ejemplo de [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md) (sección «Caso conductor»):

El módulo de calificaciones es el caso conductor de la [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md). Esta clase deja el tercer artefacto: la prueba de caracterización de `nota_final` con su costura. `SE-520` preguntará qué riesgo acumulan las dependencias que el módulo usa, y `SE-521` cómo se sustituye el módulo por partes apoyándose en estas pruebas. Cambia después un solo dato, el porcentaje de partes ausentes del 5 % a cero, y observa qué mutantes dejan de ser detectables.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md)) son:

- **La prueba pasa y producción cambia** — causa: los ejemplos no cubren los bordes de decisión. Corrección: añadir casos de borde y medir mutantes.
- **La prueba falla de forma intermitente** — causa: orden de un conjunto, reloj o azar. Corrección: repetir con condiciones distintas y normalizar la fuente.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una prueba de caracterización que se actualiza sin pensar cuando falla deja de proteger. ([SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md), [SE-310](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Arco](../a/arco.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Condición de salida](../c/condicion-de-salida.md), [Entradas de frontera](../e/entradas-de-frontera.md), [Maestro dorado](../m/maestro-dorado.md), [Rareza heredada](../r/rareza-heredada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-311 — Taller: refactorizar sin alterar comportamiento](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.
- [SE-558 — Generación de pruebas, documentación y migraciones](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md), [SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md), [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md), [SE-532](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md), [SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md), [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md), [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «snapshot».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Feathers, «Working Effectively with Legacy Code»](https://www.pearson.com/en-us/subject-catalog/p/working-effectively-with-legacy-code/P200000009466/9780131177055) — pruebas de caracterización y costuras; autoridad: libro de referencia (ISBN 9780131177055).
- [Feathers, «Working Effectively with Legacy Code»](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — pruebas de caracterización; autoridad: su autor (Prentice Hall).
- [Jia y Harman, «An Analysis and Survey of the Development of Mutation Testing»](https://doi.org/10.1109/TSE.2010.62) — pruebas de mutación; autoridad: IEEE Transactions on Software Engineering, 2011.
- [Python: sys.settrace](https://docs.python.org/3/library/sys.html#sys.settrace) — medición de líneas ejecutadas; autoridad: documentación de Python.
- [Python: PYTHONHASHSEED](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED) — origen del orden variable de los conjuntos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Prueba de arquitectura](./prueba-de-arquitectura.md) · [Prueba de carga →](./prueba-de-carga.md)
