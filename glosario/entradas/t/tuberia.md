# Tubería

[↑ Glosario](../../README.md) · [← Truthiness](./truthiness.md) · [Tubería rota →](./tuberia-rota.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Conexión de la salida estándar de un proceso con la entrada estándar de otro.

Definición de trabajo de [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md): Conexión entre la salida de un filtro y la entrada del siguiente.

## Por qué importa

En [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md), el tema «Cierre de tubería» importa porque una traza al terminar es un defecto que oculta los errores reales.

## Cómo funciona

Según [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md):

Convencionalmente, un argumento `-` significa «lee de la entrada estándar», y la herramienta debe tratar un archivo y una tubería igual. La diferencia práctica: un archivo tiene tamaño, se puede releer y se puede saltar; una tubería no. Una herramienta que necesita dos pasadas sobre la entrada debe guardarla o rechazar la tubería con un mensaje claro. Procesar línea a línea convierte la memoria en una constante; cargar todo la hace proporcional al tamaño.

Según [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md):

`notas exportar` lee de un archivo o de `-`, procesa línea a línea, escribe los datos en stdout (o en `--salida`) y los avisos en stderr, vacía el búfer al terminar cada bloque lógico de diez mil filas y trata el cierre de la tubería como una terminación normal con código 0. La codificación de entrada es UTF-8 con o sin marca de orden de bytes, la de salida UTF-8 sin marca y el salto de línea de salida es siempre `\n`, fijado al abrir el destino. Una prueba ejecuta la herramienta con un consumidor que cierra tras la primera línea y falla si aparece la palabra «Traceback» en stderr.

## Ejemplo

Ejemplo de [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md) (sección «Ejemplo profesional»):

`notas exportar` lee de un archivo o de `-`, procesa línea a línea, escribe los datos en stdout (o en `--salida`) y los avisos en stderr, vacía el búfer al terminar cada bloque lógico de diez mil filas y trata el cierre de la tubería como una terminación normal con código 0. La codificación de entrada es UTF-8 con o sin marca de orden de bytes, la de salida UTF-8 sin marca y el salto de línea de salida es siempre `\n`, fijado al abrir el destino. Una prueba ejecuta la herramienta con un consumidor que cierra tras la primera línea y falla si aparece la palabra «Traceback» en stderr.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El progreso aparece de golpe al final** — causa: el búfer de una tubería se vacía por bloques. Corrección: `flush=True`, `-u` o vaciar por bloques lógicos. ([SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md))
- **Traza al usar `head` al final de la tubería** — causa: no se maneja el cierre de la tubería. Corrección: capturar `OSError` con `errno` 22 o 32 al escribir y salir en silencio. ([SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Sin manejo, ambos salieron con código 1 y una traza (`OSError: [Errno 22] Invalid argument` y `BrokenPipeError: [Errno 32] Broken pipe`). ([SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md))
- La transferencia está lograda cuando puedes explicar qué parte de la decisión dependía de que el destino fuera una tubería y cuál del volumen, no cuando el código se parece. ([SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Filtro](../f/filtro.md), [Proceso](../p/proceso.md), [Búfer](../b/bufer.md), [Cola de rechazos](../c/cola-de-rechazos.md), [Contrapresión](../c/contrapresion.md), [Filtro con estado](../f/filtro-con-estado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (21 clases más lo mencionan; las que más):

[SE-220](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md), [SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-113](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-113-cli-flags-configuracion-y-codigos-de-salida/README.md), [SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md), [SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md), [SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md), [SE-219](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Amazon](../../../casos/exito/amazon.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «pipe».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [POSIX: Shell Command Language](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html) — tuberías, redirecciones y estado de salida; autoridad: The Open Group.
- [Python: `signal`](https://docs.python.org/3/library/signal.html) — `SIGPIPE` y tuberías cerradas; autoridad: documentación de Python.
- [Python: `subprocess`](https://docs.python.org/3/library/subprocess.html) — procesos hijo con tuberías para medir la latencia.
- [Python: `io`](https://docs.python.org/3/library/io.html) — búfer, modo texto y binario y saltos de línea; autoridad: documentación de Python.
- [Python: opciones de línea de comandos](https://docs.python.org/3/using/cmdline.html) — `-u` y variables de entorno; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Truthiness](./truthiness.md) · [Tubería rota →](./tuberia-rota.md)
