# Sistema de referencia

[↑ Glosario](../../README.md) · [← Sistema de IA](./sistema-de-ia.md) · [Sistema operativo →](./sistema-operativo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Convención que da significado a un par de coordenadas respecto de una forma y un origen de la Tierra.

Definición de trabajo de [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md).

## Por qué importa

En [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md), el tema «Sistemas de referencia y proyecciones» importa porque define qué significa un par de números y qué distorsión introduce plano.

## Cómo funciona

Según [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md):

Un par de números `(latitud, longitud)` solo significa algo respecto de un **sistema de referencia**: el más usado en intercambio es WGS 84, el de los receptores de navegación y el que fija GeoJSON. La Tierra no es una esfera ni un plano, sino algo próximo a un elipsoide; una **proyección** convierte coordenadas geográficas a un plano y siempre distorsiona algo (áreas, ángulos, distancias). Para medir distancias o áreas en una región se usa una proyección adecuada a esa región, no una universal. Mezclar datos en sistemas distintos sin transformar produce desplazamientos de metros a cientos de metros que parecen errores del dato.

Según [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md):

Para «cercanía» a escala de ciudad o país, sí. Para catastro, ingeniería o rutas largas necesitas un elipsoide y un sistema de referencia adecuado.

## Ejemplo

Ejemplo de [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md) (sección «Preguntas frecuentes»):

Para «cercanía» a escala de ciudad o país, sí. Para catastro, ingeniería o rutas largas necesitas un elipsoide y un sistema de referencia adecuado.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md)) son:

- **«Cercanías» que están más lejos de lo mostrado** — causa: distancia en grados tratada como plano. Corrección: haversine o proyección adecuada, con prueba por latitud.
- **Una ruta mide la vuelta al mundo** — causa: resta de longitudes sin tratar el antimeridiano. Corrección: diferencia mínima módulo 360 y prueba en ±180°.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un par de números `(latitud, longitud)` solo significa algo respecto de un **sistema de referencia**: el más usado en intercambio es WGS 84, el de los receptores de navegación y el que fija GeoJSON. ([SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Origen](../o/origen.md), [Hora civil](../h/hora-civil.md), [Índice de rejilla](../i/indice-de-rejilla.md), [Instante](../i/instante.md), [Proyección](../p/proyeccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [IANA, Time Zone Database](https://www.iana.org/time-zones) — reglas de las zonas horarias; autoridad: IANA.
- [IETF, RFC 3339: Date and Time on the Internet](https://www.rfc-editor.org/rfc/rfc3339) — formato de marcas de tiempo; autoridad: IETF.
- [IETF, RFC 7946: The GeoJSON Format](https://www.rfc-editor.org/rfc/rfc7946) — formato de geometrías en WGS 84 y cruce del antimeridiano; autoridad: IETF.
- [OGC, Simple Features](https://www.ogc.org/standards/sfa/) — modelo de geometrías y operaciones espaciales; autoridad: Open Geospatial Consortium.
- [PostGIS, documentación](https://postgis.net/documentation/) — tipos, funciones e índices espaciales; autoridad: proyecto PostGIS.

---

[↑ Glosario](../../README.md) · [← Sistema de IA](./sistema-de-ia.md) · [Sistema operativo →](./sistema-operativo.md)
