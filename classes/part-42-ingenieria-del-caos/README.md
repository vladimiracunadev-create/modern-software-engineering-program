# Parte 42 — Ingeniería del caos

La [Parte 41](../part-41-observabilidad-sre-e-incidentes/README.md) enseñó a observar un servicio, a prometer un nivel de servicio y a responder cuando falla. La pregunta cambia de «¿qué hacemos cuando el sistema falla?» a «¿cómo sabemos, antes de que falle, que lo que declaramos que resiste, resiste de verdad?». Esta parte trabaja sobre **el cliente de la API de entregas de la plataforma educativa y su dependencia de almacenamiento de archivos**, un caso sintético: un servicio con tiempos de espera, reintentos, cortacircuitos y respuesta alternativa que recibe 90 peticiones por segundo en cierres de plazo, con una dependencia de 8 hilos. Cada clase convierte una práctica de la ingeniería del caos (declarar, definir el estado estable, acotar el daño, inyectar, practicar, automatizar, llevar a producción, extender a datos y a seguridad, y poner límites) en un mecanismo que se puede medir, mide cómo se engaña quien la usa mal y declara qué no demuestra.

## Pregunta rectora

> ¿Qué hipótesis sobre el comportamiento de un sistema bajo falla se puede escribir, con qué daño se puede poner a prueba y qué evidencia reproducible permite a otra persona comprobarla, refutarla o decir cuándo deja de valer?

## Antes del recorrido clase por clase

Esta parte no enseña un producto de caos, una plataforma de experimentos ni una herramienta de inyección. Enseña a distinguir una resiliencia declarada de una demostrada y a ver cómo un mecanismo de protección puede mantener caído a un sistema después de que la falla terminó, a escribir un estado estable con su banda y una regla de refutación que no refute lo sano, a dimensionar el radio de explosión y las condiciones de aborto sobre el grupo que recibe la falla, a elegir las fallas por mecanismo y por la huella que dejan, a escoger la herramienta por la capa en que actúa y no por su catálogo, a ejercitar a las personas además del sistema en un día de práctica, a llevar lo automatizable al pipeline y reconocer las regresiones que ninguna defensa ve, a comprobar la integridad de los datos y la calidad de un modelo cuando nada devuelve un error, a hacer un experimento en producción con grupo de control y a calcular la holgura de una región, a producir evidencia de seguridad con un número de ensayos y una exposición medidas, a poner un presupuesto y una regla de equidad a los experimentos, y a reunir todo en un programa con validador, huella y límites. Cada clase ejecuta experimentos con datos sintéticos que muestran un mecanismo (una configuración que declara reintentos con pausa y se mantiene en 0 % de peticiones correctas 60 s después de terminar la falla, 54 % de ventanas sanas refutadas por una regla sin banda, 72 % de detección con 0,5 % del tráfico frente a 100 % con 2 %, un aborto global que dispara a los 10 s con el experimento esperado y no ve nada con el 0,5 %, una latencia de red que no mueve ninguna señal salvo el p99 y una caída de proceso casi idéntica a la lentitud, 311 ms de espera hasta el silencio frente a 10 ms hasta el reinicio de una conexión real, 12,6 defectos latentes tras dos años sin práctica frente a 1,1 con un día por trimestre, 5 de 6 regresiones dañinas detectadas por una lectura estática y 3 por una suite de cuatro escenarios, 4,3 escrituras confirmadas perdidas por conmutación, 72,7 % de exactitud con la mitad de las características ausentes, evacuaciones que solo se sostienen con 40 % de utilización previa si hay dos regiones, un umbral de saturación entre 10 % y 20 % de peticiones lentas, 59 ensayos para sostener una tasa de fallas menor que 5 %, 456 segundos de exposición media con una caché de 900 s, 38,6 % de meses incumplidos con un calendario fijo de experimentos y 252 de 360 especificaciones defectuosas detectadas por un validador) y declara lo que esa medida no demuestra.

