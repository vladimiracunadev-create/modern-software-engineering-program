# Búfer

[↑ Glosario](../../README.md) · [← Bucle del agente](./bucle-del-agente.md) · [Búfer circular →](./bufer-circular.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Memoria intermedia que acumula lo escrito antes de entregarlo al destino.

Definición de trabajo de [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md).

## Por qué importa

En [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md), el tema «Búfer y latencia» importa porque una salida retenida no sirve para mostrar progreso.

## Cómo funciona

Según [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md):

Un productor emite diez líneas, una cada 0,1 s. Un consumidor lee la tubería y marca cuándo llega la primera línea. Con el comportamiento por defecto, **la primera línea llegó a los 1,2 s en Windows y a los 1,0 s en Ubuntu**: es decir, cuando el productor terminó y vació su búfer. Con `print(flush=True)` llegó a los **0,1 s** (0,0 s en Ubuntu); con `python -u`, a los 0,1 s; con `PYTHONUNBUFFERED=1`, a los 0,2 s (0,0 s). El tiempo total de las cuatro variantes fue el mismo: 1,1 a 1,2 s. Nada se hizo más rápido; lo que cambió es cuándo ve el resultado quien lo espera.

Según [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md):

`notas exportar` lee de un archivo o de `-`, procesa línea a línea, escribe los datos en stdout (o en `--salida`) y los avisos en stderr, vacía el búfer al terminar cada bloque lógico de diez mil filas y trata el cierre de la tubería como una terminación normal con código 0. La codificación de entrada es UTF-8 con o sin marca de orden de bytes, la de salida UTF-8 sin marca y el salto de línea de salida es siempre `\n`, fijado al abrir el destino. Una prueba ejecuta la herramienta con un consumidor que cierra tras la primera línea y falla si aparece la palabra «Traceback» en stderr.

## Ejemplo

Ejemplo de [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md) (sección «Ejemplo profesional»):

`notas exportar` lee de un archivo o de `-`, procesa línea a línea, escribe los datos en stdout (o en `--salida`) y los avisos en stderr, vacía el búfer al terminar cada bloque lógico de diez mil filas y trata el cierre de la tubería como una terminación normal con código 0. La codificación de entrada es UTF-8 con o sin marca de orden de bytes, la de salida UTF-8 sin marca y el salto de línea de salida es siempre `\n`, fijado al abrir el destino. Una prueba ejecuta la herramienta con un consumidor que cierra tras la primera línea y falla si aparece la palabra «Traceback» en stderr.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El progreso aparece de golpe al final** — causa: el búfer de una tubería se vacía por bloques. Corrección: `flush=True`, `-u` o vaciar por bloques lógicos. ([SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** el productor emite pocas líneas pequeñas; con un volumen grande el búfer se llena y se entrega antes, y vaciar cada línea cuesta llamadas al sistema que aquí no se midieron. ([SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Flujos estándar](../f/flujos-estandar.md), [Modo texto y modo binario](../m/modo-texto-y-modo-binario.md), [Tubería](../t/tuberia.md), [Tubería rota](../t/tuberia-rota.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-293](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md), [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: `io`](https://docs.python.org/3/library/io.html) — búfer, modo texto y binario y saltos de línea; autoridad: documentación de Python.
- [POSIX: Shell Command Language](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html) — tuberías, redirecciones y estado de salida; autoridad: The Open Group.
- [Python: opciones de línea de comandos](https://docs.python.org/3/using/cmdline.html) — `-u` y variables de entorno; autoridad: documentación de Python.
- [Python: `signal`](https://docs.python.org/3/library/signal.html) — `SIGPIPE` y tuberías cerradas; autoridad: documentación de Python.
- [Python: `tracemalloc`](https://docs.python.org/3/library/tracemalloc.html) — medición del pico de memoria; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Bucle del agente](./bucle-del-agente.md) · [Búfer circular →](./bufer-circular.md)
