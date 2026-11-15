# Parte 28 — Concurrencia y sistemas distribuidos

La Parte 27 dejó servicios que se hablan por mensajes y toleran reintentos. La pregunta cambia de «cómo se conectan» a «qué sabe cada participante cuando muchas cosas ocurren a la vez, el reloj no coincide y una respuesta no llega». Esta parte trabaja sobre **el servicio de entregas de la plataforma en el cierre de plazo**, un caso sintético: cientos de estudiantes entregan en los últimos minutos, un contador y un cupo se actualizan desde varios procesos, una réplica se aísla de la red y una dependencia falla de forma intermitente. El servicio debe seguir siendo correcto, rápido y diagnosticable, y quien lo opera debe poder decir qué promete cuando algo falla.

## Pregunta rectora

> ¿Qué puede conocer cada participante de un sistema concurrente o distribuido, qué propiedad se mantiene cuando algo falla y qué evidencia lo demuestra?

## Antes del recorrido clase por clase

Esta parte no enseña un lenguaje de programación concurrente, un sistema de actores ni un producto de coordinación. Enseña a distinguir lo que dos tareas comparten de lo que se envían, a enumerar las intercalaciones que rompen una invariante, a decidir qué reloj usar para medir, mostrar y ordenar, a leer un tiempo agotado como un resultado desconocido y no como un error, a elegir por operación qué se rechaza y qué se reconcilia durante una partición, a exigir mayorías y testigos de cerco donde solo puede haber un titular, a hacer repetible cada efecto, a repartir y replicar con una métrica de cola larga, a probar con fallos acotados y semillas guardadas, y a declarar qué garantías ofrece un servicio y cuáles no.

```mermaid
flowchart LR
    A[Concurrencia, paralelismo y asincronía] --> B[Memoria compartida y cerrojos]
    B --> C[Actores, canales y concurrencia estructurada]
    C --> D[Tiempo, relojes y orden parcial]
    D --> E[Fallos parciales y modelos de red]
    E --> F[Consistencia, disponibilidad y particiones]
    F --> G[Consenso, elección y coordinación]
    G --> H[Idempotencia y procesamiento distribuido]
    H --> I[Replicación, sharding y balanceo]
    I --> J[Caos controlado y pruebas de distribución]
    J --> K[Taller: reproducir una carrera y un fallo parcial]
    K --> L[Proyecto: servicio distribuido con degradación]
    L -->|incidente o hallazgo| A
```

El diagrama se lee de izquierda a derecha y no es un proceso obligatorio. El retorno indica que un incidente, un fallo reproducido o un cambio en la carga reabre el diseño; un paquete aprobado no cierra la discusión, la fecha.

## Resultados acumulativos

Podrás clasificar el trabajo de un servicio en espera y cálculo y elegir entre asincronía, hilos y procesos con un modelo de tiempo y con el límite de Amdahl; enumerar las intercalaciones de un contador compartido, medir cuántas dejan un valor correcto, reproducir un interbloqueo por orden de cerrojos y ver cuánto trabajo avanza según la granularidad; comparar el orden que garantiza un buzón, el efecto de una cola sin límite y el de una acotada y lo que deja un grupo de tareas frente a tareas sueltas ante un fallo o una cancelación; distinguir relojes de pared, monotónicos, de Lamport y vectoriales y medir desde qué desfase una regla de último escritor pierde escrituras; repartir un tiempo agotado entre sus tres historias, calcular la amplificación de los reintentos y elegir el límite de un detector de fallos; decidir por operación entre rechazar y aceptar durante una partición, calcular un cuórum y comparar una reparación por último escritor con tipos fusionables; mostrar por qué la mayoría impide dos líderes, medir el daño de un titular caducado con y sin testigo de cerco y ajustar plazos de elección; comparar semánticas de entrega, retención de claves de idempotencia y escritura por clave en un trabajo distribuido; comparar políticas de balanceo con cola pesada, la pérdida al conmutar según el modo de replicación y el reparto por hash o por rango; diseñar un experimento de caos y explorar intercalaciones con semillas; y reproducir, reducir y blindar una carrera y un fallo parcial.

