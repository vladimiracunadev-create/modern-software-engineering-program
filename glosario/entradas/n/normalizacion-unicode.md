# Normalización Unicode

[↑ Glosario](../../README.md) · [← Normalización por sintaxis](./normalizacion-por-sintaxis.md) · [Normalizar →](./normalizar.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Transformación de una cadena a una forma canónica para que secuencias equivalentes se comparen como iguales.

Definición de trabajo de [SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md): Conversión de texto a una forma canónica para comparar cadenas equivalentes.
- En [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md): Conversión de un texto a una forma canónica (NFC o NFD) para poder compararlo.
- En [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md): Conversión de un texto a una forma canónica (por ejemplo, NFC) para que secuencias equivalentes se comparen como iguales.

## Por qué importa

La clase donde se define, [SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), existe con este propósito: la clase existe para que diseñes un formulario como un contrato entre una persona, el navegador y el servidor: qué se puede escribir, quién valida qué, cuándo se muestra un error y cómo se recupera lo escrito, de modo que «validar el correo» deje de significar una expresión regular copiada de internet.

## Cómo funciona

[SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para esta clase y deben contrastarse con las especificaciones enlazadas al final.

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

- **Prerrequisito:** las clases previas [SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Secuencia](../s/secuencia.md), [Ancho en pantalla](../a/ancho-en-pantalla.md), [Internacionalización](../i/internacionalizacion.md), [Locale](../l/locale.md), [Localización](../l/localizacion.md), [Pseudolocalización](../p/pseudolocalizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-233 — Formularios, validación y experiencia de error](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md).

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

[↑ Glosario](../../README.md) · [← Normalización por sintaxis](./normalizacion-por-sintaxis.md) · [Normalizar →](./normalizar.md)
