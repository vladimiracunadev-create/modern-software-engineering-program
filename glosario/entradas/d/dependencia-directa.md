# Dependencia directa

[↑ Glosario](../../README.md) · [← Dependencia del orden](./dependencia-del-orden.md) · [Dependencia directa y transitiva →](./dependencia-directa-y-transitiva.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Pieza que el proyecto declara en su manifiesto.

Definición de trabajo de [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md).

## Por qué importa

La clase donde se define, [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), existe con este propósito: la clase existe para que sepas qué código ajeno ejecuta tu producto, cómo llegó allí y qué haces cuando alguien anuncia que una pieza concreta es vulnerable.

## Cómo funciona

Según [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md):

Una dependencia **directa** es la que tu proyecto declara; una **transitiva** es la que necesita una dependencia tuya, o una dependencia de esa. La **clausura transitiva** es el conjunto de todas las piezas que se instalan y, por tanto, que pueden ejecutarse. El grafo suele tener forma de cola larga: unas pocas bibliotecas muy usadas aparecen en muchas clausuras y muchas bibliotecas aparecen en una sola. Esto tiene una consecuencia de seguridad directa: una pieza muy compartida, cuando falla, afecta a muchos proyectos a la vez, y a un proyecto concreto le llegan por varios caminos. Calcular la clausura exige leer los requisitos de cada pieza instalada y recorrer el grafo, algo que la biblioteca estándar permite con los metadatos de las distribuciones.

Según [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md):

El equipo de la API de entregas mantiene un manifiesto con seis dependencias directas y rangos amplios, y un archivo de bloqueo con 31 piezas, versiones exactas y huellas. Instalar en el CI exige las huellas y rechaza cualquier archivo distinto. Las actualizaciones llegan como solicitudes semanales automáticas que modifican el bloqueo; cada una muestra la diferencia de versiones y de huellas y pasa las pruebas antes de fusionarse. Una biblioteca de análisis de fechas de 300 líneas se vendoriza en `third_party/` con un archivo `ORIGEN.md` (versión, huella del original, diferencias aplicadas) y un dueño nombrado; un trabajo mensual compara la copia con la última versión publicada. Cuando se anuncia una vulnerabilidad, el equipo consulta el bloqueo y la copia, no el manifiesto, para responder si está afectado.

## Ejemplo

Ejemplo de [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) (sección «Ejemplo mínimo»):

Se instalan cuatro paquetes para dos dependencias directas. Registra versión de Python, comando y salida; después añade una dependencia de `ssl` hacia `serial` y comprueba que el tamaño de la clausura no cambia aunque el número de aristas sí.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md)) son:

- **El CI falla sin cambios en el repositorio** — causa: resolución sin bloqueo. Corrección: archivo de bloqueo con versiones y huellas.
- **No se sabe si un aviso afecta** — causa: inventario solo del manifiesto. Corrección: inventario de la clausura desde el bloqueo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una dependencia **directa** es la que tu proyecto declara; una **transitiva** es la que necesita una dependencia tuya, o una dependencia de esa. ([SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Manifiesto](../m/manifiesto.md), [Archivo de bloqueo](../a/archivo-de-bloqueo.md), [Clausura transitiva](../c/clausura-transitiva.md), [Dependencia transitiva](./dependencia-transitiva.md), [Vendorización](../v/vendorizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md), [SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md), [SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md), [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), [SE-051](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md).

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

[↑ Glosario](../../README.md) · [← Dependencia del orden](./dependencia-del-orden.md) · [Dependencia directa y transitiva →](./dependencia-directa-y-transitiva.md)
