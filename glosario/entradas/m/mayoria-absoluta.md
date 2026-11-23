# Mayoría absoluta

[↑ Glosario](../../README.md) · [← Matriz real](./matriz-real.md) · [MC/DC →](./mc-dc.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Más de la mitad de los nodos del grupo completo, no de los que se ven.

Definición de trabajo de [SE-391 — Consenso, elección y coordinación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md).

## Por qué importa

La clase donde se define, [SE-391 — Consenso, elección y coordinación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md), existe con este propósito: la clase existe para que sepas cuándo un sistema necesita que varios nodos se pongan de acuerdo sobre un único valor o un único líder, qué hace que ese acuerdo sea seguro (mayorías que se cruzan, mandatos crecientes, testigos de cerco) y qué parte conviene delegar en un servicio de coordinación en lugar de implementarla a mano con relojes y tiempos límite.

## Cómo funciona

Según [SE-391 — Consenso, elección y coordinación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md):

Una regla local como «soy líder si tengo el identificador mayor entre los nodos que veo» es insegura: en una partición cada lado tiene su mayor y habrá un líder por lado. La regla segura exige una **mayoría absoluta**: se es líder solo si más de la mitad del grupo total lo reconoce. Dos mayorías absolutas siempre comparten al menos un nodo, y ese nodo no puede votar por dos líderes en el mismo mandato; por eso, a lo sumo uno puede reunir la mayoría. El precio es que un grupo sin mayoría no elige a nadie: se pierde disponibilidad para conservar la unicidad, exactamente la decisión de `SE-390`.

## Ejemplo

Ejemplo de [SE-391 — Consenso, elección y coordinación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra que dos mayorías absolutas se cruzan. Antes de ejecutarlo, predice si existen dos subconjuntos disjuntos de tres nodos entre cinco.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Dos líderes tras un corte de red** — causa: regla local de elección. Corrección: mayoría absoluta del grupo completo. ([SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La regla segura exige una **mayoría absoluta**: se es líder solo si más de la mitad del grupo total lo reconoce. ([SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Consenso](../c/consenso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-391 — Consenso, elección y coordinación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Lamport, «The part-time parliament»](https://doi.org/10.1145/279227.279229) — Paxos; autoridad: artículo original (1998).
- [Ongaro y Ousterhout, Raft](https://raft.github.io/raft.pdf) — elección con mandatos y plazos aleatorios; autoridad: artículo de los autores.
- [Fischer, Lynch y Paterson, «Impossibility of distributed consensus…»](https://doi.org/10.1145/3149.214121) — límite del consenso asíncrono; autoridad: artículo original (1985).
- [Kleppmann, «How to do distributed locking»](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html) — cerrojos con expiración y testigos de cerco; autoridad: autor del texto.
- [Burrows, «The Chubby lock service…»](https://research.google/pubs/the-chubby-lock-service-for-loosely-coupled-distributed-systems/) — servicio de coordinación en producción; autoridad: artículo de Google.

---

[↑ Glosario](../../README.md) · [← Matriz real](./matriz-real.md) · [MC/DC →](./mc-dc.md)
