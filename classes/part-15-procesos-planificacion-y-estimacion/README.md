# Parte 15 — Procesos, planificación y estimación

La Parte 14 terminó con un prototipo evaluado con personas. La pregunta cambia de «qué se construye» a «cómo se organiza el trabajo, qué se promete y cómo se sabe a tiempo que el plan dejó de valer». Esta parte trabaja sobre el **plan de lanzamiento de la plataforma de entregas de tareas**, un caso sintético: la recuperación de borradores y la regla de penalización de las Partes 12 y 13 son el trabajo pendiente. Recorre un modelo de proceso por bloque, los principios que sostienen un ciclo corto, cuatro marcos leídos por sus políticas, la teoría de colas que explica la espera, estimaciones con rango, redes con dependencias, registros de riesgos y decisiones, puertas de listo y terminado, métricas con contrapesos, retrospectivas con capacidad limitada y un plan adaptativo con disparadores y barreras.

## Pregunta rectora

> ¿Qué incertidumbre, dependencia o cuello de botella condiciona la siguiente entrega y qué señal me avisaría a tiempo?

## Antes del recorrido clase por clase

Esta parte no enseña un marco. Enseña a elegir el modelo de proceso por la volatilidad de lo que se construye, a distinguir una práctica de su efecto, a describir un marco por sus políticas de entrada, compromiso y recorte, a explicar la espera con utilización, variabilidad y lotes, a comunicar una estimación como rango con su cobertura real, a calcular el plazo de una red con dependencias, a separar riesgos, supuestos, issues y decisiones, a diseñar puertas cuyas comprobaciones vean defectos distintos, a medir sin premiar la métrica, a acordar solo las mejoras que caben en la capacidad, a calibrar un pronóstico y a replanificar con reglas. Cada clase ejecuta simulaciones con datos sintéticos que muestran un mecanismo (un intervalo de retroalimentación de menor esfuerzo, una espera que se multiplica por diecinueve, un percentil 85 que se cumple dos de cada tres veces) y declara lo que ese experimento no demuestra.

```mermaid
flowchart LR
    A[Volatilidad y riesgo] --> B[Modelo y principios]
    B --> C[Políticas de los marcos]
    C --> D[Flujo y colas]
    D --> E[Estimación con rango]
    E --> F[Dependencias y entrega]
    F --> G[Riesgos y decisiones]
    G --> H[Puertas de calidad]
    H --> I[Métricas con contrapesos]
    I --> J[Mejora del sistema]
    J --> K[Plan adaptativo]
    K -->|evidencia nueva| A
```

El diagrama se lee de izquierda a derecha y no es un proceso obligatorio. El retorno indica que la evidencia de una entrega cambia la volatilidad y el riesgo con que se planifica la siguiente; un plan aprobado no cierra el trabajo, lo fecha.

## Resultados acumulativos

Podrás elegir el intervalo de retroalimentación de menor esfuerzo y localizar el cruce entre un plan predictivo y ciclos cortos; relacionar cada práctica con la decisión que cambia y el sobrecoste que impone; describir Scrum, Kanban, XP y Shape Up por sus políticas y medir la espera de un urgente y la tasa de fallo de una regla de compromiso; explicar con la ley de Little y con colas por qué el plazo crece con el trabajo en curso, la utilización, la variabilidad y los lotes; comunicar una estimación como rango y comprobar su cobertura; calcular el plazo de una red con dependencias propias y externas; separar riesgos con causas comunes de supuestos, issues y decisiones; elegir comprobaciones que no se solapen; resumir tiempos con percentiles y detectar una métrica premiada; limitar las acciones de mejora a la capacidad y evaluar un cambio con su potencia; calibrar un pronóstico y comparar márgenes con un colchón; y entregar un plan adaptativo con un disparador cuyo costo conoces y barreras con responsable.

Al finalizar podrás defender un plan con sus rangos, sus supuestos, sus señales, sus reglas de replanificación, sus barreras y una lista de lo que ninguna simulación ni verificador ve, y podrás indicar qué parte de tu conclusión es observación, cuál es inferencia y cuál es suposición.

## Prerrequisitos enlazados

