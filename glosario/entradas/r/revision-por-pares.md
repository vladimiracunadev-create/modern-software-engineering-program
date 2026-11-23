# Revisión por pares

[↑ Glosario](../../README.md) · [← Revisión por muestreo](./revision-por-muestreo.md) · [Revisiones a ignorar →](./revisiones-a-ignorar.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Lectura estructurada por personas con criterios distintos, que busca los defectos que una máquina no ve.

Definición de trabajo de [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md).

## Por qué importa

En [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), el tema «Revisión por pares» importa porque encuentra lo que el validador no ve, con límites que hay que conocer.

## Cómo funciona

Según [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), en la sección «Revisión por pares»:

Una revisión estructurada, con lectoras que usan criterios distintos, encuentra lo que el validador no puede: contradicciones semánticas, umbrales absurdos, criterios que no prueban el requisito. Para saber cuánto falta, la captura–recaptura toma prestada una idea de la ecología: si dos revisoras encuentran n₁ y n₂ defectos y coinciden en m, el total estimado es n₁·n₂/m. Funciona si las revisoras son independientes y todos los defectos son igual de fáciles de encontrar; cuando algunos son difíciles para ambas, subestima.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md):

El encabezado de la especificación entregada y el registro de revisión que la acompaña:

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md)) son:

- **La lectora tarda un día en entender qué falta** — causa: el expediente no responde sin su autor. Corrección: revisar el contenido contra la lista de elementos obligatorios.
- **El validador pasa y la especificación tiene errores graves** — causa: solo comprueba estructura. Corrección: documentar su cobertura con mutaciones y completar con revisión humana.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. La especificación base, las 16 mutaciones, los costos y las probabilidades de detección son supuestos del autor, la lista de palabras vagas es un ejemplo mínimo y no participó ninguna revisora real. La [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md) toma este expediente y estudia cómo expresarlo con mayor formalidad: especificaciones, contratos y modelos.

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
