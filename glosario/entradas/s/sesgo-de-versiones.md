# Sesgo de versiones

[↑ Glosario](../../README.md) · [← Sesgo de selección](./sesgo-de-seleccion.md) · [Sesgo del resultado →](./sesgo-del-resultado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Coexistencia de versiones distintas en uso por la cola larga de clientes que actualizan con retraso.

Definición de trabajo de [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md).

## Por qué importa

En [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md), el tema «Sesgo de versiones» importa porque los clientes no actualizan a la vez.

## Cómo funciona

Según [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md), en la sección «Sesgo de versiones»:

Se simulan 20 000 clientes que abren la aplicación cada 1, 2, 3, 7, 14, 30, 60 o 120 días (en proporciones iguales, un supuesto) durante 180 días, con un lanzamiento cada 14 días y actualización al abrir. Se mide cuántas versiones de retraso tiene cada cliente en los días 30, 90 y 180.

**Cómo leer la figura.** Cada barra es un día y se divide en el porcentaje de clientes al día (turquesa), con 1 de retraso (gris), con 2 o 3 (dorado) y con 4 o más (coral). Mira cómo aparece el tramo coral entre el día 30 y el 90: con el tiempo, una parte de la flota se queda muy atrás. **Dónde deja de valer:** las frecuencias de apertura y su reparto son un supuesto del autor, y se supone que todos actualizan al abrir; en la realidad algunas personas rechazan o difieren la actualización y otras no tienen red. La forma (una cola de clientes muy atrasados) sí es habitual y el número exacto depende del producto.

## Ejemplo

Caso medido en la sección «Sesgo de versiones y rutas de actualización» de [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md):

En el servidor, todos los clientes usan la versión que despliegas. En los equipos de las personas, la distribución de versiones es una **cola larga**: unos actualizan el mismo día, otros cuando abren la aplicación, otros meses después o nunca. Con un lanzamiento cada 14 días y clientes que abren la aplicación cada 1, 2, 3, 7, 14, 30, 60 o 120 días, aparecen en seis meses 22 caminos de actualización distintos y una parte apreciable de los saltos cruza tres o más versiones.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md)) son:

- **El programa no arranca tras una actualización interrumpida** — causa: archivos de dos versiones. Corrección: directorio nuevo y activación atómica.
- **Se instala una descarga corrupta** — causa: no se verifica antes de activar. Corrección: verificar huellas y firma sobre el directorio preparado.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron cuatro experimentos: una inyección de fallos con archivos reales en un directorio temporal (resultado idéntico en Windows 11 con CPython 3.12.9 y en Ubuntu bajo WSL2 con 3.12.3) y una simulación de 20 000 clientes con semilla fija.

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