- [Parte 4 — Pensamiento computacional](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/): modelado y razonamiento sobre evidencia.
- [Parte 7 — Estructuras de datos y algoritmos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/): medir, comparar y no confundir un resultado con un modelo.
- [Parte 11 — Economía, métricas y decisiones de producto](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-11-economia-metricas-y-decisiones-de-producto/): valor, costo de decisión y métricas con contrapesos.
- [Parte 12 — Ingeniería de requisitos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-12-ingenieria-de-requisitos/): requisitos y criterios que esta parte convierte en trabajo planificado.
- [Parte 13 — Especificaciones, contratos y modelos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-13-especificaciones-contratos-y-modelos/): ejemplos y contratos que las puertas de calidad comprueban.
- Python 3.11+ y terminal; los experimentos usan solo la biblioteca estándar y datos sintéticos.

## Bloques y progresión

1. **Elegir el modelo y los principios:** las clases 181–183 comparan modelos de proceso, separan principios de ceremonias y leen cuatro marcos por sus políticas.
2. **Entender el flujo:** la clase 184 explica la espera con la ley de Little, la utilización, la variabilidad y los límites de trabajo.
3. **Estimar y planificar:** las clases 185–186 estiman con rangos y evidencia histórica y planifican entregas con dependencias.
4. **Gestionar la incertidumbre y la calidad del proceso:** las clases 187–189 registran riesgos y decisiones, fijan puertas de listo y terminado y miden con contrapesos.
5. **Mejorar, planificar e integrar:** las clases 190–192 mejoran el sistema con capacidad limitada, planifican con incertidumbre explícita y entregan un plan adaptativo.

## Evidencia medida y límites

Las figuras y los ejemplos de esta parte usan simulaciones ejecutadas con CPython 3.12.9 en Windows 11 y repetidas con CPython 3.12.3 en Ubuntu bajo WSL2. Los datos son **sintéticos** y las semillas están fijadas: las salidas de los doce experimentos fueron idénticas en ambos sistemas, sin excepción, porque ninguno mide tiempos de ejecución ni depende de la versión de una biblioteca externa. Todo el código usa solo la biblioteca estándar.

Los experimentos son: esfuerzo total de 40 piezas según el intervalo de retroalimentación, valor entregado si el proyecto se corta al azar y cruce entre un plan predictivo y ciclos cortos según la volatilidad (`SE-181`); valor no entregado según la frecuencia con que se aprende del uso, sobrecoste de las ceremonias según la duración del ciclo y conflictos de fusión según la vida de una rama (`SE-182`); espera de un urgente de dos días con tres políticas de entrada, cinco reglas para comprometer elementos en un sprint y tiempo fijo frente a alcance fijo (`SE-183`); una cola de un servidor frente a su fórmula, la ley de Little en un tablero con límite de trabajo y variabilidad y lotes frente a la aproximación de Kingman (`SE-184`); probabilidad de cumplir la suma de medianas de 30 tareas, cobertura de un intervalo del 80 % según las semanas de historia y solape entre tallas (`SE-185`); convergencia de caminos en redes de cinco capas, dependencias externas que llegan tarde y cuatro órdenes de entrega (`SE-186`); diez riesgos con y sin causa común, orden de validación de doce supuestos y un verificador de registros de decisión con 200 mutaciones (`SE-187`); comprobaciones correlacionadas de una definición de terminado, plazo según los días de refinamiento y un verificador de criterios de aceptación con casos nuevos (`SE-188`); resumen de tiempos con cola larga, una velocidad premiada que se infla y el error de un percentil según la muestra (`SE-189`); acciones terminadas según las acordadas, potencia y falsas mejoras de una prueba de rangos y cinco intervenciones sobre una cola (`SE-190`); calibración de pronósticos de fecha, margen por tarea frente a colchón compartido y sensibilidad de un plan (`SE-191`); y reglas de replanificación con sus falsas alarmas, un validador de planes con 200 mutaciones y mil proyectos con tres estrategias (`SE-192`).