![Diagrama de flujo con 12 pasos. Recorrido: «Estado estable e hipótesis»; luego «Alcance, radio y aborto»; luego «Fallos de red, latencia y dependencias»; luego «Fallos de recursos e infraestructura»; luego «Kubernetes y plataformas cloud»; luego «Fallos de datos y de estado»; luego «Game days y respuesta a incidentes»; luego «Caos continuo: CI/CD y producción»; luego «Seguridad y gobernanza»; luego «Aprender de los experimentos»; luego «Taller: experimento acotado con aborto»; luego «Proyecto: programa de caos con evidencia». Retornos: «Proyecto: programa de caos con evidencia» lleva a «Estado estable e hipótesis» (hallazgo o cambio).](../../site/assets/figures/mermaid-61e6b9a9bf.svg)

El diagrama se lee de izquierda a derecha y no es un proceso obligatorio. El retorno indica que un hallazgo, un incidente o un cambio de la configuración reabre la pregunta de qué se declaraba y qué se había demostrado; un programa validado no cierra la práctica, la fecha.

## Resultados acumulativos

Podrás escribir un estado estable como una salida medible con su ventana y su banda, medir el ruido de un indicador sano según la ventana, calcular cuántas ventanas sanas refuta cada una de tres reglas, estimar la potencia de ver un efecto de 0,6 puntos y escribir una hipótesis con regla de refutación (`SE-505`); calcular el costo de un experimento en peticiones dañadas, estimar el radio mínimo que detecta un efecto con grupo de control, comparar cuatro condiciones de aborto ante una falla que empeora y escribir la especificación de un experimento con reversión probada (`SE-506`); comparar cinco configuraciones de un cliente (espera de 5 s, reintentos sin pausa, espera corta con reintentos con azar y dos cortacircuitos) frente a seis fallas de red, latencia y dependencias, reconocer un fallo metaestable que persiste 60 s tras terminar la falla, medir los intentos por petición que amplifican la carga y detectar cuándo un cortacircuitos sensible convierte 30 % de errores en 13 % de calidad completa (`SE-507`);

clasificar fallas por mecanismo (red, recursos, dependencias, reloj, discos y procesos), leer la huella de seis fallas en cuatro señales y encontrar las indistinguibles, calcular los tokens rechazados por un desfase de reloj según la tolerancia y comparar el registro síncrono y el asíncrono ante una parada de disco (`SE-508`); medir con sockets reales qué ve un cliente de 300 ms ante 50, 200 y 400 ms de latencia, un reinicio y un silencio, clasificar herramientas por la capa en que actúan (conexión, orquestador de Kubernetes, servicio de nube, instancia) y separar lo medido de lo documentado (`SE-509`); calcular las escrituras confirmadas perdidas al conmutar con replicación asíncrona, las lecturas obsoletas según el retraso de la réplica y la exactitud de un modelo con características ausentes, obsoletas o sustituidas por una regla de reserva (`SE-510`);

diseñar un día de práctica con roles, reglas y aborto, clasificar los defectos que encuentra y comparar cuatro programas de práctica por defectos latentes y por la edad con que salen a la luz (`SE-511`); detectar siete cambios de configuración con una lectura estática y con una suite de cuatro escenarios deterministas, medir las falsas alarmas, reconocer las regresiones tapadas por otra protección y situar el experimento continuo en producción (`SE-512`); calcular el costo de un programa de experimentos contra un presupuesto de error, medir quién carga con el daño al elegir por petición o por cliente y escribir una compuerta de decisión y una política de permisos (`SE-513`); calcular cuántos ensayos sostienen una tasa de fallas, clasificar controles de seguridad con distintos números de ensayos y medir la exposición tras revocar una credencial según la vigencia de una caché (`SE-514`);

