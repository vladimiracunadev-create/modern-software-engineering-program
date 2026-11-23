# Fuzzing

[↑ Glosario](../../README.md) · [← Fusión por clave](./fusion-por-clave.md) · [Ganancia de información →](../g/ganancia-de-informacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Generación automática de entradas para provocar fallos del programa.

Definición de trabajo de [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-464 — Secure SDLC, abuso y pruebas negativas](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md): Generación automática de entradas, aleatorias o mutadas, para provocar fallos o comportamientos inesperados.

## Por qué importa

En [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), el tema «Fuzzing con tres estrategias» importa porque el conocimiento del formato decide si se llega al código.

## Cómo funciona

Según [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md):

El fuzzing genera entradas y observa si el programa falla (excepción inesperada, caída, tiempo excesivo). Un fuzzer de bytes aleatorios casi nunca produce una entrada que supere la primera validación de un formato con cuatro campos; para llegar a las ramas profundas necesita conocer la estructura (un generador estructurado con valores límite) o descubrirla (guiado por cobertura: guarda las entradas que activan líneas nuevas y las muta). Cada estrategia cuesta algo: la estructurada exige conocer el formato y sus límites; la guiada exige instrumentación y tiempo.

Según [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md):

El equipo de la plataforma ejecuta cada noche una mutación acotada sobre los módulos que cambiaron en el día: genera los mutantes con `ast` solo en las líneas modificadas, los ejecuta contra las pruebas del módulo y publica una lista de supervivientes con su línea y el operador. Cada superviviente se revisa en la reunión semanal y se convierte en un caso nuevo, en una aserción más fuerte o en una nota de equivalencia. Para los analizadores que reciben archivos externos, un trabajo de fuzzing estructurado corre con una semilla distinta cada noche, con un corpus guardado y con el límite de tiempo de 10 minutos; las entradas que fallan se reducen y pasan a `tests/regresion/`.

## Ejemplo

Ejemplo de [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma ejecuta cada noche una mutación acotada sobre los módulos que cambiaron en el día: genera los mutantes con `ast` solo en las líneas modificadas, los ejecuta contra las pruebas del módulo y publica una lista de supervivientes con su línea y el operador. Cada superviviente se revisa en la reunión semanal y se convierte en un caso nuevo, en una aserción más fuerte o en una nota de equivalencia.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md)) son:

- **La cobertura sube y los mutantes muertos no** — causa: se añadieron casos que ejecutan líneas sin afirmar fronteras. Corrección: medir la puntuación de mutación al añadir casos.
- **Un mutante sobrevive y nadie sabe por qué** — causa: no se clasifica. Corrección: caso faltante, aserción débil o equivalente, con razón escrita.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El fuzzing busca fallos (excepciones, bloqueos), no resultados incorrectos, salvo que se le añada una propiedad como oráculo. ([SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md), [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Generación](../g/generacion.md), [Análisis estático](../a/analisis-estatico.md), [Caso de abuso](../c/caso-de-abuso.md), [Corpus](../c/corpus.md), [Mutante equivalente](../m/mutante-equivalente.md), [Puntuación de mutación](../p/puntuacion-de-mutacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-464 — Secure SDLC, abuso y pruebas negativas](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md), [SE-454](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md), [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Miller et al., «An empirical study of the reliability of UNIX utilities»](https://doi.org/10.1145/96267.96279) — origen del fuzzing; autoridad: artículo original de Communications of the ACM.
- [Böhme et al., «Coverage-based Greybox Fuzzing as Markov Chain»](https://doi.org/10.1145/2976749.2978428) — fuzzing guiado por cobertura; autoridad: artículo revisado de ACM CCS 2016.
- [Documentación de libFuzzer](https://llvm.org/docs/LibFuzzer.html) — motor de fuzzing guiado; autoridad: documentación oficial de LLVM.
- [DeMillo, Lipton y Sayward, «Hints on test data selection»](https://doi.org/10.1109/C-M.1978.218136) — origen del análisis de mutantes; autoridad: artículo original de 1978.
- [Jia y Harman, «An analysis and survey of the development of mutation testing»](https://doi.org/10.1109/TSE.2010.62) — panorama de la prueba de mutación; autoridad: artículo revisado de IEEE TSE.

---

[↑ Glosario](../../README.md) · [← Fusión por clave](./fusion-por-clave.md) · [Ganancia de información →](../g/ganancia-de-informacion.md)
