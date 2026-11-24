# Archivo de bloqueo

[↑ Glosario](../../README.md) · [← Árbol, raíz y subárbol](./arbol-raiz-y-subarbol.md) · [Archivo de gestión de riesgos →](./archivo-de-gestion-de-riesgos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Un **archivo de bloqueo** (*lockfile*) es el documento que fija la versión exacta y la huella de cada pieza de la clausura de dependencias ([SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md)); en [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) es el archivo que fija las versiones exactas de todas las dependencias para repetir una instalación.

## Por qué importa

El manifiesto suele declarar **rangos** («cualquier versión compatible con 2.3»). Un resolvedor elige en el momento de instalar las versiones concretas que satisfacen todos los rangos; mientras los paquetes publican versiones nuevas, el resultado cambia. Ese no es un defecto del resolvedor, es el significado de un rango. Para un servicio que se despliega, es una entrada no declarada del build.

## Cómo funciona

El bloqueo registra la **clausura** completa (directas y transitivas) con versión exacta y huella. Instalar desde él exige las huellas y rechaza cualquier archivo distinto. Las actualizaciones llegan como cambios revisables del bloqueo, que muestran la diferencia de versiones y de huellas. Además es la base para el inventario (SBOM) y para saber si un aviso de vulnerabilidad afecta.

## Ejemplo

[SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md): el equipo de la API de entregas mantiene un manifiesto con seis dependencias directas y rangos amplios, y un bloqueo con 31 piezas, versiones exactas y huellas. El CI instala exigiendo las huellas; las actualizaciones llegan como solicitudes semanales automáticas que modifican el bloqueo y pasan las pruebas antes de fusionarse. La clase observa que sin archivo de bloqueo el conjunto cambia casi todos los días con novedad, y con él casi nunca.

## Errores y confusiones comunes

**El CI falla sin cambios en el repositorio.** Resolución sin bloqueo: el árbol cambió al publicarse una versión; archivo de bloqueo con versiones y huellas.

## Límites y cuándo no aplica

En una biblioteca que otros consumen, el bloqueo no se distribuye con ella: manda el rango del manifiesto. El bloqueo fija lo publicado, pero no lo audita.

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
