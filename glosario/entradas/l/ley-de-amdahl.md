# Ley de Amdahl

[↑ Glosario](../../README.md) · [← Lentitud de la dependencia](./lentitud-de-la-dependencia.md) · [Ley de Conway →](./ley-de-conway.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Cota de la aceleración total por la parte no acelerada.

Definición de trabajo de [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md): Relación que acota la aceleración de una carga por la fracción que no puede dividirse.

## Por qué importa

La clase donde se define, [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md), existe con este propósito: la clase existe para que la decisión «¿usamos un acelerador?» se tome con una cuenta y no con una impresión.

## Cómo funciona

Según [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md):

La ley de Amdahl acota la mejora por la parte que no se acelera. Con una parte serie `s` y una aceleración `k` del resto, la aceleración total es `1 / (s + (1 − s)/k)`. Con un acelerador discreto aparece un término más: la fracción `t` del tiempo base que se gasta en mover datos, y la fórmula es `1 / (s + t + (1 − s)/k)`. Con `k = 50`, los valores calculados son: con `s = 0,05`, sin transferencia 14,5 veces; con `t = 0,05`, 8,4; con `t = 0,20`, 3,7. Con `s = 0,20`: 4,6 sin transferencia; 3,8 con `t = 0,05`; 2,4 con `t = 0,20`.

Según [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md):

Se calcula la ley de Amdahl para cuatro fracciones secuenciales y cinco tamaños de grupo, y cuántos trabajadores harían falta para alcanzar el 90 % del tope.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La ley de Amdahl acota la mejora por la parte que no se acelera. ([SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-280](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md), [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cota](../c/cota.md), [Relación](../r/relacion.md), [Concurrencia](../c/concurrencia.md), [Corrutina](../c/corrutina.md), [GIL](../g/gil.md), [Latencia de cola](./latencia-de-cola.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md), [SE-280](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: asyncio](https://docs.python.org/3/library/asyncio.html) — bucle de eventos y corrutinas; autoridad: documentación de Python.
- [Python: desarrollo con asyncio](https://docs.python.org/3/library/asyncio-dev.html) — modo de depuración y código bloqueante; autoridad: documentación de Python.
- [Python: glosario](https://docs.python.org/3/glossary.html) — definición del bloqueo global del intérprete; autoridad: documentación de Python.
- [Python: concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) — ejecutores de hilos y procesos; autoridad: documentación de Python.
- [Amdahl, «Validity of the single processor approach…»](https://doi.org/10.1145/1465482.1465560) — límite de aceleración; autoridad: artículo original (1967).

---

[↑ Glosario](../../README.md) · [← Lentitud de la dependencia](./lentitud-de-la-dependencia.md) · [Ley de Conway →](./ley-de-conway.md)
