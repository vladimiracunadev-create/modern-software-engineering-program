# Precedencia

[↑ Glosario](../../README.md) · [← Precarga](./precarga.md) · [Precisión →](./precision.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Orden en que se consultan las fuentes de configuración cuando hay más de una para el mismo valor.

Definición de trabajo de [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md): Orden que determina qué fuente gana por campo.
- En [SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md): Regla que establece cuál de dos instrucciones en conflicto prevalece.

## Por qué importa

En [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md), el tema «Precedencia» importa porque el orden decide quién gana cuando hay conflicto.

En [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md), el tema «Precedencia» importa porque combina fuentes en orden determinista

## Cómo funciona

Según [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md):

El valor por defecto lo decide quien escribe la herramienta; el archivo, el equipo que la despliega o la persona que la usa; la variable de entorno, quien lanza el proceso (un guion, un contenedor, un planificador); el flag, quien escribe esa invocación concreta. La precedencia habitual —flag, entorno, archivo, valor por defecto— sigue una idea: lo más cercano a la invocación manda sobre lo más general. Pero es una convención de diseño, no un hecho: algunas herramientas ponen el archivo del sistema por encima del de usuario, o permiten fijar valores que ningún flag puede cambiar (política de seguridad). Lo importante es decidirlo y escribirlo.

Según [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md):

Compara el caso normal con un entorno vacío, un `--limite 0` y un archivo con BOM. La configuración es apropiada cuando esos tres casos tienen una fila en la tabla de precedencia; es peligrosa cuando solo se ha probado «todo ausente» y «todo definido».

## Ejemplo

Ejemplo de [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md) (sección «Ejemplo profesional»):

Compara el caso normal con un entorno vacío, un `--limite 0` y un archivo con BOM. La configuración es apropiada cuando esos tres casos tienen una fila en la tabla de precedencia; es peligrosa cuando solo se ha probado «todo ausente» y «todo definido».

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Cambiar el archivo no cambia la ejecución** — causa: una variable de mayor precedencia quedó activa. Corrección: mostrar configuración efectiva y procedencia. ([SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md))
- **Cada opción puede venir de cualquier fuente** — causa: no se controló la superficie operativa. Corrección: limitar fuentes y documentar precedencia por campo. ([SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md))
- **El asistente alterna entre dos estilos** — causa: reglas contradictorias. Corrección: detectar pares y escribir una precedencia. ([SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La precedencia habitual —flag, entorno, archivo, valor por defecto— sigue una idea: lo más cercano a la invocación manda sobre lo más general. ([SE-219](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Instrucciones en conflicto](../i/instrucciones-en-conflicto.md), [Conflicto](../c/conflicto.md), [Instrucción](../i/instruccion.md), [Regla](../r/regla.md), [Configuración efectiva](../c/configuracion-efectiva.md), [Esquema](../e/esquema.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (19 clases más lo mencionan; las que más):

[SE-228](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md), [SE-113](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-113-cli-flags-configuracion-y-codigos-de-salida/README.md), [SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md), [SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md), [SE-220](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md), [SE-411](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md), [SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP — Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — delimita el contrato técnico que debe cumplirse al diseñar precedencia de configuración y tratamiento de secretos con frontera explícita.
- [The Twelve-Factor App: Config](https://12factor.net/config) — configuración fuera del código; autoridad: guía de autores, de uso extendido.
- [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/) — ubicaciones de configuración en sistemas tipo Unix; autoridad: freedesktop.org.
- [NO_COLOR](https://no-color.org/) — convención para desactivar el color; autoridad: proyecto comunitario.
- [Console Do Not Track](https://consoledonottrack.com/) — convención `DO_NOT_TRACK`; autoridad: proyecto comunitario.

---

[↑ Glosario](../../README.md) · [← Precarga](./precarga.md) · [Precisión →](./precision.md)
