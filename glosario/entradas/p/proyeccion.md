# Proyección

[↑ Glosario](../../README.md) · [← Proxy de inyección](./proxy-de-inyeccion.md) · [Proyecto nuevo →](./proyecto-nuevo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Transformación de coordenadas geográficas a un plano, que distorsiona áreas, ángulos o distancias.

Definición de trabajo de [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md).

## Por qué importa

En [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md), el tema «Sistemas de referencia y proyecciones» importa porque define qué significa un par de números y qué distorsión introduce plano.

## Cómo funciona

Según [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md):

Un par de números `(latitud, longitud)` solo significa algo respecto de un **sistema de referencia**: el más usado en intercambio es WGS 84, el de los receptores de navegación y el que fija GeoJSON. La Tierra no es una esfera ni un plano, sino algo próximo a un elipsoide; una **proyección** convierte coordenadas geográficas a un plano y siempre distorsiona algo (áreas, ángulos, distancias). Para medir distancias o áreas en una región se usa una proyección adecuada a esa región, no una universal. Mezclar datos en sistemas distintos sin transformar produce desplazamientos de metros a cientos de metros que parecen errores del dato.

## Ejemplo

Caso medido en la sección «Sistemas de referencia y proyecciones» de [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md):

Un par de números `(latitud, longitud)` solo significa algo respecto de un **sistema de referencia**: el más usado en intercambio es WGS 84, el de los receptores de navegación y el que fija GeoJSON. La Tierra no es una esfera ni un plano, sino algo próximo a un elipsoide; una **proyección** convierte coordenadas geográficas a un plano y siempre distorsiona algo (áreas, ángulos, distancias). Para medir distancias o áreas en una región se usa una proyección adecuada a esa región, no una universal.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **«Cercanías» que están más lejos de lo mostrado** — causa: distancia en grados tratada como plano. Corrección: haversine o proyección adecuada, con prueba por latitud. ([SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La Tierra no es una esfera ni un plano, sino algo próximo a un elipsoide; una **proyección** convierte coordenadas geográficas a un plano y siempre distorsiona algo (áreas, ángulos, distancias). ([SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Hora civil](../h/hora-civil.md), [Índice de rejilla](../i/indice-de-rejilla.md), [Instante](../i/instante.md), [Sistema de referencia](../s/sistema-de-referencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-297 — Sistemas geoespaciales y temporales](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), [SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md), [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md).

**Aparece en los casos de estudio:** [Quibi](../../../casos/fallo/quibi.md).

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

[↑ Glosario](../../README.md) · [← Proxy de inyección](./proxy-de-inyeccion.md) · [Proyecto nuevo →](./proyecto-nuevo.md)
