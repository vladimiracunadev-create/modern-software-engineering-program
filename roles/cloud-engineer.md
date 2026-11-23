# ☁️ Cloud Engineer
<!-- role-visual:start -->
<div align="center">

[![Familia](https://img.shields.io/badge/familia-Cloud-6f42c1?style=for-the-badge)](README.md)
[![Nivel](https://img.shields.io/badge/recorrido-semi--senior%20%E2%86%92%20principal-0969da?style=for-the-badge)](../ROADMAP.md)
[![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-P03%20%C2%B7%20P23%20%C2%B7%20P32%20%C2%B7%20P33%20%C2%B7%20P36%20%C2%B7%20P38%20%C2%B7%20P40%20%C2%B7%20P41-2da44e?style=for-the-badge)](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>
<!-- role-visual:end -->


> Diseña y automatiza capacidades cloud seguras, observables, recuperables y
> económicamente defendibles sin quedar atrapado en servicios por accidente.
>
> **Entrada habitual:** semi-senior · **Foco:** infraestructura, IAM y operación
> · **Evidencia central:** entorno reproducible con coste y recuperación comprobados

## 🧭 Qué es y por qué importa

Cloud engineering convierte servicios de proveedor en una plataforma operable. El
trabajo real abarca identidad, redes, datos, automatización, límites, facturación y
responsabilidad compartida; no consiste en hacer clic hasta que algo responda.

## 🗓️ Un día en el puesto

- revisar un cambio IaC y su impacto de permisos y coste;
- diagnosticar red, cuota, identidad o capacidad;
- diseñar aislamiento entre ambientes y cuentas;
- ensayar recuperación y destrucción segura;
- evaluar un servicio gestionado frente a alternativas.

## ✅ Responsabilidades y límites

- Responde por infraestructura declarada, seguridad base y operabilidad.
- Aplica mínimo privilegio y ownership de recursos.
- No confunde servicio gestionado con responsabilidad transferida.
- No construye multi-cloud sin amenaza, requisito o poder de negociación concreto.

## 🧠 Qué necesitas saber

Redes, IAM, cómputo, storage, containers, Kubernetes según necesidad, serverless,
IaC, GitOps, políticas, secretos, observabilidad, backup, DR, cadena de suministro, FinOps
y modelos de responsabilidad compartida.

## 📚 Tu ruta en el programa

1. Partes [01](../classes/part-01-computadores-y-representacion-de-informacion/README.md)–[09](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md) y [16](../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)–[18](../classes/part-18-cli-tui-servicios-y-automatizacion/README.md) para sistemas, automatización y colaboración.
2. Partes [20](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), [27](../classes/part-27-arquitectura-de-software-y-dominio/README.md)–[32](../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md) para cargas, arquitectura, datos y distribución.
3. [Parte 33 — Cloud, plataforma e infraestructura](../classes/part-33-cloud-plataforma-e-infraestructura/README.md).
4. Partes [36](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), [38](../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)–[41](../classes/part-41-observabilidad-sre-e-incidentes/README.md) y [43](../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md) para resiliencia, seguridad, entrega, SRE y continuidad.

<!-- role-depth:start -->
## 🗺️ Sistema profesional del rol

```mermaid
flowchart LR
    A["🎯 Cuenta"] --> B
    B["🧠 Identidad"] --> C
    C["🛠️ Infraestructura"] --> D
    D["🔎 Servicio"] --> E["📈 Recuperación"]
    classDef intent fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef work fill:#ddf4ff,stroke:#0969da,color:#24292f
    classDef proof fill:#dafbe1,stroke:#1a7f37,color:#24292f
    class A intent
    class B,C,D work
    class E proof
```

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **☁️ Cloud Engineer**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: Diseña y automatiza capacidades cloud seguras, observables, recuperables y económicamente defendibles sin quedar atrapado en servicios por accidente. Cada transición
debe conservar supuestos, responsables y una forma de volver atrás.

<table>
<tr>
<td valign="top" width="50%">

### 🎯 Responde por

- decisiones propias de la familia **Cloud**;
- el resultado observable, no sólo la actividad ejecutada;
- límites, riesgos, operación y deuda residual de su intervención;
- evidencia que otra persona pueda revisar o reproducir.

</td>
<td valign="top" width="50%">

### 🤝 Coordina con

- [🚚 DevOps Engineer](devops-engineer.md); [🛤️ Platform Engineer](platform-engineer.md); [🔐 Security Engineer](security-engineer.md);
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
| 1 | [Parte 03 · Redes, Internet y protocolos](../classes/part-03-redes-internet-y-protocolos/README.md) | desarrollada | [SE-039 · IPv4, IPv6, subredes, rutas y NAT](../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md)<br>[SE-041 · DNS, nombres, resolución y fallos](../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md)<br>[SE-043 · TLS, certificados y confianza en tránsito](../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md)<br>[SE-044 · Proxies, balanceadores, gateways y CDN](../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md) | Profundiza **redes, protocolos y fallos de comunicación** desde la responsabilidad del rol. | Traza de una petición bajo fallos. |
| 2 | [Parte 23 · Runtimes y plataformas modernas](../classes/part-23-runtimes-y-plataformas-modernas/README.md) | desarrollada | [SE-280 · GPU y aceleradores: modelo de ejecución](../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md)<br>[SE-281 · Rendimiento y costo en aceleradores](../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md)<br>[SE-282 · Contenedores, microVM y sandboxes](../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md)<br>[SE-283 · Hardware seguro: TEE y atestación](../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md)<br>[SE-286 · Confianza cero en la práctica](../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md) | Profundiza **runtimes, aislamiento, aceleradores y confianza** desde la responsabilidad del rol. | Plataforma de ejecución aislada con evidencia. |
| 3 | [Parte 32 · Concurrencia y sistemas distribuidos](../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md) | desarrollada | [SE-389 · Fallos parciales y modelos de red](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md)<br>[SE-390 · Consistencia, disponibilidad y particiones](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md)<br>[SE-393 · Replicación, sharding y balanceo](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md)<br>[SE-394 · Caos controlado y pruebas de distribución](../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md) | Profundiza **concurrencia, coordinación y fallos parciales** desde la responsabilidad del rol. | Experimento distribuido de degradación. |
| 4 | [Parte 33 · Cloud, plataforma e infraestructura](../classes/part-33-cloud-plataforma-e-infraestructura/README.md) | desarrollada | [SE-397 · IaaS, PaaS, SaaS y responsabilidad compartida](../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md)<br>[SE-399 · Orquestación y scheduling](../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md)<br>[SE-401 · Redes, identidad y secretos en cloud](../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md)<br>[SE-402 · Infraestructura como código y estado](../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md)<br>[SE-404 · Escalado, capacidad y costos](../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md)<br>[SE-408 · Proyecto: plataforma mínima reproducible](../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md) | Profundiza **cloud, infraestructura y plataformas** desde la responsabilidad del rol. | Entorno reproducible y eliminable. |
| 5 | [Parte 36 · Calidad, rendimiento y resiliencia](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) | desarrollada | [SE-436 · Latencia, throughput, saturación y capacidad](../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)<br>[SE-438 · Timeouts, retries, backoff y jitter](../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md)<br>[SE-439 · Circuit breakers, bulkheads y degradación](../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md)<br>[SE-440 · Disponibilidad, durabilidad y recuperación](../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) | Profundiza **calidad, rendimiento y resiliencia** desde la responsabilidad del rol. | Informe medido y game day. |
| 6 | [Parte 38 · Seguridad, privacidad y cumplimiento](../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md) | desarrollada | [SE-457 · Principios de seguridad y modelos de amenaza](../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md)<br>[SE-459 · Autorización, recursos y mínimo privilegio](../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md)<br>[SE-461 · Criptografía aplicada y gestión de claves](../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md)<br>[SE-462 · Secretos, configuración y separación de ambientes](../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md) | Profundiza **seguridad, privacidad y cumplimiento** desde la responsabilidad del rol. | Controles con pruebas y evidencia. |
| 7 | [Parte 40 · CI/CD, IaC y platform engineering](../classes/part-40-ci-cd-iac-y-platform-engineering/README.md) | desarrollada | [SE-484 · Credenciales efímeras y OIDC](../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md)<br>[SE-486 · Infraestructura como código en pipeline](../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md)<br>[SE-487 · GitOps y reconciliación](../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md)<br>[SE-488 · Entornos preview y datos seguros](../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) | Profundiza **CI/CD, IaC, plataforma y DevEx** desde la responsabilidad del rol. | Camino autoservicio con rollback. |
| 8 | [Parte 41 · Observabilidad, SRE e incidentes](../classes/part-41-observabilidad-sre-e-incidentes/README.md) | desarrollada | [SE-495 · Métricas, dimensiones y cardinalidad](../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md)<br>[SE-497 · SLI, SLO, SLA y presupuestos de error](../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)<br>[SE-498 · Alertas accionables y fatiga](../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md)<br>[SE-502 · Continuidad, disaster recovery y ejercicios](../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md) | Profundiza **observabilidad, SRE e incidentes** desde la responsabilidad del rol. | Incidente diagnosticado y recuperado. |

### ✅ Clases ya desarrolladas que sostienen la ruta hoy

El núcleo anterior apunta a la capacidad profesional completa. Estas clases de apoyo,
de las Partes [00](../classes/part-00-ingenieria-de-software-como-profesion/README.md)–[50](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) (`SE-001`–`SE-612`), también tienen contenido desarrollado y
permiten practicar el rol desde otros ángulos:

| Clase desarrollada | Parte |
| --- | --- |
| [SE-031 · Variables de entorno, configuración y secretos](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) | [Parte 02](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md) |
| [SE-034 · Virtualización, WSL y aislamiento local](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) | [Parte 02](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md) |
| [SE-211 · Runbooks, playbooks y documentación operacional](../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md) | [Parte 17](../classes/part-17-documentacion-y-conocimiento-tecnico/README.md) |
| [SE-250 · Health, readiness y shutdown ordenado](../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) | [Parte 20](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) |
| [SE-331 · Arquitecturas serverless, edge y peer-to-peer](../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) | [Parte 27](../classes/part-27-arquitectura-de-software-y-dominio/README.md) |
| [SE-398 · Máquinas virtuales, contenedores y aislamiento](../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) | [Parte 33](../classes/part-33-cloud-plataforma-e-infraestructura/README.md) |
| [SE-400 · Serverless y ejecución gestionada](../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md) | [Parte 33](../classes/part-33-cloud-plataforma-e-infraestructura/README.md) |
| [SE-403 · Entornos, cuentas y separación de responsabilidades](../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) | [Parte 33](../classes/part-33-cloud-plataforma-e-infraestructura/README.md) |
| [SE-405 · Multi-cloud, híbrido y portabilidad real](../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) | [Parte 33](../classes/part-33-cloud-plataforma-e-infraestructura/README.md) |
| [SE-406 · Plataformas internas y golden paths](../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) | [Parte 33](../classes/part-33-cloud-plataforma-e-infraestructura/README.md) |
| [SE-407 · Taller: desplegar y destruir un entorno seguro](../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md) | [Parte 33](../classes/part-33-cloud-plataforma-e-infraestructura/README.md) |
| [SE-357 · Backups, restauración y pruebas de recuperación](../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) | [Parte 29](../classes/part-29-datos-persistencia-y-recuperacion/README.md) |
| [SE-320 · Resiliencia: timeout, retry con jitter y circuit breaker](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) | [Parte 26](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md) |
| [SE-321 · Resiliencia: bulkhead, sidecar, ambassador y degradación](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) | [Parte 26](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md) |
| [SE-342 · Multi-tenancy y aislamiento](../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md) | [Parte 28](../classes/part-28-estilos-arquitectonicos/README.md) |
| [SE-344 · Arquitectura celular y radio de impacto](../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md) | [Parte 28](../classes/part-28-estilos-arquitectonicos/README.md) |
| [SE-345 · 12-factor y aplicaciones nativas de la nube](../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md) | [Parte 28](../classes/part-28-estilos-arquitectonicos/README.md) |
| [SE-370 · Costos y operación de plataformas de datos](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md) | [Parte 30](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md) |
| [SE-505 · Principios de la ingeniería del caos: estado estable e hipótesis](../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md) | [Parte 42](../classes/part-42-ingenieria-del-caos/README.md) |
| [SE-510 · Fallos de datos y de estado: réplicas, particiones y corrupción](../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) | [Parte 42](../classes/part-42-ingenieria-del-caos/README.md) |
| [SE-516 · Proyecto: programa de caos de un servicio con evidencia y remediación](../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md) | [Parte 42](../classes/part-42-ingenieria-del-caos/README.md) |

**Cómo recorrerla.** Empieza por [SE-039](../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md) para fijar el
primer mecanismo, usa [SE-404](../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md) para integrar el
centro de la especialidad y llega a [SE-502](../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md) cuando ya
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
| **Gestionado o autogestionado** | Comparar control carga operativa lock-in y recuperación. | TCO más prueba de salida. |
| **Una cuenta o separación** | Aislar riesgo blast radius facturación y deberes. | Policy y ejercicio de credenciales. |
| **Multi-cloud o profundidad** | Exigir necesidad de negocio antes de duplicar complejidad. | Escenario de continuidad y costes reales. |

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **Gestionado o autogestionado**, **Una cuenta o separación**
y **Multi-cloud o profundidad** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: Una credencial comprometida modifica infraestructura crítica

**Síntoma.** Un principal de CI tiene permisos y duración excesivos. La respuesta madura evita convertir la primera
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
2. **Investigar:** Rastrear identidad sesión policy cloud trail estado y recursos. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** Revocar contener reconciliar IaC rotar confianza y verificar impacto. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
| **Cambios fuera de IaC** | Drift que rompe reproducibilidad y control. | Medir sólo recursos importados. |
| **Costo por servicio** | Consumo asociado a outcome y capacidad. | Premiar ahorro que reduce resiliencia. |
| **Recuperación por región** | RTO y RPO observados ante pérdida. | Aceptar arquitectura en papel. |

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: Entorno cloud mínimo seguro

**Propósito:** crear y destruir una plataforma con identidad efímera separación y recuperación. El resultado esperado es **IaC policy OIDC estimación de coste despliegue multi-entorno alertas y ejercicio de restauración**.

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

1. ¿En qué contexto elegirías **Gestionado o autogestionado** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **Una credencial comprometida modifica infraestructura crítica**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **Entorno cloud mínimo seguro** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

- [Kubernetes Documentation](https://kubernetes.io/docs/) — **CNCF / Kubernetes**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [Terraform language documentation](https://developer.hashicorp.com/terraform/language) — **HashiCorp**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [Secure Software Development Framework SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) — **NIST**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.
<!-- role-depth:end -->

## 🧪 Evidencia de portafolio

- IaC reproducible con plan, políticas y destrucción segura;
- matriz IAM con prueba de privilegio negativo;
- estimación de coste y alertas de anomalía;
- ejercicio de restauración y failover documentado.

## 📈 Progresión

Systems/DevOps Engineer → Cloud Engineer → Senior/Staff Cloud → Platform o Architect.

## ⚠️ Mitos frecuentes

- “Cloud elimina operaciones.” Cambia su interfaz y reparto de responsabilidades.
- “Serverless no tiene servidores.” Tiene límites, regiones, cold starts y coste.
- “IaC garantiza reproducibilidad.” También importan estado, imágenes y dependencias.

## 🚀 Siguientes pasos

1. Modela identidad, red, datos y coste antes del servicio.
2. Aprovisiona y destruye un entorno sin pasos manuales ocultos.
3. Pierde una dependencia y ejecuta recuperación.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
