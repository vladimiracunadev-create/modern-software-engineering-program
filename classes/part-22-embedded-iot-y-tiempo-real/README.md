# Parte 22 — Embedded, IoT y tiempo real

La Parte 21 llevó el software a clientes que corren sobre un sistema operativo completo, con memoria abundante y una red casi siempre disponible. La pregunta cambia de «qué hace el programa» a «qué hace cuando la memoria se mide en kilobytes, el tiempo es parte de lo correcto y nadie puede ir a reiniciarlo». Esta parte trabaja sobre un **nodo ambiental de una sala de estudio**, un caso sintético: mide temperatura, humedad y CO₂, tiene un botón y un extractor, y debe funcionar quince años con una pila. Recorre el firmware y su separación del hardware, los buses y los convertidores, el presupuesto de energía, memoria y precisión, los plazos y la planificación, los datos compartidos con las interrupciones, la comunicación por una red que se corta, la actualización remota, la identidad y las claves, el procesamiento en el borde, la seguridad y la vida útil, el modelado de fallos y un dispositivo simulado operable.

## Pregunta rectora

> ¿Qué garantiza este dispositivo cuando algo falla, cuándo deja de poder garantizarlo y cómo lo sabría quien lo opera?

## Antes del recorrido clase por clase

Esta parte no enseña un microcontrolador ni una plataforma. Enseña a medir la latencia de un evento según la arquitectura, a calcular cuándo un entero de ancho fijo desborda, a contar los ciclos de un bus y comparar códigos de control, a presupuestar la vida de una pila y de una flash, a decidir si un conjunto de tareas cumple sus plazos con el peor caso, a enumerar las posiciones de una interrupción y dimensionar un búfer, a elegir una garantía de entrega y repartir los reintentos de una flota, a actualizar sin dejar el dispositivo inservible, a evaluar el alcance de una clave extraída, a decidir qué se procesa en el dispositivo, la pasarela o la nube, a calcular los límites de la redundancia y de un temporizador de vigilancia, a inyectar fallos y a reunir todo en un paquete que otra persona opere. Cada clase ejecuta simulaciones con datos sintéticos que muestran un mecanismo (un botón que espera 166 ms, una escritura que deja inservible el dispositivo en 17 de 19 cortes, una espera exponencial que no conecta a 4309 de 5000 dispositivos) y declara lo que esa simulación no demuestra.

```mermaid
flowchart LR
    A[Hardware y firmware] --> B[Periféricos y buses]
    B --> C[Energía, memoria y precisión]
    C --> D[Plazos y tiempo real]
    D --> E[Interrupciones y estado compartido]
    E --> F[Conectividad intermitente]
    F --> G[Actualización y recuperación]
    G --> H[Identidad y claves]
    H --> I[Borde y pasarelas]
    I --> J[Safety, seguridad y vida útil]
    J --> K[Modelo de fallos]
    K --> L[Dispositivo operable]
    L -->|incidente o hallazgo| A
```

El diagrama se lee de izquierda a derecha y no es un proceso obligatorio. El retorno indica que un incidente en el campo, un fallo inyectado o una actualización fallida reabre el firmware; un paquete aprobado no cierra el diseño, lo fecha.

## Resultados acumulativos

Podrás medir la latencia de un evento sondeado y atendido por interrupción; calcular el rango de un acumulador y probar la lógica contra un modelo; contar los ciclos y la eficiencia de una transacción de bus y comparar paridad, suma y CRC; presupuestar la vida de una pila, el desgaste de una flash y el error de un filtro de enteros; analizar un conjunto de tareas por prioridades fijas y reproducir una inversión de prioridad; enumerar las posiciones de una interrupción y dimensionar un búfer por la parada más larga; elegir la garantía, la cola y el reintento de cada mensaje; enumerar los cortes de una actualización y dimensionar las etapas de un despliegue; comparar esquemas de claves, ventanas de tiempo y semillas; asignar cada decisión al dispositivo, la pasarela o la nube; calcular el límite de la redundancia, el plazo de un temporizador de vigilancia y la vuelta de un contador; inyectar fallos y medir la estabilidad de un AMFE; y entregar un paquete de dispositivo con un validador cuyos límites conoces.

Al finalizar podrás defender un dispositivo con sus plazos de peor caso, su presupuesto de recursos, su política de comunicación, su plan de actualización, su política de identidad, su análisis de peligros y una lista de lo que ninguna simulación ni validador ve, y podrás indicar qué parte de tu conclusión es observación, cuál es inferencia y cuál es suposición.

