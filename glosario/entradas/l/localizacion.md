# Localización

[↑ Glosario](../../README.md) · [← Localidad](./localidad.md) · [Lockfile →](./lockfile.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Adaptación de un producto internacionalizado a una lengua y región concretas.

Definición de trabajo de [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md).

## Por qué importa

En [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md), el tema «Internacionalización, localización y traducción» importa porque fija quién hace qué y cuándo.

## Cómo funciona

Según [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md):

Internacionalizar es preparar el producto para cualquier lengua y región: texto fuera del código, formatos configurables, unicode correcto y maquetación flexible. Localizar es adaptar a una lengua y región concretas: textos, formatos, imágenes, convenciones. Traducir es una parte de la localización. Internacionalizar primero evita que cada nueva lengua obligue a tocar el código; saltarlo convierte cada traducción en una fuente de defectos.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md):

En la plataforma, los mensajes viven en recursos por locale con un formato que admite plurales y géneros, y ninguna cadena se construye por concatenación. Una prueba comprueba que cada clave existe en todos los locales con las categorías de plural que exige su lengua; otra aplica pseudolocalización y falla si una etiqueta se trunca; las fechas se guardan en ISO 8601 y los números sin separador de miles, y se formatean al mostrar. Los nombres de personas se almacenan sin cambiar su normalización y se comparan tras normalizar.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md)) son:

- **«1 entregas» o «2 entrega»** — causa: regla de plural de una sola lengua o concatenación. Corrección: mensajes completos con categorías de plural por locale.
- **Dos nombres iguales se tratan como distintos** — causa: distinta composición Unicode sin normalizar. Corrección: normalizar a NFC al comparar.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** las lecturas aplican a mano las convenciones de dos configuraciones y no consultan una biblioteca de localización; los factores de expansión son un supuesto del autor, no una medición de traducciones reales. ([SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Producto](../p/producto.md), [Región](../r/region.md), [Internacionalización](../i/internacionalizacion.md), [Locale](./locale.md), [Normalización Unicode](../n/normalizacion-unicode.md), [Pseudolocalización](../p/pseudolocalizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-177 — Internacionalización, localización y formatos culturales](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md), [SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md), [SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md), [SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md), [SE-063](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md), [SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md).

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

[↑ Glosario](../../README.md) · [← Localidad](./localidad.md) · [Lockfile →](./lockfile.md)
