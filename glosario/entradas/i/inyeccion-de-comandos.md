# Inyección de comandos

[↑ Glosario](../../README.md) · [← Inyección](./inyeccion.md) · [Inyección de dependencias →](./inyeccion-de-dependencias.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Ejecución de órdenes no previstas porque un dato se interpretó como parte de la orden.

Definición de trabajo de [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md).

## Por qué importa

La clase donde se define, [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md), existe con este propósito: el taller existe para recibir una automatización que «funciona en mi máquina», inyectarle los fallos que sufrirá en producción y endurecerla hasta que cada uno termine en un rechazo ruidoso con el estado intacto, aplicando juntas las técnicas de `SE-217` a `SE-226`.

## Cómo funciona

Según [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md):

Se pasaron doce nombres de archivo a un proceso hijo que imprime sus argumentos, una vez como cadena con `shell=True` y otra como lista. Con `shell=True`, **seis nombres se interpretaron mal en Windows y ocho en Ubuntu**, con **una inyección de comando en Windows** (`x&echo INYECTADO`) y **dos en Ubuntu** (con `;` y con `&`). Entre los casos: `a b.txt` se partió en dos argumentos en ambos; `$HOME.txt` se expandió en Ubuntu y no en Windows; `'q'.txt` y `(x).txt` fallaron en Ubuntu y no en Windows. Con la lista de argumentos, los doce fueron correctos en Ubuntu y once en Windows: el fallo restante, `ñandú.txt`, fue de codificación de la salida del hijo (la consola usa la codificación local y el padre la leyó como UTF-8), no del citado.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md):

El equipo adopta una lista de comprobación de endurecimiento para cada automatización: validar entradas antes de actuar, listas de argumentos sin shell, tiempo límite en cada proceso externo, bloqueo con `O_EXCL` y limpieza en `finally`, escritura en temporal con reemplazo atómico, verificación por resumen, orden «crear y verificar, luego retirar», códigos de salida de `SE-220` y un registro con inicio, fin y resultado.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md)) son:

- **El trabajo termina con 0 sin hacer nada** — causa: se ignora el código de la herramienta externa. Corrección: comprobar el código y propagarlo.
- **Se pierden copias existentes tras un fallo** — causa: se borra antes de verificar lo nuevo. Corrección: crear y verificar primero; retirar después.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md)) son: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): la matriz de fallos fue idéntica; el contador y el citado difirieron por sistema. Los diez fallos, las dos versiones y el contador son del autor; no se probaron permisos, disco lleno, red ni antivirus, ni bloqueos huérfanos. La siguiente clase reúne todo en un paquete operable y multiplataforma.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Bloqueo](../b/bloqueo.md), [Concurrencia](../c/concurrencia.md), [Endurecimiento](../e/endurecimiento.md), [Fallo silencioso](../f/fallo-silencioso.md), [Inyección de fallos](./inyeccion-de-fallos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md), [SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), [SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP: Command Injection](https://owasp.org/www-community/attacks/Command_Injection) — inyección de comandos; autoridad: OWASP.
- [Python: `subprocess` y consideraciones de seguridad](https://docs.python.org/3/library/subprocess.html#security-considerations) — `shell=True` y listas de argumentos; autoridad: documentación de Python.
- [CWE-78: OS Command Injection](https://cwe.mitre.org/data/definitions/78.html) — catalogación de la debilidad; autoridad: MITRE.
- [ShellCheck wiki](https://www.shellcheck.net/wiki/) — errores típicos en guiones de shell; autoridad: proyecto ShellCheck.
- [Python: `os`](https://docs.python.org/3/library/os.html) — `O_EXCL`, `os.replace` y `os.open`; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Inyección](./inyeccion.md) · [Inyección de dependencias →](./inyeccion-de-dependencias.md)
