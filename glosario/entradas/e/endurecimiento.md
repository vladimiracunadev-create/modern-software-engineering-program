# Endurecimiento

[↑ Glosario](../../README.md) · [← Endianess](./endianess.md) · [Energía →](./energia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Conjunto de cambios que hace que una automatización rechace o tolere condiciones adversas sin dañar el estado.

Definición de trabajo de [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md).

## Por qué importa

La clase donde se define, [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md), existe con este propósito: el taller existe para recibir una automatización que «funciona en mi máquina», inyectarle los fallos que sufrirá en producción y endurecerla hasta que cada uno termine en un rechazo ruidoso con el estado intacto, aplicando juntas las técnicas de `SE-217` a `SE-226`.

## Cómo funciona

Según [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md):

El equipo adopta una lista de comprobación de endurecimiento para cada automatización: validar entradas antes de actuar, listas de argumentos sin shell, tiempo límite en cada proceso externo, bloqueo con `O_EXCL` y limpieza en `finally`, escritura en temporal con reemplazo atómico, verificación por resumen, orden «crear y verificar, luego retirar», códigos de salida de `SE-220` y un registro con inicio, fin y resultado. Una suite de diez fallos inyectados corre en cada cambio en Windows y en Ubuntu y falla si algún escenario termina con éxito aparente o con una copia menos. El registro del taller guarda la matriz antes y después.

Según [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md):

Traslada el taller a otra automatización frágil (por ejemplo, un guion que sincroniza una carpeta con un servicio de almacenamiento de pruebas): lista sus debilidades, inyecta diez fallos y mide cuántos terminan con éxito aparente. La transferencia está lograda cuando puedes explicar qué parte del endurecimiento dependía del tipo de recurso y cuál era general, no cuando la lista de comprobación se parece.

## Ejemplo

Ejemplo de [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md) (sección «Ejemplo profesional»):

El equipo adopta una lista de comprobación de endurecimiento para cada automatización: validar entradas antes de actuar, listas de argumentos sin shell, tiempo límite en cada proceso externo, bloqueo con `O_EXCL` y limpieza en `finally`, escritura en temporal con reemplazo atómico, verificación por resumen, orden «crear y verificar, luego retirar», códigos de salida de `SE-220` y un registro con inicio, fin y resultado. Una suite de diez fallos inyectados corre en cada cambio en Windows y en Ubuntu y falla si algún escenario termina con éxito aparente o con una copia menos. El registro del taller guarda la matriz antes y después.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md)) son:

- **El trabajo termina con 0 sin hacer nada** — causa: se ignora el código de la herramienta externa. Corrección: comprobar el código y propagarlo.
- **Se pierden copias existentes tras un fallo** — causa: se borra antes de verificar lo nuevo. Corrección: crear y verificar primero; retirar después.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La transferencia está lograda cuando puedes explicar qué parte del endurecimiento dependía del tipo de recurso y cuál era general, no cuando la lista de comprobación se parece. ([SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Conjunto](../c/conjunto.md), [Estado](./estado.md), [Bloqueo](../b/bloqueo.md), [Concurrencia](../c/concurrencia.md), [Fallo silencioso](../f/fallo-silencioso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md), [SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md), [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md).

**Aparece en los casos de estudio:** [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: `subprocess` y consideraciones de seguridad](https://docs.python.org/3/library/subprocess.html#security-considerations) — `shell=True` y listas de argumentos; autoridad: documentación de Python.
- [OWASP: Command Injection](https://owasp.org/www-community/attacks/Command_Injection) — inyección de comandos; autoridad: OWASP.
- [CWE-78: OS Command Injection](https://cwe.mitre.org/data/definitions/78.html) — catalogación de la debilidad; autoridad: MITRE.
- [ShellCheck wiki](https://www.shellcheck.net/wiki/) — errores típicos en guiones de shell; autoridad: proyecto ShellCheck.
- [Python: `os`](https://docs.python.org/3/library/os.html) — `O_EXCL`, `os.replace` y `os.open`; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Endianess](./endianess.md) · [Energía →](./energia.md)
