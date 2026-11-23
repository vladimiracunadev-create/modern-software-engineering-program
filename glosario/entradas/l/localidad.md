# Localidad

[↑ Glosario](../../README.md) · [← Locale](./locale.md) · [Localización →](./localizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Tendencia de reutilización temporal o espacial.

Definición de trabajo de [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md).

## Por qué importa

En [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), el tema «Localidad» importa porque reutiliza datos cercanos en tiempo o espacio

## Cómo funciona

Según [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md):

Localidad temporal significa volver a datos recientes; espacial, acceder a direcciones cercanas. Cachés transfieren líneas, por lo que recorrer datos contiguos suele aprovechar espacio. El resultado depende de representación, tamaño, asociatividad, otros procesos y prefetch. Medir un patrón no prueba cuál mecanismo dominó.

## Ejemplo

Ejemplo de [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) (sección «Ejemplo mínimo»):

Acceder diez veces al mismo elemento tiene localidad temporal. Recorrer una lista contigua tiene espacial; saltar aleatoriamente reduce predictibilidad aunque haga la misma suma.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md)) son:

- **“RAM” para toda jerarquía** — causa: niveles confundidos. Corrección: declara nivel y garantía.
- **tiempo atribuido a caché concreta** — causa: instrumento insuficiente. Corrección: expresa hipótesis y alternativas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Es un patrón *compatible* con efectos de localidad, pero el script solo cronometra: no cuenta aciertos de caché. ([SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ancho de banda](../a/ancho-de-banda.md), [Latencia](./latencia.md), [Página](../p/pagina.md), [Persistencia](../p/persistencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md), [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Locale](./locale.md) · [Localización →](./localizacion.md)