Los parámetros (el 25 % de malentendidos y el 15 % de piezas afectadas, el rendimiento normal de media 10 y desviación 3, los tiempos lognormales y los rendimientos gamma, las redes aleatorias de cinco capas, los diez riesgos con una causa común del 25 %, la «dificultad» de un defecto como número entre 0 y 1, la inflación de estimaciones del 4 % por sprint, la capacidad de mejora de 2 días, la regla de expansión del trabajo y la caída del rendimiento en la mitad de los proyectos) son supuestos del autor, no datos de un producto, una institución ni de personas reales. Las reglas léxicas de los tres verificadores se ajustaron con los mismos casos que las evalúan, o con ocho casos nuevos mínimos en el de criterios de aceptación: su exactitud real es desconocida. No se usó ninguna herramienta de gestión de proyectos ni de planificación de producción, no se observó ningún equipo, no se entrevistó a nadie y no se midió ninguna retrospectiva, estimación ni métrica real. Esta parte no tiene laboratorio propio en `labs/`; el proyecto integrador `SE-192` define el plan y la evidencia. Cada clase termina con un puente hacia el trabajo con agentes.

## Guía razonada clase por clase

La plataforma de entregas mantiene un plan, un tablero y un registro estables mientras cambian las decisiones. Cada clase explica qué incertidumbre reduce, qué simulación la muestra, qué no demuestra y qué evidencia permite abandonar la conclusión.

### Bloque 1 — Elegir el modelo y los principios

#### SE-181 — Modelos predictivos, iterativos e incrementales

El modelo de proceso se elige por la volatilidad de lo que se construye y por el coste de cambiar. La clase mide cómo cambia el esfuerzo total al variar el intervalo de retroalimentación, qué valor existe si el proyecto se corta y dónde se cruzan un plan predictivo y los ciclos cortos.

El estudiante asigna un modelo a cada bloque del lanzamiento con su riesgo y su señal de cambio. `SE-182` pregunta qué hace que un ciclo corto sirva de algo.

#### SE-182 — Agile como principios y no como ceremonia

Una práctica vale por la decisión que cambia. La clase mide cuánto valor se pierde por no aprender del uso real, cuánto cuestan las ceremonias según la duración del ciclo y cómo crece la probabilidad de conflicto de integración con la vida de una rama.

El estudiante entrega la tabla de prácticas con su decisión y su señal. `SE-183` aplica el criterio a cuatro marcos.

#### SE-183 — Scrum, Kanban, XP y Shape Up

Cada marco es una combinación de políticas de entrada, compromiso y recorte. La clase mide la espera de un trabajo urgente con tres políticas, la tasa de fallo de cinco reglas de compromiso y lo que ocurre cuando se fija el tiempo y se deja variar el alcance.

El estudiante escribe las tres políticas de su equipo y la combinación elegida. `SE-184` explica por qué esas políticas tienen esos efectos.

### Bloque 2 — Entender el flujo

#### SE-184 — Lean, teoría de colas y límites de trabajo

La espera crece de forma explosiva con la utilización y depende de la variabilidad y de los lotes. La clase compara una cola simulada con su fórmula, verifica la ley de Little en un tablero con límite de trabajo y mide cuánto añaden la variabilidad y los lotes con la misma carga.

El estudiante entrega la medición de su flujo y un límite de trabajo justificado. `SE-185` usa esos datos como historia para estimar.

### Bloque 3 — Estimar y planificar

#### SE-185 — Estimación por tamaño, rango y evidencia histórica

La suma de las estimaciones típicas no es la estimación típica del total. La clase calcula con qué frecuencia se cumple la suma de medianas, cuánto cubre realmente un intervalo del 80 % según la historia y cuánto se solapan las tallas.

El estudiante comunica una estimación como rango con confianza, historia y supuestos. `SE-186` combina varias estimaciones en una red.

#### SE-186 — Planificación de entregas y gestión de dependencias

Con dependencias, el total se parece a un máximo. La clase mide la convergencia de caminos en redes anchas, la probabilidad de que lleguen a tiempo varias dependencias externas y el valor que entregan cuatro órdenes de trabajo.

El estudiante entrega la red de la entrega con su plazo en forma de rango y sus dependencias con fecha de aviso. `SE-187` convierte esas incertidumbres en registros.

### Bloque 4 — Gestionar la incertidumbre y la calidad del proceso

#### SE-187 — Riesgos, supuestos, issues y decisiones

Un plan mezcla cuatro cosas que merecen registros distintos. La clase mide qué esconde la exposición esperada cuando los riesgos comparten causa, cuánto cuesta descubrir tarde un supuesto según el orden de validación y qué ve y qué no un verificador de registros de decisión.

El estudiante entrega los cuatro registros del plan con responsable y disparador. `SE-188` fija las puertas por las que pasa el trabajo.

