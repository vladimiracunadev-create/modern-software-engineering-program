# Language server protocol

## Definición

El **Language Server Protocol** (LSP, protocolo de servidor de lenguaje) es, según `SE-097`, un protocolo que **estandariza los mensajes JSON-RPC entre un cliente (el editor) y un servidor de lenguaje** para funciones como completado, ir a la definición, buscar referencias y diagnósticos. Lo define y mantiene Microsoft como especificación abierta. El editor habla con el servidor mediante mensajes de solicitud y respuesta; el servidor entiende el lenguaje de programación y el editor lo presenta. Es un protocolo de comunicación, no un servidor concreto ni un análisis de código.

## Por qué importa

Antes de LSP, cada editor tenía que implementar su propia inteligencia para cada lenguaje: *N* editores por *M* lenguajes eran *N×M* integraciones. Con un protocolo común, cada lenguaje tiene un servidor y cada editor un cliente: *N+M*. La decisión que cambia es dónde vive la inteligencia de un lenguaje: en un servidor reutilizable, independiente del editor. Para un equipo, eso permite elegir editor sin perder análisis, y fijar en el repositorio la versión del servidor para que todos obtengan los mismos diagnósticos.

## Cómo funciona

La comunicación es un diálogo con tres fases:

1. **Inicialización:** el cliente envía `initialize` y el servidor responde con sus **capacidades** (qué soporta: completado, renombrado, formato). **Cliente y servidor negocian capacidades**; el cliente no puede asumir que algo existe sin comprobarlo.
2. **Sincronización de documentos:** el cliente notifica que se abrió o cambió un documento, con un **número de versión**, para que el servidor analice el mismo texto que el usuario ve. Si las versiones se desincronizan, los resultados se refieren a un texto distinto.
3. **Solicitudes y notificaciones:** el cliente pide, por ejemplo, completado en una posición; el servidor responde. El servidor también envía diagnósticos por su cuenta.

`SE-097` precisa un límite: el protocolo **no garantiza la calidad del análisis**. Define cómo se piden y se entregan los resultados, no que sean buenos; un servidor puede responder rápido y mal. Dos síntomas documentados: «el editor no completa» porque se asumió que el servidor ofrecía completado (se revisan las capacidades declaradas en `initialize`) y el editor y la integración continua discrepan por versiones o configuración distintas (se fijan versión y configuración en el repositorio).

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

Un diagnóstico estático no muestra necesariamente el estado que llevó al fallo (`SE-097`): LSP ofrece análisis sin ejecutar, no depuración. El protocolo cubre funciones de edición de lenguaje, no construcción ni ejecución del proyecto. Para tareas no ligadas a un lenguaje o editores muy simples, la integración puede no compensar el costo de configurarla.
