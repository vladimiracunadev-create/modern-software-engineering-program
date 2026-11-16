# Seguimiento de ejecución por partes

Registro recuperable del trabajo de profundización visual y pedagógica. Complementa
`ROADMAP.md`, `docs/MASTER-CURRICULUM-IMPLEMENTATION-PLAN.md` y
`docs/METHODOLOGY-GAP-AUDIT-2026-11-13.md`. El estado de una parte solo cambia cuando
su commit está en `main` con CI verde.

## Procedimiento por parte

1. Leer cada clase de `content/part-XX/` y su laboratorio si existe. Profundizar el contenido, no solo
   añadir figuras: mecanismos nuevos, ejemplos ejecutados y medidos, casos límite y fuentes primarias.
2. Añadir tres figuras por clase en `scripts/figures_partXX_<letra>.py` (módulos con un
   diccionario `FIGURES`) y regenerar con `python scripts/build_figures.py`.
3. Insertar cada figura junto al concepto que ilustra, con un párrafo «Cómo leer la
   figura» y «Dónde deja de valer», más fallo controlado, preguntas frecuentes, puente
   hacia agentes y fuentes primarias verificadas.
4. Reconstruir (`build_phase2.py`, `build_phase3.py`), validar, ejecutar pruebas y
   markdownlint, revisar las figuras en el navegador y hacer un commit por parte.
5. Push, esperar CI verde y marcar la parte aquí.

## Estado

