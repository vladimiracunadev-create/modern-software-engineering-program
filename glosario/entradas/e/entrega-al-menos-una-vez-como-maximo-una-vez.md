# Entrega al menos una vez / como máximo una vez

[↑ Glosario](../../README.md) · [← Entrega al menos una vez](./entrega-al-menos-una-vez.md) · [Entrega continua →](./entrega-continua.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Garantías que duplican o pierden, respectivamente, ante una caída.

Definición de trabajo de [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md).

## Por qué importa

La clase donde se define, [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md), existe con este propósito: la clase existe para diseñar automatizaciones que se pueden repetir y reanudar sin cambiar el resultado: que ejecutar dos veces lo mismo deje el mismo estado, que una caída en cualquier paso se recupere sin duplicar ni perder trabajo y que un archivo a medias nunca sea visible como si estuviera completo.

## Cómo funciona

[SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md):

La publicación nocturna de `notas` calcula una clave por fila (`ent-1:v3`), escribe las filas nuevas en un temporal del mismo directorio, vacía y reemplaza de forma atómica con reintentos ante `PermissionError`, y envía los avisos con la clave como cabecera de idempotencia. Un archivo de progreso (también reemplazado atómicamente) guarda la última clave publicada; al reanudar, la herramienta verifica contra el archivo final y no solo contra el de progreso.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md)) son:

- **Filas duplicadas tras reanudar** — causa: se escribe y luego se marca. Corrección: clave de fila y verificación antes de escribir.
- **Filas perdidas tras reanudar** — causa: se marca antes de escribir. Corrección: escribir primero o hacer ambas cosas atómicas.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md)) son: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): la matriz fue idéntica y el reemplazo con un archivo abierto difirió. Las caídas son excepciones simuladas; no se midió durabilidad, `fsync`, sistemas de archivos de red ni cortes de energía, y las operaciones son juguetes del autor. La siguiente clase pregunta cómo distribuir y actualizar la herramienta con las mismas garantías.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Garantía](../g/garantia.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Escritura atómica](./escritura-atomica.md), [Idempotencia](../i/idempotencia.md), [Punto de control](../p/punto-de-control.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [POSIX: `rename`](https://pubs.opengroup.org/onlinepubs/9699919799/functions/rename.html) — sustitución atómica del destino; autoridad: The Open Group.
- [Python: `os`](https://docs.python.org/3/library/os.html) — `os.replace` y `os.fsync`; autoridad: documentación de Python.
- [RFC 9110: Idempotent Methods](https://www.rfc-editor.org/rfc/rfc9110.html#name-idempotent-methods) — definición de idempotencia; autoridad: IETF.
- [Pillai et al., «All File Systems Are Not Created Equal»](https://www.usenix.org/conference/osdi14/technical-sessions/presentation/pillai) — suposiciones de atomicidad de las aplicaciones; autoridad: USENIX OSDI 2014.
- [Python: `tempfile`](https://docs.python.org/3/library/tempfile.html) — archivos temporales seguros; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Entrega al menos una vez](./entrega-al-menos-una-vez.md) · [Entrega continua →](./entrega-continua.md)
