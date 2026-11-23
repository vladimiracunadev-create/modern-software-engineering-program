# 🛤️ Platform Engineer
<!-- role-visual:start -->
<div align="center">

[![Familia](https://img.shields.io/badge/familia-Plataforma-6f42c1?style=for-the-badge)](README.md)
[![Nivel](https://img.shields.io/badge/recorrido-senior%20%E2%86%92%20principal-0969da?style=for-the-badge)](../ROADMAP.md)
[![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-P09%20%C2%B7%20P23%20%C2%B7%20P28%20%C2%B7%20P30%20%C2%B7%20P33%20%C2%B7%20P40%20%C2%B7%20P44%20%C2%B7%20P50-2da44e?style=for-the-badge)](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>
<!-- role-visual:end -->


> Construye una plataforma interna como producto: capacidades autoservicio que permiten
> a los equipos entregar software con menos carga cognitiva y mejores defaults.
>
> **Entrada habitual:** senior · **Foco:** IDP, golden paths y experiencia de desarrollo
> · **Evidencia central:** camino autoservicio adoptado y medido por sus usuarios

## 🧭 Qué es y por qué importa

Platform engineering aparece cuando cada equipo reinventa pipelines, observabilidad,
identidad y despliegue. La plataforma empaqueta capacidades repetibles detrás de APIs,
plantillas y documentación. Se gestiona como producto interno: discovery, roadmap,
soporte, métricas y posibilidad de decir no.

## 🗓️ Un día en el puesto

- entrevistar equipos para detectar fricción recurrente;
- diseñar una API o plantilla de plataforma;
- mantener pipelines y componentes compartidos;
- mejorar onboarding, documentación y feedback;
- medir adopción, tiempo hasta producción y fallos del camino;
- gestionar compatibilidad y deprecación sin bloquear a consumidores.

## ✅ Responsabilidades y límites

- Responde por una capacidad interna útil, confiable y comprensible.
- Define defaults seguros con escapes explícitos.
- No impone herramientas sin discovery ni evidencia de beneficio.
- No se convierte en equipo de tickets para cada despliegue.
- No mide éxito por recursos aprovisionados, sino por outcomes de equipos.

## 🧠 Qué necesitas saber

- APIs, identidad, automatización, cloud, containers e IaC;
- CI/CD, artefactos, cadena de suministro y observabilidad;
- diseño de producto, entrevistas y priorización;
- developer portals, service catalogs, golden paths y Backstage como caso;
- DevEx, cognitive load, DORA y SPACE con guardrails;
- contratos, versionado, soporte, SLO y FinOps.

## 📚 Tu ruta en el programa

1. Partes [08](../classes/part-08-entornos-herramientas-y-depuracion/README.md)–[09](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md) para herramientas, entornos y experiencia de desarrollo.
2. Partes [10](../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)–[11](../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md) para discovery, economía y medición.
3. Partes [16](../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)–[20](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) para colaboración, documentación, automatización y APIs.
4. [Parte 33](../classes/part-33-cloud-plataforma-e-infraestructura/README.md) para cloud e infraestructura.
5. [Parte 39](../classes/part-39-build-release-y-cadena-de-suministro/README.md), [Parte 40 — CI/CD, IaC y platform engineering](../classes/part-40-ci-cd-iac-y-platform-engineering/README.md) y [Parte 41](../classes/part-41-observabilidad-sre-e-incidentes/README.md) para cadena de suministro, entrega, DevEx, observabilidad y SRE.
6. [Parte 44](../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md) para diseño organizacional; partes 46–47 para plataforma de agentes.

<!-- role-depth:start -->
## 🗺️ Sistema profesional del rol

![Diagrama de flujo con 5 pasos. Recorrido: «🎯 Necesidad interna»; luego «🧠 Capacidad»; luego «🛠️ Golden path»; luego «🔎 Adopción»; luego «📈 Evolución».](../site/assets/figures/mermaid-6544c9631c.svg)

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **🛤️ Platform Engineer**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: Construye una plataforma interna como producto: capacidades autoservicio que permiten a los equipos entregar software con menos carga cognitiva y mejores defaults. Cada transición
debe conservar supuestos, responsables y una forma de volver atrás.

<table>
<tr>
<td valign="top" width="50%">

### 🎯 Responde por

- decisiones propias de la familia **Plataforma**;
- el resultado observable, no sólo la actividad ejecutada;
- límites, riesgos, operación y deuda residual de su intervención;
- evidencia que otra persona pueda revisar o reproducir.

</td>
<td valign="top" width="50%">

### 🤝 Coordina con

- [🧰 Developer Experience Engineer](developer-experience-engineer.md); [🚚 DevOps Engineer](devops-engineer.md); [🧭 Staff / Principal Engineer y Technical Lead](technical-leadership.md); [🧬 MLOps / ML Platform Engineer](mlops-ml-platform-engineer.md); [🏢 SaaS / Product Platform Engineer](saas-product-platform-engineer.md);
- producto y personas usuarias cuando cambia una tarea o outcome;
- seguridad, privacidad, accesibilidad y operación según el riesgo;
- quienes mantendrán el sistema después de la entrega.

</td>
</tr>
</table>

El título no concede autoridad automática. El alcance real depende del equipo, la
industria y la criticidad. Esta guía describe un recorrido desde **senior → principal**, pero una
vacante se evalúa por las decisiones que permite tomar, los sistemas que pone bajo
responsabilidad y la evidencia exigida, no por el nombre del cargo.

## 🧱 Partes y clases asociadas

La ruta distingue **parte** —unidad curricular con una capacidad acumulativa— de
**clase asociada** —punto concreto donde se estudia un mecanismo o una decisión. Las
clases siguientes forman el núcleo; no eliminan los prerrequisitos indicados en sus
propias páginas ni convierten en opcional la base común.

| Orden | Parte del programa | Estado | Clases clave | Por qué entra en esta ruta | Evidencia de transferencia |
| ---: | --- | --- | --- | --- | --- |
| 1 | [Parte 09 · Bibliotecas, paquetes, SDK y automatización](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md) | desarrollada | [SE-109 · Biblioteca, framework, runtime, plataforma y SDK](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md)<br>[SE-113 · CLI, flags, configuración y códigos de salida](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-113-cli-flags-configuracion-y-codigos-de-salida/README.md)<br>[SE-115 · Plugins, extensiones y puntos de integración](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md)<br>[SE-118 · Diseño de experiencia para desarrolladores](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md)<br>[SE-119 · Taller: empaquetar una capacidad reusable](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-119-taller-empaquetar-una-capacidad-reusable/README.md)<br>[SE-120 · Proyecto: SDK y CLI con compatibilidad verificada](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md) | Profundiza **paquetes, SDK, dependencias y compatibilidad** desde la responsabilidad del rol. | Paquete versionado y consumible. |
| 2 | [Parte 23 · Runtimes y plataformas modernas](../classes/part-23-runtimes-y-plataformas-modernas/README.md) | desarrollada | [SE-278 · WebAssembly en servidor y borde: component model](../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md)<br>[SE-282 · Contenedores, microVM y sandboxes](../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md)<br>[SE-286 · Confianza cero en la práctica](../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md)<br>[SE-287 · Taller: elegir y aislar un runtime para una carga no confiable](../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md) | Profundiza **runtimes, aislamiento, aceleradores y confianza** desde la responsabilidad del rol. | Plataforma de ejecución aislada con evidencia. |
| 3 | [Parte 28 · Estilos arquitectónicos](../classes/part-28-estilos-arquitectonicos/README.md) | desarrollada | [SE-338 · Microkernel y arquitecturas de plugins](../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md)<br>[SE-341 · BFF, API gateway y service mesh](../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md)<br>[SE-342 · Multi-tenancy y aislamiento](../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md)<br>[SE-344 · Arquitectura celular y radio de impacto](../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md)<br>[SE-345 · 12-factor y aplicaciones nativas de la nube](../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md) | Profundiza **estilos arquitectónicos y sus fuerzas de calidad** desde la responsabilidad del rol. | Decisión arquitectónica defendida con ADR. |
| 4 | [Parte 30 · Ingeniería de datos y plataformas de datos](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md) | desarrollada | [SE-366 · Contratos de datos y evolución de esquemas](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md)<br>[SE-367 · Linaje, catálogo y metadatos](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md)<br>[SE-370 · Costos y operación de plataformas de datos](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md)<br>[SE-372 · Proyecto: plataforma de datos mínima gobernada](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md) | Profundiza **plataformas de datos, calidad, contratos y gobierno** desde la responsabilidad del rol. | Plataforma de datos mínima gobernada. |
| 5 | [Parte 33 · Cloud, plataforma e infraestructura](../classes/part-33-cloud-plataforma-e-infraestructura/README.md) | desarrollada | [SE-398 · Máquinas virtuales, contenedores y aislamiento](../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md)<br>[SE-399 · Orquestación y scheduling](../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md)<br>[SE-402 · Infraestructura como código y estado](../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md)<br>[SE-403 · Entornos, cuentas y separación de responsabilidades](../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md)<br>[SE-406 · Plataformas internas y golden paths](../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md)<br>[SE-408 · Proyecto: plataforma mínima reproducible](../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md) | Profundiza **cloud, infraestructura y plataformas** desde la responsabilidad del rol. | Entorno reproducible y eliminable. |
| 6 | [Parte 40 · CI/CD, IaC y platform engineering](../classes/part-40-ci-cd-iac-y-platform-engineering/README.md) | desarrollada | [SE-484 · Credenciales efímeras y OIDC](../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md)<br>[SE-486 · Infraestructura como código en pipeline](../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md)<br>[SE-487 · GitOps y reconciliación](../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md)<br>[SE-489 · Developer portals y capacidades de plataforma](../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md)<br>[SE-490 · Métricas DORA y mejora sin gaming](../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md)<br>[SE-492 · Proyecto: camino a producción con rollback](../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md) | Profundiza **CI/CD, IaC, plataforma y DevEx** desde la responsabilidad del rol. | Camino autoservicio con rollback. |
| 7 | [Parte 44 · Gestión, liderazgo y práctica profesional](../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md) | desarrollada | [SE-530 · Diseño de equipos y ownership](../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md)<br>[SE-531 · Comunicación, facilitación y conflicto](../classes/part-44-gestion-liderazgo-y-practica-profesional/se-531-comunicacion-facilitacion-y-conflicto/README.md)<br>[SE-535 · Compras, proveedores y evaluación técnica](../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md)<br>[SE-537 · Economía del software y costo total](../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md) | Profundiza **liderazgo, organización y decisiones** desde la responsabilidad del rol. | Propuesta defendida ante conflicto. |
| 8 | [Parte 50 · Machine learning en producción y MLOps](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) | desarrollada | [SE-601 · Ciclo de vida de ML y por qué falla en producción](../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md)<br>[SE-603 · Experimentos y entrenamiento reproducible](../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md)<br>[SE-606 · Servir modelos: latencia, lotes y GPU](../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md)<br>[SE-607 · Despliegue seguro de modelos: shadow, canary y rollback](../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md)<br>[SE-608 · Monitoreo, deriva y reentrenamiento](../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) | Profundiza **machine learning en producción, MLOps y gobierno de IA** desde la responsabilidad del rol. | Sistema de ML operable con evidencia. |

### ✅ Clases ya desarrolladas que sostienen la ruta hoy

El núcleo anterior apunta a la capacidad profesional completa. Estas clases de apoyo,
de las Partes [00](../classes/part-00-ingenieria-de-software-como-profesion/README.md)–[50](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) (`SE-001`–`SE-612`), también tienen contenido desarrollado y
permiten practicar el rol desde otros ángulos:

| Clase desarrollada | Parte |
| --- | --- |
| [SE-104 · Dev Containers y entornos desechables](../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md) | [Parte 08](../classes/part-08-entornos-herramientas-y-depuracion/README.md) |
| [SE-114 · Scripting repetible y tareas idempotentes](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md) | [Parte 09](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md) |
| [SE-212 · Docs as code, revisión y publicación](../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) | [Parte 17](../classes/part-17-documentacion-y-conocimiento-tecnico/README.md) |
| [SE-225 · Distribución de binarios y actualizaciones](../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) | [Parte 18](../classes/part-18-cli-tui-servicios-y-automatizacion/README.md) |
| [SE-334 · Arquitectura socio-técnica y límites de equipo](../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md) | [Parte 27](../classes/part-27-arquitectura-de-software-y-dominio/README.md) |
| [SE-470 · Artefactos, repositorios y promoción](../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md) | [Parte 39](../classes/part-39-build-release-y-cadena-de-suministro/README.md) |
| [SE-472 · SBOM, procedencia y atestaciones](../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) | [Parte 39](../classes/part-39-build-release-y-cadena-de-suministro/README.md) |
| [SE-476 · Canary, blue-green y rollback](../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) | [Parte 39](../classes/part-39-build-release-y-cadena-de-suministro/README.md) |
| [SE-578 · Instrucciones de repositorio y cumplimiento determinista](../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md) | [Parte 48](../classes/part-48-harness-y-agentic-engineering/README.md) |
| [SE-579 · Herramientas, permisos y superficies de acción](../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md) | [Parte 48](../classes/part-48-harness-y-agentic-engineering/README.md) |
| [SE-582 · Sandboxes, reversibilidad y control de daño](../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md) | [Parte 48](../classes/part-48-harness-y-agentic-engineering/README.md) |
| [SE-482 · Pipelines, jobs, matrices y cachés](../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md) | [Parte 40](../classes/part-40-ci-cd-iac-y-platform-engineering/README.md) |
| [SE-483 · Tests, seguridad y políticas como gates](../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md) | [Parte 40](../classes/part-40-ci-cd-iac-y-platform-engineering/README.md) |
| [SE-409 · Qué hace distinto a un producto SaaS](../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) | [Parte 34](../classes/part-34-saas-y-plataformas-de-producto/README.md) |
| [SE-414 · Planes, derechos de uso y banderas de funcionalidad](../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) | [Parte 34](../classes/part-34-saas-y-plataformas-de-producto/README.md) |
| [SE-420 · Taller y proyecto integrador: producto SaaS mínimo con evidencia](../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md) | [Parte 34](../classes/part-34-saas-y-plataformas-de-producto/README.md) |
| [SE-505 · Principios de la ingeniería del caos: estado estable e hipótesis](../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md) | [Parte 42](../classes/part-42-ingenieria-del-caos/README.md) |
| [SE-510 · Fallos de datos y de estado: réplicas, particiones y corrupción](../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) | [Parte 42](../classes/part-42-ingenieria-del-caos/README.md) |
| [SE-516 · Proyecto: programa de caos de un servicio con evidencia y remediación](../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md) | [Parte 42](../classes/part-42-ingenieria-del-caos/README.md) |

**Cómo recorrerla.** Empieza por [SE-109](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md) para fijar el
primer mecanismo, usa [SE-399](../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md) para integrar el
centro de la especialidad y llega a [SE-608](../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md) cuando ya
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
| **Estandarizar o permitir excepción** | Ofrecer camino recomendado con escape explícito y soporte. | Adopción voluntaria más coste de excepción. |
| **Build o comprar plataforma** | Comparar diferenciación integración TCO y salida. | Experimento de onboarding y análisis económico. |
| **API o portal** | Diseñar capacidad estable antes que interfaz vistosa. | Tiempo hasta primer éxito y consumo automatizado. |

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **Estandarizar o permitir excepción**, **Build o comprar plataforma**
y **API o portal** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: Golden path falla y bloquea decenas de equipos

**Síntoma.** Una actualización central rompe un supuesto no versionado. La respuesta madura evita convertir la primera
correlación en causa y conserva evidencia antes de modificar el sistema.

![Diagrama de flujo con 6 pasos. Recorrido: «⚠️ Síntoma»; luego «🔎 Hipótesis»; luego «🧯 Contención»; luego «🧠 Diagnóstico»; luego «🛠️ Recuperación»; luego «📚 Prevención».](../site/assets/figures/mermaid-637bdc6ac9.svg)

**Cómo leer el diagrama:** empieza en «⚠️ Síntoma» y sigue las flechas hasta el final del recorrido. Las filas se leen como una serpentina: de izquierda a derecha y, en la fila siguiente, de derecha a izquierda.

1. **Detectar y delimitar:** identifica quién o qué está afectado, desde cuándo y qué
   cambió. Conserva timestamps, versiones, entradas y señales suficientes para no
   destruir la escena al intentar arreglarla.
2. **Investigar:** Identificar contrato plantilla versión dependencia blast radius y salida. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** Pausar rollout revertir ofrecer bypass seguro y añadir compatibilidad. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
| **Tiempo hasta primer despliegue** | Fricción desde repositorio nuevo hasta entorno útil. | Ensayar sólo con expertos. |
| **Adopción activa** | Equipos que usan y conservan la capacidad. | Contar repos creados. |
| **Carga cognitiva percibida** | Decisiones y conocimiento exigidos al consumidor. | Reducir opciones ocultando fallos. |

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: Plataforma interna como producto

**Propósito:** convertir una necesidad repetida en autoservicio medido y versionado. El resultado esperado es **API plantilla portal documentación SLO telemetría feedback modelo de soporte y deprecación**.

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

1. ¿En qué contexto elegirías **Estandarizar o permitir excepción** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **Golden path falla y bloquea decenas de equipos**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **Plataforma interna como producto** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

- [Kubernetes Documentation](https://kubernetes.io/docs/) — **CNCF / Kubernetes**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [DORA software delivery performance metrics](https://dora.dev/guides/dora-metrics/) — **Google Cloud**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — **IEEE Computer Society**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.
<!-- role-depth:end -->

## 🧪 Evidencia de portafolio

- entrevista y mapa de fricción de equipos consumidores;
- golden path que crea, prueba, publica y observa un servicio;
- API de plataforma con compatibilidad y deprecación;
- portal o catálogo mínimo con ownership y documentación;
- métricas de adopción, satisfacción y tiempo de feedback con límites;
- cálculo de coste y decisión build-vs-buy.

## 📈 Progresión

DevOps/SRE/Backend Senior → Platform Engineer → Senior/Staff Platform → Platform Lead
o Architect. El crecimiento cambia de automatizar recursos a diseñar un ecosistema
que muchos equipos pueden evolucionar.

## ⚠️ Mitos frecuentes

- “Plataforma es Kubernetes.” Kubernetes puede ser una implementación, no el producto.
- “El portal es la plataforma.” Sin capacidades detrás es solo una interfaz.
- “Golden path significa único camino.” Debe ser recomendado, no una cárcel.
- “Los desarrolladores son usuarios cautivos.” La baja adopción sigue siendo un fallo de producto.

## 🚀 Siguientes pasos

1. Identifica una fricción repetida en tres equipos.
2. Diseña la capacidad mínima y su contrato antes del portal.
3. Prueba el onboarding con una persona no autora.
4. Mide adopción y feedback; retira lo que no resuelva el problema.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
