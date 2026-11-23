# Auto-actualización

[↑ Glosario](../../README.md) · [← Autenticación](./autenticacion.md) · [Autocompletado →](./autocompletado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Mecanismo por el cual la aplicación consulta, descarga e instala su propia versión nueva.

Definición de trabajo de [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md).

## Por qué importa

La clase donde se define, [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md), existe con este propósito: la clase existe para que decidas cómo llega tu software al equipo de otra persona, qué ocurre cuando la instalación o la actualización se interrumpe y cuántas versiones distintas estarán en uso al mismo tiempo.

## Cómo funciona

Según [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md):

Hay cuatro grandes formas. En un **gestor de paquetes** (el del sistema operativo o el de un lenguaje), el gestor descarga, verifica, instala y actualiza; tú publicas en un índice y heredas su modelo de confianza y de dependencias. Un **instalador** nativo (MSI, `.pkg`, `.deb`) copia archivos, registra metadatos y puede ejecutar acciones con privilegios; tiene mucho poder y mucha superficie. Un **binario autónomo** (un archivo ejecutable o un archivo comprimido que se descomprime) es lo más simple de distribuir y deja al usuario la responsabilidad de actualizar. La **auto-actualización** hace que la propia aplicación consulte un canal, descargue y se reemplace; da control al equipo y exige diseñar con cuidado el canal y la instalación atómica.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md):

El procedimiento de actualización de `entregas-cli` descarga el paquete y su manifiesto firmado a un directorio temporal dentro de la misma partición que la instalación, verifica la firma con la clave incorporada y la secuencia, calcula la huella de cada archivo, descomprime en `versiones/2.0.0/`, ejecuta la migración de configuración sobre una copia y una comprobación de humo (`entregas --version` y una subida de prueba a un entorno de ensayo) y cambia el puntero `actual` con un renombrado.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md)) son:

- **El programa no arranca tras una actualización interrumpida** — causa: archivos de dos versiones. Corrección: directorio nuevo y activación atómica.
- **Se instala una descarga corrupta** — causa: no se verifica antes de activar. Corrección: verificar huellas y firma sobre el directorio preparado.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron cuatro experimentos: una inyección de fallos con archivos reales en un directorio temporal (resultado idéntico en Windows 11 con CPython 3.12.9 y en Ubuntu bajo WSL2 con 3.12.3) y una simulación de 20 000 clientes con semilla fija.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Mecanismo](../m/mecanismo.md), [Versión](../v/version.md), [Activación](./activacion.md), [Instalación atómica](../i/instalacion-atomica.md), [Sesgo de versiones](../s/sesgo-de-versiones.md), [Versión mínima soportada](../v/version-minima-soportada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-477 — Instaladores, paquetes y actualizaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md).

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

[↑ Glosario](../../README.md) · [← Autenticación](./autenticacion.md) · [Autocompletado →](./autocompletado.md)