## Prerrequisitos enlazados

- [Parte 4 — Pensamiento computacional](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/): modelado, enumeración de casos y razonamiento sobre evidencia.
- [Parte 7 — Estructuras de datos y algoritmos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/): medir, comparar y no confundir un resultado con un modelo.
- [Parte 13 — Especificaciones, contratos y modelos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-13-especificaciones-contratos-y-modelos/): eventos duplicados, compatibilidad entre versiones y contratos comprobables.
- [Parte 15 — Procesos, planificación y estimación](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/): flujo, colas, riesgos y reglas de replanificación.
- [Parte 21 — Software móvil, escritorio y multiplataforma](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-21-software-movil-escritorio-y-multiplataforma/): ciclo de vida, almacenamiento local y distribución de actualizaciones.
- Python 3.11+ y terminal; los experimentos usan solo la biblioteca estándar y datos sintéticos.

## Bloques y progresión

1. **Del hardware al firmware:** las clases 265–267 separan hardware, firmware y lógica, miden los buses y los convertidores y presupuestan energía, memoria y precisión.
2. **Tiempo y concurrencia:** las clases 268–269 analizan los plazos con el peor caso y los datos compartidos con las interrupciones.
3. **El dispositivo en una red:** las clases 270–272 tratan la conectividad intermitente, la actualización con recuperación y la identidad con claves.
4. **Arquitectura y vida útil:** las clases 273–274 asignan el procesamiento al dispositivo, la pasarela o la nube y calculan los límites de safety, seguridad y vida útil.
5. **Aplicar e integrar:** las clases 275–276 modelan fallos físicos y digitales y entregan un dispositivo simulado operable y actualizable.

## Evidencia medida y límites

Las figuras y los ejemplos de esta parte usan simulaciones ejecutadas con CPython 3.12.9 en Windows 11 y repetidas con CPython 3.12.3 en Ubuntu bajo WSL2. Los datos son **sintéticos** y las semillas están fijadas: las salidas de los doce experimentos fueron idénticas en ambos sistemas salvo la codificación de los acentos en la consola de Windows, sin diferencias en ninguna cifra. Ninguno mide tiempos de ejecución. Todo el código usa solo la biblioteca estándar.

Los experimentos son: latencia de un botón sondeado y por interrupción, un acumulador de 16 bits que desborda y los mutantes de un antirrebote (`SE-265`); la eficiencia de I²C y SPI, los errores no detectados por paridad, suma y CRC-8 y el sobremuestreo de un convertidor de 10 bits (`SE-266`); la vida de una pila según el periodo y el reposo, el desgaste de una flash con tres políticas y la zona muerta de un filtro de enteros (`SE-267`); la planificabilidad de conjuntos de tareas con análisis exacto, los plazos incumplidos con tiempos de ejecución variables y una inversión de prioridad con y sin herencia (`SE-268`); las diez posiciones de una interrupción, las lecturas partidas de 16 bits y un búfer circular (`SE-269`); tres niveles de garantía de entrega, una cola de almacenar y reenviar y una tormenta de reconexión (`SE-270`); los cortes de energía de una actualización, el tamaño de una actualización diferencial y un despliegue por etapas (`SE-271`); el alcance de una clave extraída con HMAC real, las ventanas de tiempo y las semillas débiles (`SE-272`); cinco estrategias de reporte, una decisión con plazo local o en la nube y las codificaciones de la carga (`SE-273`); la votación dos de tres con causa común, el plazo de un temporizador de vigilancia y la vuelta de un contador de 32 bits (`SE-274`); una campaña de inyección de fallos, los cortes de la escritura de una configuración y la estabilidad de un AMFE (`SE-275`); y un mes de mil dispositivos, un validador de paquetes con 200 mutaciones y un despliegue a mil dispositivos (`SE-276`).