#### SE-188 — Definition of Ready, Done y aceptación

Las puertas del proceso se justifican por los escapes que evitan y por lo que cuestan. La clase mide cuántos defectos se escapan según el número y la correlación de las comprobaciones, cuánto retrasa el refinamiento previo y qué atrapa un verificador de criterios.

El estudiante entrega las definiciones por tipo de trabajo con el escape que justifica cada casilla. `SE-189` mide lo que ocurre al cruzarlas.

#### SE-189 — Métricas de flujo, calidad y resultados

Una métrica informa una decisión o se infla. La clase compara los resúmenes de un tiempo con cola larga, simula una velocidad premiada y mide cuánto varía un percentil según el tamaño de la muestra.

El estudiante entrega un tablero de cinco números con su decisión y su contrapeso. `SE-190` usa el tablero para decidir qué mejorar.

### Bloque 5 — Mejorar, planificar e integrar

#### SE-190 — Retrospectivas y mejora del sistema de trabajo

La capacidad de mejora limita lo que se termina y los datos limitan lo que se concluye. La clase mide cuántas acciones se terminan según las acordadas, con qué frecuencia una prueba detecta una mejora real y declara una falsa, y qué intervenciones mueven una cola.

El estudiante entrega una acción con hipótesis, señal, duración y criterio de abandono. `SE-191` integra todo en un taller.

#### SE-191 — Taller: planificar bajo incertidumbre explícita

Un pronóstico probabilístico solo vale si está calibrado. El taller comprueba la cobertura real de pronósticos de fecha, compara un margen por tarea con un colchón compartido y ordena los supuestos de un plan por sensibilidad.

El estudiante entrega un plan comunicado como distribución con tres supuestos vigilados. `SE-192` lo convierte en un plan adaptativo.

#### SE-192 — Proyecto: plan adaptativo con evidencia y guardrails

Toda regla de replanificación intercambia falsas alarmas por retraso. El proyecto mide seis reglas, valida un plan con 200 mutaciones y separa en mil proyectos el efecto de ordenar por valor del de prometer menos. La Parte 16 pasa a cómo se colabora sobre el código con Git.

El estudiante entrega el plan, la regla elegida con su costo, las barreras con su comprobación y la lista de lo que no ve el validador.

## Resumen operativo del recorrido

| Clase | Capacidad que construye | Pregunta que resuelve | Evidencia acumulativa |
|---|---|---|---|
| [SE-181](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/) | Modelos predictivos, iterativos e incrementales | ¿Cada cuánto necesito saber si construyo lo correcto? | `model-log.md` con intervalo, corte y cruce |
| [SE-182](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/) | Agile como principios y no como ceremonia | ¿Qué práctica cambia una decisión y cuál es ritual? | `agile-log.md` con prácticas y ciclo |
| [SE-183](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/) | Scrum, Kanban, XP y Shape Up | ¿Qué política explica la espera y el fallo que observo? | `frameworks-log.md` con tres políticas |
| [SE-184](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/) | Lean, teoría de colas y límites de trabajo | ¿Qué determina cuánto espera un elemento? | `flow-log.md` con Little y límite |
| [SE-185](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/) | Estimación por tamaño, rango y evidencia | ¿Qué rango es creíble con la evidencia que tengo? | `estimation-log.md` con rango y cobertura |
| [SE-186](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/) | Planificación de entregas y dependencias | ¿Qué caminos y dependencias fijan la fecha? | `release-plan-log.md` con red y orden |
| [SE-187](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/) | Riesgos, supuestos, issues y decisiones | ¿Qué puede salir mal y quién lo mira? | `risk-log.md` con cuatro registros |
| [SE-188](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/) | Definition of Ready, Done y aceptación | ¿Qué riesgo evita cada puerta y qué cuesta? | `gates-log.md` con puertas por tipo |
| [SE-189](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/) | Métricas de flujo, calidad y resultados | ¿Qué decisión informa cada número? | `metrics-log.md` con tablero y contrapesos |
| [SE-190](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/) | Retrospectivas y mejora del sistema | ¿Qué cambio probaré y cómo sabré si funcionó? | `retro-log.md` con acción y criterio |
| [SE-191](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/) | Taller: planificar bajo incertidumbre | ¿Está calibrado mi pronóstico y qué supuesto vigilo? | `workshop-log.md` con calibración y sensibilidad |
| [SE-192](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/) | Proyecto: plan adaptativo con guardrails | ¿Qué regla me avisa a tiempo sin cambiar el plan por ruido? | `plan-log.md`, validador, regla y barreras |

