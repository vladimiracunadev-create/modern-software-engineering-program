# Parte 31 — Calidad, rendimiento y resiliencia

La Parte 30 decidió qué pruebas ejecutar según el riesgo y cómo demostrar que una prueba detecta defectos. La pregunta cambia de «¿esta prueba ve el defecto?» a «¿qué promesa de calidad hace el sistema, con qué medida, y qué ocurre cuando se le somete a presión?». Esta parte trabaja sobre **la API de entregas de la plataforma educativa**, un caso sintético: subir una entrega, listar las entregas de un curso y consultar una calificación, con picos de uso en los cierres de plazo. Cada clase convierte una palabra vaga (rápido, fiable, compatible, usable) en una medida, mide cómo se engaña quien la usa mal y declara qué no demuestra.

## Pregunta rectora

> ¿Qué promesa de calidad se puede hacer, con qué medida y qué evidencia reproducible permite a otra persona comprobarla, refutarla o decir cuándo deja de valer?

## Antes del recorrido clase por clase

Esta parte no enseña una herramienta de pruebas de carga ni un producto de observabilidad. Enseña a escribir un requisito de calidad como un escenario con una medida, a ver qué esconde cada estadístico y cada ventana, a decidir qué comprueba una revisión, un análisis estático y una compuerta y qué se les escapa, a elegir la forma de una prueba de carga y a distinguir un generador que oculta la espera de uno que no, a explicar con teoría de colas por qué la latencia se dispara cerca de la saturación y a planificar la capacidad desde un objetivo de cola, a medir con relojes y perfiladores sin creer que miden lo que no miden, a decidir timeouts y reintentos con presupuesto, a limitar el daño de una dependencia caída con interruptores, mamparos y respuestas degradadas, a calcular disponibilidad y durabilidad con la causa común a la vista, a comprobar la compatibilidad entre sistemas y versiones ejecutándola, a fijar presupuestos de experiencia con dueño y a someter un sistema a presión con una hipótesis, un radio acotado y un criterio de aborto. Cada clase ejecuta experimentos con datos sintéticos o sondas reales que muestran un mecanismo (una media de 157 ms sobre un p99 de 1 929 ms, un p99 de 232 ms que oculta una pausa de diez segundos, tres capas que envían 27 intentos a una base caída, siete de doce sondas que lanzan una excepción en un sistema y no en otro) y declara lo que esa medida no demuestra.

```mermaid
flowchart LR
    A[Modelos de calidad y atributos medibles] --> B[Revisión, análisis estático y quality gates]
    B --> C[Carga, estrés, picos y endurance]
    C --> D[Latencia, throughput, saturación y capacidad]
    D --> E[Perfiles, benchmarks y errores de medición]
    E --> F[Timeouts, retries, backoff y jitter]
    F --> G[Circuit breakers, bulkheads y degradación]
    G --> H[Disponibilidad, durabilidad y recuperación]
    H --> I[Compatibilidad, portabilidad e interoperabilidad]
    I --> J[Calidad de experiencia y presupuestos]
    J --> K[Taller de presión controlada]
    K --> L[Informe reproducible de calidad]
    L -->|incidente o hallazgo| A
```

El diagrama se lee de izquierda a derecha y no es un proceso obligatorio. El retorno indica que un incidente, un hallazgo del ensayo de presión o una queja de una persona usuaria reabre los escenarios de calidad; un informe aprobado no cierra la calidad, la fecha.

## Resultados acumulativos

Podrás escribir un requisito de calidad como un escenario de seis partes y comprobar con un verificador de forma qué detecta y qué deja pasar; calcular la media, la mediana y los percentiles de una misma muestra y aplicar varias definiciones del mismo objetivo a una ventana para ver cuál oculta un incidente; escribir reglas de análisis estático con `ast`, medir su precisión y sus defectos no vistos, comparar una compuerta de cobertura total con una del cambio y contar los bloqueos espurios al encadenar comprobaciones; elegir entre carga, estrés, pico y resistencia por la pregunta que cada una responde, medir el colapso por trabajo para clientes ausentes y la omisión coordinada de un generador cerrado; explicar con la fórmula de una cola por qué la espera crece como 1/(1 − utilización), cuánto añade la variabilidad del servicio, por qué no se promedian percentiles y cuántos servidores exige un objetivo de p99;

