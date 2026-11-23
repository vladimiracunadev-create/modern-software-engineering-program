# Interpretación estricta

[↑ Glosario](../../README.md) · [← Interpretación](./interpretacion.md) · [Interrupción →](./interrupcion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Conversión de texto a tipo que rechaza lo no reconocido en vez de adivinar.

Definición de trabajo de [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md).

## Por qué importa

La clase donde se define, [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md), existe con este propósito: la clase existe para decidir de dónde obtiene una herramienta cada valor —valor por defecto, archivo, variable de entorno o flag—, en qué orden se imponen y cómo se comprueba que ese orden se cumple también en los casos extraños: valores vacíos, booleanos escritos de varias formas y secretos.

## Cómo funciona

Según [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md):

Una variable de entorno es una cadena. `bool("false")` es `True` porque la cadena no está vacía; `int("٣")` es `3` porque Python acepta dígitos de otros alfabetos; `"1" == 1` es falso. Una interpretación estricta define el conjunto de formas aceptadas —por ejemplo, `1/true/yes/on` y `0/false/no/off`, sin distinguir mayúsculas ni espacios— y **rechaza el resto con un error de uso** en lugar de adivinar. Adivinar convierte un error de tipeo en un comportamiento silencioso.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md):

`notas` carga el archivo de usuario (`~/.config/notas/config.ini` o el equivalente de Windows), después el del proyecto, lee las variables con prefijo `NOTAS_`, interpreta los booleanos con el analizador estricto y aplica los flags. El comando `notas config --efectiva` imprime cada opción con su valor y su fuente, con los secretos enmascarados. El token se lee de un archivo (`--token-file`) o de la entrada estándar; no existe `--token`.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **`NOTAS_VERBOSE=false` activa el modo detallado** — causa: se aplicó `bool()` a una cadena. Corrección: interpretación estricta con conjunto cerrado. ([SE-219](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una interpretación estricta define el conjunto de formas aceptadas —por ejemplo, `1/true/yes/on` y `0/false/no/off`, sin distinguir mayúsculas ni espacios— y **rechaza el resto con un error de uso** en lugar de adivinar. ([SE-219](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tipo](../t/tipo.md), [Configuración efectiva](../c/configuracion-efectiva.md), [Precedencia](../p/precedencia.md), [Secreto](../s/secreto.md), [Valor definido](../v/valor-definido.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Twelve-Factor App: Config](https://12factor.net/config) — configuración fuera del código; autoridad: guía de autores, de uso extendido.
- [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/) — ubicaciones de configuración en sistemas tipo Unix; autoridad: freedesktop.org.
- [NO_COLOR](https://no-color.org/) — convención para desactivar el color; autoridad: proyecto comunitario.
- [Console Do Not Track](https://consoledonottrack.com/) — convención `DO_NOT_TRACK`; autoridad: proyecto comunitario.
- [CWE-214: Invocation of Process Using Visible Sensitive Information](https://cwe.mitre.org/data/definitions/214.html) — riesgo de secretos en argumentos; autoridad: MITRE.

---

[↑ Glosario](../../README.md) · [← Interpretación](./interpretacion.md) · [Interrupción →](./interrupcion.md)
