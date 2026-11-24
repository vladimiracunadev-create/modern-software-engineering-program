# Gestor de versiones

[↑ Glosario](../../README.md) · [← Generador](./generador.md) · [GIL →](./gil.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

En este contexto ([SE-102](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md)), un **gestor de versiones** es una herramienta que **instala y selecciona versiones de *runtimes*** (intérpretes y compiladores como Python, Node o Ruby), por archivo de configuración o por comando. Sirve para que cada proyecto use la versión del lenguaje que declara, sin depender de la que haya instalado el sistema. No debe confundirse con el **control de versiones** del código (como Git), que registra el historial de cambios; este gestor administra qué versión del *runtime* se ejecuta.

## Por qué importa

Proyectos distintos necesitan versiones distintas del mismo lenguaje, y la del sistema suele ser una sola y antigua. Sin gestor, el comando `python` apunta a lo que haya, y el mismo script se comporta distinto en cada máquina. [SE-102](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md) documenta el síntoma: el script usa otro Python en otra máquina porque se invoca `python` a secas. La decisión que cambia es cómo se determina el *runtime* de un proyecto: se declara y se verifica, no se asume.

## Cómo funciona

La mayoría de los gestores usan **shims**: pequeños ejecutables que se colocan al inicio de la ruta de búsqueda (`PATH`) con los nombres de los comandos (`python`, `node`). Al invocar `python`, se ejecuta el *shim*, que consulta qué versión corresponde (por un archivo del proyecto, por una variable o por la configuración global) y delega en el ejecutable adecuado. Tres consecuencias:

- **El *shim* intercepta la resolución** de comandos, de modo que **debe inicializarse en el *shell***; si no, el comando se resuelve contra el sistema y se obtiene otra versión.
- **La configuración versionada** (un archivo con la versión deseada en el repositorio) **expresa intención**, pero no la garantiza: depende de que el gestor la lea.
- **La integración continua debe instalar explícitamente** la versión y **comprobar la versión efectiva**, en lugar de asumir que la intención se cumple.

Fijar el *runtime* no aísla los paquetes instalados: dos proyectos con la misma versión de Python siguen compartiendo el espacio de paquetes global si no usan un entorno virtual ([SE-102](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md)).

## Ejemplo

Un proyecto declara la versión en un archivo del repositorio y la verifica al inicio del script:

```python
import sys
REQUERIDA = (3, 12)
if sys.version_info[:2] != REQUERIDA:
    raise SystemExit(f"Se requiere Python {REQUERIDA[0]}.{REQUERIDA[1]}, "
                     f"se encontró {sys.version.split()[0]} en {sys.executable}")
```

Si otra máquina resuelve `python` a una versión distinta, el fallo es inmediato y dice **cuál** se usó y **dónde** está. Es la corrección del error documentado: declarar la versión y verificarla al inicio. En la misma clase, otra consecuencia: una medición de rendimiento no se repite en otro equipo por compilación o sistema distintos, y la corrección es registrar versión y sistema con cada medición.

## Errores y confusiones comunes

- **Invocar `python` a secas.** Resuelve a lo que haya en la ruta.
- **No inicializar el gestor en el *shell*.** El *shim* no interviene y se usa la versión del sistema.
- **Dar por hecho que el archivo de versión se cumple.** Hay que comprobar la versión efectiva, sobre todo en integración continua.
- **Creer que aísla paquetes.** Solo fija el *runtime*.

## Límites y cuándo no aplica

Fijar el *runtime* no aísla paquetes instalados ([SE-102](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md)); para eso están los entornos virtuales, que la clase siguiente explica. Un gestor de versiones tampoco fija bibliotecas del sistema ni compiladores nativos, que pueden variar entre máquinas; para entornos completos se recurre a contenedores. En proyectos con una sola versión soportada y sin otros proyectos en la misma máquina, el gestor aporta poco más que una verificación.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Comando](../c/comando.md), [Runtime](../r/runtime.md), [Actualización y rollback](../a/actualizacion-y-rollback.md), [Compatibilidad y sintaxis](../c/compatibilidad-y-sintaxis.md), [Resolución por path](../r/resolucion-por-path.md), [Runtime e implementación](../r/runtime-e-implementacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-102 — Gestores de versiones de runtimes](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md), [SE-103](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Language Server Protocol 3.18](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/) — Mensajes, capacidades y sincronización entre editor y servidor; autoridad: Microsoft.
- [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) — Breakpoints, frames, variables y negociación de capacidades; autoridad: Microsoft.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Pdb, cprofile, timeit, tracemalloc y límites instrumentales; autoridad: Python Software Foundation.
- [Python venv](https://docs.python.org/3/library/venv.html) — Aislamiento de intérprete, scripts y entorno virtual; autoridad: Python Software Foundation.
- [Development Container Specification](https://containers.dev/implementors/spec/) — Configuración reproducible de herramientas y ciclo de vida del contenedor; autoridad: Dev Container Specification maintainers.

---

[↑ Glosario](../../README.md) · [← Generador](./generador.md) · [GIL →](./gil.md)
