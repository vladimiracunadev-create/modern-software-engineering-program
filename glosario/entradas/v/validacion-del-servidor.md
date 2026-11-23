# Validación del servidor

[↑ Glosario](../../README.md) · [← Validación del paquete](./validacion-del-paquete.md) · [Validación por capas →](./validacion-por-capas.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Comprobación que se ejecuta donde la persona no puede alterarla y que decide si un dato se acepta.

Definición de trabajo de [SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md).

## Por qué importa

La clase donde se define, [SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), existe con este propósito: la clase existe para que diseñes un formulario como un contrato entre una persona, el navegador y el servidor: qué se puede escribir, quién valida qué, cuándo se muestra un error y cómo se recupera lo escrito, de modo que «validar el correo» deje de significar una expresión regular copiada de internet.

## Cómo funciona

Según [SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md):

Hay tres lugares: las restricciones nativas (inmediatas, sin código), la validación del cliente (reglas propias, mensajes propios) y la del servidor. Las dos primeras son comodidades; el cliente lo controla quien escribe, y cualquiera puede enviar una petición sin pasar por él. Por eso la validación del servidor es obligatoria y las otras dos son una mejora de la experiencia. La consecuencia de diseño: las reglas deben definirse una vez y aplicarse en ambos lados (o repetirse con una prueba que las compare), y el servidor debe devolver errores con el mismo formato que el cliente sabe mostrar.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md):

El formulario de entrega usa `type="email"` y `autocomplete="email"`, valida en el cliente al salir del campo y de nuevo en cada cambio solo si ya hay un error mostrado, y el servidor aplica las mismas reglas con una prueba que compara ambas implementaciones con el corpus de la clase. Los nombres se guardan tal como se escriben y se comparan normalizados y plegados; la longitud máxima se define en grafemas y se comprueba en bytes en el servidor.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md)) son:

- **Una dirección con `+` o apóstrofo es rechazada** — causa: expresión más estricta que el estándar. Corrección: usar la del estándar con reglas de longitud y probar con un corpus.
- **La misma persona aparece dos veces en el sistema** — causa: nombres con acentos en formas Unicode distintas. Corrección: normalizar y plegar para comparar; guardar el nombre tal como se escribió.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md)) son: Las definiciones son operativas para esta clase y deben contrastarse con las especificaciones enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El corpus y sus etiquetas son del autor, los diez nombres son inventados y la simulación de escritura es mecánica: no se midió a ninguna persona ni se usó un navegador. La siguiente clase pregunta cómo se identifica cada pantalla del formulario con una dirección que sobreviva a una recarga y a un enlace compartido.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-232](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Clave de idempotencia](../c/clave-de-idempotencia.md), [Mensaje de error asociado](../m/mensaje-de-error-asociado.md), [Normalización Unicode](../n/normalizacion-unicode.md), [Plegado de mayúsculas](../p/plegado-de-mayusculas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HTML Standard: dirección de correo válida (WHATWG)](https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address) — expresión y advertencia sobre su alcance; autoridad: WHATWG.
- [Unicode UAX #15: formas de normalización](https://unicode.org/reports/tr15/) — NFC, NFD, NFKC y NFKD; autoridad: Unicode Consortium.
- [Unicode UAX #29: segmentación de texto](https://unicode.org/reports/tr29/) — grafemas y límites de texto; autoridad: Unicode Consortium.
- [WCAG 2.2: Identificación de errores](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html) — requisito de identificar y describir errores; autoridad: W3C WAI.
- [W3C WAI: tutorial de formularios](https://www.w3.org/WAI/tutorials/forms/) — etiquetas, instrucciones y mensajes accesibles; autoridad: W3C WAI.

---

[↑ Glosario](../../README.md) · [← Validación del paquete](./validacion-del-paquete.md) · [Validación por capas →](./validacion-por-capas.md)
