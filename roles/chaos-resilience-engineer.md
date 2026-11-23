# 🌪️ Chaos & Resilience Engineer
<!-- role-visual:start -->
<div align="center">

[![Familia](https://img.shields.io/badge/familia-Confiabilidad-6f42c1?style=for-the-badge)](README.md)
[![Nivel](https://img.shields.io/badge/recorrido-semi--senior%20%E2%86%92%20principal-0969da?style=for-the-badge)](../ROADMAP.md)
[![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-P26%20%C2%B7%20P28%20%C2%B7%20P32%20%C2%B7%20P36%20%C2%B7%20P39%20%C2%B7%20P40%20%C2%B7%20P41%20%C2%B7%20P42-2da44e?style=for-the-badge)](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>
<!-- role-visual:end -->

> Comprueba con experimentos controlados que un sistema sigue cumpliendo su tarea útil
> cuando algo falla: formula la hipótesis, acota el daño, inyecta el fallo, observa y
> corrige lo que la evidencia refute.
>
> **Entrada habitual:** semi-senior · **Foco:** hipótesis de estado estable, inyección
> de fallos y diseño para degradar · **Evidencia central:** un programa de experimentos
> con criterios de aborto, resultados medidos y remediación verificada

## 🧭 Qué es y por qué importa

Los sistemas distribuidos fallan por partes: una dependencia se vuelve lenta, una réplica
diverge, un reintento amplifica una caída, una zona se pierde. Las pruebas unitarias y de
integración rara vez ejercitan esas condiciones, y los diagramas de arquitectura prometen
tolerancia que nadie ha comprobado. La ingeniería del caos propone una respuesta
empírica: tratar cada promesa de resiliencia como una hipótesis y buscar activamente la
evidencia que la refute, de forma controlada y antes de que el fallo llegue solo.

Este rol diseña esos experimentos y, sobre todo, lo que ocurre después: convertir un
hallazgo en un cambio de diseño, de configuración o de operación y repetir el experimento
hasta que la hipótesis se sostenga. El caos sin hipótesis, sin límites y sin aprendizaje
es solo sabotaje.

## 🗓️ Un día en el puesto

- escribir la hipótesis de estado estable de un servicio a partir de sus SLI;
- definir el radio de impacto, la autorización y el criterio de aborto de un experimento;
- inyectar latencia o pérdida en una dependencia y comparar lo observado con lo esperado;
- preparar un game day con roles, escenario, canal de comunicación y registro;
- revisar con el equipo un hallazgo, priorizar su corrección y programar el experimento de verificación;
- auditar timeouts, reintentos y circuit breakers para detectar amplificación de fallos.

## ✅ Responsabilidades y límites

- Responde por la calidad de los experimentos: hipótesis clara, alcance acotado, aborto automático y registro.
- Traduce los resultados en cambios concretos y comprueba que el cambio funcionó.
- Distingue resiliencia demostrada de resiliencia declarada: ninguna garantía cuenta sin experimento.
- No ejecuta fallos sin autorización ni fuera de su alcance acordado, y nunca provoca daño real a clientes como método de aprendizaje.
- No reemplaza a SRE, a observabilidad ni a seguridad: depende de las señales que esas disciplinas proveen y comparte con ellas la respuesta a incidentes.

## 🧠 Qué necesitas saber

Fallos parciales y modelos de red, consistencia y disponibilidad ante particiones,
consenso y coordinación, idempotencia, timeouts, reintentos con jitter, circuit
breakers y bulkheads, degradación elegante, SLI, SLO y presupuestos de error,
telemetría para detectar cambios de estado estable, despliegue progresivo con
reversión, gestión de incidentes y diseño de experimentos con control y criterio
de aborto.

## 📚 Tu ruta en el programa

1. [Parte 42 — Ingeniería del caos](../classes/part-42-ingenieria-del-caos/README.md) para hipótesis de estado estable, diseño de experimentos, inyección de fallos, game days, gobernanza y aprendizaje.
2. [Parte 32 — Concurrencia y sistemas distribuidos](../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md) para fallos parciales, tiempo, consenso, replicación y caos controlado.
3. [Parte 36 — Calidad, rendimiento y resiliencia](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) para timeouts, circuit breakers, bulkheads, capacidad y recuperación.
4. [Parte 41 — Observabilidad, SRE e incidentes](../classes/part-41-observabilidad-sre-e-incidentes/README.md) para SLO, alertas, runbooks, incidentes, postmortems y continuidad.
5. [Parte 40 — CI/CD, IaC y platform engineering](../classes/part-40-ci-cd-iac-y-platform-engineering/README.md) para llevar los experimentos a pipelines, GitOps y métricas de entrega sin gaming.
6. [Parte 26 — Patrones de diseño, empresariales y de resiliencia](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md) para patrones de resiliencia: retry con jitter, circuit breaker y degradación.
7. [Parte 28 — Estilos arquitectónicos](../classes/part-28-estilos-arquitectonicos/README.md) para arquitectura celular, microservicios y evolución entre estilos.
8. [Parte 39 — Build, release y cadena de suministro](../classes/part-39-build-release-y-cadena-de-suministro/README.md) para feature flags, canary y rollback como mecanismos de aborto.

<!-- role-depth:start -->
## 🗺️ Sistema profesional del rol

![Diagrama de flujo con 5 pasos. Recorrido: «🎯 Estado estable»; luego «🧠 Hipótesis»; luego «🛠️ Experimento»; luego «🔎 Contención»; luego «📈 Aprendizaje».](../site/assets/figures/mermaid-3f2c77080c.svg)

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **🌪️ Chaos & Resilience Engineer**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: Comprueba con experimentos controlados que un sistema sigue cumpliendo su tarea útil cuando algo falla: formula la hipótesis, acota el daño, inyecta el fallo, observa y corrige lo que la evidencia refute. Cada transición
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

- [📈 Site Reliability Engineer](site-reliability-engineer.md); [🌐 Distributed Systems Engineer](distributed-systems-engineer.md); [🔭 Observability Engineer](observability-engineer.md);
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
| 1 | [Parte 26 · Patrones de diseño, empresariales y de resiliencia](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md) | desarrollada | [SE-320 · Resiliencia: timeout, retry con jitter y circuit breaker](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md)<br>[SE-321 · Resiliencia: bulkhead, sidecar, ambassador y degradación](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md)<br>[SE-322 · Antipatrones y deuda de diseño](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md) | Profundiza **patrones de diseño, empresariales y de resiliencia** desde la responsabilidad del rol. | Catálogo de patrones con su costo. |
| 2 | [Parte 28 · Estilos arquitectónicos](../classes/part-28-estilos-arquitectonicos/README.md) | desarrollada | [SE-337 · Estilos como respuestas a fuerzas de calidad](../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md)<br>[SE-340 · Microservicios y sus costes reales](../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md)<br>[SE-344 · Arquitectura celular y radio de impacto](../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md) | Profundiza **estilos arquitectónicos y sus fuerzas de calidad** desde la responsabilidad del rol. | Decisión arquitectónica defendida con ADR. |
| 3 | [Parte 32 · Concurrencia y sistemas distribuidos](../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md) | desarrollada | [SE-388 · Tiempo, relojes y orden parcial](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md)<br>[SE-389 · Fallos parciales y modelos de red](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md)<br>[SE-390 · Consistencia, disponibilidad y particiones](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md)<br>[SE-391 · Consenso, elección y coordinación](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md)<br>[SE-392 · Idempotencia y procesamiento distribuido](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md)<br>[SE-394 · Caos controlado y pruebas de distribución](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md)<br>[SE-396 · Proyecto: servicio distribuido con degradación](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md) | Profundiza **concurrencia, coordinación y fallos parciales** desde la responsabilidad del rol. | Experimento distribuido de degradación. |
| 4 | [Parte 36 · Calidad, rendimiento y resiliencia](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) | desarrollada | [SE-435 · Carga, estrés, picos y endurance](../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md)<br>[SE-436 · Latencia, throughput, saturación y capacidad](../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)<br>[SE-438 · Timeouts, retries, backoff y jitter](../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md)<br>[SE-439 · Circuit breakers, bulkheads y degradación](../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md)<br>[SE-440 · Disponibilidad, durabilidad y recuperación](../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md)<br>[SE-443 · Taller: someter un sistema a presión controlada](../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) | Profundiza **calidad, rendimiento y resiliencia** desde la responsabilidad del rol. | Informe medido y game day. |
| 5 | [Parte 39 · Build, release y cadena de suministro](../classes/part-39-build-release-y-cadena-de-suministro/README.md) | desarrollada | [SE-475 · Feature flags y entrega progresiva](../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md)<br>[SE-476 · Canary, blue-green y rollback](../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) | Profundiza **build, release y cadena de suministro** desde la responsabilidad del rol. | Release firmado y verificable. |
| 6 | [Parte 40 · CI/CD, IaC y platform engineering](../classes/part-40-ci-cd-iac-y-platform-engineering/README.md) | desarrollada | [SE-485 · Entrega y despliegue continuos](../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md)<br>[SE-487 · GitOps y reconciliación](../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md)<br>[SE-490 · Métricas DORA y mejora sin gaming](../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md)<br>[SE-492 · Proyecto: camino a producción con rollback](../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md) | Profundiza **CI/CD, IaC, plataforma y DevEx** desde la responsabilidad del rol. | Camino autoservicio con rollback. |
| 7 | [Parte 41 · Observabilidad, SRE e incidentes](../classes/part-41-observabilidad-sre-e-incidentes/README.md) | desarrollada | [SE-497 · SLI, SLO, SLA y presupuestos de error](../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)<br>[SE-498 · Alertas accionables y fatiga](../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md)<br>[SE-499 · Runbooks, on-call y escalamiento](../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md)<br>[SE-500 · Gestión de incidentes y comunicación](../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md)<br>[SE-501 · Postmortems sin culpa y aprendizaje](../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md)<br>[SE-502 · Continuidad, disaster recovery y ejercicios](../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md)<br>[SE-503 · Taller: diagnosticar con telemetría incompleta](../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md) | Profundiza **observabilidad, SRE e incidentes** desde la responsabilidad del rol. | Incidente diagnosticado y recuperado. |
| 8 | [Parte 42 · Ingeniería del caos](../classes/part-42-ingenieria-del-caos/README.md) | desarrollada | [SE-505 · Principios de la ingeniería del caos: estado estable e hipótesis](../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md)<br>[SE-506 · Diseñar experimentos de fallo: alcance y radio de impacto](../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md)<br>[SE-507 · Inyección de fallos de red, latencia y dependencias](../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md)<br>[SE-508 · Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md)<br>[SE-510 · Fallos de datos y de estado: réplicas, particiones y corrupción](../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md)<br>[SE-511 · Game days y ejercicios de respuesta a incidentes](../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md)<br>[SE-512 · Caos continuo: automatización en CI/CD y en producción](../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md)<br>[SE-513 · Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar](../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md)<br>[SE-514 · Aprender de los experimentos: hallazgos, métricas y mejora](../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md)<br>[SE-516 · Proyecto: programa de caos de un servicio con evidencia y remediación](../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md) | Profundiza **ingeniería del caos: hipótesis, inyección de fallos, game days y aprendizaje** desde la responsabilidad del rol. | Programa de caos de un servicio con evidencia y remediación. |

### ✅ Clases ya desarrolladas que sostienen la ruta hoy

El núcleo anterior apunta a la capacidad profesional completa. Estas clases de apoyo,
de las Partes [00](../classes/part-00-ingenieria-de-software-como-profesion/README.md)–[50](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) (`SE-001`–`SE-612`), también tienen contenido desarrollado y
permiten practicar el rol desde otros ángulos:

| Clase desarrollada | Parte |
| --- | --- |
| [SE-246 · Idempotencia, reintentos y deduplicación](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) | [Parte 20](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) |
| [SE-249 · Caching, rate limiting y protección](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) | [Parte 20](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) |
| [SE-347 · Taller: seleccionar un estilo con escenarios de calidad](../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md) | [Parte 28](../classes/part-28-estilos-arquitectonicos/README.md) |
| [SE-357 · Backups, restauración y pruebas de recuperación](../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) | [Parte 29](../classes/part-29-datos-persistencia-y-recuperacion/README.md) |
| [SE-404 · Escalado, capacidad y costos](../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md) | [Parte 33](../classes/part-33-cloud-plataforma-e-infraestructura/README.md) |
| [SE-444 · Proyecto: informe reproducible de calidad](../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) | [Parte 36](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) |
| [SE-480 · Proyecto: release firmado y recuperable](../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md) | [Parte 39](../classes/part-39-build-release-y-cadena-de-suministro/README.md) |
| [SE-504 · Proyecto: operación observable y recuperable](../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) | [Parte 41](../classes/part-41-observabilidad-sre-e-incidentes/README.md) |

**Cómo recorrerla.** Empieza por [SE-320](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) para fijar el
primer mecanismo, usa [SE-485](../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) para integrar el
centro de la especialidad y llega a [SE-516](../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md) cuando ya
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
| **Radio de impacto o realismo** | Empezar con fallos pequeños y ampliar el alcance solo con evidencia de contención. | Condiciones de aborto y registro del alcance real de cada experimento. |
| **Producción o preproducción** | Decidir dónde se inyecta según fidelidad del fallo y riesgo asumido. | Comparación de hallazgos entre entornos y autorización explícita. |
| **Reintentar o degradar** | Elegir la respuesta del sistema al fallo parcial antes de inyectarlo. | Experimento que demuestra que la degradación conserva la tarea útil. |

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **Radio de impacto o realismo**, **Producción o preproducción**
y **Reintentar o degradar** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: El reintento amplifica la caída

**Síntoma.** Una dependencia lenta provoca reintentos en cascada y satura al servicio sano. La respuesta madura evita convertir la primera
correlación en causa y conserva evidencia antes de modificar el sistema.

![Diagrama de flujo con 6 pasos. Recorrido: «⚠️ Síntoma»; luego «🔎 Hipótesis»; luego «🧯 Contención»; luego «🧠 Diagnóstico»; luego «🛠️ Recuperación»; luego «📚 Prevención».](../site/assets/figures/mermaid-637bdc6ac9.svg)

**Cómo leer el diagrama:** empieza en «⚠️ Síntoma» y sigue las flechas hasta el final del recorrido. Las filas se leen como una serpentina: de izquierda a derecha y, en la fila siguiente, de derecha a izquierda.

1. **Detectar y delimitar:** identifica quién o qué está afectado, desde cuándo y qué
   cambió. Conserva timestamps, versiones, entradas y señales suficientes para no
   destruir la escena al intentar arreglarla.
2. **Investigar:** Reconstruir la línea temporal con trazas colas y presupuestos de reintento. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** Cortar con circuit breaker limitar reintentos y repetir el experimento hasta que la hipótesis se sostenga. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
| **Hipótesis refutadas** | Supuestos de resiliencia que el experimento desmintió. | Premiar experimentos que siempre pasan. |
| **Tiempo de detección y recuperación** | Segundos hasta la señal y hasta recuperar el estado estable. | Medir solo el promedio y no el peor caso. |
| **Hallazgos cerrados** | Debilidades corregidas y verificadas con un nuevo experimento. | Contar hallazgos abiertos sin priorizar por impacto. |

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: Programa de caos de un servicio

**Propósito:** diseñar hipótesis de estado estable inyectar fallos acotados y remediar lo que se refute. El resultado esperado es **catálogo de experimentos criterios de aborto resultados con evidencia informe de remediación y game day documentado**.

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

1. ¿En qué contexto elegirías **Radio de impacto o realismo** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **El reintento amplifica la caída**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **Programa de caos de un servicio** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

- [Principles of Chaos Engineering](https://principlesofchaos.org/) — **Principles of Chaos Engineering**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [Site Reliability Engineering](https://sre.google/books/) — **Google**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [Cloud design patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/) — **Microsoft Azure Architecture Center**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/) — **CNCF / OpenTelemetry**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.
<!-- role-depth:end -->

## 🧪 Evidencia de portafolio

- hipótesis de estado estable de un servicio, con SLI y umbrales explícitos;
- catálogo de experimentos con radio de impacto, autorización y criterio de aborto;
- resultado medido de al menos un experimento que refutó una hipótesis, con la corrección y su repetición;
- informe de game day con línea temporal, decisiones, tiempo de detección y recuperación;
- análisis de amplificación de reintentos en una cadena de dependencias, con presupuesto propuesto.

## 📈 Progresión

SRE, Backend o Distributed Systems Engineer → Chaos & Resilience Engineer → Staff Reliability Engineer o Principal de Resiliencia.

## ⚠️ Mitos frecuentes

- “El caos es romper cosas en producción.” Es un método experimental con hipótesis, alcance acotado y aborto; el daño sin control es una falla de proceso.
- “Si el experimento pasa, el sistema es resiliente.” Solo lo es frente al fallo ensayado, con la carga y las condiciones de ese momento.
- “Los reintentos hacen más robusto al sistema.” Sin límites y jitter amplifican la caída que querían absorber.
- “Basta con una herramienta de inyección.” La herramienta produce fallos; el valor está en la hipótesis, la lectura de señales y la corrección.

## 🚀 Siguientes pasos

1. Escribe la hipótesis de estado estable de un servicio propio con dos SLI y un umbral de aborto.
2. Inyecta latencia en una dependencia en un entorno de pruebas y registra si los reintentos la amplifican.
3. Convierte el hallazgo en un cambio y repite el experimento para demostrar que se sostiene.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
