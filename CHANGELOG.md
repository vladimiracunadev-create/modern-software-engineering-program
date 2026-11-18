# Changelog

## 2026-11-17 — Documentación alineada con las 588 clases desarrolladas

- README, ROADMAP, plan maestro, arquitectura, matriz de cobertura, plan de publicación, guía de ampliación, mapa de roles, `curriculum/README.md`, `casos/GUIDE.md`, `DATA_LICENSES.md` y el About (`.github/repository-metadata.json` y GitHub) dicen ahora 588 clases desarrolladas en 49 partes (`SE-001`–`SE-588`); ADR-004 y ADR-006 se citan una sola vez como origen del alcance.
- el texto de la nota de partes sale de `scripts/build_phase2.py`, corregido en el generador; sigue pendiente la revisión editorial humana independiente.
- commit: ver `docs/PART-EXECUTION-TRACKER.md`.

## 2026-11-17 — Parte 46: Machine learning en producción y MLOps (SE-553 a SE-564)

- doce clases desarrolladas con mecanismos, causas, ejemplos y límites sobre el ciclo de vida y las fallas de un sistema de ML, datos, etiquetas y feature stores, entrenamiento reproducible, evaluación y sesgos, ajuste fino y costo, servicio con lotes y GPU, despliegue seguro (sombra, canary y rollback), monitoreo y reentrenamiento, seguridad y robustez, gobierno de IA y regulación, taller de degradación y recuperación y proyecto de sistema operable con evidencia;
- experimentos reproducibles en `scripts/experiments_part46_*.py` con numpy 2.4.4 y scikit-learn 1.8.0 (versiones fijadas en `scripts/requirements-part46.txt`), datos sintéticos de *Avisos-ML* con semilla 46, sin GPU, sin herramientas de terceros y sin modelos de lenguaje; 36 figuras en `scripts/figures_part46_a.py` y `_b.py`;
- fuentes verificadas con curl; el reglamento europeo se consultó en el Diario Oficial y el calendario en la página de la Comisión (paquete de simplificación incluido), y las normas ISO se citan por su fuente oficial sin reproducir su texto; el triaje de riesgo y el expediente de gobierno se declaran provisionales y no son asesoría jurídica;
- sin revisión humana independiente todavía; commit y CI en `docs/PART-EXECUTION-TRACKER.md`

## 2026-11-17 — Ampliación de clases existentes con temas ausentes (InnerSource, software verde, confianza cero, CRDT y Raft, RTOS, calidad de datos, regulación de IA y ajuste fino)

- diez clases ampliadas sin renumerar ni cambiar la estructura de las partes, cada una con una sección «Ampliación», un experimento reproducible (`scripts/experiments_partNN_ext.py`, semilla fija o medición real), una figura nueva sin repetir tablas y fuentes verificadas con curl: `SE-200` InnerSource (cola de revisión), `SE-268` RTOS y EDF frente a prioridades fijas, `SE-330` controles de calidad y linaje de datos, `SE-342` conjuntos CRDT, `SE-343` Raft y Paxos con un modelo reducido, `SE-353` confianza cero y movimiento lateral, `SE-356` software verde y SCI, `SE-386` confianza cero y credenciales robadas, `SE-466` Reglamento de IA e ISO/IEC 42001, `SE-513` ajuste fino y contaminación de la evaluación;
- las ampliaciones sobre datos y sobre IA apuntan a las Partes 45 y 46, todavía no publicadas; los experimentos son modelos sintéticos o mediciones de un solo equipo y cada clase lo declara en «Límites»; la norma ISO/IEC 42001 y las páginas de ISO no se pudieron verificar con curl (error 403) y se declara;
- sin cambio de contadores; commits `cc00faeb`, `68a33a7f`, `4b799dc3`, `bd960d70`, `37dcb4a8`, `f47c49b3`, `a790d695`, `3cb80365` y `05b87612`, con Validate, Pages y Security en verde sobre `05b87612`.

## 2026-11-17 — Parte 48: Runtimes y plataformas modernas (SE-577 a SE-588)

- doce clases desarrolladas con mecanismos, causas, ejemplos y límites sobre WebAssembly y WASI, WebAssembly en servidor y borde, eBPF, modelo de ejecución y costo de aceleradores, contenedores, microVM y sandboxes, hardware seguro y atestación, computación cuántica, criptografía poscuántica, confianza cero, un taller con batería hostil y un proyecto de plataforma de ejecución aislada con evidencia;
- experimentos reproducibles en `scripts/experiments_part48_*.py`: módulos de WebAssembly ejecutados con `wasmtime` 50.0.1, nueve programas eBPF cargados en el núcleo de Linux de WSL2, proxies de CPU con NumPy, ML-KEM-768 y ML-DSA-65 reales (bibliotecas de estudio), simulación cuántica con vectores de estado y una plataforma mínima con registro encadenado e informe firmado; 36 figuras sin tablas repetidas;
- lo que no se ejecutó se declara en cada clase: ninguna GPU (el controlador informó «GPU is lost»), ningún TEE ni TPM, ningún ordenador cuántico ni SDK, el modelo de componentes de WebAssembly, ningún contenedor ni microVM;

## 2026-11-17 — Parte 45: Ingeniería de datos y plataformas de datos (SE-541 a SE-552)

- 12 clases nuevas con las 16 secciones del contrato, README de la parte con guía razonada y resumen operativo, `part.json` con 39 fuentes verificadas y 36 figuras (`scripts/figures_part45_a.py` y `_b.py`) sin figuras que repitan una tabla;
- experimentos reproducibles en `scripts/experiments_part45_*.py` (semilla 45, solo biblioteca estándar: SQLite, `zlib`, `array`, `hmac`, `tempfile`): bytes y bloqueo en una base operacional, ingesta con marcas de agua y reentregas, estrella frente a Data Vault, cargas idempotentes y backfills, detectores de volumen, compatibilidad de esquemas, linaje por perturbación, formato columnar propio y manifiesto, privacidad y borrado propagado, costos y ruta crítica, pipeline con ocho defectos y plataforma gobernada con diez mutaciones;
- los tiempos de reloj varían entre equipos y los precios, volúmenes y defectos son parámetros del autor; no se ejecutó ninguna herramienta de terceros ni se evaluó ningún sistema real; sigue pendiente la revisión editorial humana independiente;
- commit `e8cbab8a` (Validate, Pages y Security en verde); detalle en `docs/PART-EXECUTION-TRACKER.md`.

## 2026-11-17 — Parte 47 desarrollada con experimentos reales y simulaciones de sistemas críticos y normas de seguridad (SE-565 a SE-576)

- las clases `SE-565`–`SE-576` pasan de planificadas a clases completas sobre el *Horno de curado*: peligro, riesgo y seguridad funcional (HARA, FMEA, FTA y STPA), IEC 61508, automoción (ISO 26262), aviación (DO-178C, DO-254 y ARP4754), dispositivos médicos (IEC 62304), casos de seguridad y trazabilidad, RTOS y planificación de tiempo real, codificación segura (MISRA y CERT), verificación formal (TLA+, SPARK y Alloy), verificación y cobertura (MC/DC, HIL y SIL), taller del Therac-25 y proyecto de paquete de aseguramiento;
- 36 figuras con experimentos ejecutados con la biblioteca estándar (CPython 3.12.9, semilla 47): árbol de fallos con causa común, FMEA, probabilidad de fallo bajo demanda, inyección de fallos, cobertura estructural, clases de seguridad, trazabilidad con resúmenes, planificación con inversión de prioridad, reglas de código, verificador de estados, MC/DC por mutantes, modelos del Therac-25 y paquete de aseguramiento;
- `content/part-47/part.json` aporta 23 fuentes nuevas verificadas (FAA, SAE, FDA, IEC, ESA, NASA, SEI, GSN, TLA+, SPARK, Alloy, Holzmann y el caso del Pathfinder); las normas de pago se describen sin reproducir su texto y lo no público se declara;
- no se ejecutó TLA+, SPARK, Alloy ni ningún RTOS y no se compiló C (no había compilador); no se afirma conformidad con ninguna norma ni revisión humana independiente;
- los contadores pasan a contar la Parte 47 como desarrollada (12 clases más); commit `eb99d1ae` (Validate, Pages y Security en verde); detalle en `docs/PART-EXECUTION-TRACKER.md`.

## 2026-11-17 — Infraestructura para las Partes 45–48 y tres roles nuevos (ADR-006)

- el alcance planificado pasa de 540 clases en 45 partes a 588 clases en 49 partes sin renumerar nada: Parte 45 Ingeniería de datos y plataformas de datos (`SE-541`–`SE-552`), 46 Machine learning en producción y MLOps (`SE-553`–`SE-564`), 47 Sistemas críticos, tiempo real y normas de seguridad (`SE-565`–`SE-576`) y 48 Runtimes y plataformas modernas (`SE-577`–`SE-588`); nacen planificadas, sin clases publicadas, y las 540 clases desarrolladas no cambian;
- el blueprint fija los 48 títulos exactos; `program_state.py`, los generadores, los validadores y las pruebas leen el estado real (540 desarrolladas, 48 planificadas) y dejan de asumir 45 partes y 540 clases, de modo que «Fin del programa» pasa a ser la última clase desarrollada;
- tres guías de rol nuevas con el mismo esquema, longitud, identidad visual y dos gráficos que las demás (MLOps / ML Platform Engineer, AI Governance & Responsible AI Engineer, Runtime & Systems Engineer) y filas de ampliación en 19 guías existentes (entre ellas Data Engineer, Safety-Critical, Embedded & IoT, Green Software, InnerSource, Security, AI Systems y Distributed Systems);
- ADR-006, plan maestro con las casillas `SE-541`–`SE-588`, ROADMAP, README, STATUS, portal, catálogo, About y `docs/ADDING-A-PART.md` con los rangos y títulos finales;
- commit `0a3f7a95`, con Validate, Pages y Security en verde; las Partes 45–48 siguen planificadas y el contenido de cada una se publica en su propio commit.

## 2026-11-17 — Casos de éxito: esquema del negocio y costos operativos (Amazon, Spotify, Airbnb y Stripe)

- esquema del negocio con figura en los cuatro casos; costos operativos con cifras del 10-K de Amazon y de Airbnb y del formulario 6-K de Spotify, con márgenes por segmento; Stripe, empresa privada, declara que costos y competidores no son públicos;
- competidores nombrados por el 10-K de Airbnb, plantilla y propiedades del 10-K de Amazon y el proveedor de nube de Airbnb; las cifras de la SEC se leyeron con WebFetch porque curl está bloqueado y la fuente lo declara;
- commits `18591f0f`, `bd6bd497`, `1d500a55` y `6fbc8502`; sin cambio de contadores 540/45

## 2026-11-17 — Casos de fallo: negocio, organización, costos, hardware, software, infraestructura y tolerancia a fallos

- Knight Capital, HealthCare.gov, TSB y Meta 2021 con secciones nuevas de sedes y organización, visión y misión, esquema de la operación, costos del incidente, competidores, hardware, software, infraestructura y mecanismos a prueba de fallos, cada una con figura propia (22 a 24 figuras por caso, 11 000 a 12 000 palabras);
- fuentes nuevas: Form 10-K de Knight de 2012 y Form 10-Q de Facebook; lo que las fuentes públicas no publican (hardware, lenguajes, centros de datos, plantilla, misión) queda marcado como no se sabe y no se inventa;
- commits `c6cfd632`, `99baa5da`, `6366c211` y `7d55893b`; sin cambio de contadores 540/45

## 2026-11-17 — Casos de éxito: hardware, software, infraestructura y tolerancia a fallos (Amazon, Spotify, Airbnb y Stripe)

- cada caso suma secciones y figuras propias de hardware, software, características de la infraestructura, tolerancia a fallos, visión y misión, y estructura y presencia mundial, con cada afirmación rotulada documentado, inferido o no se sabe; donde las fuentes no publican el dato (hardware de Airbnb, nube de Airbnb, plantilla por área) se declara;
- fuentes nuevas verificadas con curl: páginas institucionales y de principios de Amazon, página de contacto de Spotify y documentación de Stripe;
- commits `58eccfa6`, `262bacf0`, `33245217` y `6ee3018d`; sin cambio de contadores 540/45

## 2026-11-17 — Casos de éxito ampliados: Netflix, WhatsApp, Uber y Mercado Libre

- los cuatro casos pasan de unas 2 900 a 4 200 palabras a entre 11 000 y 16 200 (Netflix 16 200, WhatsApp 13 100, Uber 12 400, Mercado Libre 11 200) y de 4 a 6 figuras a entre 22 y 25, con arquitectura en niveles de zoom (contexto, contenedores, componentes, secuencias, datos, despliegue), esquema del negocio, costos operativos por rubro, plantilla, hardware, software, infraestructura, tolerancia a fallos, alternativas descartadas rotuladas como análisis propio, vínculos concepto → clase, preguntas y mini-ejercicios;
- hechos nuevos verificados contra los 10-K de Netflix (2007, 2016, 2025), Uber (2020, 2023, 2025), Meta (2025), Facebook (2014) y MercadoLibre (2019, 2021, 2024, 2025), la ficha de Open Connect, los repositorios de Netflix, el libro blanco y los blogs de WhatsApp, la nota de la Comisión Europea de 2017, los artículos de ingeniería de Uber y el caso de Go; donde no hay fuente pública (cuota de mercado, plantilla por área, hardware de servidores de WhatsApp, Uber y Mercado Libre) queda como «no se sabe» y los casos no alcanzan el 5x pedido;
- commits `58e46c7f`, `0c16a46e`, `3a04b135`, `88443568`, `13d44d05`, `c64aeb9c`, `1ddbcdfa`, `e05fbc04` y `683392d1`; sin cambio de contadores 540/45

## 2026-11-17 — Casos de fallo, segunda ampliación: CrowdStrike, Therac-25, GitLab 2017 y Quibi

- sedes y equipo, organización, visión y misión, esquema del negocio, costos, competidores, hardware, software, infraestructura y mecanismos a prueba de fallos, con 5 a 7 figuras nuevas por caso y rótulo documentado, inferido o no se sabe;
- datos nuevos del informe anual 10-K de CrowdStrike, del S-1 de GitLab, de Leveson y Turner y de la prensa sobre Quibi; los datos de hardware y software que no son públicos se declaran así;
- commits `e57975cf`, `3a5164c4`, `87b47deb` y `ccc64fa9`; sin cambio de contadores 540/45

## 2026-11-17 — Casos de éxito ×3: Amazon, Spotify, Airbnb y Stripe

- los cuatro casos ampliados al triple (de unas 3 600 a 4 000 palabras a entre 10 400 y 12 900, y de 4 a 6 figuras a entre 18 y 22), con arquitectura en varios niveles de zoom, viajes completos por tipo de usuario, economía con cifras citadas, alternativas y trade-offs rotulados como análisis propio, vínculos concepto → clase, preguntas de discusión y mini-ejercicios;
- hechos nuevos verificados contra Dynamo, la Biblioteca de Constructores de Amazon y el comunicado del cuarto trimestre de 2025; los blogs de ingeniería, Loud & Clear y el comunicado del cuarto trimestre de Spotify; los blogs de ingeniería, los artículos de búsqueda y las páginas de ayuda de Airbnb; y los blogs, la documentación y las cartas anuales de Stripe;
- commits `11ff8fd0`, `1bb41e42`, `24dc8955` y `df5afc9f`; sin cambio de contadores 540/45

## 2026-11-17 — Casos de fallo ×3: CrowdStrike, Therac-25, GitLab 2017 y Quibi

- los cuatro casos ampliados al triple (de unas 4 000 a 4 900 palabras a entre 12 500 y 16 300, y de 5 o 6 figuras a entre 17 y 19), con arquitectura en varios niveles de zoom, árbol de fallas, análisis causal, mejoras por factor, comparables, preguntas de discusión y mini-ejercicios;
- hechos nuevos verificados contra el análisis de causa raíz y el hub de CrowdStrike, los blogs de Microsoft, el artículo de Leveson y Turner, el postmortem de GitLab, los resúmenes de AWS y Atlassian, el post mortem de Cloudflare de 2019, el informe de Google Cloud de 2025 y la prensa sobre Quibi;
- commits `b90f735c`, `5fce6562`, `16b59c55` y `83578796`; sin cambio de contadores 540/45

## 2026-11-17 — Casos de fallo ×3: Knight Capital, HealthCare.gov, TSB y Meta 2021

- los cuatro casos de fallo ampliados al triple: de unas 3 300 a 3 700 palabras a entre 9 800 y 10 400, y de 5 o 6 figuras a entre 16 y 19, con arquitectura en ocho niveles de zoom, árbol de fallas, línea de tiempo con más resolución, mejoras por factor (control técnico, de proceso y de gobierno), vínculos concepto → clase, preguntas y mini-ejercicios, y la separación explícita entre documentado, inferido y no se sabe;
- hechos nuevos verificados contra la orden de la SEC y la Regulación SCI, GAO-14-694, GAO-15-238, GAO-13-601, la OIG de HHS, el Final Notice de la FCA, el comunicado de TSB de 2019, las publicaciones de Meta y Cloudflare y el informe de Google Cloud de 2019;
- commits `3a6bceff`, `4bd565bf`, `3cc31a97` y `ca76bfda`; sin cambio de contadores 540/45

## 2026-11-17 — Casos de estudio: Knight Capital, HealthCare.gov, TSB y Meta 2021

- cuatro casos de fallo escritos con el esquema de 14 secciones de `casos/GUIDE.md`, separando lo documentado, lo inferido y lo que no se sabe, con 5 o 6 figuras propias cada uno y fuentes oficiales comprobadas el 16 de noviembre de 2026.
- sin cambio de contadores 540/45 (commits `262724ac`, `55831842`, `fa29b660` y `8122dc35`)

## 2026-11-17 — Casos de éxito: Amazon, Spotify, Airbnb y Stripe

- cuatro casos terminados en `casos/exito/` con el esquema único, 23 figuras propias y fuentes públicas citadas; commits `20c1ad30` y `07a54c5b`, sin cambio de contadores

## 2026-11-17 — Casos de fallo: CrowdStrike, Therac-25, GitLab 2017 y Quibi

- cuatro casos de fallo completos en `casos/fallo/` con el esquema de 14 secciones, hechos separados de interpretación y mejoras rotuladas como análisis propio;
- 23 figuras propias (`scripts/figures_case_*.py`) sin tablas dibujadas; fuentes públicas verificadas el 16 de noviembre de 2026;
- commits `b0c9789c`, `6b42788a` y `bffb904b`; contadores 540 clases y 45 partes sin cambio.

## 2026-11-17 — Casos de éxito: Netflix, WhatsApp, Uber y Mercado Libre

- cuatro casos completos con fichas verificadas, hechos separados en documentado, inferido y no se sabe, fuentes públicas citadas y 22 figuras propias (`scripts/figures_case_<slug>.py`).
- cada caso enlaza las clases reales que enseñan sus conceptos; sin cambio de contadores 540/45 (commit `e565f7b4`, CI verde: Validate, Pages y Security).

## 2026-11-16 — Casos de estudio: estructura de la superficie

- nueva superficie propia «Casos de estudio» (no son clases ni roles; los contadores 540/45 no cambian): páginas `casos/exito/` y `casos/fallo/` con mapa visual e índice, 16 casos fijados en esqueleto, `casos/GUIDE.md` con el esquema único y las reglas editoriales.
- `scripts/build_cases.py` (portal `site/casos/`, sección del README entre las partes y los roles), contrato `scripts/figures_case_<slug>.py` descubierto por `build_figures.py`, `scripts/validate_cases.py`, `tests/test_cases.py` y trinquete de tablas con tope 0 para los casos (commit `29c2943d`, CI verde: Validate, Pages y Security).

## 2026-11-16 — Esquema único de README de parte y navegación doble en las 540 clases

- las Partes 18, 19 y 26-44 sustituyen los enlaces «Abrir la clase» sueltos dentro de la guía por la tabla «Resumen operativo del recorrido» (12 filas con enlace, núcleo profesional y aporte acumulativo); `scripts/part_summary_tables.py` reemplaza a `link_part_classes.py` y las 45 partes comparten el orden guía → resumen
- las 60 clases de las Partes 40-44 no tenían el pie de navegación y SE-480 no enlazaba la siguiente: `published_markdown` en `build_phase3.py` compone ahora el enlace anterior/siguiente arriba y abajo cuando falta o está desactualizado, y las 540 clases y páginas del portal lo llevan arriba y abajo (SE-001 sin anterior, SE-540 sin siguiente)
- `tests/test_part_readmes.py` exige el esquema en las 45 partes y la navegación doble en las 540 clases y 540 páginas (commit `cc77b3d2`, CI verde (Validate, Pages y Security) en `cc77b3d2`)

## 2026-11-16 — Parte 09: figuras como gráficos, no como tablas

- 29 figuras (SE-109 a SE-120) que dibujaban una tabla se rediseñan como gráficos y diagramas de mecanismo con los mismos números medidos.
- `alt` y «Cómo leer la figura» describen cada figura; `figure_tab_baseline.json` queda en 0 en `tables`, `embedded_tables` y `table_alts` (commit `d74d02f5`, CI verde: Validate, Pages y Security).

