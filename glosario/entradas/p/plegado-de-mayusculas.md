# Plegado de mayúsculas

[↑ Glosario](../../README.md) · [← Plazo de visibilidad](./plazo-de-visibilidad.md) · [Poda →](./poda.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Transformación para comparar sin distinguir mayúsculas, más completa que pasar a minúsculas.

Definición de trabajo de [SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md).

## Por qué importa

La clase donde se define, [SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), existe con este propósito: la clase existe para que diseñes un formulario como un contrato entre una persona, el navegador y el servidor: qué se puede escribir, quién valida qué, cuándo se muestra un error y cómo se recupera lo escrito, de modo que «validar el correo» deje de significar una expresión regular copiada de internet.

## Cómo funciona

Según [SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md):

Se generaron 5000 registros de diez nombres con acentos (`José`, `María`, `Zoé`, `Ångström`, `Renée`…), 30 % de ellos en forma descompuesta y 30 % en mayúsculas. Sin normalizar, el sistema cuenta **38** nombres distintos; tras normalizar a NFC, **20**; tras normalizar y plegar mayúsculas (`casefold`), **10**, que son las diez personas. Se midieron también longitudes: `José` con tilde compuesta tiene 4 puntos de código y 5 bytes UTF-8; descompuesta, 5 y 6. Una familia con emoji (`👨‍👩‍👧`) tiene 5 puntos de código, 8 unidades UTF-16 y 18 bytes; `Straße` plegada es `strasse`, y `lower()` no la iguala a `STRASSE` pero `casefold()` sí.

## Ejemplo

Ejemplo de [SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md) (sección «Ejemplo mínimo»):

Registra versión del intérprete y salida. Añade `casefold()` y predice si `JOSÉ` en forma descompuesta coincide con `josé` compuesta tras normalizar.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md)) son:

- **Una dirección con `+` o apóstrofo es rechazada** — causa: expresión más estricta que el estándar. Corrección: usar la del estándar con reglas de longitud y probar con un corpus.
- **La misma persona aparece dos veces en el sistema** — causa: nombres con acentos en formas Unicode distintas. Corrección: normalizar y plegar para comparar; guardar el nombre tal como se escribió.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Sin normalizar, el sistema cuenta **38** nombres distintos; tras normalizar a NFC, **20**; tras normalizar y plegar mayúsculas (`casefold`), **10**, que son las diez personas. ([SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-232](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Clave de idempotencia](../c/clave-de-idempotencia.md), [Mensaje de error asociado](../m/mensaje-de-error-asociado.md), [Normalización Unicode](../n/normalizacion-unicode.md), [Validación del servidor](../v/validacion-del-servidor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md), [SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «casefold».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HTML Standard: dirección de correo válida (WHATWG)](https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address) — expresión y advertencia sobre su alcance; autoridad: WHATWG.
- [Unicode UAX #15: formas de normalización](https://unicode.org/reports/tr15/) — NFC, NFD, NFKC y NFKD; autoridad: Unicode Consortium.
- [Unicode UAX #29: segmentación de texto](https://unicode.org/reports/tr29/) — grafemas y límites de texto; autoridad: Unicode Consortium.
- [WCAG 2.2: Identificación de errores](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html) — requisito de identificar y describir errores; autoridad: W3C WAI.
- [W3C WAI: tutorial de formularios](https://www.w3.org/WAI/tutorials/forms/) — etiquetas, instrucciones y mensajes accesibles; autoridad: W3C WAI.

---

[↑ Glosario](../../README.md) · [← Plazo de visibilidad](./plazo-de-visibilidad.md) · [Poda →](./poda.md)
