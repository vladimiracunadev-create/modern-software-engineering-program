# Bloqueo

[↑ Glosario](../../README.md) · [← Bloque y rejilla](./bloque-y-rejilla.md) · [Bloqueo del estado →](./bloqueo-del-estado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Mecanismo de exclusión mutua; aquí, un archivo creado en exclusiva.

Definición de trabajo de [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-453 — Verificación formal y model checking: TLA+, SPARK y Alloy](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md): Estado sin transiciones que no es un estado final.

## Por qué importa

En [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md), el tema «Tiempo límite y bloqueo» importa porque un proceso colgado o duplicado no debe romper el sistema.

## Cómo funciona

Según [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md):

Primero se **lee** la automatización buscando debilidades conocidas: rutas sin comillas, códigos de salida ignorados, borrado antes de verificar, ausencia de tiempo límite y de bloqueo, escritura en el sitio. Segundo, se **define el resultado esperado** de cada fallo posible: ¿qué debe quedar si no hay origen? ¿Y si la copia está a medias? Tercero, se **inyecta** cada fallo y se compara. Cuarto, se **endurece** una debilidad por vez y se vuelve a inyectar. El método hace visible lo que antes era intuición y deja pruebas que evitan que vuelva.

Según [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md):

El equipo adopta una lista de comprobación de endurecimiento para cada automatización: validar entradas antes de actuar, listas de argumentos sin shell, tiempo límite en cada proceso externo, bloqueo con `O_EXCL` y limpieza en `finally`, escritura en temporal con reemplazo atómico, verificación por resumen, orden «crear y verificar, luego retirar», códigos de salida de `SE-220` y un registro con inicio, fin y resultado. Una suite de diez fallos inyectados corre en cada cambio en Windows y en Ubuntu y falla si algún escenario termina con éxito aparente o con una copia menos. El registro del taller guarda la matriz antes y después.

## Ejemplo

Ejemplo de [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md) (sección «Ejemplo profesional»):

El equipo adopta una lista de comprobación de endurecimiento para cada automatización: validar entradas antes de actuar, listas de argumentos sin shell, tiempo límite en cada proceso externo, bloqueo con `O_EXCL` y limpieza en `finally`, escritura en temporal con reemplazo atómico, verificación por resumen, orden «crear y verificar, luego retirar», códigos de salida de `SE-220` y un registro con inicio, fin y resultado. Una suite de diez fallos inyectados corre en cada cambio en Windows y en Ubuntu y falla si algún escenario termina con éxito aparente o con una copia menos. El registro del taller guarda la matriz antes y después.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Dos instancias se pisan** — causa: no hay exclusión. Corrección: bloqueo con `O_EXCL` y limpieza en `finally`. ([SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Primero se **lee** la automatización buscando debilidades conocidas: rutas sin comillas, códigos de salida ignorados, borrado antes de verificar, ausencia de tiempo límite y de bloqueo, escritura en el sitio. ([SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-226](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Exclusión](../e/exclusion.md), [Mecanismo](../m/mecanismo.md), [Transición](../t/transicion.md), [Concurrencia](../c/concurrencia.md), [Contraejemplo](../c/contraejemplo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-227 — Taller: endurecer una automatización frágil](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-453 — Verificación formal y model checking: TLA+, SPARK y Alloy](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (87 clases más lo mencionan; las que más):

[SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), [SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md), [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md).

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «lock».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: `subprocess` y consideraciones de seguridad](https://docs.python.org/3/library/subprocess.html#security-considerations) — `shell=True` y listas de argumentos; autoridad: documentación de Python.
- [OWASP: Command Injection](https://owasp.org/www-community/attacks/Command_Injection) — inyección de comandos; autoridad: OWASP.
- [CWE-78: OS Command Injection](https://cwe.mitre.org/data/definitions/78.html) — catalogación de la debilidad; autoridad: MITRE.
- [ShellCheck wiki](https://www.shellcheck.net/wiki/) — errores típicos en guiones de shell; autoridad: proyecto ShellCheck.
- [Python: `os`](https://docs.python.org/3/library/os.html) — `O_EXCL`, `os.replace` y `os.open`; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Bloque y rejilla](./bloque-y-rejilla.md) · [Bloqueo del estado →](./bloqueo-del-estado.md)
