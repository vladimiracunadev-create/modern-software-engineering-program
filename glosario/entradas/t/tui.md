# TUI

[↑ Glosario](../../README.md) · [← Tubería rota](./tuberia-rota.md) · [Túnel →](./tunel.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Interfaz de usuario de texto interactiva que redibuja el terminal y recibe teclado.

Definición de trabajo de [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md).

## Por qué importa

En [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md), el tema «Interfaz interactiva» importa porque una TUI debe tener una versión no interactiva equivalente.

## Cómo funciona

Según [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md):

Un lector de pantalla lee texto: un rojo no dice nada y una barra de progreso que se reescribe con retorno de carro se lee como ruido. Las pautas de accesibilidad (WCAG) piden no usar el color como único medio de información y ofrecer alternativas: un prefijo textual («ERROR», «AVISO»), un modo sin animación y una salida estructurada equivalente. Una TUI (interfaz de texto interactiva) añade teclado, foco y, a menudo, redibujado continuo: debe poder usarse solo con el teclado, anunciar los cambios y tener un equivalente no interactivo para guiones.

Según [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md):

Cuando la tarea es exploratoria (revisar una cola, navegar entre decenas de elementos) sí; cuando es de ejecución repetible, una CLI con salida estructurada es más automatizable. Una TUI debe tener siempre una versión no interactiva equivalente.

## Ejemplo

Ejemplo de [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md) (sección «Preguntas frecuentes»):

Cuando la tarea es exploratoria (revisar una cola, navegar entre decenas de elementos) sí; cuando es de ejecución repetible, una CLI con salida estructurada es más automatizable. Una TUI debe tener siempre una versión no interactiva equivalente.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md)) son:

- **Aparecen secuencias de escape en un archivo** — causa: el color no depende del destino. Corrección: `isatty()`, `NO_COLOR` y `--color`.
- **Dos filas distintas parecen iguales** — causa: se truncó por el final un prefijo compartido. Corrección: truncar por el medio o mostrar primero lo distintivo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una TUI (interfaz de texto interactiva) añade teclado, foco y, a menudo, redibujado continuo: debe poder usarse solo con el teclado, anunciar los cambios y tener un equivalente no interactivo para guiones. ([SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-220](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Interfaz](../i/interfaz.md), [Terminal](./terminal.md), [Ancho en pantalla](../a/ancho-en-pantalla.md), [Normalización Unicode](../n/normalizacion-unicode.md), [Secuencia de escape](../s/secuencia-de-escape.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-221 — TUI, terminales y accesibilidad](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ECMA-48: Control Functions for Coded Character Sets](https://ecma-international.org/publications-and-standards/standards/ecma-48/) — secuencias de control de los terminales; autoridad: Ecma International.
- [NO_COLOR](https://no-color.org/) — convención para desactivar el color; autoridad: proyecto comunitario.
- [Unicode UAX #11: East Asian Width](https://www.unicode.org/reports/tr11/) — clasificación de anchos de carácter; autoridad: Consorcio Unicode.
- [Unicode UAX #15: Normalization Forms](https://www.unicode.org/reports/tr15/) — NFC y NFD; autoridad: Consorcio Unicode.
- [W3C: WCAG 2.2](https://www.w3.org/TR/WCAG22/) — pautas de accesibilidad; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Tubería rota](./tuberia-rota.md) · [Túnel →](./tunel.md)
