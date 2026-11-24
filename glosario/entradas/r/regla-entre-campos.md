# Regla entre campos

[↑ Glosario](../../README.md) · [← Regla decidible](./regla-decidible.md) · [Regla mecanizable →](./regla-mecanizable.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Una **regla entre campos** es una condición que relaciona el valor de dos o más campos de un mismo documento, y que un esquema de forma no expresa ([SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md)). Ejemplos: `fin ≥ inicio`; una prórroga que no excede el tope de la tarea; una nota que coincide con su calificación.

## Por qué importa

Cada campo puede ser válido por sí solo y el conjunto, incoherente. Un esquema (como JSON Schema) valida tipos, rangos y formatos por campo, pero ninguna palabra clave estándar relaciona dos campos de forma general. Si nadie escribe estas reglas, los datos «válidos» pero absurdos entran al sistema y se detectan tarde. Cambia el diseño de la frontera de validación: además de la forma, hay una capa de reglas de coherencia.

## Cómo funciona

[SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md) sitúa la validación en capas en la frontera del sistema. Primero, **longitud y tamaño** del documento (para rechazar entradas desmedidas antes de procesarlas). Segundo, **forma**, con el esquema versionado junto al código del productor y del consumidor. Tercero, las **reglas entre campos**, con funciones con nombre (`fin_no_anterior_a_inicio`, `prorroga_no_supera_tope`). Cada rechazo devuelve el campo, la regla y un código estable, sin repetir valores sensibles.

Las salidas posibles para expresarlas son tres: comprobarlas en código, expresarlas con una extensión del esquema o moverlas a una regla de negocio con nombre. Lo importante, dice la clase, es que **alguien las sea dueño**: una regla entre campos ausente es una de las causas más habituales de datos válidos e incoherentes. El efecto práctico de darles nombre es que se pueden probar, versionar y reutilizar en el cliente y en el servidor.

La clase añade una precaución sobre los patrones de texto (expresiones regulares) usados en la validación de forma: se revisan por cuantificadores anidados (riesgo de backtracking catastrófico) y se miden con una entrada hostil.

## Ejemplo

Un documento de entrega: `{"inicio": "2026-05-10", "fin": "2026-05-01", "prorroga_horas": 120}`. El esquema acepta ambos campos de fecha (cada uno tiene formato válido) y el entero. Las reglas entre campos rechazan: `fin_no_anterior_a_inicio` falla (el fin es anterior al inicio), y `prorroga_no_supera_tope` falla si el tope de la tarea es de 72 horas. La respuesta indica el campo, la regla y un código estable. (Documento ilustrativo; las reglas son las de [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md).)

## Errores y confusiones comunes

- **Datos válidos pero incoherentes**: las reglas no están en ninguna capa; corrección: escribirlas con nombre y aplicarlas en la frontera.
- **Duplicarlas en cliente y servidor con lógica distinta.**
- **Poner la regla solo en la interfaz**: cualquier otro cliente la evade.
- **Devolver el valor sensible en el mensaje de error.**

## Límites y cuándo no aplica

Algunas reglas dependen de estado externo (el tope depende de otra tabla, un identificador existe o no) y no son verificables con el documento solo; son reglas de negocio con acceso a datos. Las extensiones de esquema no son portables entre herramientas. Una regla entre campos válida hoy puede cambiar con la política; por eso se nombra y se versiona.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Esquema](../e/esquema.md), [Valor](../v/valor.md), [Esquema abierto](../e/esquema-abierto.md), [Esquema cerrado](../e/esquema-cerrado.md), [Esquema de datos](../e/esquema-de-datos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Reglas entre campos».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [JSON Schema 2020-12: Validation](https://json-schema.org/draft/2020-12/json-schema-validation) — palabras clave de validación y su semántica; autoridad: proyecto JSON Schema.
- [Understanding JSON Schema](https://json-schema.org/understanding-json-schema/) — guía oficial de uso, incluido `additionalProperties`; autoridad: proyecto JSON Schema.
- [RFC 8259: The JSON Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259) — sintaxis y tipos de JSON; autoridad: IETF.
- [OWASP: Regular expression Denial of Service](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS) — retroceso exponencial como vector de ataque; autoridad: OWASP.
- [OWASP: Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) — validar en la frontera, listas permitidas y límites; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← Regla decidible](./regla-decidible.md) · [Regla mecanizable →](./regla-mecanizable.md)
