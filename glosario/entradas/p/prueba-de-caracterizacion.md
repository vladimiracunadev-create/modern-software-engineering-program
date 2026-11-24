# Prueba de caracterización

[↑ Glosario](../../README.md) · [← Prueba de arquitectura](./prueba-de-arquitectura.md) · [Prueba de carga →](./prueba-de-carga.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Una **prueba de caracterización** es una prueba que fija el comportamiento actual de un código, sea o no el correcto, para detectar cambios no deseados ([SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md)). [SE-311](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md), [SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md) y [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md) la usan en el mismo sentido: fija lo que el código hace hoy, sin afirmar que sea lo correcto. Es el fundamento del maestro dorado.

## Por qué importa

En un sistema heredado muchas veces no hay especificación fiable: la especificación es el propio sistema. Escribir antes «lo correcto» puede ser imposible o carísimo. La decisión que cambia es el orden del trabajo: primero se observa y se registra lo que el código hace, y con esa red de seguridad se refactoriza o se moderniza.

## Cómo funciona

Una prueba normal expresa lo que el código **debería** hacer según una especificación. Una prueba de caracterización expresa lo que **hace hoy**: se ejecuta el código con una entrada, se observa la salida y se escribe como expectativa. Su valor es que sirve de red de seguridad: si después de un cambio la salida difiere, el cambio alteró un comportamiento, y entonces alguien decide si fue deseado ([SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md)).

La técnica invierte el orden habitual (primero se observa, luego se afirma). El resultado puede incluir comportamientos que hoy parecen errores; se registran igual, porque otros sistemas pueden depender de ellos, y se marcan para decidir aparte.

[SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md) la presenta como maestro dorado (también llamado prueba de aprobación): en el experimento se generan 5 000 entradas con semilla fija (canal, urgencia, horas, adjuntos y tamaño del grupo) y se guarda la salida de la función antigua; el refactor produce la misma salida en las 5 000 (0 diferencias). La semilla es parte de la evidencia: sin ella, otra persona no puede repetir la comprobación. La calidad depende de que las entradas cubran los bordes de decisión, y de medir mutantes para saber si las pruebas detectarían un cambio real.

## Ejemplo

Una función heredada de cálculo de plazos no tiene pruebas. Se generan entradas representativas y de borde, se ejecuta la función y se guardan las salidas como expectativas. Se refactoriza por pasos y se ejecutan las pruebas tras cada paso. Una diferencia en un caso concreto revela un cambio de comportamiento antes de llegar a producción. Procedimiento de [SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md).

## Errores y confusiones comunes

- **La prueba pasa y producción cambia**: los ejemplos no cubren los bordes de decisión; se corrige añadiendo casos de borde y midiendo mutantes.
- **La prueba falla de forma intermitente**: orden de un conjunto, reloj o azar; se corrige repitiendo con condiciones distintas y normalizando la fuente.
- **Actualizarla sin pensar cuando falla**: deja de proteger.
- **Tratarla como especificación**: registra defectos junto con virtudes.

## Límites y cuándo no aplica

Es útil cuando no hay pruebas finas y se quiere cambiar sin definir primero lo correcto; donde existen pruebas que documentan la intención, esas son preferibles. No dice que el comportamiento sea bueno, solo que no cambió. Y protege únicamente los comportamientos que las entradas ejercitan: sin buena cobertura y medición de mutantes, da una confianza que el código no tiene.

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
