# Modo texto y modo binario

[↑ Glosario](../../README.md) · [← Modo sombra](./modo-sombra.md) · [Módulo →](./modulo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Formas de abrir un flujo con o sin decodificación y traducción de saltos de línea.

Definición de trabajo de [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md).

## Por qué importa

La clase donde se define, [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md), existe con este propósito: la clase existe para que una herramienta se comporte bien como pieza de una tubería: lea de la entrada estándar sin cargar todo en memoria, escriba datos y diagnósticos en flujos distintos, entregue lo que produce a tiempo y termine en silencio cuando el consumidor ya no quiere más.

## Cómo funciona

[SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md):

`notas exportar` lee de un archivo o de `-`, procesa línea a línea, escribe los datos en stdout (o en `--salida`) y los avisos en stderr, vacía el búfer al terminar cada bloque lógico de diez mil filas y trata el cierre de la tubería como una terminación normal con código 0. La codificación de entrada es UTF-8 con o sin marca de orden de bytes, la de salida UTF-8 sin marca y el salto de línea de salida es siempre `\n`, fijado al abrir el destino.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md)) son:

- **El progreso aparece de golpe al final** — causa: el búfer de una tubería se vacía por bloques. Corrección: `flush=True`, `-u` o vaciar por bloques lógicos.
- **Traza al usar `head` al final de la tubería** — causa: no se maneja el cierre de la tubería. Corrección: capturar `OSError` con `errno` 22 o 32 al escribir y salir en silencio.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md)) son: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos salvo la excepción de la tubería y los tiempos. No se midió ninguna tubería de más de dos procesos, ningún terminal interactivo ni ningún consumidor de red; el productor, el tamaño del archivo y el tamaño de bloque son supuestos del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Flujo](../f/flujo.md), [Salto](../s/salto.md), [Traducción](../t/traduccion.md), [Búfer](../b/bufer.md), [Flujos estándar](../f/flujos-estandar.md), [Tubería](../t/tuberia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [POSIX: Shell Command Language](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html) — tuberías, redirecciones y estado de salida; autoridad: The Open Group.
- [Python: `io`](https://docs.python.org/3/library/io.html) — búfer, modo texto y binario y saltos de línea; autoridad: documentación de Python.
- [Python: opciones de línea de comandos](https://docs.python.org/3/using/cmdline.html) — `-u` y variables de entorno; autoridad: documentación de Python.
- [Python: `signal`](https://docs.python.org/3/library/signal.html) — `SIGPIPE` y tuberías cerradas; autoridad: documentación de Python.
- [Python: `tracemalloc`](https://docs.python.org/3/library/tracemalloc.html) — medición del pico de memoria; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Modo sombra](./modo-sombra.md) · [Módulo →](./modulo.md)
