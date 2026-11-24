# Editor e ide

[↑ Glosario](../../README.md) · [← Edición asistida](./edicion-asistida.md) · [Efecto →](./efecto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

Un **editor** manipula texto y puede integrar capacidades adicionales (resaltado, búsqueda, complementos); un **IDE** (*Integrated Development Environment*, entorno de desarrollo integrado) reúne en una sola herramienta el **proyecto, la construcción, la ejecución, la depuración y la navegación** del código ([SE-097](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md)). La frontera no es absoluta: un editor con complementos puede acercarse a un IDE, y un IDE puede usarse solo como editor. El programa no define dos categorías cerradas, sino dos extremos de un espectro de capacidades.

## Por qué importa

La elección de herramienta afecta la velocidad con que se navega, se refactoriza y se diagnostica. Pero también afecta algo menos visible: si el entorno vive en una herramienta, el proyecto depende de ella. [SE-097](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md) pide **describir tareas y costos** al elegir y no usar «IDE» como sinónimo de herramienta profesional; un editor ligero con buen soporte de lenguaje puede ser la elección correcta para una persona o tarea, y un IDE completo para otra. La decisión que cambia es el criterio de selección: qué tareas hay que hacer, con qué frecuencia y qué se paga por cada capacidad (memoria, configuración, curva de aprendizaje).

## Cómo funciona

La diferencia es de **qué está integrado**, no de tamaño:

- **Editor:** abre, edita y guarda texto. Con complementos puede añadir resaltado de sintaxis, completado, ejecución de comandos.
- **IDE:** además, conoce el **proyecto** (estructura, dependencias), lo **construye y ejecuta**, ofrece un **depurador** y **navega** semánticamente (ir a la definición, buscar usos).

Hoy gran parte de las capacidades de lenguaje (completado, diagnósticos, ir a definición) viene de un **servidor de lenguaje** que el editor consulta mediante un protocolo estándar; así, un editor y un IDE pueden compartir la misma inteligencia de lenguaje. Esto explica un fallo documentado en [SE-097](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md): «el editor no completa» porque se asumió que el servidor ofrecía completado; la corrección es revisar las **capacidades declaradas** en `initialize`, la fase del protocolo donde servidor y cliente acuerdan qué soporta cada uno. Un segundo fallo es que **el editor y la integración continua discrepan**, por versiones o configuración distintas; se corrige fijando versión y configuración en el repositorio.

## Ejemplo

Dos personas del mismo equipo usan herramientas distintas: una un IDE completo, otra un editor ligero con un servidor de lenguaje. El proyecto fija en el repositorio la versión del formateador y del analizador estático, y un archivo de configuración compartido. Ambas obtienen los mismos diagnósticos y el mismo formato; la integración continua ejecuta las mismas herramientas con la misma configuración. Un comando documentado funciona sin ningún editor:

```bash
python -m ruff check . && python -m pytest
```

Así, el IDE es una comodidad individual y no una dependencia del proyecto.

## Errores y confusiones comunes

- **Equiparar IDE con «profesional».** La elección debe justificarse con tareas y costos.
- **Asumir capacidades del servidor.** No todos los servidores ofrecen completado, renombrado o formato; hay que revisar lo declarado.
- **Configuración solo local.** El editor muestra un resultado y la integración continua otro.
- **Depender del IDE para construir o probar.** Nadie más puede reproducir el flujo.

## Límites y cuándo no aplica

Un diagnóstico estático, el que da un editor al escribir, no muestra necesariamente el estado que llevó al fallo ([SE-097](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md)): para eso se necesita ejecutar y depurar. Para tareas remotas o muy puntuales (editar un archivo en un servidor), un IDE completo es excesivo. Y las capacidades de IDE no sustituyen conocer las herramientas de línea de comandos que usan por debajo.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Capacidad](../c/capacidad.md), [Confianza y extensiones](../c/confianza-y-extensiones.md), [Language server protocol](../l/language-server-protocol.md), [Modelo sintáctico y semántico](../m/modelo-sintactico-y-semantico.md), [Workspace y configuración](../w/workspace-y-configuracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-097 — Editores, IDE y servidores de lenguaje](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

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

[↑ Glosario](../../README.md) · [← Edición asistida](./edicion-asistida.md) · [Efecto →](./efecto.md)