medir la variación de una misma función entre procesos, el efecto de un perfilador y de una caché sobre un benchmark y la tasa de falsas diferencias entre dos copias idénticas; comparar políticas de reintento tras una degradación y una oleada, calcular la amplificación por capas y elegir un timeout con la distribución de latencias; medir qué evita un interruptor, qué confina un mamparo y qué respuesta útil produce cada política de sobrecarga; calcular disponibilidad en serie y en paralelo con y sin causa común, la pérdida de datos según el tiempo de reparación y el umbral de un detector de fallos; ejecutar sondas de portabilidad en dos sistemas, medir datos que cambian de significado al cruzar una frontera y construir una matriz de compatibilidad de versiones; comparar el laboratorio con el campo, tres compuertas ante una deriva de peso y el contraste de los colores del propio repositorio; fijar umbrales de estado estable, inyectar cuatro fallos sobre una referencia y una variante endurecida y calcular la detección frente al radio de impacto; y validar un paquete de informe, medir qué artefactos se reproducen entre sistemas y estimar cuántos informes declararían una mejora falsa según cómo se elija el resultado.

Al finalizar podrás defender un informe de calidad con su plan fijado de antemano, sus datos crudos con huella, sus escenarios medibles, sus políticas de resiliencia, sus presupuestos, su ensayo de presión y una lista de lo que ninguna medición ni validador ve, y podrás indicar qué parte de tu conclusión es observación, cuál es inferencia y cuál es suposición.

## Prerrequisitos enlazados

- [Parte 4 — Pensamiento computacional](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/): modelado, enumeración de casos y razonamiento sobre evidencia.
- [Parte 7 — Estructuras de datos y algoritmos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/): costo de las operaciones, colas y montículos.
- [Parte 13 — Especificaciones, contratos y modelos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-13-especificaciones-contratos-y-modelos/): contratos comprobables y compatibilidad entre versiones.
- [Parte 20 — Backend, APIs y procesamiento asíncrono](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-20-backend-apis-y-procesamiento-asincrono/): idempotencia, reintentos y consistencia en el servidor.
- [Parte 25 — Arquitectura de software y dominio](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-25-arquitectura-de-software-y-dominio/): atributos de calidad, fronteras y decisiones registradas.
- [Parte 26 — Datos, persistencia y recuperación](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-26-datos-persistencia-y-recuperacion/): copias, restauración y réplicas.
- [Parte 30 — Estrategia y técnicas de prueba](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-30-estrategia-y-tecnicas-de-prueba/): riesgo, pruebas y capacidad de detección.
- Python 3.11+ y terminal; los experimentos usan solo la biblioteca estándar y datos sintéticos, salvo las sondas de portabilidad y las mediciones de tiempo, que son lecturas reales del equipo.

## Bloques y progresión

1. **Definir y vigilar la calidad:** las clases 373 y 374 convierten una promesa en un escenario con medida y deciden qué comprueban la revisión, el análisis estático y las compuertas.
2. **Medir bajo carga:** las clases 375 a 377 eligen la forma de la prueba de carga, explican la latencia con teoría de colas y miden con relojes sin engañarse.
3. **Resistir el fallo:** las clases 378 a 380 deciden timeouts, reintentos, interruptores, mamparos, degradación, disponibilidad y recuperación.
4. **Compatibilidad y experiencia:** las clases 381 y 382 miden diferencias entre sistemas y versiones y fijan presupuestos de experiencia.
5. **Aplicar e integrar:** las clases 383 y 384 someten el sistema a presión controlada y entregan un informe reproducible de calidad.

## Evidencia medida y límites

Las figuras y los ejemplos de esta parte usan experimentos ejecutados con CPython 3.12.9 en Windows 11 y repetidos con CPython 3.12.3 en Ubuntu bajo WSL2. Los datos son **sintéticos**, las semillas están fijadas y la mayoría de los experimentos (colas, reintentos, interruptores, disponibilidad, presupuestos, estabilidad y selección) corren en **tiempo virtual**: no hay reloj, red ni servidor reales, y las salidas de los experimentos de tiempo virtual fueron idénticas en ambos sistemas, cifra por cifra. Hay tres excepciones, todas intencionales: las **sondas de portabilidad** de `SE-381` y los artefactos dependientes del sistema de `SE-384` difieren entre Windows y Ubuntu por diseño, porque eso es lo que miden, y las **mediciones de tiempo de reloj** de `SE-377` (variación entre procesos, factor del perfilador y efecto de una caché) son lecturas de un equipo concreto que cambian en cada ejecución y no se reproducen al milisegundo; lo que se reproduce es la conclusión.

