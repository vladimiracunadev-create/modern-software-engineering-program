# Flujos estándar

[↑ Glosario](../../README.md) · [← Flujos calientes y fríos](./flujos-calientes-y-frios.md) · [Fork →](./fork.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Canal numerado de un proceso: entrada (0), salida (1) y error (2).

Definición de trabajo de [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md).

## Por qué importa

En [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md), el tema «Flujos estándar» importa porque separar datos y diagnóstico permite componer y automatizar.

En [SE-029 — Terminales, shells y composición de comandos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md), el tema «Flujos estándar» importa porque separan datos y diagnóstico

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

- **Prerrequisito:** [Proceso](../p/proceso.md).
- **Ver también:** [Argumento](../a/argumento.md), [Búfer](../b/bufer.md), [Código de salida](../c/codigo-de-salida.md), [Modo texto y modo binario](../m/modo-texto-y-modo-binario.md), [Pipeline](../p/pipeline.md), [Redirección](../r/redireccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-029 — Terminales, shells y composición de comandos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-218 — Entrada estándar, salida y composición por pipes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), [SE-072](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md), [SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «flujo estándar».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [POSIX: Shell Command Language](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html) — tuberías, redirecciones y estado de salida; autoridad: The Open Group.
- [Python: `io`](https://docs.python.org/3/library/io.html) — búfer, modo texto y binario y saltos de línea; autoridad: documentación de Python.
- [Python: opciones de línea de comandos](https://docs.python.org/3/using/cmdline.html) — `-u` y variables de entorno; autoridad: documentación de Python.
- [Python: `signal`](https://docs.python.org/3/library/signal.html) — `SIGPIPE` y tuberías cerradas; autoridad: documentación de Python.
- [Python: `tracemalloc`](https://docs.python.org/3/library/tracemalloc.html) — medición del pico de memoria; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Flujos calientes y fríos](./flujos-calientes-y-frios.md) · [Fork →](./fork.md)
