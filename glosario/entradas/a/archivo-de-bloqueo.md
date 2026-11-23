# Archivo de bloqueo

[↑ Glosario](../../README.md) · [← Árbol, raíz y subárbol](./arbol-raiz-y-subarbol.md) · [Archivo de gestión de riesgos →](./archivo-de-gestion-de-riesgos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Documento que fija la versión exacta y la huella de cada pieza de la clausura.

Definición de trabajo de [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md): Archivo que fija las versiones exactas de todas las dependencias para repetir una instalación.

## Por qué importa

En [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), el tema «Archivo de bloqueo y huellas» importa porque fijar versiones y huellas hace comparable el build.

## Cómo funciona

Según [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md):

El manifiesto suele declarar **rangos**: «cualquier versión compatible con 2.3». Un **resolvedor** elige, en el momento de instalar, las versiones concretas que satisfacen todos los rangos a la vez. Mientras los paquetes publican versiones nuevas, el resultado cambia: el mismo manifiesto instalado hoy y dentro de un mes produce árboles distintos. Esto no es un defecto del resolvedor, es el significado de un rango. Para un servicio que se despliega, esa deriva es una entrada no declarada del build: contradice lo que se enseñó en `SE-469`. La solución es separar dos documentos con funciones distintas: el **manifiesto** (qué rango acepto) y el **archivo de bloqueo** (qué versiones concretas, con su huella, se instalaron y se probaron).

Según [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md):

El equipo de la API de entregas mantiene un manifiesto con seis dependencias directas y rangos amplios, y un archivo de bloqueo con 31 piezas, versiones exactas y huellas. Instalar en el CI exige las huellas y rechaza cualquier archivo distinto. Las actualizaciones llegan como solicitudes semanales automáticas que modifican el bloqueo; cada una muestra la diferencia de versiones y de huellas y pasa las pruebas antes de fusionarse. Una biblioteca de análisis de fechas de 300 líneas se vendoriza en `third_party/` con un archivo `ORIGEN.md` (versión, huella del original, diferencias aplicadas) y un dueño nombrado; un trabajo mensual compara la copia con la última versión publicada. Cuando se anuncia una vulnerabilidad, el equipo consulta el bloqueo y la copia, no el manifiesto, para responder si está afectado.

## Ejemplo

Ejemplo de [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) (sección «Ejemplo profesional»):

El equipo de la API de entregas mantiene un manifiesto con seis dependencias directas y rangos amplios, y un archivo de bloqueo con 31 piezas, versiones exactas y huellas. Instalar en el CI exige las huellas y rechaza cualquier archivo distinto. Las actualizaciones llegan como solicitudes semanales automáticas que modifican el bloqueo; cada una muestra la diferencia de versiones y de huellas y pasa las pruebas antes de fusionarse. Una biblioteca de análisis de fechas de 300 líneas se vendoriza en `third_party/` con un archivo `ORIGEN.md` (versión, huella del original, diferencias aplicadas) y un dueño nombrado; un trabajo mensual compara la copia con la última versión publicada.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El CI falla sin cambios en el repositorio** — causa: resolución sin bloqueo. Corrección: archivo de bloqueo con versiones y huellas. ([SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Mira que sin archivo de bloqueo el conjunto cambia casi todos los días con novedad, y con él casi nunca. ([SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md))
- Construye dos días seguidos sin archivo de bloqueo con una publicación nueva entre ambos. ([SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](../d/dependencia.md), [Documento](../d/documento.md), [Huella](../h/huella.md), [Versión](../v/version.md), [Clausura transitiva](../c/clausura-transitiva.md), [Dependencia atrasada](../d/dependencia-atrasada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-103](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), [SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md), [SE-108](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md), [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: importlib.metadata](https://docs.python.org/3/library/importlib.metadata.html) — lectura de metadatos de distribuciones; autoridad: documentación de Python.
- [PEP 440](https://peps.python.org/pep-0440/) — versiones y especificadores; autoridad: Python Enhancement Proposals.
- [pip: instalaciones seguras](https://pip.pypa.io/en/stable/topics/secure-installs/) — fijar y comprobar huellas; autoridad: documentación de pip.
- [Ohm et al., «Backstabber's Knife Collection»](https://doi.org/10.1007/978-3-030-52683-2_2) — ataques a paquetes de código abierto; autoridad: DIMVA 2020, Springer.
- [NVD: CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) — ejemplo de vulnerabilidad en una pieza transitiva; autoridad: NIST National Vulnerability Database.

---

[↑ Glosario](../../README.md) · [← Árbol, raíz y subárbol](./arbol-raiz-y-subarbol.md) · [Archivo de gestión de riesgos →](./archivo-de-gestion-de-riesgos.md)
