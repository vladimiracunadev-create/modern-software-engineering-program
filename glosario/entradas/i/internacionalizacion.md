# Internacionalización

[↑ Glosario](../../README.md) · [← Intermediario](./intermediario.md) · [Internationalization Engineer →](./internationalization-engineer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Preparación de un producto para que funcione en cualquier lengua y región.

Definición de trabajo de [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md).

## Por qué importa

En [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md), el tema «Internacionalización, localización y traducción» importa porque fija quién hace qué y cuándo.

## Cómo funciona

Según [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md):

Compara el caso normal con un nombre con acento combinado, el plural de 21 en ruso y una fecha 03/04 de una persona de otra región. Una internacionalización es apropiada cuando esos tres casos están cubiertos; es peligrosa cuando solo se probó con el español de quien la escribió.

## Ejemplo

Ejemplo de [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md) (sección «Ejemplo profesional»):

Compara el caso normal con un nombre con acento combinado, el plural de 21 en ruso y una fecha 03/04 de una persona de otra región. Una internacionalización es apropiada cuando esos tres casos están cubiertos; es peligrosa cuando solo se probó con el español de quien la escribió.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md)) son:

- **«1 entregas» o «2 entrega»** — causa: regla de plural de una sola lengua o concatenación. Corrección: mensajes completos con categorías de plural por locale.
- **Dos nombres iguales se tratan como distintos** — causa: distinta composición Unicode sin normalizar. Corrección: normalizar a NFC al comparar.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ninguna biblioteca de localización, no se tradujo contenido real y las reglas de plural se aplicaron a mano a enteros de 0 a 120; la expansión del texto es un supuesto del autor. La siguiente clase pregunta cómo medir si las personas logran la tarea con todo esto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Producto](../p/producto.md), [Región](../r/region.md), [Locale](../l/locale.md), [Localización](../l/localizacion.md), [Normalización Unicode](../n/normalizacion-unicode.md), [Pseudolocalización](../p/pseudolocalizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md), [SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C Internationalization: ¿qué es la internacionalización?](https://www.w3.org/International/questions/qa-i18n) — conceptos y buenas prácticas; autoridad: W3C.
- [ECMA-402: API de internacionalización de ECMAScript](https://tc39.es/ecma402/) — formato de números, fechas y plurales en JavaScript; autoridad: Ecma International.
- [Unicode CLDR: reglas de plural](https://cldr.unicode.org/index/cldr-spec/plural-rules) — categorías de plural por lengua; autoridad: Unicode Consortium.
- [Unicode TR35: números](https://www.unicode.org/reports/tr35/tr35-numbers.html) — formatos y patrones de números por región; autoridad: Unicode Consortium.
- [Unicode UAX #15: formas de normalización](https://www.unicode.org/reports/tr15/) — NFC y NFD; autoridad: Unicode Consortium.

---

[↑ Glosario](../../README.md) · [← Intermediario](./intermediario.md) · [Internationalization Engineer →](./internationalization-engineer.md)
