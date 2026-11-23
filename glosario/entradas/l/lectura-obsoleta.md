# Lectura obsoleta

[↑ Glosario](../../README.md) · [← Lectura estática de la configuración](./lectura-estatica-de-la-configuracion.md) · [Lectura partida →](./lectura-partida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Lectura que devuelve datos anteriores a una escritura ya confirmada.

Definición de trabajo de [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md): Lectura de una caché cuyo dato ya cambió en el origen.

## Por qué importa

En [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), el tema «Lecturas obsoletas» importa porque una réplica sana puede devolver datos viejos.

## Cómo funciona

Según [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md):

**Cómo leer la figura.** El eje horizontal es el retraso de replicación en escala logarítmica y el vertical, el porcentaje de lecturas obsoletas. Con 5 ms, 10 % de las lecturas llegan antes de que la réplica tenga el dato; con 20 ms, 35 %; con 100 ms, 85 %; con 500 ms, casi todas. **Dónde deja de valer:** el tiempo entre la escritura y la lectura se modeló exponencial con media de 50 ms; si la interfaz espera la respuesta de la escritura antes de recargar, ese tiempo es mayor y la fracción baja. El experimento correcto no mide «cuántas lecturas son viejas» en el vacío sino cuántas lo son en el flujo de la persona: «leer tu propia escritura».

Según [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md):

Se generan 200 000 lecturas (100 por segundo) de 5 000 entregas con popularidad Zipf de exponente 1,0 (semilla 249); cada entrega cambia cada 300 a 900 s. Una caché LRU con capacidad de 50, 500 o 2 500 entradas y TTL de 10, 60 o 600 s cuenta aciertos y lecturas obsoletas (un acierto cuya versión ya cambió).

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md):

Supón, como caso hipotético y no como medición, que el equipo del almacenamiento escribe tres experimentos de datos. El primero mata el primario en preproducción con una carga sintética de 200 escrituras por segundo y compara el registro de confirmaciones del cliente con la réplica promovida; la hipótesis es «se pierden menos de 5 escrituras» y la señal, el conteo diferencial. El segundo inyecta 100 ms de retraso en la réplica y comprueba que el flujo «subir y recargar» muestra la entrega propia en el 99,9 % de los casos.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md)) son:

- **Escrituras confirmadas desaparecen tras una conmutación** — causa: replicación asíncrona con RPO declarado de cero. Corrección: medir la pérdida y elegir replicación semisíncrona o ajustar el RPO.
- **Una persona no ve lo que acaba de subir** — causa: lectura desde una réplica atrasada. Corrección: leer del primario tras escribir o devolver el estado en la escritura.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md)) son: Las definiciones son operativas para el almacenamiento de las entregas y su modelo. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos.

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
