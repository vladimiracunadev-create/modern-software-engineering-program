# Esquema de datos

[↑ Glosario](../../README.md) · [← Esquema cerrado](./esquema-cerrado.md) · [Estabilidad →](./estabilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Descripción declarativa de la forma (tipos, rangos, formatos, campos requeridos) que debe cumplir un documento.

Definición de trabajo de [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md).

## Por qué importa

La clase donde se define, [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md), existe con este propósito: la clase existe para describir con un esquema la forma que deben tener los datos que cruzan una frontera, y para saber qué errores atrapa ese esquema, cuáles no, y qué ataques abre el propio acto de validar.

## Cómo funciona

[SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md):

En la plataforma, el esquema del documento de entrega vive en un archivo versionado junto al código del consumidor y del productor. La frontera valida primero la longitud y el tamaño del documento, después la forma con el esquema y por último las reglas entre campos con funciones con nombre (`fin_no_anterior_a_inicio`, `prorroga_no_supera_tope`). Cada rechazo devuelve el campo, la regla y un código estable, sin repetir valores sensibles. Los patrones se revisan por cuantificadores anidados y se miden con una entrada hostil en integración continua.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md)) son:

- **Una nota `true` se almacena como 1** — causa: el validador usa `isinstance(x, int)` y `bool` es subclase de `int`. Corrección: excluir booleanos explícitamente y probar tipos con casos de cada lenguaje.
- **Un campo opcional mal escrito se descarta en silencio** — causa: esquema abierto sin comprobación de campos conocidos. Corrección: cerrar el esquema donde la evolución lo permita o registrar los campos desconocidos.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): conteos idénticos y tiempos distintos. No se usó una biblioteca de validación completa, las fechas se sortearon de forma independiente y no se midió ninguna integración real. La siguiente clase coloca este esquema dentro de contratos de interfaz y de eventos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Documento](../d/documento.md), [Rango](../r/rango.md), [Tipo](../t/tipo.md), [Esquema abierto](./esquema-abierto.md), [Esquema cerrado](./esquema-cerrado.md), [Regla entre campos](../r/regla-entre-campos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

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

[↑ Glosario](../../README.md) · [← Esquema cerrado](./esquema-cerrado.md) · [Estabilidad →](./estabilidad.md)
