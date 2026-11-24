# Clave caliente

[↑ Glosario](../../README.md) · [← Clausura transitiva](./clausura-transitiva.md) · [Clave de caché →](./clave-de-cache.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Una **clave caliente** es una clave que recibe una fracción desproporcionada de las peticiones ([SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md)). En un sistema particionado por clave, la partición que la contiene soporta una carga muy superior a la de las demás, aunque los datos estén repartidos de forma equilibrada.

## Por qué importa

Particionar por clave promete escalar horizontalmente: más nodos, más capacidad. La clave caliente rompe esa promesa, porque la capacidad que se añade no llega al nodo saturado. La decisión que cambia es dónde se busca la solución: no en comprar más nodos, sino en rediseñar la clave o en sacar la carga de esa partición. Reconocerla evita gastar en escala que no alivia el cuello de botella.

## Cómo funciona

El reparto por clave solo equilibra la carga si la popularidad de las claves es aproximadamente uniforme. [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) señala el caso real: unos pocos estudiantes o cursos concentran muchas peticiones. Como una clave vive en una sola partición, esa partición recibe todo el tráfico de la clave, y **añadir nodos no la alivia** porque la clave no se reparte entre ellos. En la simulación de [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) la popularidad sigue una distribución de Zipf (supuesto del autor), donde pocas claves acumulan la mayoría de las peticiones.

[SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) da tres salidas:

1. **Cambiar la clave**, repartiendo por un campo más fino.
2. **Dividir la clave caliente en subclaves**: las escrituras se reparten, a costa de que las lecturas deban consultar todas y de complejidad adicional.
3. **Servirla desde una caché** ([SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md)), que absorbe las lecturas repetidas.

Y un agravante: un rango contiguo de identificadores es la peor elección cuando los identificadores recientes son los populares, porque todo el tráfico cae en la última partición.

## Ejemplo

Una plataforma de entregas particiona por identificador de curso. Un curso muy activo en fecha de entrega recibe la mayor parte del tráfico y su nodo se satura, mientras los otros están ociosos. Duplicar los nodos no cambia nada. Repartir por curso y estudiante reparte la carga; o se divide el curso caliente en subclaves, o se sirve su lectura desde caché. Ilustración del escenario de [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md).

## Errores y confusiones comunes

- **Un nodo está saturado y los demás ociosos**: clave caliente o rango contiguo; se corrige cambiando la clave, repartiendo en subclaves o con caché.
- **Responder con más nodos**: no mueve la carga de la clave.
- **Confundirla con un desequilibrio de datos**: el problema es de tráfico, no de volumen almacenado.
- **Olvidar el costo del reparto en subclaves**: las lecturas pasan a tocar varias particiones.

## Límites y cuándo no aplica

[SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) advierte que sus tres simulaciones con semilla fija no usaron base distribuida ni red; el retardo exponencial, la lectura uniforme y la popularidad Zipf son supuestos del autor, y no se midió latencia ni el costo de mover datos. El concepto aplica a sistemas particionados por clave; con carga realmente uniforme o con un solo nodo, no es el problema. La caché solo ayuda con lecturas, no con escrituras sobre la misma clave.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cuórum](./cuorum.md), [Hash consistente](../h/hash-consistente.md), [Lectura de la propia escritura](../l/lectura-de-la-propia-escritura.md), [Replicación asíncrona](../r/replicacion-asincrona.md), [Retardo de replicación](../r/retardo-de-replicacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [PostgreSQL: replicación y servidores en espera](https://www.postgresql.org/docs/current/warm-standby.html) — replicación síncrona y asíncrona; autoridad: documentación oficial de PostgreSQL.
- [PostgreSQL: particionado](https://www.postgresql.org/docs/current/ddl-partitioning.html) — particionado por rango, lista y hash; autoridad: documentación oficial de PostgreSQL.
- [Karger et al., «Consistent hashing and random trees»](https://dl.acm.org/doi/10.1145/258533.258660) — hash consistente; autoridad: artículo original (1997).
- [DeCandia et al., «Dynamo»](https://www.allthingsdistributed.com/2007/10/amazons_dynamo.html) — cuórum, nodos virtuales y reparto; autoridad: artículo de los autores.
- [Jepsen: modelos de consistencia](https://jepsen.io/consistency) — mapa de modelos de consistencia; autoridad: proyecto Jepsen.

---

[↑ Glosario](../../README.md) · [← Clausura transitiva](./clausura-transitiva.md) · [Clave de caché →](./clave-de-cache.md)
