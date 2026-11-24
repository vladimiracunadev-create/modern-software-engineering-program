# Language server protocol

[↑ Glosario](../../README.md) · [← Lakehouse](./lakehouse.md) · [Lanzamiento por fases →](./lanzamiento-por-fases.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md)

## Definición

El **Language Server Protocol** (LSP, protocolo de servidor de lenguaje) es, según [SE-097](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md), un protocolo que **estandariza los mensajes JSON-RPC entre un cliente (el editor) y un servidor de lenguaje** para funciones como completado, ir a la definición, buscar referencias y diagnósticos. Lo define y mantiene Microsoft como especificación abierta. El editor habla con el servidor mediante mensajes de solicitud y respuesta; el servidor entiende el lenguaje de programación y el editor lo presenta. Es un protocolo de comunicación, no un servidor concreto ni un análisis de código.

## Por qué importa

Antes de LSP, cada editor tenía que implementar su propia inteligencia para cada lenguaje: *N* editores por *M* lenguajes eran *N×M* integraciones. Con un protocolo común, cada lenguaje tiene un servidor y cada editor un cliente: *N+M*. La decisión que cambia es dónde vive la inteligencia de un lenguaje: en un servidor reutilizable, independiente del editor. Para un equipo, eso permite elegir editor sin perder análisis, y fijar en el repositorio la versión del servidor para que todos obtengan los mismos diagnósticos.

## Cómo funciona

La comunicación es un diálogo con tres fases:

1. **Inicialización:** el cliente envía `initialize` y el servidor responde con sus **capacidades** (qué soporta: completado, renombrado, formato). **Cliente y servidor negocian capacidades**; el cliente no puede asumir que algo existe sin comprobarlo.
2. **Sincronización de documentos:** el cliente notifica que se abrió o cambió un documento, con un **número de versión**, para que el servidor analice el mismo texto que el usuario ve. Si las versiones se desincronizan, los resultados se refieren a un texto distinto.
3. **Solicitudes y notificaciones:** el cliente pide, por ejemplo, completado en una posición; el servidor responde. El servidor también envía diagnósticos por su cuenta.

[SE-097](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md) precisa un límite: el protocolo **no garantiza la calidad del análisis**. Define cómo se piden y se entregan los resultados, no que sean buenos; un servidor puede responder rápido y mal. Dos síntomas documentados: «el editor no completa» porque se asumió que el servidor ofrecía completado (se revisan las capacidades declaradas en `initialize`) y el editor y la integración continua discrepan por versiones o configuración distintas (se fijan versión y configuración en el repositorio).

## Ejemplo

Un mensaje JSON-RPC de solicitud de completado (ilustración, abreviado):

```json
{"jsonrpc": "2.0", "id": 7, "method": "textDocument/completion",
 "params": {"textDocument": {"uri": "file:///proyecto/app.py"},
            "position": {"line": 12, "character": 8}}}
```

Y la respuesta lista los candidatos. Si el servidor no declaró la capacidad de completado en `initialize`, el editor no debería enviar esta solicitud, y el síntoma «el editor no completa» se explica sin buscar un error en el código.

## Errores y confusiones comunes

- **Creer que LSP es el analizador.** Es el protocolo; la calidad depende del servidor.
- **Suponer capacidades.** No todo servidor ofrece todo; se revisan las declaradas.
- **Confundirlo con un compilador o con un linter.** El servidor puede usar ambos, pero LSP es la interfaz hacia el editor.
- **Diferencias entre editor e integración continua.** Se fija la versión del servidor y la configuración.

## Límites y cuándo no aplica

Un diagnóstico estático no muestra necesariamente el estado que llevó al fallo ([SE-097](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md)): LSP ofrece análisis sin ejecutar, no depuración. El protocolo cubre funciones de edición de lenguaje, no construcción ni ejecución del proyecto. Para tareas no ligadas a un lenguaje o editores muy simples, la integración puede no compensar el costo de configurarla.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Diagnóstico](../d/diagnostico.md), [Referencia](../r/referencia.md), [Confianza y extensiones](../c/confianza-y-extensiones.md), [Editor e ide](../e/editor-e-ide.md), [Modelo sintáctico y semántico](../m/modelo-sintactico-y-semantico.md), [Workspace y configuración](../w/workspace-y-configuracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-097 — Editores, IDE y servidores de lenguaje](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md) — [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md), Entornos, herramientas y depuración.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-098](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md), [SE-099](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md), [SE-100](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md), [SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md), [SE-102](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md), [SE-103](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md), [SE-104](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md), [SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md).

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

[↑ Glosario](../../README.md) · [← Lakehouse](./lakehouse.md) · [Lanzamiento por fases →](./lanzamiento-por-fases.md)
