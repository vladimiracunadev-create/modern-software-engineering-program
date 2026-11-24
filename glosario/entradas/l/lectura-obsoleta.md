# Lectura obsoleta

[↑ Glosario](../../README.md) · [← Lectura estática de la configuración](./lectura-estatica-de-la-configuracion.md) · [Lectura partida →](./lectura-partida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Una **lectura obsoleta** (*stale read*) es una lectura que devuelve datos anteriores a una escritura ya confirmada. [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) la trata en réplicas y particiones: una réplica sana puede devolver datos viejos. [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) la usa para cachés: la lectura de una caché cuyo dato ya cambió en el origen, es decir, un acierto cuya versión ya cambió.

## Por qué importa

No es un error del sistema, sino una consecuencia de copiar datos: cada réplica o caché tarda en enterarse. La decisión que cambia es dónde la persona *no puede* ver un dato viejo (leer su propia escritura, un saldo) y dónde sí (un historial).

## Cómo funciona

Una escritura se confirma en un nodo y se propaga a otros con un retraso. Una lectura que llega a una réplica antes de que reciba el dato lo ve viejo. [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) mide la fracción de lecturas obsoletas contra el retraso de replicación, modelando el tiempo entre escritura y lectura como exponencial con media de 50 ms: con 5 ms, el 10 % de las lecturas llegan antes de que la réplica tenga el dato; con 20 ms, el 35 %; con 100 ms, el 85 %; con 500 ms, casi todas.

La clase advierte un límite del modelo: si la interfaz espera la respuesta de la escritura antes de recargar, ese tiempo es mayor y la fracción baja. El experimento correcto mide cuántas lecturas son viejas *en el flujo de la persona*: «leer tu propia escritura».

En cachés ([SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md)), el experimento genera 200 000 lecturas de 5 000 entregas con popularidad Zipf; cada entrega cambia cada 300 a 900 s; una caché LRU de 50, 500 o 2 500 entradas con TTL de 10, 60 o 600 s cuenta aciertos y lecturas obsoletas. Un TTL más largo sube los aciertos y también las lecturas obsoletas.

## Ejemplo

Ilustración propia del flujo: una persona edita su perfil, la escritura va al nodo principal y la página recarga leyendo de una réplica con 100 ms de retraso; ve su dato anterior. Remedios habituales: leer del principal tras escribir, o enviar la versión escrita y esperar a que la réplica la alcance.

## Errores y confusiones comunes

- **Pensar que una réplica obsoleta está dañada:** está sana y atrasada.
- **Medir «cuántas lecturas son viejas» sin referirse al flujo del usuario.**
- **Subir el TTL para ganar aciertos sin contar el costo en obsolescencia.**
- **Confundirla con lectura sucia** (leer un dato no confirmado).

## Límites y cuándo no aplica

Las cifras vienen de modelos con parámetros del autor, no de un sistema medido. En un sistema de una sola copia con lecturas del principal no existe. Y para datos que cambian poco o toleran edad, no es un problema.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Origen](../o/origen.md), [429](../0-9/429.md), [Almacén de características](../a/almacen-de-caracteristicas.md), [Clave de caché](../c/clave-de-cache.md), [Cubeta de fichas](../c/cubeta-de-fichas.md), [Degradación elegante](../d/degradacion-elegante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), [SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md), [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md), [SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Lecturas obsoletas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Jepsen](https://jepsen.io/) — análisis de seguridad de sistemas distribuidos de datos; autoridad: proyecto de investigación Jepsen.
- [Sculley et al., Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — riesgos propios de los sistemas de ML; autoridad: artículo de NIPS 2015.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — variar eventos reales y medir la salida; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Google SRE: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — pruebas de recuperación e integridad de datos; autoridad: libro de ingeniería de confiabilidad de Google.
- [Python: random](https://docs.python.org/3/library/random.html) — generador con semilla usado en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Lectura estática de la configuración](./lectura-estatica-de-la-configuracion.md) · [Lectura partida →](./lectura-partida.md)
