# Consenso

[↑ Glosario](../../README.md) · [← Consecuencia negativa](./consecuencia-negativa.md) · [Consenso perezoso →](./consenso-perezoso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Acuerdo de un conjunto de nodos sobre un único valor, con acuerdo, validez y terminación.

Definición de trabajo de [SE-391 — Consenso, elección y coordinación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md).

## Por qué importa

En [SE-391 — Consenso, elección y coordinación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md), el tema «Consenso y sus límites» importa porque fija qué puede prometer un protocolo de acuerdo.

## Cómo funciona

Según [SE-391 — Consenso, elección y coordinación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md):

El **consenso** exige que un conjunto de nodos decida un valor con tres propiedades: acuerdo (todos los que deciden eligen el mismo), validez (el valor decidido fue propuesto por alguien) y terminación (los nodos correctos terminan por decidir). Fischer, Lynch y Paterson demostraron que, en un sistema asíncrono, no existe un protocolo determinista que garantice las tres si un solo proceso puede fallar: no se distingue un nodo lento de uno caído. Los protocolos prácticos esquivan el límite renunciando a la terminación en el peor caso: Paxos y Raft nunca violan el acuerdo, pero pueden no avanzar durante periodos de inestabilidad, y confían en tiempos límite y aleatoriedad para avanzar casi siempre. La seguridad (nunca dos valores) no depende del tiempo; la vivacidad (terminar) sí.

Según [SE-391 — Consenso, elección y coordinación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md):

El equipo clasifica las funciones de la plataforma. Publicar notas al cierre del plazo exige un único ejecutor: usa el servicio de coordinación que ya opera la plataforma, con un grupo de cinco nodos (tolera dos caídas), y pide un cerrojo cuya concesión incluye un testigo de cerco. La publicación escribe en la base con el testigo en cada sentencia y la base rechaza cualquier número menor que el último visto; así una pausa de recolección de memoria no puede pisar la publicación del siguiente titular. Las tareas repetibles (enviar un recordatorio) no usan titular: se hacen idempotentes (`SE-392`). El equipo no implementa Raft: mide cuántas tareas superan el arrendamiento con sus pausas reales, ajusta su duración y registra que el cerco es la defensa real.

## Ejemplo

Ejemplo de [SE-391 — Consenso, elección y coordinación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md) (sección «Ejemplo profesional»):

El equipo clasifica las funciones de la plataforma. Publicar notas al cierre del plazo exige un único ejecutor: usa el servicio de coordinación que ya opera la plataforma, con un grupo de cinco nodos (tolera dos caídas), y pide un cerrojo cuya concesión incluye un testigo de cerco. La publicación escribe en la base con el testigo en cada sentencia y la base rechaza cualquier número menor que el último visto; así una pausa de recolección de memoria no puede pisar la publicación del siguiente titular. Las tareas repetibles (enviar un recordatorio) no usan titular: se hacen idempotentes (`SE-392`).

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-391 — Consenso, elección y coordinación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md)) son:

- **Dos líderes tras un corte de red** — causa: regla local de elección. Corrección: mayoría absoluta del grupo completo.
- **Un trabajo se ejecuta dos veces** — causa: titular caducado que sigue actuando. Corrección: testigo de cerco comprobado por el recurso.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Implementar consenso es difícil y los errores no se ven en las pruebas. ([SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](./conjunto.md), [Sobre](../s/sobre.md), [Terminación](../t/terminacion.md), [Valor](../v/valor.md), [Mayoría absoluta](../m/mayoria-absoluta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-391 — Consenso, elección y coordinación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), [SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md), [SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md), [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fischer, Lynch y Paterson, «Impossibility of distributed consensus…»](https://doi.org/10.1145/3149.214121) — límite del consenso asíncrono; autoridad: artículo original (1985).
- [Lamport, «The part-time parliament»](https://doi.org/10.1145/279227.279229) — Paxos; autoridad: artículo original (1998).
- [Ongaro y Ousterhout, Raft](https://raft.github.io/raft.pdf) — elección con mandatos y plazos aleatorios; autoridad: artículo de los autores.
- [Kleppmann, «How to do distributed locking»](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html) — cerrojos con expiración y testigos de cerco; autoridad: autor del texto.
- [Burrows, «The Chubby lock service…»](https://research.google/pubs/the-chubby-lock-service-for-loosely-coupled-distributed-systems/) — servicio de coordinación en producción; autoridad: artículo de Google.

---

[↑ Glosario](../../README.md) · [← Consecuencia negativa](./consecuencia-negativa.md) · [Consenso perezoso →](./consenso-perezoso.md)