## 2026-11-16 — Parte 04: figuras como gráficos, no como tablas

- 32 figuras (SE-049 a SE-060) que dibujaban una tabla con `Fig.table()` se rediseñan con las primitivas del kit y diagramas (barras agrupadas y apiladas, líneas, un diagrama de estados del pedido y diagramas de flujo) y los mismos números medidos; la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada figura; `figure_tab_baseline.json` ya no tiene entrada de `embedded_tables` para la Parte 04 (commit `2e720e0f`, CI verde (Validate, Pages y Security))

## 2026-11-16 — Parte 06: figuras como gráficos, no como tablas

- 18 figuras (SE-073 a SE-084) que dibujaban una tabla con `Fig.table()` se rediseñan con barras agrupadas, diagramas de flujo y de mecanismo y los mismos números medidos; la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada figura; `figure_tab_baseline.json` ya no tiene entrada de `embedded_tables` para la Parte 06 (commit `6c8dd4c8`)

## 2026-11-16 — Parte 08: figuras como gráficos, no como tablas

- las 28 figuras `tab()` de SE-097 a SE-108 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas, líneas, mapas de calor, líneas de tiempo, diagramas de flujo, de grupos y anidados); la tabla Markdown se conserva y la figura muestra el patrón o el mecanismo
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 08 (commit `5ba2c369`, CI verde (Validate, Pages y Security) en `5ba2c369`)

## 2026-11-16 — Parte 13: figuras como gráficos, no como tablas

- las 15 figuras `tab()` de SE-157 a SE-168 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas, líneas, mapas de calor y diagramas de flujo); la tabla Markdown se conserva y la figura muestra el patrón o el mecanismo
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 13 (commit `2b1bdfa3`, CI verde (Validate, Pages y Security) en `a87b3e0d`, que contiene el commit)

## 2026-11-16 — Parte 18: figuras como gráficos, no como tablas

- las 22 figuras `tab()` de SE-217 a SE-228 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas y apiladas, líneas, mapas de calor, dumbbell y diagramas de flujo); la tabla Markdown se conserva y la figura muestra el patrón o el mecanismo
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 18 (commit `d7b1bf8d`, CI verde (Validate, Pages y Security) en `d7b1bf8d`)

## 2026-11-16 — Parte 33: figuras como gráficos, no como tablas

- las 30 figuras `tab()` de SE-397 a SE-408 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas, líneas, mapas de calor, intervalos de percentiles y diagramas de flujo); la tabla Markdown se conserva y la figura muestra el patrón o el mecanismo
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 33 (commit `a87b3e0d`, CI verde (Validate, Pages y Security) en `a87b3e0d`)

## 2026-11-16 — Parte 38: figuras como gráficos, no como tablas

- las 29 figuras `tab()` de SE-457 a SE-468 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas y apiladas, líneas, dispersiones, mapas de calor, intervalos y diagramas de flujo); la tabla Markdown se conserva y la figura muestra el patrón o el mecanismo
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 38 (commit `9b1cd867`, CI verde (Validate, Pages y Security) en `9b1cd867`)

## 2026-11-16 — Parte 43: figuras como gráficos, no como tablas

- las 21 figuras `tab()` de SE-517 a SE-528 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas y apiladas, líneas, dispersión, dumbbell y diagramas de flujo); la tabla Markdown se conserva y la figura muestra el patrón o el mecanismo
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 43 (commit `8f441a40`, CI verde (Validate, Pages y Security) en `8f441a40`)

## 2026-11-16 — Parte 44: figuras como gráficos, no como tablas

- las 29 figuras `tab()` de SE-529 a SE-540 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas y apiladas, líneas, mapas de calor); la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 44 (commit `068385e1`, CI verde (Validate, Pages y Security) en `068385e1`, que contiene el commit)

## 2026-11-16 — Parte 39: figuras como gráficos, no como tablas

- las 37 figuras `tab()` de SE-469 a SE-480 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas y apiladas, líneas, mapas de calor); la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 39 (commit `9ef3f731`, CI verde (Validate, Pages y Security) en `068385e1`, que contiene el commit)

## 2026-11-16 — Parte 34: figuras como gráficos, no como tablas

- las 32 figuras `tab()` de SE-409 a SE-420 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas y apiladas, líneas, mapas de calor); la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 34 (commit `b0b01d96`, CI verde (Validate, Pages y Security) en `068385e1`, que contiene el commit)

## 2026-11-16 — Parte 19: figuras como gráficos, no como tablas

- las 21 figuras `tab()` de SE-229 a SE-240 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas y apiladas, líneas, mapas de calor, intervalos de percentiles); la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 19 (commit `26440ceb`, CI verde (Validate, Pages y Security) en `068385e1`, que contiene el commit)

## 2026-11-16 — Parte 14: figuras como gráficos, no como tablas

- las 17 figuras `tab()` de SE-169 a SE-180 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas y apiladas, líneas, mapas de calor, intervalos de percentiles); la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 14 (commit `b5377e61`, CI verde (Validate, Pages y Security) en `068385e1`, que contiene el commit)

## 2026-11-16 — Parte 10: figuras como gráficos, no como tablas

- las 22 figuras `tab()` de SE-121 a SE-132 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas y apiladas, líneas, mapas de calor, intervalos de percentiles); la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 10 (commit `364a225a`, CI verde (Validate, Pages y Security) en `068385e1`, que contiene el commit)

## 2026-11-16 — Parte 16: figuras como gráficos, no como tablas

- 21 figuras (SE-193 a SE-204) que repetían la tabla Markdown se rediseñan con las primitivas del kit (gráficos de barras, líneas, mapa de calor, diagramas de áreas de Git y de recuperación y diagramas de flujo) y los mismos números medidos; la tabla se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 16 (commit `0367eb80`)

## 2026-11-16 — Parte 21: figuras como gráficos, no como tablas

- 15 de las 16 figuras (SE-253 a SE-264) que repetían la tabla Markdown se rediseñan con las primitivas del kit (gráficos de líneas, mapas de calor, dispersión, barras apiladas y diagramas de flujo; la comparación de siete comportamientos de texto entre Windows y Ubuntu queda como excepción justificada en `allowed_tables`) y los mismos números medidos; la tabla se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 21 (commit `a3c43790`)

## 2026-11-16 — Parte 36: figuras como gráficos, no como tablas

- 34 figuras (SE-433 a SE-444) que repetían la tabla Markdown se rediseñan con las primitivas del kit (intervalos de percentiles, líneas, dispersiones, barras, mapas de calor, un dumbbell y diagramas de flujo) y los mismos números medidos; la tabla se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 36 (commit `eb8bea96`)

## 2026-11-16 — Parte 41: figuras como gráficos, no como tablas

- 13 figuras (SE-493 a SE-504) que repetían la tabla Markdown se rediseñan con las primitivas del kit (barras apiladas y agrupadas, líneas, dispersión y diagramas de flujo y de grupos) y los mismos números medidos; la tabla se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 41 (commit `826cca8a`)

## 2026-11-16 — Parte 42: figuras como gráficos, no como tablas

- las 23 figuras `tab()` de SE-505 a SE-516 se rediseñan con las primitivas del kit y los mismos números medidos (líneas, barras agrupadas, mapas de calor, dispersión, intervalos de percentiles y tarjetas de casos); la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 42 (commit `53d71305`, CI verde (Validate, Pages y Security) en `b5377e61`, que contiene el commit)

## 2026-11-16 — Parte 37: figuras como gráficos, no como tablas

- las 36 figuras `tab()` de SE-445 a SE-456 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas y apiladas, líneas, dispersión, intervalos de percentiles y tarjetas de casos); la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 37 (commit `e5e1fedb`, CI verde (Validate, Pages y Security) en `b5377e61`, que contiene el commit)

## 2026-11-16 — Parte 32: figuras como gráficos, no como tablas

- las 30 figuras `tab()` de SE-385 a SE-396 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas, líneas, mapas de calor, dispersión, intervalos de percentiles y tarjetas de casos); la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 32 (commit `32efe6a1`, CI verde (Validate, Pages y Security) en `b5377e61`, que contiene el commit)

## 2026-11-16 — Parte 17: figuras como gráficos, no como tablas

- las 23 figuras `tab()` de SE-205 a SE-216 se rediseñan con las primitivas del kit y los mismos números medidos (líneas, barras agrupadas y apiladas, mapas de calor y tarjetas de casos); la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 17 (commit `ba653c0a`, CI verde (Validate, Pages y Security) en `b5377e61`, que contiene el commit)

## 2026-11-16 — Parte 12: figuras como gráficos, no como tablas

- las 24 figuras `tab()` de SE-145 a SE-156 se rediseñan con las primitivas del kit y los mismos números medidos (líneas, barras agrupadas y apiladas, mapas de calor, un dumbbell, una dispersión, intervalos de percentiles y tarjetas de casos); la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 12 (commit `5efa3185`, CI verde (Validate, Pages y Security) en `b5377e61`, que contiene el commit)

## 2026-11-16 — Parte 07: figuras como gráficos, no como tablas

- las 29 figuras `tab()` de SE-085 a SE-096 se rediseñan con las primitivas del kit y los mismos números medidos (barras agrupadas y apiladas, líneas en doble escala logarítmica, un mapa de calor, un dumbbell y tarjetas de casos para los resultados cualitativos (helper `figure_cases.py`)); la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 07 (commit `8b5071b2`, CI verde (Validate, Pages y Security))

## 2026-11-16 — Parte 11: figuras como gráficos, no como tablas

- las figuras `tab()` de la Parte 11 se rediseñan con las primitivas del kit y los mismos números; la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 11 (commit `c512b06d`)

## 2026-11-16 — Parte 15: figuras como gráficos, no como tablas

- las figuras `tab()` de la Parte 15 se rediseñan con las primitivas del kit y los mismos números; la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 15 (commit `9b7813cf`)

## 2026-11-16 — Parte 20: figuras como gráficos, no como tablas

- las figuras `tab()` de la Parte 20 se rediseñan con las primitivas del kit y los mismos números; la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 20 (commit `68039829`)

## 2026-11-16 — Parte 35: figuras como gráficos, no como tablas

- las figuras `tab()` de la Parte 35 se rediseñan con las primitivas del kit y los mismos números; la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 35 (commit `8ffcc798`)

## 2026-11-16 — Partes 02 y 03: figuras que dibujaban tablas, rediseñadas

- las 24 figuras de la Parte 02 y las 26 de la Parte 03 que dibujaban una tabla con `Fig.table()` pasan a diagramas de mecanismo o gráficos con los mismos datos; la tabla Markdown se conserva
- `embedded_tables` queda en 0 para las Partes 02 y 03 en `figure_tab_baseline.json`; ayudantes nuevos en `scripts/figure_flows.py` (commits `2d0ea288`, `4a0bfb73` y `21a1cc80`)

## 2026-11-16 — Parte 40: figuras como gráficos, no como tablas

- las figuras `tab()` de la Parte 40 se rediseñan con las primitivas del kit y los mismos números; la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 40 (commit `867c36b0`)

## 2026-11-16 — Parte 31: figuras como gráficos, no como tablas

- las 35 figuras `tab()` de SE-373 a SE-384 se rediseñan con las primitivas del kit y los mismos números medidos: barras agrupadas y apiladas, líneas (con eje logarítmico donde el rango lo exige), una dispersión, intervalos, dumbbells, mapas de calor y una línea de tiempo
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 31 (commit `0eb3595c`, CI verde)

## 2026-11-16 — Parte 30: figuras como gráficos, no como tablas

- las 31 figuras `tab()` de SE-361 a SE-372 se rediseñan con las primitivas del kit y los mismos números medidos: intervalos de mediana, percentil 90 y máximo, un mapa de calor, barras agrupadas y apiladas, líneas (con eje logarítmico donde el rango lo exige) y diagramas de mecanismo (dependencias de una función, bytes de «é» por sistema, casos de frontera de la nota, reasignación tras un incidente); la tabla Markdown se conserva
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 30 (commit `bb629460`, CI verde). En SE-368 la figura decía «73 a 101 de 1 000» y ahora coincide con la tabla de la clase (87 a 101)

## 2026-11-16 — Parte 28: figuras como gráficos, no como tablas

- las 32 figuras `tab()` de SE-337 a SE-348 se rediseñan con las primitivas del kit y los mismos números medidos: barras agrupadas y apiladas, líneas (algunas en escala logarítmica), mancuernas, intervalos de percentiles, una dispersión, una línea de tiempo y un diagrama de órdenes; la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 28 (commit `a84e0477`, CI verde)

## 2026-11-16 — Parte 27: figuras como gráficos, no como tablas

- las 36 figuras `tab()` de SE-325 a SE-336 se rediseñan con las primitivas del kit y los mismos números medidos: líneas, barras agrupadas y apiladas, mapas de calor y diagramas de mecanismo (estructuras de mensajería, relevo del outbox, capa anticorrupción); la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 27 (commit `117600f1`, CI verde)

## 2026-11-16 — Parte 29: figuras como gráficos, no como tablas

- las 30 figuras `tab()` de SE-349 a SE-360 se rediseñan con las primitivas del kit y los mismos números medidos: barras apiladas y agrupadas (algunas en escala logarítmica), líneas, mapas de calor, una mancuerna, dispersiones, intervalos de mediana y percentil 90 y un diagrama de normalización; la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 29 (commit `2912aad5`, CI verde)

## 2026-11-16 — Parte 26: figuras como gráficos, no como tablas

- las 32 figuras `tab()` de SE-313 a SE-324 se rediseñan con las primitivas del kit y los mismos números medidos: barras apiladas y agrupadas, líneas, mapas de calor, un dumbbell, una dispersión y líneas de tiempo; la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 26 (commit `8b0d5eaf`, CI verde)

## 2026-11-16 — Parte 23: figuras rediseñadas como gráficos

- las 34 figuras de `SE-277` a `SE-288` que redibujaban la tabla Markdown pasan a gráficos con los mismos números medidos: barras agrupadas, líneas (algunas en escala logarítmica), mapas de calor, un dumbbell, intervalos de mínimo y máximo, una línea de tiempo del año con cambio de hora y un diagrama por bloques para las seis comprobaciones de dinero
- cada clase reescribe el texto alternativo y el bloque «Cómo leer la figura. Dónde deja de valer» para describir el gráfico; las figuras `tab()` y los `alt` que empiezan por «Tabla» de la Parte 23 bajan de 34 a 0 en `scripts/figure_tab_baseline.json`
- commit `33d2208d`, CI verde (Validate, Pages y Security)

## 2026-11-16 — Parte 25: figuras como gráficos, no como tablas

- las 31 figuras `tab()` de SE-301 a SE-312 se rediseñan con las primitivas del kit y los mismos números medidos; la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 25 (commit `ef4c950c`)

## 2026-11-16 — Parte 24: figuras como gráficos, no como tablas

- las 31 figuras `tab()` de SE-289 a SE-300 se rediseñan con las primitivas del kit y los mismos números medidos; la tabla Markdown se conserva y la figura muestra el patrón
- `alt` y «Cómo leer la figura» describen cada gráfico; `figure_tab_baseline.json` ya no tiene entrada para la Parte 24 (commit `49d7686d`)

## 2026-11-16 — Parte 22: figuras rediseñadas como gráficos

- las 27 figuras de `SE-266` a `SE-276` que redibujaban la tabla Markdown pasan a gráficos con los mismos números medidos: líneas en escala logarítmica, barras agrupadas y apiladas, mapas de calor, dispersión, dumbbell, una línea de tiempo (lectura partida de 16 bits) y un diagrama de posiciones de la interrupción
- cada clase reescribe el texto alternativo y el bloque «Cómo leer la figura. Dónde deja de valer» para describir el gráfico; las figuras `tab()` y los `alt` que empiezan por «Tabla» de la Parte 22 bajan de 27 a 0 en `scripts/figure_tab_baseline.json`
- commit `d4d080e5`, CI verde (Validate, Pages y Security)

## 2026-11-16 — Kit de gráficos y trinquete contra figuras que repiten una tabla

- `scripts/figure_kit.py` incorpora primitivas de gráfico deterministas y sin dependencias: `grouped_bars` (vertical u horizontal, escala logarítmica), `stacked_bars`, `line_chart`, `scatter`, `heatmap`, `dumbbell`, `percentile_intervals` y `timeline`, con ejes, unidades, leyenda y rótulos de valor; fallan con `ValueError` si una etiqueta no cabe; el catálogo con datos ilustrativos está en `scripts/figure_kit_gallery.py`
- `docs/PEDAGOGICAL-STANDARD.md` fija la regla anti-duplicado y la primitiva recomendada por tipo de dato; `docs/FIGURE-REDESIGN-GUIDE.md` da el procedimiento para que cada parte sustituya sus figuras `tab()`
- tres figuras de la Parte 22 sirven de modelo con los mismos números medidos: latencia de un botón (`SE-265`, barras en escala logarítmica), acumulador de 16 bits (`SE-265`, mapa de calor) y eficiencia de un bus (`SE-266`, líneas); sus textos alternativos y su «Cómo leer la figura» hablan del gráfico
- `tests/test_figure_redesign.py` y `scripts/figure_tab_baseline.json` impiden que suba el número de figuras `tab()`, de imágenes con `alt` que empieza por «Tabla» o de diagramas hechos con `Fig.table()`, y exigen bajar el tope al reducirlo; meta: 0 salvo excepciones justificadas en `allowed_tables`
- el resto de las partes no se toca: 988 figuras `tab()` siguen pendientes de rediseño (una sesión por parte)

## 2026-11-16 — Documentación alineada con las 540 clases desarrolladas (Partes 00–44)

- README, ROADMAP, plan maestro, arquitectura, plan de publicación, matriz de cobertura, mapa de competencias, guías de roles, licencias y workflows dejan de afirmar «480 desarrolladas», «Partes 00–39» o «Partes 40–44 planificadas»; las cifras se verificaron contra `curriculum.yaml`, `catalog.json` y los archivos de `content/`
- `schemas/curriculum.schema.json` acepta de 1 a 45 partes y hasta 540 clases en lugar de exigir exactamente 40 y 480; el contrato del roadmap exige «540 clases (ADR-004)»
- el About de GitHub y `.github/repository-metadata.json` dicen «540 clases en 45 partes (540 desarrolladas, SE-001–SE-540)»; los documentos históricos (ADR-002/003, auditorías, antecedentes de 480 clases) se conservan como registro de lo que fue cierto entonces
- las Partes 40–44 cumplen `tests/test_part_readmes.py`: cada README enlaza sus 12 clases
- la revisión editorial humana independiente sigue pendiente

## 2026-11-16 — Parte 43 desarrollada con experimentos reales y simulaciones de patrones de diseño, empresariales y de resiliencia (SE-517 a SE-528)

- las clases `SE-517`–`SE-528` pasan de planificadas a clases completas sobre el servicio *Avisos*: criterios para usar un catálogo, patrones GoF creacionales, estructurales y conductuales, GRASP, Repository, Unit of Work y Active Record, patrones de integración, timeout, reintentos con jitter y circuit breaker, bulkhead, sidecar, ambassador y degradación, antipatrones y deuda de diseño, un taller de refactor y un catálogo de patrones
- 36 figuras con experimentos ejecutados con la biblioteca estándar en Windows (CPython 3.12) y sin invocar ningún modelo de lenguaje: costo de Strategy frente a `if/elif` medido con `ast`, 24 ordenaciones de pruebas con un Singleton, dos órdenes de una pila de decoradores, 10.000 secuencias contra banderas y máquina de estados, un cambio de regla en dos diseños, consultas contadas en una base `sqlite3` en memoria, un canal con 208 duplicados y receptor idempotente, cuatro políticas de reintento con 1000 clientes y un circuit breaker, compartimentos y degradación simulados, un salto medido con sockets locales, métricas de cohesión y ciclos, un maestro dorado con seis mutantes y dos detectores de patrones sobre un corpus etiquetado
- `content/part-43/part.json` aporta las fuentes de la parte (catorce fuentes nuevas con enlaces verificados); los contadores pasan a una parte desarrollada más y doce clases más

## 2026-11-16 — Parte 44 desarrollada con experimentos reales y simulaciones de estilos arquitectónicos (SE-529 a SE-540)

- las clases `SE-529`–`SE-540` pasan de planificadas a clases completas sobre el servicio *Avisos*: decisión por fuerzas de calidad, microkernel, pipes and filters, microservicios, BFF con gateway y malla, multi-tenancy, data mesh, arquitectura celular, 12-factor, migración entre estilos, taller de escenarios y proyecto de ADR defendido
- 36 figuras con experimentos ejecutados con la biblioteca estándar en Windows (CPython 3.12.9): matriz de seis estilos con sensibilidad, núcleo de complementos, memoria de una cadena de filtros sobre 100 000 registros, llamadas por HTTP local y cadenas de servicios simuladas, un proxy TCP, doce consultas sobre SQLite con una barrera de vistas, una cola de equipo de datos validada con Erlang C, celdas y fragmentación aleatoria, un linter de 12-factor, un modo sombra sobre 20 000 peticiones, un modelo de tres candidatos y una prueba de arquitectura sobre el árbol sintáctico; no se invocó ningún modelo ni se ejecutó ninguna herramienta de terceros
- `content/part-44/part.json` aporta 29 fuentes nuevas verificadas (SEI, AWS, Microsoft, Fowler, Dehghani, 12factor, Istio, Kubernetes, ADR, ArchUnit, SQLite y RFC)
- los contadores pasan a contar la Parte 44 como desarrollada (12 clases más); la revisión editorial humana independiente sigue pendiente

