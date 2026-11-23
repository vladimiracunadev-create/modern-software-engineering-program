# 🔭 Observability Engineer
<!-- role-visual:start -->
<div align="center">

[![Familia](https://img.shields.io/badge/familia-Confiabilidad-6f42c1?style=for-the-badge)](README.md)
[![Nivel](https://img.shields.io/badge/recorrido-semi--senior%20%E2%86%92%20principal-0969da?style=for-the-badge)](../ROADMAP.md)
[![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-P03%20%C2%B7%20P08%20%C2%B7%20P20%20%C2%B7%20P23%20%C2%B7%20P30%20%C2%B7%20P32%20%C2%B7%20P36%20%C2%B7%20P41%20%C2%B7%20P49-2da44e?style=for-the-badge)](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>
<!-- role-visual:end -->


> Diseña señales, contexto y herramientas que permiten formular y responder preguntas
> sobre sistemas en producción sin convertir telemetría en ruido o vigilancia.
>
> **Entrada habitual:** senior · **Foco:** logs, métricas, trazas y diagnóstico
> · **Evidencia central:** recorrido de fallo correlacionado desde síntoma hasta causa

## 🧭 Qué es y por qué importa

Observabilidad es la capacidad práctica de inferir el estado interno a partir de
señales útiles. Este rol normaliza contexto, instrumentación y experiencia de consulta
para reducir tiempo de diagnóstico, coste y alertas sin dueño.

## 🗓️ Un día en el puesto

- diseñar convenciones de atributos y correlation IDs;
- revisar cardinalidad, muestreo y retención;
- instrumentar un recorrido distribuido con OpenTelemetry;
- mejorar dashboard, alerta o flujo de investigación;
- controlar acceso, datos sensibles y coste de telemetría.

## ✅ Responsabilidades y límites

- Responde por calidad, gobernanza y utilidad de señales compartidas.
- Conecta telemetría con preguntas, SLO y runbooks.
- No confunde almacenar muchos logs con comprender el sistema.
- No expone PII ni usa telemetría de ingeniería para vigilar individuos.

## 🧠 Qué necesitas saber

Logs estructurados, métricas, traces, profiling, OpenTelemetry, propagación de
contexto, sampling, cardinalidad, almacenamiento, consultas, SLO, alerting,
privacidad, seguridad, coste y experiencia de diagnóstico.

## 📚 Tu ruta en el programa

1. Partes [02](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)–[03](../classes/part-03-redes-internet-y-protocolos/README.md) y [08](../classes/part-08-entornos-herramientas-y-depuracion/README.md) para sistemas, redes y debugging.
2. Partes [20](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) y [29](../classes/part-29-datos-persistencia-y-recuperacion/README.md)–[33](../classes/part-33-cloud-plataforma-e-infraestructura/README.md) para instrumentar servicios y datos distribuidos.
3. [Partes 36](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) y [35 — Observabilidad, SRE e incidentes](../classes/part-41-observabilidad-sre-e-incidentes/README.md).
4. Partes [40](../classes/part-40-ci-cd-iac-y-platform-engineering/README.md) y [44](../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md)–[47](../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md) para plataforma, ownership y agentes operativos.

<!-- role-depth:start -->
## 🗺️ Sistema profesional del rol

![Diagrama de flujo con 5 pasos. Recorrido: «🎯 Pregunta»; luego «🧠 Instrumentación»; luego «🛠️ Correlación»; luego «🔎 Diagnóstico»; luego «📈 Acción».](../site/assets/figures/mermaid-af6725d2fa.svg)

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **🔭 Observability Engineer**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: Diseña señales, contexto y herramientas que permiten formular y responder preguntas sobre sistemas en producción sin convertir telemetría en ruido o vigilancia. Cada transición
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

- [📈 Site Reliability Engineer](site-reliability-engineer.md); [⏱️ Performance Engineer](performance-engineer.md); [🛤️ Platform Engineer](platform-engineer.md); [🌪️ Chaos & Resilience Engineer](chaos-resilience-engineer.md);
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
| 1 | [Parte 03 · Redes, Internet y protocolos](../classes/part-03-redes-internet-y-protocolos/README.md) | desarrollada | [SE-041 · DNS, nombres, resolución y fallos](../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md)<br>[SE-044 · Proxies, balanceadores, gateways y CDN](../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md)<br>[SE-046 · Captura, medición y diagnóstico de tráfico](../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md)<br>[SE-047 · Taller: seguir una petición de extremo a extremo](../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md)<br>[SE-048 · Proyecto: servicio observable y tolerante a fallos de red](../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md) | Profundiza **redes, protocolos y fallos de comunicación** desde la responsabilidad del rol. | Traza de una petición bajo fallos. |
| 2 | [Parte 08 · Entornos, herramientas y depuración](../classes/part-08-entornos-herramientas-y-depuracion/README.md) | desarrollada | [SE-098 · Depuradores, breakpoints y observación de estado](../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md)<br>[SE-099 · Profilers de CPU, memoria, I/O y red](../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md)<br>[SE-105 · Reproducción de errores y reducción de casos](../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md)<br>[SE-107 · Taller: diagnosticar un fallo desconocido](../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md) | Profundiza **depuración, profiling y reproducción de fallos** desde la responsabilidad del rol. | Expediente de causa raíz. |
| 3 | [Parte 20 · Backend, APIs y procesamiento asíncrono](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) | desarrollada | [SE-244 · Validación, errores y contratos consistentes](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md)<br>[SE-246 · Idempotencia, reintentos y deduplicación](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md)<br>[SE-250 · Health, readiness y shutdown ordenado](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md)<br>[SE-252 · Proyecto: servicio contractual operable](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) | Profundiza **servicios, APIs y procesamiento asíncrono** desde la responsabilidad del rol. | Servicio contractual operable. |
| 4 | [Parte 23 · Runtimes y plataformas modernas](../classes/part-23-runtimes-y-plataformas-modernas/README.md) | desarrollada | [SE-279 · eBPF: observabilidad, red y seguridad en el kernel](../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md)<br>[SE-280 · GPU y aceleradores: modelo de ejecución](../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md)<br>[SE-281 · Rendimiento y costo en aceleradores](../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md)<br>[SE-282 · Contenedores, microVM y sandboxes](../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md) | Profundiza **runtimes, aislamiento, aceleradores y confianza** desde la responsabilidad del rol. | Plataforma de ejecución aislada con evidencia. |
| 5 | [Parte 30 · Ingeniería de datos y plataformas de datos](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md) | desarrollada | [SE-364 · Transformación y orquestación idempotente con backfills](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md)<br>[SE-365 · Calidad y observabilidad de datos](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md)<br>[SE-367 · Linaje, catálogo y metadatos](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md)<br>[SE-370 · Costos y operación de plataformas de datos](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md) | Profundiza **plataformas de datos, calidad, contratos y gobierno** desde la responsabilidad del rol. | Plataforma de datos mínima gobernada. |
| 6 | [Parte 32 · Concurrencia y sistemas distribuidos](../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md) | desarrollada | [SE-388 · Tiempo, relojes y orden parcial](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md)<br>[SE-389 · Fallos parciales y modelos de red](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md)<br>[SE-394 · Caos controlado y pruebas de distribución](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md)<br>[SE-395 · Taller: reproducir una carrera y un fallo parcial](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md) | Profundiza **concurrencia, coordinación y fallos parciales** desde la responsabilidad del rol. | Experimento distribuido de degradación. |
| 7 | [Parte 36 · Calidad, rendimiento y resiliencia](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) | desarrollada | [SE-436 · Latencia, throughput, saturación y capacidad](../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)<br>[SE-437 · Perfiles, benchmarks y errores de medición](../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md)<br>[SE-442 · Calidad de experiencia y presupuestos](../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md)<br>[SE-444 · Proyecto: informe reproducible de calidad](../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) | Profundiza **calidad, rendimiento y resiliencia** desde la responsabilidad del rol. | Informe medido y game day. |
| 8 | [Parte 41 · Observabilidad, SRE e incidentes](../classes/part-41-observabilidad-sre-e-incidentes/README.md) | desarrollada | [SE-493 · Señales, eventos y observabilidad útil](../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md)<br>[SE-494 · Logs estructurados y correlación](../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md)<br>[SE-495 · Métricas, dimensiones y cardinalidad](../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md)<br>[SE-496 · Trazas distribuidas y contexto](../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md)<br>[SE-498 · Alertas accionables y fatiga](../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md)<br>[SE-503 · Taller: diagnosticar con telemetría incompleta](../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md) | Profundiza **observabilidad, SRE e incidentes** desde la responsabilidad del rol. | Incidente diagnosticado y recuperado. |
| 9 | [Parte 49 · Patrones agénticos y sistemas con LLM](../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md) | desarrollada | [SE-596 · Ejecución durable, reintentos e idempotencia](../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md)<br>[SE-597 · Evals y LLMOps de sistemas con LLM](../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md)<br>[SE-598 · Costo, latencia y seguridad en sistemas con LLM](../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md)<br>[SE-600 · Proyecto: sistema con LLM evaluado y operable](../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md) | Profundiza **patrones agénticos, evaluación y operación de sistemas con LLM** desde la responsabilidad del rol. | Sistema con LLM evaluado y operable. |

### ✅ Clases ya desarrolladas que sostienen la ruta hoy

El núcleo anterior apunta a la capacidad profesional completa. Estas clases de apoyo,
de las Partes [00](../classes/part-00-ingenieria-de-software-como-profesion/README.md)–[50](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) (`SE-001`–`SE-612`), también tienen contenido desarrollado y
permiten practicar el rol desde otros ángulos:

| Clase desarrollada | Parte |
| --- | --- |
| [SE-033 · Logs del sistema y diagnóstico de fallos](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md) | [Parte 02](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md) |
| [SE-220 · Códigos de salida, errores y diagnóstico](../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md) | [Parte 18](../classes/part-18-cli-tui-servicios-y-automatizacion/README.md) |
| [SE-226 · Telemetría opt-in y privacidad en herramientas](../classes/part-18-cli-tui-servicios-y-automatizacion/se-226-telemetria-opt-in-y-privacidad-en-herramientas/README.md) | [Parte 18](../classes/part-18-cli-tui-servicios-y-automatizacion/README.md) |
| [SE-308 · Diseño para cambio, prueba y operación](../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md) | [Parte 25](../classes/part-25-diseno-patrones-y-refactorizacion/README.md) |
| [SE-137 · Telemetría de producto y consentimiento](../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md) | [Parte 11](../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md) |
| [SE-382 · Observabilidad y seguridad de integraciones](../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md) | [Parte 31](../classes/part-31-integracion-eventos-y-mensajeria/README.md) |
| [SE-497 · SLI, SLO, SLA y presupuestos de error](../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) | [Parte 41](../classes/part-41-observabilidad-sre-e-incidentes/README.md) |
| [SE-499 · Runbooks, on-call y escalamiento](../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) | [Parte 41](../classes/part-41-observabilidad-sre-e-incidentes/README.md) |
| [SE-504 · Proyecto: operación observable y recuperable](../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) | [Parte 41](../classes/part-41-observabilidad-sre-e-incidentes/README.md) |
| [SE-550 · ODD: desarrollo orgánico y su contraste con SDD](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md) | [Parte 45](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md) |
| [SE-585 · Observabilidad y evals del propio harness](../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md) | [Parte 48](../classes/part-48-harness-y-agentic-engineering/README.md) |
| [SE-587 · Taller: diagnosticar el fallo de un harness](../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md) | [Parte 48](../classes/part-48-harness-y-agentic-engineering/README.md) |
| [SE-608 · Monitoreo, deriva y reentrenamiento](../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) | [Parte 50](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) |
| [SE-505 · Principios de la ingeniería del caos: estado estable e hipótesis](../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md) | [Parte 42](../classes/part-42-ingenieria-del-caos/README.md) |
| [SE-510 · Fallos de datos y de estado: réplicas, particiones y corrupción](../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) | [Parte 42](../classes/part-42-ingenieria-del-caos/README.md) |
| [SE-516 · Proyecto: programa de caos de un servicio con evidencia y remediación](../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md) | [Parte 42](../classes/part-42-ingenieria-del-caos/README.md) |

**Cómo recorrerla.** Empieza por [SE-041](../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md) para fijar el
primer mecanismo, usa [SE-367](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) para integrar el
centro de la especialidad y llega a [SE-600](../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md) cuando ya
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
| **Más datos o mejor señal** | Capturar contexto necesario con coste cardinalidad y privacidad controlados. | Preguntas diagnósticas respondidas por señal. |
| **Logs métricas o trazas** | Combinar según evento tendencia y causalidad distribuida. | Escenario de investigación con presupuesto. |
| **Centralizar o federar** | Equilibrar consistencia ownership y acceso. | SLO de plataforma y contrato de telemetría. |

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **Más datos o mejor señal**, **Logs métricas o trazas**
y **Centralizar o federar** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: Una petición lenta cruza servicios sin identificador común

**Síntoma.** Cada componente registra tiempo pero no conserva contexto. La respuesta madura evita convertir la primera
correlación en causa y conserva evidencia antes de modificar el sistema.

![Diagrama de flujo con 6 pasos. Recorrido: «⚠️ Síntoma»; luego «🔎 Hipótesis»; luego «🧯 Contención»; luego «🧠 Diagnóstico»; luego «🛠️ Recuperación»; luego «📚 Prevención».](../site/assets/figures/mermaid-637bdc6ac9.svg)

**Cómo leer el diagrama:** empieza en «⚠️ Síntoma» y sigue las flechas hasta el final del recorrido. Las filas se leen como una serpentina: de izquierda a derecha y, en la fila siguiente, de derecha a izquierda.

1. **Detectar y delimitar:** identifica quién o qué está afectado, desde cuándo y qué
   cambió. Conserva timestamps, versiones, entradas y señales suficientes para no
   destruir la escena al intentar arreglarla.
2. **Investigar:** Seguir propagación sampling reloj atributos y límites de privacidad. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** Restaurar correlación capturar evidencia mínima y añadir contrato de instrumentación. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
| **Preguntas diagnosticables** | Incidentes que pueden explicarse con datos disponibles. | Contar terabytes ingeridos. |
| **Costo por señal útil** | Valor diagnóstico frente a almacenamiento y procesamiento. | Reducir retención sin evaluar investigación. |
| **Cardinalidad controlada** | Dimensiones que no saturan backend ni presupuesto. | Bloquear etiquetas útiles de forma global. |

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: Plataforma de diagnóstico interoperable

**Propósito:** responder preguntas de fallo sin depender de dashboards preconstruidos. El resultado esperado es **convenciones OTel collector logs métricas trazas presupuesto de cardinalidad y guía de instrumentación**.

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

1. ¿En qué contexto elegirías **Más datos o mejor señal** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **Una petición lenta cruza servicios sin identificador común**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **Plataforma de diagnóstico interoperable** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

- [OpenTelemetry Documentation](https://opentelemetry.io/docs/) — **CNCF / OpenTelemetry**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [Site Reliability Engineering](https://sre.google/books/) — **Google**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — **ISO**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.
<!-- role-depth:end -->

## 🧪 Evidencia de portafolio

- convención de telemetría y modelo de ownership;
- traza correlacionada entre cliente, API, cola y base de datos;
- alerta basada en impacto con runbook;
- análisis de cardinalidad, privacidad, retención y coste.

## 📈 Progresión

SRE/Backend/Data Engineer → Observability Engineer → Staff Telemetry Platform.

## ⚠️ Mitos frecuentes

- “Tres pilares bastan.” Importa la pregunta que pueden responder juntos.
- “Más retención siempre ayuda.” También aumenta coste y exposición.
- “Un dashboard previene incidentes.” Sin acción y ownership es decoración.

## 🚀 Siguientes pasos

1. Formula una pregunta de diagnóstico antes de instrumentar.
2. Sigue una solicitud y un evento de extremo a extremo.
3. Retira una señal inútil y documenta el ahorro.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
