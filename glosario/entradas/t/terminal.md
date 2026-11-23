# Terminal

[↑ Glosario](../../README.md) · [← Terminación en falso](./terminacion-en-falso.md) · [Términos, hechos y consultas →](./terminos-hechos-y-consultas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Dispositivo interactivo de texto; `isatty()` indica si un flujo está conectado a uno.

Definición de trabajo de [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-029 — Terminales, shells y composición de comandos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md): Interfaz que transporta entrada y salida de una sesión.

## Por qué importa

En [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md), el tema «Detección de terminal» importa porque el color en una tubería contamina la salida que otro programa lee.

## Cómo funciona

Según [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md):

Un terminal interpreta secuencias de escape (ECMA-48) para color, movimiento del cursor y borrado. Pero la salida de una herramienta puede ir a un archivo, a una tubería, a un contenedor sin terminal o a un registro de CI. La regla de oro: **emitir secuencias de control solo cuando la salida es un terminal** (`isatty()`), respetar `NO_COLOR` y ofrecer un interruptor explícito (`--color=auto|siempre|nunca`). Quien fuerza el color «siempre» acepta que su salida no es texto plano.

Según [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md):

`notas validar` decide su presentación así: color solo si `isatty()` y no existe `NO_COLOR`, con `--color` como interruptor; prefijos textuales (`ERROR`, `AVISO`, `OK`) que repiten lo que dice el color; ancho tomado de `shutil.get_terminal_size()` y respetado por una función de tabla que alinea por ancho en pantalla; identificadores truncados por el medio con una opción `--ancho-completo`; texto normalizado a NFC al leer; y un modo `--sin-animacion` (por defecto cuando no hay terminal) que escribe una línea por evento. Una prueba ejecuta el informe en tubería y falla si encuentra una secuencia de escape; otra compara la tabla con nombres NFC y NFD y exige igual alineación.

## Ejemplo

Ejemplo de [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md) (sección «Ejemplo profesional»):

`notas validar` decide su presentación así: color solo si `isatty()` y no existe `NO_COLOR`, con `--color` como interruptor; prefijos textuales (`ERROR`, `AVISO`, `OK`) que repiten lo que dice el color; ancho tomado de `shutil.get_terminal_size()` y respetado por una función de tabla que alinea por ancho en pantalla; identificadores truncados por el medio con una opción `--ancho-completo`; texto normalizado a NFC al leer; y un modo `--sin-animacion` (por defecto cuando no hay terminal) que escribe una línea por evento. Una prueba ejecuta el informe en tubería y falla si encuentra una secuencia de escape; otra compara la tabla con nombres NFC y NFD y exige igual alineación.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md)) son:

- **Aparecen secuencias de escape en un archivo** — causa: el color no depende del destino. Corrección: `isatty()`, `NO_COLOR` y `--color`.
- **Dos filas distintas parecen iguales** — causa: se truncó por el final un prefijo compartido. Corrección: truncar por el medio o mostrar primero lo distintivo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Pero la salida de una herramienta puede ir a un archivo, a una tubería, a un contenedor sin terminal o a un registro de CI. ([SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md))
- La transferencia está lograda cuando puedes explicar qué parte de la política dependía del terminal y cuál del texto, no cuando la tabla se parece. ([SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dispositivo](../d/dispositivo.md), [Flujo](../f/flujo.md), [Interfaz](../i/interfaz.md), [Ancho en pantalla](../a/ancho-en-pantalla.md), [Argumento](../a/argumento.md), [Código de salida](../c/codigo-de-salida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-029 — Terminales, shells y composición de comandos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (216 clases más lo mencionan; las que más):

[SE-579](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md), [SE-080](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md), [SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md), [SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md), [SE-079](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), [SE-102](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md), [SE-097](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md), [SE-098](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md).

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «TTY».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: `shutil.get_terminal_size`](https://docs.python.org/3/library/shutil.html) — consulta del ancho del terminal; autoridad: documentación de Python.
- [ECMA-48: Control Functions for Coded Character Sets](https://ecma-international.org/publications-and-standards/standards/ecma-48/) — secuencias de control de los terminales; autoridad: Ecma International.
- [NO_COLOR](https://no-color.org/) — convención para desactivar el color; autoridad: proyecto comunitario.
- [Unicode UAX #11: East Asian Width](https://www.unicode.org/reports/tr11/) — clasificación de anchos de carácter; autoridad: Consorcio Unicode.
- [Unicode UAX #15: Normalization Forms](https://www.unicode.org/reports/tr15/) — NFC y NFD; autoridad: Consorcio Unicode.

---

[↑ Glosario](../../README.md) · [← Terminación en falso](./terminacion-en-falso.md) · [Términos, hechos y consultas →](./terminos-hechos-y-consultas.md)