## 2026-11-16 — Parte 42 desarrollada con experimentos reales y simulaciones de patrones agénticos y sistemas con LLM (SE-505 a SE-516)

- las clases `SE-505`–`SE-516` pasan de planificadas a clases completas sobre el asistente de *Avisos*: workflows frente a agentes, encadenado, enrutamiento y paralelización, orquestador-trabajadores y evaluador-optimizador, ReAct, plan-and-execute y reflexión, memoria, embeddings y recuperación, MCP y A2A, ejecución durable e idempotencia, evals y LLMOps, costo, latencia y seguridad, taller de selección y degradación, y proyecto con puerta de entrada
- 36 figuras con experimentos ejecutados con la biblioteca estándar: modelo sintético con semilla fija y tasas declaradas, y código real para las herramientas, el enrutador, el verificador, los hilos, la recuperación sobre 835 fragmentos de las Partes 39 y 40, un servidor JSON-RPC por un proceso hijo, un diario SQLite con caídas inyectadas y un motor de política de capacidades; no se invocó ningún modelo de lenguaje ni se ejecutó ningún producto de terceros
- `content/part-42/part.json` aporta 23 fuentes nuevas verificadas (Anthropic, MCP, A2A, JSON-RPC, Temporal, IETF, OWASP, OpenTelemetry y artículos de referencia)
- los contadores pasan de 41 a 42 partes desarrolladas y de 492 a 504 clases; las Partes 41, 43 y 44 siguen planificadas y la revisión editorial humana independiente sigue pendiente

## 2026-11-16 — Parte 41 desarrollada con experimentos reales y simulaciones de harness y agentic engineering (SE-493 a SE-504)

- las clases `SE-493`–`SE-504` pasan de planificadas a clases completas sobre el arnés del equipo de *Avisos*: anatomía de un harness, instrucciones con cumplimiento determinista, herramientas y permisos, contexto y relevo, bucles y reglas de parada, sandboxes y control de daño, verificación y menú único, multiagente, observabilidad y evaluación del harness, gobierno frente a vibe coding, taller de diagnóstico y proyecto de harness gobernado
- 36 figuras con experimentos ejecutados con la biblioteca estándar y Git en Windows (CPython 3.12.9, Git 2.55): ablación de un harness mínimo sobre seis tareas, un comprobador de seis reglas sobre diecisiete casos, treinta comandos con dos políticas de permisos, un modelo de contexto de 120 turnos, cinco reglas de parada sobre 4 000 tareas simuladas, cinco acciones destructivas con cuatro configuraciones de recuperación, cinco compuertas sobre doce cambios, cuatro fusiones reales de Git, comparaciones con ruido de dos harness, un modelo de gobierno de 20 000 cambios, seis fallos inyectados con dos diagnosticadores y un harness gobernado con seis controles y cuatro escenarios adversos
- el «modelo» de los laboratorios es una política guionizada: no se invocó ningún modelo de lenguaje ni se ejecutó ningún producto de agentes; las cifras no son tasas reales y el informe de límites está en el README de la parte
- `content/part-41/part.json` aporta las fuentes de la parte (22 fuentes nuevas verificadas y `NIST-AI-RMF` de la línea base)

## 2026-11-16 — Parte 40 desarrollada con experimentos reales y simulaciones de metodologías de desarrollo (SE-481 a SE-492)

- las clases `SE-481`–`SE-492` pasan de planificadas a clases completas sobre el núcleo de *Avisos*: mapa de metodologías, TDD (ciclo y escuelas), BDD, ATDD y Specification by Example, DDD, diseño y pruebas de contrato, SDD, EDD, ODD, taller de cinco metodologías y política de equipo
- 36 figuras con experimentos ejecutados con la biblioteca estándar en Windows (CPython 3.12.9) y Ubuntu/WSL2 (3.12.3): 20 mutantes y cinco oráculos, un ciclo rojo-verde de ocho pasos, dos estilos de prueba ante refactores, nueve escenarios ejecutados, cuatro conjuntos de ejemplos, un recuento de «entrega» en 4 249 frases del corpus, doce cambios de proveedor con tres detectores, diez derivas de especificación, una simulación de puerta de evaluación, dos historiales de Git reales y una simulación de cinco políticas; no se invocó ningún modelo ni se ejecutó ninguna herramienta de terceros
- `content/part-40/part.json` aporta las fuentes de la parte (primer uso del mecanismo de ADR-005); `validate_repository.py` valida las fuentes extra; se corrige la descripción de ODD en `role_profiles.py` (Organic Driven Development, no observabilidad)
- los contadores pasan de 40 a 41 partes desarrolladas y de 480 a 492 clases; 48 clases (Partes 41–44) siguen planificadas

## 2026-11-16 — Infraestructura para publicar las Partes 40–44 (SE-481–SE-540) sin tocar scripts

- nuevo `scripts/program_state.py`: una parte está desarrollada si y solo si existen `content/part-NN/README.md` y los doce `SE-NNN.md`; de ahí salen contadores, rangos y textos de estado
- `scripts/build_program_blueprint.py` define las 45 partes y los 540 títulos; `curriculum.yaml` lista solo las partes desarrolladas y declara el alcance en `planned_scope` (45 partes, 540 clases, 2.430 horas, partes sin publicar con `status: planned`); `catalog.json` añade `planned_parts`, `planned_classes` y `unpublished_parts`
- `build_phase2/3/4.py`, `build_role_guides.py`, los validadores, las pruebas y `pages.yml` dejan de usar 40, 480 o 521 como constantes; el README regenera su bloque de estado entre marcadores `<!-- state:… -->`; las filas de las Partes 40–44 pasan de «planificada» a enlace al tener contenido
- metadatos de fuentes propios de cada parte en `content/part-NN/part.json`; `tests/test_figures.py` incluye automáticamente toda parte desarrollada
- plan maestro y ROADMAP incorporan las Partes 40–44 (60 casillas sin marcar); nuevos `docs/adr/ADR-005-publish-parts-40-44-from-content.md` y `docs/ADDING-A-PART.md`
- el estado real no cambia: 480 clases desarrolladas (Partes 00–39) y 60 planificadas (Partes 40–44), sin presentar como existente lo que no lo es

## 2026-11-16 — Documentación alineada con las Partes 00–39 (480 clases desarrolladas)

- las 480 clases del catálogo (`SE-001`–`SE-480`, Partes 00–39) tienen texto íntegro en `content/` y figuras; se verificó contando archivos: 480 documentos en `content/part-*/SE-*.md`, 480 README de clase, 480 `lesson.json`, 480 páginas `site/classes`, 40 páginas `site/parts`, 360 actividades y 360 rúbricas (fases 3–4) y 42 guías de rol; las Partes 40–44 (`SE-481`–`SE-540`) siguen solo planificadas, sin clases ni carpetas, y los contadores generados de 480 clases y 40 partes no cambian;
- `DEVELOPED_LAST_CLASS` pasa de 324 a 480 y las páginas del portal de `SE-325`–`SE-480` dejan de decir «Contenido en revisión»; los textos generados de `STATUS.md`, `classes/README.md`, las páginas de parte 06–39 y la portada del portal dejan de hablar de borradores y estructura; las guías de rol y `scripts/role_profiles.py` marcan las Partes 00–39 como desarrolladas;
- se actualizan el README raíz, `ROADMAP.md`, `docs/PROGRAM-ARCHITECTURE.md`, `docs/COVERAGE-MATRIX.md`, `docs/PEDAGOGICAL-STANDARD.md`, las auditorías de fase 3 y 4, de cobertura y de brechas metodológicas, el plan maestro, `roles/README.md`, `llms.txt` y `.github/repository-metadata.json` («540 clases planificadas en 45 partes (480 desarrolladas, SE-001–SE-480)»);
- las pruebas que usaban `SE-325` como ejemplo de borrador ahora exigen que esa página diga «Contenido desarrollado» y no «Contenido en revisión», y la prueba de clases de apoyo de las guías acepta hasta `SE-480`; no se debilita ninguna comprobación;
- la afirmación de estado sigue siendo la misma: desarrolladas, pero sin revisión editorial humana independiente.

## 2026-11-16 — Parte 39 desarrollada y profundizada con experimentos sintéticos y ejecuciones reales de especificación, agentes y ciclo de vida agentic

- las clases `SE-469`–`SE-480` pasan de estructura sin contenido a clases completas sobre el servicio de recordatorios de entrega de la plataforma educativa (*Avisos*) construido desde una especificación: de la intención a la especificación durable, constitución, clarificación, plan y tareas, implementación y convergencia contra la especificación, proyecto nuevo, cambio sobre código existente, corrección de errores y evaluación de ideas, agentes, herramientas, permisos y límites de autoridad, habilidades, extensiones, ganchos y entornos aislados, MCP, recursos, plantillas de petición y confianza, delegación y subagentes, aprobación humana y acciones reversibles, seguridad agentic, inyección de instrucciones y auditoría, un taller de parada, recuperación y evaluación de un agente y un proyecto final de producto operable validado por el sistema; el portal publica el contenido íntegro de las doce clases y el índice de la parte incluye «Evidencia medida y límites»;
- 37 figuras con experimentos de semilla fija y ejecuciones reales de código en dos sistemas, sin invocar ningún modelo de lenguaje: cuatro detectores de vaguedad sobre 125 frases, las interpretaciones posibles de una especificación con ocho decisiones abiertas y la trazabilidad entre requisitos y pruebas con doce defectos inyectados; un analizador de tres artefactos, cinco preguntas de clarificación para catorce ambigüedades y el plan de cuarenta tareas con ruta crítica; el bucle de implementar y converger con cuatro tasas de regresión, el verificador parcial y diez variantes defectuosas; cinco estrategias de lectura de un repositorio de 300 módulos, cuatro políticas de verificación de un arreglo y el valor de evaluar una idea;
  cuatro políticas de permisos sobre treinta órdenes, el radio de daño de cuatro configuraciones y la acumulación de reglas «permitir siempre»; un gancho ejecutado como proceso, cuarenta habilidades con cien peticiones y veintidós intentos de escape de rutas; cien mensajes con tres niveles de validación, un catálogo de veinte herramientas con huellas y una caché con cinco tiempos de vida; el contexto con subagentes, la retención de hechos, las colisiones de edición y tres protocolos de escritura sobre SQLite; cuatro políticas de aprobación, sesenta acciones deshechas con un diario y un flujo de cinco pasos con compensaciones; cuatro filtros de instrucciones inyectadas, las tres capacidades de doce tareas y cinco manipulaciones de un registro de auditoría; cuatro reglas de parada, la reanudación tras 500 caídas y la comparación de dos agentes con cinco tamaños de conjunto; y un servicio de diez requisitos con seis defectos inyectados, la restauración de copias y la matriz de evidencia;
- tres o más figuras por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref (Spec Kit, la especificación MCP 2026-07-28, la documentación de Claude Code, OWASP, NIST, Saltzer y Schroeder, Garcia-Molina y Salem, Wilson) y un puente hacia el trabajo con agentes;
- las simulaciones y los recuentos se ejecutaron con CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu bajo WSL2 con cifras idénticas; la lectura de reloj del arranque de un proceso de `SE-474` cambia de equipo en equipo; los parámetros son supuestos del autor, no se invocó ningún modelo ni agente real, no se ejecutó ninguna herramienta de Spec Kit ni se contactó con ningún servidor MCP, el manejador de mensajes de `SE-475` es una imitación y no una implementación conforme, no se midió la tasa de éxito de ninguna inyección ni se desarrolló ninguna técnica efectiva contra un sistema, y los filtros, el motor de permisos, el analizador, las variantes defectuosas y las reglas de parada se evaluaron con casos escritos sabiendo qué buscan;
- hallazgos del análisis: el revisor por lista de palabras tiene una precisión del 80,0 % y un recobrado del 66,7 % sobre 125 frases; 200 implementaciones de una especificación con ocho decisiones abiertas dan 184 comportamientos distintos y ninguno coincide con la intención; con cinco preguntas, elegir por orden del documento deja sin resolver el 64,3 % del costo esperado y por costo esperado el 29,3 %; con una regresión del 5 % por pasada el 62,4 % de los bucles no converge en diez pasadas; con un verificador que cubre el 80 % de los criterios el 93,7 % de las corridas declara convergencia con criterios abiertos; tres casos del camino feliz detectan 3 de 10 variantes y diecisiete criterios las 10;
  buscar por nombre en un repositorio de 300 módulos lee 11,8 KB y encuentra 4 de los 5 usos, y la batería existente acepta el código sin corregir en los cinco errores; una lista de permisos por prefijo deja pasar 13 de 16 órdenes peligrosas y el análisis de segmentos con confinamiento de rutas ninguna; con todas las herramientas y alcance completo el 41,6 % de las sesiones tiene algún daño y con herramientas mínimas, escritura confinada y aprobación el 0,0 %; un gancho que se cae o se cuelga deja pasar 6 de 18 acciones peligrosas si solo el código 2 bloquea; una comparación de prefijo de texto deja pasar 3 de 12 escapes de rutas y rechaza 7 de 10 rutas legítimas; con la autorización por cabecera y la ejecución por cuerpo, 5 de 5 mensajes no permitidos atraviesan los dos primeros niveles de validación; un buscador de patrones halla 3 de 4 descripciones con instrucciones y marca 3 legítimas, y una huella alerta en las 6 actualizaciones;
  con un tiempo de vida de un día, el 79,0 % de las respuestas de una caché de listados es vieja; delegar en subagentes procesa el 22 % de los tokens de entrada con lectura mínima y el 89 % con lectura redundante de seis veces, y una retención del 95 % por hecho deja llegar los cinco hechos en el 77,4 % de los casos; con cuatro agentes y reparto al azar el 94,4 % de las repeticiones tiene un conflicto de edición; la escritura ciega pierde 600 de 800 contribuciones; preguntar por cada acción deja ejecutar 3,02 acciones irreversibles por sesión frente a 0,54 con una pausa solo para lo irreversible; un flujo con un paso irreversible deja un efecto residual en el 12,1 % de las ejecuciones; un filtro de frase fija detecta 8 de 40 órdenes escondidas y el patrón amplio las 40 con 19 falsas alarmas en 160 documentos inocuos; el 73,5 % de las configuraciones aleatorias de seis herramientas reúne las tres capacidades; una cadena de huellas sin referencia externa no detecta cortes ni reescrituras;
  reiniciar sin punto de control duplica 20,9 avisos de 30 y un punto de control en otra transacción duplica en el 31 % de las caídas; distinguir dos agentes que difieren en seis puntos exige del orden de mil tareas (89,5 % de detección con 1 000 y 4,3 % con 20); la autodeclaración de un agente con tres pruebas del camino feliz no detecta ninguno de seis defectos inyectados, las pruebas por requisito los seis; con una copia diaria el 87 % de las caídas reenvía avisos y con una copia por hora ninguna; cuatro de diez requisitos están en verde sin una variante que demuestre que su prueba puede fallar;
- las clases posteriores a `SE-360` se publican con el mecanismo que `build_phase2.py` y `build_phase4.py` incorporaron con la Parte 30 (texto íntegro desde `content/part-XX/SE-NNN.md`, sin `activity.yaml` ni `rubric.json`); aquí solo se añade el rango `SE-469`–`SE-480` a las clases editoriales, a las pruebas de figuras y al plan maestro; `DEVELOPED_LAST_CLASS` y los textos globales no cambian en esta entrada, y la parte no tiene laboratorio en `labs/`; el contenido sigue pendiente de revisión humana independiente.

## 2026-11-16 — Parte 38 desarrollada y profundizada con experimentos sintéticos y ejecuciones reales de desarrollo de software asistido por IA

- las clases `SE-457`–`SE-468` pasan de estructura sin contenido a clases completas sobre el equipo de la plataforma educativa que incorpora un asistente al trabajo sobre el módulo de calificaciones: capacidades y límites de los modelos generativos, prompting y criterios de salida, contexto, memoria y recuperación, autocompletado, chat, edición y generación, prototipado y exploración de alternativas, generación de pruebas, documentación y migraciones, revisión, refactorización y explicación asistidas, context engineering y reducción de ambigüedad, evals de exactitud, utilidad, costo y latencia, privacidad, propiedad intelectual y código inseguro, un taller que compara flujos manual, asistido y automatizado y un proyecto de cambio real con trazabilidad y revisión humana; el portal publica el contenido íntegro de las doce clases y el índice de la parte incluye «Evidencia medida y límites»;
- 36 figuras calculadas desde los mismos módulos de experimentos (`scripts/experiments_part38_a.py` y `scripts/experiments_part38_b.py`), con semilla fija o ejecuciones reales de código de la biblioteca estándar: muestreo de cinco respuestas candidatas, calibración de 1 000 preguntas y conjuntos que caben en cuatro ventanas de contexto; requisitos escritos frente a no escritos, validación por capas de 200 salidas y conflicto entre instrucciones; recuperación BM25 sobre 240 documentos, memoria con cuatro caducidades y presupuesto de contexto; tres políticas de aceptación, una edición dirigida frente a un archivo regenerado medida con `difflib` y 467 pulsaciones según el retardo; la mejor de N alternativas, un andamiaje medido con `ast` y la brecha a producción;
  ocho mutantes frente a dos estilos de prueba, `doctest` sobre 30 funciones y una migración de 2 000 notas en SQLite; el umbral de un revisor, cuatro versiones refactorizadas frente a la original y treinta explicaciones; 729 interpretaciones de una petición, versiones mezcladas en la recuperación y contradicciones en archivos de instrucciones; intervalos de Wilson, seis configuraciones por costo por solución aceptada y los sesgos de un juez; un escáner de tres reglas sobre 240 mensajes, texto frente a árbol sintáctico sobre 17 fragmentos y huellas frente a un corpus con licencia; tres flujos sobre 200 tareas, el punto de equilibrio y la potencia de dos diseños; una bitácora encadenada atacada de cinco maneras, cuatro compuertas y la reversión limpia;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes;
- los experimentos se ejecutaron con CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu bajo WSL2 con salidas idénticas cifra por cifra (comprobadas por suma de verificación de la salida completa) y no dependen de la semilla de hash; ninguna medición usa el reloj, los parámetros son supuestos del autor, no se llamó a ningún modelo de lenguaje, no se evaluó ningún asistente, agente, revisor, escáner ni juez de terceros, no se midió a ninguna persona ni equipo, las cadenas que simulan secretos se generan al azar al ejecutar y los casos de prueba se escribieron sabiendo qué buscan; lo dicho sobre protección de datos, propiedad intelectual o la Ley de IA no es asesoría legal;
- hallazgos del análisis: a temperatura 0,2 el voto de mayoría de cinco acierta el 2,2 % cuando la respuesta correcta es la segunda más probable y al menos una de cinco la incluye el 80,2 % a temperatura 1,0; la confianza declarada de 88,6 % convive con un acierto de 77,9 % y casi no distingue las preguntas fáciles de las difíciles (87,3 % frente a 56,8 % de acierto); con los seis requisitos escritos se cumplen todos el 73,4 % de las veces y con ninguno el 1,6 %; tres capas de validación atrapan 167 de 200 salidas defectuosas; 20 reglas «siempre/nunca» sobre 25 temas se contradicen el 97,4 % de las veces;
  con fragmentos de 900 palabras se envían dieciocho veces más palabras que con 150 para el mismo acierto con clave única; una memoria sin caducidad responde obsoleto el 54,4 % de las veces; aceptar sin leer deja entrar 229 defectos por cada 1 000 sugerencias y leer y ejecutar 44; el mismo arreglo cambia 2 líneas editado y 124 regenerado; la ganadora de 20 alternativas con ruido 1 se mide en 2,63 y vale 1,29; el 90 % de las 40 funciones de un andamiaje no se usa; una suite que copia la salida actual detecta 4 de 8 mutantes y una derivada de la especificación 8; la conversión directa de 2 000 notas convierte en silencio 99 valores inválidos;
  una diferencia presente en el 1,04 % de las entradas se detecta con el 5,1 % de probabilidad con cinco entradas y el 65,0 % con cien; «calcula la nota final» admite 729 interpretaciones y cada restricción las divide por tres; 20 tareas ordenan bien un 70 % frente a un 75 % solo el 58,3 % de las veces; el costo por solución aceptada de las configuraciones varía de 0,55 a 0,77 mientras el costo por intento varía por un factor de 55; un juez con 83,5 % de acuerdo cambia el veredicto en el 25,5 % de los casos al intercambiar el orden; una cadena hexadecimal de 32 caracteres no supera el umbral de entropía; el flujo asistido deja de ahorrar tiempo con un 50 % de aciertos y el diseño pareado detecta una diferencia del 15 % con 20 tareas en el 83 % de los casos frente al 12 %; recalcular la cola de una bitácora encadenada no se detecta sin un ancla externa; cuatro compuertas dejan pasar 240 defectos de 10 000 frente a 2 029 sin ellas; con cinco ediciones posteriores la reversión limpia baja al 53,4 %;
