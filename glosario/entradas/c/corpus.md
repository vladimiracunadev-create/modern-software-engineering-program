# Corpus

[↑ Glosario](../../README.md) · [← Copyright y licencia](./copyright-y-licencia.md) · [Corrección hacia delante →](./correccion-hacia-delante.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Conjunto de entradas que un fuzzer conserva y muta.

Definición de trabajo de [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md).

## Por qué importa

La clase donde se define, [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), existe con este propósito: la clase existe para que midas la calidad de las pruebas con mutación (¿qué cambios del código detectan?) y para que uses la generación automática de entradas (fuzzing) donde los casos escritos a mano no llegan, sabiendo qué conocimiento del formato hace falta darle al generador.

## Cómo funciona

Según [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md):

Un fuzzer encuentra entradas que fallan; el trabajo útil es reducirlas, entender la causa y fijarlas como pruebas. Una entrada hallada y no convertida en prueba reaparece la próxima vez que alguien cambie el código. La entrada mínima se guarda como caso de regresión y el defecto se corrige; el fuzzer sigue corriendo con la entrada original en su corpus.

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

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con un módulo sintético de 21 líneas, 18 mutantes y cuatro defectos escritos por el autor, en Windows y Ubuntu (WSL2), con salidas idénticas. No se usó una herramienta de mutación ni un fuzzer real, y los generadores estructurado y guiado contienen valores que el autor sabía que importaban. La equivalencia se decidió con una rejilla finita.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md), [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](./conjunto.md), [Fuzzing](../f/fuzzing.md), [Mutante equivalente](../m/mutante-equivalente.md), [Puntuación de mutación](../p/puntuacion-de-mutacion.md), [Variante defectuosa](../v/variante-defectuosa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (17 clases más lo mencionan; las que más):

[SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md), [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), [SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md), [SE-213](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md), [SE-084](../../../classes/part-06-paradigmas-de-programacion/se-084-proyecto-comparacion-semantica-con-pruebas-comunes/README.md), [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [DeMillo, Lipton y Sayward, «Hints on test data selection»](https://doi.org/10.1109/C-M.1978.218136) — origen del análisis de mutantes; autoridad: artículo original de 1978.
- [Jia y Harman, «An analysis and survey of the development of mutation testing»](https://doi.org/10.1109/TSE.2010.62) — panorama de la prueba de mutación; autoridad: artículo revisado de IEEE TSE.
- [Petrović e Ivanković, «State of Mutation Testing at Google»](https://research.google/pubs/state-of-mutation-testing-at-google/) — mutación a gran escala; autoridad: Google Research.
- [Inozemtseva y Holmes, «Coverage is not strongly correlated with test suite effectiveness»](https://doi.org/10.1145/2568225.2568271) — cobertura y eficacia; autoridad: artículo revisado de ICSE 2014.
- [Miller et al., «An empirical study of the reliability of UNIX utilities»](https://doi.org/10.1145/96267.96279) — origen del fuzzing; autoridad: artículo original de Communications of the ACM.

---

[↑ Glosario](../../README.md) · [← Copyright y licencia](./copyright-y-licencia.md) · [Corrección hacia delante →](./correccion-hacia-delante.md)
