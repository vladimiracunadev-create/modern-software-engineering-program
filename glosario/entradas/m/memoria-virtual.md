# Memoria virtual

[↑ Glosario](../../README.md) · [← Memoria persistente](./memoria-persistente.md) · [Menor privilegio →](./menor-privilegio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Memoria virtual es el espacio de direcciones que el sistema
presenta a un proceso.

Tomado del glosario de [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md).

## Por qué importa

En [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), el tema «Memoria virtual» importa porque mapea direcciones del proceso

## Cómo funciona

Según [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md):

Las direcciones que ve un proceso son virtuales. El hardware y el sistema operativo las traducen a direcciones físicas por *páginas*, bloques de tamaño fijo (en este equipo `mmap.PAGESIZE` es 4096 bytes). Una tabla de páginas asocia cada página virtual con un marco físico, y una pequeña caché de traducciones, el TLB, evita consultar la tabla en cada acceso. Esta indirección da aislamiento (un proceso no puede nombrar la memoria de otro), permite compartir páginas de forma controlada y hace posible reservar más memoria virtual que RAM física.

Según [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md):

No es una buena idea general. La memoria virtual sostiene el aislamiento y la compartición entre procesos; desactivarla o limitar el intercambio cambia el comportamiento ante falta de memoria (el sistema puede terminar procesos en lugar de ralentizarse). Cualquier ajuste debe probarse bajo carga y con un plan de recuperación.

## Ejemplo

Ejemplo de [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) (sección «Preguntas frecuentes»):

No es una buena idea general. La memoria virtual sostiene el aislamiento y la compartición entre procesos; desactivarla o limitar el intercambio cambia el comportamiento ante falta de memoria (el sistema puede terminar procesos en lugar de ralentizarse). Cualquier ajuste debe probarse bajo carga y con un plan de recuperación.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md)) son:

- **“RAM” para toda jerarquía** — causa: niveles confundidos. Corrección: declara nivel y garantía.
- **tiempo atribuido a caché concreta** — causa: instrumento insuficiente. Corrección: expresa hipótesis y alternativas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Esta indirección da aislamiento (un proceso no puede nombrar la memoria de otro), permite compartir páginas de forma controlada y hace posible reservar más memoria virtual que RAM física. ([SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Proceso](../p/proceso.md), [ABI](../a/abi.md), [Ancho de banda](../a/ancho-de-banda.md), [Arquitectura](../a/arquitectura.md), [Dispositivo](../d/dispositivo.md), [Estado](../e/estado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Memoria persistente](./memoria-persistente.md) · [Menor privilegio →](./menor-privilegio.md)
