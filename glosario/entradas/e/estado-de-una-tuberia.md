# Estado de una tubería

[↑ Glosario](../../README.md) · [← Estado como memoria de la ejecución](./estado-como-memoria-de-la-ejecucion.md) · [Estado derivado →](./estado-derivado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Valor de salida de una tubería, por defecto el de su última etapa.

Definición de trabajo de [SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md).

## Por qué importa

En [SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md), el tema «Tuberías y guiones» importa porque el estado de una tubería puede ocultar el fallo de una etapa.

## Cómo funciona

Según [SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md):

El estado de una tubería es, por defecto, el de la última orden. `false | cat` devuelve 0. Bash ofrece `set -o pipefail` (el estado es el del último comando que falló) y la variable `PIPESTATUS` (el estado de cada etapa). `set -e` detiene el guion en el primer fallo, con excepciones sutiles (condiciones de `if`, listas con `&&`/`||`). La regla práctica: un guion que automatiza debe activar `pipefail`, comprobar el estado de las etapas críticas y fallar de forma ruidosa. En Python, `subprocess` obliga a mirar el código de cada proceso; una tubería construida a mano necesita leer el de cada etapa.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md):

`notas` documenta cinco códigos: 0 éxito; 2 uso incorrecto; 65 datos inválidos (con número de línea); 73 no se pudo crear la salida; 75 fallo temporal (recurso ocupado, tiempo de espera). Nunca devuelve un valor mayor que 125. Los mensajes van a stderr, en una línea, con la causa y la acción; la opción `--debug` añade la traza. El guion nocturno activa `set -euo pipefail`, comprueba cada etapa con `PIPESTATUS` cuando hay una tubería y reintenta solo ante el código 75, con tres intentos y espera creciente.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md)) son:

- **El guion termina con 0 tras un fallo intermedio** — causa: el estado de la tubería es el de la última etapa. Corrección: `set -o pipefail` y `PIPESTATUS`.
- **El código 256 se lee como éxito en Linux** — causa: se devolvió un valor fuera de 0–255. Corrección: limitar a 0–125 y comprobar el rango.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md)) son: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos salvo los códigos fuera de 0–255 y los de señales. Los porcentajes de fallo, la probabilidad de recuperación y el máximo de intentos son supuestos del autor; no se midió ningún planificador, ni PowerShell ni `cmd`. La siguiente clase pasa de la salida de un proceso a la interfaz que una persona usa en un terminal.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-219](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tubería](../t/tuberia.md), [Valor](../v/valor.md), [Código de salida](../c/codigo-de-salida.md), [Fallo permanente](../f/fallo-permanente.md), [Fallo temporal](../f/fallo-temporal.md), [Mensaje accionable](../m/mensaje-accionable.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [POSIX: Shell Command Language](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html) — estado de salida de órdenes y tuberías; autoridad: The Open Group.
- [sysexits(3)](https://man.freebsd.org/cgi/man.cgi?query=sysexits) — vocabulario de códigos 64–78; autoridad: proyecto FreeBSD.
- [Python: `sys.exit`](https://docs.python.org/3/library/sys.html) — código de salida de un proceso Python; autoridad: documentación de Python.
- [Bash: The Set Builtin](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html) — `set -e` y `pipefail`; autoridad: proyecto GNU.
- [Microsoft: `ExitProcess`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess) — código de salida en Windows; autoridad: Microsoft Learn.

---

[↑ Glosario](../../README.md) · [← Estado como memoria de la ejecución](./estado-como-memoria-de-la-ejecucion.md) · [Estado derivado →](./estado-derivado.md)
