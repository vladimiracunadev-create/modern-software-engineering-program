# Contenido de una especificación

[↑ Glosario](../../README.md) · [← Contenedor de desarrollo](./contenedor-de-desarrollo.md) · [Contenido no confiable →](./contenido-no-confiable.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

El **contenido de una especificación** es el conjunto de elementos que permite a una lectora decidir sin preguntar. Según [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), una especificación revisable incluye el problema, los supuestos, el alcance, los requisitos con origen y criterio, las dependencias y la línea base. El criterio de suficiencia es funcional: si la lectora necesita llamar al autor para entender qué falta, la especificación está incompleta.

## Por qué importa

Cambia contra qué se revisa un documento. Una especificación puede estar bien escrita y no responder lo esencial. [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) fija la prueba: debe responder sin que su autor esté presente. Cuando falta un elemento, la lectora tendrá que preguntar, que es exactamente lo que el expediente debe evitar.

## Cómo funciona

[SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) enumera lo que la especificación debe responder:

- cuál es el problema y a quién afecta;
- qué se supone del mundo;
- qué queda fuera de alcance;
- cuáles son los requisitos, cada uno con **origen**, **texto singular y verificable**, **criterio de aceptación**, **dueño** y **prioridad**;
- cómo se relacionan (dependencias);
- qué obligaciones externas hay y quién las interpretó;
- qué **línea base** representa;
- qué defectos conocidos quedan abiertos.

La lista funciona como lista de verificación para la revisión. Un validador puede comprobar que cada elemento esté presente, pero eso es solo estructura: la clase muestra con mutaciones que un validador puede pasar mientras la especificación contiene errores graves, y por eso su cobertura se documenta y se complementa con revisión humana.

## Ejemplo

[SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) entrega la especificación de la plataforma con un encabezado (problema, supuestos, alcance, línea base) y un registro de revisión que la acompaña. Cada requisito lleva su origen y su criterio; las dependencias forman un grafo explícito. Una lectora externa puede decidir si el requisito está completo mirando solo ese expediente.

## Errores y confusiones comunes

- **La lectora tarda un día en entender qué falta.** El expediente no responde sin su autor; corrección: revisar el contenido contra la lista de elementos obligatorios.
- **El validador pasa y la especificación tiene errores graves.** Solo comprueba estructura; documentar su cobertura con mutaciones y completar con revisión humana.
- **Omitir los supuestos y el alcance excluido.** Son lo que más preguntas genera.
- **Escribir requisitos sin origen.** Impiden saber a quién preguntar y qué cambiaría si el origen cambia.

## Límites y cuándo no aplica

La lista es un contenido mínimo para una especificación revisable de la plataforma, no un estándar universal: un prototipo desechable no necesita todos los elementos. Las 16 mutaciones, costos y probabilidades de detección de [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) son supuestos del autor, con datos sintéticos; sirven para entender qué detecta un validador, no para predecir cuántos errores atrapará en un proyecto real. Que el contenido esté completo no garantiza que sea correcto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Línea base](../l/linea-base.md), [Alcance](../a/alcance.md), [Base](../b/base.md), [Conjunto](./conjunto.md), [Camino crítico](./camino-critico.md), [Decisión de entrega](../d/decision-de-entrega.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md).

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

[↑ Glosario](../../README.md) · [← Contenedor de desarrollo](./contenedor-de-desarrollo.md) · [Contenido no confiable →](./contenido-no-confiable.md)
