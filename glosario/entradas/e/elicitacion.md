# Elicitación

[↑ Glosario](../../README.md) · [← Elevación](./elevacion.md) · [ELT →](./elt.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

La **elicitación** es el conjunto de técnicas para hacer aparecer el conocimiento sobre lo que se necesita, incluida la parte que nadie escribe ni enuncia. Es el sentido de [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), donde es la primera de cuatro actividades de la ingeniería de requisitos: elicitación, análisis, especificación y validación. Elicitar es provocar que aparezca conocimiento que no está escrito en ningún sitio.

## Por qué importa

Cambia qué técnica se usa para cada tipo de conocimiento. Entrevistar no llega a lo tácito, y una especificación puede quedar «completa» y decepcionar a quienes usan el sistema porque solo se entrevistó a quien paga. [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) ilustra el límite con una simulación: hablar con todo el mundo cubre apenas el 77 % de lo necesario.

## Cómo funciona

Cada técnica tiene un alcance. Una **entrevista** recoge lo que la persona sabe y es capaz de decir. La **observación** recoge lo que hace. El **análisis de documentos** recoge lo que la organización ya decidió. Un **prototipo** recoge reacciones ante algo concreto. La razón es que el conocimiento tácito no se declara: preguntarle a una docente «¿qué necesita el sistema?» no revelará que siempre abre las entregas en el móvil mientras camina, porque ella no lo considera un dato.

Elegir la técnica es, entonces, elegir qué clase de conocimiento se puede obtener. Y como cada técnica deja huecos, se combinan. Después de elicitar viene el análisis, que trata lo recogido como conjunto para encontrar conflictos, y la validación con la persona usuaria, no solo con el cliente. Un requisito debe registrar además su origen, y hay que separar necesidad, requisito y supuesto: si una frase mezcla requisito y solución, dos equipos pueden discutirla una hora porque entienden cosas distintas.

## Ejemplo

En la plataforma de entregas de [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), entrevistar a la docente produce los requisitos que ella sabe nombrar; observar cómo corrige entregas en su jornada revela restricciones que no mencionó; analizar el reglamento académico recoge plazos ya decididos; un prototipo muestra reacciones ante el flujo. Ninguna técnica sola cubre todo.

## Errores y confusiones comunes

- **Identificar elicitar con «hablar con el cliente».** Es una técnica entre varias.
- **Entrevistar solo a quien paga.** El conocimiento tácito de quien usa no se elicita; añadir observación y validar con la persona usuaria.
- **Confundir elicitar con analizar.** El análisis empieza cuando lo recogido se trata como conjunto.
- **Registrar la solución en lugar de la necesidad.** Mezcla requisito y solución.

## Límites y cuándo no aplica

La elicitación solo obtiene lo que alguien sabe, hace o decidió; no descubre lo que nadie sabe todavía, para lo cual se usan experimentos y descubrimiento de producto. El 77 % de [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) sale de una simulación, no de un estudio de proyectos reales. Y con requisitos regulados la elicitación se apoya en documentos y no en preferencias.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Sobre](../s/sobre.md), [Análisis](../a/analisis.md), [Conocimiento tácito y supuestos](../c/conocimiento-tacito-y-supuestos.md), [Especificación](./especificacion.md), [Validación](../v/validacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-145 — Elicitación, análisis, especificación y validación](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nuseibeh y Easterbrook: Requirements engineering, a roadmap (2000)](https://doi.org/10.1145/336512.336523) — panorama de las actividades de la disciplina; autoridad: ACM, The Future of Software Engineering.
- [Zave y Jackson: Four dark corners of requirements engineering (1997)](https://doi.org/10.1145/237432.237434) — relación entre requisitos, supuestos del dominio y especificación; autoridad: ACM Transactions on Software Engineering and Methodology.
- [Boehm: Verifying and validating software requirements and design specifications (1984)](https://doi.org/10.1109/MS.1984.233702) — validación frente a verificación; autoridad: IEEE Software.
- [Fagan: Design and code inspections to reduce errors in program development (1976)](https://doi.org/10.1147/sj.153.0182) — inspección estructurada con roles; autoridad: IBM Systems Journal.
- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — procesos y elementos de información de la ingeniería de requisitos; autoridad: ISO, IEC e IEEE.

---

[↑ Glosario](../../README.md) · [← Elevación](./elevacion.md) · [ELT →](./elt.md)
