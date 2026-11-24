# Decisión de entrega

[↑ Glosario](../../README.md) · [← Decisión con rangos](./decision-con-rangos.md) · [Decisión declarada →](./decision-declarada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

La **decisión de entrega** es el juicio explícito, con criterios de salida comprobables y defectos conocidos, sobre si se puede construir sobre una especificación ([SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md)). [SE-550](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md) usa el mismo término de otro modo, en el contexto de IA agéntica: la acción de empujar, abrir un pull request o fusionar, que se separa de la implementación y se decide aparte.

## Por qué importa

Entregar una especificación es una decisión con riesgo, no un hito de calendario. Si se entrega por la fecha, quien construye hereda defectos sin saberlo. Con una decisión explícita, queda dicho qué se sabe que falta y quién responde. Cambia el momento de la responsabilidad: el equipo que especifica declara el estado real de su trabajo.

## Cómo funciona

[SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) pide criterios de salida **comprobables**:

- el validador de estructura no produce errores;
- las mutaciones que el validador no detecta están documentadas;
- se hicieron dos revisiones con criterios distintos;
- los defectos abiertos tienen responsable;
- el defecto estimado restante es conocido, con su incertidumbre.

La frase de la clase es que lo que se entrega **incluye lo que se sabe que falta**. Una especificación entregada no es «completa»; es suficiente para construir con el riesgo declarado. El expediente que acompaña a la entrega es el registro de revisión: encabezado, resultados de las comprobaciones, defectos abiertos y la decisión con responsable y fecha. La estimación de defectos restantes se apoya en la detección de defectos con técnicas distintas, y en lo que se sabe de la cobertura del validador (medida con mutaciones).

En el sentido de [SE-550](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md), la decisión de entrega en desarrollo con agentes es la misma idea de separar el juicio del hacer: el agente puede implementar, pero empujar, abrir un PR o fusionar son acciones que se deciden aparte, con una persona responsable y criterios de salida.

## Ejemplo

El encabezado de una especificación entregada dice: «Versión 1.0. Validador: 0 errores. Mutaciones no detectadas: 3 (documentadas). Revisiones: 2 (una de contenido, una de consistencia). Defectos abiertos: 4 (con responsable). Estimación de defectos restantes: entre 2 y 7. Decisión: construir. Responsable: producto. Fecha: …». Quien construye sabe qué riesgo hereda. (Estructura ilustrativa derivada de los criterios de [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md).)

## Errores y confusiones comunes

- **La lectora tarda un día en entender qué falta**: el expediente no responde sin su autor; corrección: revisar contra la lista de elementos obligatorios.
- **El validador pasa y hay errores graves**: solo comprueba estructura.
- **Decidir por el calendario.**
- **Entregar sin defectos abiertos declarados**: «sin defectos» casi nunca es verdad.

## Límites y cuándo no aplica

Los criterios de salida y las estimaciones de defectos de [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) son supuestos del autor. Para especificaciones pequeñas o exploratorias, el expediente completo es excesivo. Una decisión explícita no elimina el riesgo; lo hace visible y asignado.

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
