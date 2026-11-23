# Decisión de entrega

[↑ Glosario](../../README.md) · [← Decisión con rangos](./decision-con-rangos.md) · [Decisión declarada →](./decision-declarada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Juicio explícito, con criterios de salida comprobables y defectos conocidos, sobre si se puede construir sobre la especificación.

Definición de trabajo de [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md): Push, pull request o merge, separados de la implementación.

## Por qué importa

En [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), el tema «Decisión de entrega» importa porque define cuándo la especificación es lo bastante buena para construir sobre ella.

## Cómo funciona

Según [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), en la sección «Decisión de entrega»:

Entregar una especificación es una decisión con riesgo, no un hito de calendario. Los criterios de salida deben ser comprobables: el validador no produce errores, las mutaciones no detectadas están documentadas, las dos revisiones se hicieron con criterios distintos, los defectos abiertos tienen responsable y el defecto estimado restante es conocido con su incertidumbre. Lo que se entrega incluye lo que se sabe que falta.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md):

El encabezado de la especificación entregada y el registro de revisión que la acompaña:

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md)) son:

- **La lectora tarda un día en entender qué falta** — causa: el expediente no responde sin su autor. Corrección: revisar el contenido contra la lista de elementos obligatorios.
- **El validador pasa y la especificación tiene errores graves** — causa: solo comprueba estructura. Corrección: documentar su cobertura con mutaciones y completar con revisión humana.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. La especificación base, las 16 mutaciones, los costos y las probabilidades de detección son supuestos del autor, la lista de palabras vagas es un ejemplo mínimo y no participó ninguna revisora real. La [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md) toma este expediente y estudia cómo expresarlo con mayor formalidad: especificaciones, contratos y modelos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Criterio de salida](../c/criterio-de-salida.md), [Pull request](../p/pull-request.md), [Especificación](../e/especificacion.md), [Sobre](../s/sobre.md), [Camino crítico](../c/camino-critico.md), [Contenido de una especificación](../c/contenido-de-una-especificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-039](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md).

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

[↑ Glosario](../../README.md) · [← Decisión con rangos](./decision-con-rangos.md) · [Decisión declarada →](./decision-declarada.md)