Al finalizar podrás defender un servicio distribuido con garantías declaradas por operación, presupuestos de tiempo y de reintentos, una escalera de degradación, protección ante la sobrecarga, una prueba por promesa y una lista de lo que ninguna prueba ni validador ve, y podrás indicar qué parte de tu conclusión es observación, cuál es inferencia y cuál es suposición.

## Prerrequisitos enlazados

- [Parte 4 — Pensamiento computacional](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/): modelado, enumeración de casos y razonamiento sobre evidencia.
- [Parte 7 — Estructuras de datos y algoritmos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/): colas, costos y estructuras de búsqueda.
- [Parte 20 — Backend, APIs y procesamiento asíncrono](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-20-backend-apis-y-procesamiento-asincrono/): idempotencia, reintentos y consistencia en el servidor.
- [Parte 26 — Datos, persistencia y recuperación](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-26-datos-persistencia-y-recuperacion/): transacciones, intercalaciones, replicación y cachés.
- [Parte 27 — Integración, eventos y mensajería](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-27-integracion-eventos-y-mensajeria/): mensajes, reintentos y flujos tolerantes a fallos.
- Python 3.11+ y terminal; los experimentos usan solo la biblioteca estándar (incluidos `asyncio`, `threading` y `sqlite3`) y datos o modelos sintéticos.

## Bloques y progresión

1. **Concurrencia dentro de un proceso:** las clases 337 a 339 separan concurrencia, paralelismo y asincronía, enumeran las intercalaciones de un dato compartido y sustituyen el estado compartido por mensajes con buzones acotados y tareas atadas a un bloque.
2. **Tiempo, fallos y garantías:** las clases 340 a 342 miden qué orden inventa cada reloj, qué significa un silencio y qué se rechaza o se reconcilia durante una partición.
3. **Acuerdo y repetición:** las clases 343 y 344 exigen mayorías y testigos de cerco donde solo cabe un titular y hacen que cada efecto sea repetible.
4. **Reparto y evidencia:** las clases 345 y 346 miden balanceo, replicación y reparto y prueban con fallos acotados y planificadores con semilla.
5. **Aplicar e integrar:** las clases 347 y 348 reproducen una carrera y un fallo parcial hasta un caso mínimo y entregan un servicio con degradación declarada.

## Evidencia medida y límites

Las figuras y los ejemplos de esta parte usan experimentos y modelos ejecutados con CPython 3.12.9 en Windows 11 y repetidos con CPython 3.12.3 en Ubuntu bajo WSL2. No se midió ningún servicio, red, base de datos distribuida, cola de mensajes ni equipo real: los datos son **sintéticos**, las semillas están fijadas y los parámetros son supuestos del autor. Las salidas de los doce experimentos fueron idénticas en ambos sistemas en todas las cifras salvo dos excepciones propias del entorno, no del método: la resolución de los relojes de Python (15,6 ms en Windows y 1 ns en Ubuntu, `SE-340`) y el resultado de una versión real con dos hilos, dos cerrojos y un tiempo límite, que depende de la temporización (en Windows ambos hilos agotaron el tiempo y en Ubuntu uno completó, `SE-338`).