calcular la carga de las regiones que sobreviven a una evacuación, encontrar el umbral de saturación entre un experimento difuso y uno concentrado y ejecutar un experimento acotado con control, aborto y las ocho precondiciones de un primer experimento en producción (`SE-515`); y validar especificaciones de experimento frente a 360 mutaciones, ejecutar un ciclo con grupo de control y huella reproducible y entregar un programa con catálogo, especificaciones, política, validador, resultados, remediación y límites (`SE-516`).

Al finalizar podrás defender un programa de experimentos de caos con sus hipótesis, su estado estable, su radio y su aborto, su catálogo de fallas, su día de práctica, su etapa de pipeline, sus experimentos de datos, su gobernanza, sus criterios de evidencia, un validador, una huella reproducible, un plan de remediación y una lista de lo que ningún validador ve, y podrás indicar qué parte de tu conclusión es observación, cuál es inferencia y cuál es suposición.

## Prerrequisitos enlazados

- [Parte 29 — Datos, persistencia y recuperación](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-29-datos-persistencia-y-recuperacion/): copias, réplicas y recuperación.
- [Parte 32 — Concurrencia y sistemas distribuidos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-32-concurrencia-y-sistemas-distribuidos/): fallos parciales, relojes, consistencia y la clase de caos controlado.
- [Parte 33 — Cloud, plataforma e infraestructura](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-33-cloud-plataforma-e-infraestructura/): regiones, contenedores y dependencias de plataforma.
- [Parte 36 — Calidad, rendimiento y resiliencia](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-36-calidad-rendimiento-y-resiliencia/): percentiles, colas, reintentos, cortacircuitos, bulkheads y recuperación.
- [Parte 40 — CI/CD, IaC y platform engineering](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-40-ci-cd-iac-y-platform-engineering/): camino a producción, gates y credenciales efímeras.
- [Parte 41 — Observabilidad, SRE e incidentes](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-41-observabilidad-sre-e-incidentes/): señales, objetivos, alertas, incidentes y continuidad.
- Python 3.11+ y terminal; los experimentos usan solo la biblioteca estándar y datos sintéticos, salvo la medición de sockets locales de `SE-509`, que es una lectura real del equipo.

## Bloques y progresión

1. **Definir y acotar:** las clases 505 y 506 fijan el estado estable y la hipótesis con su ruido, y dimensionan el alcance, el radio de impacto y las condiciones de aborto.
2. **Inyectar:** las clases 507 a 510 inyectan fallas de red, latencia y dependencias, de recursos e infraestructura, con herramientas de Kubernetes y de nube, y de datos y de estado.
3. **Practicar y automatizar:** las clases 511 y 512 ejercitan a las personas en un día de práctica y llevan lo automatizable al pipeline y a la producción continua.
4. **Gobernar y aprender:** las clases 513 y 514 ponen presupuesto, permisos y registro a la práctica y miden qué se aprende de un experimento.
5. **Aplicar e integrar:** las clases 515 y 516 ejecutan un experimento acotado con aborto y reúnen la parte en un programa con evidencia, validador, huella y remediación.

## Evidencia medida y límites

Las figuras y los ejemplos de esta parte usan experimentos ejecutados con CPython 3.12.9 en Windows 11 y repetidos con CPython 3.12.3 en Ubuntu bajo WSL2. Los datos son **sintéticos**, las semillas están fijadas y casi todos los experimentos corren en **tiempo virtual** sobre un simulador de eventos discretos de un cliente con espera, reintentos y cortacircuitos frente a una dependencia con hilos y cola: no hay reloj, red ni servidor reales, y las salidas de esos experimentos fueron idénticas en ambos sistemas, cifra por cifra. Hay una excepción intencional: la **medición de sockets locales** de `SE-509` (un proxy propio de unas 80 líneas, un servidor HTTP local y un cliente con espera de 300 ms, con 30 peticiones secuenciales por escenario) usa relojes y conexiones reales; sus conteos de éxitos se repiten y sus milisegundos varían unos puntos entre ejecuciones y sistemas, y por eso la figura usa los valores medidos el 23 de noviembre de 2026 en Windows 11 y los declara como tales.

