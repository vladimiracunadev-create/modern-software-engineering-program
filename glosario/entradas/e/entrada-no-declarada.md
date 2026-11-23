# Entrada no declarada

[↑ Glosario](../../README.md) · [← Entrada de portafolio comprobable](./entrada-de-portafolio-comprobable.md) · [Entradas de frontera →](./entradas-de-frontera.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Dato que el build lee y que no figura en su lista de entradas.

Definición de trabajo de [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md).

## Por qué importa

La clase donde se define, [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), existe con este propósito: la clase existe para que puedas responder, con evidencia y no con una promesa, a la pregunta «¿este binario sale de este código?».

## Cómo funciona

Según [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md):

Cuando dos builds difieren, el hash completo no dice dónde. La técnica es comparar por partes: abrir ambos archivos, listar las entradas y comparar cada una; la primera entrada distinta apunta a la entrada no declarada. En la clase, dos builds con una fecha incrustada difirieron en un solo archivo de 42 (`pyproject.toml`). Existen herramientas que automatizan este paso (comparadores de archivos que descomprimen y comparan recursivamente), pero el principio es el mismo y se puede hacer con la biblioteca estándar. Es también el modo de convertir una discrepancia en una acción: el archivo que difiere indica qué entrada falta por declarar o neutralizar.

Según [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** el revisor externo obtiene un hash distinto del publicado y la sospecha recae en el release. **Hipótesis rivales:** (a) el release fue alterado; (b) hubo una dependencia distinta; (c) el build incrusta un dato del entorno. **Prueba:** compara ambos archivos por entrada; si solo difiere un archivo y la diferencia es una cadena de fecha, la causa es (c). **Conclusión:** el build no es reproducible por una entrada no declarada. **Regresión:** añade al CI una segunda construcción en un entorno distinto que compare huellas, y una prueba que falle si el artefacto contiene una fecha, una ruta absoluta o un nombre de usuario.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md):

El equipo escribe el script de empaquetado de la API de entregas con cuatro reglas: ordena los nombres, fija la fecha a la del commit etiquetado (la variable `SOURCE_DATE_EPOCH`), fija modo y sistema de creación de cada entrada y excluye cualquier archivo generado que contenga rutas o fechas. Declara sus entradas en un archivo (`build-inputs.md`) con el commit, la versión de Python, la lista de dependencias con huella y el comando exacto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El build «funciona» pero lee una variable** — causa: entrada no declarada. Corrección: ejecutar con un entorno vacío y sin red. ([SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La técnica es comparar por partes: abrir ambos archivos, listar las entradas y comparar cada una; la primera entrada distinta apunta a la entrada no declarada. ([SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Build hermético](../b/build-hermetico.md), [Build reproducible](../b/build-reproducible.md), [Huella](../h/huella.md), [Normalizar](../n/normalizar.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-469 — Build reproducible y hermético](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reproducible Builds: definición](https://reproducible-builds.org/docs/definition/) — qué es un build reproducible; autoridad: proyecto Reproducible Builds.
- [Reproducible Builds: SOURCE_DATE_EPOCH](https://reproducible-builds.org/docs/source-date-epoch/) — fecha fija para el build; autoridad: proyecto Reproducible Builds.
- [Lamb y Zacchiroli, «Reproducible Builds: Increasing the Integrity of Software Supply Chains»](https://doi.org/10.1109/MS.2021.3073045) — motivación y técnicas; autoridad: IEEE Software.
- [Thompson, «Reflections on trusting trust»](https://doi.org/10.1145/358198.358210) — compiladores comprometidos; autoridad: Communications of the ACM.

---

[↑ Glosario](../../README.md) · [← Entrada de portafolio comprobable](./entrada-de-portafolio-comprobable.md) · [Entradas de frontera →](./entradas-de-frontera.md)
