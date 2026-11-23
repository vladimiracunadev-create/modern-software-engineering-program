# Exploración con semilla

[↑ Glosario](../../README.md) · [← Exploración](./exploracion.md) · [Exploración frente a producto →](./exploracion-frente-a-producto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Ejecución de una prueba bajo un planificador pseudoaleatorio con semilla registrada para poder repetirla.

Definición de trabajo de [SE-394 — Caos controlado y pruebas de distribución](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md).

## Por qué importa

La clase donde se define, [SE-394 — Caos controlado y pruebas de distribución](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), existe con este propósito: la clase existe para que pruebes un sistema distribuido como se rompe: inyectando fallos con una hipótesis, un alcance acotado y una condición de aborto, y explorando intercalaciones de forma sistemática y reproducible en lugar de repetir una prueba esperando suerte.

## Cómo funciona

Según [SE-394 — Caos controlado y pruebas de distribución](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md):

Un defecto de concurrencia vive en algunas intercalaciones, y la probabilidad de caer en ellas depende del **planificador**. Un planificador que alterna hilos en cada paso explora órdenes muy distintos; uno que mantiene un hilo en marcha casi siempre (como un sistema operativo con cuantos largos) casi nunca cambia en el punto malo. Dos técnicas lo aprovechan: la **exploración con semilla** (cada ejecución usa un planificador pseudoaleatorio con semilla registrada, de modo que un fallo se repite exactamente) y la **exploración sistemática** (se enumeran las intercalaciones o se limita el número de cambios, como hace CHESS). Ambas cambian «a veces falla» por «falla con esta semilla».

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-394 — Caos controlado y pruebas de distribución](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md):

El equipo escribe su primer plan de caos para el cierre de plazo. Estado estable: 99 % de las entregas aceptadas en menos de 800 ms, 0 entregas con acuse y sin registro. Hipótesis: con una réplica de calificaciones caída y el 10 % del tráfico de un curso de prueba, se mantiene el estado estable. Fallo inyectado: detener la réplica. Alcance: un curso interno en preproducción, 30 minutos. Aborto: el percentil 99 supera 2 000 ms durante 60 s o aparece una entrega con acuse sin registro.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una prueba inestable se reintenta hasta pasar** — causa: se oculta un defecto de concurrencia. Corrección: exploración con semillas y regresión. ([SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-394 — Caos controlado y pruebas de distribución](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos. No se ejecutó ninguna herramienta de caos ni se inyectó un fallo en un sistema real: el cliente, la dependencia, el planificador y las reglas del linter son construcciones del autor. La siguiente clase es un taller: reproducir una carrera y un fallo parcial hasta tener un caso mínimo y una regresión estable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Planificador](../p/planificador.md), [Semilla](../s/semilla.md), [Condición de aborto](../c/condicion-de-aborto.md), [Estado estable](./estado-estable.md), [Radio de explosión](../r/radio-de-explosion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-394 — Caos controlado y pruebas de distribución](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Basiri et al., «Chaos Engineering»](https://doi.org/10.1109/MS.2016.60) — la disciplina; autoridad: artículo de IEEE Software (2016).
- [Principios de la ingeniería del caos](https://principlesofchaos.org/) — método del experimento; autoridad: autores del manifiesto.
- [Alvaro et al., «Lineage-driven fault injection»](https://doi.org/10.1145/2723372.2723711) — inyección guiada por linaje; autoridad: artículo original (2015).
- [Jepsen](https://jepsen.io/) — pruebas con inyección de fallos y verificadores; autoridad: Jepsen.
- [Musuvathi et al., CHESS](https://www.usenix.org/legacy/event/osdi08/tech/full_papers/musuvathi/musuvathi.pdf) — exploración sistemática de intercalaciones; autoridad: artículo de OSDI (2008).

---

[↑ Glosario](../../README.md) · [← Exploración](./exploracion.md) · [Exploración frente a producto →](./exploracion-frente-a-producto.md)
