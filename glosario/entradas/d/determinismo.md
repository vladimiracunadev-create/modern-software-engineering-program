# Determinismo

[↑ Glosario](../../README.md) · [← Detector estructural](./detector-estructural.md) · [Determinismo de una prueba →](./determinismo-de-una-prueba.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Propiedad de producir el mismo resultado ante las mismas entradas declaradas.

Definición de trabajo de [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md): Propiedad de una simulación que, con el mismo estado y las mismas entradas, llega siempre al mismo estado.
- En [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md): El resultado depende solo de las entradas declaradas.

## Por qué importa

En [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md), el tema «Fuentes de no determinismo» importa porque cada una tiene un remedio distinto.

## Cómo funciona

Según [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md):

Traslada el análisis a otra suite (por ejemplo, las pruebas de un sistema de reservas): ejecútalas en órdenes aleatorios, mide qué estrategia de fixture aísla mejor y a qué costo, e inventaría las fuentes de no determinismo. La transferencia está lograda cuando puedes explicar qué prueba dependía de cuál y cómo lo supiste, no cuando la tabla se parece.

Según [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md):

Una simulación es **determinista** si, partiendo del mismo estado y las mismas entradas, llega siempre al mismo estado. Con paso variable el estado final depende de la secuencia de duraciones de los fotogramas, que cambia con la carga de la máquina; dos ejecuciones con las mismas entradas terminan en estados distintos. Con paso fijo la secuencia de pasos es la misma, y el resultado solo depende de las entradas. Para sincronizar dos máquinas, repetir una partida o encontrar un fallo con una grabación se necesita el paso fijo. El determinismo entre máquinas distintas exige además la misma aritmética (la no asociatividad de `SE-289` reaparece) y el mismo orden de actualización.

## Ejemplo

Ejemplo de [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) (sección «Caso conductor»):

La plataforma de entregas es el caso conductor. Esta clase deja el octavo artefacto: las reglas de fixtures del equipo, la transacción por prueba y el inventario de fuentes de no determinismo. `SE-429` pasa de lo que se puede automatizar a la exploración con criterio humano. Cambia después una sola decisión, el orden de ejecución a aleatorio con semilla, y observa si aparece una dependencia que nadie había notado.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md)) son:

- **Las pruebas pasan una a una y fallan juntas** — causa: estado compartido mutable. Corrección: transacción con retroceso o base nueva por prueba.
- **Una prueba falla una vez de cada diez** — causa: datos aleatorios sin semilla o propiedad mal enunciada. Corrección: registrar la semilla y revisar la propiedad.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Traslada el análisis a otra suite (por ejemplo, las pruebas de un sistema de reservas): ejecútalas en órdenes aleatorios, mide qué estrategia de fixture aísla mejor y a qué costo, e inventaría las fuentes de no determinismo. ([SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-291](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Propiedad](../p/propiedad.md), [Resultado](../r/resultado.md), [Backfill](../b/backfill.md), [Bucle de juego](../b/bucle-de-juego.md), [Dato tardío](./dato-tardio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-292 — Videojuegos, loops, entidades y simulación](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (16 clases más lo mencionan; las que más):

[SE-116](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md), [SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md), [SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), [SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md), [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md), [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Martin Fowler, «Eradicating Non-Determinism in Tests»](https://martinfowler.com/articles/nonDeterminism.html) — causas del no determinismo; autoridad: autor del texto.
- [pytest: cómo usar fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) — ámbitos y limpieza; autoridad: documentación oficial de pytest.
- [SQLite: transacciones](https://www.sqlite.org/lang_transaction.html) — `BEGIN` y `ROLLBACK`; autoridad: documentación oficial de SQLite.
- [Documentación del módulo random](https://docs.python.org/3/library/random.html) — semillas y límites; autoridad: documentación oficial de Python.
- [Martin Fowler, «ObjectMother»](https://martinfowler.com/bliki/ObjectMother.html) — fábricas de datos de prueba; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Detector estructural](./detector-estructural.md) · [Determinismo de una prueba →](./determinismo-de-una-prueba.md)
