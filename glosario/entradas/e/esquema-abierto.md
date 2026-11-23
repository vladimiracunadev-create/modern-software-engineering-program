# Esquema abierto

[↑ Glosario](../../README.md) · [← Esquema](./esquema.md) · [Esquema cerrado →](./esquema-cerrado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Esquema que acepta propiedades no declaradas.

Definición de trabajo de [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md).

## Por qué importa

En [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md), el tema «Esquema abierto o cerrado» importa porque decide si un campo desconocido se acepta, se ignora o se rechaza.

## Cómo funciona

Según [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md):

Un esquema **abierto** acepta propiedades no declaradas; uno **cerrado** (`additionalProperties: false`) las rechaza. El abierto favorece la evolución (un productor puede añadir campos sin romper a nadie) y deja pasar errores de escritura (`comentaro` se descarta sin aviso). El cerrado atrapa esos errores y convierte cualquier campo nuevo en un cambio incompatible. No hay una respuesta correcta: la elección expresa cómo evoluciona el contrato, y se relaciona directamente con el principio del lector tolerante de `SE-164`.

Según [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md):

Porque convierte cada campo nuevo del productor en un cambio incompatible. Si los productores evolucionan con frecuencia y los consumidores no pueden actualizarse al mismo ritmo, conviene un esquema abierto con reglas claras sobre qué se ignora.

## Ejemplo

Ejemplo de [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md) (sección «Preguntas frecuentes»):

Porque convierte cada campo nuevo del productor en un cambio incompatible. Si los productores evolucionan con frecuencia y los consumidores no pueden actualizarse al mismo ritmo, conviene un esquema abierto con reglas claras sobre qué se ignora.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un campo opcional mal escrito se descarta en silencio** — causa: esquema abierto sin comprobación de campos conocidos. Corrección: cerrar el esquema donde la evolución lo permita o registrar los campos desconocidos. ([SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un esquema **abierto** acepta propiedades no declaradas; uno **cerrado** (`additionalProperties: false`) las rechaza. ([SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Esquema](./esquema.md), [Propiedad](../p/propiedad.md), [Esquema cerrado](./esquema-cerrado.md), [Esquema de datos](./esquema-de-datos.md), [Regla entre campos](../r/regla-entre-campos.md), [Retroceso catastrófico](../r/retroceso-catastrofico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [JSON Schema 2020-12: Validation](https://json-schema.org/draft/2020-12/json-schema-validation) — palabras clave de validación y su semántica; autoridad: proyecto JSON Schema.
- [Understanding JSON Schema](https://json-schema.org/understanding-json-schema/) — guía oficial de uso, incluido `additionalProperties`; autoridad: proyecto JSON Schema.
- [RFC 8259: The JSON Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259) — sintaxis y tipos de JSON; autoridad: IETF.
- [OWASP: Regular expression Denial of Service](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS) — retroceso exponencial como vector de ataque; autoridad: OWASP.
- [OWASP: Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) — validar en la frontera, listas permitidas y límites; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← Esquema](./esquema.md) · [Esquema cerrado →](./esquema-cerrado.md)
