# Runtime e implementación

[↑ Glosario](../../README.md) · [← Runtime & Systems Engineer](./runtime-systems-engineer.md) · [Ruta →](./ruta.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

**Runtime e implementación** nombra, en [SE-102](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md), la distinción de que **la versión del lenguaje, la implementación y la arquitectura son dimensiones distintas**: «Python 3.12» no identifica por sí solo qué programa corre. Una misma versión del lenguaje puede ejecutarse con distintas **implementaciones** (CPython, PyPy y otras), sobre distintas **arquitecturas** de procesador (x86-64, ARM) y con distintos *builds* (opciones de compilación, distribución del sistema, versión de la biblioteca de C). El término *runtime* designa el entorno que ejecuta el programa; la implementación es una de sus dimensiones.

## Por qué importa

Cuando alguien dice «funciona en Python 3.12», comunica menos de lo que parece. Las extensiones nativas se compilan para una arquitectura y una interfaz binaria (ABI) concretas; la velocidad y el comportamiento de ciertas operaciones cambian entre implementaciones; la distribución del sistema trae su propia biblioteca de C. [SE-102](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md) extrae la consecuencia práctica: **«Python 3.12» no identifica necesariamente *build*, ABI ni distribución**. La decisión que cambia es qué se declara como soportado y qué se prueba de verdad.

## Cómo funciona

Hay tres dimensiones que conviene mantener separadas:

- **Versión del lenguaje:** qué sintaxis y qué biblioteca estándar existen (3.9, 3.12).
- **Implementación:** el programa concreto que interpreta o compila el lenguaje. Cumplen la misma especificación general, pero difieren en rendimiento, gestión de memoria y soporte de extensiones nativas.
- **Arquitectura y *build*:** el procesador y el sistema, y la forma de construir el intérprete. Determinan si un paquete binario precompilado (una rueda) existe para esa combinación o hay que compilar desde el código fuente.

La consecuencia de que sean dimensiones distintas es que las pruebas en una combinación no se transfieren a las demás. El proyecto debe **declarar un rango soportado** (qué promete) y mantener una **matriz realmente probada** (qué verificó), y distinguir ambas: el rango es una intención, la matriz es evidencia. Una celda sin ejecutar es «no verificada», no «soportada».

## Ejemplo

Un script de medición produce tiempos distintos en dos equipos. Antes de culpar al código, se registra el entorno completo:

```python
import platform, sys
print(sys.version.split()[0],            # versión
      platform.python_implementation(),  # CPython, PyPy...
      platform.machine(),                # x86_64, arm64...
      platform.platform())               # sistema y versión
```

[SE-102](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md) documenta el síntoma: la medición no se repite en otro equipo por compilación o sistema distintos; la corrección es registrar versión y sistema con cada medición. Y el síntoma de la resolución del intérprete: el script usa otro Python en otra máquina porque se invoca `python` a secas, y se corrige declarando la versión y verificándola al inicio.

## Errores y confusiones comunes

- **Equiparar versión con entorno.** «3.12» no basta para reproducir un resultado.
- **Declarar soporte sin probar.** El rango declarado no es la matriz verificada.
- **Ignorar la arquitectura.** Una rueda precompilada puede no existir para ARM o para otra distribución.
- **Comparar mediciones de equipos distintos.** Sin registrar el entorno, la comparación no es válida.

## Límites y cuándo no aplica

Fijar el *runtime* no aísla paquetes instalados ([SE-102](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md)). Para código puro de Python sin extensiones nativas, las diferencias de arquitectura casi no se notan, y el rigor sobre ABI y *build* es innecesario. La distinción importa más cuanto más dependa el proyecto de código nativo, de rendimiento o de comportamiento específico del intérprete.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Arquitectura](../a/arquitectura.md), [Dimensión](../d/dimension.md), [Versión](../v/version.md), [Actualización y rollback](../a/actualizacion-y-rollback.md), [Compatibilidad y sintaxis](../c/compatibilidad-y-sintaxis.md), [Gestor de versiones](../g/gestor-de-versiones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-102 — Gestores de versiones de runtimes](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

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

[↑ Glosario](../../README.md) · [← Runtime & Systems Engineer](./runtime-systems-engineer.md) · [Ruta →](./ruta.md)