Los experimentos son: la comparación de un planificador en tiempo virtual entre ejecución secuencial, concurrente y paralela, los latidos que emite un bucle de eventos de `asyncio` según cada cuánto cede un cálculo y la tabla de la ley de Amdahl (`SE-337`); las 70 intercalaciones de un contador con y sin cerrojo (y cuatro hilos reales que no mostraron la carrera en tres ejecuciones), el modelo exhaustivo de dos hilos y dos cerrojos y la fracción de trabajo que avanza con tres granularidades de cerrojo (`SE-338`); el orden que conserva un buzón de `asyncio` en 2 000 ejecuciones, una cola sin límite y dos acotadas frente a un productor tres veces más rápido, y `TaskGroup` frente a `gather` y la cancelación de una transferencia de cuatro pasos con y sin escudo (`SE-339`); relojes de Lamport y vectoriales sobre 300 sucesos de tres nodos, la pérdida de escrituras por desfase con la regla del último escritor y la resolución y el retroceso de los relojes de Python (`SE-340`); la proporción de tiempos agotados que corresponden a una operación ejecutada, la amplificación de reintentos con presupuesto y jitter y un detector de fallos con cinco tiempos límite (`SE-341`); una partición de 300 de 1 000 operaciones con rechazo o aceptación, la enumeración de cuórums de tres réplicas y una reparación con último escritor frente a un contador por réplica y una unión de conjuntos (`SE-342`); las biparticiones de cinco nodos con una regla ingenua y con mayoría, titulares caducados con y sin testigo de cerco y una elección con plazos aleatorios (`SE-343`); tres órdenes de aplicar y confirmar sobre SQLite real, una tabla de claves con huella y retención, y un trabajo de 200 tareas con anexión o escritura por clave (`SE-344`); cuatro políticas de balanceo con tamaños de cola pesada, la pérdida al conmutar con tres modos de replicación y el reparto por hash o por rango (`SE-345`); un cliente con reintentos e interruptor frente a un fallo creciente, cuatro planificadores que exploran un defecto de concurrencia y un linter de planes de caos sobre 200 mutaciones (`SE-346`); la reducción de un calendario fallido de 40 pasos a 6, la enumeración de puntos de fallo de un flujo de cinco pasos y las repeticiones necesarias para ver un fallo raro (`SE-347`); y una caída de la base con tres estrategias, una sobrecarga del 50 % con tres políticas y un validador de paquete sobre 200 mutaciones (`SE-348`).

Los parámetros (las 200 solicitudes de 10 ms de CPU y 90 de espera, el 5 % de serie de Amdahl, los 8 trabajadores con claves Zipf 1,1, los tres emisores con retardos de 0 a 3 turnos, la tasa de 3 mensajes por turno frente a 1, los desfases de ±50 a ±1 000 ms, el ajuste de reloj de −80 ms, las probabilidades de pérdida y de lentitud, la distribución lognormal del retardo, la partición de 300 de 1 000 operaciones, las pausas exponenciales de media 4 s, los retardos de mensajes de hasta 25 ms, la caída del 5 % del consumidor, la carga del 85 % con tamaños Pareto de forma 1,5, el retraso de réplica de 30 ms, los ocho fragmentos, la capacidad de 100, los 4,84 % del planificador pegajoso, la caída de 60 s y la sobrecarga de 150 contra 100) son construcciones del autor y no se extrapolan a otros sistemas, cargas ni redes. Los verificadores de forma (el linter de planes de caos y el validador de paquetes) se escribieron conociendo las mutaciones, de modo que cada tipo sale al 0 % o al 100 % y su exactitud real sobre material de personas es desconocida. No se evaluó ningún producto concreto, no se ejecutó Raft ni Paxos, y no se mide el costo de operar nada de lo descrito.

## Guía razonada clase por clase

El servicio de entregas mantiene un contador, un cupo, una réplica y una dependencia estables mientras cambian las decisiones. Cada clase explica qué incertidumbre reduce, qué experimento la muestra, qué no demuestra y qué evidencia permite abandonar la conclusión.

### Bloque 1 — Concurrencia dentro de un proceso

#### SE-337 — Concurrencia, paralelismo y asincronía

Elegir mal entre solapar esperas y repartir cálculo significa pagar complejidad sin ganar tiempo. La clase compara cuatro modelos de ejecución de un mismo lote con tres proporciones de espera y cálculo, cuenta cuántos latidos alcanza a emitir un servicio mientras otra tarea calcula sin ceder y calcula cuántos trabajadores justifica una parte secuencial.

El estudiante entrega una clasificación de tareas en espera y cálculo con una regla de decisión. `SE-338` pregunta qué ocurre cuando dos de esas tareas tocan el mismo dato.

#### SE-338 — Memoria compartida, locks y condiciones de carrera

