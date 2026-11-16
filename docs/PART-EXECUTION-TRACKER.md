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
| 41 | Desarrollada y profundizada con experimentos reales y simulaciones sintéticas de harness y agentic engineering (ablación, comprobador de reglas, permisos, contexto, reglas de parada, control de daño, compuertas, fusiones de Git, trazas, gobierno y diagnóstico) ejecutados en Windows, CI verde (Validate, Pages y Security) | `1f594db2` |
| 00–44 | Alineación de la documentación con las 540 clases desarrolladas (README, ROADMAP, plan maestro, arquitectura, plan de publicación, mapas de roles, esquema y About), sin rastro de «480 desarrolladas»; sigue pendiente la revisión editorial humana independiente | `e58ea6a3` |
| 00–44 | Kit de gráficos (`grouped_bars`, `stacked_bars`, `line_chart`, `scatter`, `heatmap`, `dumbbell`, `percentile_intervals`, `timeline`), regla anti-duplicado, guía de rediseño y trinquete contra figuras `tab()` (tres figuras modelo en la Parte 22); CI verde (Validate, Pages y Security); el resto de las partes sigue pendiente de rediseño | `1855050c` |
| 00–44 | README raíz corregido en los generadores: tabla única de 45 partes sin comentarios dentro, estado de revisión dicho una vez, mapa de roles en tablas por familia con detalle colapsable; CI verde (Validate, Pages y Security) | `86291381` |
| 24 | Las 31 figuras que redibujaban una tabla (SE-289 a SE-300) pasan a gráficos con los mismos números medidos (barras agrupadas, líneas, mancuernas, intervalos, dispersión, mapa de calor, barras apiladas); alt y «Cómo leer la figura» reescritos; tope `tab()` de la parte a 0; CI verde (Validate, Pages y Security) | `49d7686d` |
| 22 | Rediseño de las 27 figuras que repetían una tabla (SE-266 a SE-276) como gráficos con los mismos números medidos (líneas, barras agrupadas y apiladas, mapas de calor, dispersión, dumbbell, línea de tiempo y diagrama de posiciones); `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `d4d080e5` |
| 25 | Rediseño de las 31 figuras que repetían una tabla (SE-301 a SE-312) como gráficos con los mismos números medidos (intervalos de percentiles, líneas, barras agrupadas y apiladas, mapa de calor y dispersión); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `ef4c950c` |
| 23 | Rediseño de las 34 figuras que repetían una tabla (SE-277 a SE-288) como gráficos con los mismos números medidos (barras agrupadas, líneas, mapas de calor, dumbbell, intervalos, línea de tiempo y diagrama por bloques); `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `33d2208d` |
| 26 | Rediseño de las 32 figuras que repetían una tabla (SE-313 a SE-324) como gráficos y diagramas con los mismos números medidos (barras apiladas y agrupadas, líneas, mapas de calor, mancuernas, dispersión y líneas de tiempo); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `8b0d5eaf` |
| 28 | Rediseño de las 32 figuras que repetían una tabla (SE-337 a SE-348) como gráficos y diagramas con los mismos números medidos (barras agrupadas y apiladas, líneas, mancuernas, intervalos de percentiles, dispersión, línea de tiempo y diagrama de órdenes); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `a84e0477` |
| 11 | Rediseño de las 23 figuras que repetían una tabla (SE-133 a SE-144) como gráficos con los mismos números (líneas, barras agrupadas y apiladas, mancuernas, intervalos, mapa de calor); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `c512b06d` |
| 15 | Rediseño de las 20 figuras que repetían una tabla (SE-181 a SE-192) como gráficos con los mismos números (líneas, barras, mapa de calor, intervalos y dispersión); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `9b7813cf` |
| 20 | Rediseño de las 16 figuras que repetían una tabla (SE-241 a SE-252) como gráficos con los mismos números (barras agrupadas y apiladas, líneas, mapa de calor y dispersión); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `68039829` |
| 35 | Rediseño de las 36 figuras que repetían una tabla (SE-421 a SE-432) como gráficos con los mismos números de los experimentos (barras, líneas, mapas de calor e intervalos); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `8ffcc798` |
| 40 | Rediseño de las 22 figuras que repetían una tabla (SE-481 a SE-492) como gráficos y diagramas de decisión con los mismos números (barras, líneas, mapas de calor y dispersión); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `867c36b0` |
| 29 | Rediseño de las 30 figuras que repetían una tabla (SE-349 a SE-360) como gráficos y diagramas con los mismos números medidos (barras apiladas y agrupadas, líneas, mapas de calor, mancuernas, dispersión, intervalos y un diagrama de normalización); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `2912aad5` |
| 27 | Rediseño de las 36 figuras que repetían una tabla (SE-325 a SE-336) como gráficos y diagramas con los mismos números medidos (líneas, barras agrupadas y apiladas, mapas de calor y diagramas de mecanismo); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `117600f1` |
| 30 | Rediseño de las 31 figuras que repetían una tabla (SE-361 a SE-372) como gráficos y diagramas con los mismos números medidos (intervalos de mediana, p90 y máximo, mapa de calor, barras agrupadas y apiladas, líneas con ejes logarítmicos, diagramas de mecanismo y de bytes); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `bb629460` |
| 31 | Rediseño de las 35 figuras que repetían una tabla (SE-373 a SE-384) como gráficos con los mismos números medidos (barras agrupadas y apiladas, líneas con ejes logarítmicos, dispersión, intervalos, dumbbells, mapas de calor y línea de tiempo); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `0eb3595c` |
| 07 | Rediseño de las 29 figuras que repetían una tabla (SE-085 a SE-096) como gráficos y tarjetas de casos con los mismos números medidos (barras agrupadas y apiladas, líneas en doble escala logarítmica, un mapa de calor, un dumbbell y tarjetas de casos para los resultados cualitativos (helper `figure_cases.py`)); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `8b5071b2` |
| 12 | Rediseño de las 24 figuras que repetían una tabla (SE-145 a SE-156) como gráficos y tarjetas de casos con los mismos números medidos (líneas, barras agrupadas y apiladas, mapas de calor, un dumbbell, una dispersión, intervalos de percentiles y tarjetas de casos); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) en `b5377e61`, que contiene el commit | `5efa3185` |
| 17 | Rediseño de las 23 figuras que repetían una tabla (SE-205 a SE-216) como gráficos y tarjetas de casos con los mismos números medidos (líneas, barras agrupadas y apiladas, mapas de calor y tarjetas de casos); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) en `b5377e61`, que contiene el commit | `ba653c0a` |
| 32 | Rediseño de las 30 figuras que repetían una tabla (SE-385 a SE-396) como gráficos y tarjetas de casos con los mismos números medidos (barras agrupadas, líneas, mapas de calor, dispersión, intervalos de percentiles y tarjetas de casos); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) en `b5377e61`, que contiene el commit | `32efe6a1` |
| 37 | Rediseño de las 36 figuras que repetían una tabla (SE-445 a SE-456) como gráficos y tarjetas de casos con los mismos números medidos (barras agrupadas y apiladas, líneas, dispersión, intervalos de percentiles y tarjetas de casos); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) en `b5377e61`, que contiene el commit | `e5e1fedb` |
| 42 | Rediseño de las 23 figuras que repetían una tabla (SE-505 a SE-516) como gráficos y tarjetas de casos con los mismos números medidos (líneas, barras agrupadas, mapas de calor, dispersión, intervalos de percentiles y tarjetas de casos); alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) en `b5377e61`, que contiene el commit | `53d71305` |
| 16 | Rediseño de 21 figuras (SE-193 a SE-204) como gráficos de barras, líneas, mapa de calor, diagramas de áreas de Git y de recuperación y diagramas de flujo con los mismos números medidos; alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `0367eb80` |
| 21 | Rediseño de 15 de las 16 figuras (SE-253 a SE-264) como gráficos de líneas, mapas de calor, dispersión, barras apiladas y diagramas de flujo; la comparación de siete comportamientos de texto entre Windows y Ubuntu queda como excepción justificada en `allowed_tables` con los mismos números medidos; alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `a3c43790` |
| 36 | Rediseño de 34 figuras (SE-433 a SE-444) como intervalos de percentiles, líneas, dispersiones, barras, mapas de calor, un dumbbell y diagramas de flujo con los mismos números medidos; alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `eb8bea96` |
| 41 | Rediseño de 13 figuras (SE-493 a SE-504) como barras apiladas y agrupadas, líneas, dispersión y diagramas de flujo y de grupos con los mismos números medidos; alt y «Cómo leer la figura» reescritos; `tab()` y alt «Tabla» de la parte en 0; CI verde (Validate, Pages y Security) | `826cca8a` |
