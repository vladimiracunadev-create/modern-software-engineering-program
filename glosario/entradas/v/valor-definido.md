# Valor definido

[↑ Glosario](../../README.md) · [← Valor de vida y costo de adquisición](./valor-de-vida-y-costo-de-adquisicion.md) · [Valor del aprendizaje →](./valor-del-aprendizaje.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Valor que una fuente aporta según el criterio documentado (presente, no vacío, etc.).

Definición de trabajo de [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md).

## Por qué importa

La clase donde se define, [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md), existe con este propósito: la clase existe para decidir de dónde obtiene una herramienta cada valor —valor por defecto, archivo, variable de entorno o flag—, en qué orden se imponen y cómo se comprueba que ese orden se cumple también en los casos extraños: valores vacíos, booleanos escritos de varias formas y secretos.

## Cómo funciona

[SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md):

`notas` carga el archivo de usuario (`~/.config/notas/config.ini` o el equivalente de Windows), después el del proyecto, lee las variables con prefijo `NOTAS_`, interpreta los booleanos con el analizador estricto y aplica los flags. El comando `notas config --efectiva` imprime cada opción con su valor y su fuente, con los secretos enmascarados. El token se lee de un archivo (`--token-file`) o de la entrada estándar; no existe `--token`.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md)) son:

- **`--limite 0` se ignora** — causa: se escribió `if flag:` en lugar de `is not None`. Corrección: distinguir ausencia de valor falso.
- **`NOTAS_VERBOSE=false` activa el modo detallado** — causa: se aplicó `bool()` a una cadena. Corrección: interpretación estricta con conjunto cerrado.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md)) son: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos salvo el mecanismo de lectura del secreto. Los seis defectos, los valores de cada capa, el conjunto de booleanos aceptados y el secreto falso son supuestos del autor; no se midió ningún despliegue real. La siguiente clase pregunta qué significa para quien invoca que la configuración o la ejecución fallen: los códigos de salida.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor](./valor.md), [Configuración efectiva](../c/configuracion-efectiva.md), [Interpretación estricta](../i/interpretacion-estricta.md), [Precedencia](../p/precedencia.md), [Secreto](../s/secreto.md).
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

[↑ Glosario](../../README.md) · [← Valor de vida y costo de adquisición](./valor-de-vida-y-costo-de-adquisicion.md) · [Valor del aprendizaje →](./valor-del-aprendizaje.md)
