# Pseudolocalización

[↑ Glosario](../../README.md) · [← Prueba unitaria](./prueba-unitaria.md) · [PSI →](./psi.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Transformación del texto fuente que simula expansión y acentos para detectar problemas antes de traducir.

Definición de trabajo de [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md).

## Por qué importa

En [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md), el tema «Expansión del texto y pseudolocalización» importa porque hace visibles los problemas de longitud antes de traducir.

## Cómo funciona

Según [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md):

Las traducciones suelen ser más largas que el original y las cadenas cortas crecen más en proporción. Una pseudolocalización transforma el texto fuente (acentos, relleno, corchetes) para detectar cadenas truncadas, concatenaciones y texto fijo en el código sin traducir nada. La holgura de la maquetación debe decidirse con las longitudes reales de las traducciones, y los botones y etiquetas con texto fijo son los primeros en romperse.

Según [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md):

En la plataforma, los mensajes viven en recursos por locale con un formato que admite plurales y géneros, y ninguna cadena se construye por concatenación. Una prueba comprueba que cada clave existe en todos los locales con las categorías de plural que exige su lengua; otra aplica pseudolocalización y falla si una etiqueta se trunca; las fechas se guardan en ISO 8601 y los números sin separador de miles, y se formatean al mostrar. Los nombres de personas se almacenan sin cambiar su normalización y se comparan tras normalizar.

## Ejemplo

Ejemplo de [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md) (sección «Ejemplo profesional»):

En la plataforma, los mensajes viven en recursos por locale con un formato que admite plurales y géneros, y ninguna cadena se construye por concatenación. Una prueba comprueba que cada clave existe en todos los locales con las categorías de plural que exige su lengua; otra aplica pseudolocalización y falla si una etiqueta se trunca; las fechas se guardan en ISO 8601 y los números sin separador de miles, y se formatean al mostrar. Los nombres de personas se almacenan sin cambiar su normalización y se comparan tras normalizar.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una etiqueta se corta al traducir** — causa: contenedor sin holgura para la expansión. Corrección: pseudolocalización y maquetación flexible. ([SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una pseudolocalización transforma el texto fuente (acentos, relleno, corchetes) para detectar cadenas truncadas, concatenaciones y texto fijo en el código sin traducir nada. ([SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Problemas](./problemas.md), [Internacionalización](../i/internacionalizacion.md), [Locale](../l/locale.md), [Localización](../l/localizacion.md), [Normalización Unicode](../n/normalizacion-unicode.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Unicode CLDR: reglas de plural](https://cldr.unicode.org/index/cldr-spec/plural-rules) — categorías de plural por lengua; autoridad: Unicode Consortium.
- [Unicode TR35: números](https://www.unicode.org/reports/tr35/tr35-numbers.html) — formatos y patrones de números por región; autoridad: Unicode Consortium.
- [Unicode UAX #15: formas de normalización](https://www.unicode.org/reports/tr15/) — NFC y NFD; autoridad: Unicode Consortium.
- [Unicode UAX #29: segmentación de texto](https://www.unicode.org/reports/tr29/) — grafemas, palabras y oraciones; autoridad: Unicode Consortium.
- [W3C Internationalization: ¿qué es la internacionalización?](https://www.w3.org/International/questions/qa-i18n) — conceptos y buenas prácticas; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Prueba unitaria](./prueba-unitaria.md) · [PSI →](./psi.md)