- las clases posteriores a `SE-360` se publican con el mecanismo que `build_phase2.py` y `build_phase4.py` incorporaron con la Parte 30 (texto íntegro desde `content/part-XX/SE-NNN.md`, sin `activity.yaml` ni `rubric.json`); aquí solo se añade el rango `SE-457`–`SE-468` a las clases editoriales y a las pruebas de figuras; `DEVELOPED_LAST_CLASS` y los textos globales no cambian en esta entrada, y la parte no tiene laboratorio en `labs/`; el contenido sigue pendiente de revisión humana independiente.
## 2026-11-16 — Parte 37 desarrollada y profundizada con experimentos sintéticos de liderazgo, equipos, riesgo, economía y práctica profesional

- las clases `SE-445`–`SE-456` pasan de estructura sin contenido a clases completas sobre el equipo de plataforma educativa: liderazgo técnico sin autoridad formal, equipos y ownership, comunicación y conflicto, mentoría y retroalimentación, estimación y compromisos, riesgos y decisiones ejecutivas, compras y proveedores, propiedad intelectual, contratos y ética, economía del software, portafolio y defensa, un taller de revisión de una decisión difícil y un proyecto de dossier defendible;
- 36 figuras con experimentos de semilla fija: siembra y umbrales de adopción, cuello de botella de aprobaciones, factor de camión, fronteras de equipo, carga de guardia, anclaje y pérdida de campos de una decisión, reciprocidad con ruido, tareas que estiran, retraso del aviso, ruido de evaluación, suma de medianas, pronóstico por flujo, ciclo y carga, matrices de riesgo, valor de la información, sensibilidad de pesos, costo a cinco años, disponibilidad compuesta, clasificación de licencias, firmas de origen, costo de demora y valor presente, entrevistas, portafolio, defensa por profundidad, resultado frente a proceso, cobertura de paneles, calibración y verificación de dossier;
- tres secciones nuevas por clase, preguntas, errores, ejercicios y fallos controlados propios, fuentes verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes;
- los experimentos (`scripts/experiments_part37_a.py` y `_b.py`) se ejecutaron en Windows (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3) con salidas idénticas; los parámetros son supuestos del autor, no se estudió ningún equipo, contrato ni persona reales, el analizador de licencias y los verificadores son versiones simplificadas, nada de la parte es asesoría legal y el contenido sigue pendiente de revisión humana independiente.

## 2026-11-16 — Parte 34 desarrollada y profundizada con experimentos sintéticos de CI/CD, infraestructura como código y plataforma

- las clases `SE-409`–`SE-420` pasan de estructura sin contenido a clases completas sobre la canalización de la API de entregas: integración continua, pipelines y cachés, compuertas, credenciales efímeras y OIDC, entrega y despliegue, infraestructura como código, GitOps, entornos de vista previa y datos seguros, plataformas internas, métricas DORA, un taller de endurecimiento y un proyecto de camino a producción con retroceso; el portal publica el contenido íntegro y el índice de la parte, sin cambiar los conteos de 480 clases ni de 40 partes;
- 36 figuras con experimentos de semilla fija en tiempo virtual: choque de ramas y lotes, ruta crítica, matrices y cachés, orden de etapas, reglas sobre workflows y reintentos, verificación de tokens, ventana de exposición y detectores de secretos, estrategias de despliegue y potencia del canario, estado concurrente, deriva, disputa de controladores y poda, reidentificación y costo de entornos, adopción y catálogo, definiciones DORA y ruido, endurecimiento, inyección ejecutada de verdad y retroceso con SQLite real;
- tres secciones nuevas por clase, preguntas, errores, ejercicios y fallos controlados propios, fuentes verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3) con cifras publicadas idénticas; los parámetros son supuestos del autor, no se midió ningún sistema ni herramienta reales, los verificadores se afinaron con los mismos casos que los evalúan y el contenido sigue pendiente de revisión humana independiente; `DEVELOPED_LAST_CLASS` y los textos globales no cambian.

## 2026-11-16 — Parte 32 desarrollada y profundizada con experimentos sintéticos de seguridad, privacidad y cumplimiento

- las clases `SE-385`–`SE-396` pasan de estructura sin contenido a clases completas sobre la plataforma de entregas vista desde quien la ataca y quien la protege: modelos de amenaza, identidad y sesiones, autorización y mínimo privilegio, inyección y codificación, criptografía y claves, secretos y ambientes, privacidad por diseño, secure SDLC y abuso, vulnerabilidades y divulgación, cumplimiento y evidencia, un taller de controles aparentes y un proyecto de paquete de seguridad verificable; el portal publica el contenido íntegro de las doce clases y el índice de la parte, sin cambiar los conteos de 480 clases ni de 40 partes;
- 36 figuras con experimentos de semilla fija ejecutados en Windows (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3) con cifras idénticas, salvo las lecturas de reloj y las sondas de portabilidad, que difieren por diseño; los parámetros son supuestos del autor, no se atacó ningún sistema real ni se usó dato personal real, el cifrado de `SE-389` es didáctico, la clase no da asesoría legal y los validadores, escáneres y mutantes se afinaron con los mismos casos que los evalúan;
- hallazgos del análisis: corregir la inyección SQL no mueve el camino más barato de un grafo de ataque (7 antes y después); con una función de hash rápida cae el 70 % de las cuentas en una hora y con 600 000 iteraciones de PBKDF2 y sal el 0,9 %; un límite por dirección y un bloqueo por cuenta no reducen un relleno de credenciales; una suite de ruta feliz detecta 0 de 13 defectos de autorización y la matriz completa 13; el 88,2 % de 5 000 estudiantes sintéticos es único con cuatro atributos exactos; un registro encadenado no ve el truncamiento sin una huella publicada fuera; un validador de paquetes ve 195 de 210 mutaciones y ninguna de la evidencia que parece correcta;
- el contenido sigue pendiente de revisión humana independiente; `DEVELOPED_LAST_CLASS` y los textos globales no cambian en esta entrada.
## 2026-11-16 — Parte 33 desarrollada y profundizada con experimentos sintéticos, firmas reales y escaneo de flujos de CI

- las clases `SE-397`–`SE-408` pasan de estructura sin contenido a clases completas sobre el canal de release de la API de entregas: build reproducible y hermético, artefactos y promoción, dependencias y vendorización, SBOM y procedencia, firmas y verificación, versionado y changelog, banderas, canary y rollback, instaladores y actualizaciones, riesgos de CI, un taller de verificación de procedencia y un proyecto de release firmado y recuperable; el portal publica el contenido íntegro de las doce clases y el índice de la parte, sin cambiar los conteos de 480 clases ni de 40 partes;
- 36 figuras con experimentos de semilla fija y sondas reales: ocho fuentes de variación de un build y un campo de zip que cambia el hash entre Windows y Ubuntu, reconstruir frente a promover, la clausura real de 349 y 63 distribuciones, un validador de SBOM frente a 240 mutaciones, seis estrategias frente a nueve ataques con firmas Ed25519 de `openssl`, un comparador de firmas con `ast`, segmentación por huella, canario con falsas alarmas, inyección de fallos en cuatro estrategias de actualización, un escáner frente a 155 mutaciones de los flujos reales y un canal con verificación cruzada entre sistemas;
- hallazgos: el mismo árbol normalizado da `bb3ff54418db0198` en Windows y `2d20872cfbd34c32` en Ubuntu hasta fijar `create_system`; con una deriva del 5 % el 4,7 % de los lanzamientos llega distinto a producción; sin bloqueo 60 días de builds resuelven 37 conjuntos de versiones; un validador de SBOM ve 120 de 240 mutaciones; 0 de 6 casos coherentes son rechazados por un verificador que rechaza 12 de 12 manipulaciones; sobrescribir en sitio deja 6 de 7 interrupciones corruptas y un directorio nuevo con puntero, ninguna; los tres flujos de este repositorio tienen sus 20 acciones fijadas y 0 hallazgos con siete reglas;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios, fuentes verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes; el código está en `scripts/experiments_part33/`;
- los parámetros son supuestos del autor, no se usó ninguna herramienta real de firma, SBOM, CI ni despliegue, las lecturas de reloj y de entorno cambian entre ejecuciones y sistemas, `DEVELOPED_LAST_CLASS` y los textos globales no cambian, y el contenido sigue pendiente de revisión humana independiente.

## 2026-11-16 — Parte 35 desarrollada y profundizada con experimentos sintéticos y mediciones de observabilidad, SRE e incidentes

- las clases `SE-421`–`SE-432` pasan de estructura sin contenido a clases completas sobre la API de entregas operada en producción: señales y observabilidad, registros estructurados y correlación, métricas y cardinalidad, trazas y contexto, SLI/SLO/SLA y presupuestos, alertas y fatiga, runbooks y guardia, gestión de incidentes, postmortems sin culpa, continuidad y recuperación, un taller de diagnóstico con telemetría incompleta y un proyecto de paquete operativo; el portal publica el contenido íntegro y el índice de la parte, sin cambiar los conteos de 480 clases ni de 40 partes;
- 36 figuras con experimentos de semilla fija en tiempo virtual (atribución en una cadena de cuatro servicios, falla de un cliente pequeño, series y cubetas, fragmentación de trazas, presupuesto por peticiones o minutos, seis reglas de alerta, carga de guardia, kappa de severidad, recurrencia de incidentes, pérdida de datos, resolución de dependencias, diagnóstico con señales ausentes y cadena de respuesta) y mediciones reales de copias de SQLite y sondas de plataforma en Windows (CPython 3.12.9) y Ubuntu/WSL2 (3.12.3);
- las cifras de tiempo virtual son idénticas en ambos sistemas; las sondas de plataforma y los tiempos de reloj difieren por diseño; los parámetros son supuestos del autor, no se operó ningún sistema real, y los verificadores se afinaron con los mismos casos que los evalúan;
- las clases se publican con el mecanismo `has_editorial_class`; solo se añade el rango `SE-421`–`SE-432` a las clases editoriales y a las pruebas de figuras; `DEVELOPED_LAST_CLASS` y los textos globales no cambian; el contenido sigue pendiente de revisión humana independiente.

## 2026-11-15 — Parte 36 desarrollada y profundizada con experimentos sintéticos y ejecuciones reales de mantenimiento y modernización legacy

- las clases `SE-433`–`SE-444` pasan de estructura sin contenido a clases completas sobre el módulo legado de calificaciones de la plataforma educativa: mantenimiento correctivo, adaptativo y perfectivo, arqueología de código y recuperación de conocimiento, pruebas de caracterización y seams, dependencias obsoletas y riesgo acumulado, strangler, branch by abstraction y anticorruption, migraciones de runtime, lenguaje y framework, migraciones de datos sin interrupción, compatibilidad, coexistencia y doble escritura, retiro, archivado y disposición de sistemas, economía de reescribir frente a evolucionar, un taller de estabilización previa y un proyecto de migración incremental reversible; el portal publica el contenido íntegro de las doce clases y el índice de la parte incluye «Evidencia medida y límites»;
- 36 figuras con experimentos de semilla fija y ejecuciones reales de código en dos sistemas: 24 meses de capacidad con y sin reserva preventiva, la clasificación de 600 solicitudes y la probabilidad de llegar a una fecha impuesta; puntos calientes en 4 000 commits, archivos huérfanos con una rotación del 2 % mensual y dos técnicas de detección de código muerto; cobertura de líneas frente a doce mutantes, ocho procesos con semilla de hash distinta y el costo de una costura; cuatro cadencias de actualización, la exposición a 31 avisos y el radio de impacto en 200 grafos; tres estrategias de corte, el tamaño de muestra de la sombra y 5 000 registros traducidos por una capa anticorrupción;
  cuatro comportamientos del intérprete que cambian sin excepción, tres métodos de reescritura sobre 400 fragmentos y tres políticas de versiones; cinco tamaños de lote, cuatro estrategias de relleno sobre SQLite y el costo de los cambios de esquema; tres formas de escribir en dos almacenes, el costo de detectar la divergencia y una matriz de compatibilidad ejecutable; seis ventanas de observación, una retención por reglas y tres formatos de archivo con una suma de verificación; tres opciones económicas en 20 000 escenarios con su sensibilidad y su horizonte; el ruido de las pruebas inestables, dos construcciones del mismo código y la incertidumbre de una línea base; y una migración de seis fases con el costo de volver atrás y el reposo antes de contraer;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes;
- las simulaciones y los recuentos se ejecutaron con CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu bajo WSL2 con cifras idénticas; los tiempos de reloj de `SE-435` y `SE-439` son lecturas de un equipo que cambian en cada ejecución y las huellas de construcción de `SE-443` difieren entre sistemas por diseño; los parámetros son supuestos del autor, no se migró ni analizó ningún sistema, repositorio, base de datos, equipo ni persona reales, no se usó ninguna herramienta de migración, de mutación ni de reescritura de terceros, y los clasificadores, verificadores y técnicas se evaluaron con casos escritos sabiendo qué buscan; los plazos de retención no son asesoría legal;
- hallazgos del análisis: sin una reserva del 20 % la carga correctiva pasa de 19,7 a 59,7 unidades al mes y con ella baja a 14,0; empezar una adaptación con un margen igual a su mediana llega a tiempo en el 44,0 % de los casos; ordenar por tamaño captura el 23,5 % de las correcciones y por frecuencia por tamaño el 55,6 %; con una rotación del 2 % mensual quedan huérfanos 194 de 300 archivos a los cinco años; el análisis por nombre propone 45 funciones muertas y 25 están vivas;
  los cinco ejemplos de la documentación cubren el 89 % de las líneas y detectan 4 de 12 mutantes, mil entradas aleatorias los 12; ocho procesos producen ocho salidas distintas por el orden de un conjunto; actualizar una sola vez a las 48 versiones cuesta 71,4 horas frente a 12,6 en cada versión; un lote anual deja un aviso expuesto 224 días de mediana frente a 22; actualizar un concentrador arrastra 12 paquetes de mediana; un corte único afecta 20 000 peticiones frente a 1 000 del escalonado al 5 %; una ventana de sombra de doce semanas incluye un cierre en el 43 % de los casos; una traducción ingenua se cae con el 88,0 % de 5 000 registros;
  `round` cambia el 5,0 % de las notas con dos decimales frente a la regla antigua y ordenar por punto de código difiere en el 91,4 % de las posiciones; la sustitución de texto reescribe 252 fragmentos de más y el árbol sintáctico ninguno; un lote único hace esperar una escritura 3 969 ms en el percentil 99 y uno de 2 000 filas 44 ms; un relleno ingenuo deja 389 de 20 000 filas obsoletas con los recuentos iguales y activar la doble escritura no lo corrige; sin una bandeja de salida con secuencia quedan 292 claves distintas con un 1 % de fallos; un lector estricto falla en 11 de 12 celdas y uno tolerante en 4, algunas «pasando» con la nota ausente; una ventana de 30 días rompería al 14 % de los consumidores reales; un corte único de retención borra 5 479 registros de más y conserva 7 368; el CSV pierde los ceros de 10 080 códigos;
  en los escenarios simulados evolucionar es la opción más barata en 16 269 de 20 000 y el costo de construir domina la decisión; con cinco pruebas inestables y dos reintentos el 90,3 % de los commits con un defecto intermitente salen verdes; con 20 cambios una tasa del 15 % queda entre el 0 % y el 30 %; volver atrás a los 7 días de dejar de escribir en el esquema antiguo afecta 406 de 5 000 filas y un reposo de 3 días deja el 86,7 % de los defectos para después de contraer;
- las clases posteriores a `SE-360` se publican con el mecanismo que `build_phase2.py` y `build_phase4.py` incorporaron con la Parte 30 (texto íntegro desde `content/part-XX/SE-NNN.md`, sin `activity.yaml` ni `rubric.json`); aquí solo se añade el rango `SE-433`–`SE-444` a las clases editoriales y a las pruebas de figuras; `DEVELOPED_LAST_CLASS` y los textos globales no cambian en esta entrada, y la parte no tiene laboratorio en `labs/`; el contenido sigue pendiente de revisión humana independiente.

## 2026-11-15 — Parte 31 desarrollada y profundizada con experimentos sintéticos y sondas reales de calidad, rendimiento y resiliencia

- las clases `SE-373`–`SE-384` pasan de estructura sin contenido a clases completas sobre la API de entregas de la plataforma educativa: modelos de calidad y atributos medibles, revisión, análisis estático y quality gates, carga, estrés, picos y endurance, latencia, throughput, saturación y capacidad, perfiles, benchmarks y errores de medición, timeouts, retries, backoff y jitter, circuit breakers, bulkheads y degradación, disponibilidad, durabilidad y recuperación, compatibilidad, portabilidad e interoperabilidad, calidad de experiencia y presupuestos, un taller de presión controlada y un proyecto de informe reproducible de calidad; el portal publica el contenido íntegro de las doce clases y el índice de la parte, sin cambiar los conteos de 480 clases ni de 40 partes;
- 36 figuras con experimentos de semilla fija en tiempo virtual y sondas reales de dos sistemas: la media de 157 ms frente a un p99 de 1 929 ms, un mes con seis definiciones del mismo objetivo y un verificador de escenarios frente a 180 mutaciones; reglas de `ast` sobre 300 funciones, compuertas de cobertura total y del cambio y bloqueos espurios al reintentar; cuatro pruebas de carga sobre una cola, tres generadores ante una pausa de diez segundos y la duración y el calentamiento;
  la latencia de una cola M/M/1 frente a su fórmula, cuatro formas de variabilidad con la ley de Little y la agregación de percentiles de ocho servidores; la variación de una ordenación entre cinco procesos, el efecto de un perfilador y de una caché y dos copias idénticas comparadas con tres estadísticos; cinco políticas de reintento tras un brownout y una oleada, tres capas encadenadas y seis timeouts;
  un interruptor de circuito con cuatro configuraciones, un pool compartido frente a tres mamparos y cuatro políticas de sobrecarga; disponibilidad de 400 años con y sin causa común, pérdida de datos según el tiempo de reparación y seis umbrales de detección de fallos; doce sondas de portabilidad, cinco fronteras de datos y una matriz de compatibilidad de 25 pares; el laboratorio frente al campo, tres compuertas ante una deriva de peso y el contraste de los colores del repositorio;
  tres umbrales de estabilidad, una matriz de cuatro fallos sobre dos configuraciones y la detección frente al radio de impacto; y un validador frente a 240 mutaciones, ocho artefactos entre dos sistemas y la selección de resultados favorables;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes;