Los experimentos son: la media y los percentiles de 20 000 latencias con una cola lenta, un mes con seis definiciones del mismo objetivo y un verificador de forma frente a 180 mutaciones de escenarios (`SE-373`); tres reglas de análisis estático sobre 300 funciones generadas, tres compuertas de cobertura sobre 500 cambios y los bloqueos espurios de una cadena de comprobaciones (`SE-374`); cuatro pruebas sobre una cola de cuatro servidores, tres generadores de carga ante una pausa de diez segundos y la duración y el calentamiento de una prueba (`SE-375`); la latencia de una cola M/M/1 frente a su fórmula, cuatro formas de variabilidad del servicio con la ley de Little y la agregación de percentiles de ocho servidores (`SE-376`); la variación de una ordenación entre cinco procesos, un perfilador y una caché que distorsionan un benchmark y la comparación de dos copias idénticas con tres estadísticos (`SE-377`); cinco políticas de reintento tras un brownout de diez segundos y tras una oleada sincronizada de 400 clientes, tres capas encadenadas y seis timeouts (`SE-378`); un interruptor de circuito con cuatro configuraciones, un pool compartido frente a tres mamparos y cuatro políticas bajo una sobrecarga del doble (`SE-379`); la disponibilidad de 400 años simulados con y sin causa común, la pérdida de datos con dos y tres réplicas y seis umbrales de detección de fallos (`SE-380`); doce sondas de portabilidad, cinco fronteras de datos y una matriz de compatibilidad de 25 pares (`SE-381`); la misma página en el laboratorio y en tres segmentos, tres compuertas ante una deriva de peso y el contraste de los colores del repositorio (`SE-382`); tres umbrales de estabilidad, una matriz de cuatro fallos sobre dos configuraciones y la detección frente al radio de impacto (`SE-383`); y un validador de paquetes frente a 240 mutaciones, ocho artefactos entre dos sistemas y la selección de resultados favorables (`SE-384`).

Los parámetros (los 20 000 y los 2 000 diarios de peticiones, la cola del 1,5 %, los 4 servidores de 50 ms, la paciencia de 2 s, la fuga de una conexión cada 5 000 solicitudes, el calentamiento del 30 %, el ruido del 4 % con interferencias del 8 %, el timeout de 1 s con tres reintentos, el 3 % de peticiones lentas, el pool de 150 y el de 20, el costo de 5 ms de la respuesta degradada, el MTBF de 500 h y el MTTR de 0,5 h, las tasas anuales de fallo del 2 y del 20 %, los latidos con pérdida del 0,5 %, los tres segmentos de dispositivos, la deriva del 0,6 % por compilación, los seis trabajadores y los 40 solicitudes por segundo del modelo del taller y las doce mutaciones del validador) son **supuestos del autor**, no mediciones. Cada clase los lista y dice qué cambiaría si fueran otros.

Lo que **no se hizo**: no se midió ninguna API, base de datos, red ni servicio reales, ni se envió una sola petición a un sistema; no se usó ninguna herramienta de carga, de observabilidad, de interruptores ni de caos; no se midió ninguna persona usuaria, dispositivo ni navegador, ni se evaluó conformidad con WCAG, más allá de la razón de contraste de los colores declarados en el repositorio, que encontró una etiqueta del portal por debajo del 4,5:1 y queda registrada como seguimiento; no se probó macOS ni otras versiones de Python; el validador, el verificador de escenarios y las reglas de análisis se afinaron con los mismos casos que los evalúan, de modo que sus porcentajes muestran una frontera y no una tasa; y el resultado sobre el jitter de `SE-378` es propio de su modelo. La parte no tiene laboratorio en `labs/`, y su contenido sigue pendiente de revisión humana independiente.

## Guía razonada clase por clase

