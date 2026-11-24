# Revisión por pares

[↑ Glosario](../../README.md) · [← Revisión por muestreo](./revision-por-muestreo.md) · [Revisiones a ignorar →](./revisiones-a-ignorar.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

La **revisión por pares** es una lectura estructurada por personas con criterios distintos, que busca los defectos que una máquina no ve ([SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md)). En requisitos, complementa al validador de estructura: este comprueba la forma; la revisión busca contradicciones semánticas, umbrales absurdos y criterios que no prueban el requisito.

## Por qué importa

Encuentra lo que el validador no ve, con límites que hay que conocer. Un validador puede dar verde sobre una especificación con errores graves; una lectura atenta los encuentra. Cambia cómo se organiza una revisión: con lectoras que usan criterios distintos, no la misma lista repetida, y con una estimación de cuántos defectos quedan.

## Cómo funciona

Una revisión estructurada tiene lectoras que miran con **criterios distintos** (una el contenido, otra la consistencia, por ejemplo), de modo que no dependen de los mismos puntos ciegos. Es el mismo argumento de las comprobaciones correlacionadas: dos revisiones iguales encuentran lo mismo.

Para saber **cuánto falta**, [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) toma prestada de la ecología la técnica de **captura–recaptura**: si dos revisoras encuentran n₁ y n₂ defectos y coinciden en m, el total estimado es n₁·n₂/m. Por ejemplo, si una encuentra 10, otra 8 y coinciden en 5, el total estimado es 10 × 8 / 5 = 16, de modo que quedan 16 − (10 + 8 − 5) = 3 por encontrar. La estimación **funciona si** las revisoras trabajan de forma independiente y los defectos son igualmente fáciles de encontrar; falla cuando hay defectos difíciles que ninguna ve (la correlación sesga el total hacia abajo).

La revisión es parte de la **decisión de entrega** de una especificación: el expediente registra las dos revisiones, los criterios de cada una y el defecto estimado restante con su incertidumbre. Y se combina con el validador y con las mutaciones, que miden qué detecta el validador. Un riesgo: confiar en la revisión porque «alguien la leyó»; sin criterios explícitos, cada lectora mira lo que le llama la atención.

## Ejemplo

Dos revisoras leen la misma especificación con criterios distintos. Ana encuentra 12 defectos y Luis 9; coinciden en 6. El total estimado es 12 × 9 / 6 = 18. Hay 12 + 9 − 6 = 15 encontrados y quedan unos 3 sin encontrar. Si el equipo exigía como criterio de salida menos de 2, hace una tercera revisión. (Aritmética de captura–recaptura de [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), con cifras ilustrativas.)

## Errores y confusiones comunes

- **El validador pasa y la especificación tiene errores graves**: solo comprueba estructura.
- **La lectora tarda un día en entender qué falta**: el expediente no responde sin su autor.
- **Revisoras con los mismos criterios.**
- **Tomar la estimación de captura–recaptura como exacta.**

## Límites y cuándo no aplica

La estimación supone independencia y homogeneidad que rara vez se cumplen. Las cifras de [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) son supuestos del autor. Para documentos muy pequeños, una revisión informal basta. Una revisión no sustituye la validación con quienes usarán el sistema.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Camino crítico](../c/camino-critico.md), [Contenido de una especificación](../c/contenido-de-una-especificacion.md), [Decisión de entrega](../d/decision-de-entrega.md), [Validador de estructura](../v/validador-de-estructura.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), [SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md), [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — contenido de una especificación y características de los requisitos; autoridad: ISO, IEC e IEEE.
- [Fagan: Design and code inspections to reduce errors in program development (1976)](https://doi.org/10.1147/sj.153.0182) — inspecciones con roles; autoridad: IBM Systems Journal.
- [Eick et al.: Estimating software fault content before coding (1992)](https://doi.org/10.1145/143062.143090) — captura–recaptura aplicada a revisiones; autoridad: ACM, International Conference on Software Engineering.
- [Zave y Jackson: Four dark corners of requirements engineering (1997)](https://doi.org/10.1145/237432.237434) — requisitos, supuestos y especificación; autoridad: ACM Transactions on Software Engineering and Methodology.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — revisión y gestión de requisitos; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Revisión por muestreo](./revision-por-muestreo.md) · [Revisiones a ignorar →](./revisiones-a-ignorar.md)
