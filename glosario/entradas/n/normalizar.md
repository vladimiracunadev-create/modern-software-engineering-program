# Normalizar

[↑ Glosario](../../README.md) · [← Normalización Unicode](./normalizacion-unicode.md) · [Normativo →](./normativo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Fijar o eliminar toda información del entorno (hora, orden, ruta, usuario) que el formato incrusta.

Definición de trabajo de [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md).

## Por qué importa

La clase donde se define, [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), existe con este propósito: la clase existe para que puedas responder, con evidencia y no con una promesa, a la pregunta «¿este binario sale de este código?».

## Cómo funciona

Según [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md):

Las fuentes de variación más habituales son metadatos que el formato guarda sin que el programador lo pida. La **marca de tiempo** de cada archivo (la hora a la que se creó o se copió) cambia en cada build. El **orden** en que se listan los archivos depende del sistema de archivos y de la herramienta: algunos devuelven los nombres en orden de creación, otros alfabético, otros sin orden definido. Los **permisos** y el propietario varían con la máscara de creación (`umask`) y con el usuario. Las **estructuras sin orden** (un diccionario o un conjunto serializados tal cual) pueden salir en otro orden. Los **saltos de línea** de una fuente cambian si un sistema de control de versiones convierte LF en CRLF al extraer.

Según [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md):

Reproduce el fallo clásico de la clase: **dos construcciones del mismo commit con hashes distintos y nadie sabe por qué**. Construye el árbol dos veces dejando la fecha incrustada sin normalizar.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md):

El equipo escribe el script de empaquetado de la API de entregas con cuatro reglas: ordena los nombres, fija la fecha a la del commit etiquetado (la variable `SOURCE_DATE_EPOCH`), fija modo y sistema de creación de cada entrada y excluye cualquier archivo generado que contenga rutas o fechas. Declara sus entradas en un archivo (`build-inputs.md`) con el commit, la versión de Python, la lista de dependencias con huella y el comando exacto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Cada build produce un hash distinto** — causa: fechas, orden o rutas incrustadas. Corrección: normalizar tiempo y orden; eliminar rutas. ([SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cada vez se deja **una** fuente sin normalizar y se cuenta cuántos hashes distintos aparecen; después se dejan todas y por último ninguna. ([SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md))
- Construye el árbol dos veces dejando la fecha incrustada sin normalizar. ([SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Entorno](../e/entorno.md), [Ruta](../r/ruta.md), [Build hermético](../b/build-hermetico.md), [Build reproducible](../b/build-reproducible.md), [Entrada no declarada](../e/entrada-no-declarada.md), [Huella](../h/huella.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (26 clases más lo mencionan; las que más):

[SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md), [SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md), [SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md), [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md), [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reproducible Builds: definición](https://reproducible-builds.org/docs/definition/) — qué es un build reproducible; autoridad: proyecto Reproducible Builds.
- [Reproducible Builds: SOURCE_DATE_EPOCH](https://reproducible-builds.org/docs/source-date-epoch/) — fecha fija para el build; autoridad: proyecto Reproducible Builds.
- [Lamb y Zacchiroli, «Reproducible Builds: Increasing the Integrity of Software Supply Chains»](https://doi.org/10.1109/MS.2021.3073045) — motivación y técnicas; autoridad: IEEE Software.
- [Thompson, «Reflections on trusting trust»](https://doi.org/10.1145/358198.358210) — compiladores comprometidos; autoridad: Communications of the ACM.

---

[↑ Glosario](../../README.md) · [← Normalización Unicode](./normalizacion-unicode.md) · [Normativo →](./normativo.md)
