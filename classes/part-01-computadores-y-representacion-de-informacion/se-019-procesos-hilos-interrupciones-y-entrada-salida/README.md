# SE-019 — Procesos, hilos, interrupciones y entrada/salida

[← SE-018](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) · [↑ Parte 01](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-01-computadores-y-representacion-de-informacion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [SE-020 →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md)

> Estado: **PLANNED** · Borrador público conservado íntegramente y sometido a auditoría técnica y pedagógica.

## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para atribuir concurrencia y espera a procesos, hilos, interrupciones e I/O según su mecanismo.

**Por qué aparece aquí.** Se sitúa después de **Memoria, cachés, almacenamiento y jerarquías** y antes de **Compilación, interpretación, bytecode y JIT**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Inferir paralelismo de CPU porque dos hilos se solapan.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Concurrency-observation.md con cronología, tiempos de pared/CPU e hipótesis descartadas. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** Scheduler, GIL y primitivas dependen de plataforma e implementación.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [Python `threading`](https://docs.python.org/3/library/threading.html) |  define hilos y restricciones de CPython | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [Python `time`](https://docs.python.org/3/library/time.html) |  define relojes de pared y proceso | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [RISC-V Privileged Architecture](https://docs.riscv.org/reference/isa/priv/) |  contextualiza interrupciones y niveles privilegiados | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

`SE-018` mostró que acceder a datos tiene jerarquías. Ahora el analizador local de eventos lee, calcula y escribe
mientras el sistema comparte CPU y dispositivos con otros programas. Modelarás proceso,
hilo, llamada al sistema e interrupción sin tratarlos como sinónimos de programa o CPU.

## Prerrequisitos

Estado e instrucciones de `SE-017`, jerarquía de `SE-018`, Python 3.11+.

## Problema auténtico

Una aplicación “usa varios hilos” y se espera que tarde la mitad. La carga es CPU-bound,
comparte estado y corre en un runtime con restricciones. Concurrencia fue confundida con paralelismo y rendimiento.

## Objetivos observables

Distinguirás programa, proceso e hilo; explicarás planificación y cambio de contexto;
seguirás una llamada de I/O; relacionarás interrupciones con eventos; compararás bloqueo y concurrencia.

## Temas y por qué importan

| Tema | Mecanismo | Por qué importa |
| --- | --- | --- |
| Proceso | aísla espacio y recursos | contiene fallos y propiedad |
| Hilo | comparte proceso y mantiene ejecución | habilita concurrencia con riesgos |
| Planificación | asigna CPU a unidades listas | explica pausas y competencia |
| I/O e interrupción | coordinan dispositivos y software | separan espera de cálculo |
## Mapa conceptual

```mermaid
flowchart LR
 P[el analizador local de eventos solicita lectura] --> K[Sistema operativo valida y programa I/O]
 K --> D[Dispositivo inicia la operación]
 D --> I[Interrupción o señal de completado]
 I --> R[Kernel despierta el hilo bloqueado]
 R --> P2[el analizador local de eventos recibe los datos]
```

El sistema real puede usar polling, DMA, buffers y completado asíncrono. La secuencia
muestra responsabilidades, no cada transición de hardware.

## Conceptos y decisiones

### 1. Programa es descripción; proceso es ejecución aislada

Un archivo de programa puede originar múltiples procesos. Cada proceso posee espacio de
direcciones virtual, identificador, recursos y estado administrado por el sistema. El
aislamiento limita acceso accidental, pero no es una frontera de seguridad absoluta sin permisos y controles.

### 2. Los hilos comparten y por eso coordinan

Hilos de un proceso comparten memoria y recursos, pero mantienen pila y estado de
ejecución propios. Compartir reduce copia y permite trabajo concurrente; introduce
carreras, orden y necesidad de sincronización. Más hilos agregan overhead y no crean núcleos.

### 3. Concurrencia y paralelismo responden preguntas distintas

Concurrencia organiza tareas que progresan en intervalos superpuestos. Paralelismo
ejecuta simultáneamente. I/O concurrente puede aprovechar esperas en un núcleo; cálculo
paralelo requiere capacidad y runtime apropiados. La métrica debe distinguir latencia de una tarea y throughput total.

### 4. Planificación produce pausas legítimas

El sistema decide qué hilo listo usa CPU. Un cambio de contexto conserva estado y carga
otro; tiene costo y efectos de caché. Tiempo de pared incluye ejecución, espera y
desplanificación. Tiempo de CPU aproxima trabajo ejecutado por el proceso, no espera externa.

### 5. I/O cruza una frontera protegida

El programa solicita operaciones mediante APIs que llegan a llamadas del sistema. El
kernel valida y coordina controladores. Dispositivos pueden avisar completado mediante
interrupciones; DMA puede mover datos sin que la CPU copie cada byte. Una llamada
bloqueante suspende al hilo hasta una condición, no necesariamente ocupa CPU todo el tiempo.

## Caso conductor: leer y resumir eventos

El analizador local de eventos lee un archivo pequeño, calcula y escribe. Se registran tiempo de pared y CPU. Una
versión con dos hilos procesa dos archivos sintéticos; el objetivo no es ganar, sino
explicar qué trabajo se solapa, qué estado se comparte y qué medición refutaría la ventaja.

## Definiciones de trabajo

- **proceso:** instancia de ejecución con recursos aislados;
- **hilo:** secuencia planificable dentro de un proceso;
- **concurrencia:** composición de progresos superpuestos;
- **interrupción:** señal que desvía control para atender un evento;
- **I/O bloqueante:** operación que suspende la unidad llamante hasta progreso.

## Glosario

**Context switch** cambia unidad ejecutada. **Syscall** solicita servicio al kernel.
**DMA** permite transferencias de dispositivo a memoria con intervención acotada de CPU.

## Ejemplo mínimo

`time.sleep()` aumenta tiempo de pared casi sin aumentar CPU: el hilo espera. Un bucle
numérico aumenta ambos y añadir hilos de CPython no garantiza paralelismo de bytecode.

## Ejemplo profesional

Un servidor atiende muchas conexiones con I/O asíncrono para evitar un hilo bloqueado
por conexión. Si el cuello es cálculo, se consideran procesos o trabajo vectorizado, siempre midiendo costos de coordinación.

## Práctica guiada

1. Crea dos archivos sintéticos y una versión secuencial del analizador local de eventos.
2. Mide `perf_counter` y `process_time` en lectura y cálculo por separado.
3. Implementa dos hilos solo para las lecturas y registra timeline.
4. Protege un contador compartido o evita compartir mediante resultados separados.
5. Repite, cambia tamaño y registra causas alternativas.
6. Entrega `io_probe.py`, `timeline.md`, `samples.csv`.

## Ejercicios

1. Clasifica cuatro estados: ejecutando, listo, bloqueado y terminado.
2. Da un caso concurrente no paralelo.
3. Explica por qué una interrupción no es un hilo de aplicación.

## Reto verificable

Otra persona reconstruye cuándo el analizador local de eventos calcula, espera y es planificable. Aprueba si la
línea temporal no atribuye tiempo de pared completo a CPU.

## Preguntas frecuentes

### ¿Un proceso tiene un solo hilo?
Puede comenzar con uno y crear más; el modelo depende del sistema y runtime.

### ¿Asíncrono siempre es más rápido?
No. Mejora composición de esperas en ciertos contextos y añade complejidad.

## Fallo controlado y diagnóstico

Actualiza un contador compartido desde hilos sin contrato. Si el fallo no aparece, no
concluyas seguridad; explica por qué una carrera depende de intercalado y diseña sincronización o eliminación del estado compartido.

## Errores comunes y cómo corregirlos

| Síntoma | Causa | Corrección |
| --- | --- | --- |
| programa = proceso | archivo confundido con ejecución | distingue descripción e instancia |
| hilos duplican velocidad | concurrencia = paralelismo | identifica carga, núcleos y runtime |
| tiempo de pared = CPU | esperas ignoradas | mide pared y CPU por separado |
| interrupción = excepción de lenguaje | niveles mezclados | ubica señal de hardware/kernel y manejo de runtime |

## Entorno y archivos clave

Python 3.11+, `threading`, `time`, `pathlib`; archivos sintéticos menores de 10 MB. Limpieza explícita del directorio.

## Seguridad, ética y accesibilidad

Limita carga y tamaño. No inspecciones procesos ajenos. Presenta timeline textual además del diagrama.

## Transferencia

Compara threads, procesos y async para un servidor de archivos; identifica propiedad de memoria.

## Evaluación y evidencia

Se exigen timeline, dos relojes, estado compartido explícito y conclusión condicionada.

## Fuentes


- [Python `threading`](https://docs.python.org/3/library/threading.html) define hilos y restricciones de CPython.
- [Python `time`](https://docs.python.org/3/library/time.html) define relojes de pared y proceso.
- [RISC-V Privileged Architecture](https://docs.riscv.org/reference/isa/priv/) contextualiza interrupciones y niveles privilegiados.

## Límites y siguiente paso

No administra servicios ni señales del SO; eso corresponde a la Parte 02. `SE-020` abre la traducción del programa.

---
[← SE-018](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) · [↑ Parte 01](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-01-computadores-y-representacion-de-informacion/README.md) · [SE-020 →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md)
