# Subcomando

[↑ Glosario](../../README.md) · [← Subcarga](./subcarga.md) · [Subida reanudable →](./subida-reanudable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Acción con nombre propio dentro de una herramienta (`notas exportar`), con sus propias opciones.

Definición de trabajo de [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md).

## Por qué importa

La clase donde se define, [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md), existe con este propósito: la clase existe para diseñar una interfaz de línea de comandos como un contrato con dos lectores —una persona que escribe y un programa que invoca— de modo que cambiar un flag, un mensaje o un código no rompa ni a la persona que lo memorizó ni al guion que lo automatizó.

## Cómo funciona

Según [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md):

Las convenciones POSIX describen opciones de una letra (`-v`), su agrupación (`-vq`) y el delimitador `--` que indica «lo que sigue no son opciones»; las GNU añadieron opciones largas (`--verbose`) y `--help`/`--version`. Una herramienta con varias acciones suele organizarse en subcomandos (`notas exportar`, `notas validar`), cada uno con sus propias opciones. La decisión de diseño es de qué depende el significado: un flag global afecta a todo, uno de subcomando solo a ese. Una gramática regular —los mismos nombres para lo mismo— se aprende una vez; una irregular se consulta siempre. Los booleanos son otro punto delicado: `--force` activa, pero ¿cómo se desactiva algo que por defecto está activo? Diseñar el par (`--color` / `--no-color`) o un valor explícito evita que la ausencia de flag signifique dos cosas.

Según [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md):

En la plataforma, `notas` documenta su contrato en un archivo corto: tabla de flags (nombre, tipo, valor por defecto, desde qué versión), tabla de códigos (0 éxito, 2 uso incorrecto, 65 datos inválidos, 75 fallo temporal), destino de cada flujo y política de deprecación. Las abreviaturas están desactivadas en todos los analizadores, incluidos los de subcomandos. Una prueba de contrato ejecuta la herramienta como lo haría un guion y comprueba código, flujo y presencia de ciertas cadenas en la ayuda; no compara el texto completo. Una segunda prueba falla si alguien añade un flag sin documentarlo.

## Ejemplo

Ejemplo de [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md) (sección «Ejemplo profesional»):

En la plataforma, `notas` documenta su contrato en un archivo corto: tabla de flags (nombre, tipo, valor por defecto, desde qué versión), tabla de códigos (0 éxito, 2 uso incorrecto, 65 datos inválidos, 75 fallo temporal), destino de cada flujo y política de deprecación. Las abreviaturas están desactivadas en todos los analizadores, incluidos los de subcomandos. Una prueba de contrato ejecuta la herramienta como lo haría un guion y comprueba código, flujo y presencia de ciertas cadenas en la ayuda; no compara el texto completo. Una segunda prueba falla si alguien añade un flag sin documentarlo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **`allow_abbrev=False` no surte efecto en un subcomando** — causa: la opción no se hereda en los subanalizadores. Corrección: pasarla en cada `add_parser`. ([SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una herramienta con varias acciones suele organizarse en subcomandos (`notas exportar`, `notas validar`), cada uno con sus propias opciones. ([SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Herramientas](../h/herramientas.md), [Opción](../o/opcion.md), [Abreviatura de flag](../a/abreviatura-de-flag.md), [Contrato de línea de comandos](../c/contrato-de-linea-de-comandos.md), [Deprecación](../d/deprecacion.md), [Sugerencia](./sugerencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-217 — Diseño de interfaces de línea de comandos](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md), [SE-228](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md), [SE-579](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md), [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md), [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-072](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Command Line Interface Guidelines](https://clig.dev/) — principios de diseño de interfaces de línea de comandos; autoridad: guía de autores, de uso extendido.
- [POSIX: Utility Conventions](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html) — sintaxis de opciones y argumentos; autoridad: The Open Group.
- [GNU Coding Standards: Command-Line Interfaces](https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html) — `--help`, `--version` y opciones largas; autoridad: proyecto GNU.
- [Python: `argparse`](https://docs.python.org/3/library/argparse.html) — `allow_abbrev`, subanalizadores y código de salida 2; autoridad: documentación de Python.
- [Python: `difflib`](https://docs.python.org/3/library/difflib.html) — `get_close_matches` y su umbral de similitud; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Subcarga](./subcarga.md) · [Subida reanudable →](./subida-reanudable.md)
