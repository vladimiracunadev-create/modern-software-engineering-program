# ⚙️ Systems Programmer
<!-- role-visual:start -->
<div align="center">

[![Familia](https://img.shields.io/badge/familia-Ingenier%C3%ADa%20general-6f42c1?style=for-the-badge)](README.md)
[![Nivel](https://img.shields.io/badge/recorrido-semi--senior%20%E2%86%92%20principal-0969da?style=for-the-badge)](../ROADMAP.md)
[![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-P01%20%C2%B7%20P02%20%C2%B7%20P06%20%C2%B7%20P23%20%C2%B7%20P26%20%C2%B7%20P28%20%C2%B7%20P32%20%C2%B7%20P36%20%C2%B7%20P37-2da44e?style=for-the-badge)](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>
<!-- role-visual:end -->


> Construye software cercano al sistema operativo y al runtime con control explícito
> de memoria, concurrencia, recursos, interfaces y portabilidad.
>
> **Entrada habitual:** semi-senior · **Foco:** runtimes, procesos y rendimiento
> · **Evidencia central:** componente medido con invariantes y fallos de recursos probados

## 🧭 Qué es y por qué importa

Systems programming crea runtimes, motores, drivers, bases de datos, herramientas y
componentes donde una abstracción insuficiente se convierte en corrupción, deadlock o
degradación. Exige razonar desde hardware y sistema operativo hasta API pública.

## 🗓️ Un día en el puesto

- depurar memoria, syscall, bloqueo o carrera;
- perfilar CPU, caché e I/O;
- diseñar una interfaz estable y manejo de recursos;
- revisar comportamiento indefinido y portabilidad;
- ejecutar fuzzing, sanitizers y benchmarks.

## ✅ Responsabilidades y límites

- Responde por seguridad de memoria, recursos y semántica de concurrencia.
- Elige C, C++, Rust u otra herramienta por restricciones verificadas.
- No usa bajo nivel como sinónimo de rendimiento sin medir.
- No expone primitivas peligrosas sin contrato y encapsulación.

## 🧠 Qué necesitas saber

Arquitectura de computador, memoria, procesos, syscalls, compilación, linking,
ABI, concurrencia, estructuras de datos, redes, archivos, debugging, profiling,
property testing, fuzzing, portabilidad y reproducible builds.

## 📚 Tu ruta en el programa

1. [Parte 01 — Computadores y representación](../classes/part-01-computadores-y-representacion-de-informacion/README.md) y partes 02–09 como núcleo de máquina, programación y herramientas.
2. Partes 18 y 22 para servicios, automatización y embedded.
3. Partes 25, 29 y 32 para diseño, almacenamiento y concurrencia.
4. Partes 35–36 y 38–39 para pruebas, resiliencia, seguridad y build.

<!-- role-depth:start -->
## 🗺️ Sistema profesional del rol

```mermaid
flowchart LR
    A["🎯 Modelo de máquina"] --> B
    B["🧠 Recursos"] --> C
    C["🛠️ Concurrencia"] --> D
    D["🔎 Medición"] --> E["📈 Recuperación"]
    classDef intent fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef work fill:#ddf4ff,stroke:#0969da,color:#24292f
    classDef proof fill:#dafbe1,stroke:#1a7f37,color:#24292f
    class A intent
    class B,C,D work
    class E proof
```

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **⚙️ Systems Programmer**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: Construye software cercano al sistema operativo y al runtime con control explícito de memoria, concurrencia, recursos, interfaces y portabilidad. Cada transición
debe conservar supuestos, responsables y una forma de volver atrás.

<table>
<tr>
<td valign="top" width="50%">

### 🎯 Responde por

- decisiones propias de la familia **Ingeniería general**;
- el resultado observable, no sólo la actividad ejecutada;
- límites, riesgos, operación y deuda residual de su intervención;
- evidencia que otra persona pueda revisar o reproducir.

</td>
<td valign="top" width="50%">

### 🤝 Coordina con

- [⏱️ Performance Engineer](performance-engineer.md); [🔌 Embedded & IoT Engineer](embedded-iot-engineer.md); [🌐 Distributed Systems Engineer](distributed-systems-engineer.md); [🧮 Runtime & Systems Engineer](runtime-systems-engineer.md);
- producto y personas usuarias cuando cambia una tarea o outcome;
- seguridad, privacidad, accesibilidad y operación según el riesgo;
- quienes mantendrán el sistema después de la entrega.

</td>
</tr>
</table>

El título no concede autoridad automática. El alcance real depende del equipo, la
industria y la criticidad. Esta guía describe un recorrido desde **semi-senior → principal**, pero una
vacante se evalúa por las decisiones que permite tomar, los sistemas que pone bajo
responsabilidad y la evidencia exigida, no por el nombre del cargo.

## 🧱 Partes y clases asociadas

La ruta distingue **parte** —unidad curricular con una capacidad acumulativa— de
**clase asociada** —punto concreto donde se estudia un mecanismo o una decisión. Las
clases siguientes forman el núcleo; no eliminan los prerrequisitos indicados en sus
propias páginas ni convierten en opcional la base común.

| Orden | Parte del programa | Estado | Clases clave | Por qué entra en esta ruta | Evidencia de transferencia |
| ---: | --- | --- | --- | --- | --- |
| 1 | [Parte 01 · Computadores y representación de información](../classes/part-01-computadores-y-representacion-de-informacion/README.md) | desarrollada | [SE-017 · CPU, instrucciones, registros y ciclos de ejecución](../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md)<br>[SE-018 · Memoria, cachés, almacenamiento y jerarquías](../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md)<br>[SE-019 · Procesos, hilos, interrupciones y entrada/salida](../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md)<br>[SE-021 · Runtimes, máquinas virtuales y recolección de basura](../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md)<br>[SE-022 · Rendimiento, consumo energético y límites físicos](../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) | Profundiza **máquina, memoria, representación y coste físico** desde la responsabilidad del rol. | Experimento reproducible de recursos. |
| 2 | [Parte 02 · Sistemas operativos, terminal y automatización base](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md) | desarrollada | [SE-026 · Sistemas de archivos, rutas, enlaces y metadatos](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)<br>[SE-027 · Usuarios, grupos, permisos y elevación de privilegios](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md)<br>[SE-028 · Procesos, señales, servicios y tareas programadas](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md)<br>[SE-033 · Logs del sistema y diagnóstico de fallos](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md) | Profundiza **sistemas operativos, automatización y diagnóstico** desde la responsabilidad del rol. | Kit de preparación y recuperación. |
| 3 | [Parte 06 · Paradigmas de programación](../classes/part-06-paradigmas-de-programacion/README.md) | desarrollada | [SE-073 · Programación imperativa y estado mutable](../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md)<br>[SE-079 · Programación orientada a eventos](../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md)<br>[SE-081 · Programación concurrente y actores](../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md)<br>[SE-082 · Selección y combinación responsable de paradigmas](../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md) | Profundiza **paradigmas y semánticas alternativas** desde la responsabilidad del rol. | Comparación razonada de implementaciones. |
| 4 | [Parte 23 · Runtimes y plataformas modernas](../classes/part-23-runtimes-y-plataformas-modernas/README.md) | desarrollada | [SE-277 · WebAssembly y WASI](../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md)<br>[SE-279 · eBPF: observabilidad, red y seguridad en el kernel](../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md)<br>[SE-280 · GPU y aceleradores: modelo de ejecución](../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md)<br>[SE-282 · Contenedores, microVM y sandboxes](../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md)<br>[SE-283 · Hardware seguro: TEE y atestación](../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md) | Profundiza **runtimes, aislamiento, aceleradores y confianza** desde la responsabilidad del rol. | Plataforma de ejecución aislada con evidencia. |
| 5 | [Parte 26 · Patrones de diseño, empresariales y de resiliencia](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md) | desarrollada | [SE-313 · Criterios para usar un catálogo de patrones](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md)<br>[SE-320 · Resiliencia: timeout, retry con jitter y circuit breaker](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md)<br>[SE-321 · Resiliencia: bulkhead, sidecar, ambassador y degradación](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md)<br>[SE-322 · Antipatrones y deuda de diseño](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md) | Profundiza **patrones de diseño, empresariales y de resiliencia** desde la responsabilidad del rol. | Catálogo de patrones con su costo. |
| 6 | [Parte 28 · Estilos arquitectónicos](../classes/part-28-estilos-arquitectonicos/README.md) | desarrollada | [SE-337 · Estilos como respuestas a fuerzas de calidad](../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md)<br>[SE-338 · Microkernel y arquitecturas de plugins](../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md)<br>[SE-339 · Pipes and filters y arquitecturas de flujo](../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md)<br>[SE-344 · Arquitectura celular y radio de impacto](../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md) | Profundiza **estilos arquitectónicos y sus fuerzas de calidad** desde la responsabilidad del rol. | Decisión arquitectónica defendida con ADR. |
| 7 | [Parte 32 · Concurrencia y sistemas distribuidos](../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md) | desarrollada | [SE-385 · Concurrencia, paralelismo y asincronía](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md)<br>[SE-386 · Memoria compartida, locks y condiciones de carrera](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md)<br>[SE-387 · Actores, canales y structured concurrency](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md)<br>[SE-389 · Fallos parciales y modelos de red](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) | Profundiza **concurrencia, coordinación y fallos parciales** desde la responsabilidad del rol. | Experimento distribuido de degradación. |
| 8 | [Parte 36 · Calidad, rendimiento y resiliencia](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) | desarrollada | [SE-435 · Carga, estrés, picos y endurance](../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md)<br>[SE-436 · Latencia, throughput, saturación y capacidad](../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)<br>[SE-437 · Perfiles, benchmarks y errores de medición](../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md)<br>[SE-440 · Disponibilidad, durabilidad y recuperación](../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) | Profundiza **calidad, rendimiento y resiliencia** desde la responsabilidad del rol. | Informe medido y game day. |
| 9 | [Parte 37 · Sistemas críticos, tiempo real y normas de seguridad](../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md) | desarrollada | [SE-451 · RTOS y planificación de tiempo real](../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md)<br>[SE-452 · Codificación segura: MISRA y CERT](../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md)<br>[SE-453 · Verificación formal y model checking: TLA+, SPARK y Alloy](../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md)<br>[SE-454 · Verificación y cobertura: MC/DC, HIL y SIL](../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md) | Profundiza **sistemas críticos, tiempo real y normas de seguridad** desde la responsabilidad del rol. | Paquete de aseguramiento de un controlador. |

### ✅ Clases ya desarrolladas que sostienen la ruta hoy

El núcleo anterior apunta a la capacidad profesional completa. Estas clases de apoyo,
de las Partes 00–33, 35–41 y 43–50 (`SE-001`–`SE-408`, `SE-421`–`SE-504` y `SE-517`–`SE-612`), también tienen contenido desarrollado y
permiten practicar el rol desde otros ángulos:

| Clase desarrollada | Parte |
| --- | --- |
| [SE-020 · Compilación, interpretación, bytecode y JIT](../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md) | Parte 01 |
| [SE-094 · Complejidad empírica, benchmarks y perfiles](../classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md) | Parte 07 |
| [SE-099 · Profilers de CPU, memoria, I/O y red](../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md) | Parte 08 |
| [SE-105 · Reproducción de errores y reducción de casos](../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md) | Parte 08 |
| [SE-391 · Consenso, elección y coordinación](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md) | Parte 32 |

**Cómo recorrerla.** Empieza por [SE-017](../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md) para fijar el
primer mecanismo, usa [SE-320](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) para integrar el
centro de la especialidad y llega a [SE-454](../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md) cuando ya
puedas explicar cómo detectar y recuperar un fallo. Una clase se considera estudiada
sólo cuando su concepto cambia una decisión y deja evidencia; abrir todos los enlaces
no constituye competencia.

> [!IMPORTANT]
> El mapa expresa el currículo vigente. Las Partes 00–33, 35–41 y 43–50 (`SE-001`–`SE-408`, `SE-421`–`SE-504` y `SE-517`–`SE-612`) están
> desarrolladas, a falta de una revisión editorial humana independiente. Esta ruta no
> declara aprobadas esas clases ni reemplaza el [roadmap](../ROADMAP.md).

## 🔭 Ampliación planificada: Partes 34 y 42 (sin clases publicadas)

> [!NOTE]
> Las Partes 34 y 42 (`SE-409`–`SE-420` y `SE-505`–`SE-516`) están **planificadas**; sus números están reservados desde el 23 de
> noviembre de 2026 ([ADR-007](../docs/adr/ADR-007-pedagogical-renumbering-and-new-parts.md)). Todavía no
> tienen clases ni README, por lo que no se enlazan aquí y ninguna de sus clases debe
> considerarse disponible.

| Parte planificada | Rango previsto | Qué cambiará para este rol |
| --- | --- | --- |
| — | — | Las partes que este rol esperaba ya están desarrolladas y figuran en el núcleo o en las clases de apoyo. |

Hasta que esas partes se publiquen, el rol se apoya en el núcleo y en las clases
desarrolladas de arriba. La planificación indica hacia dónde crecerá la ruta; no es
evidencia de que el contenido exista ni de que su alcance final coincida con esta
descripción.

## ⚖️ Decisiones y trade-offs que debes defender

| Decisión recurrente | Criterio profesional | Evidencia mínima antes de defenderla |
| --- | --- | --- |
| **Rendimiento o seguridad** | Evitar optimizaciones que rompen memoria aislamiento o portabilidad. | Benchmark y pruebas de sanitización. |
| **Bloqueo o progreso** | Elegir exclusión sincronización o diseño sin estado según garantías. | Reproducir carreras y demostrar ausencia de deadlock. |
| **Portabilidad o especialización** | Aislar dependencias de plataforma detrás de contratos. | Ejecutar el mismo comportamiento en entornos declarados. |

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **Rendimiento o seguridad**, **Bloqueo o progreso**
y **Portabilidad o especialización** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: Proceso que se degrada hasta bloquear el host

**Síntoma.** Crecen memoria hilos y latencia sin error único. La respuesta madura evita convertir la primera
correlación en causa y conserva evidencia antes de modificar el sistema.

```mermaid
flowchart LR
    S["⚠️ Síntoma"] --> H["🔎 Hipótesis"]
    H --> C["🧯 Contención"]
    C --> D["🧠 Diagnóstico"]
    D --> R["🛠️ Recuperación"]
    R --> P["📚 Prevención"]
```

1. **Detectar y delimitar:** identifica quién o qué está afectado, desde cuándo y qué
   cambió. Conserva timestamps, versiones, entradas y señales suficientes para no
   destruir la escena al intentar arreglarla.
2. **Investigar:** Capturar perfil dumps límites y secuencia temporal. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** Liberar recursos aplicar backpressure y probar estabilidad prolongada. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
| **CPU y memoria por operación** | Coste físico de una unidad funcional. | Medir sólo un promedio caliente. |
| **Latencia de cola** | Contención y scheduling bajo carga. | Culpar al runtime sin perfil. |
| **Errores de recursos** | Handles memoria descriptores o threads agotados. | Reiniciar sin localizar la fuga. |

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: Servicio de sistema portable

**Propósito:** construir un proceso concurrente observable con límites de recursos. El resultado esperado es **binario reproducible perfiles pruebas de carrera matriz multi-OS y procedimiento de recuperación**.

Entrega un expediente revisable con estas piezas:

1. **Contexto y alcance:** usuario, sistema, restricción, supuestos, fuera de alcance y
   criterio de no éxito.
2. **Decisión:** al menos dos alternativas reales, trade-offs, coste de reversión y un
   ADR o memo que indique cuándo revisar la elección.
3. **Artefacto principal:** una implementación, modelo, flujo o política coherente con
   las clases núcleo; no una captura aislada ni una presentación sin mecanismo.
4. **Fallo controlado:** introduce una condición adversa relacionada con el escenario
   anterior y conserva el resultado observado, sin inventar una ejecución.
5. **Verificación:** prueba, rúbrica, revisión o medición que pueda fallar y que conecte
   directamente con el resultado profesional.
6. **Operación y salida:** telemetría, recuperación, mantenimiento, deprecación o retiro
   según corresponda; incluye límites y deuda residual.

**Criterio de aceptación:** otra persona puede reconstruir el razonamiento, reproducir
la comprobación y distinguir claramente qué quedó demostrado de lo que sólo se propone.
El proyecto no se aprueba por cantidad de archivos ni por utilizar una marca concreta.

## 📈 Dominio esperado por alcance

| Alcance | Qué resuelve | Qué evidencia su autonomía |
| --- | --- | --- |
| **Inicial** | ejecuta una tarea acotada con criterios y acompañamiento | reproduce el caso, pregunta por supuestos y entrega evidencia legible |
| **Intermedio** | decide dentro de un componente o flujo conocido | compara alternativas, prueba fallos previsibles y coordina dependencias |
| **Senior** | conduce problemas ambiguos que cruzan sistemas o equipos | hace explícito el riesgo, diseña recuperación y mejora el mecanismo de trabajo |
| **Staff / Lead** | cambia capacidades compartidas y decisiones de largo plazo | multiplica criterio, define guardrails, mide adopción y conserva opciones futuras |

Progresar no significa alejarse de la práctica. Significa aumentar ambigüedad, horizonte,
blast radius y responsabilidad por consecuencias. La persona senior todavía debe poder
explicar el mecanismo; la persona Staff además crea condiciones para que otros lo
operen sin depender de ella.

## 🗓️ Plan de práctica 30 · 60 · 90 días

- **Días 1–30 — comprender y reproducir.** Estudia las primeras clases de cada parte,
  reproduce un caso pequeño y escribe un mapa de responsabilidades. El entregable es
  una baseline con preguntas abiertas, no una transformación prematura.
- **Días 31–60 — intervenir y fallar con control.** Construye el artefacto central,
  introduce el escenario de fallo y mide el comportamiento. Revisa el trabajo con una
  persona de una ruta vecina para descubrir supuestos de frontera.
- **Días 61–90 — operar y transferir.** Ejecuta recuperación, corrige la causa, publica
  runbook o guía de uso y presenta la decisión con trade-offs. Termina con una
  retrospectiva que separe resultado, evidencia, límites y siguiente inversión.

Este plan es una secuencia de práctica, no una promesa de empleabilidad en noventa días.
La experiencia previa, el dominio y el acceso a sistemas reales cambian el tiempo
necesario.

## 🎤 Preguntas para revisión o entrevista

1. ¿En qué contexto elegirías **Rendimiento o seguridad** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **Proceso que se degrada hasta bloquear el host**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **Servicio de sistema portable** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

- [The Open Group Base Specifications, Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/) — **The Open Group / IEEE**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — **ISO**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — **IEEE Computer Society**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.
<!-- role-depth:end -->

## 🧪 Evidencia de portafolio

- biblioteca o servicio con contrato de recursos;
- benchmark y perfil reproducibles;
- prueba de carrera, agotamiento y recuperación;
- build portable con sanitizers, fuzzing y artefacto verificable.

## 📈 Progresión

Software Engineer → Systems Programmer → Senior/Staff Systems → Runtime/Platform Architect.

## ⚠️ Mitos frecuentes

- “Bajo nivel siempre es más rápido.” Diseño y acceso a datos suelen dominar.
- “Compilar significa seguro.” No prueba carreras ni límites de recursos.
- “Portabilidad es evitar APIs nativas.” Requiere contratos y entornos comprobados.

## 🚀 Siguientes pasos

1. Define invariantes de memoria, tiempo y recursos.
2. Mide antes de reemplazar una abstracción.
3. Inyecta agotamiento, cancelación y concurrencia adversa.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
