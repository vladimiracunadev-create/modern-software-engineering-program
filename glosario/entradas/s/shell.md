# Shell

[↑ Glosario](../../README.md) · [← SHA de commit](./sha-de-commit.md) · [Sidecar →](./sidecar.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Lenguaje que analiza órdenes y coordina procesos.

Definición de trabajo de [SE-029 — Terminales, shells y composición de comandos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md).

## Por qué importa

En [SE-029 — Terminales, shells y composición de comandos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md), el tema «Análisis del shell» importa porque convierte texto en invocaciones y redirecciones

## Cómo funciona

Según [SE-029 — Terminales, shells y composición de comandos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md):

La terminal es una interfaz de entrada/salida —hoy normalmente un emulador— conectada a una sesión. El shell es un intérprete y lenguaje que lee órdenes, realiza expansiones y lanza comandos. Dentro de Windows Terminal pueden ejecutarse PowerShell, `cmd` o un shell de WSL; cambiar la ventana no cambia automáticamente la semántica del lenguaje.

Según [SE-029 — Terminales, shells y composición de comandos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md):

Protege de la expansión del shell, pero no del programa que reciba el texto: si una herramienta interpreta su argumento como patrón, expresión regular o código (por ejemplo, `sed` o `find -exec`), el contenido sigue siendo peligroso. Y las comillas cambian entre shells: las simples de Bash y las de PowerShell no son idénticas.

## Ejemplo

Ejemplo de [SE-029 — Terminales, shells y composición de comandos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md) (sección «Preguntas frecuentes»):

Protege de la expansión del shell, pero no del programa que reciba el texto: si una herramienta interpreta su argumento como patrón, expresión regular o código (por ejemplo, `sed` o `find -exec`), el contenido sigue siendo peligroso. Y las comillas cambian entre shells: las simples de Bash y las de PowerShell no son idénticas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una ruta con espacios se divide** — causa: el shell interpretó una cadena sin protección. Corrección: pasar argumentos como colección o citar según el shell. ([SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Dentro de Windows Terminal pueden ejecutarse PowerShell, `cmd` o un shell de WSL; cambiar la ventana no cambia automáticamente la semántica del lenguaje. ([SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Proceso](../p/proceso.md).
- **Ver también:** [Argumento](../a/argumento.md), [Código de salida](../c/codigo-de-salida.md), [Flujos estándar](../f/flujos-estandar.md), [Pipeline](../p/pipeline.md), [Redirección](../r/redireccion.md), [Stderr](./stderr.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-029 — Terminales, shells y composición de comandos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (35 clases más lo mencionan; las que más):

[SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md), [SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md), [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-220](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md), [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Open Group — Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [GNU Bash Reference Manual 5.3](https://www.gnu.org/software/bash/manual/) — documenta parsing, expansión, quoting, pipelines y estado de salida en Bash.
- [Microsoft Learn — PowerShell documentation](https://learn.microsoft.com/powershell/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Microsoft Learn — about_Pipelines](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pipelines) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.

---

[↑ Glosario](../../README.md) · [← SHA de commit](./sha-de-commit.md) · [Sidecar →](./sidecar.md)
