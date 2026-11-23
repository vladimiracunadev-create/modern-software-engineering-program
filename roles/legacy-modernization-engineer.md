# 🏚️ Legacy Modernization Engineer
<!-- role-visual:start -->
<div align="center">

[![Familia](https://img.shields.io/badge/familia-Evoluci%C3%B3n-6f42c1?style=for-the-badge)](README.md)
[![Nivel](https://img.shields.io/badge/recorrido-senior%20%E2%86%92%20principal-0969da?style=for-the-badge)](../ROADMAP.md)
[![Núcleo](https://img.shields.io/badge/n%C3%BAcleo-P08%20%C2%B7%20P25%20%C2%B7%20P28%20%C2%B7%20P29%20%C2%B7%20P30%20%C2%B7%20P31%20%C2%B7%20P39%20%C2%B7%20P43%20%C2%B7%20P44-2da44e?style=for-the-badge)](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>
<!-- role-visual:end -->


> Comprende y cambia sistemas críticos existentes sin perder continuidad, datos ni
> conocimiento; moderniza por evidencia, no por desprecio a lo antiguo.
>
> **Entrada habitual:** senior · **Foco:** brownfield, compatibilidad y migraciones ·
> **Evidencia central:** cambio incremental reversible sobre un sistema ajeno

## 🧭 Qué es y por qué importa

Legacy no significa simplemente tecnología vieja. Es software valioso cuyo cambio es
arriesgado por acoplamiento, conocimiento perdido, dependencias obsoletas o falta de
pruebas. Modernizar requiere arqueología, caracterización y estrategia. Reescribir es
una opción extrema, no el punto de partida.

## 🗓️ Un día en el puesto

- entrevistar usuarios y operadores para recuperar conocimiento;
- mapear dependencias, datos y flujos sin documentación confiable;
- capturar comportamiento con pruebas de caracterización;
- aislar un límite mediante adapter o anti-corruption layer;
- ejecutar migración progresiva y reconciliar resultados;
- planificar deprecación, archivo, retención y retiro seguro.

## ✅ Responsabilidades y límites

- Preserva comportamiento valioso antes de cambiarlo.
- Declara incertidumbre y crea checkpoints reversibles.
- No reescribe para mejorar estética ni adoptar una moda.
- No migra datos sin conciliación, backup y rollback.
- No retira un sistema sin ownership, retención y dependencias verificadas.

## 🧠 Qué necesitas saber

- lectura de código, depuración e ingeniería inversa;
- characterization tests, dependency mapping y análisis de datos;
- strangler fig, branch by abstraction y anti-corruption layer;
- rehost, replatform, refactor, rearchitect y rewrite;
- migraciones de API, esquema y datos con compatibilidad;
- EOL, decommissioning, archivo, retención y borrado seguro.

## 📚 Tu ruta en el programa

1. [Parte 08](../classes/part-08-entornos-herramientas-y-depuracion/README.md) para investigación y debugging; partes 12–13 para reconstruir contratos.
2. Partes [16](../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)–[17](../classes/part-17-documentacion-y-conocimiento-tecnico/README.md) para historia, colaboración y documentación.
3. Partes [25](../classes/part-25-diseno-patrones-y-refactorizacion/README.md), [27](../classes/part-27-arquitectura-de-software-y-dominio/README.md), [29](../classes/part-29-datos-persistencia-y-recuperacion/README.md) y [31](../classes/part-31-integracion-eventos-y-mensajeria/README.md)–[32](../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md) para refactorización, arquitectura, datos e integración.
4. Partes [35](../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)–[36](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) y [38](../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)–[41](../classes/part-41-observabilidad-sre-e-incidentes/README.md) para caracterización, resiliencia, seguridad, entrega y observabilidad.
5. [Parte 43 — Mantenimiento y modernización legacy](../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md).
6. Partes [44](../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md) y [46](../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)–[47](../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md) para cambio organizacional e IA controlada sobre brownfield.

<!-- role-depth:start -->
## 🗺️ Sistema profesional del rol

![Diagrama de flujo con 5 pasos. Recorrido: «🎯 Descubrir»; luego «🧠 Caracterizar»; luego «🛠️ Aislar»; luego «🔎 Migrar»; luego «📈 Retirar».](../site/assets/figures/mermaid-741de2704b.svg)

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **🏚️ Legacy Modernization Engineer**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: Comprende y cambia sistemas críticos existentes sin perder continuidad, datos ni conocimiento; moderniza por evidencia, no por desprecio a lo antiguo. Cada transición
debe conservar supuestos, responsables y una forma de volver atrás.

<table>
<tr>
<td valign="top" width="50%">

### 🎯 Responde por

- decisiones propias de la familia **Evolución**;
- el resultado observable, no sólo la actividad ejecutada;
- límites, riesgos, operación y deuda residual de su intervención;
- evidencia que otra persona pueda revisar o reproducir.

</td>
<td valign="top" width="50%">

### 🤝 Coordina con

- [🏛️ Software Architect](software-architect.md); [🗄️ Database Reliability Engineer](database-reliability-engineer.md); [🧭 Staff / Principal Engineer y Technical Lead](technical-leadership.md);
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
| 1 | [Parte 08 · Entornos, herramientas y depuración](../classes/part-08-entornos-herramientas-y-depuracion/README.md) | desarrollada | [SE-098 · Depuradores, breakpoints y observación de estado](../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md)<br>[SE-099 · Profilers de CPU, memoria, I/O y red](../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md)<br>[SE-105 · Reproducción de errores y reducción de casos](../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md)<br>[SE-107 · Taller: diagnosticar un fallo desconocido](../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md) | Profundiza **depuración, profiling y reproducción de fallos** desde la responsabilidad del rol. | Expediente de causa raíz. |
| 2 | [Parte 25 · Diseño, patrones y refactorización](../classes/part-25-diseno-patrones-y-refactorizacion/README.md) | desarrollada | [SE-306 · Code smells y diagnóstico contextual](../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md)<br>[SE-307 · Refactorización segura apoyada por pruebas](../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md)<br>[SE-309 · Complejidad accidental y esencial](../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md)<br>[SE-310 · Deuda técnica, interés y opciones](../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md)<br>[SE-311 · Taller: refactorizar sin alterar comportamiento](../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md)<br>[SE-312 · Proyecto: evolución compatible de un componente](../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md) | Profundiza **diseño, patrones y refactorización segura** desde la responsabilidad del rol. | Evolución compatible protegida por pruebas. |
| 3 | [Parte 28 · Estilos arquitectónicos](../classes/part-28-estilos-arquitectonicos/README.md) | desarrollada | [SE-337 · Estilos como respuestas a fuerzas de calidad](../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md)<br>[SE-340 · Microservicios y sus costes reales](../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md)<br>[SE-346 · Evolución y migración entre estilos](../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md)<br>[SE-348 · Proyecto: decisión arquitectónica defendida con ADR](../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md) | Profundiza **estilos arquitectónicos y sus fuerzas de calidad** desde la responsabilidad del rol. | Decisión arquitectónica defendida con ADR. |
| 4 | [Parte 29 · Datos, persistencia y recuperación](../classes/part-29-datos-persistencia-y-recuperacion/README.md) | desarrollada | [SE-352 · Restricciones, invariantes y consistencia](../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md)<br>[SE-354 · Migraciones compatibles y evolución de esquema](../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md)<br>[SE-357 · Backups, restauración y pruebas de recuperación](../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md)<br>[SE-359 · Taller: corregir una migración peligrosa](../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) | Profundiza **persistencia, transacciones y recuperación** desde la responsabilidad del rol. | Capa de datos restaurable. |
| 5 | [Parte 30 · Ingeniería de datos y plataformas de datos](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md) | desarrollada | [SE-361 · Del dato operacional al analítico](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md)<br>[SE-364 · Transformación y orquestación idempotente con backfills](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md)<br>[SE-366 · Contratos de datos y evolución de esquemas](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md)<br>[SE-367 · Linaje, catálogo y metadatos](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) | Profundiza **plataformas de datos, calidad, contratos y gobierno** desde la responsabilidad del rol. | Plataforma de datos mínima gobernada. |
| 6 | [Parte 31 · Integración, eventos y mensajería](../classes/part-31-integracion-eventos-y-mensajeria/README.md) | desarrollada | [SE-378 · CDC, ETL, ELT y sincronización](../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md)<br>[SE-380 · Compatibilidad de esquemas y registros](../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md)<br>[SE-381 · Anti-corruption layers y traducción de modelos](../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md)<br>[SE-384 · Proyecto: flujo integrado tolerante a reintentos](../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) | Profundiza **eventos, mensajería y compatibilidad** desde la responsabilidad del rol. | Flujo tolerante a duplicados. |
| 7 | [Parte 39 · Build, release y cadena de suministro](../classes/part-39-build-release-y-cadena-de-suministro/README.md) | desarrollada | [SE-471 · Dependencias directas, transitivas y vendorización](../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md)<br>[SE-474 · Versionado, compatibilidad y changelog](../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md)<br>[SE-475 · Feature flags y entrega progresiva](../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md)<br>[SE-476 · Canary, blue-green y rollback](../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) | Profundiza **build, release y cadena de suministro** desde la responsabilidad del rol. | Release firmado y verificable. |
| 8 | [Parte 43 · Mantenimiento y modernización legacy](../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md) | desarrollada | [SE-519 · Pruebas de caracterización y seams](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md)<br>[SE-521 · Strangler, branch by abstraction y anticorruption](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md)<br>[SE-523 · Migraciones de datos sin interrupción](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md)<br>[SE-524 · Compatibilidad, coexistencia y doble escritura](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md)<br>[SE-526 · Economía de reescribir frente a evolucionar](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md)<br>[SE-528 · Proyecto: migración incremental reversible](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md) | Profundiza **mantenimiento, modernización y retiro** desde la responsabilidad del rol. | Migración incremental reversible. |
| 9 | [Parte 44 · Gestión, liderazgo y práctica profesional](../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md) | desarrollada | [SE-534 · Gestión de riesgos y decisiones ejecutivas](../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md)<br>[SE-535 · Compras, proveedores y evaluación técnica](../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md)<br>[SE-537 · Economía del software y costo total](../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md)<br>[SE-539 · Taller: conducir una revisión de decisión difícil](../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md) | Profundiza **liderazgo, organización y decisiones** desde la responsabilidad del rol. | Propuesta defendida ante conflicto. |

### ✅ Clases ya desarrolladas que sostienen la ruta hoy

El núcleo anterior apunta a la capacidad profesional completa. Estas clases de apoyo,
de las Partes [00](../classes/part-00-ingenieria-de-software-como-profesion/README.md)–[50](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) (`SE-001`–`SE-612`), también tienen contenido desarrollado y
permiten practicar el rol desde otros ángulos:

| Clase desarrollada | Parte |
| --- | --- |
| [SE-108 · Proyecto: entorno de desarrollo autocontenido](../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md) | [Parte 08](../classes/part-08-entornos-herramientas-y-depuracion/README.md) |
| [SE-110 · SemVer, compatibilidad y contratos públicos](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md) | [Parte 09](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md) |
| [SE-142 · Decisiones reversibles e irreversibles](../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md) | [Parte 11](../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md) |
| [SE-164 · Compatibilidad, versionado y evolución de contratos](../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) | [Parte 13](../classes/part-13-especificaciones-contratos-y-modelos/README.md) |
| [SE-195 · Ramas, integración, rebase y conflictos](../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) | [Parte 16](../classes/part-16-git-colaboracion-y-codigo-abierto/README.md) |
| [SE-208 · ADRs, RFCs y registro de decisiones](../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) | [Parte 17](../classes/part-17-documentacion-y-conocimiento-tecnico/README.md) |
| [SE-517 · Mantenimiento correctivo, adaptativo y perfectivo](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md) | [Parte 43](../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md) |
| [SE-518 · Arqueología de código y recuperación de conocimiento](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md) | [Parte 43](../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md) |
| [SE-520 · Dependencias obsoletas y riesgo acumulado](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) | [Parte 43](../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md) |
| [SE-522 · Migraciones de runtime, lenguaje y framework](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md) | [Parte 43](../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md) |
| [SE-525 · Retiro, archivado y disposición de sistemas](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md) | [Parte 43](../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md) |
| [SE-527 · Taller: estabilizar antes de modernizar](../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md) | [Parte 43](../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md) |

**Cómo recorrerla.** Empieza por [SE-098](../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md) para fijar el
primer mecanismo, usa [SE-366](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md) para integrar el
centro de la especialidad y llega a [SE-539](../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md) cuando ya
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
| **Reescribir o evolucionar** | Comparar valor riesgo coexistencia y conocimiento perdido. | Caso económico más prueba de caracterización. |
| **Strangler o branch by abstraction** | Elegir frontera según tráfico datos y ciclo de despliegue. | Migración reversible. |
| **Compatibilidad o limpieza inmediata** | Pagar coexistencia temporal para reducir riesgo. | Telemetría de consumidores y criterio de retiro. |

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **Reescribir o evolucionar**, **Strangler o branch by abstraction**
y **Compatibilidad o limpieza inmediata** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: Nueva implementación produce totales distintos sin especificación confiable

**Síntoma.** El comportamiento real incluye reglas implícitas y datos históricos. La respuesta madura evita convertir la primera
correlación en causa y conserva evidencia antes de modificar el sistema.

![Diagrama de flujo con 6 pasos. Recorrido: «⚠️ Síntoma»; luego «🔎 Hipótesis»; luego «🧯 Contención»; luego «🧠 Diagnóstico»; luego «🛠️ Recuperación»; luego «📚 Prevención».](../site/assets/figures/mermaid-637bdc6ac9.svg)

**Cómo leer el diagrama:** empieza en «⚠️ Síntoma» y sigue las flechas hasta el final del recorrido. Las filas se leen como una serpentina: de izquierda a derecha y, en la fila siguiente, de derecha a izquierda.

1. **Detectar y delimitar:** identifica quién o qué está afectado, desde cuándo y qué
   cambió. Conserva timestamps, versiones, entradas y señales suficientes para no
   destruir la escena al intentar arreglarla.
2. **Investigar:** Comparar salidas fixtures trazas decisiones y excepciones de negocio. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** Detener migración preservar ambos caminos y convertir diferencia en requisito. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
| **Cobertura de comportamiento crítico** | Rutas legacy protegidas por caracterización. | Usar cobertura de líneas. |
| **Porcentaje de tráfico migrado** | Adopción real de la nueva ruta con calidad equivalente. | Mover tráfico sin datos. |
| **Tiempo de rollback** | Capacidad de volver ante divergencia. | Confiar en backup no ensayado. |

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: Migración incremental reversible

**Propósito:** comprender un sistema ajeno estabilizarlo y retirar una capacidad sin big bang. El resultado esperado es **mapa dependencias caracterización ADR strangler migración datos observabilidad rollout rollback y decommission**.

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

1. ¿En qué contexto elegirías **Reescribir o evolucionar** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **Nueva implementación produce totales distintos sin especificación confiable**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **Migración incremental reversible** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — **IEEE Computer Society**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — **ISO**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.
- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) — **Semantic Versioning project**. Se usa como referencia primaria u oficial; la guía no sustituye la fuente.

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.
<!-- role-depth:end -->

## 🧪 Evidencia de portafolio

- mapa de contexto, dependencias y conocimiento faltante;
- suite de caracterización que captura comportamientos relevantes;
- ADR comparando seis estrategias de modernización;
- migración dual-read/dual-write o equivalente con conciliación;
- rollout progresivo con criterios de abortar;
- plan de retiro con archivo, retención y borrado verificable.

## 📈 Progresión

Senior Engineer → Modernization Lead → Staff/Principal o Architect. También existe como
especialidad temporal en consultoría. El valor está en reducir riesgo y recuperar
capacidad de cambio, no en la cantidad de código reemplazado.

## ⚠️ Mitos frecuentes

- “Legacy es código malo.” Puede contener décadas de reglas no documentadas.
- “Una rewrite será más rápida.” Reinicia aprendizaje y suele subestimar paridad.
- “Mover a cloud moderniza.” Rehost cambia ubicación, no diseño ni operación.
- “Cuando el nuevo sistema arranca, el viejo se apaga.” Dependencias y datos pueden sobrevivir años.

## 🚀 Siguientes pasos

1. Toma un sistema pequeño ajeno y reconstruye su mapa de comportamiento.
2. Añade caracterización antes de refactorizar.
3. Extrae una capacidad detrás de un contrato compatible.
4. Ensaya reversión y documenta qué incertidumbre permanece.

---

[⬅️ Volver a las rutas](README.md) · [🏠 Inicio del programa](../README.md)