La API de entregas mantiene un contrato, un conjunto de escenarios y un informe estables mientras cambian las decisiones. Cada clase explica qué incertidumbre reduce, qué experimento la muestra, qué no demuestra y qué evidencia permite abandonar la conclusión.

### Bloque 1 — Definir y vigilar la calidad

#### SE-373 — Modelos de calidad y atributos medibles

Una promesa de calidad sin estadístico, ventana y alcance admite conclusiones opuestas con los mismos datos. La clase mide cuánto oculta la media de una cola lenta, aplica seis definiciones del objetivo «p95 ≤ 300 ms» a un mes con un incidente de tres horas y evalúa un verificador de forma de escenarios frente a 180 mutaciones.

El estudiante entrega cuatro escenarios de seis partes con medida y un árbol de utilidad. `SE-374` pregunta cómo se vigila que cada cambio no los empeore.

#### SE-374 — Revisión, análisis estático y quality gates

Una compuerta convierte una medida en una decisión y puede dejar pasar lo malo o bloquear lo bueno. La clase mide la precisión y los defectos no vistos de tres reglas con `ast`, compara una compuerta de cobertura total con una del cambio y calcula cuántos cambios bloquea el ruido al encadenar comprobaciones y qué pasa al reintentar.

El estudiante entrega las comprobaciones del cambio con su regla de decisión. `SE-375` pone a prueba el escenario de eficiencia con carga.

### Bloque 2 — Medir bajo carga

#### SE-375 — Carga, estrés, picos y endurance

Cada forma de carga responde una pregunta distinta y el generador es parte del experimento. La clase compara carga, estrés, pico y resistencia sobre la misma cola, muestra cómo un generador cerrado reduce un p99 de 9 071 ms a 232 ms ante una pausa y mide cuánto sesga el arranque.

El estudiante entrega un plan de pruebas con pregunta, generador, duración y criterio de parada. `SE-376` explica por qué la latencia crece como crece.

#### SE-376 — Latencia, throughput, saturación y capacidad

La espera crece como 1/(1 − utilización), se multiplica con la variabilidad del servicio y no se promedia. La clase contrasta una simulación con la fórmula de una cola, cambia solo la variabilidad con el mismo promedio y agrega los percentiles de ocho servidores de cuatro maneras.

El estudiante entrega un modelo de capacidad con su objetivo de cola. `SE-377` pregunta cómo se mide el tiempo sin engañarse.

#### SE-377 — Perfiles, benchmarks y errores de medición

Un benchmark devuelve una muestra de una distribución que depende del equipo y de lo que haga el instrumento. La clase mide la variación de una ordenación entre cinco procesos de un equipo real, el efecto de un perfilador y de una caché y cuántas veces dos copias idénticas «difieren» según el estadístico y las repeticiones.

El estudiante entrega un protocolo de benchmark con su prueba A/A. `SE-378` usa la forma de la cola de latencias para decidir timeouts y reintentos.

### Bloque 3 — Resistir el fallo

#### SE-378 — Timeouts, retries, backoff y jitter

El calendario de los reintentos reparte la carga y no limita su cantidad. La clase simula un brownout y una oleada sincronizada con cinco políticas y diez semillas, calcula los 27 intentos de tres capas sobre una base caída y compara seis timeouts frente a una distribución con cola.

El estudiante entrega una política de timeouts y reintentos con presupuesto y plazo propagado. `SE-379` limita el daño cuando la dependencia no se recupera.

#### SE-379 — Circuit breakers, bulkheads y degradación

Cada defensa tiene un costo y una señal. La clase mide cuántas llamadas evita un interruptor y cuánto retrasa la recuperación, cuánto arrastra una dependencia lenta a un pool compartido y qué respuestas útiles produce cada política bajo una sobrecarga del doble.

El estudiante entrega un mapa de dependencias con sus defensas. `SE-380` cuantifica qué disponibilidad y durabilidad se logran.

#### SE-380 — Disponibilidad, durabilidad y recuperación

La redundancia solo ayuda a la capa donde se aplica y una causa común la anula. La clase simula 400 años de operación con y sin despliegues que tumban ambas réplicas, calcula la pérdida de datos con dos y tres réplicas según el tiempo de reparación y compara seis umbrales de detección de fallos.

El estudiante entrega un presupuesto de fiabilidad con RTO y RPO medibles. `SE-381` pregunta qué ocurre con la compatibilidad.

