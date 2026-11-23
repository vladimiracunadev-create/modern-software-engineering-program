# Confianza y extensiones

[↑ Glosario](../../README.md) · [← Confianza cero](./confianza-cero.md) · [Configuración efectiva →](./configuracion-efectiva.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

Una extensión ejecuta código con acceso relevante al workspace.

Definición de trabajo de [SE-097 — Editores, IDE y servidores de lenguaje](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md).

## Por qué importa

En [SE-097 — Editores, IDE y servidores de lenguaje](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md), el tema «Confianza y extensiones» importa porque una extensión ejecuta código con acceso relevante al workspace.

## Cómo funciona

Según [SE-097 — Editores, IDE y servidores de lenguaje](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md), en la sección «Confianza y extensiones»:

Una extensión ejecuta código con acceso relevante al workspace. Procedencia, permisos, actualización y política de red forman parte del riesgo. Un perfil mínimo reduce variabilidad y facilita recuperar el entorno sin exportar secretos personales.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-097 — Editores, IDE y servidores de lenguaje](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md):

En el entorno reproducible de diagnóstico, una investigación conserva síntoma, entorno, reproducción, hipótesis, observaciones, causa, corrección y regresión. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-097 — Editores, IDE y servidores de lenguaje](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md)) son:

- **«El editor no completa»** — causa: se asume que el servidor ofrece completado. Corrección: revisar las capacidades declaradas en `initialize`.
- **El editor y la CI discrepan** — causa: versiones o configuración distintas. Corrección: fijar versión y configuración en el repositorio.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-097 — Editores, IDE y servidores de lenguaje](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md)) son: Las definiciones son operativas para el entorno reproducible de diagnóstico. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Un diagnóstico estático no muestra necesariamente el estado que llevó al fallo. La siguiente clase detiene la ejecución y observa frames sin asumir que observar es neutral.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Extensión](../e/extension.md), [Editor e ide](../e/editor-e-ide.md), [Language server protocol](../l/language-server-protocol.md), [Modelo sintáctico y semántico](../m/modelo-sintactico-y-semantico.md), [Workspace y configuración](../w/workspace-y-configuracion.md).
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

[↑ Glosario](../../README.md) · [← Confianza cero](./confianza-cero.md) · [Configuración efectiva →](./configuracion-efectiva.md)