- los experimentos de tiempo virtual se ejecutaron en Windows (CPython 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con cifras idénticas; las sondas de portabilidad y los artefactos de escritura difieren entre sistemas por diseño y las mediciones de reloj de `SE-377` son lecturas de un equipo que cambian en cada ejecución; los parámetros son supuestos del autor, no se midió ninguna API, red, servicio, persona ni dispositivo reales, no se usó ninguna herramienta de carga, de interruptores ni de caos, y el validador, el verificador y las reglas se afinaron con los mismos casos que los evalúan;
- hallazgos del análisis: una media de 157 ms deja pasar un p99 de 1 929 ms; el p95 de todo un mes (227 ms) cumple y el del día del incidente (2 294 ms) no; una compuerta de cobertura total deja pasar 117 de 117 cambios con pruebas pobres y una del cambio ninguno; un generador cerrado reduce el p99 de una pausa de 9 071 ms a 232 ms; con 8 veces más variabilidad del servicio la espera media pasa de 101 a 1 364 ms con el mismo promedio; promediar los p99 de ocho servidores da 345 ms cuando el real es 323 ms;
  el jitter no evita el colapso tras un brownout (94 % del trabajo es para clientes ausentes) y un presupuesto de reintentos sí; tres capas con tres intentos envían 27 intentos a una base caída; un interruptor baja de 4 430 a unas 150 las llamadas a una dependencia colgada; un pool compartido deja a la dependencia sana en 74,3 % atendido y los mamparos en 100 %; duplicar solo una capa lleva la disponibilidad de 99,70 % a 99,80 % y cuatro despliegues malos al año le quitan 238 minutos; las doce sondas de portabilidad difieren entre Windows y Ubuntu y el tamaño de un texto con eñe es igual con bytes distintos;
  el 49,9 % de los identificadores de 54 bits cambia al pasar por un decimal de 64 bits; el contraste de la etiqueta `eyebrow` del portal sobre el papel es 3,51:1, por debajo de 4,5:1 (hallazgo registrado, no corregido en esta entrada); un validador de paquetes ve 140 de 240 mutaciones y ninguna de las coherentes; dos versiones idénticas declaran una mejora de al menos 5 % en el 96,4 % de los informes si se elige la mejor de seis métricas y de cinco repeticiones;
- las clases posteriores a `SE-360` se publican con el mecanismo que `build_phase2.py` y `build_phase4.py` incorporaron con la Parte 30 (texto íntegro desde `content/part-XX/SE-NNN.md`, sin `activity.yaml` ni `rubric.json`); aquí solo se añade el rango `SE-373`–`SE-384` a las clases editoriales y a las pruebas de figuras; `DEVELOPED_LAST_CLASS` y los textos globales no cambian en esta entrada, y la parte no tiene laboratorio en `labs/`; el contenido sigue pendiente de revisión humana independiente.
## 2026-11-15 — Parte 29 desarrollada y profundizada con simulaciones sintéticas y mediciones de cloud, plataforma e infraestructura

- las clases `SE-349`–`SE-360` pasan de borradores genéricos a clases completas sobre la plataforma de entregas de tareas llevada a una infraestructura gestionada: IaaS, PaaS, SaaS y responsabilidad compartida, máquinas virtuales, contenedores y aislamiento, orquestación y scheduling, ejecución gestionada sin servidores, redes, identidad y secretos, infraestructura como código y estado, entornos y cuentas, escalado, capacidad y costos, multi-cloud y portabilidad, plataformas internas y caminos dorados, un taller de despliegue y destrucción de un entorno y un paquete de plataforma mínima reproducible; el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con simulaciones de semilla fija y mediciones reales de tiempo: una matriz de 12 capas, la exposición anual a vulnerabilidades y la probabilidad de un error de configuración; el arranque de hilos y procesos, la densidad de instancias y el vecino ruidoso; pods sin ubicar según la política y el orden, réplicas ausentes según el intervalo de un controlador y la saturación con sobreasignación; arranques en frío, el peso de las dependencias y las reentregas que deja pasar una ventana de deduplicación;
saltos hasta la base de datos tras cada regla posible, permisos concedidos y usados y un detector de secretos; la deriva con y sin refresco, las escrituras simultáneas de un estado y el camino crítico de un grafo; el alcance de un error por estructura de cuentas, la divergencia entre entornos y las combinaciones tóxicas de permisos; políticas de escalado, latencia según la utilización y nivel de compromiso; disponibilidad compuesta, funciones comunes y tiempo y costo de mover datos; pasos manuales frente a un camino dorado, la cola del equipo de plataforma y un verificador de políticas; cortes de la creación de un entorno, orden de destrucción y barrido por etiqueta; y sumas de comprobación entre sistemas, un validador de paquetes y el gasto de entornos olvidados;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes;
- los experimentos usan solo la biblioteca estándar y se ejecutaron con CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu bajo WSL2 en el mismo equipo de 8 hilos lógicos, con salidas idénticas en todas las simulaciones y cálculos; los tiempos reales de arranque de procesos e intérpretes cambian entre ejecuciones y sistemas y se publican con su mediana y su rango, y las sumas de comprobación de `SE-360` coinciden entre sistemas solo cuando el archivo normaliza también el campo que registra el sistema creador (0 en Windows, 3 en Linux); los parámetros, los precios y las tasas son supuestos del autor, los proveedores de `SE-357` son ficticios, los tres validadores se afinaron con los mismos casos que los evalúan, no se usó ningún proveedor, orquestador, contenedor, máquina virtual, función sin servidores ni herramienta de infraestructura, no se midió latencia de red, costo ni disponibilidad reales y la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: de 12 capas, un modelo SaaS deja 3 al cliente (identidad, datos y configuración del servicio) y el 60,7 % de la exposición que queda; con un 1 % de error por ajuste, 14 ajustes dejan al menos un error en el 13,1 % de los casos y 300 en el 95,1 %; con el 91 % de la CPU ocupada, ordenar los pods por CPU decreciente deja 34 sin ubicar frente a menos de uno con llegada al azar; con 0,05 peticiones por minuto el 96,6 % arranca en frío si la instancia se descarta al minuto; ninguna regla de entropía de un detector de secretos supera el 40 % de precisión con exhaustividad mayor del 50 %;
un plan sin refresco ve de media 0,49 de 5 recursos alterados a mano y uno refrescado revierte 4,51 arreglos manuales; con tres aplicaciones simultáneas 84 de 90 intercalaciones pierden trabajo del estado; con una sola cuenta el 5,54 % de los errores de desarrollo toca producción y con una por entorno ninguno; un segundo proveedor con un DNS compartido deja los mismos 262,9 minutos de caída que uno solo; un validador de paquetes ve 16 de 16 mutaciones estructurales y 0 de 16 de las cinco que exigen interpretar el contenido; y el gasto mediano de un mes con entornos olvidados baja de 340 a 110 unidades con un plazo de 24 horas.

## 2026-11-15 — Parte 30 desarrollada con experimentos reproducibles de estrategia y técnicas de prueba

- las clases `SE-361`–`SE-372` pasan de estructura generada a clases completas sobre la estrategia de pruebas de la plataforma de entregas de tareas: calidad por riesgo y reparto de un presupuesto de pruebas, pruebas unitarias y diseño testable, integración, componentes y contratos, recorridos de extremo a extremo y aceptación, propiedades y modelos, mutación y fuzzing, dobles y entornos, datos deterministas y fixtures, exploración, accesibilidad y sondas de entrada, pruebas inestables, un taller para demostrar que una prueba detecta defectos y un proyecto que entrega una estrategia ejecutable y validable; el portal publica el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con experimentos de datos sintéticos y semilla fija: pérdida residual de cinco repartos de 40 horas, sensibilidad a estimaciones erradas y niveles de prueba contra clases de fallo; dependencias ocultas con `ast`, cobertura frente a mutantes muertos y reloj real frente a hora inyectada; ocho cambios de un proveedor frente a cuatro pruebas, contratos por consumidor y localización de un defecto de interfaz; inestabilidad por pasos, recorridos críticos elegidos e instantánea frente a aserciones semánticas; casos hasta el primer fallo de una propiedad, reducción de contraejemplos y secuencias contra un modelo; cobertura frente a mutación, fuzzing de un analizador y mutantes que sobreviven; fidelidad de los dobles, pruebas acopladas a la interacción y diferencias de entorno entre Windows y Ubuntu; fixtures frente al orden de ejecución, datos aleatorios con semilla y fuentes de no determinismo; defectos hallados por exploración, accesibilidad decidible por una regla y sondas de entrada; corridas limpias según el tamaño de la suite, una carrera enumerada y real y clasificación de la causa de una prueba inestable; poder de detección de catorce pruebas, conjunto mínimo y un validador de evidencia con 200 mutaciones; y un trimestre simulado, reasignación tras un incidente y un validador de estrategias con 200 mutaciones;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes;
- los doce experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con cifras idénticas salvo las que dependen del entorno por diseño (separador de rutas, codificación y bytes de un archivo de texto, orden de un conjunto y suma de flotantes mezclada con salidas distintas que cambian en cada ejecución y una tasa sin semilla fija); los datos son sintéticos, los parámetros son supuestos del autor, los clasificadores y los validadores se afinaron con los mismos casos que los evalúan y no se usó ningún marco de pruebas, herramienta de mutación, fuzzer, navegador, contenedor ni servidor de integración continua; la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: cinco casos con el 100 % de las líneas ejecutadas matan 9 de 16 cambios mecánicos y catorce con fronteras 13 de 16; pasar del 72 % al 94 % de cobertura de líneas no mata ningún mutante más (11 de 18) y una sola prueba sin aserciones cubre el 67 % de las líneas; un doble que acepta lo que la base rechaza pasa 4 de 8 comprobaciones de contrato; 490 de 500 órdenes aleatorios fallan con un fixture compartido y ninguno con una transacción con retroceso; con 0,1 % de fallo espurio por prueba una suite de 1 000 pasa limpia el 36,8 % de las veces y un reintento deja en verde un defecto real que falla el 30 % de las ejecuciones el 91,2 %; una condición de carrera que da verde en 100 ejecuciones falla en 40 de 40 al aumentar el trabajo; y repartir 40 horas por exposición baja la pérdida simulada de un trimestre un 11 % frente al reparto uniforme;
- se amplían `build_phase2.py` y `build_phase4.py` para publicar las clases posteriores a `SE-360` que tienen texto íntegro en `content/` sin generar actividad ni rúbrica ni alterar los conteos generados (480 clases, 40 partes, 360 contratos de actividad); `DEVELOPED_LAST_CLASS` y los textos globales no cambian en este commit.

## 2026-11-15 — Parte 28 desarrollada y profundizada con experimentos y modelos sintéticos y reproducibles de concurrencia y sistemas distribuidos

- las clases `SE-337`–`SE-348` pasan de borradores genéricos a clases completas sobre el servicio de entregas de la plataforma en el cierre de plazo: concurrencia, paralelismo y asincronía; memoria compartida, cerrojos y condiciones de carrera; actores, canales y concurrencia estructurada; tiempo, relojes y orden parcial; fallos parciales y modelos de red; consistencia, disponibilidad y particiones; consenso, elección y coordinación; idempotencia y procesamiento distribuido; replicación, reparto y balanceo; caos controlado y pruebas de distribución; un taller para reproducir una carrera y un fallo parcial y un proyecto de servicio distribuido con degradación; el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con experimentos y modelos de datos sintéticos y semilla fija: planificador en tiempo virtual, bucle de eventos que no cede y ley de Amdahl; las 70 intercalaciones de un contador, interbloqueo por orden de cerrojos y granularidad del cerrojo; orden de un buzón, cola sin límite frente a acotada y grupo de tareas frente a tareas sueltas; relojes de Lamport y vectoriales, pérdida por desfase con último escritor y resolución de los relojes de dos sistemas; qué significa un tiempo agotado, amplificación de reintentos y detector de fallos; rechazar o aceptar durante una partición, cuórums de tres réplicas y reparación con tipos fusionables; líderes por regla de elección, testigo de cerco y plazos de elección; aplicar y confirmar sobre SQLite real, retención de claves de idempotencia y salida por anexo o por clave; balanceo con cola pesada, pérdida al conmutar y reparto por hash o rango; reintentos e interruptor ante un fallo creciente, planificadores que exponen un defecto raro y un linter de planes de caos; reducción de un calendario fallido, fallos parciales de un flujo y repeticiones para ver un fallo raro; y escalera de degradación, sobrecarga con prioridad y un validador de paquete con 200 mutaciones;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes;
- los experimentos se ejecutaron con CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu bajo WSL2 con resultados idénticos salvo la resolución de los relojes de Python (15,6 ms frente a 1 ns) y una versión real de dos hilos con tiempo límite que depende de la temporización; los parámetros son supuestos del autor y no se midió ningún servicio, red, base distribuida, cola ni equipo real, ni se ejecutó Raft o Paxos;
- no cambian los conteos globales de clases desarrolladas, el README, el roadmap, el estado ni el About: se actualizarán al final de la serie de partes en una pasada aparte.

## 2026-11-15 — Parte 27 desarrollada y profundizada con experimentos sintéticos reproducibles de integración, eventos y mensajería

- las clases `SE-325`–`SE-336` pasan de borradores genéricos a clases completas sobre el flujo de la plataforma de entregas de tareas (entrega, calificación, aviso y registro): integración síncrona y asíncrona, mensajes, eventos, comandos y documentos, colas, tópicos y logs, semánticas de entrega, orden y duplicación, outbox, inbox y sagas, captura de cambios y sincronización, webhooks, sondeo y suscripciones, compatibilidad de esquemas, capas anticorrupción, observabilidad y seguridad de integraciones, un taller de duplicados y un proyecto de flujo tolerante a reintentos; el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con experimentos de datos sintéticos y semilla fija: disponibilidad de una cadena síncrona, reintentos apilados y vaciado de una cola tras una caída; contenido de un evento, comandos y eventos con distinto número de manejadores y campos del sobre; cola, tópico y log, carga por partición con una clave popular y retención frente a compactación;
  pérdidas y duplicados de tres semánticas, desorden con guarda de versión y ventanas de deduplicación; doble escritura, relevo del outbox y orden de los pasos de una saga; detección de cambios, costo de sincronizar y eventos repetidos; sondeo, verificación de webhooks y reintentos del emisor; compatibilidad de siete cambios de esquema, despliegue gradual y valores nuevos de una enumeración;
  registros de un sistema externo, cambio del proveedor y traducción con pérdida; correlación, señales de un consumidor y fugas en los registros; cinco causas de duplicados, defensas y orden de clave y efecto; y validador de un paquete, flujo ingenuo frente a tolerante y tormenta de reintentos;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` (las de la editorial ACM, que bloquea las peticiones automáticas, con Crossref) y un puente hacia el trabajo con agentes; el código de los doce experimentos se publica en `scripts/experiments_part27_a.py` y `scripts/experiments_part27_b.py`;
- los experimentos se ejecutaron con CPython 3.12.9 en Windows 11 (SQLite 3.45.3) y 3.12.3 en Ubuntu bajo WSL2 (SQLite 3.45.1) con cifras idénticas salvo los pasos de la máquina virtual de SQLite del costo de registrar cambios (un 5 % o menos de diferencia con la misma proporción); los datos son sintéticos y los parámetros son supuestos del autor,
  las reglas del validador de `SE-336` y las de normalización de `SE-333` se afinaron con los mismos casos que las evalúan, el corredor, las colas, el bus y las fallas son modelos y no se usó ningún corredor, proveedor, red, nube ni herramienta de trazado, ni se midió tiempo de reloj o cumplimiento de norma alguna; la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: una cadena de cinco dependencias que fallan el 1 % completa el 95,2 % de las peticiones; tres capas con dos reintentos cada una multiplican por 27 las llamadas a un servicio caído; con 30 % de entidades que cambian antes de leerse, una notificación mínima y un evento con el estado completo producen 299 lecturas equivocadas cada uno en consumidores distintos; deduplicar por contenido quita 835 mensajes cuando los duplicados son 200;
  una clave popular fija en 3 643 de 20 000 eventos el piso de carga de una partición; una ventana de deduplicación de 5 minutos deja pasar 1 521 de 86 590 reentregas; confirmar la base y luego publicar deja 34 de 1 000 entregas sin evento; poner la bienvenida antes del último paso de una saga deja 603 de 10 000 con un correo irreversible; sondear por marca de tiempo deja 194 filas borradas en la réplica;
  añadir un campo obligatorio rompe a 801 o 2 809 de 10 000 mensajes según qué lado se despliega primero; convertir notas externas con `float` acepta 411 fuera de rango y rompe 3 868 de 5 000; sin propagar la correlación solo el 86,1 % de las trazas de tres saltos queda completo con 5 % de pérdida por salto; la clave del mensaje deja pasar 103 duplicados del reintento del productor; un validador de paquete detecta 140 de 200 mutaciones y ninguna de las que requieren entender el sentido.

## 2026-11-13 — Documentación y About alineados con las Partes 00–26 (324 clases desarrolladas)

- el estado publicado pasa de «Partes 00–22 (`SE-001`–`SE-276`) desarrolladas» a «Partes 00–26 (`SE-001`–`SE-324`) desarrolladas»; las Partes 27–29 (`SE-325`–`SE-360`, 36 clases) siguen como borradores, las Partes 30–39 (`SE-361`–`SE-480`) como estructura y las Partes 40–44 (`SE-481`–`SE-540`) como alcance planificado sin clases publicadas (ADR-004);
- las páginas del portal de las clases 277 a 324 dejan de marcarse como «contenido en revisión»; la revisión editorial humana independiente sigue declarada como pendiente;
- README, STATUS, ROADMAP, estándar pedagógico, auditorías de fases 3 y 4, matriz de cobertura, plan maestro (hitos `SE-073`–`SE-324` marcados como hechos), auditoría de brechas, seguimiento por partes, guías de rol y `.github/repository-metadata.json` (About del repositorio: «324 desarrolladas, SE-001–SE-324», 540 clases planificadas en 45 partes) usan las mismas cifras: 324 desarrolladas, 36 borradores, 120 con estructura y 60 planificadas;
- las guías de rol añaden a «Ya desarrolladas de apoyo» clases de las Partes 23–26 verificadas contra `curriculum.yaml`;
- los conteos generados del programa (480 clases publicadas, 40 partes) no cambian.

## 2026-11-13 — Parte 25 desarrollada y profundizada con simulaciones sintéticas y mediciones reproducibles de arquitectura

- las clases `SE-301`–`SE-312` pasan de borradores genéricos a clases completas sobre la plataforma de entregas y corrección de tareas de un curso: drivers, restricciones y atributos de
  arquitectura, vistas lógica, de ejecución, de datos y de despliegue, monolito, monolito modular y servicios, capas, hexagonal y puertos y adaptadores, Domain-Driven Design estratégico
  y táctico, eventos, CQRS y event sourcing, serverless, borde y entre pares, funciones de aptitud, ADR y evaluación de alternativas, arquitectura socio-técnica, un taller de revisión
  contra escenarios y un dossier de arquitectura verificable; el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con simulaciones de datos sintéticos y semilla fija: capacidad que exige un pico, disponibilidad en serie con causa común y frontera de Pareto; dependencias no declaradas
  frente a trazas, radio de explosión por nodo y latencia de una cadena de servicios; coste de una llamada, consistencia entre servicios y un comprobador de fronteras con `ast`; módulos
  que arrastra cambiar la base de datos, velocidad de las pruebas y pruebas de contrato; acoplamiento entre contextos, invariante de un agregado y redondeo de notas; consumidores de
  eventos bajo duplicados y desorden, reconstrucción con instantáneas y retraso del modelo de lectura; arranques en frío, equilibrio de costo y difusión por rumor; coste según cuándo se
  detecta una violación, falsas alarmas de una prueba de rendimiento y alarmas sobre una deriva; ganador de una matriz según pesos, un comprobador de ADR y cuánto esperar antes de
  decidir; reparto de módulos entre equipos, módulos huérfanos y colas de entrega; revisión ejecutable contra doce escenarios, cobertura según quién revisa y sensibilidad por parámetro;
  y un validador de dossier con 200 mutaciones, mil meses de cuatro arquitecturas e impacto de revertir una decisión;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- las doce simulaciones se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con cifras idénticas salvo dos mediciones reales de tiempo (coste de una llamada y
  velocidad de una prueba), cuyos valores dependen de la máquina y se publican como rangos; los datos son sintéticos, los parámetros son supuestos del autor, los validadores de ADR y de
  dossier se afinaron con los mismos casos que los evalúan y no se midió ningún sistema, equipo, proveedor, agente de mensajería ni base de datos de producción; la parte no tiene
  laboratorio en `labs/`;
- hallazgos del análisis: con cuatro trabajadores el 70,6 % de las entregas del cierre tarda más de 2 s y con cinco ninguna; duplicar componentes baja la caída 1000 veces solo si son
  independientes y con un 30 % de causa común baja 3,5 veces; replicar la base de datos no protege si la web vive en un único nodo; una llamada por TCP en bucle local cuesta entre 200 y
  770 veces una llamada de función; cambiar la base arrastra 17 de 40 módulos por capas y 2 en hexagonal; tres ejemplos de camino feliz detectan 1 de 7 defectos de un doble y un contrato
  los 7; un contador que suma mensajes se equivoca en 1824 de 2000 entregas con 5 % de duplicados; el 11,1 % de las peticiones de los primeros 10 s de un pico arranca en frío; con 30
  muestras no hay umbral que dé pocas falsas alarmas y pocas regresiones perdidas; el 72,5 % de los cambios cruza equipos con un reparto por capa técnica y el 16,3 % con uno por
  afinidad; un validador de dossier detecta 150 de 200 mutaciones y ninguna de las dos de sentido.

## 2026-11-13 — Parte 26 desarrollada y profundizada con experimentos sintéticos reproducibles de datos, persistencia y recuperación

- las clases `SE-313`–`SE-324` pasan de borradores genéricos a clases completas sobre la capa de datos de la plataforma de entregas de tareas: modelado conceptual, lógico y físico, modelos relacional, documental, de clave-valor y de grafos, transacciones y aislamiento, restricciones e invariantes, consultas e índices,
  migraciones compatibles, replicación y partición, cachés entre capas, backups y pruebas de recuperación, privacidad, retención y ciclo de vida del dato, un taller de migración peligrosa y un paquete de capa de datos recuperable; el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con experimentos de datos sintéticos y semilla fija, la mayoría sobre SQLite real: anomalías de una tabla plana, tamaño de la clave primaria y falsos positivos de una lista en una columna; filas frente a documentos, búsqueda por clave y consultas recursivas con ciclo; actualización perdida en 90 intercalaciones, cortes de una transferencia y sesgo de escritura;
  filas inválidas por capa de restricciones, comprobar y luego insertar y borrado con la clave foránea apagada; pasos con y sin índice, orden de un índice compuesto y costo de escritura; compatibilidad entre versiones, lotes de relleno y migraciones revertidas; lecturas obsoletas y cuórum, claves movidas por un anillo de hash y claves calientes;
  políticas de caché, estampida y carrera de relleno; pérdida por intervalo de copia, copia en caliente y niveles de verificación; restos tras borrar, retención y personas únicas; analizador de migraciones, ensayo en tres entornos y cortes de una migración; y validador de paquetes, un mes con dos incidentes y costo de retener copias;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes;
- los doce experimentos se ejecutaron en Windows (Python 3.12.9, SQLite 3.45.3) y en Ubuntu bajo WSL2 (3.12.3, SQLite 3.45.1) con cifras idénticas salvo los pasos de la máquina virtual del relleno por lotes (un 7 % mayores en Ubuntu con la misma proporción) y los bytes comprimidos con zlib (menos de un 1 % de diferencia); los datos son sintéticos, los parámetros son supuestos del autor,
  los dos validadores se afinaron con los mismos casos que los evalúan, el modelo de niveles de aislamiento, el cuórum, las cachés y la bitácora del mes simulado son modelos y no motores, y no se usó ningún servidor de bases de datos, base distribuida, caché real ni nube, ni se midió tiempo de reloj, de restauración ni cumplimiento legal; la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: leer-sumar-escribir acierta en 6 de 90 intercalaciones de tres clientes; una lista de identificadores en una columna devuelve 33 099 resultados cuando los correctos son 7 408; con una restricción `UNIQUE` los duplicados dejan de colarse y el motor rechaza 108 inserciones; con las claves foráneas apagadas, que es el valor por defecto de SQLite, borrar un curso deja 50 entregas huérfanas sin error;
  un índice sobre una columna con el 90 % de las filas iguales ahorra un 3 %; el reparto por módulo mueve el 79,9 % de las claves al añadir un quinto nodo frente al 21,1 % de un anillo con 128 puntos; copiar el archivo de una base en uso da `integrity_check` en ok y una suma 197 unidades menor; los niveles de verificación estructurales ven 88 de 200 copias alteradas y todos los niveles 180;
  tras borrar la mitad de las filas siguen 2 087 de 2 090 ocurrencias de un valor en el archivo; tres atributos aparentemente inofensivos dejan únicas a 3 094 de 5 000 personas y un hash de correo sin clave se invierte por completo con un diccionario; un analizador de texto ve 141 de 200 mutaciones de una migración y ninguna de las que dañan los datos sin romper la sintaxis.

## 2026-11-13 — Parte 24 desarrollada y profundizada con análisis de código y simulaciones reproducibles

- las clases `SE-289`–`SE-300` pasan de borradores genéricos a clases completas sobre el componente `tarifas` de una plataforma de entregas: cohesión, acoplamiento y encapsulación, SOLID y sus límites, composición, herencia y delegación, patrones creacionales, estructurales y conductuales, patrones funcionales, reactivos y concurrentes, code smells y diagnóstico contextual, refactorización segura apoyada por pruebas, diseño para cambio, prueba y operación, complejidad accidental y esencial, deuda técnica, interés y opciones, un taller de refactorización de una función heredada y un proyecto de evolución compatible de un componente; el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con código analizado con `ast` y simulaciones de semilla fija: LCOM4, sitios de edición y primer ciclo de dependencias; reglas añadidas, violaciones de Liskov e interfaces anchas; clase base frágil, orden de decoradores y herencia múltiple al azar; singleton y orden de pruebas, aislamiento de observadores y similitud entre patrones; detección de impureza, contrapresión e intercalaciones de dos hilos; umbrales de olores sobre código real fijado por commit, duplicación frente a parámetros y envidia de características; mutación, cobertura frente a mutantes y tamaño del paso de un refactor; módulos tocados por cambio, reloj real e inyectado y correlación de registros; la misma regla en dos formas, cobertura por pares y complejidad ciclomática y cognitiva; políticas de pago de deuda, refactorizar ahora o después y puntos calientes; maestro dorado por pasos, mutantes y caminos según las entradas; y firma frente a comportamiento, ventana de deprecación y contratos de consumidor;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes;
- los experimentos usan solo la biblioteca estándar y se ejecutaron con CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu bajo WSL2 con salidas idénticas; los parámetros son supuestos del autor, el análisis de `SE-294` se fija al commit `4dafaa63` y no se midió ningún proyecto de producción, ningún reloj real, ningún hilo ni ningún consumidor real; el contenido sigue pendiente de revisión humana independiente.

## 2026-11-13 — Parte 23 desarrollada y profundizada con simulaciones sintéticas reproducibles

- las clases `SE-277`–`SE-288` pasan de borradores genéricos a clases completas sobre una plataforma educativa ficticia que incorpora una pieza de un dominio especializado en cada una: software científico y
  reproducibilidad, ingeniería de datos y procesamiento analítico, aprendizaje automático como componente de producto, videojuegos y simulación, gráficos, audio y realidad extendida, fintech e invariantes
  monetarias, salud y datos sensibles, cadenas de bloques y contratos inteligentes, sistemas geoespaciales y temporales, low-code y automatización visual, un taller de comparación de riesgos entre dominios
  y un proyecto de diseño profundo de un dominio elegido; el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con simulaciones de datos sintéticos y semilla fija: orden de la suma, dispersión entre semillas y horizonte del caos; reintentos con duplicados, eventos tardíos y asimetría de claves; fuga de la
  etiqueta, prevalencia y alarmas de deriva; paso de tiempo fijo, atravesar una pared y espiral de la muerte; latencia y subcargas de audio, aliasing y fotogramas fuera de presupuesto; dinero con coma flotante,
  mutantes de un libro mayor y cobros duplicados; anonimización por generalización, fusión de fichas y fatiga de alarmas; prueba de trabajo, doble gasto y reentrada; distancia en grados, un año de reloj e índice
  de rejilla; caminos frente a pares, eventos duplicados y automatizaciones huérfanas; estabilidad de un ranking, acuerdo entre evaluadores y cobertura de controles; y mutaciones de un dosier, sensibilidad de
  supuestos y huella del paquete;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes;
- las simulaciones se ejecutaron con CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu bajo WSL2 con salidas idénticas (salvo el orden de listado de elementos empatados en `SE-287`); los parámetros son supuestos
  del autor y las puntuaciones de riesgo de `SE-287` son un juicio ilustrativo; no se usó ningún código científico real, motor de procesamiento, modelo de aprendizaje automático, motor de juego, dato clínico,
  procesador de pagos ni red de cadena de bloques, no se midió confort ni percepción y no se evaluó ninguna norma;
- el alcance (480 clases publicadas, 540 planificadas) y los textos globales no cambian en esta entrada.


## 2026-11-13 — Guías por rol alineadas con el alcance de 540 clases: 42 guías

- dos guías nuevas, de más de 2.200 palabras cada una y con la misma estructura, generador y contrato que las demás: `Agentic Harness Engineer` (harness, contexto, herramientas, bucles, evaluación y recuperación de agentes) y `Domain & Methodology Engineer` (TDD, BDD, ATDD, DDD, contratos y SDD como práctica de equipo); el programa pasa de 40 a 42 guías profesionales;
- cada guía, el mapa del README y `roles/README.md` incorporan el estado real de cada parte (00–22 desarrolladas, 23–29 borradores, 30–39 estructura), una sección «Clases ya desarrolladas que sostienen la ruta hoy» con clases de las Partes 00–22 verificadas contra `curriculum.yaml` y una sección «Ampliación planificada» con las Partes 40–44 (`SE-481`–`SE-540`) por rol, sin enlaces porque esas clases no existen;
- las guías `ai-augmented-software-engineer`, `ai-systems-engineer`, `qa-test-engineer` y `software-architect` delimitan su frontera con las dos nuevas para evitar solapamiento;
- la tabla de cuerpos de conocimiento del README añade referencias a TDD, BDD, Gherkin, Specification by Example, DDD, Pact, GoF, POSA, PoEAA, Enterprise Integration Patterns, patrones cloud, ISO/IEC/IEEE 42010, estilos arquitectónicos, patrones agénticos, sistemas con LLM, evaluación de agentes, A2A, ISO/IEC 42001, Spec Kit y AGENTS.md; cada URL se comprobó con `curl` (las páginas de ISO responden 403 a clientes automatizados);
- «Cobertura disponible hoy» se corrige con los conteos reales (276 desarrolladas, 84 borradores, 120 con estructura y 60 planificadas); `STATUS.md`, `validate_repository.py` y `tests/test_roles.py` pasan a exigir 42 guías y a comprobar que ninguna guía enlace una parte planificada;
- los conteos generados del programa (480 clases publicadas, 40 partes) no cambian.

## 2026-11-13 — Documentación alineada con las Partes 00–22 y el alcance de 540 clases

- el estado publicado pasa de «Partes 00–05» a «Partes 00–22 (`SE-001`–`SE-276`) desarrolladas»; las páginas de las clases 73 a 276 dejan de marcarse como «contenido en revisión» y la revisión editorial humana independiente sigue declarada como pendiente;
- README, ROADMAP, STATUS, portal, guías de rol y estándar pedagógico describen el alcance planificado de 540 clases (Partes 40–44, `SE-481`–`SE-540`) sin publicarlo como clases: los conteos generados siguen siendo 480 clases y 40 partes;
- nueva decisión `ADR-004-expand-to-540-class-scope.md`.

## 2026-11-13 — Parte 22 desarrollada y profundizada con simulaciones sintéticas reproducibles

- las clases `SE-265`–`SE-276` pasan de borradores genéricos a clases completas sobre un nodo ambiental de una sala de estudio: hardware, firmware y software embebido,
  microcontroladores, periféricos y buses, restricciones de memoria, energía y cómputo, sistemas de tiempo real, interrupciones y estado compartido, protocolos IoT y conectividad
  intermitente, actualizaciones OTA y recuperación, identidad de dispositivo y gestión de claves, edge y pasarelas, safety, seguridad y vida útil prolongada, un taller de modelado
  de fallos y un dispositivo simulado operable y actualizable; el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con simulaciones de datos sintéticos y semilla fija: latencia de un botón, un acumulador de 16 bits y mutantes de un antirrebote; eficiencia de I²C y SPI, errores no
  detectados por paridad, suma y CRC-8 y sobremuestreo de un convertidor; vida de una pila, desgaste de una flash y zona muerta de un filtro de enteros; planificabilidad rate-monotonic,
  plazos incumplidos e inversión de prioridad; posiciones de una interrupción, lecturas partidas y búfer circular; garantías de entrega, cola de almacenar y reenviar y tormenta de
  reconexión; cortes de energía en una actualización, actualización diferencial y despliegue por etapas; alcance de una clave extraída, ventanas de tiempo y semillas débiles;
  estrategias de reporte, decisión local o en la nube y codificación de la carga; votación con causa común, plazo de vigilancia y vuelta de un contador; inyección de fallos, cortes
  durante una escritura y estabilidad de un AMFE; y un mes de flota simulada, un validador de paquetes y una versión defectuosa en mil dispositivos;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- las doce simulaciones se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con cifras idénticas, sin excepción; los datos son sintéticos, los parámetros son
  supuestos del autor, los dos validadores se afinaron con los mismos casos que los evalúan y no se usó ningún microcontrolador, sistema operativo de tiempo real, agente MQTT,
  cargador de arranque, pasarela ni red real, ni se midió consumo, peor caso de ejecución o ataque alguno; la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: sondear un botón en un bucle con radio da una espera máxima de 166 ms frente a 0,03 ms con una interrupción; 32 lecturas de 12 bits desbordan siempre un
  acumulador de 16 bits con señal alta; la paridad no detecta ningún error de dos bits; sobrescribir una imagen deja el dispositivo inservible en 17 de 19 cortes de energía; una
  espera exponencial sin jitter deja 4309 de 5000 dispositivos sin conectar a los 900 s; la comparación directa de tiempos decide mal el 33,35 % de los temporizadores armados antes
  de la vuelta de un contador de 32 bits; una deriva lenta pasa todas las comprobaciones locales y solo una referencia independiente la ve.

## 2026-11-13 — Parte 20 desarrollada y profundizada con experimentos sintéticos y modelos reproducibles de backend, APIs y procesamiento asíncrono

- las clases `SE-241`–`SE-252` pasan de borradores genéricos a clases completas sobre el backend de la plataforma de entregas de tareas: fronteras de confirmación, recursos y semántica de
  métodos, estilos de interfaz, validación y errores, identidad y autorización por objeto, idempotencia y reintentos, trabajo diferido, archivos extensos, caché y limitación de tasa,
  sondeos y apagado ordenado, un taller de reparación de una API defectuosa y un proyecto de servicio contractual; el portal publica ahora el contenido íntegro de las doce clases y el
  índice de la parte;
- 36 figuras con cálculos, simulaciones y mediciones de datos sintéticos y semilla fija: cadena síncrona frente a diferida, 24 escenarios de caída con y sin outbox y tres servidores HTTP
  locales, un GET con efecto frente a un rastreador, actualización perdida e `If-Match` y paginación por desplazamiento frente a clave, bytes por pantalla, consultas N+1 y coste de consultas
  anidadas, 14 cargas JSON contra dos validadores, deriva de un contrato y reintentos por clase de error, ocho ataques a un token, filas ajenas con y sin comprobación de dueño y cobertura de
  una política, duplicados con y sin clave, tormenta de reintentos y ventana de la clave, efectos duplicados en una cola, espera frente a M/M/1 y mensaje venenoso, memoria por trozos,
  subida reanudable, nombres hostiles y bombas de descompresión, aciertos y obsolescencia de una caché, estampida y cuatro limitadores, sondeos de vida, apagado con drenaje y
  calentamiento, tres suites contra una API con diez defectos, inyección SQL y caídas inyectadas, alertas por tasa de consumo y deriva de un contrato;
- cada clase añade tres secciones con experimentos, `Fallo controlado`, `Errores comunes`, `Preguntas frecuentes`, `Puente hacia el trabajo con agentes` y fuentes vinculadas a afirmaciones;
  los experimentos usan CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu bajo WSL2 con salidas deterministas idénticas; las diferencias informadas son los tiempos de servidor local, las
  consultas al origen sin protección en una estampida de hilos, los nombres de archivo con barra invertida y los tiempos de comparación de firmas;
- los parámetros (latencias, porcentajes de caída, capacidades, SLO, defectos de la API y mutaciones) son supuestos del autor; no se midió a ninguna persona, producto ni servicio, y las
  fuentes sin enlace verificado en esta ejecución (por falta de acceso de red autorizado) se citan por título y se enumeran en `Evidencia medida y límites`;
- la guía de la parte incorpora una sección «Evidencia medida y límites», el resumen operativo y el proyecto integrador.

## 2026-11-13 — Parte 21 desarrollada y profundizada con experimentos sintéticos y modelos reproducibles de software móvil, escritorio y multiplataforma

- las clases `SE-253`–`SE-264` pasan de borradores genéricos a clases completas sobre el cliente de la plataforma de entregas de tareas: modelos de aplicación, ciclo de vida y restauración
  del estado, decisión de construcción, almacenamiento local y fusión, permisos y capacidades, interacción y accesibilidad, distribución y versiones que conviven, trabajo sin conexión y
  conflictos, presupuesto de recursos, seguridad del cliente, un taller de adaptación a dos plataformas y un proyecto con sincronización; el portal publica ahora el contenido íntegro
  de las doce clases y el índice de la parte;
- 36 figuras con cálculos, simulaciones y mediciones de datos sintéticos y semilla fija: dos copias sobre un archivo compartido, controles alcanzables según el ancho y arranques en frío,
  ediciones perdidas por política de guardado, restauración con tres políticas de lectura y coste de guardar de forma atómica, pesos sorteados de cuatro opciones, coste de una frontera
  entre capas y capacidades comunes, modos de SQLite, terminación a mitad de escritura y fusión por registro o campo, estados de permiso, revocación y unicidad de la ubicación, acierto
  de toques simulados, orden de foco y contraste, adopción por canal, clientes rotos al retirar un campo y descarga por bloques, estructuras replicadas, duplicados y relojes desfasados,
  lista completa o ventana, sondeo, lote y empuje y tamaño de caché, integridad, confinamiento de rutas y secretos, siete diferencias entre Windows y Ubuntu, coste de adaptación con
  intervalo y contrato de adaptadores, sincronización con fallos, un servidor local con clave de idempotencia y 240 mutaciones de un paquete;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con salidas deterministas idénticas salvo los tiempos, la versión de SQLite (3.45.3 y 3.45.1)
  y los siete comportamientos de sistema que `SE-263` mide porque difieren; los datos son sintéticos, los parámetros son supuestos del autor, no se usó ningún teléfono, emulador, SDK,
  tienda ni biblioteca de producción, no se midió la batería ni se cortó la energía y los secretos y rutas son ficticios; la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: dos copias de una aplicación sobre un mismo archivo dejan 127,65 de 200 actualizaciones; con una recuperación de memoria agresiva el 66,5 % de los regresos
  parte de cero; guardar solo al cerrar pierde 109 ediciones por sesión y combinar guardado periódico y de segundo plano 1,7; el ganador de una tabla de decisión cambia con una
  unidad en las puntuaciones en el 41 % de los casos; 500 inserciones tardan 2874 ms en transacciones separadas y 8 ms en un lote; un par de lugares a 1 km identifica al 99,1 % de
  2000 personas ficticias; un gris habitual queda a 0,02 del contraste mínimo; retirar un campo a los 30 días rompe al 73,7 % de un canal empresarial lento; reintentar sin identificador
  convierte 30 operaciones en 44; siete de siete comportamientos del sistema de archivos difieren entre Windows y Ubuntu; y un validador de presencia deja pasar 104 de 240 mutaciones.

## 2026-11-13 — Parte 18 desarrollada y profundizada con experimentos sintéticos y procesos locales reproducibles

- las clases `SE-217`–`SE-228` pasan de borradores genéricos a clases completas sobre `notas`, una herramienta de línea de comandos sintética de la plataforma de entregas: diseño de la
  superficie de una CLI, entrada y salida estándar y tuberías, configuración y precedencia, códigos de salida y diagnóstico, presentación en terminales y accesibilidad, servicios y
  ciclo de vida, planificadores, trabajadores y lotes, automatización idempotente y reanudable, distribución y actualización de binarios, telemetría opt-in, un taller de
  endurecimiento y un paquete operable multiplataforma; el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con cálculos, simulaciones y mediciones de procesos locales: abreviaturas de flags que dejan de valer, contrato observable de una CLI, búfer y cierre de tuberías,
  seis resolvedores de precedencia frente a 64 combinaciones, códigos de salida por sistema, coste de los reintentos, color y truncado en tuberías, ancho de nombres Unicode,
  terminación y preparación de servicios, políticas de solape y trabajos venenosos, seis estrategias de escritura frente a 40 caídas, integridad y lanzamientos escalonados,
  unicidad de atributos y sesgo del opt-in, diez fallos inyectados, citado de argumentos y trece pruebas de contrato con seis defectos y 102 mutantes de un manifiesto;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con salidas idénticas salvo las diferencias que se informan como resultados (el código
  de salida fuera de 0–255, la excepción de una tubería cerrada, `terminate()` frente a `SIGTERM`, el reemplazo de un archivo abierto, el citado con `shell=True`, el salto de línea
  del hash de un archivo y los tiempos); los datos son sintéticos, los parámetros son supuestos del autor, los defectos inyectados son variaciones sobre herramientas de juguete y
  no se usó ningún terminal interactivo, servicio de Windows, systemd, orquestador, cola real ni telemetría de personas; la parte no tiene laboratorio en `labs/`;
- `build_phase3.py` y `build_phase4.py` publican ahora el contenido de `content/part-XX/` también para las clases de la fase 4 que lo tienen (`published_markdown`);
- hallazgos del análisis: un flag nuevo rompió 9 de 14 abreviaturas que funcionaban; `sys.exit(256)` se lee como éxito en Linux y como 256 en Windows; `false | cat` devuelve 0; el
  color partió la búsqueda de una frase en 200 líneas; `terminate()` no ejecuta limpieza en Windows; reintentar todo gastó 24 092 intentos inútiles; la estrategia «anexar y marcar»
  duplicó en 19 de 40 caídas; `os.replace` falla con el destino abierto en Windows; seis de diez atributos hicieron únicas a dos de cada tres instalaciones; la versión frágil de una
  copia de seguridad dañó en silencio 7 de 10 escenarios; y una suite de contrato descubrió que `allow_abbrev` no se hereda en los subcomandos.

## 2026-11-13 — Parte 19 desarrollada y profundizada con experimentos sintéticos reproducibles

- las clases `SE-229`–`SE-240` pasan de borradores genéricos a clases completas sobre una aplicación web de entregas de tareas con conectividad irregular: HTML semántico, contraste y
  cascada, JavaScript, DOM y eventos, renderizado en cliente, servidor, estático e híbrido, estado y datos remotos, formularios y validación, URLs y enrutado, rendimiento y presupuestos,
  seguridad del navegador, PWA y sincronización, SEO y metadatos, un taller de flujo resiliente y un proyecto de aplicación accesible y offline; el portal publica ahora el contenido
  íntegro de las doce clases y el índice de la parte;
- 36 figuras con cálculos y simulaciones de datos sintéticos y semilla fija: un linter semántico con 220 mutaciones y la razón de contraste de 5000 pares de colores, una carrera de
  especificidad, un modelo de dos colas del bucle de eventos contrastado con Node y una delegación de eventos en un modelo de DOM, bytes reales y un modelo de tiempo de tres
  estrategias de renderizado, desajustes de hidratación y obsolescencia por caducidad, reconciliación de listas, estado copiado frente a derivado y respuestas fuera de orden,
  seis validadores de correo y normalización Unicode, normalización de URLs, enrutado y estado en la URL, compresión, ruta crítica y percentiles con pocas visitas, codificación por
  contexto, políticas de contenido, SameSite y CORS, estrategias de caché, descargas por versión y duplicados al sincronizar, dos analizadores de `robots.txt`, navegación facetada y
  un auditor de metadatos, una máquina de estados mutada, reintentos con y sin dispersión y defectos de accesibilidad automatizables, y un validador de manifiesto, una auditoría de
  cabeceras de un servidor local y una suite de pares frente a defectos de tres factores;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9, Node 24.11) y en Ubuntu bajo WSL2 (3.12.3, Node 20.20) con salidas idénticas salvo los tiempos de compresión y de render;
  los datos son sintéticos, los parámetros son supuestos del autor, las reglas de los linters se escribieron sabiendo qué mutaciones se aplicarían, y no se usó ningún navegador,
  lector de pantalla, service worker real, buscador ni herramienta de auditoría ni se midió a ninguna persona; la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: un linter de ocho reglas detecta 200 de 220 mutaciones y ninguna de las 20 que cambian el significado de un texto alternativo; solo 11 % de los pares de colores
  aleatorios alcanza 4,5:1; un modelo de dos colas acierta el orden de 300 programas y uno de una cola 221; un total copiado diverge en 13,5 % de las secuencias con 1 % de olvidos; la
  última respuesta recibida deja un resultado obsoleto en 34,67 % de las búsquedas; con 30 visitas se declara que se cumple un presupuesto que no se cumple en 22 % de los casos; sin clave
  de idempotencia 2000 envíos producen 476 duplicados; el reintento exponencial sin dispersión tarda 902 s frente a 23 s con dispersión; y una suite de pares halla 32 de 60 defectos de tres
  factores.

## 2026-11-13 — Parte 17 desarrollada y profundizada con experimentos sintéticos y de Git reproducibles

- las clases `SE-205`–`SE-216` pasan de borradores genéricos a clases completas sobre el portal documental de la plataforma de entregas de tareas: audiencias y tareas, los cuatro
  tipos de página, README y primer éxito, registros de decisiones, diagramas generados, documentación de una API con ejemplos ejecutables, runbooks, documentación como código,
  búsqueda y glosarios, documentación para máquinas y agentes, un taller de reconstrucción de conocimiento perdido y un portal versionado con paquete reproducible y auditoría; el
  portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con cálculos y simulaciones de datos sintéticos y semilla fija: clics hasta una página y coherencia de un dato repetido, un clasificador de tipos de página y un tutorial
  ejecutable, un embudo de pasos y un detector de deriva del README, un linter de ADR y la caducidad de sus suposiciones, cruces de aristas y un generador de diagramas estable, ejemplos
  de una API y los códigos de un servidor local, idempotencia de los pasos de un runbook, enlaces rotos y huellas de construcción, búsqueda con sinónimos, fragmentación de documentos
  para recuperación, el factor de camión y `git log -S`, versiones etiquetadas y un paquete zip reproducible;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9, Git 2.55) y en Ubuntu bajo WSL2 (3.12.3, Git 2.43) con salidas idénticas; durante el trabajo aparecieron dos
  diferencias entre sistemas que se corrigieron y se documentan: un servidor local que responde 413 sin leer el cuerpo aborta la conexión en Windows y no en Ubuntu, y un zip con
  orden, fecha y permisos fijos tenía huellas distintas en cada sistema hasta fijar también el campo de sistema de origen; los datos son sintéticos, los parámetros son supuestos
  del autor, las reglas léxicas se probaron con casos construidos por el propio autor, no se usó ningún modelo de lenguaje, herramienta de documentación de producción ni portal real,
  y la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: con tres cambios al año, un dato repetido en seis páginas solo sigue coherente el 5,3 % de las veces; un linter de ADR que ve la forma no detecta ninguna de
  las alternativas vacías; renombrar 5 archivos y 8 títulos rompe 66 enlaces; el 55 % de las respuestas de un servidor ante peticiones erróneas lleva códigos no documentados; un
  linter que ignora los bloques de código da 102 avisos de los cuales 97 son falsos; fragmentar por 500 caracteres separa la regla de su excepción en dos de cada tres casos; un
  filtro léxico detecta las 6 instrucciones ocultas literales y ninguna de las 8 ofuscadas; cuando se va la persona con más commits queda sin responsable el 45 % de los archivos.


## 2026-11-13 — Parte 16 desarrollada y profundizada con experimentos reproducibles de Git y colaboración

- las clases `SE-193`–`SE-204` pasan de borradores genéricos a clases completas sobre el repositorio de la plataforma de entregas de tareas: modelo de objetos y áreas de Git, commits
  atómicos y recuperación, integración con fusión, rebase y squash, revisión por riesgo, flujos de ramas, trazabilidad de issues, propietarios y convenciones, contribución externa y
  gobernanza, licencias, firmas y protección del repositorio, un taller de rescate de una integración y un proyecto de contribución revisable; el portal publica ahora el contenido
  íntegro de las doce clases y el índice de la parte;
- 36 figuras con experimentos de Git real en repositorios temporales con identidad y fechas fijas o con datos sintéticos y semilla fija: identificadores de blob, árbol y commit
  reconstruidos a mano, estados entre las tres áreas, objetos sueltos frente a empaquetados, bisección sobre cuatro historias, qué sobrevive a seis errores, reiniciar frente a
  revertir, fusión, rebase y squash, probabilidad de conflicto según distancia y ediciones, `rerere`, `range-diff`, triaje por riesgo de 300 pull requests sintéticos, pilas de PR,
  conflictos según la vida de la rama, un conflicto semántico, backports, extracción de cierres con dos reglas, reproducción según el detalle del informe, una matriz de trazabilidad,
  un archivo de propietarios sobre 600 rutas, un validador de mensajes, autoría tras un reformateo, concentración de commits, reglas de decisión, un fork desfasado, un analizador de
  expresiones de licencia, un inventario transitivo, la huella de un texto de licencia, firmas SSH, la reescritura de una cadena de firmados, políticas de protección, seis órdenes de
  fusión de tres ramas, tres rescates, estilos de marcas y un validador de doce comprobaciones sobre catorce contribuciones;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9 y Git 2.55) y en Ubuntu bajo WSL2 (Python 3.12.3 y Git 2.43) con salidas idénticas salvo los tiempos de firma y verificación
  de commits; los datos son sintéticos, los parámetros son supuestos del autor, la clave de firma es desechable, la regla de cierres y el modelo de CODEOWNERS simplifican los de una
  plataforma, y no se usó ningún alojamiento, servicio de firma ni herramienta de inventario de licencias; la parte no tiene laboratorio en `labs/` y no ofrece asesoría legal;
- hallazgos del análisis: agrupar cuatro cambios por commit ahorra dos ejecuciones de bisección y multiplica por 2,5 las líneas que hay que leer; un cambio sin agregar o un archivo sin
  rastrear no se recuperan tras un `reset --hard`; reiniciar y forzar la publicación hace reaparecer los commits «borrados» cuando otro clon publica; las ediciones en líneas contiguas
  entran en conflicto el 100 % de las veces; una fusión sin conflicto de texto dejó un panel imprimiendo 42 en lugar de 60; revertir una fusión mala y volver a fusionar responde
  «Already up to date»; una comparación literal decidió mal 146 de 300 expresiones de licencia y un análisis de dependencias directas no ve el 89 % de los paquetes fuera de política;
  una prueba que afirma `True` pasa las doce comprobaciones de forma.

## 2026-11-13 — Parte 15 desarrollada y profundizada con simulaciones sintéticas reproducibles

- las clases `SE-181`–`SE-192` pasan de borradores genéricos a clases completas sobre el plan de lanzamiento de la plataforma de entregas de tareas: modelos predictivos, iterativos
  e incrementales, principios ágiles frente a ceremonias, Scrum, Kanban, XP y Shape Up leídos por sus políticas, Lean, teoría de colas y límites de trabajo, estimación con rango y
  evidencia histórica, planificación de entregas y dependencias, riesgos, supuestos, issues y decisiones, definiciones de listo, terminado y aceptación, métricas de flujo, calidad
  y resultados, retrospectivas y mejora del sistema de trabajo, un taller de planificación bajo incertidumbre y un plan adaptativo con disparadores y barreras; el portal publica
  ahora el contenido íntegro de las doce clases y el índice de la parte, y `build_phase4.py` usa las fuentes editoriales de `content/part-15/` para esas clases;
- 36 figuras con simulaciones de datos sintéticos y semilla fija: esfuerzo según el intervalo de retroalimentación, valor si el proyecto se corta y cruce según la volatilidad;
  valor perdido por no aprender del uso, sobrecoste de ceremonias y conflictos según la vida de una rama; espera de un urgente, reglas de compromiso y tiempo fijo; espera según la
  utilización, ley de Little con límite de trabajo y variabilidad con lotes; suma de medianas, cobertura de intervalos y solape de tallas; convergencia de caminos, dependencias
  externas y órdenes de entrega; riesgos con causa común, orden de validación de supuestos y un verificador de decisiones; comprobaciones correlacionadas, refinamiento previo y un
  verificador de criterios; resumen de tiempos, velocidad premiada y tamaño de muestra de un percentil; acciones por retrospectiva, detección de una mejora e intervenciones sobre una
  cola; calibración de pronósticos, margen frente a colchón y sensibilidad; disparadores de replanificación, un validador de planes y mil proyectos con tres estrategias;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- las doce simulaciones se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con salidas idénticas, sin excepción; los datos son sintéticos, los parámetros son
  supuestos del autor, los tres verificadores se afinaron con pocos ejemplos y se evaluaron con casos propios o nuevos mínimos, y no se observó ningún equipo ni se midió ninguna
  estimación, retrospectiva o métrica real; la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: el intervalo de menor esfuerzo está en ciclos de cuatro piezas y no en el más corto; comprometer la media del rendimiento falla en 44 % de los sprints;
  la espera se multiplica por 19 entre 50 % y 95 % de utilización; cumplir la suma de medianas de 30 tareas ocurre en 12,4 % de los casos; un intervalo del 80 % con 3 semanas de
  historia cubre 32,5 %; con una causa común el percentil 85 del retraso de diez riesgos sube de 35 a 66 días; añadir comprobaciones correlacionadas deja los escapes en 4258 de 10 000;
  acordar 8 acciones por retrospectiva termina las mismas 9,4 que acordar 2; un disparador de 4 semanas con un aviso da falsa alarma en 68 % de los proyectos sanos.

## 2026-11-13 — Parte 14 desarrollada y profundizada con experimentos sintéticos reproducibles

- las clases `SE-169`–`SE-180` pasan de borradores genéricos a clases completas sobre la entrega de una tarea en la plataforma de entregas: diseño centrado en personas y tareas,
  arquitectura de información, interacción y retroalimentación, estados vacíos, de carga y de error, criterios de accesibilidad, semántica, teclado y foco, diseño visual,
  adaptación a anchos y preferencias, internacionalización, medición de usabilidad, un taller de auditoría y reparación y un prototipo evaluado; el portal publica ahora el
  contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con cálculos y simulaciones de datos sintéticos y semilla fija: tres diseños cronometrados con operadores, la persona promedio en varias dimensiones y un embudo,
  anchura de menús, ordenamiento de tarjetas y alcance de un grafo, tamaño del objetivo, doble envío y confirmar frente a deshacer, estados imposibles, reintentos y latencias,
  razones de contraste, un auditor de reglas y destinos, orden de foco, nombre accesible y encabezados, daltonismo, reflujo e inversión de colores, anchos de pantalla, matriz
  de preferencias y peso de imágenes, plurales, Unicode y fechas ambiguas, problemas hallados, intervalos y potencia, una auditoría con órdenes de reparación y mutaciones y
  la probabilidad de ver una barrera, la cobertura de modalidades y kappa;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con salidas idénticas; los datos son sintéticos, los parámetros son supuestos del autor
  o valores medios de la literatura, las matrices de daltonismo son una aproximación, y no se usó ningún escáner de producción, lector de pantalla, navegador ni biblioteca de
  localización ni se evaluó a ninguna persona; la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: un formulario de nueve campos tarda 50,7 s frente a 18,6 s con tres; con diez dimensiones ninguna de 5 000 personas es promedio en todas; una sola
  etapa de seis pierde 315 de 1 000 personas; un auditor de reglas detecta 7 de 12 defectos y ninguno de los presentes pero incorrectos; el rojo y el verde caen de 119,8 a 7,3 de
  distancia en deuteranopía; invertir colores hace perder el contraste a 956 de 2 441 pares que lo cumplían; la regla de «uno o plural» falla en 120 de 121 números en ruso; cinco
  participantes hallan 62 % de los problemas frente al 76,6 % de la fórmula; y declarar conformidad ignorando lo no probado permite 368 de 1 000 afirmaciones que una política
  estricta no admite.

## 2026-11-13 — Parte 13 desarrollada y profundizada con experimentos sintéticos reproducibles

- las clases `SE-157`–`SE-168` pasan de borradores genéricos a clases completas sobre la regla de penalización por entrega tardía de una plataforma de entregas: especificación
  informal, semiformal y formal, ejemplos y BDD, contratos e invariantes, modelos, máquinas de estados, esquemas, interfaces y eventos, compatibilidad y versionado, papel de la
  especificación frente al código, pruebas contractuales, un taller y un paquete de especificaciones trazables; el portal publica ahora el contenido íntegro de las doce clases y
  el índice de la parte;
- 36 figuras con cálculos y simulaciones de datos sintéticos y semilla fija: dieciséis lecturas de una frase y huecos de una tabla de decisión, variantes defectuosas frente a suites
  de ejemplos y cobertura de pares, contratos frente a pruebas de ejemplo y subtipado, deriva entre modelo y código y normalización en SQLite, búsqueda en anchura con contraejemplo,
  explosión de estados e intercalados de una carrera, esquemas abiertos y cerrados y una expresión regular con retroceso, un linter OpenAPI, eventos duplicados y reordenados,
  compatibilidad entre lectores y ventanas de deprecación, deriva y regeneración de código, contratos de consumidor frente a un doble, un bucle de contraejemplos y un validador
  de trazabilidad con huellas;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con salidas idénticas salvo los tiempos, la versión de SQLite (3.45.3 y 3.45.1), las
  latencias de un servidor local y la huella de un paquete escrito con el modo de texto por defecto; los datos son sintéticos, los parámetros son supuestos del autor, las reglas
  léxicas se afinaron con pocos ejemplos y se probaron con seis casos nuevos, y no se usó ninguna herramienta de producción ni se auditó una API real; la parte no tiene laboratorio
  en `labs/`;
- hallazgos del análisis: el ejemplo más típico elimina solo la mitad de las dieciséis lecturas de una frase; tres ejemplos elegidos matan los nueve mutantes distinguibles que diez
  al azar no matan; cinco pruebas de ejemplo no detectan ninguno de nueve defectos que los contratos sí detectan; una expresión regular tarda 1,65 s con 25 caracteres; comprobar
  una deriva cada 20 commits la deja 13 commits; el mismo paquete tiene dos huellas distintas en Windows y Ubuntu si no se fija el salto de línea.


## 2026-11-13 — Parte 12 desarrollada y profundizada con experimentos sintéticos reproducibles

- las clases `SE-145`–`SE-156` pasan de borradores genéricos a clases completas sobre el requisito conductor de la plataforma de entregas de tareas (recuperar el borrador
  cuando la sesión expira): elicitación, análisis, especificación y validación, requisitos funcionales y reglas de negocio, atributos de calidad y restricciones, casos de
  uso, historias y job stories, criterios de aceptación y ejemplos, priorización con dependencias y negociación, trazabilidad, requisitos regulatorios, de datos y
  seguridad, gestión de cambios y líneas base, ambigüedad, contradicción e incompletitud, un taller de reparación y un proyecto de especificación revisable; el portal
  publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con cálculos y simulaciones de datos sintéticos y semilla fija: cobertura de elicitación y revisión con defectos desiguales, tabla de decisión con huecos,
  horas locales inexistentes y mutantes frente a suites, media frente a percentil, ventanas de disponibilidad y costo de PBKDF2, caminos de un caso de uso y corte
  vertical, mutantes y pruebas de pares, dependencias, inflación de Must y ciclos de mayoría, densidad de trazabilidad y trazas con `sys.settrace`, variantes de una regla
  de retención, STRIDE por elemento y cadena de hashes, alcance de cambios y hash normalizado, lecturas de frases con conectores y conflictos mínimos, la regla de tres, y
  un validador de especificaciones con 16 mutaciones y captura–recaptura;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y un puente
  hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con salidas idénticas salvo los tiempos de PBKDF2 de `SE-147` y las latencias de
  un servidor local de `SE-155`; los datos son sintéticos, los parámetros son supuestos del autor y las reglas léxicas se afinaron con pocos ejemplos: no hubo personas,
  organizaciones ni normas interpretadas, y la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: ocho entrevistas cubren 77,2 % de 40 requisitos sintéticos por el conocimiento tácito; cinco reglas razonables dejan 4 de 24 combinaciones con hueco
  o conflicto; la media cumple «menos de 2 s» mientras el percentil 99 no; los ejemplos felices detectan 0 de 10 mutantes y las fronteras los 10; los primeros k por
  valor/costo no son entregables; ningún par de doce requisitos se contradice y el conjunto sí; y un validador con 11 de 16 mutaciones detectadas deja pasar los defectos semánticos.
## 2026-11-13 — Parte 11 desarrollada y profundizada con experimentos de economía, métricas y decisiones

- las clases `SE-133`–`SE-144` pasan de borradores genéricos a clases completas sobre la economía de la plataforma de entregas de tareas: modelos de negocio y sostenibilidad,
  costos de construcción, operación y oportunidad, resultados frente a actividad, adopción y retención, telemetría y consentimiento, experimentos y causalidad, métrica norte
  con guardas, FinOps y costo por resultado, portafolio y opciones, decisiones reversibles, un taller de árbol de métricas y un proyecto de caso de viabilidad; el portal publica
  el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con cálculos y simulaciones de datos sintéticos y semilla fija: razón de valor de vida y costo de adquisición como intervalo, tres modelos de precio y concentración
  de ingresos, costo de propiedad y suma de medianas, tasa de descuento que invierte un ranking, meta de cerrados frente a resueltos, registros acumulados frente a activos,
  curva de retención por mezcla y cohortes incompletas, sesgo por consentimiento y unicidad por campos, once mutantes de una puerta de consentimiento, sesgo de selección, control
  de proporciones y regresión a la media, optimización con y sin guarda, alarmas con varias guardas, reparto de costos con tres reglas y compromiso de capacidad, arrepentimiento
  de una cartera, valor de un piloto, secuencias con dependencias, umbral de reversibilidad, seis migraciones en SQLite, despliegue progresivo, dos validadores con dieciséis
  mutaciones cada uno, descomposición exacta, oscilación del valor presente y compuerta de abandono;
- tres secciones nuevas por clase, preguntas frecuentes, tabla de errores, ejercicios y fallo controlado propios de cada una, un puente hacia el trabajo con agentes y fuentes
  primarias verificadas con `curl` (la página del Reglamento (UE) 2016/679 en EUR-Lex no respondió desde el entorno de ejecución y se sustituyó por las directrices del EDPB; dos
  páginas que devolvieron 403 se excluyeron);
- hallazgos del análisis: contar cohortes incompletas como no retenidas baja una retención de 34 % a 27 %; una tasa constante ajustada a cuatro semanas subestima 15 veces la
  retención a 26 semanas; tres pruebas del camino feliz matan 2 de 11 mutantes de una puerta de consentimiento y nueve pruebas dirigidas matan 10; una compuerta de abandono no
  elevó el valor esperado en ningún umbral y solo redujo el riesgo; solo 3 de 6 migraciones vuelven con todos sus datos;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (Python 3.12.3) con salidas idénticas, salvo la versión de SQLite (3.45.3 y 3.45.1); la parte no
  tiene laboratorio en `labs/`; todos los precios, costos, tasas y probabilidades son supuestos del autor en unidades ficticias y no se midió ninguna plataforma, empresa o persona.

## 2026-11-13 — Parte 09 profundizada con experimentos de bibliotecas, paquetes, SDK y automatización

- 36 figuras para `SE-109`–`SE-120` con mediciones reales: pila de llamadas de biblioteca y framework, costo de importar y timeout por defecto, versiones PEP 440
  frente a SemVer, cambios de firma y de contrato, un resolutor con retroceso, `pip` sobre ruedas locales y hashes, ruedas sin y con `package-data`, sombras en `sys.path` y
  etiquetas, códigos de salida, precedencia de configuración y tuberías, idempotencia, escritura atómica y actualización perdida, carga y aislamiento de plugins, generación
  determinista e inyección en plantillas, metadatos y expresiones de licencia y cobertura SPDX de este repositorio, tiempo hasta el primer éxito, errores y obsolescencia,
  siete defectos de empaquetado, doce mutantes de un SDK, archivo de referencia de la CLI y compilaciones reproducibles;
- tres secciones nuevas por clase, y sustitución de las preguntas frecuentes, la tabla de errores y los ejercicios, que eran idénticos en las doce clases, por versiones
  específicas de cada una; fuentes primarias verificadas con `curl` (dos páginas de gnu.org devolvieron 403 y se excluyeron) y un puente hacia el trabajo con agentes;
- hallazgos del análisis: el orden de `entry_points` difiere entre Windows y Linux con el mismo código; un bloqueo `O_EXCL` mató a un proceso en Windows con `PermissionError`;
  setuptools 84.0.0 incluye `py.typed` por sí solo y 68.1.2 no; la rueda sale distinta entre plataformas aun con `SOURCE_DATE_EPOCH`; este repositorio no tiene cabeceras SPDX
  en ninguno de 3 176 archivos revisados;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Linux (Python 3.12.3); la parte no tiene laboratorio en `labs/`; los tiempos son de un equipo y no se midieron
  otros constructores, gestores, intérpretes ni macOS.
## 2026-11-13 — Parte 10 desarrollada y profundizada con experimentos sintéticos reproducibles

- las clases `SE-121`–`SE-132` pasan de borradores genéricos a clases completas sobre una plataforma de entregas de tareas: síntomas frente a causas, actores y contextos,
  entrevistas y evidencia cualitativa, hipótesis, propuesta de valor, segmentos y mercado, experimentos, priorización, ética y protección de participantes, criterios de
  abandono, un taller y un proyecto integrador (brief respaldado por evidencia); el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con cálculos y simulaciones de datos sintéticos y semilla fija: conteo de frases frente a causas y dimensionamiento con rangos, usuario promedio y paradoja de
  Simpson, saturación de temas y kappa, sensibilidad de supuestos y comparaciones múltiples, estabilidad de rankings y de k-means frente a ruido, tamaño de muestra y
  falsos positivos al mirar varias veces, RICE bajo perturbación y coste del retraso, unicidad por cuasi-identificadores y reversión de un hash, reglas de abandono y zona
  gris, y un validador de briefs con doce mutaciones;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y un puente
  hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con salidas idénticas salvo los tiempos de hash de `SE-129`; los datos son
  sintéticos, los parámetros son supuestos del autor y las reglas léxicas se afinaron con pocos ejemplos y se probaron con casos nuevos mínimos: no hubo personas, usuarios
  ni mercados reales, y la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: la frase más repetida de 600 tickets no coincide con la causa más frecuente; con cinco atributos corrientes el 64,2 % de 500 participantes es único;
  un hash sin clave de siete dígitos se revierte en 16–20 s; mirar 10 veces una prueba A/A produce 21,1 % de falsos positivos; una regla léxica con 100 % de acierto en sus
  ejemplos acierta 50 % con preguntas nuevas.

## 2026-11-13 — Parte 08 profundizada con experimentos de herramientas y entornos

- 36 figuras para `SE-097`–`SE-108` con mediciones reales: un intercambio LSP con `ruff server`, una sesión de `pdb` y el costo de observar la ejecución, perfiladores
  por llamada, de memoria y por muestreo, la matriz de defectos de ruff y mypy, el estado oculto de un cuaderno, el arranque y la resolución de intérpretes,
  entornos virtuales, la instalación de una rueda local, reducción de casos y bisección, contraste WCAG y la reproducibilidad de una rueda;
- tres secciones nuevas por clase y sustitución de las preguntas frecuentes, la tabla de errores y los ejercicios por versiones específicas de cada clase; fuentes verificadas y un puente hacia agentes;
- con el motor de Docker en marcha se construyó una imagen mínima desde `scratch` (9 383 bytes, dos construcciones con identificadores distintos) y se creó un contenedor en 314 ms; no se arrancó ningún proceso en un contenedor y se declara como límite; los tiempos son de un equipo y se leen como razones.

## 2026-11-13 — Parte 05 profundizada con mediciones y mutaciones del laboratorio

- 36 figuras para `SE-061`–`SE-072` con datos reales: expresiones y tipos, tabla de verdad, recursión y memoria de iteradores, argumentos por defecto y cierres,
  jerarquía y costo de excepciones, colecciones, codificaciones y plataformas, `json`, grafo de importaciones, diez mutaciones de la suite del laboratorio,
  métricas con `ast`, un refactor protegido, semántica Python/Rust (Rust solo documentada) y catorce invocaciones de la CLI con sus códigos de salida;
- tres secciones nuevas por clase, y sustitución de las preguntas frecuentes, errores, ejercicios y fallos controlados genéricos por versiones propias de cada clase;
  fuentes primarias verificadas y un puente hacia el trabajo con agentes;
- hallazgos del análisis: seis de diez mutaciones sobreviven a la suite original, cinco se cierran con pruebas nuevas (verificadas en una copia) y la sexta es
  equivalente; los mensajes de error de la CLI incluyen la ruta absoluta del archivo;
- las quince pruebas del laboratorio se ejecutaron en Windows (Python 3.12.9) y Linux (3.12.3); `rustc` no estaba disponible y el puerto Rust no se compiló.

## 2026-11-13 — Parte 07 profundizada con experimentos de estructuras y algoritmos

- 36 figuras para `SE-085`–`SE-096` con mediciones y cuentas reales: capacidad de listas y `pop(0)` frente a `deque`, colas de prioridad y empates,
  colisiones de hash y claves mutadas, altura de árboles (BST, AVL, trie y `bisect`), BFS frente a DFS y representaciones de grafos, comparaciones por
  algoritmo de ordenamiento, monedas, intervalos y mochila, n reinas y poda, índices de SQLite, filtros de Bloom y Count-Min, pendientes log-log y
  ruido de medición, matrices de compromisos por carga y mutantes frente a un oráculo diferencial;
- tres secciones nuevas por clase, y sustitución de las preguntas frecuentes, la tabla de errores y los ejercicios, que eran idénticos en las doce clases,
  por versiones específicas de cada una; fuentes primarias verificadas (enlaces con `curl`, DOI con Crossref) y un puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Linux (Python 3.12.3); la parte no tiene laboratorio en `labs/`; los tiempos son de un
  equipo y varían entre pasadas (una pendiente dio 1,21 y luego 1,02), y no se midieron otros intérpretes ni cargas reales.

## 2026-11-13 — Parte 06 profundizada con experimentos de paradigmas ejecutados

- 36 figuras para `SE-073`–`SE-084` con mediciones reales: aliasing y costo de copiar, costo de llamar funciones y límite de
  recursión, memoria con `__slots__`, resolución de herencia, formas de filtrar, planes de consulta de SQLite, conflictos entre reglas,
  costo del orden de las metas y unificación, orden y bloqueo del bucle de `asyncio`, contrapresión, condición de carrera, hilos frente a
  procesos y buzones, y una misma regla en cinco paradigmas con contrato común, superficie de cambio y mutantes;
- tres secciones nuevas por clase, y sustitución de las preguntas frecuentes, la tabla de errores y los ejercicios, que eran idénticos en las
  doce clases, por versiones específicas de cada una; fuentes primarias verificadas (los DOI de ACM bloquean `curl` y se marcan como no verificados) y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Linux (Python 3.12.3); la parte no tiene laboratorio en `labs/`; no se ejecutaron Prolog,
  Erlang, Rust ni bibliotecas reactivas, y se declara como límite.

## 2026-11-13 — Parte 04 profundizada con cálculos y mediciones reales

- 36 figuras para `SE-049`–`SE-060`: descomposición del incidente, implicación y modelos, orden topológico y ciclos, aserciones y contratos,
  recursión y memoización, terminación (Euclides y Collatz), crecimiento al duplicar n, heurísticas frente al óptimo, máquina de estados de un pedido,
  bisección y pruebas intermitentes, requisitos contradictorios y las trece pruebas del laboratorio;
- tres secciones nuevas por clase y sustitución de las preguntas frecuentes, errores y ejercicios idénticos por versiones propias de cada clase; fuentes verificadas y puente hacia agentes;
- las trece pruebas del laboratorio pasaron en Windows (Python 3.12.9) y en Linux (Python 3.12.3); los tiempos son de un equipo y se declaran como límite.

## 2026-11-13 — Parte 03 profundizada con mediciones de red reales

- 36 figuras para `SE-037`–`SE-048` con mediciones reales: fases de una petición HTTPS, MTU y límite de 1472 bytes,
  aritmética y clasificación de direcciones, estados TCP, rechazo frente a silencio y la espera de Nagle, resolución DNS y TTL,
  cabeceras y estados HTTP, certificado y veredictos TLS con una CA de laboratorio, proxy y balanceo simulados, contrapresión, variación
  por fase, la suite del laboratorio y el reintento con retroceso y jitter;
- tres secciones nuevas por clase, y sustitución de las preguntas frecuentes, la tabla de errores y los ejercicios, que eran idénticos en las doce clases, por
  versiones específicas de cada una; fuentes primarias verificadas y un puente hacia el trabajo con agentes;
- las once pruebas del laboratorio se ejecutaron en Windows (Python 3.12.9) y en Linux (Python 3.12.3); no se capturaron paquetes ni se midió
  Wi-Fi, QUIC o HTTP/3, y se declara como límite.

## 2026-11-13 — Parte 02 profundizada con evidencia medida en Windows y Linux

- 36 figuras para `SE-025`–`SE-036` con datos reales de Windows 11 y Ubuntu 24.04 bajo WSL2: sistemas de
  archivos (NTFS, ext4 y 9p) y su costo de metadatos, efecto de `chmod`, códigos de salida de procesos, expansión
  de argumentos y pipelines en Bash y PowerShell 5.1, visibilidad de un secreto ficticio, propiedad de archivos en
  `dpkg`, registros, espacios de nombres con `unshare` y la secuencia del laboratorio;
- tres a cuatro secciones nuevas por clase, fallos controlados ampliados, preguntas frecuentes, puentes hacia el
  trabajo con agentes y fuentes verificadas;
- las diez pruebas del laboratorio se ejecutaron en Windows (Python 3.12.9) y en Linux (Python 3.12.3);
  macOS, PowerShell 7 y los contenedores de Docker no se ejecutaron y se declaran como documentados;
- las pruebas de figuras cubren las Partes 00 a 02.

## 2026-11-13 — Parte 01 profundizada en contenido y figuras

- 40 figuras SVG para `SE-013`–`SE-024` (de tres a cuatro por clase), varias con datos medidos
  en CPython 3.12.9 sobre Windows y declarados como tales: tiempo de pared frente a CPU,
  recorrido secuencial frente a barajado, memoria de una lista frente a un `array`, costo de
  `fsync`, hilos frente a procesos, compilar frente a cargar bytecode y retención frente a flujo;
- cada clase añade entre tres y cuatro secciones de contenido nuevo con mecanismo, ejemplos
  ejecutados y límites (complemento a dos, aritmética de números de secuencia, UTF-8 por dentro,
  absorción y cancelación en coma flotante, simulador de ISA con 22 instrucciones dinámicas,
  jerarquía y durabilidad, GIL y carreras de datos, etapas de compilación y `.pyc`, conteo de
  referencias y ciclos, protocolo de benchmark, percentiles, Amdahl, dossier de referencia y
  estudio de ejemplo con regla de decisión previa);
- fallos controlados ampliados, preguntas frecuentes, puentes hacia el trabajo con agentes y
  fuentes primarias verificadas (DOI comprobados con Crossref, enlaces con respuesta 200);
- el generador de figuras pasa a `scripts/build_figures.py`, que descubre los módulos
  `scripts/figures_partXX_*.py`; las pruebas de figuras cubren las Partes 00 y 01.

## 2026-11-13 — Parte 00 profundizada con figuras de apoyo

- 36 figuras SVG estáticas (tres por clase) para `SE-001`–`SE-012`: modelos del
  mecanismo, secuencias de fallo, comparaciones y gráficos con datos sintéticos
  declarados, cada una con título, descripción, texto alternativo y un párrafo que
  explica cómo leerla y dónde deja de valer;
- cada clase añade un fallo controlado con protocolo, preguntas frecuentes sobre
  ambigüedades reales, un puente hacia el trabajo con agentes y fuentes primarias
  nuevas verificadas;
- el portal publica las figuras sin JavaScript externo (`site/assets/figures/`) y el
  README de GitHub las enlaza por ruta relativa; el generador de figuras vive en
  `scripts/build_figures.py` y se comprueba con `--check`;
- nuevo documento `docs/METHODOLOGY-GAP-AUDIT-2026-11-13.md` con la auditoría de
  brechas (metodologías de la era de la IA, patrones y arquitecturas) y el alcance
  decidido de 540 clases; el alcance no se publica en `curriculum.yaml` hasta que cada
  parte tenga contenido desarrollado.

## 2026-10-06 — Parte 05 desarrollada

- revisión clase a clase de `SE-061`–`SE-072`, conservando el hilo desde tipos y
  control hasta módulos, pruebas, mantenimiento y entrega;
- laboratorio empaquetado con quince contratos para parsing estricto, estado
  inmutable, JSONL acotado, errores explícitos, streams y códigos de salida;
- puerto Rust compilado en CI contra fixtures compartidas, con alcance de equivalencia
  deliberadamente limitado y documentado;
- actividades, rúbricas, portal y métricas reconciliados a 72 clases desarrolladas,
  288 borradores y 120 estructuras curriculares.

## 2026-10-06 — Parte 04 desarrollada

- revisión clase a clase de `SE-049`–`SE-060`, preservando la progresión desde
  ambigüedad hasta especificación, algoritmo, oráculo y contraejemplos;
- laboratorio ejecutable con trece pruebas para lógica, grafos, contratos,
  terminación, complejidad, heurísticas, estados y requisitos contradictorios;
- actividades, rúbricas, portal y métricas reconciliados a 60 clases desarrolladas,
  300 borradores y 120 estructuras curriculares.

## 2026-10-06 — Parte 03 desarrollada

- revisión cualitativa clase a clase de `SE-037`–`SE-048`, con DNSSEC, caché
  negativa, confianza de cabeceras y Trace Context vinculados a fuentes primarias;
- laboratorio local de petición observable con siete escenarios, once pruebas,
  resultados tipados, correlación, redacción y limpieza determinista;
- actividades y rúbricas específicas, portal íntegro, índices y estado reconciliados
  a 48 clases desarrolladas, 312 borradores y 120 estructuras curriculares.

## Unreleased — fase 3

### Parte 02 — sistemas operativos, terminal y automatización base

- revisión cualitativa y publicación como desarrolladas de `SE-025`–`SE-036`, con
  actividades, rúbricas, fallos y evidencia específica para cada competencia;
- laboratorio seguro sin dependencias externas para preparar, inspeccionar, reparar
  y limpiar un entorno controlado, con diez pruebas y adaptadores PowerShell/Bash;
- fuentes primarias reconsultadas para POSIX.1-2024, GNU Bash 5.3, PowerShell y WSL,
  sin copiar estándares protegidos ni atribuir capacidades no ejecutadas;
- CI ampliada con pruebas del laboratorio, smoke tests nativos y matriz
  Windows/macOS/Linux; estado reconciliado a 36 clases desarrolladas, 324 borradores
  y 120 estructuras curriculares.

### Parte 01 — computadores y representación de información

- revisión cualitativa y publicación como desarrolladas de `SE-013`–`SE-024`, con
  secuencias, actividades y rúbricas específicas para cada competencia;
- laboratorio reproducible sin dependencias externas para inspección de
  representación, Unicode, números, AST, bytecode, memoria y medición de tiempo;
- actualización no retroactiva de las referencias vigentes a Unicode 18.0 y Java
  Virtual Machine Specification SE 27;
- CI ampliada con las seis pruebas del laboratorio en estructura y portabilidad;
- nueva auditoría de cobertura y backlog trazable: 24 clases desarrolladas, 336
  borradores y 120 estructuras, sin crear IDs nuevos antes de demostrar una brecha
  indivisible.

### Licencias y automatización

- transición no retroactiva desde MIT a una matriz explícita: Apache-2.0 para
  software propio y CC BY-NC-SA 4.0 para contenido educativo, datos y activos
  originales;
- incorporación de `NOTICE`, auditoría, historia verificable, marcas e inventarios
  de terceros, datos y activos, con un validador y pruebas dedicados;
- workflow de seguridad con Gitleaks, Bandit y gobernanza semanal; CI ampliada con
  lint Markdown, resumen de evidencia y contratos de licencia;
- Pages cubre todas sus fuentes de generación y configura el despliegue mediante una
  acción fijada a SHA; la arquitectura y los límites de los tres workflows quedan
  documentados en profundidad;

### README y rutas profesionales

- rediseño integral del README principal siguiendo el ritmo visual y documental del
  programa de ciberseguridad: identidad, fuentes, mapa completo, uso, rutas, calidad,
  límites, licencia y llamada final a apoyar el repositorio;
- cabecera y cierre centrados, badges jerarquizados, accesos visuales, comparación en
  dos columnas y badges sociales reales de stars, forks y seguimiento;
- 40 guías profesionales propias, derivadas de las capacidades reales de las partes,
  con misión, jornada, responsabilidades, límites, conocimientos, recorrido,
  evidencia de portafolio, progresión, mitos y siguientes pasos;
- índice por familias y mapa de transiciones para distinguir especialización técnica,
  producto, calidad, plataforma, gobierno, arquitectura, liderazgo e IA;
- validación automática del inventario, la estructura y la navegación de las rutas.
- profundización de las 40 guías a más de 2.200 palabras cada una, con dos gráficos
  Mermaid, mapas parte → clases asociadas → evidencia, decisiones, escenarios de
  fallo, métricas, proyectos integradores, planes 30/60/90 y fuentes oficiales;
- mapa profesional ampliado en el README principal y en `roles/README.md`, con enlaces
  directos a 480 asociaciones de clase, tarjetas verticales adaptables y generación
  reproducible de los bloques;

### Roadmap curricular y simplificación editorial

- retiro de `PROMPT_MAESTRO.md`: la definición pública del programa vive ahora en un
  roadmap curricular detallado y las reglas de agentes permanecen en `AGENTS.md`;
- eliminación de etiquetas de flujo o madurez por clase en manifiestos, esquemas,
  generadores, portal, actividades, auditorías pedagógicas e índices;
- roadmap de las 40 partes con contenidos, artefactos y comprobaciones concretas,
  además de progresión, ejes transversales, proyectos y fases de implementación;
- auditoría de cobertura fechada con matriz de estado, profundidad, brechas y acción;
- ADR que preserva `SE-001`–`SE-480` y condiciona la aproximación a 500 clases a
  competencias no cubiertas, sin renumeración ni relleno;
- guardrails automáticos para impedir que misión, auditoría y decisión arquitectónica
  desaparezcan o se desincronicen silenciosamente.

### Corrección de integridad pedagógica

- fase 3 reabierta con alcance correcto de 180 clases (`SE-001`–`SE-180`);
- retiro de la afirmación incorrecta de 156 clases desarrolladas;
- incorporación del estándar pedagógico permanente y gate cualitativo;
- publicación del contenido completo de cada borrador en lugar de fichas resumidas;
- descripción factual del contenido disponible, sin asignar estados a cada clase.

### Fase 3 — declaración anterior, sustituida por la corrección

- 156 clases de las etapas A y C declaradas desarrolladas sin evidencia suficiente;
- guías específicas con conceptos, ejemplos, prácticas, ejercicios y fallos controlados;
- 156 contratos de actividad y 156 rúbricas machine-readable;
- catálogo de fuentes primarias u oficiales verificadas para trece partes;
- portal con páginas enlazadas al material completo;
- validador de fase 3 y quince pruebas estructurales.

### Fase 2 — generadores y controles

- scaffolding no destructivo para 480 clases y 40 partes;
- metadatos e índices generados desde `curriculum.yaml`;
- registro bibliográfico inicial para cada clase;
- validadores dedicados de contrato pedagógico y UTF-8;
- sitio estático de 521 páginas con búsqueda y filtros;
- workflow de GitHub Pages con acciones fijadas a SHA;
- diez pruebas estructurales y comprobación multiplataforma.

### Fase 1 — especificación y arquitectura

- arquitectura de ocho etapas, 40 partes y 480 clases planificadas;
- manifiesto y catálogo generados con 2.160 horas estimadas;
- mapa de cobertura, fronteras, ADR y plan de publicación pública;
- línea base de fuentes oficiales y primarias;
- validación estricta, pruebas estructurales y CI multiplataforma fijado por SHA;
- repositorio público con metadatos coherentes y workflow verde.

## 0.1.0 — 2026-08-19

- suite integradora inicial;
- programa profesional de 260 horas;
- documento de instrucciones interno, retirado posteriormente al consolidar el roadmap;
- manifiesto de cuatro repositorios;
- mapa de competencias, proyectos y blueprint;
- portal local y validación automática;
- plantillas de ingeniería y rúbrica final.
