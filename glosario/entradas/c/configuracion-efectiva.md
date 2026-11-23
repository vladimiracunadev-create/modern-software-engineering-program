# Configuración efectiva

[↑ Glosario](../../README.md) · [← Confianza y extensiones](./confianza-y-extensiones.md) · [Configuración por capas →](./configuracion-por-capas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Valores resultantes junto con su procedencia.

Definición de trabajo de [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md): Valor final de cada opción tras aplicar la precedencia, con su fuente.

## Por qué importa

La clase donde se define, [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md), existe con este propósito: la clase existe para diseñar precedencia de configuración y tratamiento de secretos con frontera explícita.

## Cómo funciona

Según [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md):

Con `resolver(None, "8081", "8082", "8080")` el resultado es `("entorno", "8081")`; con `resolver("9000", "8081", "8082", "8080")`, `("argumento", "9000")`; y con tres `None`, `("default", "8080")`. El valor de que devuelva la *fuente* es doble: permite explicar la configuración efectiva («el puerto viene del entorno») y probar el orden con casos sencillos. El laboratorio aplica exactamente este orden a `profile` y su reporte conserva la fuente elegida.

Según [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md):

Un resolvedor que devuelve solo el valor obliga a depurar a ciegas. Uno que devuelve también la fuente («formato = json, de `config.ini` línea 3») ahorra horas. Una opción `--print-config` o un modo detallado que muestre la configuración efectiva y su origen, **enmascarando los secretos**, es una herramienta de diagnóstico y también la mejor documentación de la precedencia.

## Ejemplo

Ejemplo de [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md) (sección «Preguntas frecuentes»):

Por cercanía a la invocación: quien escribe el flag lo hace ahora, para esta ejecución. Pero es una convención. Algunas herramientas ponen primero una política administrativa; lo esencial es que el orden esté escrito, probado y visible en la configuración efectiva.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Cambiar el archivo no cambia la ejecución** — causa: una variable de mayor precedencia quedó activa. Corrección: mostrar configuración efectiva y procedencia. ([SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md))
- **Nadie sabe de dónde salió un valor** — causa: el resolvedor no informa de la fuente. Corrección: mostrar la configuración efectiva con su origen. ([SE-219](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md)) son: No diseñamos una infraestructura empresarial de secretos ni garantizamos borrado físico de memoria. El kit de diagnóstico multiplataforma también depende de herramientas instaladas; la siguiente clase analiza gestores de paquetes, procedencia y reversibilidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Opción](../o/opcion.md), [Precedencia](../p/precedencia.md), [Procedencia](../p/procedencia.md), [Valor](../v/valor.md), [Esquema](../e/esquema.md), [Herencia](../h/herencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-219 — Configuración, flags, archivos y precedencia](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — about_Environment_Variables](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_environment_variables) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [The Open Group — Environment Variables](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap08.html) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [OWASP — Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — delimita el contrato técnico que debe cumplirse al diseñar precedencia de configuración y tratamiento de secretos con frontera explícita.
- [Python documentation — configparser](https://docs.python.org/3/library/configparser.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [The Twelve-Factor App: Config](https://12factor.net/config) — configuración fuera del código; autoridad: guía de autores, de uso extendido.

---

[↑ Glosario](../../README.md) · [← Confianza y extensiones](./confianza-y-extensiones.md) · [Configuración por capas →](./configuracion-por-capas.md)
