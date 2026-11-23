# Fallo permanente

[↑ Glosario](../../README.md) · [← Fallo parcial](./fallo-parcial.md) · [Fallo silencioso →](./fallo-silencioso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Fallo que se repetirá igual mientras no cambien la entrada o el entorno.

Definición de trabajo de [SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md).

## Por qué importa

La clase donde se define, [SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md), existe con este propósito: la clase existe para que lo que una herramienta dice al terminar —un número y un mensaje— permita a una persona corregir y a un programa decidir si reintenta, alerta o se detiene, sin confundir éxito con silencio ni fallo permanente con fallo temporal.

## Cómo funciona

Según [SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md):

Una simulación con 10 000 trabajos y cinco tipos de fallo (40 % temporales, 15 % de uso, 20 % de datos, 10 % de conflicto y 15 % internos); un trabajo temporal se recupera con probabilidad 0,7 en cada intento y los demás nunca. Tres políticas con un máximo de 4 intentos: **nunca reintentar** recuperó 2 785 trabajos con 10 000 intentos; **reintentar solo el código 75** recuperó **3 950** con **11 675** intentos y ningún reintento inútil; **reintentar todo** recuperó los mismos 3 950 con **29 744** intentos, de los que **24 092** fueron reintentos inútiles sobre fallos permanentes.

Según [SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md):

Porque quien lee el código no puede decidir: reintentar un fallo permanente es inútil y no reintentar uno temporal pierde trabajo. Distinguir cuesta una tabla de cinco filas.

## Ejemplo

Ejemplo de [SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md) (sección «Preguntas frecuentes»):

Porque quien lee el código no puede decidir: reintentar un fallo permanente es inútil y no reintentar uno temporal pierde trabajo. Distinguir cuesta una tabla de cinco filas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El reintento repite un fallo permanente** — causa: todos los errores devuelven el mismo código. Corrección: distinguir un código temporal del resto. ([SE-220](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Porque quien lee el código no puede decidir: reintentar un fallo permanente es inútil y no reintentar uno temporal pierde trabajo. ([SE-220](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-219](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Entorno](../e/entorno.md), [Código de salida](../c/codigo-de-salida.md), [Estado de una tubería](../e/estado-de-una-tuberia.md), [Fallo temporal](./fallo-temporal.md), [Mensaje accionable](../m/mensaje-accionable.md), [Reintentos](../r/reintentos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md).

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

[↑ Glosario](../../README.md) · [← Fallo parcial](./fallo-parcial.md) · [Fallo silencioso →](./fallo-silencioso.md)
