# Sesgo de versiones

[↑ Glosario](../../README.md) · [← Sesgo de selección](./sesgo-de-seleccion.md) · [Sesgo del resultado →](./sesgo-del-resultado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

El **sesgo de versiones** es la coexistencia de versiones distintas en uso, producida por la cola larga de clientes que actualizan con retraso. [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md) lo define así en el contexto de la distribución de aplicaciones de escritorio y móviles: aunque se publique una versión nueva, la población en uso nunca es toda de la última.

## Por qué importa

Cambia qué se supone al diseñar un lanzamiento. Quien asume que «todos están en la última versión» rompe a quienes no lo están: un servidor que deja de aceptar un formato antiguo, una migración de datos que exige el cliente nuevo. El sesgo obliga a mantener compatibilidad durante más tiempo del que se cree y a medir la distribución real de versiones antes de retirar algo.

## Cómo funciona

La causa es la diferencia de frecuencia de uso. Un cliente que abre la aplicación a diario se actualiza casi de inmediato; uno que la abre cada dos meses actualiza dos meses después de cada lanzamiento. La flota resultante es una mezcla con una **cola larga** de clientes muy atrasados, aunque el mecanismo de actualización sea automático.

[SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md) lo simula: 20 000 clientes que abren la aplicación cada 1, 2, 3, 7, 14, 30, 60 o 120 días (en proporciones iguales, supuesto del autor) durante 180 días, con un lanzamiento cada 14 días y actualización al abrir. Se mide cuántas versiones de retraso tiene cada cliente en los días 30, 90 y 180. La figura de la clase divide cada día en clientes al día, con 1 de retraso, con 2 o 3 y con 4 o más; el tramo de 4 o más aparece entre el día 30 y el 90: con el tiempo, una parte de la flota queda muy atrás.

## Ejemplo

Un equipo publica cada dos semanas y planea retirar una API antigua «cuando todos hayan actualizado». Con el modelo anterior, aun a los 180 días hay una fracción de clientes con cuatro o más versiones de retraso, justo los que abren la aplicación cada 60 o 120 días. Retirar la API a los 30 días rompería a quienes aún no la han abierto. La decisión correcta es medir la distribución real de versiones, fijar una fecha de retirada anunciada con antelación y, si hay una actualización forzosa, informarla en el propio cliente.

## Errores y confusiones comunes

- **El programa no arranca tras una actualización interrumpida.** Mezcla de archivos de dos versiones; corrección de [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md): directorio nuevo y activación atómica.
- **Se instala una descarga corrupta.** No se verifica antes de activar; verificar huellas y firma sobre el directorio preparado.
- **Suponer que actualizar automáticamente elimina el sesgo.** Solo lo acorta para quien abre la aplicación.
- **Confundirlo con el sesgo estadístico.** Aquí «sesgo» es la composición desigual de la flota, no un error de medición.

## Límites y cuándo no aplica

Las frecuencias de apertura y su reparto en la simulación son un supuesto del autor, y se supone que todos actualizan al abrir; en la realidad, algunas personas rechazan o difieren la actualización y otras no tienen red. La forma (una cola de clientes muy atrasados) sí es habitual y el número exacto depende del producto. No aplica a software que el proveedor controla íntegramente (un servicio web sin cliente instalable), aunque allí puede haber un sesgo equivalente en las integraciones que consumen la API.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cola larga](../c/cola-larga.md), [Versión](../v/version.md), [Activación](../a/activacion.md), [Auto-actualización](../a/auto-actualizacion.md), [Instalación atómica](../i/instalacion-atomica.md), [Versión mínima soportada](../v/version-minima-soportada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [POSIX: rename()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/rename.html) — reemplazo atómico; autoridad: The Open Group.
- [Python: os.replace](https://docs.python.org/3/library/os.html#os.replace) — renombrado con reemplazo; autoridad: documentación de Python.
- [Microsoft: MoveFileExW](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-movefileexw) — reemplazo de archivos en Windows; autoridad: documentación de Microsoft.
- [The Update Framework](https://theupdateframework.io/specification/) — metadatos firmados con secuencia y caducidad; autoridad: proyecto TUF, CNCF.
- [PEP 427: wheel](https://peps.python.org/pep-0427/) — formato de distribución de paquetes de Python; autoridad: Python Enhancement Proposals.

---

[↑ Glosario](../../README.md) · [← Sesgo de selección](./sesgo-de-seleccion.md) · [Sesgo del resultado →](./sesgo-del-resultado.md)
