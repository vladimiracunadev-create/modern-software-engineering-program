# Page fault

[↑ Glosario](../../README.md) · [← Pagador, usuario y decisor](./pagador-usuario-y-decisor.md) · [Página →](./pagina.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Page fault requiere intervención para resolver una página.

Tomado del glosario de [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md).

## Por qué importa

La clase donde se define, [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), existe con este propósito: la clase existe para elegir almacenamiento y acceso por localidad, latencia, capacidad y durabilidad.

## Cómo funciona

Según [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md):

Las direcciones que ve el analizador local de eventos son virtuales. El sistema y hardware traducen páginas a memoria física o manejan ausencia. Esto permite aislamiento, compartición controlada y espacios mayores que RAM, pero un acceso puede provocar page fault. Una dirección impresa no revela ubicación física estable.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md):

Un índice acelera búsqueda y aumenta memoria y escrituras. La decisión compara carga real y conjunto de trabajo, no asume que “más caché siempre mejora”.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md)) son:

- **“RAM” para toda jerarquía** — causa: niveles confundidos. Corrección: declara nivel y garantía.
- **tiempo atribuido a caché concreta** — causa: instrumento insuficiente. Corrección: expresa hipótesis y alternativas.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md)) son: No perfila cachés físicas ni NUMA. `SE-019` explica procesos, hilos e I/O que compiten por recursos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Página](./pagina.md), [Resolver](../r/resolver.md), [Ancho de banda](../a/ancho-de-banda.md), [Latencia](../l/latencia.md), [Localidad](../l/localidad.md), [Persistencia](./persistencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Pagador, usuario y decisor](./pagador-usuario-y-decisor.md) · [Página →](./pagina.md)
