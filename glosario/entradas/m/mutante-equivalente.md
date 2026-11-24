# Mutante equivalente

[↑ Glosario](../../README.md) · [← Mutante del silencio](./mutante-del-silencio.md) · [Mutante superviviente →](./mutante-superviviente.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Un **mutante equivalente** es una variante de un programa (o de una regla) producida por una mutación que no cambia ninguna salida observable sobre el dominio considerado, por lo que ninguna prueba puede distinguirla del original: no se puede «matar» ([SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md), [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), [SE-265](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md)).

## Por qué importa

Corrige la lectura de una cifra de mutación. Si una suite deja sobrevivir algunos mutantes, no todos indican una prueba que falta: algunos son equivalentes y perseguirlos cuesta tiempo sin valor. [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) lo resume: cualquier cifra de mutantes muertos debe calcularse sobre los **no equivalentes**. Sin esa distinción, se castiga a una suite buena o se persigue un 100 % imposible.

## Cómo funciona

La prueba de mutación introduce defectos pequeños y deliberados (cambiar `>=` por `>`, quitar un rechazo) y cuenta cuántos detecta la suite. Un mutante sobrevive si ninguna prueba falla con él. Entonces hay dos posibilidades: la suite no tiene la prueba necesaria, o el mutante no cambia el comportamiento. En el segundo caso es equivalente. Decidir si un mutante es equivalente es, en general, un problema indecidible; en la práctica se revisa a mano.

[SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) da el ejemplo de la clase: cambiar `offset != 1` por `offset > 1` no altera el comportamiento cuando los únicos umbrales posibles son 72, 24 y 1; ningún oráculo puede matarlo porque no hay diferencia observable. Los dos equivalentes del laboratorio (M19 y M20) sobreviven a los cinco oráculos, y eso es lo correcto.

[SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md) añade una fuente frecuente en seguridad: la **defensa en profundidad**. Cuando dos comprobaciones rechazan lo mismo, quitar una no cambia nada visible, y el mutante resultante es equivalente. La conclusión no es borrar la comprobación redundante (la redundancia es intencional), sino anotar por qué el mutante sobrevive. Y [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) y [SE-265](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md) usan la misma noción para reglas: una variante que no cambia ninguna salida sobre el dominio considerado.

## Ejemplo

Una regla de plazos solo acepta desplazamientos de 72, 24 o 1 hora. El código `if offset != 1` se muta a `if offset > 1`. Con esos tres valores, ambas condiciones dan el mismo resultado en todo el dominio; ninguna prueba puede distinguirlas. De 20 mutantes, 2 son equivalentes y la suite mata los otros 18: la puntuación correcta es 18/18 (100 %), no 18/20 (90 %). (Escenario construido con los datos de la clase.)

## Errores y confusiones comunes

- **Contar equivalentes como fallos de la suite.**
- **Escribir pruebas contorsionadas para «matar» un equivalente**, lo que fija detalles internos irrelevantes.
- **Declarar equivalente un mutante que no lo es** solo porque es difícil de matar: hay que comprobarlo sobre el dominio.
- **Confundir equivalente con superviviente**: todo equivalente sobrevive, pero no todo superviviente es equivalente.

## Límites y cuándo no aplica

La equivalencia depende del dominio considerado: un mutante equivalente hoy puede dejar de serlo si el dominio se amplía (por ejemplo, aparecen nuevos umbrales). Revisar equivalentes a mano no escala en bases de código grandes; las herramientas tienen heurísticas imperfectas. Si el dominio no está bien definido, no se puede afirmar equivalencia.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Variante defectuosa](../v/variante-defectuosa.md), [Dominio](../d/dominio.md), [Regla](../r/regla.md), [Sobre](../s/sobre.md), [Ambigüedad](../a/ambiguedad.md), [Capa de acceso al hardware](../c/capa-de-acceso-al-hardware.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-422 — Pruebas unitarias y diseño testable](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-464 — Secure SDLC, abuso y pruebas negativas](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.
- [SE-541 — Mapa de metodologías: qué decide cada una y cómo elegir](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md), [SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md), [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md), [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md), [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Mutantes equivalentes».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [DeMillo, Lipton y Sayward, «Hints on test data selection»](https://doi.org/10.1109/C-M.1978.218136) — origen del análisis de mutantes; autoridad: artículo original de 1978.
- [Jia y Harman, «An analysis and survey of the development of mutation testing»](https://doi.org/10.1109/TSE.2010.62) — panorama de la prueba de mutación; autoridad: artículo revisado de IEEE TSE.
- [Petrović e Ivanković, «State of Mutation Testing at Google»](https://research.google/pubs/state-of-mutation-testing-at-google/) — mutación a gran escala; autoridad: Google Research.
- [Inozemtseva y Holmes, «Coverage is not strongly correlated with test suite effectiveness»](https://doi.org/10.1145/2568225.2568271) — cobertura y eficacia; autoridad: artículo revisado de ICSE 2014.
- [Miller et al., «An empirical study of the reliability of UNIX utilities»](https://doi.org/10.1145/96267.96279) — origen del fuzzing; autoridad: artículo original de Communications of the ACM.

---

[↑ Glosario](../../README.md) · [← Mutante del silencio](./mutante-del-silencio.md) · [Mutante superviviente →](./mutante-superviviente.md)