Los experimentos son: el ruido de un indicador sano con 24 ejecuciones de 240 s, la tasa de refutaciones falsas de tres reglas y la potencia frente a un efecto de 4 ms (`SE-505`); la detección y el daño para siete radios con 60 repeticiones y cuatro condiciones de aborto ante una falla que empeora (`SE-506`); cinco configuraciones del cliente frente a seis fallas con tres semillas, la serie temporal de un fallo metaestable y los intentos por petición (`SE-507`); la huella de seis fallas en cuatro señales, 100 000 tokens por celda para tres tolerancias y seis desfases, y una parada de disco con registro síncrono y tres búferes (`SE-508`); la medición de sockets locales (`SE-509`); 20 000 conmutaciones por perfil de retraso, la probabilidad de lecturas obsoletas y un modelo logístico con 4 000 peticiones de prueba y tres políticas (`SE-510`); cuatro programas de práctica con 300 simulaciones de 24 meses cada uno (`SE-511`); siete cambios de configuración frente a cuatro escenarios con ocho semillas, las reglas estáticas y las falsas alarmas (`SE-512`); 4 000 meses con tres políticas y 40 clientes con 24 experimentos (`SE-513`); la probabilidad de pasar ensayos, la regla de tres con 20 000 controles, 30 controles con cuatro números de ensayos y la exposición de 2 000 clientes tras una revocación (`SE-514`); 16 combinaciones de regiones y utilizaciones y nueve fracciones de peticiones lentas para tres clientes (`SE-515`); y un validador frente a 360 mutaciones de diez tipos con cuatro experimentos y su huella (`SE-516`).

Los parámetros (los 90 peticiones por segundo, la dependencia de 8 hilos con 40 ms de servicio y su cola de 1,5 s, las cinco configuraciones y sus umbrales, las seis fallas y sus intensidades, el 0,4 % de errores de fondo y la cola larga del indicador, el 5 % de errores y la sorpresa a los 60 s del experimento, los umbrales de 1 %, 50 % y 300 peticiones de aborto, los tokens de 300 s, el búfer y la parada de 2 s, los defectos de tres técnicas y tres humanas con 6 % de salida mensual y 70 % y 80 % de hallazgo, las siete regresiones y las reglas estáticas, los 200 escrituras por segundo y los retrasos con picos, el modelo de seis características, la capacidad de 200 peticiones por segundo por región, los 30 controles con eficacias de 99,9, 97 y 80 %, los 2 000 clientes con vigencias de caché, los 1,2 incidentes por mes y los 40 clientes con cuota 1/k y las diez mutaciones de la especificación) son **supuestos del autor**, no mediciones. Cada clase los lista y dice qué cambiaría si fueran otros.

Lo que **no se hizo**: no se inyectó ninguna falla, no se dañó ninguna petición ni se evacuó ninguna región de un sistema real, ni se envió una sola petición a un servicio de terceros; no se ejecutó ninguna de las herramientas descritas (Toxiproxy, Chaos Mesh, LitmusChaos, AWS Fault Injection Service, Azure Chaos Studio, Chaos Monkey), y lo que se dice de ellas procede de su documentación oficial y de los artículos de ingeniería de Netflix, que se atribuyen; no se organizó ningún día de práctica ni se midió ningún equipo; no se revocó ninguna credencial real ni se auditó ningún control; no se conmutó ninguna base de datos ni se entrenó ningún modelo real; no se probó macOS ni otras versiones de Python; el validador, las reglas estáticas y las políticas de aborto se afinaron con los mismos casos que los evalúan, de modo que sus porcentajes muestran una frontera y no una tasa de detección; y los resultados sobre frecuencia de práctica, radio mínimo y umbrales de saturación son propios de sus modelos. La parte no tiene laboratorio en `labs/`, y su contenido sigue pendiente de revisión humana independiente.

