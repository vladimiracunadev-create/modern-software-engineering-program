# Changelog

## Unreleased — fase 3

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
