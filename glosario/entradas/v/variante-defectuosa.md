# Variante defectuosa

[↑ Glosario](../../README.md) · [← Variante](./variante.md) · [Vary →](./vary.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Una **variante defectuosa** es una copia del código (o de un programa, de un manifiesto o de un producto) con un cambio pequeño introducido a propósito, cuyo objetivo es comprobar si las pruebas lo detectan. Es el término que el programa usa para lo que la bibliografía llama **mutante** (*mutant*): [SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md) la define como una copia con un cambio mecánico pequeño, «muerta» si alguna prueba falla y «superviviente» si todas pasan; [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) usa «muere» y «sobrevive» respecto de los oráculos; [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md) la presenta junto con la mutación y el *fuzzing*. Quince clases la definen con variantes de redacción, siempre con el mismo núcleo: un defecto plantado para medir la capacidad de detección.

## Por qué importa

Una prueba que nunca ha fallado no demuestra que pueda fallar. La variante defectuosa responde a esa pregunta: si se rompe el código a propósito y todas las pruebas siguen pasando, la prueba no protege lo que parecía proteger. [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md) lo formula como comprobar que una prueba puede fallar. La alternativa habitual, la cobertura de líneas, responde otra pregunta: no «¿se ejecutó esta línea?», sino «si esta línea cambia, ¿falla algo?» ([SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md)).

## Cómo funciona

El mecanismo, según [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), se apoya en un **operador de mutación**: una regla de cambio mecánico, como sustituir `<` por `<=`, `and` por `or`, sumar uno a una constante o negar una condición. Aplicado en cada lugar posible, produce una población de variantes, cada una un error plausible en pequeño. Se ejecuta la suite sobre cada una:

- Si alguna prueba falla, la variante **muere** (la suite la detectó).
- Si todas pasan, la variante **sobrevive**, y hay que clasificarla: caso faltante, aserción débil o variante **equivalente** (un cambio que no altera ninguna salida y que ninguna prueba puede matar), con la razón escrita ([SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md)).

La **puntuación de mutación** es la fracción de variantes no equivalentes que alguna prueba mata. Se apoya en dos hipótesis con apoyo empírico parcial, no leyes: que los defectos reales son combinaciones de errores pequeños y que una batería que detecta los simples detecta la mayoría de los complejos.

## Ejemplo

En [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), un módulo de 21 líneas se muta con seis operadores y produce 18 variantes, ninguna equivalente. Se ejecutan cuatro baterías de pruebas. Pasar de la batería A a la B suma 22 puntos de cobertura y no mata ninguna variante más: los casos nuevos ejecutan líneas sin probar los límites. La batería D no tiene ninguna aserción, ejecuta dos tercios de las líneas y mata 6 variantes, todas porque el cambio provoca una excepción: es un detector de caídas, no de comportamientos erróneos. La C llega a 17 de 18 y su único superviviente cambia el redondeo de uno a dos decimales, porque ningún promedio probado tiene segundo decimal. Son datos de un módulo pequeño elegido por la clase.

## Errores y confusiones comunes

- **La cobertura sube y los mutantes muertos no.** Se añadieron casos que ejecutan líneas sin afirmar fronteras; corrección ([SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md)): medir la puntuación de mutación al añadir casos.
- **Un superviviente que nadie explica.** No se clasifica; hay que decidir si falta un caso, la aserción es débil o es equivalente.
- **Usar la puntuación como probabilidad de detectar defectos reales.** No lo es: es una comparación entre baterías sobre el mismo conjunto de variantes ([SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md)).

## Límites y cuándo no aplica

La puntuación solo compara baterías sobre el mismo conjunto de variantes: no mide la calidad del producto ni la probabilidad de detectar defectos reales ([SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md)). Las variantes equivalentes no se pueden matar con ninguna prueba y por eso se excluyen de la puntuación, lo que obliga a clasificar cada superviviente con una razón escrita. Y como el programa usa nombres cercanos (mutante, mutación, variante defectuosa), conviene leerlos como el mismo mecanismo con énfasis distinto: el de la técnica, el del procedimiento y el del objeto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cambio mínimo](../c/cambio-minimo.md), [Defecto sembrado](../d/defecto-sembrado.md), [Manifiesto](../m/manifiesto.md), [Oráculo](../o/oraculo.md), [Cobertura de pares](../c/cobertura-de-pares.md), [Consentimiento](../c/consentimiento.md).
- **Se confunde con:** Es la fracción de mutantes no equivalentes que alguna prueba mata.

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-137 — Telemetría de producto y consentimiento](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-422 — Pruebas unitarias y diseño testable](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-454 — Verificación y cobertura: MC/DC, HIL y SIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.
- [SE-459 — Autorización, recursos y mínimo privilegio](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.
- [SE-519 — Pruebas de caracterización y seams](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.
- [SE-541 — Mapa de metodologías: qué decide cada una y cómo elegir](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.
- [SE-558 — Generación de pruebas, documentación y migraciones](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.
- [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.
- [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.
- [SE-612 — Proyecto: sistema de ML operable con evidencia](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (32 clases más lo mencionan; las que más):

[SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), [SE-551](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md), [SE-544](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md), [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), [SE-545](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md), [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «mutante», «Variantes defectuosas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [EDPB: Guidelines 05/2020 on consent under Regulation 2016/679](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052020-consent-under-regulation-2016679_en) — condiciones del consentimiento válido y su retirada; autoridad: Comité Europeo de Protección de Datos.
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — vocabulario para gestionar riesgo de privacidad; autoridad: NIST.
- [k-Anonymity: A Model for Protecting Privacy (Sweeney, 2002)](https://epic.org/wp-content/uploads/privacy/reidentification/Sweeney_Article.pdf) — la reidentificación por combinación de atributos y el criterio de k-anonimato; autoridad: artículo académico (International Journal on Uncertainty, Fuzziness and Knowledge-based Systems).
- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — medir lo necesario para mejorar un servicio; autoridad: Government Digital Service.
- [Python: `collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter) — conteo de grupos para la unicidad.

---

[↑ Glosario](../../README.md) · [← Variante](./variante.md) · [Vary →](./vary.md)
