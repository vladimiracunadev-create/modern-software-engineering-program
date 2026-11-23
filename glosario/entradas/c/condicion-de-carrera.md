# Condición de carrera

[↑ Glosario](../../README.md) · [← Condición de aborto](./condicion-de-aborto.md) · [Condición de fallo →](./condicion-de-fallo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Una **condición de carrera** es una situación en que el resultado depende del orden en que se intercalan operaciones concurrentes cuyo orden no está controlado. Las clases lo formulan igual en contextos distintos: [SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) y [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) en programas con varios hilos, [SE-418](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md) en un carrito y un inventario con operaciones simultáneas y [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md) en un sistema crítico, donde el orden relativo de eventos que no se controla lleva a un estado inconsistente. El sentido que usa el programa es la dependencia del **orden relativo**, no la mera existencia de concurrencia.

## Por qué importa

Es un defecto que solo aparece a veces: el mismo código puede pasar cien pruebas y fallar en producción. [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) extrae la consecuencia práctica: «lo corrí cien veces y pasó» no demuestra nada. En sistemas críticos el costo es mayor: [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md) analiza un caso en que una edición durante una ventana del proceso dejó parámetros inconsistentes en un equipo médico.

## Cómo funciona

Una carrera ocurre cuando dos o más actores leen y escriben un estado compartido sin una regla que ordene sus pasos. El ejemplo de [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md): dos hilos incrementan un contador en dos pasos (leer, escribir). Hay seis intercalaciones posibles de los pasos, y solo dos terminan bien (33,3 %); con tres hilos, 6 de 90 (6,7 %). La causa de que sea tan difícil detectarla ejecutando es que el sistema real **no recorre todas las intercalaciones**: el intérprete cede el control en puntos concretos, y un código más corto o una versión distinta cambia la proporción de fallos de 0 % a 100 %.

De ahí dos consecuencias metodológicas. Primero, lo que demuestra la presencia o ausencia de la carrera es **enumerar** las intercalaciones o usar una herramienta que las fuerce, no repetir ejecuciones. Segundo, la defensa no es «tener más suerte» sino imponer orden o atomicidad: exclusión mutua, operaciones atómicas, restricciones únicas o transacciones, según dónde viva el estado.

## Ejemplo

[SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md) modela una carrera real documentada: la edición del operador ocurre dentro de una ventana de 8 segundos del ajuste de imanes, después de que la rutina de espera comprobó por última vez si había cambios, y los parámetros quedan inconsistentes. En el modelo del laboratorio, con 100 000 tratamientos, una probabilidad de edición del 15 % (supuesto) y el instante de edición uniforme en los primeros 20 segundos, hay 5 705 inconsistencias en la variante original; con una ventana de 2 segundos son 1 129 y con 12 segundos, 8 611. El riesgo crece casi en proporción a la ventana durante la cual una edición no se vuelve a comprobar. Es un modelo con supuestos declarados, no una reconstrucción del suceso.

## Errores y confusiones comunes

- **Creer que pasar muchas pruebas descarta la carrera.** Las ejecuciones reales visitan pocas intercalaciones ([SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md)).
- **Comprobar y luego actuar en el código de la aplicación.** Comprobar «¿existe?» y después insertar deja una ventana; la restricción única de la base de datos la cierra ([SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) lo desarrolla para idempotencia).

## Límites y cuándo no aplica

Las cifras de [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) y [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md) salen de modelos y de supuestos declarados, de modo que fijan el método de razonamiento, no la frecuencia real de las carreras en un sistema concreto. Eliminar una carrera concreta no elimina la clase: [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md) insiste en que lo decisivo es cambiar el diseño para que no exista la ventana, no estrecharla.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Operación](../o/operacion.md), [Resultado](../r/resultado.md), [Actualización condicional atómica](../a/actualizacion-condicional-atomica.md), [Captura](./captura.md), [Contrapresión](./contrapresion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-418 — Comercio electrónico: carrito, inventario, pagos y devoluciones](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-455 — Taller: analizar un fallo real frente a las normas](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), [SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md), [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md), [SE-098](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md), [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Condiciones de carrera».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Luo et al., «An empirical analysis of flaky tests»](https://doi.org/10.1145/2635868.2635920) — causas de las pruebas inestables; autoridad: artículo revisado de FSE 2014.
- [Lam et al., «iDFlakies»](https://doi.org/10.1109/ICST.2019.00038) — detección de pruebas inestables; autoridad: artículo revisado de ICST 2019.
- [Google Testing Blog: Flaky Tests at Google and How We Mitigate Them](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html) — mitigación en una organización; autoridad: equipo de pruebas de Google.
- [Micco, «The State of Continuous Integration Testing @Google»](https://research.google/pubs/the-state-of-continuous-integration-testing-google/) — integración continua a gran escala; autoridad: Google Research.
- [Martin Fowler, «Eradicating Non-Determinism in Tests»](https://martinfowler.com/articles/nonDeterminism.html) — causas y tratamiento; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Condición de aborto](./condicion-de-aborto.md) · [Condición de fallo →](./condicion-de-fallo.md)