Un cerrojo resuelve la carrera a cambio de dos problemas nuevos. La clase enumera las 70 intercalaciones de un contador, explora el interbloqueo de dos hilos con orden opuesto y mide cuánto trabajo avanza con un cerrojo global, por fragmentos y por curso con claves uniformes y con popularidad concentrada.

El estudiante entrega un orden global de adquisición y la clasificación de cada dato compartido. `SE-339` propone evitar el problema pasando mensajes.

#### SE-339 — Actores, canales y structured concurrency

Un dueño único y un buzón sustituyen al estado compartido, pero el orden global no existe y una cola sin límite solo traslada el problema a la memoria. La clase cuenta los órdenes de tres emisores, compara colas sin límite y acotadas ante un productor más rápido y observa qué dejan un grupo de tareas y tareas sueltas ante un error y una cancelación.

El estudiante entrega el diseño de un actor con buzón acotado y operaciones cancelables clasificadas. `SE-340` pregunta cómo ordenar sucesos sin reloj común.

### Bloque 2 — Tiempo, fallos y garantías

#### SE-340 — Tiempo, relojes y orden parcial

La hora no es un orden. La clase mide cuántos pares de sucesos son concurrentes y cuántos de ellos ordena un reloj de Lamport de forma aparente, calcula desde qué desfase una regla de último escritor pierde escrituras posteriores y compara la resolución y los retrocesos de los relojes de dos sistemas operativos.

El estudiante entrega la decisión de reloj por uso y la política ante vectores incomparables. `SE-341` pregunta qué se sabe cuando una respuesta no llega.

#### SE-341 — Fallos parciales y modelos de red

Un tiempo agotado es un resultado desconocido. La clase reparte los silencios entre petición perdida, respuesta perdida y respuesta tardía, calcula cuántos intentos recibe el servicio final cuando varias capas reintentan y mide las falsas sospechas y el retraso de un detector con cinco tiempos límite.

El estudiante entrega un modelo de fallos, una política de reintentos y el límite de un detector justificado. `SE-342` pregunta qué se mantiene cuando la red se parte.

#### SE-342 — Consistencia, disponibilidad y particiones

La elección entre consistencia y disponibilidad se hace por operación y mientras dura la partición. La clase compara rechazar y aceptar con una réplica aislada, enumera los cuórums de tres réplicas con su disponibilidad y compara una reparación por último escritor con tipos que se fusionan.

El estudiante entrega la decisión por operación y el cuórum por dato. `SE-343` pregunta cómo se ponen de acuerdo los nodos cuando no cabe divergir.

### Bloque 3 — Acuerdo y repetición

#### SE-343 — Consenso, elección y coordinación

La mayoría impide dos líderes y el testigo de cerco impide que un titular caducado escriba. La clase enumera las biparticiones de cinco nodos con dos reglas, mide cuántas escrituras de un titular pausado acepta un almacén con y sin cerco y ajusta los plazos de una elección aleatoria.

El estudiante entrega la clasificación de funciones con titular único y el cerco por recurso. `SE-344` hace repetible lo que aun así se ejecuta dos veces.

#### SE-344 — Idempotencia y procesamiento distribuido

No hay exactamente una vez entre sistemas; hay efecto único. La clase compara tres órdenes de aplicar y confirmar sobre SQLite, mide cuántos duplicados escapan a una clave según su retención y compara anexar con escribir por clave en un trabajo con reintentos.

El estudiante entrega la clasificación de operaciones y la retención de claves justificada. `SE-345` reparte el trabajo ya repetible.

### Bloque 4 — Reparto y evidencia

#### SE-345 — Replicación, sharding y balanceo

Igualar solicitudes no iguala trabajo y confirmar antes de replicar cuesta escrituras. La clase compara cuatro políticas de balanceo con cola pesada, mide la pérdida al conmutar con tres modos de replicación y cuenta dónde caen las escrituras y cuántos fragmentos toca una consulta con hash y con rango.

El estudiante entrega la política de balanceo, el RPO por dato y la clave de reparto con su consulta cara. `SE-346` comprueba que todo esto resiste fallos.

