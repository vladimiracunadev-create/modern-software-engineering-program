# 📈 Site Reliability Engineer
<!-- role-visual:start -->
<div align="center">

[![Familia](https://img.shields.io/badge/familia-Confiabilidad-6f42c1?style=for-the-badge)](README.md)
[![Nivel](https://img.shields.io/badge/recorrido-semi--senior%20%E2%86%92%20principal-0969da?style=for-the-badge)](../ROADMAP.md)
[![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-P03%20%C2%B7%20P23%20%C2%B7%20P26%20%C2%B7%20P32%20%C2%B7%20P36%20%C2%B7%20P41%20%C2%B7%20P43%20%C2%B7%20P50-2da44e?style=for-the-badge)](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>
<!-- role-visual:end -->


> Aplica ingeniería de software a la confiabilidad: convierte expectativas de servicio
> en señales, automatización, límites de riesgo y aprendizaje operativo.
>
> **Entrada habitual:** semi-senior/senior · **Foco:** SLO, capacidad e incidentes ·
> **Evidencia central:** servicio que detecta, degrada y recupera de forma ensayada

## 🧭 Qué es y por qué importa

SRE gestiona la tensión entre velocidad de cambio y confiabilidad mediante objetivos
explícitos. Define SLI/SLO, usa error budgets, reduce toil con software y aprende de
incidentes sin buscar culpables. No promete disponibilidad infinita: acuerda qué nivel
de servicio importa y qué inversión lo sostiene.

## 🗓️ Un día en el puesto

- revisar alertas y distinguir síntoma accionable de ruido;
- analizar capacidad, saturación y tendencias;
- automatizar una operación manual repetitiva;
- participar en guardia, contención o postmortem;
- ajustar SLO con producto y equipos de servicio;
- ejecutar un game day o validar recuperación de backup.

## ✅ Responsabilidades y límites

- Responde por mecanismos y feedback de confiabilidad, no por absorber todo incidente.
- Comparte guardia y aprendizaje con quienes construyen el servicio.
- No convierte cada métrica en alerta.
- No usa error budgets como castigo ni SLO como SLA contractual sin acuerdo.
- No automatiza una operación que todavía no comprende.

## 🧠 Qué necesitas saber

- sistemas operativos, redes, concurrencia y sistemas distribuidos;
- latencia, throughput, percentiles y capacity planning;
- logs, métricas, trazas, profiling y OpenTelemetry;
- SLI, SLO, SLA, error budgets y toil;
- fault tolerance, backups, RTO/RPO y disaster recovery;
- incident command, runbooks, postmortems y chaos engineering.

## 📚 Tu ruta en el programa

1. Partes [02](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)–[03](../classes/part-03-redes-internet-y-protocolos/README.md), [08](../classes/part-08-entornos-herramientas-y-depuracion/README.md) y [20](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) para sistemas, red, debugging y servicios.
2. Partes [29](../classes/part-29-datos-persistencia-y-recuperacion/README.md) y [31](../classes/part-31-integracion-eventos-y-mensajeria/README.md)–[33](../classes/part-33-cloud-plataforma-e-infraestructura/README.md) para datos, eventos, distribución y cloud.
3. [Parte 36](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) para rendimiento y resiliencia.
4. [Parte 40](../classes/part-40-ci-cd-iac-y-platform-engineering/README.md) para entrega progresiva y rollback.
5. [Parte 41 — Observabilidad, SRE e incidentes](../classes/part-41-observabilidad-sre-e-incidentes/README.md).
6. [Parte 43](../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md) para continuidad de sistemas legacy; partes 46–47 para agentes operativos controlados.

<!-- role-depth:start -->
## 🗺️ Sistema profesional del rol

```mermaid
flowchart LR
    A["🎯 Expectativa"] --> B
    B["🧠 SLI"] --> C
    C["🛠️ SLO"] --> D
    D["🔎 Respuesta"] --> E["📈 Aprendizaje"]
    classDef intent fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef work fill:#ddf4ff,stroke:#0969da,color:#24292f
    classDef proof fill:#dafbe1,stroke:#1a7f37,color:#24292f
    class A intent
    class B,C,D work
    class E proof
```

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **📈 Site Reliability Engineer**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: Aplica ingeniería de software a la confiabilidad: convierte expectativas de servicio en señales, automatización, límites de riesgo y aprendizaje operativo. Cada transición
debe conservar supuestos, responsables y una forma de volver atrás.

<table>
<tr>
<td valign="top" width="50%">

### 🎯 Responde por

- decisiones propias de la familia **Confiabilidad**;
- el resultado observable, no sólo la actividad ejecutada;
- límites, riesgos, operación y deuda residual de su intervención;
- evidencia que otra persona pueda revisar o reproducir.

</td>
<td valign="top" width="50%">

### 🤝 Coordina con

- [🔭 Observability Engineer](observability-engineer.md); [🚚 DevOps Engineer](devops-engineer.md); [🗄️ Database Reliability Engineer](database-reliability-engineer.md); [🌪️ Chaos & Resilience Engineer](chaos-resilience-engineer.md);
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
| 1 | [Parte 03 · Redes, Internet y protocolos](../classes/part-03-redes-internet-y-protocolos/README.md) | desarrollada | [SE-040 · TCP, UDP, QUIC y decisiones de transporte](../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md)<br>[SE-041 · DNS, nombres, resolución y fallos](../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md)<br>[SE-044 · Proxies, balanceadores, gateways y CDN](../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md)<br>[SE-046 · Captura, medición y diagnóstico de tráfico](../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md) | Profundiza **redes, protocolos y fallos de comunicación** desde la responsabilidad del rol. | Traza de una petición bajo fallos. |
| 2 | [Parte 23 · Runtimes y plataformas modernas](../classes/part-23-runtimes-y-plataformas-modernas/README.md) | desarrollada | [SE-279 · eBPF: observabilidad, red y seguridad en el kernel](../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md)<br>[SE-282 · Contenedores, microVM y sandboxes](../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md)<br>[SE-286 · Confianza cero en la práctica](../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md)<br>[SE-287 · Taller: elegir y aislar un runtime para una carga no confiable](../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md) | Profundiza **runtimes, aislamiento, aceleradores y confianza** desde la responsabilidad del rol. | Plataforma de ejecución aislada con evidencia. |
| 3 | [Parte 26 · Patrones de diseño, empresariales y de resiliencia](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md) | desarrollada | [SE-319 · Enterprise Integration Patterns como lenguaje común](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md)<br>[SE-320 · Resiliencia: timeout, retry con jitter y circuit breaker](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md)<br>[SE-321 · Resiliencia: bulkhead, sidecar, ambassador y degradación](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md)<br>[SE-322 · Antipatrones y deuda de diseño](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md) | Profundiza **patrones de diseño, empresariales y de resiliencia** desde la responsabilidad del rol. | Catálogo de patrones con su costo. |
| 4 | [Parte 32 · Concurrencia y sistemas distribuidos](../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md) | desarrollada | [SE-389 · Fallos parciales y modelos de red](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md)<br>[SE-390 · Consistencia, disponibilidad y particiones](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md)<br>[SE-391 · Consenso, elección y coordinación](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md)<br>[SE-392 · Idempotencia y procesamiento distribuido](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md)<br>[SE-394 · Caos controlado y pruebas de distribución](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md)<br>[SE-396 · Proyecto: servicio distribuido con degradación](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md) | Profundiza **concurrencia, coordinación y fallos parciales** desde la responsabilidad del rol. | Experimento distribuido de degradación. |
| 5 | [Parte 36 · Calidad, rendimiento y resiliencia](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) | desarrollada | [SE-435 · Carga, estrés, picos y endurance](../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md)<br>[SE-436 · Latencia, throughput, saturación y capacidad](../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)<br>[SE-438 · Timeouts, retries, backoff y jitter](../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md)<br>[SE-439 · Circuit breakers, bulkheads y degradación](../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md)<br>[SE-440 · Disponibilidad, durabilidad y recuperación](../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md)<br>[SE-443 · Taller: someter un sistema a presión controlada](../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) | Profundiza **calidad, rendimiento y resiliencia** desde la responsabilidad del rol. | Informe medido y game day. |
| 6 | [Parte 41 · Observabilidad, SRE e incidentes](../classes/part-41-observabilidad-sre-e-incidentes/README.md) | desarrollada | [SE-497 · SLI, SLO, SLA y presupuestos de error](../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)<br>[SE-498 · Alertas accionables y fatiga](../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md)<br>[SE-499 · Runbooks, on-call y escalamiento](../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md)<br>[SE-500 · Gestión de incidentes y comunicación](../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md)<br>[SE-501 · Postmortems sin culpa y aprendizaje](../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md)<br>[SE-502 · Continuidad, disaster recovery y ejercicios](../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md) | Profundiza **observabilidad, SRE e incidentes** desde la responsabilidad del rol. | Incidente diagnosticado y recuperado. |
| 7 | [Parte 43 · Mantenimiento y modernización legacy](../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md) | desarrollada | [SE-517 · Mantenimiento correctivo, adaptativo y perfectivo](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md)<br>[SE-520 · Dependencias obsoletas y riesgo acumulado](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md)<br>[SE-523 · Migraciones de datos sin interrupción](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md)<br>[SE-527 · Taller: estabilizar antes de modernizar](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md) | Profundiza **mantenimiento, modernización y retiro** desde la responsabilidad del rol. | Migración incremental reversible. |
| 8 | [Parte 50 · Machine learning en producción y MLOps](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) | desarrollada | [SE-606 · Servir modelos: latencia, lotes y GPU](../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md)<br>[SE-607 · Despliegue seguro de modelos: shadow, canary y rollback](../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md)<br>[SE-608 · Monitoreo, deriva y reentrenamiento](../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md)<br>[SE-611 · Taller: degradar y recuperar un modelo](../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) | Profundiza **machine learning en producción, MLOps y gobierno de IA** desde la responsabilidad del rol. | Sistema de ML operable con evidencia. |

### ✅ Clases ya desarrolladas que sostienen la ruta hoy

El núcleo anterior apunta a la capacidad profesional completa. Estas clases de apoyo,
de las Partes [00](../classes/part-00-ingenieria-de-software-como-profesion/README.md)–[50](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) (`SE-001`–`SE-612`), también tienen contenido desarrollado y
permiten practicar el rol desde otros ángulos:

| Clase desarrollada | Parte |
| --- | --- |
| [SE-033 · Logs del sistema y diagnóstico de fallos](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md) | [Parte 02](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md) |
| [SE-211 · Runbooks, playbooks y documentación operacional](../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md) | [Parte 17](../classes/part-17-documentacion-y-conocimiento-tecnico/README.md) |
| [SE-224 · Automatización idempotente y reanudable](../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) | [Parte 18](../classes/part-18-cli-tui-servicios-y-automatizacion/README.md) |
| [SE-250 · Health, readiness y shutdown ordenado](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) | [Parte 20](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) |
| [SE-355 · Replicación, partición y distribución](../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) | [Parte 29](../classes/part-29-datos-persistencia-y-recuperacion/README.md) |
| [SE-357 · Backups, restauración y pruebas de recuperación](../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) | [Parte 29](../classes/part-29-datos-persistencia-y-recuperacion/README.md) |
| [SE-246 · Idempotencia, reintentos y deduplicación](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) | [Parte 20](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) |
| [SE-249 · Caching, rate limiting y protección](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) | [Parte 20](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) |
| [SE-475 · Feature flags y entrega progresiva](../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md) | [Parte 39](../classes/part-39-build-release-y-cadena-de-suministro/README.md) |
| [SE-476 · Canary, blue-green y rollback](../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) | [Parte 39](../classes/part-39-build-release-y-cadena-de-suministro/README.md) |
| [SE-478 · Riesgos de CI y dependencias comprometidas](../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md) | [Parte 39](../classes/part-39-build-release-y-cadena-de-suministro/README.md) |
| [SE-490 · Métricas DORA y mejora sin gaming](../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md) | [Parte 40](../classes/part-40-ci-cd-iac-y-platform-engineering/README.md) |
| [SE-445 · Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) | [Parte 37](../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md) |
| [SE-581 · Loops de agentes y criterios de parada](../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md) | [Parte 48](../classes/part-48-harness-y-agentic-engineering/README.md) |
| [SE-582 · Sandboxes, reversibilidad y control de daño](../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md) | [Parte 48](../classes/part-48-harness-y-agentic-engineering/README.md) |
| [SE-505 · Principios de la ingeniería del caos: estado estable e hipótesis](../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md) | [Parte 42](../classes/part-42-ingenieria-del-caos/README.md) |
| [SE-510 · Fallos de datos y de estado: réplicas, particiones y corrupción](../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) | [Parte 42](../classes/part-42-ingenieria-del-caos/README.md) |
| [SE-516 · Proyecto: programa de caos de un servicio con evidencia y remediación](../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md) | [Parte 42](../classes/part-42-ingenieria-del-caos/README.md) |

**Cómo recorrerla.** Empieza por [SE-040](../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md) para fijar el
primer mecanismo, usa [SE-436](../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) para integrar el
centro de la especialidad y llega a [SE-611](../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) cuando ya
puedas explicar cómo detectar y recuperar un fallo. Una clase se considera estudiada
sólo cuando su concepto cambia una decisión y deja evidencia; abrir todos los enlaces
no constituye competencia.

> [!IMPORTANT]
> El mapa expresa el currículo vigente. Las Partes [00](../classes/part-00-ingenieria-de-software-como-profesion/README.md)–[50](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) (`SE-001`–`SE-612`) están
> desarrolladas, a falta de una revisión editorial humana independiente. Esta ruta no
> declara aprobadas esas clases ni reemplaza el [roadmap](../ROADMAP.md).

## ✅ Ampliación completada: todas las partes del alcance

> [!NOTE]
> Todas las partes del alcance ya están desarrolladas ([ADR-007](../docs/adr/ADR-007-pedagogical-renumbering-and-new-parts.md)); sus clases figuran en el núcleo y en las clases de apoyo de esta guía.


## ⚖️ Decisiones y trade-offs que debes defender

| Decisión recurrente | Criterio profesional | Evidencia mínima antes de defenderla |
| --- | --- | --- |
| **Confiabilidad o velocidad** | Usar error budget como señal de decisión compartida. | SLO y tendencia de consumo. |
| **Automatizar o documentar** | Automatizar toil entendido y conservar ruta manual segura. | Horas de toil y fallo de automatización. |
| **Redundancia o simplicidad** | Añadir copias sólo si reducen modos de fallo netos. | Game day y coste operativo. |

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **Confiabilidad o velocidad**, **Automatizar o documentar**
y **Redundancia o simplicidad** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: Servicio responde pero incumple su tarea útil

**Síntoma.** Health checks pasan mientras una dependencia devuelve datos obsoletos. La respuesta madura evita convertir la primera
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
2. **Investigar:** Comparar SLI de usuario saturación trazas dependencia y despliegues. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** Degradar contener comunicar recuperar y revisar objetivo. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
| **Cumplimiento de SLO** | Experiencia buena medida sobre ventana acordada. | Usar uptime de proceso como servicio. |
| **Consumo de error budget** | Ritmo y concentración del riesgo. | Convertirlo en castigo al equipo. |
| **Toil por guardia** | Trabajo manual repetitivo y automatizable. | Automatizar sin medir demanda. |

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: Servicio con confiabilidad ensayada

**Propósito:** definir SLO observar degradación y recuperar una falla compuesta. El resultado esperado es **SLI dashboard alertas runbook game day timeline postmortem y backlog priorizado**.

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

1. ¿En qué contexto elegirías **Confiabilidad o velocidad** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **Servicio responde pero incumple su tarea útil**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **Servicio con confiabilidad ensayada** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

- [Site Reliability Engineering](https://sre.google/books/) — **Google**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/) — **CNCF / OpenTelemetry**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [DORA software delivery performance metrics](https://dora.dev/guides/dora-metrics/) — **Google Cloud**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.
<!-- role-depth:end -->

## 🧪 Evidencia de portafolio

- SLO derivado de una experiencia de usuario y SLI implementado;
- alertas por síntomas con runbook y prueba de escalado;
- dashboard que diferencia tráfico, errores, latencia y saturación;
- load/soak test con capacidad y límites declarados;
- restore ensayado con RTO/RPO observado;
- postmortem con timeline, factores contribuyentes y acciones verificables.

## 📈 Progresión

Software/Systems Engineer → SRE → Senior SRE → Staff Reliability / SRE Lead. También
puede transitar a plataforma, arquitectura distribuida o liderazgo de infraestructura.
La progresión reduce riesgo sistémico más allá de un servicio.

## ⚠️ Mitos frecuentes

- “SRE es operaciones con otro nombre.” Requiere ingeniería y objetivos explícitos.
- “Cinco nueves es siempre mejor.” Puede costar más que el valor que protege.
- “No hubo incidentes, somos confiables.” Quizá faltan tráfico o detección.
- “El postmortem sin culpa no tiene responsables.” Sí tiene ownership, sin simplificar causas.

## 🚀 Siguientes pasos

1. Define un SLO pequeño a partir de un recorrido de usuario.
2. Instrumenta la señal y prueba que detecta degradación.
3. Satura una dependencia en un entorno controlado.
4. Recupera, escribe el postmortem y verifica las acciones posteriores.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
