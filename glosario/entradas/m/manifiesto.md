# Manifiesto

[↑ Glosario](../../README.md) · [← Manejador](./manejador.md) · [Manifiesto de aplicación web →](./manifiesto-de-aplicacion-web.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

En el programa, un **manifiesto** es una lista de elementos con su identificador y su huella, que permite verificar un conjunto. Tiene varios usos según la clase: en [SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md), la lista de resúmenes de los archivos de evidencia en el momento de una revisión; en [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) y [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), la lista de artefactos o ficheros de un paquete con la huella de cada uno; en [SE-368](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md), la lista de archivos de una versión de una tabla de lakehouse; en [SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md), el archivo con las huellas, la semilla, las versiones y las métricas de un modelo; en [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), el archivo estructurado que describe la pregunta, el plan, el entorno, los datos, los resultados, el veredicto y los límites de un informe. No es el manifiesto de una aplicación web ni el manifiesto ágil.

## Por qué importa

Hace detectable un cambio que las demás comprobaciones no ven. Un manifiesto fija qué había en el conjunto en un momento dado; comparándolo después se descubre qué cambió. Cambia la confianza en un paquete o una versión: se verifica en lugar de suponer.

## Cómo funciona

El mecanismo es una lista de pares (elemento, huella), donde la huella es un resumen criptográfico (por ejemplo SHA-256) del contenido. Si el contenido cambia, la huella cambia. Dos usos ilustran su valor.

**Evidencia ([SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md)).** Las comprobaciones de contenido no ven un cambio que mantenga todas las referencias válidas. Si se edita el texto de un requisito (REQ-02 pasa de «la puerta abierta» a «abierta o entreabierta»), todas las pruebas siguen enlazadas y pasan, y el paquete sigue «en verde», pero la prueba verificó un requisito anterior. La defensa mínima es un manifiesto con el SHA-256 de cada archivo de evidencia en el momento de la revisión: al comparar, el archivo editado aparece con otra huella y la revisión debe repetirse.

**Datos ([SE-368](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md)).** Una tabla de un lakehouse no es una carpeta de archivos sino la lista de archivos de una versión, guardada en un manifiesto. Una escritura añade archivos nuevos y publica una **nueva versión del manifiesto** con un único renombrado atómico. Un lector que abrió la versión 1 sigue viendo sus archivos mientras una compactación prepara la versión 2; un lector nuevo ve la 2. Así se logran lecturas consistentes durante los cambios.

En los paquetes de [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) y [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), el manifiesto permite verificar la integridad de lo recibido antes de usarlo.

## Ejemplo

Un paquete de evidencia tiene tres archivos. Su manifiesto registra `requisitos.md: 9f2c…`, `pruebas.md: 41ab…` y `resultados.json: c07d…`. Tras la revisión, alguien edita `requisitos.md`. Al verificar, la huella de ese archivo difiere y la revisión se declara obsoleta, aunque todos los enlaces sigan válidos. (Ilustración del mecanismo de [SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md); las huellas son ficticias.)

## Errores y confusiones comunes

- **Creer que «en verde» implica que lo revisado es lo vigente.**
- **Manifiesto sin verificar** nunca.
- **Almacenar el manifiesto junto al contenido sin protegerlo**: quien altera el contenido altera también la lista.
- **Confundir manifiesto con índice**: el índice dice dónde está; el manifiesto, qué contenido tiene.

## Límites y cuándo no aplica

Un manifiesto prueba integridad, no corrección. Protege contra cambios si la propia lista está protegida (firmada o guardada aparte). Para conjuntos que cambian constantemente, mantenerlo a mano es impracticable y se genera automáticamente.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](../a/artefacto.md), [Entorno](../e/entorno.md), [Evidencia](../e/evidencia.md), [Huella](../h/huella.md), [Afirmación refutable](../a/afirmacion-refutable.md), [Alcance de un cambio](../a/alcance-de-un-cambio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.
- [SE-612 — Proyecto: sistema de ML operable con evidencia](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (30 clases más lo mencionan; las que más):

[SE-228](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md), [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md), [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gotel y Finkelstein, «An analysis of the requirements traceability problem» (ICRE, 1994)](https://doi.org/10.1109/ICRE.1994.292398) — definición y problemas de la trazabilidad de requisitos; autoridad: IEEE International Conference on Requirements Engineering.
- [Cleland-Huang et al., «Software traceability: trends and future directions» (FOSE, 2014)](https://doi.org/10.1145/2593882.2593891) — técnicas de creación y mantenimiento de enlaces; autoridad: ACM Future of Software Engineering.
- [FIPS 180-4: Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) — especificación de SHA-256; autoridad: NIST.
- [Git: gitattributes](https://git-scm.com/docs/gitattributes) — control de los saltos de línea y de las conversiones; autoridad: proyecto Git.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — requisitos, configuración y calidad de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Manejador](./manejador.md) · [Manifiesto de aplicación web →](./manifiesto-de-aplicacion-web.md)
