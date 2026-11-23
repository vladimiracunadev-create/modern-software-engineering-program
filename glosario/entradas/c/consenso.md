# Consenso

[↑ Glosario](../../README.md) · [← Consecuencia negativa](./consecuencia-negativa.md) · [Consenso perezoso →](./consenso-perezoso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

El **consenso** es el acuerdo de un conjunto de nodos sobre un único valor, con tres propiedades que [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md) exige: **acuerdo** (todos los que deciden eligen el mismo valor), **validez** (el valor decidido fue propuesto por alguien) y **terminación** (los nodos correctos terminan por decidir). No es lo mismo que que los nodos tengan copias parecidas: es una decisión única y compartida, por ejemplo quién es el líder o qué entrada ocupa un lugar del registro.

## Por qué importa

Sin consenso, dos partes de un sistema pueden creerse con derecho a lo mismo. [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md) lo muestra con la elección de líder: una regla local como «soy líder si tengo el identificador mayor entre los nodos que veo» es insegura, porque en una partición cada lado tiene su mayor y habrá un líder por lado. Los errores de este tipo no se ven en pruebas con todos los nodos sanos, y por eso la clase pide delegarlos en protocolos bien conocidos.

## Cómo funciona

El resultado de Fischer, Lynch y Paterson que cita [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md): en un sistema asíncrono no existe un protocolo determinista que garantice las tres propiedades si un solo proceso puede fallar, porque no se distingue un nodo lento de uno caído. Los protocolos prácticos esquivan el límite renunciando a la terminación en el peor caso. Paxos y Raft nunca violan el acuerdo, pero pueden no avanzar durante periodos de inestabilidad, y confían en tiempos límite y aleatoriedad para avanzar casi siempre. La **seguridad** (nunca dos valores) no depende del tiempo; la **vivacidad** (terminar) sí.

Piezas que la clase desarrolla:

- **Mayoría absoluta.** Se es líder solo si más de la mitad del grupo total lo reconoce; dos mayorías absolutas comparten al menos un nodo, que no puede votar por dos líderes en el mismo mandato. El precio es que un grupo sin mayoría no elige a nadie: se pierde disponibilidad para conservar la unicidad.
- **Tamaño del grupo.** Un grupo de 2*f* + 1 nodos tolera *f* caídas: con 3 nodos, 1; con 5, 2; con 7, 3. Un grupo de tamaño par no ayuda: 4 nodos toleran 1 caída, igual que 3, con más mensajes.
- **Mandatos y plazos aleatorios (Raft).** El tiempo se divide en mandatos; si dos nodos se postulan a la vez, los votos se reparten y el mandato termina sin líder; aleatorizar el plazo de cada nodo hace que casi siempre uno se postule antes. La dispersión debe superar el retardo de los mensajes.
- **Arrendamientos y testigos de cerco.** Un arrendamiento concede un derecho por un tiempo, pero un titular pausado puede actuar tras caducar; el testigo de cerco, un número creciente que el recurso comprueba en cada escritura, hace que la seguridad dependa del recurso y no de que el titular crea estar vigente.

## Ejemplo

En la enumeración de [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md) sobre un grupo de cinco nodos, la regla ingenua del identificador mayor produce dos o tres líderes en toda partición; la regla de mayoría produce uno, o ninguno cuando ningún grupo tiene mayoría (2 | 2 | 1). El caso sin líder es el precio de la seguridad: el servicio se detiene en lugar de mentir. En otro experimento, con arrendamientos de 10 s y pausa media de 4 s, hay 849 escrituras de un titular caducado en 10 000 tareas; sin cerco el almacén las acepta todas, con cerco las rechaza todas.

## Errores y confusiones comunes

- **Dos líderes tras un corte de red.** Regla local de elección; corrección ([SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md)): mayoría absoluta del grupo completo.
- **Un trabajo se ejecuta dos veces.** Titular caducado que sigue actuando; corrección: testigo de cerco comprobado por el recurso.
- **La elección tarda o no termina.** Plazos sin aleatoriedad o con poca dispersión; corrección: aleatorizar con dispersión mayor que el retardo.
- **El servicio se detiene sin mayoría.** Grupo sin cuórum; corrección: dimensionar el grupo y diseñar el modo degradado.

## Límites y cuándo no aplica

Los modelos de [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md) son deliberadamente parciales: la enumeración de particiones no incluye mensajes ni retrasos, y la simulación de elección es un modelo para entender por qué aleatorizar, no un simulador de Raft. La mayoría es necesaria pero la clase no afirma que sea suficiente; un protocolo real debe garantizar además que un líder anterior deje de actuar. El testigo de cerco solo protege si el recurso compara testigos: si es una API externa que no lo hace, no protege. Implementar consenso es difícil y los errores no se ven en las pruebas, por lo que la clase recomienda delegarlo en un servicio de coordinación pequeño.

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
