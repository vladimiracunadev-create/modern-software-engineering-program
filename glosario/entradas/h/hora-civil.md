# Hora civil

[↑ Glosario](../../README.md) · [← Hook](./hook.md) · [Horizonte de equilibrio →](./horizonte-de-equilibrio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Hora que marca el reloj de pared en una zona según sus reglas vigentes.

Definición de trabajo de [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md).

## Por qué importa

La clase donde se define, [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md), existe con este propósito: la clase existe para que trates una coordenada y un instante como datos con modelo propio: una posición depende de un sistema de referencia y de una forma de la Tierra, y un momento depende de una zona y de reglas que cambian.

## Cómo funciona

Según [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md):

Un **instante** es un punto de la línea del tiempo, independiente de cualquier reloj; se guarda mejor en UTC. La **hora civil** es lo que marca el reloj de pared en una zona y depende de reglas decididas por cada jurisdicción y modificadas con frecuencia; la base de datos de zonas horarias de IANA las recoge. Un desplazamiento fijo respecto de UTC (como en el formato del RFC 3339) identifica un instante pero no conserva la regla: «UTC−4» no dice qué hora será dentro de seis meses. Los cambios de hora crean horas locales **inexistentes** (el reloj salta) y **ambiguas** (el reloj repite), y días de 23 o 25 horas. Una tarea recurrente «a las 09:00» debe guardar la hora local y la zona, no un instante fijo.

Según [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md):

El equipo de la plataforma guarda cada sesión con tres campos: el instante de inicio en UTC, el identificador de la zona del docente y la hora local de la regla («09:00»), y calcula la hora civil de cada participante en el momento de mostrarla, usando la base de datos de zonas horarias del sistema y registrando la versión de la base en la salida. Los intercambios usan el formato RFC 3339. Las sedes se almacenan como longitud y latitud en WGS 84 con cinco decimales (cerca de un metro); la búsqueda de sedes cercanas usa haversine sobre un prefiltro de rejilla de 5 km, y el cruce del antimeridiano se prueba con una sede en cada lado.

## Ejemplo

Ejemplo de [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma guarda cada sesión con tres campos: el instante de inicio en UTC, el identificador de la zona del docente y la hora local de la regla («09:00»), y calcula la hora civil de cada participante en el momento de mostrarla, usando la base de datos de zonas horarias del sistema y registrando la versión de la base en la salida. Los intercambios usan el formato RFC 3339.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md)) son:

- **«Cercanías» que están más lejos de lo mostrado** — causa: distancia en grados tratada como plano. Corrección: haversine o proyección adecuada, con prueba por latitud.
- **Una ruta mide la vuelta al mundo** — causa: resta de longitudes sin tratar el antimeridiano. Corrección: diferencia mínima módulo 360 y prueba en ±180°.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **hora civil** es lo que marca el reloj de pared en una zona y depende de reglas decididas por cada jurisdicción y modificadas con frecuencia; la base de datos de zonas horarias de IANA las recoge. ([SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Reloj de pared](../r/reloj-de-pared.md), [Regla](../r/regla.md), [Zona](../z/zona.md), [Índice de rejilla](../i/indice-de-rejilla.md), [Instante](../i/instante.md), [Proyección](../p/proyeccion.md).
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

[↑ Glosario](../../README.md) · [← Hook](./hook.md) · [Horizonte de equilibrio →](./horizonte-de-equilibrio.md)
