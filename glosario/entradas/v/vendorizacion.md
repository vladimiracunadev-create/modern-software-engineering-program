# Vendorización

[↑ Glosario](../../README.md) · [← Vecino ruidoso](./vecino-ruidoso.md) · [Ventana →](./ventana.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Copia del código de una dependencia dentro del repositorio propio.

Definición de trabajo de [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md).

## Por qué importa

En [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), el tema «Vendorización» importa porque copiar elimina un riesgo de disponibilidad y crea otro de mantenimiento.

## Cómo funciona

Según [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), en la sección «Vendorización»:

**Vendorizar** es copiar el código de una dependencia dentro de tu repositorio. Ventajas: no depende de un índice externo, se puede revisar línea a línea, se puede parchear sin esperar al autor. Costos: la copia deja de recibir las actualizaciones automáticamente y, si nadie es dueño, envejece; los avisos de vulnerabilidad se emiten para el paquete publicado, y una herramienta que mire solo el manifiesto no verá la copia. Las copias bien gestionadas tienen un dueño, un registro de su origen (versión y huella del original), un procedimiento de actualización y una comprobación automática de que la copia coincide con el original o declara sus diferencias. Una copia sin dueño es la peor de las opciones: tiene todos los riesgos de la dependencia y ninguna de sus ventajas.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md):

El equipo de la API de entregas mantiene un manifiesto con seis dependencias directas y rangos amplios, y un archivo de bloqueo con 31 piezas, versiones exactas y huellas. Instalar en el CI exige las huellas y rechaza cualquier archivo distinto. Las actualizaciones llegan como solicitudes semanales automáticas que modifican el bloqueo; cada una muestra la diferencia de versiones y de huellas y pasa las pruebas antes de fusionarse.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md)) son:

- **El CI falla sin cambios en el repositorio** — causa: resolución sin bloqueo. Corrección: archivo de bloqueo con versiones y huellas.
- **No se sabe si un aviso afecta** — causa: inventario solo del manifiesto. Corrección: inventario de la clausura desde el bloqueo.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutó una medición real de los metadatos de dos entornos de Python (349 y 63 distribuciones, que difieren por diseño) y tres simulaciones con semilla fija, idénticas en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3).

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](../d/dependencia.md), [Archivo de bloqueo](../a/archivo-de-bloqueo.md), [Clausura transitiva](../c/clausura-transitiva.md), [Dependencia directa](../d/dependencia-directa.md), [Dependencia transitiva](../d/dependencia-transitiva.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-471 — Dependencias directas, transitivas y vendorización](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md).

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

[↑ Glosario](../../README.md) · [← Vecino ruidoso](./vecino-ruidoso.md) · [Ventana →](./ventana.md)
