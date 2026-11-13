# Changelog

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
