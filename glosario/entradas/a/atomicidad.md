# Atomicidad

[↑ Glosario](../../README.md) · [← Atestación](./atestacion.md) · [Atribución de costos →](./atribucion-de-costos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

La **atomicidad** es la propiedad de una operación que se confirma completa o no deja efectos, y que ningún otro contexto observa a medias. Las clases la presentan en dos escalas del mismo hecho: [SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md) y [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) como «se confirma completa o no deja efectos» (el punto de vista de quien ejecuta, típico de una transacción de base de datos y de la unidad de trabajo) y [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) como «ningún otro contexto observa la operación a medias» (el punto de vista de quien observa, típico de interrupciones, hilos y estado compartido). No es sinónimo de rapidez ni de «una sola línea de código»: es la garantía de todo o nada.

## Por qué importa

Un proceso puede detenerse en cualquier instante: por un corte de energía, un error o una orden de terminación. Sin atomicidad, el estado queda a medio camino y nadie lo avisa. [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) lo ilustra con una transferencia de cupos de cuatro pasos (registrar, descontar, sumar, cerrar) cortada en el tercero: el sistema queda con 55 cupos en lugar de 60. Lo grave es que el sistema sigue funcionando con un estado inválido.

## Cómo funciona

Una transacción agrupa varias sentencias de modo que, si falla cualquiera, ninguna deja huella ([SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md)). La causa de que no dependa de la velocidad es que un corte puede llegar en cualquier punto, por rápida que sea la secuencia: lo que se necesita es un mecanismo que permita deshacer o descartar lo hecho a medias. En una base de datos, ese mecanismo es la transacción con confirmación y reversión; en SQLite y PostgreSQL abarca también las sentencias de definición de esquema ([SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md)), pero en otros motores no.

En estado compartido, [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) explica por qué una línea no es atómica: `contador++` se traduce en leer el valor, sumar uno y escribirlo. Si una interrupción incrementa el mismo contador entre la lectura y la escritura, el programa principal escribe el valor viejo más uno y borra el incremento de la interrupción. De las diez posiciones posibles de una interrupción dentro de una vuelta de diez instrucciones, solo las dos situadas entre la lectura y la escritura pierden el incremento, y por eso una prueba corta rara vez lo ve. Se corrige enmascarando las interrupciones durante esas instrucciones, con una operación atómica del procesador o con un diseño donde solo un contexto escribe.

## Ejemplo

El caso de [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md): una transferencia de cupos en cuatro pasos (registrar, descontar, sumar, cerrar). Sin transacción, si el proceso se corta en el tercer paso, el sistema queda con 55 cupos en lugar de 60 y nadie lo avisa. Con los cuatro pasos dentro de una transacción, o se aplican los cuatro o ninguno, y el total permanece en 60. Son números del experimento de la clase.

## Errores y confusiones comunes

- **Creer que una secuencia rápida es atómica.** La atomicidad no depende de la velocidad: un corte puede llegar en cualquier punto ([SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md)).
- **Creer que una línea de código es atómica.** `contador++` son tres instrucciones; una interrupción entre la lectura y la escritura pierde el incremento ([SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md)).
- **Confundir atomicidad con idempotencia.** La primera garantiza todo o nada en una ejecución; la segunda, que repetir no cambie el efecto. [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) pide distinguir qué parte del diseño dependía de cada una.
- **Suponer que todo motor trata igual el esquema.** En SQLite y PostgreSQL las sentencias de definición de esquema forman parte de la transacción; en otros motores no ([SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md)).

## Límites y cuándo no aplica

La atomicidad vale dentro de un límite: una transacción local no cubre un proceso que cruza varios servicios, donde se usan compensaciones (véase saga, [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md)). Tampoco cubre efectos externos que ya ocurrieron, como un correo enviado, que ninguna reversión de base de datos deshace. Y es solo una de las propiedades de una transacción: aislamiento y consistencia son otras, que [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) y [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md) tratan aparte.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Efecto](../e/efecto.md), [Operación](../o/operacion.md), [Propiedad](../p/propiedad.md), [Active Record](./active-record.md), [Búfer circular](../b/bufer-circular.md).
- **Se confunde con:** El mapa separa dos preguntas que se confunden: si los cambios de una operación se aplican enteros (atomicidad) y qué ven las demás mientras tanto (aislamiento).

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (19 clases más lo mencionan; las que más):

[SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), [SE-113](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-113-cli-flags-configuracion-y-codigos-de-salida/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md), [SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md), [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md), [SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [PostgreSQL: aislamiento de transacciones](https://www.postgresql.org/docs/current/transaction-iso.html) — niveles y anomalías; autoridad: documentación oficial de PostgreSQL.
- [SQLite: aislamiento](https://www.sqlite.org/isolation.html) — comportamiento entre conexiones; autoridad: documentación oficial de SQLite.
- [SQLite: transacciones](https://www.sqlite.org/lang_transaction.html) — `BEGIN` diferido e inmediato; autoridad: documentación oficial de SQLite.
- [Berenson et al., «A Critique of ANSI SQL Isolation Levels»](https://arxiv.org/abs/cs/0701157) — anomalías no cubiertas por el estándar; autoridad: artículo de los autores.
- [Cahill, Röhm y Fekete (2008)](https://dl.acm.org/doi/10.1145/1376616.1376690) — serializabilidad sobre instantáneas; autoridad: artículo original.

---

[↑ Glosario](../../README.md) · [← Atestación](./atestacion.md) · [Atribución de costos →](./atribucion-de-costos.md)