## Guía razonada clase por clase

El cliente de la API de entregas mantiene una configuración, un catálogo de fallas y un paquete de experimentos estables mientras cambian las decisiones. Cada clase explica qué incertidumbre reduce, qué experimento la muestra, qué no demuestra y qué evidencia permite abandonar la conclusión.

### Bloque 1 — Definir y acotar

#### SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis

Una resiliencia declarada no es una resiliencia demostrada, y para demostrarla hay que decidir contra qué se compara. La clase mide la dispersión de un indicador sano según la ventana, cuenta cuántas ventanas sanas refuta cada regla (54 % la que no tiene banda) y estima qué efecto puede ver una ventana de dos minutos.

El estudiante entrega una hipótesis con métrica, ventana, banda y regla de refutación. `SE-506` decide cuánta gente puede pagar el experimento.

#### SE-506 — Diseñar experimentos de fallo: alcance y radio de impacto

El daño y la detección crecen distinto con el radio. La clase calcula el costo en peticiones dañadas, mide la detección con grupo de control (72 % con 0,5 % del tráfico, 100 % desde 2 %) y compara cuatro condiciones de aborto ante una falla que empeora.

El estudiante entrega la especificación de un experimento con aborto y reversión. `SE-507` inyecta las primeras fallas.

### Bloque 2 — Inyectar

#### SE-507 — Inyección de fallos de red, latencia y dependencias

Una arquitectura con tiempos de espera, reintentos y cortacircuitos no es una arquitectura probada. La clase somete cinco configuraciones a seis fallas, mide los intentos por petición que amplifican la carga y muestra un fallo metaestable que sigue 60 s después de terminar la falla y un cortacircuitos sensible que baja la calidad completa a 13 % con 30 % de errores.

El estudiante entrega una tabla «mecanismo declarado → falla → resultado esperado». `SE-508` completa el catálogo.

#### SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos

Red, recursos, dependencias, reloj, discos y procesos no producen lo mismo. La clase lee la huella de seis fallas en cuatro señales, calcula los rechazos por desfase de reloj y compara el registro síncrono y asíncrono ante una parada de disco.

El estudiante entrega un catálogo de fallas por mecanismo con su señal. `SE-509` elige con qué se inyectan.

#### SE-509 — Caos en Kubernetes y en plataformas cloud

La herramienta se elige por la capa en que actúa y por sus controles. La clase mide con sockets reales un proxy que añade latencia, reinicia o calla, y compara Toxiproxy, Chaos Mesh, LitmusChaos, AWS Fault Injection Service, Azure Chaos Studio y las herramientas históricas de Netflix a partir de su documentación.

El estudiante entrega una tabla falla → capa → herramienta → control de seguridad. `SE-510` lleva el método a los datos.

#### SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción

En los datos, la falla más dañina no hace ruido. La clase calcula las escrituras confirmadas perdidas al conmutar, las lecturas obsoletas según el retraso y la degradación de un modelo con características ausentes, obsoletas o sustituidas por una regla.

El estudiante entrega un catálogo de fallas de datos con señales de integridad. `SE-511` ejercita la respuesta con personas.

### Bloque 3 — Practicar y automatizar

#### SE-511 — Game days y ejercicios de respuesta a incidentes

Los defectos de personas y procedimientos solo los ve un ejercicio con personas. La clase diseña un día de práctica con roles, reglas y aborto, y compara cuatro programas por defectos latentes (12,6 sin práctica, 1,1 con un día por trimestre).

El estudiante entrega el plan de un día de práctica y un calendario. `SE-512` automatiza lo técnico.

#### SE-512 — Caos continuo: automatización en CI/CD y en producción

Una protección que se retira sin que ninguna prueba falle no estaba protegida. La clase mide qué regresiones de siete cambios detectan una lectura estática (5 de 6) y una suite de escenarios (3 de 6), las falsas alarmas y las regresiones tapadas, y sitúa los experimentos continuos en producción.