| Parte | Estado | Commit |
|---|---|---|
| 00 | Profundizada con figuras, CI verde | `6e90ab8` |
| 01 | Profundizada en contenido y figuras, CI verde | `a809280` |
| 02 | Profundizada con evidencia medida en Windows y Linux, CI verde | `d8969ff` |
| 03 | Profundizada con mediciones de red reales | `ddd3b90` |
| 04 | Profundizada con cálculos y mediciones reales | `e5923c21` |
| 05 | Profundizada con mediciones y mutaciones del laboratorio en Windows y Linux | `28465a51` |
| 06 | Profundizada con experimentos de paradigmas ejecutados en Windows y Linux | `d855d80a` |
| 07 | Profundizada con experimentos de estructuras y algoritmos ejecutados en Windows y Linux | `9c857e4a` |
| 08 | Profundizada con experimentos de herramientas, entornos y Docker en Windows y Linux, CI verde | `342e7f20` |
| 09 | Profundizada con experimentos de paquetes, SDK y automatización ejecutados en Windows y Linux, CI verde | `0f56ff75` |
| 10 | Desarrollada y profundizada con experimentos sintéticos ejecutados en Windows y Linux; su ejecución de Validate fue cancelada por el push siguiente y el contenido quedó validado en verde por el commit `0f56ff75` | `08a052b4` |
| 11 | Desarrollada y profundizada con experimentos sintéticos de economía, métricas y decisiones ejecutados en Windows y Linux, CI verde | `d96a14a6` |
| 12 | Desarrollada y profundizada con experimentos sintéticos de requisitos ejecutados en Windows y Linux, CI verde | `ab725ae6` |
| 13 | Desarrollada y profundizada con experimentos sintéticos ejecutados en Windows y Linux CI verde | `758ca58b` |
| 14 | Desarrollada y profundizada con experimentos sintéticos de experiencia, accesibilidad e internacionalización ejecutados en Windows y Linux CI verde | `91f431fd` |
| 15 | Desarrollada y profundizada con simulaciones sintéticas de proceso, planificación y estimación ejecutadas en Windows y Linux, CI verde | `ad5b871e` |
| 16 | Desarrollada y profundizada con experimentos de Git real y simulaciones sintéticas de colaboración ejecutados en Windows y Linux, CI verde | `c2e96890` |
| 17 | Desarrollada y profundizada con experimentos sintéticos y de Git real de documentación y conocimiento técnico ejecutados en Windows y Linux, CI verde | `41921319` |
| 18 | Desarrollada y profundizada con experimentos sintéticos y procesos locales de CLI, servicios y automatización ejecutados en Windows y Linux, CI verde | `449e60d9` |
| 19 | Desarrollada y profundizada con experimentos sintéticos y modelos de web, accesibilidad, caché y seguridad ejecutados en Windows y Linux CI verde | `739f9443` |
| 20 | Desarrollada y profundizada con experimentos sintéticos y modelos de backend, APIs y procesamiento asíncrono ejecutados en Windows y Linux, CI verde | `1fb76b53` |
| 21 | Desarrollada y profundizada con experimentos sintéticos y modelos de software móvil, escritorio y multiplataforma ejecutados en Windows y Linux CI verde | `a0798f74` |
| 22 | Desarrollada y profundizada con simulaciones sintéticas de embebidos, IoT y tiempo real ejecutadas en Windows y Linux, CI verde | `4dafaa63` |
| 23 | Desarrollada y profundizada con simulaciones sintéticas de dominios especializados ejecutadas en Windows y Linux (CI verde) | `5103274d` |
| 24 | Desarrollada y profundizada con análisis de código y simulaciones sintéticas de diseño, patrones y refactorización ejecutados en Windows y Linux, CI verde | `4a8cd0b6` |
| 25 | Desarrollada y profundizada con simulaciones sintéticas y mediciones de arquitectura ejecutadas en Windows y Linux, CI verde | `30386e11` |
| 26 | Desarrollada y profundizada con experimentos sintéticos y modelos de datos, persistencia y recuperación ejecutados en Windows y Linux CI verde | `d50af249` |
| 27 | Desarrollada y profundizada con experimentos sintéticos y modelos de integración, eventos y mensajería ejecutados en Windows y Linux, CI verde (la corrección de Bandit y el CI verde corresponden al commit `35da5ee3`) | `68757419` |
| 28 | Desarrollada y profundizada con experimentos y modelos sintéticos de concurrencia y sistemas distribuidos ejecutados en Windows y Linux, CI verde | `166da6a5` |
| 29 | Desarrollada y profundizada con simulaciones sintéticas y mediciones de cloud, plataforma e infraestructura ejecutadas en Windows y Linux, CI verde | `1a2fcc75` |
| 30 | Desarrollada y profundizada con experimentos sintéticos y modelos de estrategia y técnicas de prueba ejecutados en Windows y Linux, CI verde | `d624d0c8` |
| 31 | Desarrollada y profundizada con experimentos sintéticos y sondas reales de calidad, rendimiento y resiliencia ejecutados en Windows y Linux, CI verde | `82974c6e` |
| 36 | Desarrollada y profundizada con experimentos sintéticos y ejecuciones reales de mantenimiento y modernización legacy en Windows y Linux, CI verde | `6212ab15` |
| 35 | Desarrollada y profundizada con experimentos sintéticos y mediciones de observabilidad, SRE e incidentes ejecutados en Windows y Linux , CI verde (Validate y Pages en verde sobre `141d5942`, que incluye el commit; Security verde en `23e1f16e`; el fallo de Security posterior es de la Parte 33) | `f1312f65` |
| 33 | Desarrollada y profundizada con experimentos sintéticos, firmas reales y escaneo de flujos de CI ejecutados en Windows y Linux, CI verde salvo Gitleaks ajeno de la Parte 34 | `db80b671` |
| 32 | Desarrollada y profundizada con experimentos sintéticos de seguridad, privacidad y cumplimiento ejecutados en Windows y Linux ; Validate y Pages verdes, Security rojo por hallazgos ajenos de las Partes 33 y 34 | `141d5942` |
| 34 | Desarrollada y profundizada con experimentos sintéticos y modelos de CI/CD, infraestructura como código y plataforma ejecutados en Windows y Linux, CI verde (la corrección de Gitleaks y el CI verde corresponden al commit `af1c70ac`) | `808ef333` |
| 37 | Desarrollada y profundizada con experimentos sintéticos y verificadores propios de liderazgo, equipos, riesgo, economía y práctica profesional ejecutados en Windows y Linux, CI verde (Validate, Pages y Security en verde sobre `41a1d015`) | `41a1d015` |
| 38 | Desarrollada y profundizada con experimentos sintéticos y ejecuciones reales de desarrollo de software asistido por IA en Windows y Linux, CI verde (Validate, Pages y Security) | `302a4011` |
| 39 | Desarrollada y profundizada con experimentos sintéticos y ejecuciones reales de especificación, agentes y ciclo de vida agentic en Windows y Linux , CI verde (Validate, Pages y Security) | `5fe0dc2e` |
| doc | Documentación, portal y About alineados con las Partes 00–39 (480 clases desarrolladas), CI verde (Validate, Pages y Security) | `9055cb1d` |
| infra | Infraestructura de publicación de las Partes 40–44 (ADR-005): estado derivado del contenido, contadores reales, guía `docs/ADDING-A-PART.md`, CI verde (Validate, Pages y Security) | `df561b8b` |
| 40 | Desarrollada y profundizada con experimentos reales y simulaciones sintéticas de metodologías de desarrollo (mutantes, escenarios, contratos, especificación, evaluaciones, Git real y política de equipo) ejecutados en Windows y Linux, CI verde (Validate, Pages y Security) | `263bbfc2` |
| 42 | Desarrollada y profundizada con experimentos reales y simulaciones sintéticas de patrones agénticos y sistemas con LLM (workflows, agentes, orquestación, memoria, recuperación sobre el corpus, servidor JSON-RPC real, diario SQLite con caídas, evaluación estadística, costo, latencia, seguridad y degradación) ejecutados en Windows, CI verde (Validate, Pages y Security en verde sobre `3e81efe5`) | `32013269` |
| 43 | Desarrollada y profundizada con experimentos reales y simulaciones de patrones de diseño, empresariales y de resiliencia (ast, sqlite3 en memoria, canales simulados y sockets locales) ejecutados en Windows, CI verde (Validate, Pages y Security) | `32a1d33a` |
| 44 | Desarrollada y profundizada con experimentos reales y simulaciones sintéticas de estilos arquitectónicos (decisión por escenarios, complementos, flujo de filtros, servicios por HTTP local, BFF y proxy, aislamiento en SQLite, data mesh, celdas, doce factores, migración en sombra, ADR con prueba de arquitectura) ejecutados en Windows, CI verde (Validate, Pages y Security) | `fca1bf75` |
| 41–44 | Planificadas (ADR-004); aún sin publicar. Procedimiento: `docs/ADDING-A-PART.md` | — |
