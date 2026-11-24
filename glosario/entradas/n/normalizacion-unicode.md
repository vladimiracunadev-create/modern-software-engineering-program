# Normalización Unicode

[↑ Glosario](../../README.md) · [← Normalización por sintaxis](./normalizacion-por-sintaxis.md) · [Normalizar →](./normalizar.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

La **normalización Unicode** transforma una cadena a una forma canónica para que secuencias equivalentes se comparen como iguales ([SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), [SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md), [SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md), [SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md)). Unicode permite representar un mismo carácter visible de más de una manera: «é» puede ser un único carácter precompuesto o una «e» seguida de un acento combinante. Las dos se ven igual y no son iguales byte a byte.

## Por qué importa

Sin normalizar, la misma palabra escrita por dos teclados o sistemas distintos es dos cadenas diferentes: la misma persona aparece duplicada, una búsqueda no encuentra lo que existe, una comparación de contraseñas o de identificadores falla de modo inconsistente. [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md) lo cita como causa de que «la misma persona aparezca dos veces en el sistema»: nombres con acentos en formas Unicode distintas.

## Cómo funciona

Las formas canónicas más usadas, nombradas en [SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md) y [SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md), son **NFC** (compone: prefiere el carácter precompuesto) y **NFD** (descompone: carácter base más marcas combinantes). Existen además las formas de compatibilidad (NFKC y NFKD), que también unifican variantes como ligaduras o anchuras. Se normaliza ambos lados antes de comparar: dos cadenas equivalentes dan los mismos bytes tras normalizarse a la misma forma.

[SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md) aplica la idea a un formulario de entrega: los nombres se guardan **tal como se escriben** (lo que la persona escribió se respeta) y se comparan **normalizados y plegados** (normalización más plegado de mayúsculas). Y la longitud máxima se define en **grafemas** (lo que la persona percibe como un carácter) y se comprueba en bytes en el servidor, porque un grafema puede ocupar varios puntos de código y varios bytes. Separar lo que se guarda de lo que se compara evita perder información y a la vez evita duplicados.

## Ejemplo

El nombre «José» escrito desde un teclado que genera «é» precompuesto (U+00E9) y desde otro que genera «e» + U+0301 son visualmente idénticos. Comparados byte a byte, difieren; el sistema crea dos personas. Tras normalizar ambos a NFC, coinciden. En Python, `unicodedata.normalize("NFC", s)` hace esa conversión. (Ilustración con la biblioteca estándar; [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md) describe el mismo principio.)

## Errores y confusiones comunes

- **La misma persona aparece dos veces**: nombres con acentos en formas distintas; corrección: normalizar y plegar para comparar, y guardar el nombre tal como se escribió.
- **Normalizar antes de guardar y perder lo escrito**: algunas formas de compatibilidad alteran el texto.
- **Medir la longitud en caracteres o bytes sin considerar grafemas.**
- **Confundir normalización con plegado de mayúsculas o con eliminación de acentos**: son operaciones distintas.

## Límites y cuándo no aplica

La normalización no resuelve la confusión visual entre caracteres distintos de aspecto parecido (una «a» latina y una «а» cirílica son caracteres diferentes y seguirán diferenciándose), lo que importa en seguridad. No es apropiada para datos binarios ni para identificadores que deben compararse byte a byte. La forma elegida debe ser la misma en todo el sistema, o la comparación sigue siendo inconsistente.

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