El estudiante entrega una etapa de resiliencia del pipeline con la lista de lo que no ve. `SE-513` gobierna la práctica.

### Bloque 4 — Gobernar y aprender

#### SE-513 — Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar

Los experimentos se pagan con el presupuesto de las personas usuarias. La clase mide el efecto de un calendario fijo (38,6 % de meses incumplidos frente a 16,2 %), quién carga con el daño al elegir por petición o por cliente, y propone una compuerta de decisión y una política de permisos.

El estudiante entrega una política y una compuerta. `SE-514` mide qué se aprende de un experimento.

#### SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora

Un control declarado no es un control comprobado, y un experimento solo enseña lo que sus ensayos sostienen. La clase calcula cuántos ensayos hacen falta para sostener una tasa de fallas, clasifica controles con distinto número de ensayos y mide la exposición tras una revocación según la caché.

El estudiante entrega criterios de aceptación con ensayos y tolerancia. `SE-515` los aplica en un taller.

### Bloque 5 — Aplicar e integrar

#### SE-515 — Taller: ejecutar un experimento de caos acotado con criterio de aborto

La producción cambia lo que se aprende y lo que se arriesga. El taller calcula la carga tras evacuar una región, muestra el umbral que solo cruza un experimento concentrado, ejecuta la comparación con un control y separa lo documentado del caso de Netflix de lo que no debe generalizarse.

El estudiante entrega un experimento acotado con precondiciones, aborto y evidencia. `SE-516` lo integra.

#### SE-516 — Proyecto: programa de caos de un servicio con evidencia y remediación

Un programa es un sistema con dueños, calendario, presupuesto y registro. La clase mide qué detecta un validador de especificaciones frente a 360 mutaciones (252) y qué ninguno ve, ejecuta el ciclo con control y huella y entrega un paquete reproducible con su plan de remediación.

El estudiante entrega el paquete con catálogo, especificaciones, política, validador, resultados con huella, remediación y límites.

## Resumen operativo del recorrido

| Clase | Núcleo profesional | Aporte acumulativo |
|---|---|---|
| [SE-505](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/) | Principios de la ingeniería del caos: estado estable e hipótesis | Entrega una hipótesis con métrica, ventana, banda y regla de refutación |
| [SE-506](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/) | Diseñar experimentos de fallo: alcance y radio de impacto | Entrega la especificación de un experimento con radio, aborto y reversión |
| [SE-507](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/) | Inyección de fallos de red, latencia y dependencias | Entrega una tabla mecanismo declarado → falla → resultado esperado |
| [SE-508](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/) | Fallos de recursos e infraestructura: CPU, memoria, disco y nodos | Entrega un catálogo de fallas por mecanismo con su señal |
| [SE-509](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/) | Caos en Kubernetes y en plataformas cloud | Entrega una tabla falla → capa → herramienta → control de seguridad |
| [SE-510](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/) | Fallos de datos y de estado: réplicas, particiones y corrupción | Entrega un catálogo de fallas de datos con señales de integridad |
| [SE-511](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/) | Game days y ejercicios de respuesta a incidentes | Entrega el plan de un día de práctica y un calendario |
| [SE-512](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/) | Caos continuo: automatización en CI/CD y en producción | Entrega una etapa de resiliencia del pipeline con la lista de lo que no ve |
| [SE-513](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/) | Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar | Entrega una política de presupuesto, selección y permisos con una compuerta de decisión |
| [SE-514](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/) | Aprender de los experimentos: hallazgos, métricas y mejora | Entrega criterios de aceptación con ensayos, tolerancia y evidencia |
| [SE-515](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/) | Taller: ejecutar un experimento de caos acotado con criterio de aborto | Entrega un experimento acotado con precondiciones, aborto y evidencia |
| [SE-516](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/) | Proyecto: programa de caos de un servicio con evidencia y remediación | Entrega un programa con validador, huella, remediación e informe de límites |
