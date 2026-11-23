# ⚙️ Backend Engineer
<!-- role-visual:start -->
<div align="center">

[![Familia](https://img.shields.io/badge/familia-Producto%20digital-6f42c1?style=for-the-badge)](README.md)
[![Nivel](https://img.shields.io/badge/recorrido-junior%20%E2%86%92%20principal-0969da?style=for-the-badge)](../ROADMAP.md)
[![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-P20%20%C2%B7%20P26%20%C2%B7%20P27%20%C2%B7%20P28%20%C2%B7%20P29%20%C2%B7%20P31%20%C2%B7%20P36%20%C2%B7%20P41-2da44e?style=for-the-badge)](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>
<!-- role-visual:end -->


> Diseña servicios, reglas de negocio, contratos y datos que siguen siendo confiables
> cuando aparecen concurrencia, fallos parciales y cambios de versión.
>
> **Entrada habitual:** junior/semi-senior · **Foco:** APIs, dominio, datos y operación
> · **Evidencia central:** servicio observable con contrato y recuperación probados

## 🧭 Qué es y por qué importa

Backend engineering construye las capacidades que viven detrás de una interfaz:
autorización, reglas, persistencia, integración y procesos asíncronos. El reto no es
solo responder HTTP; es conservar invariantes frente a duplicados, reintentos,
concurrencia, migraciones y dependencias degradadas.

## 🗓️ Un día en el puesto

- refinar una regla de negocio y convertirla en casos verificables;
- diseñar o evolucionar una API sin romper consumidores;
- investigar una consulta lenta, un timeout o un mensaje duplicado;
- revisar esquemas, migraciones y límites transaccionales;
- desplegar un cambio gradual y observar latencia, errores y saturación;
- coordinar con frontend, datos, seguridad, plataforma y producto.

## ✅ Responsabilidades y límites

- Responde por contratos, invariantes, datos y comportamiento bajo fallo.
- Debe comprender autenticación, autorización, privacidad y abuso.
- No convierte cada módulo en microservicio por defecto.
- No usa una cola para ocultar inconsistencias ni una caché para evitar modelar datos.
- No promete “exactly once” sin explicar el mecanismo y sus límites.

## 🧠 Qué necesitas saber

- estructuras de datos, concurrencia, procesos y redes;
- modelado de dominio, modularidad, errores e idempotencia;
- REST/RPC/GraphQL/gRPC, eventos, webhooks y contratos;
- transacciones, índices, caché, partición, réplica y migraciones;
- pruebas unitarias, integración, contrato, rendimiento y seguridad;
- logs estructurados, métricas, trazas, SLO y respuesta a incidentes.

## 📚 Tu ruta en el programa

1. Partes 00–09 para fundamentos y construcción.
2. Partes 10–13 para producto, requisitos, dominio y contratos.
3. [Parte 20 — Backend, APIs y procesamiento asíncrono](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md).
4. [Parte 25 — Diseño, patrones y refactorización](../classes/part-25-diseno-patrones-y-refactorizacion/README.md) y Parte 27.
5. Partes 29 y 31–32 para persistencia, eventos y distribución.
6. Partes 35–36 y 38–41 para pruebas, seguridad, entrega y operación.
7. Partes 43, 46 y 47 para evolución y trabajo asistido por agentes.

<!-- role-depth:start -->
## 🗺️ Sistema profesional del rol

```mermaid
flowchart LR
    A["🎯 Regla de negocio"] --> B
    B["🧠 Contrato"] --> C
    C["🛠️ Persistencia"] --> D
    D["🔎 Telemetría"] --> E["📈 Evolución"]
    classDef intent fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef work fill:#ddf4ff,stroke:#0969da,color:#24292f
    classDef proof fill:#dafbe1,stroke:#1a7f37,color:#24292f
    class A intent
    class B,C,D work
    class E proof
```

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **⚙️ Backend Engineer**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: Diseña servicios, reglas de negocio, contratos y datos que siguen siendo confiables cuando aparecen concurrencia, fallos parciales y cambios de versión. Cada transición
debe conservar supuestos, responsables y una forma de volver atrás.

<table>
<tr>
<td valign="top" width="50%">

### 🎯 Responde por

- decisiones propias de la familia **Producto digital**;
- el resultado observable, no sólo la actividad ejecutada;
- límites, riesgos, operación y deuda residual de su intervención;
- evidencia que otra persona pueda revisar o reproducir.

</td>
<td valign="top" width="50%">

### 🤝 Coordina con

- [🔗 API Engineer](api-engineer.md); [🧱 Data Engineer](data-engineer.md); [🌐 Distributed Systems Engineer](distributed-systems-engineer.md);
- producto y personas usuarias cuando cambia una tarea o outcome;
- seguridad, privacidad, accesibilidad y operación según el riesgo;
- quienes mantendrán el sistema después de la entrega.

</td>
</tr>
</table>

El título no concede autoridad automática. El alcance real depende del equipo, la
industria y la criticidad. Esta guía describe un recorrido desde **junior → principal**, pero una
vacante se evalúa por las decisiones que permite tomar, los sistemas que pone bajo
responsabilidad y la evidencia exigida, no por el nombre del cargo.

## 🧱 Partes y clases asociadas

La ruta distingue **parte** —unidad curricular con una capacidad acumulativa— de
**clase asociada** —punto concreto donde se estudia un mecanismo o una decisión. Las
clases siguientes forman el núcleo; no eliminan los prerrequisitos indicados en sus
propias páginas ni convierten en opcional la base común.

| Orden | Parte del programa | Estado | Clases clave | Por qué entra en esta ruta | Evidencia de transferencia |
| ---: | --- | --- | --- | --- | --- |
| 1 | [Parte 20 · Backend, APIs y procesamiento asíncrono](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) | desarrollada | [SE-241 · Responsabilidades y fronteras del backend](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md)<br>[SE-244 · Validación, errores y contratos consistentes](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md)<br>[SE-245 · Autenticación, autorización y contexto](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)<br>[SE-246 · Idempotencia, reintentos y deduplicación](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md)<br>[SE-247 · Jobs, colas y procesamiento diferido](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md)<br>[SE-250 · Health, readiness y shutdown ordenado](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) | Profundiza **servicios, APIs y procesamiento asíncrono** desde la responsabilidad del rol. | Servicio contractual operable. |
| 2 | [Parte 26 · Patrones de diseño, empresariales y de resiliencia](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md) | desarrollada | [SE-318 · Repository, Unit of Work y Active Record](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md)<br>[SE-319 · Enterprise Integration Patterns como lenguaje común](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md)<br>[SE-320 · Resiliencia: timeout, retry con jitter y circuit breaker](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md)<br>[SE-321 · Resiliencia: bulkhead, sidecar, ambassador y degradación](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) | Profundiza **patrones de diseño, empresariales y de resiliencia** desde la responsabilidad del rol. | Catálogo de patrones con su costo. |
| 3 | [Parte 27 · Arquitectura de software y dominio](../classes/part-27-arquitectura-de-software-y-dominio/README.md) | desarrollada | [SE-327 · Monolito, modular monolith y servicios](../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md)<br>[SE-328 · Capas, hexagonal, clean y ports and adapters](../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md)<br>[SE-329 · Domain-Driven Design estratégico y táctico](../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md)<br>[SE-330 · Event-driven, CQRS y event sourcing](../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md) | Profundiza **arquitectura, dominio y atributos de calidad** desde la responsabilidad del rol. | Arquitectura defendible con ADR. |
| 4 | [Parte 28 · Estilos arquitectónicos](../classes/part-28-estilos-arquitectonicos/README.md) | desarrollada | [SE-337 · Estilos como respuestas a fuerzas de calidad](../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md)<br>[SE-340 · Microservicios y sus costes reales](../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md)<br>[SE-341 · BFF, API gateway y service mesh](../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md)<br>[SE-345 · 12-factor y aplicaciones nativas de la nube](../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md) | Profundiza **estilos arquitectónicos y sus fuerzas de calidad** desde la responsabilidad del rol. | Decisión arquitectónica defendida con ADR. |
| 5 | [Parte 29 · Datos, persistencia y recuperación](../classes/part-29-datos-persistencia-y-recuperacion/README.md) | desarrollada | [SE-351 · Transacciones, aislamiento y concurrencia](../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md)<br>[SE-352 · Restricciones, invariantes y consistencia](../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md)<br>[SE-353 · Consultas, índices y patrones de acceso](../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md)<br>[SE-354 · Migraciones compatibles y evolución de esquema](../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md)<br>[SE-357 · Backups, restauración y pruebas de recuperación](../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) | Profundiza **persistencia, transacciones y recuperación** desde la responsabilidad del rol. | Capa de datos restaurable. |
| 6 | [Parte 31 · Integración, eventos y mensajería](../classes/part-31-integracion-eventos-y-mensajeria/README.md) | desarrollada | [SE-376 · Entrega, orden, duplicación y semánticas](../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md)<br>[SE-377 · Outbox, inbox, sagas y compensación](../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md)<br>[SE-380 · Compatibilidad de esquemas y registros](../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md)<br>[SE-382 · Observabilidad y seguridad de integraciones](../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md) | Profundiza **eventos, mensajería y compatibilidad** desde la responsabilidad del rol. | Flujo tolerante a duplicados. |
| 7 | [Parte 36 · Calidad, rendimiento y resiliencia](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) | desarrollada | [SE-436 · Latencia, throughput, saturación y capacidad](../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)<br>[SE-438 · Timeouts, retries, backoff y jitter](../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md)<br>[SE-439 · Circuit breakers, bulkheads y degradación](../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md)<br>[SE-440 · Disponibilidad, durabilidad y recuperación](../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) | Profundiza **calidad, rendimiento y resiliencia** desde la responsabilidad del rol. | Informe medido y game day. |
| 8 | [Parte 41 · Observabilidad, SRE e incidentes](../classes/part-41-observabilidad-sre-e-incidentes/README.md) | desarrollada | [SE-493 · Señales, eventos y observabilidad útil](../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md)<br>[SE-496 · Trazas distribuidas y contexto](../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md)<br>[SE-497 · SLI, SLO, SLA y presupuestos de error](../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)<br>[SE-500 · Gestión de incidentes y comunicación](../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) | Profundiza **observabilidad, SRE e incidentes** desde la responsabilidad del rol. | Incidente diagnosticado y recuperado. |

### ✅ Clases ya desarrolladas que sostienen la ruta hoy

El núcleo anterior apunta a la capacidad profesional completa. Estas clases de apoyo,
de las Partes 00–33, 35–41 y 43–50 (`SE-001`–`SE-408`, `SE-421`–`SE-504` y `SE-517`–`SE-612`), también tienen contenido desarrollado y
permiten practicar el rol desde otros ángulos:

| Clase desarrollada | Parte |
| --- | --- |
| [SE-242 · REST y semántica de recursos](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) | Parte 20 |
| [SE-243 · RPC, GraphQL y selección de interfaz](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md) | Parte 20 |
| [SE-248 · Archivos, streaming y cargas extensas](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) | Parte 20 |
| [SE-249 · Caching, rate limiting y protección](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) | Parte 20 |

**Cómo recorrerla.** Empieza por [SE-241](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) para fijar el
primer mecanismo, usa [SE-345](../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md) para integrar el
centro de la especialidad y llega a [SE-500](../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) cuando ya
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
| **Parte 34 · SaaS y plataformas de producto** | `SE-409`–`SE-420` | Trasladará los servicios al contexto SaaS: identidad de organización, medición de uso, facturación y aprovisionamiento del tenant. |

Hasta que esas partes se publiquen, el rol se apoya en el núcleo y en las clases
desarrolladas de arriba. La planificación indica hacia dónde crecerá la ruta; no es
evidencia de que el contenido exista ni de que su alcance final coincida con esta
descripción.

## ⚖️ Decisiones y trade-offs que debes defender

| Decisión recurrente | Criterio profesional | Evidencia mínima antes de defenderla |
| --- | --- | --- |
| **Síncrono o asíncrono** | Evaluar latencia acoplamiento confirmación y reintentos. | Prueba contractual más experimento de duplicación. |
| **Consistencia o disponibilidad** | Declarar qué invariantes no se negocian durante particiones. | Historial de operaciones y reconciliación verificable. |
| **Monolito o servicio** | Separar por límites y autonomía reales no por moda. | ADR con costes de operación y estrategia de retorno. |

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **Síncrono o asíncrono**, **Consistencia o disponibilidad**
y **Monolito o servicio** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: Cobro o comando aplicado dos veces

**Síntoma.** Un cliente reintenta después de perder la respuesta. La respuesta madura evita convertir la primera
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
2. **Investigar:** Correlacionar request key transacción outbox y efectos externos. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** Contener compensar y probar que el mismo intento conserva el invariante. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
| **Errores por operación** | Corrección observada por contrato y tipo de fallo. | Mezclar validación con dependencia caída. |
| **Latencia p50 p95 p99** | Distribución y cola bajo carga conocida. | Publicar percentiles sin volumen ni ventana. |
| **Duplicados reconciliados** | Eficacia de idempotencia y deduplicación. | Ocultar el problema descartando mensajes. |

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: Servicio contractual recuperable

**Propósito:** operar una capacidad de negocio bajo reintentos degradación y migración. El resultado esperado es **OpenAPI migración compatible pruebas de contrato dashboard SLO y runbook**.

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

1. ¿En qué contexto elegirías **Síncrono o asíncrono** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **Cobro o comando aplicado dos veces**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **Servicio contractual recuperable** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — **OpenAPI Initiative**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — **IETF**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [Site Reliability Engineering](https://sre.google/books/) — **Google**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.
<!-- role-depth:end -->

## 🧪 Evidencia de portafolio

- OpenAPI o contrato equivalente con ejemplos positivos y negativos;
- API idempotente con pruebas de duplicación y reintento;
- migración de esquema compatible con rollback;
- consumidor asíncrono que recupera poison messages;
- dashboard y runbook para una degradación de dependencia;
- ADR comparando monolito modular, servicio separado y alternativa comprada.

## 📈 Progresión

Backend Junior → Backend Engineer → Senior → Staff/Principal o especialización en
datos, distribución, seguridad, plataforma o arquitectura. El crecimiento consiste
en proteger más invariantes y coordinar más consumidores, no en sumar endpoints.

## ⚠️ Mitos frecuentes

- “Backend es CRUD.” El CRUD trivial termina donde empiezan reglas, concurrencia y fallos.
- “Microservicios escalan equipos.” También multiplican contratos y operación.
- “La base de datos resuelve consistencia.” Solo dentro de garantías bien entendidas.
- “Más caché siempre mejora.” Puede empeorar corrección, coste y diagnóstico.

## 🚀 Siguientes pasos

1. Construye un monolito modular pequeño antes de distribuirlo.
2. Define invariantes y pruebas contractuales antes de optimizar.
3. Introduce una falla de dependencia y demuestra recuperación.
4. Mide p50/p95/p99 y explica qué carga produjo esos datos.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