### Bloque 4 — Compatibilidad y experiencia

#### SE-381 — Compatibilidad, portabilidad e interoperabilidad

El mismo software cambia de comportamiento con el sistema, la versión y el lector, casi siempre sin una excepción. La clase ejecuta doce sondas en Windows y Ubuntu, mide cuántos datos cambian de significado al cruzar una frontera y construye una matriz de compatibilidad de 25 pares con lectores estrictos y tolerantes.

El estudiante entrega un contrato de interoperabilidad con una matriz ejecutable. `SE-382` fija presupuestos de experiencia.

#### SE-382 — Calidad de experiencia y presupuestos

Un presupuesto es una restricción con dueño y con medida, y el percentil de la población puede cumplir mientras un segmento no. La clase compara el laboratorio con el campo, tres compuertas ante una deriva de peso del 0,6 % por compilación y el contraste de los colores del repositorio, que encuentra una etiqueta del portal por debajo del 4,5:1.

El estudiante entrega un presupuesto de experiencia con compuerta de tendencia. `SE-383` reúne las defensas en una prueba de presión.

### Bloque 5 — Aplicar e integrar

#### SE-383 — Taller: someter un sistema a presión controlada

Un experimento de presión enseña si la hipótesis, el radio y el aborto se decidieron antes. El taller compara tres umbrales de estado estable, inyecta cuatro fallos sobre una configuración ingenua y una endurecida y calcula cuánto tráfico hay que afectar para detectar un fallo débil.

El estudiante entrega un plan de experimento con sus hallazgos. `SE-384` lo integra en un informe reproducible.

#### SE-384 — Proyecto: informe reproducible de calidad

Un paquete completo no es un paquete honesto. El proyecto mide qué detecta un validador sobre 240 mutaciones, qué artefactos de un canal coinciden entre dos ejecuciones y entre Windows y Ubuntu y cuántos informes de dos versiones idénticas declararían una mejora según cómo se elija el resultado.

El estudiante entrega un paquete de informe con plan registrado, datos con huella, validador, ejecución en dos sistemas y `LIMITES.md`. La Parte 32 lleva la mirada a la seguridad, la privacidad y el cumplimiento.

## Resumen operativo del recorrido

| Clase | Núcleo profesional | Aporte acumulativo |
|---|---|---|
| [SE-373](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-31-calidad-rendimiento-y-resiliencia/se-373-modelos-de-calidad-y-atributos-medibles/) | Modelos de calidad y atributos medibles | Entrega cuatro escenarios de seis partes con medida y un árbol de utilidad |
| [SE-374](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-31-calidad-rendimiento-y-resiliencia/se-374-revision-analisis-estatico-y-quality-gates/) | Revisión, análisis estático y quality gates | Entrega las comprobaciones del cambio con su regla de decisión |
| [SE-375](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-31-calidad-rendimiento-y-resiliencia/se-375-carga-estres-picos-y-endurance/) | Carga, estrés, picos y endurance | Entrega un plan de pruebas con pregunta, generador, duración y criterio de parada |
| [SE-376](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-31-calidad-rendimiento-y-resiliencia/se-376-latencia-throughput-saturacion-y-capacidad/) | Latencia, throughput, saturación y capacidad | Entrega un modelo de capacidad con su objetivo de cola |
| [SE-377](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-31-calidad-rendimiento-y-resiliencia/se-377-perfiles-benchmarks-y-errores-de-medicion/) | Perfiles, benchmarks y errores de medición | Entrega un protocolo de benchmark con su prueba A/A |
| [SE-378](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-31-calidad-rendimiento-y-resiliencia/se-378-timeouts-retries-backoff-y-jitter/) | Timeouts, retries, backoff y jitter | Entrega una política de timeouts y reintentos con presupuesto y plazo propagado |
| [SE-379](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-31-calidad-rendimiento-y-resiliencia/se-379-circuit-breakers-bulkheads-y-degradacion/) | Circuit breakers, bulkheads y degradación | Entrega un mapa de dependencias con sus defensas |
| [SE-380](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-31-calidad-rendimiento-y-resiliencia/se-380-disponibilidad-durabilidad-y-recuperacion/) | Disponibilidad, durabilidad y recuperación | Entrega un presupuesto de fiabilidad con RTO y RPO medibles |
| [SE-381](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-31-calidad-rendimiento-y-resiliencia/se-381-compatibilidad-portabilidad-e-interoperabilidad/) | Compatibilidad, portabilidad e interoperabilidad | Entrega un contrato de interoperabilidad con una matriz ejecutable |
| [SE-382](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-31-calidad-rendimiento-y-resiliencia/se-382-calidad-de-experiencia-y-presupuestos/) | Calidad de experiencia y presupuestos | Entrega un presupuesto de experiencia con compuerta de tendencia |
| [SE-383](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-31-calidad-rendimiento-y-resiliencia/se-383-taller-someter-un-sistema-a-presion-controlada/) | Taller: someter un sistema a presión controlada | Entrega un plan de experimento con sus hallazgos |
| [SE-384](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-31-calidad-rendimiento-y-resiliencia/se-384-proyecto-informe-reproducible-de-calidad/) | Proyecto: informe reproducible de calidad | Entrega un paquete de informe con plan registrado, datos con huella, validador, ejecución en dos sistemas y `LIMITES.md` |