#### SE-346 — Caos controlado y pruebas de distribución

Una suite verde no demuestra resistencia a fallos. La clase mide el éxito y las llamadas de tres estrategias de cliente ante un fallo creciente, cuenta cuántas ejecuciones expone un defecto según el planificador y evalúa un linter de planes de caos sobre 200 mutaciones.

El estudiante entrega un plan de experimento completo y una estrategia de exploración con semillas. `SE-347` reproduce los fallos hasta lo esencial.

### Bloque 5 — Aplicar e integrar

#### SE-347 — Taller: reproducir una carrera y un fallo parcial

Un fallo que no se reproduce no se corrige. El taller enumera las intercalaciones de un cupo, reduce un calendario de 40 pasos a 6, separa corte y respuesta perdida en un flujo de cinco pasos y calcula cuántas repeticiones hacen falta para ver un fallo raro.

El estudiante entrega un reproductor mínimo con una regresión que falla antes y pasa después. `SE-348` lo integra en un servicio.

#### SE-348 — Proyecto: servicio distribuido con degradación

Un paquete completo no es un paquete correcto. El proyecto compara tres estrategias ante una caída de la base, tres políticas ante una sobrecarga del 50 % y mide qué detecta un validador de forma sobre 200 mutaciones de un paquete.

El estudiante entrega un paquete de servicio con garantías, presupuestos, escalera de degradación, protección ante sobrecarga, pruebas por promesa y `LIMITES.md`. La Parte 29 lleva ese servicio a una plataforma de nube.

## Fuentes

- [Lamport, «Time, clocks, and the ordering of events in a distributed system»](https://doi.org/10.1145/359545.359563) — orden parcial y relojes lógicos; autoridad: artículo original.
- [Fischer, Lynch y Paterson, «Impossibility of distributed consensus with one faulty process»](https://doi.org/10.1145/3149.214121) — límite del consenso asíncrono; autoridad: artículo original.
- [Gilbert y Lynch, «Brewer's conjecture…»](https://doi.org/10.1145/564585.564601) y [Brewer, «CAP twelve years later»](https://doi.org/10.1109/MC.2012.37) — compromiso entre consistencia y disponibilidad; autoridad: artículos de los autores.
- [Ongaro y Ousterhout, Raft](https://raft.github.io/raft.pdf) y [Lamport, «The part-time parliament»](https://doi.org/10.1145/279227.279229) — consenso con mayorías; autoridad: artículos originales.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — modelos de fallo, consistencia y procesamiento; autoridad: autor del libro.
- [Jepsen](https://jepsen.io/) — pruebas de sistemas distribuidos con inyección de fallos; autoridad: Jepsen.
- [Python: asyncio](https://docs.python.org/3/library/asyncio.html) y [threading](https://docs.python.org/3/library/threading.html) — herramientas usadas en los experimentos; autoridad: documentación de Python.
- [Principios de la ingeniería del caos](https://principlesofchaos.org/) y [Google SRE: manejo de sobrecarga](https://sre.google/sre-book/handling-overload/) — experimentos acotados y protección del servicio; autoridad: autores del manifiesto y Google.
- [Amdahl (1967)](https://doi.org/10.1145/1465482.1465560) y [Little (1961)](https://doi.org/10.1287/opre.9.3.383) — límites de aceleración y relación entre cola y espera; autoridad: artículos originales.

Las fuentes se vinculan también dentro de cada clase. Definen vocabulario y mecanismos; la adecuación de las decisiones del servicio se demuestra con el caso, la evidencia trazable y la revisión de otra persona, no con la autoridad de la fuente.

## Criterios de aceptación de la parte

- cada clase conecta mecanismo, medida y límite en una conclusión revisable;
- cada medida puede reproducirse desde un checkout limpio con las mismas semillas;
- ninguna afirmación sobre una red, un producto o personas reales se apoya en una simulación;
- los límites declarados permiten a otra persona decidir qué comprobar antes de confiar.

[Volver al índice de clases](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md)
