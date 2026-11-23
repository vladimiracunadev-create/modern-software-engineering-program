# Editor e ide

[↑ Glosario](../../README.md) · [← Edición asistida](./edicion-asistida.md) · [Efecto →](./efecto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

Un editor manipula texto y puede integrar capacidades; un ide reúne proyecto, build, ejecución, depuración y navegación.

Definición de trabajo de [SE-097 — Editores, IDE y servidores de lenguaje](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md).

## Por qué importa

En [SE-097 — Editores, IDE y servidores de lenguaje](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md), el tema «Editor e IDE» importa porque un editor manipula texto y puede integrar capacidades; un IDE reúne proyecto, build, ejecución, depuración y navegación.

## Cómo funciona

Según [SE-097 — Editores, IDE y servidores de lenguaje](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md), en la sección «Editor e IDE»:

Un editor manipula texto y puede integrar capacidades; un IDE reúne proyecto, build, ejecución, depuración y navegación. La frontera no es absoluta. Elegir uno exige describir tareas y costos, no usar `IDE` como sinónimo de herramienta profesional.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-097 — Editores, IDE y servidores de lenguaje](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md):

En el entorno reproducible de diagnóstico, una investigación conserva síntoma, entorno, reproducción, hipótesis, observaciones, causa, corrección y regresión. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-097 — Editores, IDE y servidores de lenguaje](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md)) son:

- **«El editor no completa»** — causa: se asume que el servidor ofrece completado. Corrección: revisar las capacidades declaradas en `initialize`.
- **El editor y la CI discrepan** — causa: versiones o configuración distintas. Corrección: fijar versión y configuración en el repositorio.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-097 — Editores, IDE y servidores de lenguaje](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md)) son: Las definiciones son operativas para el entorno reproducible de diagnóstico. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Un diagnóstico estático no muestra necesariamente el estado que llevó al fallo. La siguiente clase detiene la ejecución y observa frames sin asumir que observar es neutral.

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
