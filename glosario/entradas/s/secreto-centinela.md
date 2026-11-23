# Secreto centinela

[↑ Glosario](../../README.md) · [← Secreto](./secreto.md) · [Secreto incrustado →](./secreto-incrustado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Valor ficticio reconocible usado para comprobar filtraciones.

Definición de trabajo de [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md).

## Por qué importa

La clase donde se define, [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md), existe con este propósito: la clase existe para diseñar precedencia de configuración y tratamiento de secretos con frontera explícita.

## Cómo funciona

[SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md):

Un servicio rota un token en un almacén, pero un volcado de entorno conserva el anterior. La corrección elimina volcados generales, construye un entorno mínimo para hijos y prueba el centinela en excepciones y paquetes diagnósticos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md)) son:

- **Cambiar el archivo no cambia la ejecución** — causa: una variable de mayor precedencia quedó activa. Corrección: mostrar configuración efectiva y procedencia.
- **`false` se interpreta como verdadero** — causa: se convirtió texto por presencia. Corrección: definir y validar un vocabulario booleano.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md)) son: No diseñamos una infraestructura empresarial de secretos ni garantizamos borrado físico de memoria. El kit de diagnóstico multiplataforma también depende de herramientas instaladas; la siguiente clase analiza gestores de paquetes, procedencia y reversibilidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor](../v/valor.md), [Configuración efectiva](../c/configuracion-efectiva.md), [Esquema](../e/esquema.md), [Herencia](../h/herencia.md), [Precedencia](../p/precedencia.md), [Redacción](../r/redaccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), [SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — about_Environment_Variables](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_environment_variables) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [The Open Group — Environment Variables](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap08.html) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [OWASP — Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — delimita el contrato técnico que debe cumplirse al diseñar precedencia de configuración y tratamiento de secretos con frontera explícita.
- [Python documentation — configparser](https://docs.python.org/3/library/configparser.html) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Secreto](./secreto.md) · [Secreto incrustado →](./secreto-incrustado.md)
