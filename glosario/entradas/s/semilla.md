# Semilla

[↑ Glosario](../../README.md) · [← Semiabierto](./semiabierto.md) · [Semver →](./semver.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Una **semilla** es el valor inicial de un generador pseudoaleatorio que permite repetir su secuencia ([SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md)). Con la misma semilla, el generador produce los mismos «azares» en el mismo orden. En [SE-411](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md) el término tiene otro sentido: los datos iniciales que se crean para que un cliente nuevo tenga algo con qué empezar (*seed data*).

## Por qué importa

Los datos aleatorios amplían los casos que se prueban, pero rompen la reproducibilidad: un fallo que no se puede repetir no se puede investigar. La decisión que cambia es que el azar se conserva, pero su origen se registra. Con la semilla impresa, un fallo intermitente se vuelve determinista.

## Cómo funciona

[SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) lo plantea así: la corrección no es quitar el azar sino **registrar la semilla**. Cada ejecución genera con una semilla impresa en el informe, y quien ve un fallo lo repite con ella. La clase añade un efecto de composición: una propiedad que falla con probabilidad pequeña por elemento falla con probabilidad mucho mayor con veinte elementos, de modo que un generador con muchos elementos por prueba hace aflorar casos raros a menudo y los hace parecer intermitentes.

La clase fija reglas concretas para el equipo de la plataforma: la suite se ejecuta cada noche en un orden aleatorio con semilla impresa y un fallo se repite con una opción `--semilla`; toda prueba con datos aleatorios recibe un generador con semilla de un único punto; los constructores crean datos con valores por defecto y los valores con significado se nombran. Un inventario trimestral busca usos de reloj, `uuid`, `random` y conjuntos sin orden definido, que son las fuentes habituales de no determinismo.

En [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md) (ML en producción), una corrida de entrenamiento es función de cinco cosas: los datos (filas y orden), las etiquetas, la configuración, el generador aleatorio con su semilla y el entorno (versiones de numpy y scikit-learn, sistema operativo, hilos). Fijar la semilla es una condición para reproducir un modelo, pero no la única.

## Ejemplo

Una prueba con datos generados al azar falla una de cada diez ejecuciones. Con la semilla impresa en el informe de la ejecución fallida, se vuelve a lanzar con `--semilla 12345` y falla siempre, lo que permite depurarla. Sin la semilla, el fallo habría parecido intermitente e inexplicable. Procedimiento de [SE-428](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md).

## Errores y confusiones comunes

- **Una prueba falla una vez de cada diez**: datos aleatorios sin semilla o propiedad mal enunciada; se corrige registrando la semilla y revisando la propiedad.
- **Fijar una semilla en el código y olvidarla**: se pierde la exploración de casos nuevos.
- **Creer que la semilla basta para reproducir un entrenamiento**: también cuentan los datos, la configuración y el entorno.
- **Mezclar sentidos**: la semilla de un generador no es el dato inicial de un cliente.

## Límites y cuándo no aplica

Una semilla garantiza repetir la secuencia solo si el resto del programa es determinista: relojes, orden de hilos y orden de iteración de conjuntos pueden seguir introduciendo variación. Un generador pseudoaleatorio no sirve para fines criptográficos. Y reproducir un fallo con la semilla no explica su causa: solo permite estudiarlo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Generador](../g/generador.md), [Secuencia](./secuencia.md), [Valor](../v/valor.md), [Aprovisionamiento](../a/aprovisionamiento.md), [Compensación](../c/compensacion.md), [Configuración por capas](../c/configuracion-por-capas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-428 — Datos deterministas y gestión de fixtures](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-428-datos-deterministas-y-gestion-de-fixtures/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (451 clases más lo mencionan; las que más):

[SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md), [SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md), [SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md), [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Documentación del módulo random](https://docs.python.org/3/library/random.html) — semillas y límites; autoridad: documentación oficial de Python.
- [Martin Fowler, «Eradicating Non-Determinism in Tests»](https://martinfowler.com/articles/nonDeterminism.html) — causas del no determinismo; autoridad: autor del texto.
- [pytest: cómo usar fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) — ámbitos y limpieza; autoridad: documentación oficial de pytest.
- [SQLite: transacciones](https://www.sqlite.org/lang_transaction.html) — `BEGIN` y `ROLLBACK`; autoridad: documentación oficial de SQLite.
- [Martin Fowler, «ObjectMother»](https://martinfowler.com/bliki/ObjectMother.html) — fábricas de datos de prueba; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Semiabierto](./semiabierto.md) · [Semver →](./semver.md)
