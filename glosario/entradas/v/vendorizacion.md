# Vendorización

[↑ Glosario](../../README.md) · [← Vecino ruidoso](./vecino-ruidoso.md) · [Ventana →](./ventana.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

**Vendorizar** (de *vendoring*) es copiar el código de una dependencia dentro del repositorio propio. Es la definición de trabajo de [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), dentro de la cadena de suministro. El código de terceros pasa a vivir en tu árbol de archivos (a menudo en un directorio `vendor/`) en lugar de resolverse desde un índice externo al construir.

## Por qué importa

Es una decisión con ventajas y costos opuestos, y tomarla sin verlos produce el peor resultado. [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) lo resume: una copia sin dueño es la peor de las opciones, porque tiene todos los riesgos de la dependencia y ninguna de sus ventajas.

## Cómo funciona

[SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) enumera ventajas y costos.

**Ventajas:**
- no depende de un índice externo (ni de su disponibilidad ni de que el paquete siga publicado);
- se puede **revisar línea a línea**;
- se puede **parchear** sin esperar al autor.

**Costos:**
- la copia **deja de recibir actualizaciones** automáticamente y, si nadie es dueño, envejece;
- los avisos de vulnerabilidad se emiten para el *paquete publicado*, y una herramienta que mire solo el manifiesto **no verá la copia**.

La causa del segundo costo es que el vínculo entre la copia y su origen existía en el manifiesto y se perdió al copiar. Por eso una copia bien gestionada necesita cuatro cosas: un **dueño**, un **registro de su origen** (versión y huella del original), un **procedimiento de actualización** y una **comprobación automática** de que la copia coincide con el original o declara sus diferencias.

## Ejemplo

Un equipo copia una biblioteca de análisis de fechas en `vendor/fechas/`. Añade un archivo `ORIGEN` con la versión y la huella del original, nombra a una persona responsable y una tarea de CI que descarga esa versión del original y compara con la copia, fallando si hay diferencias no declaradas en un archivo de parches. Cuando aparece un aviso de vulnerabilidad para esa versión, el inventario de componentes (generado desde el bloqueo y el registro de copias, no solo desde el manifiesto) permite saber de inmediato que el repositorio está afectado. Sin ese registro, nadie lo sabría. (Ilustración del mecanismo de [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md).)

## Errores y confusiones comunes

- **El CI falla sin cambios en el repositorio.** Resolución sin bloqueo; corrección: archivo de bloqueo con versiones y huellas ([SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md)).
- **No se sabe si un aviso afecta.** Inventario solo del manifiesto; corrección: inventario de la clausura desde el bloqueo (y de las copias vendorizadas).
- **Vendorizar «para no preocuparse».** Se cambia un riesgo por otro y se hereda el trabajo de actualizar.
- **Parchear sin registrar.** La próxima actualización pierde el parche o lo pisa sin aviso.

## Límites y cuándo no aplica

[SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) declara que sus definiciones son operativas para la API de entregas y que midió, en la práctica, los metadatos de dos entornos de Python (349 y 63 distribuciones, que difieren por diseño). No se sigue que vendorizar sea la mejor opción: para la mayoría de las dependencias, un bloqueo con versiones y huellas da la reproducibilidad con mucho menor costo de mantenimiento. Vendorizar compensa cuando se necesita independencia del índice, revisión total o parches propios, y solo si hay quien mantenga la copia. Y no resuelve las dependencias transitivas de lo copiado: también hay que gestionarlas.

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
