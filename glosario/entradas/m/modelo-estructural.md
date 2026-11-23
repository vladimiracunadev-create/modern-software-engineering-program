# Modelo estructural

[↑ Glosario](../../README.md) · [← Modelo ejecutable de arquitectura](./modelo-ejecutable-de-arquitectura.md) · [Modelo generativo →](./modelo-generativo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Descripción de las partes de un sistema y sus relaciones, sin el orden en que ocurren las cosas.

Definición de trabajo de [SE-160 — Modelos estructurales, conductuales y de información](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md).

## Por qué importa

La clase donde se define, [SE-160 — Modelos estructurales, conductuales y de información](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md), existe con este propósito: la clase existe para elegir qué se modela (estructura, comportamiento o información), con qué nivel de detalle y cómo se comprueba que el modelo sigue diciendo la verdad del sistema, de modo que un diagrama deje de ser un dibujo que envejece.

## Cómo funciona

Según [SE-160 — Modelos estructurales, conductuales y de información](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md):

Un modelo estructural describe qué partes existen y cómo se conectan: entidades con atributos, relaciones con cardinalidad, componentes con dependencias. Responde a preguntas de alcance («¿qué toca cambiar la entrega si cambia el curso?») y de coherencia («¿toda prórroga pertenece a una tarea y a una estudiante?»). Su límite es que no dice cuándo ni en qué orden ocurre algo. UML ofrece una notación estándar; para muchos fines basta una tabla de entidades con sus campos y referencias, comprobable por programa.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-160 — Modelos estructurales, conductuales y de información](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md):

En la plataforma, el modelo de entidades vive en un archivo estructurado junto al código (entidad, campos con tipo, referencias con cardinalidad). Un comprobador de integración continua verifica la consistencia estructural; un segundo extrae del código las clases con `ast` y compara nombres y tipos con el modelo, y falla con un mensaje que dice qué cambio de qué archivo causó la divergencia. Los diagramas para humanos se generan a partir de ese archivo, no al revés.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-160 — Modelos estructurales, conductuales y de información](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md)) son:

- **El diagrama no coincide con la base en producción** — causa: se dibujó una vez y no se comprueba. Corrección: generar el diagrama desde un archivo que se compara con el código o la base.
- **El comprobador estructural da verde y la relación está invertida** — causa: la semántica no es comprobable estructuralmente. Corrección: revisión por una persona con el dominio y ejemplos de datos que contradigan la relación.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un modelo estructural describe qué partes existen y cómo se conectan: entidades con atributos, relaciones con cardinalidad, componentes con dependencias. ([SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Relación](../r/relacion.md), [Deriva](../d/deriva.md), [Modelo conductual](./modelo-conductual.md), [Modelo de información](./modelo-de-informacion.md), [Normalización](../n/normalizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-160 — Modelos estructurales, conductuales y de información](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OMG: Unified Modeling Language](https://www.omg.org/spec/UML/) — especificación de la notación de modelos estructurales y conductuales; autoridad: Object Management Group.
- [Chen, «The entity-relationship model» (ACM TODS, 1976)](https://doi.org/10.1145/320434.320440) — entidades, relaciones y cardinalidades; autoridad: ACM Transactions on Database Systems.
- [Codd, «A relational model of data for large shared data banks» (CACM, 1970)](https://doi.org/10.1145/362384.362685) — modelo relacional y fundamento de la normalización; autoridad: Communications of the ACM.
- [The C4 model](https://c4model.com/) — vistas de la arquitectura por nivel de detalle; autoridad: autor del modelo.
- [Harel, «Statecharts» (Science of Computer Programming, 1987)](https://doi.org/10.1016/0167-6423%2887%2990035-9) — formalismo visual para modelos conductuales; autoridad: Science of Computer Programming.

---

[↑ Glosario](../../README.md) · [← Modelo ejecutable de arquitectura](./modelo-ejecutable-de-arquitectura.md) · [Modelo generativo →](./modelo-generativo.md)
