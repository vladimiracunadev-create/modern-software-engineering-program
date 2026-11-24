# Determinismo

[↑ Glosario](../../README.md) · [← Detector estructural](./detector-estructural.md) · [Determinismo de una prueba →](./determinismo-de-una-prueba.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

El **determinismo** es la propiedad de producir el mismo resultado ante las mismas entradas declaradas. El programa lo usa con ese núcleo en varios contextos: en [SE-292](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md), una simulación es determinista si, con el mismo estado y las mismas entradas, llega siempre al mismo estado; en [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), un paso de transformación es determinista si su resultado depende solo de las entradas declaradas; en [SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md), el determinismo de los datos y de las pruebas se pierde por «fuentes de no determinismo» que hay que inventariar.

## Por qué importa

Lo que no se puede repetir no se puede depurar, comparar ni reconstruir. Con determinismo, un fallo se reproduce con una grabación de entradas, dos máquinas se sincronizan, y una transformación se puede rehacer (*backfill*) sin cambiar resultados. Sin él, una prueba que falla «a veces» no distingue un defecto de un accidente.

## Cómo funciona

La clave es **declarar todas las entradas**: todo lo que influye en el resultado y no está declarado es una fuente de no determinismo.

- **Simulación y videojuegos ([SE-292](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md)).** Con paso de tiempo variable, el estado final depende de la secuencia de duraciones de los fotogramas, que cambia con la carga de la máquina; dos ejecuciones con las mismas entradas terminan distintas. Con **paso fijo**, la secuencia de pasos es la misma y el resultado solo depende de las entradas. Para sincronizar dos máquinas, repetir una partida o encontrar un fallo con una grabación se necesita paso fijo. Entre máquinas distintas exige además la misma aritmética (la no asociatividad de [SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md) reaparece).
- **Datos y pruebas ([SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md)).** Cada fuente de no determinismo (reloj, orden de ejecución, estado compartido entre pruebas, datos aleatorios sin semilla) tiene un remedio distinto: inyectar el reloj, fijar semillas, aislar fixtures.
- **Transformaciones ([SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md)).** Si el resultado depende solo de las entradas declaradas, repetir el trabajo da lo mismo, requisito para backfills idempotentes.

## Ejemplo

[SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) propone ejecutar una suite en órdenes aleatorios, medir qué estrategia de fixture aísla mejor y a qué costo, e inventariar las fuentes de no determinismo; la transferencia está lograda cuando puedes explicar qué prueba dependía de cuál y cómo lo supiste. Ilustración propia: una prueba que compara «hoy» con una fecha fija falla en año bisiesto; la causa es el reloj como entrada no declarada.

## Errores y confusiones comunes

- **Confundir determinismo con ausencia de aleatoriedad:** un generador con semilla fija es determinista aunque «parezca» aleatorio.
- **Asumir determinismo entre máquinas** sin comprobar la aritmética.
- **Paso variable en una simulación** que se quiere repetir ([SE-292](../../../classes/part-24-software-especializado-y-dominios/se-292-videojuegos-loops-entidades-y-simulacion/README.md)).
- **Confundirlo con idempotencia:** esta es repetir una operación sin cambiar el estado; el determinismo es mismo resultado con mismas entradas.

## Límites y cuándo no aplica

El determinismo total es caro y a veces innecesario: un sistema distribuido con relojes y redes reales no lo ofrece de gratis. Es una propiedad respecto de las entradas *declaradas*; si se declara poco, vale poco. Y no implica corrección: un programa puede ser determinista y estar mal.

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