Los parámetros (el bucle de 10 a 50 ms, las lecturas con ruido gaussiano, los conjuntos de tareas generados al azar y los tiempos lognormales, las corrientes de 15 y 80 mA, los 10 000 borrados por sector, la pérdida independiente por paquete, las desconexiones geométricas de media 30 minutos, el colapso del servidor sobre 1,5 veces su capacidad, la flota de 10 000 dispositivos, el desfase gaussiano del reloj, la señal de temperatura con ocho picos, p = 0,1 por sensor, un cuelgue al mes, los seis tipos de fallo, las puntuaciones sintéticas del AMFE, el 3 % de fallo de una versión y el 90 % de informe y de reparación) son supuestos del autor, no datos de un producto, una institución ni de personas reales. Las reglas léxicas de los dos validadores se ajustaron con los mismos casos que las evalúan: su exactitud real es desconocida. Los generadores de números pseudoaleatorios de Python se usaron solo para simular; no son criptográficos. No se usó ningún microcontrolador, compilador de firmware, sistema operativo de tiempo real, agente MQTT, cargador de arranque, pasarela, sensor ni red; no se midió consumo ni peor caso de ejecución, no se atacó ningún chip y no se hizo un análisis de seguridad funcional. Esta parte no tiene laboratorio propio en `labs/`; el proyecto integrador `SE-276` define el paquete y la evidencia. Cada clase termina con un puente hacia el trabajo con agentes.

## Guía razonada clase por clase

El nodo ambiental mantiene un firmware, un presupuesto y un paquete estables mientras cambian las decisiones. Cada clase explica qué incertidumbre reduce, qué simulación la muestra, qué no demuestra y qué evidencia permite abandonar la conclusión.

### Bloque 1 — Del hardware al firmware

#### SE-265 — Hardware, firmware y software embebido

La arquitectura del firmware decide qué garantiza sobre la respuesta a un evento y qué parte puede probarse sin el dispositivo. La clase mide la latencia de un botón sondeado frente a uno atendido por interrupción, calcula cuándo un acumulador de 16 bits desborda y mide qué mutantes de un antirrebote matan unos ejemplos y unas secuencias con rebotes.

El estudiante separa la lógica del acceso al hardware y escribe las condiciones de rango del nodo. `SE-266` baja a los periféricos y los buses.

#### SE-266 — Microcontroladores, periféricos y buses

Leer un dato cuesta ciclos, puede corromperse y tiene una resolución que depende del ruido. La clase calcula la eficiencia de I²C y de SPI, mide los errores que dejan pasar la paridad, la suma y el CRC-8 y mide cuánto mejora el sobremuestreo con y sin ruido.

El estudiante elige un bus, un código de control y un factor de sobremuestreo con sus supuestos. `SE-267` traduce esas decisiones en energía y memoria.

#### SE-267 — Restricciones de memoria, energía y cómputo

La energía, la memoria no volátil y la precisión numérica son tres recursos escasos con tres mecanismos de agotamiento distintos. La clase calcula la vida de una pila según el periodo y el reposo, simula el desgaste de una flash con tres políticas de reparto y mide la zona muerta de un filtro de enteros con truncado y con redondeo.

El estudiante entrega un presupuesto con sus supuestos. `SE-268` añade los plazos que el firmware debe cumplir.

### Bloque 2 — Tiempo y concurrencia

#### SE-268 — Sistemas de tiempo real y deadlines

Un plazo se cumple con el peor caso, no con la media. La clase mide qué fracción de conjuntos de tareas es planificable por prioridades fijas, cuántos plazos incumple una tarea con tiempo de ejecución variable y cuánto retrasa una inversión de prioridad a la tarea más importante, con y sin herencia.

El estudiante entrega el análisis de plazos del nodo con su peor caso declarado. `SE-269` entra en cómo las tareas y las interrupciones comparten estado.

#### SE-269 — Interrupciones, concurrencia y estado compartido

Una interrupción corre entre dos instrucciones cualesquiera. La clase enumera las diez posiciones en que pierde un incremento, mide la frecuencia y el tamaño de una lectura partida de 16 bits y dimensiona un búfer circular por la parada más larga del consumidor.

El estudiante escribe la regla de datos compartidos del nodo. `SE-270` saca esos datos del dispositivo.

### Bloque 3 — El dispositivo en una red

#### SE-270 — Protocolos IoT y conectividad intermitente

La red se corta y cada garantía de entrega compra paquetes. La clase simula tres niveles de calidad de servicio sobre un enlace con pérdidas, dimensiona una cola de almacenar y reenviar y compara tres políticas de reintento tras una caída de 5000 dispositivos.

El estudiante entrega la política de comunicación del nodo. `SE-271` usa ese canal para actualizar el firmware.

#### SE-271 — Actualizaciones OTA y recuperación

