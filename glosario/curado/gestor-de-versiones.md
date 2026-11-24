# Gestor de versiones

## Definición

En este contexto (`SE-102`), un **gestor de versiones** es una herramienta que **instala y selecciona versiones de *runtimes*** (intérpretes y compiladores como Python, Node o Ruby), por archivo de configuración o por comando. Sirve para que cada proyecto use la versión del lenguaje que declara, sin depender de la que haya instalado el sistema. No debe confundirse con el **control de versiones** del código (como Git), que registra el historial de cambios; este gestor administra qué versión del *runtime* se ejecuta.

## Por qué importa

Proyectos distintos necesitan versiones distintas del mismo lenguaje, y la del sistema suele ser una sola y antigua. Sin gestor, el comando `python` apunta a lo que haya, y el mismo script se comporta distinto en cada máquina. `SE-102` documenta el síntoma: el script usa otro Python en otra máquina porque se invoca `python` a secas. La decisión que cambia es cómo se determina el *runtime* de un proyecto: se declara y se verifica, no se asume.

## Cómo funciona

La mayoría de los gestores usan **shims**: pequeños ejecutables que se colocan al inicio de la ruta de búsqueda (`PATH`) con los nombres de los comandos (`python`, `node`). Al invocar `python`, se ejecuta el *shim*, que consulta qué versión corresponde (por un archivo del proyecto, por una variable o por la configuración global) y delega en el ejecutable adecuado. Tres consecuencias:

- **El *shim* intercepta la resolución** de comandos, de modo que **debe inicializarse en el *shell***; si no, el comando se resuelve contra el sistema y se obtiene otra versión.
- **La configuración versionada** (un archivo con la versión deseada en el repositorio) **expresa intención**, pero no la garantiza: depende de que el gestor la lea.
- **La integración continua debe instalar explícitamente** la versión y **comprobar la versión efectiva**, en lugar de asumir que la intención se cumple.

Fijar el *runtime* no aísla los paquetes instalados: dos proyectos con la misma versión de Python siguen compartiendo el espacio de paquetes global si no usan un entorno virtual (`SE-102`).

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

Fijar el *runtime* no aísla paquetes instalados (`SE-102`); para eso están los entornos virtuales, que la clase siguiente explica. Un gestor de versiones tampoco fija bibliotecas del sistema ni compiladores nativos, que pueden variar entre máquinas; para entornos completos se recurre a contenedores. En proyectos con una sola versión soportada y sin otros proyectos en la misma máquina, el gestor aporta poco más que una verificación.
