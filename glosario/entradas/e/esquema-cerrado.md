# Esquema cerrado

[↑ Glosario](../../README.md) · [← Esquema abierto](./esquema-abierto.md) · [Esquema de datos →](./esquema-de-datos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Esquema que rechaza propiedades no declaradas.

Definición de trabajo de [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md): Esquema que rechaza campos no declarados.

## Por qué importa

La clase donde se define, [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md), existe con este propósito: la clase existe para describir con un esquema la forma que deben tener los datos que cruzan una frontera, y para saber qué errores atrapa ese esquema, cuáles no, y qué ataques abre el propio acto de validar.

## Cómo funciona

Según [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md):

**Cómo leer la figura.** Cada grupo es una situación y las barras son los documentos rechazados, de 1 000, por el esquema abierto (turquesa) y por el cerrado (coral). Mira que la barra coral es siempre completa y la turquesa solo en la primera: el cerrado atrapa más errores y también rechaza el campo nuevo legítimo. **Dónde deja de valer:** el experimento supone un único error por documento; en producción el mismo documento puede tener varios, y el motivo de un rechazo del esquema cerrado debe decir qué campo sobra para que no parezca un fallo del proveedor. Elegir es decidir quién paga: el productor que añade campos o el consumidor que pierde errores de escritura.

Según [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md):

Una comprobación que mira solo el código de estado y un ejemplo parcial (`id` y `estado`) detecta **155**; un esquema abierto con tipos y campos obligatorios, **181**; uno cerrado (sin campos extra), **232**; y uno cerrado con enumeración del estado, **283**. Las 51 mutaciones de campo extra solo las ve el esquema cerrado, y las de valor, la enumeración.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md):

En la plataforma, el esquema del documento de entrega vive en un archivo versionado junto al código del consumidor y del productor. La frontera valida primero la longitud y el tamaño del documento, después la forma con el esquema y por último las reglas entre campos con funciones con nombre (`fin_no_anterior_a_inicio`, `prorroga_no_supera_tope`). Cada rechazo devuelve el campo, la regla y un código estable, sin repetir valores sensibles. Los patrones se revisan por cuantificadores anidados y se miden con una entrada hostil en integración continua.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un cliente consigue campos que no debería tener** — causa: esquema abierto: los campos extra pasan al dominio. Corrección: esquema cerrado y lista de permitidos. ([SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** el experimento supone un único error por documento; en producción el mismo documento puede tener varios, y el motivo de un rechazo del esquema cerrado debe decir qué campo sobra para que no parezca un fallo del proveedor. ([SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Esquema](./esquema.md), [Propiedad](../p/propiedad.md), [Asignación masiva](../a/asignacion-masiva.md), [Deriva del contrato](../d/deriva-del-contrato.md), [Enumeración](./enumeracion.md), [Error permanente](./error-permanente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-162 — Esquemas de datos y validación](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md).

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

[↑ Glosario](../../README.md) · [← Esquema abierto](./esquema-abierto.md) · [Esquema de datos →](./esquema-de-datos.md)