Una actualización es una secuencia de pasos que puede cortarse en cualquiera. La clase enumera los puntos de corte de cuatro estrategias, compara dos métodos de actualización diferencial y simula un despliegue por etapas de una versión defectuosa.

El estudiante entrega el plan de actualización con ranuras, reversión, etapas y criterio de parada. `SE-272` pregunta cómo el dispositivo sabe que el código es legítimo.

#### SE-272 — Identidad de dispositivo y gestión de claves

La seguridad de una clave depende de cuántos dispositivos la comparten, de qué impide reproducir un mensaje y de cómo se generó. La clase mide el alcance de una extracción con HMAC real en tres esquemas, los rechazos de una ventana de tiempo según el desfase del reloj y las claves repetidas y recuperables con una semilla débil.

El estudiante entrega la política de identidad del nodo. `SE-273` mueve parte del procesamiento al borde.

### Bloque 4 — Arquitectura y vida útil

#### SE-273 — Edge, gateways y procesamiento local

Cada decisión vive donde su plazo y su dato se cumplen. La clase compara cinco estrategias de reporte de una señal con ocho eventos, mide el cumplimiento de un plazo de 100 ms para una decisión local y para otra en la nube y compara los bytes por muestra de JSON y de binario con y sin compresión.

El estudiante asigna cada decisión al dispositivo, la pasarela o la nube. `SE-274` pregunta qué ocurre con la seguridad y la vida útil.

#### SE-274 — Safety, seguridad y vida útil prolongada

Un dispositivo que dura años cruza fechas y fallos que el desarrollo olvida. La clase calcula cuánto reduce una votación dos de tres el fallo según la causa común, el plazo de un temporizador de vigilancia por sus reinicios falsos y la vuelta de un contador de 32 bits con dos comparaciones.

El estudiante entrega el análisis de peligros del nodo. `SE-275` los pone a prueba con fallos deliberados.

### Bloque 5 — Aplicar e integrar

#### SE-275 — Taller: modelar fallos físicos y digitales

Una defensa se mide inyectando el fallo que debe ver. El taller detecta 600 fallos de seis tipos con cinco conjuntos de comprobaciones, enumera los cortes de la escritura de una configuración y mide cuán estable es el orden de un AMFE si dos personas puntúan distinto.

El estudiante entrega el modelo de fallos del nodo con lo que queda sin cubrir. `SE-276` lo integra.

#### SE-276 — Proyecto: dispositivo simulado operable y actualizable

Un dispositivo es operable cuando otra persona puede mantenerlo sin su autor. El proyecto simula un mes de mil dispositivos con cuatro configuraciones, valida un paquete con 200 mutaciones y separa en un despliegue a mil dispositivos el efecto de las etapas del de la reversión. La Parte 23 pasa a los dominios especializados.

El estudiante entrega el paquete, el validador, la simulación y la lista de lo que el validador no ve.

## Resumen operativo del recorrido

| Clase | Capacidad que construye | Pregunta que resuelve | Evidencia acumulativa |
|---|---|---|---|
| [SE-265](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/) | Hardware, firmware y software embebido | ¿Qué garantiza el firmware sobre un evento? | `embedded-log.md` con latencia, rango y mutantes |
| [SE-266](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/) | Microcontroladores, periféricos y buses | ¿Cuánto cuesta y qué errores deja pasar cada lectura? | `bus-log.md` con eficiencia, códigos y ADC |
| [SE-267](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/) | Restricciones de memoria, energía y cómputo | ¿Qué recurso se agota primero? | `budget-log.md` con presupuesto y supuestos |
| [SE-268](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/) | Sistemas de tiempo real y deadlines | ¿Cumple cada tarea su plazo con el peor caso? | `rt-log.md` con análisis de plazos |
| [SE-269](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/) | Interrupciones, concurrencia y estado compartido | ¿Qué pasa si una interrupción cae aquí? | `isr-log.md` con regla de datos compartidos |
| [SE-270](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/) | Protocolos IoT y conectividad intermitente | ¿Qué garantía necesita cada mensaje y qué hace el nodo sin red? | `net-log.md` con política de comunicación |
| [SE-271](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/) | Actualizaciones OTA y recuperación | ¿En qué paso un corte me deja sin dispositivo? | `ota-log.md` con plan de actualización |
| [SE-272](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/) | Identidad de dispositivo y gestión de claves | ¿Qué pasa si se extrae una clave? | `identity-log.md` con política de identidad |
| [SE-273](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/) | Edge, gateways y procesamiento local | ¿Qué se decide dónde y qué viaja? | `edge-log.md` con asignación por niveles |
| [SE-274](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/) | Safety, seguridad y vida útil | ¿Qué falla, qué lo cubre y qué lo rompe? | `safety-log.md` con análisis de peligros |
| [SE-275](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/) | Taller: modelar fallos físicos y digitales | ¿Qué fallo no ve ninguna defensa? | `fault-model-log.md` con inyección y cobertura |
| [SE-276](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/) | Proyecto: dispositivo operable y actualizable | ¿Puede otra persona operarlo sin su autor? | `device-package-log.md`, validador y simulación |

