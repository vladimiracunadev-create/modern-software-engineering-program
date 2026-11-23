# Índice de rejilla

[↑ Glosario](../../README.md) · [← Índice compuesto](./indice-compuesto.md) · [Índice secundario →](./indice-secundario.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Estructura que guarda los puntos por celda de un reticulado para limitar los candidatos de una consulta espacial.

Definición de trabajo de [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md).

## Por qué importa

La clase donde se define, [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md), existe con este propósito: la clase existe para que trates una coordenada y un instante como datos con modelo propio: una posición depende de un sistema de referencia y de una forma de la Tierra, y un momento depende de una zona y de reglas que cambian.

## Cómo funciona

[SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el mapa de sedes y el calendario. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md):

El equipo de la plataforma guarda cada sesión con tres campos: el instante de inicio en UTC, el identificador de la zona del docente y la hora local de la regla («09:00»), y calcula la hora civil de cada participante en el momento de mostrarla, usando la base de datos de zonas horarias del sistema y registrando la versión de la base en la salida. Los intercambios usan el formato RFC 3339.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md)) son:

- **«Cercanías» que están más lejos de lo mostrado** — causa: distancia en grados tratada como plano. Corrección: haversine o proyección adecuada, con prueba por latitud.
- **Una ruta mide la vuelta al mundo** — causa: resta de longitudes sin tratar el antimeridiano. Corrección: diferencia mínima módulo 360 y prueba en ±180°.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md)) son: Las definiciones son operativas para el mapa de sedes y el calendario. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún elipsoide, proyección, índice de una base de datos espacial ni la base de zonas horarias: los puntos, la regla de cambio de hora y la rejilla son construcciones del autor. La siguiente clase pasa a la automatización visual y al software sin código.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Candidato](../c/candidato.md), [Celda](../c/celda.md), [Estructura](../e/estructura.md), [Guarda](../g/guarda.md), [Hora civil](../h/hora-civil.md), [Instante](./instante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

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

[↑ Glosario](../../README.md) · [← Índice compuesto](./indice-compuesto.md) · [Índice secundario →](./indice-secundario.md)