## Proyecto integrador

El proyecto **SE-192** entrega un plan adaptativo con objetivo, supuestos con responsable y fecha, rangos con confianza calibrados, disparadores con señal, umbral, ventana y responsable, barreras con comprobación, métricas con definición y fecha de revisión, además de la simulación que muestra el costo de la regla elegida y la separación entre ordenar por valor y prometer menos. Se acompaña de los límites declarados: qué cambios de sentido no detecta el validador y qué parte del plan no se comprobó con proyectos reales.

## Criterios de salida

- las doce clases explican todos sus temas mediante mecanismos, ejemplos y límites;
- cada estimación del plan es un rango con confianza, historia y supuestos, y su cobertura se ha comprobado;
- las probabilidades, los porcentajes y los parámetros son declarados como supuestos y nunca como mediciones de un equipo;
- cada puerta del proceso tiene un escape que la justifica y cada métrica una decisión y un contrapeso;
- la regla de replanificación declara su tasa de falsas alarmas y su retraso, y las barreras tienen comprobación y responsable;
- otra persona reproduce comandos y resultados desde un checkout limpio;
- el informe declara lo observado, lo inferido y lo no ejecutado.

## Preguntas de control por bloque

- ¿Con qué volatilidad y qué coste de cambiar elijo un plan único o ciclos cortos?
- ¿Qué decisión cambia esta práctica y qué política explica esta espera?
- ¿Qué rango, con qué confianza y con qué historia, y cuánto se cumpliría de verdad?
- ¿Qué dependencia o causa común puede mover la fecha entera?
- ¿Qué parte del plan depende de que una persona lea el sentido y no de una comprobación?

## Fuentes de la parte

- [Boehm, «A spiral model of software development and enhancement» (IEEE Computer, 1988)](https://doi.org/10.1109/2.59) — modelo de proceso guiado por riesgo; autoridad: IEEE Computer.
- [Larman y Basili, «Iterative and incremental developments: a brief history» (IEEE Computer, 2003)](https://doi.org/10.1109/MC.2003.1204375) — historia de las prácticas iterativas e incrementales; autoridad: IEEE Computer.
- [Manifiesto por el Desarrollo Ágil de Software](https://agilemanifesto.org/) — valores y principios; autoridad: autores del manifiesto.
- [The Scrum Guide](https://scrumguides.org/scrum-guide.html) — definición de Scrum; autoridad: Scrum.org y Scrum Inc. (autores de la guía).
- [The Kanban Guide](https://kanbanguides.org/english/) — definición de Kanban y límites de trabajo; autoridad: Scrum.org (Kanban Guide).
- [Little, «A proof for the queuing formula: L = λW» (Operations Research, 1961)](https://doi.org/10.1287/opre.9.3.383) — ley de Little; autoridad: Operations Research.
- [Kingman, «The single server queue in heavy traffic» (1961)](https://doi.org/10.1017/S0305004100036094) — espera con carga alta; autoridad: Math. Proc. Cambridge Philos. Soc.
- [Flyvbjerg, «From Nobel Prize to project management: getting risks right» (Project Management Journal, 2006)](https://doi.org/10.1177/875697280603700302) — optimismo en la planificación y clases de referencia; autoridad: Project Management Journal.
- [Malcolm et al., «Application of a technique for research and development program evaluation» (Operations Research, 1959)](https://doi.org/10.1287/opre.7.5.646) — PERT y redes con duraciones inciertas; autoridad: Operations Research.
- [Boehm, «Software risk management: principles and practices» (IEEE Software, 1991)](https://doi.org/10.1109/52.62930) — gestión de riesgos de proyecto; autoridad: IEEE Software.
- [DORA: investigación](https://dora.dev/research/) — métricas de entrega y estabilidad; autoridad: DORA (Google Cloud).
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — gestión de ingeniería de software; autoridad: IEEE Computer Society.

Las fuentes se vinculan también dentro de cada clase. Definen vocabulario y mecanismos; la adecuación de las decisiones de la plataforma de entregas se demuestra con el caso, la evidencia trazable y la revisión de otra persona, no con la autoridad de la fuente.