## Proyecto integrador

El proyecto **SE-276** entrega un paquete de dispositivo con nueve secciones (identidad, versiones y reversión, claves, umbrales, reintentos, despliegue, vigilancia, responsable y revisión), un validador de forma con sus mutaciones, la simulación de un mes de una flota con cuatro configuraciones, la separación de las etapas y la reversión en un despliegue y la lista de decisiones de sentido que el validador no ve. Se acompaña de los límites declarados: qué parte del paquete no se comprobó con hardware ni con un cargador real.

## Criterios de salida

- las doce clases explican todos sus temas mediante mecanismos, ejemplos y límites;
- cada plazo del dispositivo se analiza con el peor caso y su origen declarado, no con la media;
- cada dato compartido con una interrupción tiene un escritor, un lector y una protección declarados;
- cada paso de la actualización tolera un corte, comprobado por enumeración;
- cada clave tiene un alcance de extracción conocido, un mecanismo anti-reproducción y un origen de aleatoriedad;
- las probabilidades, los porcentajes y los parámetros se declaran como supuestos y nunca como mediciones de un producto;
- otra persona reproduce comandos y resultados desde un checkout limpio;
- el informe declara lo observado, lo inferido y lo no ejecutado.

## Preguntas de control por bloque

- ¿Qué parte de este firmware se comprobó sin el dispositivo y cuál exige hardware?
- ¿Cuál es el peor caso de esta tarea y quién lo midió?
- ¿Qué pasa si una interrupción cae entre estas dos instrucciones?
- ¿En qué paso de la actualización un corte me deja sin dispositivo?
- ¿Qué parte del paquete depende de que una persona lea el sentido y no de una comprobación?

## Fuentes de la parte

- [Lee y Seshia, «Introduction to Embedded Systems: A Cyber-Physical Systems Approach»](https://ptolemy.berkeley.edu/books/leeseshia/) — sistemas embebidos y ciberfísicos con el tiempo en la semántica; autoridad: autores del libro (UC Berkeley).
- [Barr Group, «Embedded C Coding Standard»](https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard) — reglas de codificación para firmware; autoridad: Barr Group.
- [Liu y Layland, «Scheduling algorithms for multiprogramming in a hard-real-time environment» (JACM, 1973)](https://doi.org/10.1145/321738.321743) — planificación por prioridades por periodo; autoridad: Journal of the ACM.
- [Sha, Rajkumar y Lehoczky, «Priority inheritance protocols» (IEEE Transactions on Computers, 1990)](https://doi.org/10.1109/12.57058) — herencia de prioridad; autoridad: IEEE Transactions on Computers.
- [OASIS, MQTT versión 3.1.1](https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html) — niveles de calidad de servicio; autoridad: OASIS.
- [Moran et al., RFC 9019: A Firmware Update Architecture for Internet of Things](https://www.rfc-editor.org/rfc/rfc9019) — arquitectura de actualización de firmware; autoridad: IETF.
- [NIST SP 800-57 Parte 1 rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) — gestión de claves; autoridad: NIST.
- [ETSI EN 303 645](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/) — requisitos básicos de ciberseguridad para IoT de consumo; autoridad: ETSI.
- [Hsueh, Tsai e Iyer, «Fault injection techniques and tools» (IEEE Computer, 1997)](https://doi.org/10.1109/2.585157) — inyección de fallos; autoridad: IEEE Computer.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.

Las fuentes se vinculan también dentro de cada clase. Definen vocabulario y mecanismos; la adecuación de las decisiones del nodo ambiental se demuestra con el caso, la evidencia trazable y la revisión de otra persona, no con la autoridad de la fuente.