## Fuentes

- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — modelo de calidad del producto; autoridad: organismo de normalización.
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/), [Embracing Risk](https://sre.google/sre-book/embracing-risk/) y [Handling Overload](https://sre.google/sre-book/handling-overload/) — objetivos, riesgo y sobrecarga; autoridad: Google, libro de ingeniería de confiabilidad.
- [Little, «A proof for the queuing formula: L = λW»](https://doi.org/10.1287/opre.9.3.383) y [Dean y Barroso, «The tail at scale»](https://doi.org/10.1145/2408776.2408794) — colas y latencia de cola; autoridad: artículos originales.
- [Mytkowicz et al.](https://doi.org/10.1145/1508244.1508275) y [Kalibera y Jones](https://doi.org/10.1145/2464157.2464160) — errores de medición y rigor en benchmarks; autoridad: ASPLOS 2009 e ISMM 2013.
- [AWS Builders' Library: timeouts, retries y jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) y [Bronson et al., «Metastable failures»](https://doi.org/10.1145/3458336.3465286) — reintentos y fallos metaestables; autoridad: Amazon Web Services y HotOS 2021.
- [Fowler, «CircuitBreaker»](https://martinfowler.com/bliki/CircuitBreaker.html) y [Microsoft Azure Architecture: Bulkhead](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead) — interruptores y mamparos; autoridad: autor del texto y documentación de Microsoft.
- [Ford et al.](https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Ford.pdf) y [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) — fallos correlacionados y objetivos de recuperación; autoridad: OSDI 2010 y NIST.
- [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259) y [Unicode UAX #15](https://unicode.org/reports/tr15/) — interoperabilidad de números y de texto; autoridad: IETF y Unicode Consortium.
- [web.dev: LCP](https://web.dev/articles/lcp) y [W3C: contraste mínimo](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — experiencia medible; autoridad: Google y W3C.
- [Basiri et al., «Chaos Engineering»](https://doi.org/10.1109/MS.2016.60) y [Principios del caos](https://principlesofchaos.org/) — experimentos de presión; autoridad: IEEE Software 2016 y comunidad de ingeniería del caos.
- [Peng, «Reproducible research in computational science»](https://doi.org/10.1126/science.1213847) y [Simmons, Nelson y Simonsohn](https://doi.org/10.1177/0956797611417632) — reproducibilidad y flexibilidad analítica; autoridad: Science 2011 y Psychological Science 2011.

Las fuentes se vinculan también dentro de cada clase. Definen vocabulario y mecanismos; la adecuación de las decisiones de calidad se demuestra con el caso, la evidencia trazable y la revisión de otra persona, no con la autoridad de la fuente.

## Criterios de aceptación de la parte

- cada clase conecta mecanismo, medida y límite en una conclusión revisable;
- cada medida puede reproducirse desde un checkout limpio con las mismas semillas, salvo las lecturas de reloj, que declaran por qué no;
- ninguna afirmación sobre una API, una persona usuaria o un sistema real se apoya en una simulación;
- los límites declarados permiten a otra persona decidir qué comprobar antes de confiar.

[Volver al índice de clases](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md)
