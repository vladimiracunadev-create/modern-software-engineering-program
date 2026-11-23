# Mapa de migración de identificadores (ADR-007)

Este mapa se generó con `scripts/migrate_renumber.py emit-map` y vive también en
[`ID-MIGRATION.json`](ID-MIGRATION.json), que es la fuente que leen las páginas
de redirección del portal. La decisión y sus razones están en
[ADR-007](adr/ADR-007-pedagogical-renumbering-and-new-parts.md).

## Cómo usarlo

- Una referencia anterior al 2026-11-23 (`SE-nnn` o «Parte NN») usa la numeración histórica
  por orden de aparición. Busca la parte en la primera tabla; el ID nuevo de una clase es
  `ID nuevo = 12 × parte nueva + posición dentro de la parte` (la posición no cambia).
- Las Partes 00–22 conservan número y clases. Cambian las Partes antiguas 23–48.
- Las Partes 34 y 42 son huecos reservados: aún no tienen clases (`SE-409`–`SE-420`
  y `SE-505`–`SE-516`). Los IDs que antes ocupaban esos números se movieron a otras partes.
- La etiqueta Git `pre-reorder-2026-11-23` conserva el árbol anterior completo, con la numeración histórica.
- Una URL antigua `classes/SE-nnn.html` ya no corresponde a la misma clase cuando el número
  cambió: el portal ofrece `site/legacy/` con una página por cada ID y parte antiguos que
  enlaza su destino actual. Las direcciones vacantes (partes 34 y 42) muestran `404.html`,
  que explica el cambio.

## Partes

| Parte nueva | Parte antigua | Título | Clases nuevas | Clases antiguas | Estado |
| ---: | ---: | --- | --- | --- | --- |
| 00 | 00 | Ingeniería de software como profesión | SE-001–SE-012 | SE-001–SE-012 | desarrollada, sin cambios |
| 01 | 01 | Computadores y representación de información | SE-013–SE-024 | SE-013–SE-024 | desarrollada, sin cambios |
| 02 | 02 | Sistemas operativos, terminal y automatización base | SE-025–SE-036 | SE-025–SE-036 | desarrollada, sin cambios |
| 03 | 03 | Redes, Internet y protocolos | SE-037–SE-048 | SE-037–SE-048 | desarrollada, sin cambios |
| 04 | 04 | Pensamiento computacional y resolución de problemas | SE-049–SE-060 | SE-049–SE-060 | desarrollada, sin cambios |
| 05 | 05 | Fundamentos de programación | SE-061–SE-072 | SE-061–SE-072 | desarrollada, sin cambios |
| 06 | 06 | Paradigmas de programación | SE-073–SE-084 | SE-073–SE-084 | desarrollada, sin cambios |
| 07 | 07 | Estructuras de datos y algoritmos | SE-085–SE-096 | SE-085–SE-096 | desarrollada, sin cambios |
| 08 | 08 | Entornos, herramientas y depuración | SE-097–SE-108 | SE-097–SE-108 | desarrollada, sin cambios |
| 09 | 09 | Bibliotecas, paquetes, SDK y automatización | SE-109–SE-120 | SE-109–SE-120 | desarrollada, sin cambios |
| 10 | 10 | Descubrimiento y estrategia de producto | SE-121–SE-132 | SE-121–SE-132 | desarrollada, sin cambios |
| 11 | 11 | Economía, métricas y decisiones de producto | SE-133–SE-144 | SE-133–SE-144 | desarrollada, sin cambios |
| 12 | 12 | Ingeniería de requisitos | SE-145–SE-156 | SE-145–SE-156 | desarrollada, sin cambios |
| 13 | 13 | Especificaciones, contratos y modelos | SE-157–SE-168 | SE-157–SE-168 | desarrollada, sin cambios |
| 14 | 14 | Experiencia, accesibilidad e internacionalización | SE-169–SE-180 | SE-169–SE-180 | desarrollada, sin cambios |
| 15 | 15 | Procesos, planificación y estimación | SE-181–SE-192 | SE-181–SE-192 | desarrollada, sin cambios |
| 16 | 16 | Git, colaboración y código abierto | SE-193–SE-204 | SE-193–SE-204 | desarrollada, sin cambios |
| 17 | 17 | Documentación y conocimiento técnico | SE-205–SE-216 | SE-205–SE-216 | desarrollada, sin cambios |
| 18 | 18 | CLI, TUI, servicios y automatización | SE-217–SE-228 | SE-217–SE-228 | desarrollada, sin cambios |
| 19 | 19 | Web, frontend y aplicaciones progresivas | SE-229–SE-240 | SE-229–SE-240 | desarrollada, sin cambios |
| 20 | 20 | Backend, APIs y procesamiento asíncrono | SE-241–SE-252 | SE-241–SE-252 | desarrollada, sin cambios |
| 21 | 21 | Software móvil, escritorio y multiplataforma | SE-253–SE-264 | SE-253–SE-264 | desarrollada, sin cambios |
| 22 | 22 | Embedded, IoT y tiempo real | SE-265–SE-276 | SE-265–SE-276 | desarrollada, sin cambios |
| 23 | 48 | Runtimes y plataformas modernas | SE-277–SE-288 | SE-577–SE-588 | desarrollada, renumerada |
| 24 | 23 | Software especializado y dominios | SE-289–SE-300 | SE-277–SE-288 | desarrollada, renumerada |
| 25 | 24 | Diseño, patrones y refactorización | SE-301–SE-312 | SE-289–SE-300 | desarrollada, renumerada |
| 26 | 43 | Patrones de diseño, empresariales y de resiliencia | SE-313–SE-324 | SE-517–SE-528 | desarrollada, renumerada |
| 27 | 25 | Arquitectura de software y dominio | SE-325–SE-336 | SE-301–SE-312 | desarrollada, renumerada |
| 28 | 44 | Estilos arquitectónicos | SE-337–SE-348 | SE-529–SE-540 | desarrollada, renumerada |
| 29 | 26 | Datos, persistencia y recuperación | SE-349–SE-360 | SE-313–SE-324 | desarrollada, renumerada |
| 30 | 45 | Ingeniería de datos y plataformas de datos | SE-361–SE-372 | SE-541–SE-552 | desarrollada, renumerada |
| 31 | 27 | Integración, eventos y mensajería | SE-373–SE-384 | SE-325–SE-336 | desarrollada, renumerada |
| 32 | 28 | Concurrencia y sistemas distribuidos | SE-385–SE-396 | SE-337–SE-348 | desarrollada, renumerada |
| 33 | 29 | Cloud, plataforma e infraestructura | SE-397–SE-408 | SE-349–SE-360 | desarrollada, renumerada |
| 34 | — | SaaS y plataformas de producto | SE-409–SE-420 | — | reservada, planificada |
| 35 | 30 | Estrategia y técnicas de prueba | SE-421–SE-432 | SE-361–SE-372 | desarrollada, renumerada |
| 36 | 31 | Calidad, rendimiento y resiliencia | SE-433–SE-444 | SE-373–SE-384 | desarrollada, renumerada |
| 37 | 47 | Sistemas críticos, tiempo real y normas de seguridad | SE-445–SE-456 | SE-565–SE-576 | desarrollada, renumerada |
| 38 | 32 | Seguridad, privacidad y cumplimiento | SE-457–SE-468 | SE-385–SE-396 | desarrollada, renumerada |
| 39 | 33 | Build, release y cadena de suministro | SE-469–SE-480 | SE-397–SE-408 | desarrollada, renumerada |
| 40 | 34 | CI/CD, IaC y platform engineering | SE-481–SE-492 | SE-409–SE-420 | desarrollada, renumerada |
| 41 | 35 | Observabilidad, SRE e incidentes | SE-493–SE-504 | SE-421–SE-432 | desarrollada, renumerada |
| 42 | — | Ingeniería del caos | SE-505–SE-516 | — | reservada, planificada |
| 43 | 36 | Mantenimiento y modernización legacy | SE-517–SE-528 | SE-433–SE-444 | desarrollada, renumerada |
| 44 | 37 | Gestión, liderazgo y práctica profesional | SE-529–SE-540 | SE-445–SE-456 | desarrollada, renumerada |
| 45 | 40 | Metodologías de desarrollo: de TDD a ODD | SE-541–SE-552 | SE-481–SE-492 | desarrollada, renumerada |
| 46 | 38 | Desarrollo de software asistido por IA | SE-553–SE-564 | SE-457–SE-468 | desarrollada, renumerada |
| 47 | 39 | SPEC, agentes y ciclo de vida agentic | SE-565–SE-576 | SE-469–SE-480 | desarrollada, renumerada |
| 48 | 41 | Harness y agentic engineering | SE-577–SE-588 | SE-493–SE-504 | desarrollada, renumerada |
| 49 | 42 | Patrones agénticos y sistemas con LLM | SE-589–SE-600 | SE-505–SE-516 | desarrollada, renumerada |
| 50 | 46 | Machine learning en producción y MLOps | SE-601–SE-612 | SE-553–SE-564 | desarrollada, renumerada |

## Clases que cambian de ID

Las clases se mueven por partes completas de doce (diez clases, un taller y un proyecto) y
conservan su posición. La tabla por clase está en [`ID-MIGRATION.json`](ID-MIGRATION.json)
(`classes[]`: `old`, `new`, `old_path`, `new_path`, `old_url`, `new_url`); aquí van los rangos.

| Rango antiguo | Rango nuevo | Parte nueva |
| --- | --- | --- |
| SE-577–SE-588 | SE-277–SE-288 | 23 · Runtimes y plataformas modernas |
| SE-277–SE-288 | SE-289–SE-300 | 24 · Software especializado y dominios |
| SE-289–SE-300 | SE-301–SE-312 | 25 · Diseño, patrones y refactorización |
| SE-517–SE-528 | SE-313–SE-324 | 26 · Patrones de diseño, empresariales y de resiliencia |
| SE-301–SE-312 | SE-325–SE-336 | 27 · Arquitectura de software y dominio |
| SE-529–SE-540 | SE-337–SE-348 | 28 · Estilos arquitectónicos |
| SE-313–SE-324 | SE-349–SE-360 | 29 · Datos, persistencia y recuperación |
| SE-541–SE-552 | SE-361–SE-372 | 30 · Ingeniería de datos y plataformas de datos |
| SE-325–SE-336 | SE-373–SE-384 | 31 · Integración, eventos y mensajería |
| SE-337–SE-348 | SE-385–SE-396 | 32 · Concurrencia y sistemas distribuidos |
| SE-349–SE-360 | SE-397–SE-408 | 33 · Cloud, plataforma e infraestructura |
| SE-361–SE-372 | SE-421–SE-432 | 35 · Estrategia y técnicas de prueba |
| SE-373–SE-384 | SE-433–SE-444 | 36 · Calidad, rendimiento y resiliencia |
| SE-565–SE-576 | SE-445–SE-456 | 37 · Sistemas críticos, tiempo real y normas de seguridad |
| SE-385–SE-396 | SE-457–SE-468 | 38 · Seguridad, privacidad y cumplimiento |
| SE-397–SE-408 | SE-469–SE-480 | 39 · Build, release y cadena de suministro |
| SE-409–SE-420 | SE-481–SE-492 | 40 · CI/CD, IaC y platform engineering |
| SE-421–SE-432 | SE-493–SE-504 | 41 · Observabilidad, SRE e incidentes |
| SE-433–SE-444 | SE-517–SE-528 | 43 · Mantenimiento y modernización legacy |
| SE-445–SE-456 | SE-529–SE-540 | 44 · Gestión, liderazgo y práctica profesional |
| SE-481–SE-492 | SE-541–SE-552 | 45 · Metodologías de desarrollo: de TDD a ODD |
| SE-457–SE-468 | SE-553–SE-564 | 46 · Desarrollo de software asistido por IA |
| SE-469–SE-480 | SE-565–SE-576 | 47 · SPEC, agentes y ciclo de vida agentic |
| SE-493–SE-504 | SE-577–SE-588 | 48 · Harness y agentic engineering |
| SE-505–SE-516 | SE-589–SE-600 | 49 · Patrones agénticos y sistemas con LLM |
| SE-553–SE-564 | SE-601–SE-612 | 50 · Machine learning en producción y MLOps |

## Rutas, figuras y archivos

| Elemento | Regla |
| --- | --- |
| Carpeta de contenido | `content/part-AA/` pasa a `content/part-NN/` |
| Clase fuente | `content/part-AA/SE-aaa.md` pasa a `content/part-NN/SE-nnn.md` |
| Figuras | `content/part-AA/figures/se-aaa-<nombre>.svg` pasa a `content/part-NN/figures/se-nnn-<nombre>.svg` |
| Clase generada | `classes/part-AA-<parte>/se-aaa-<clase>/` pasa a `classes/part-NN-<parte>/se-nnn-<clase>/` |
| Portal | `site/classes/SE-aaa.html` y `site/parts/AA.html` pasan a los números nuevos |
| Guiones | `scripts/figures_partAA_*.py` y `scripts/experiments_partAA_*.py` pasan a `partNN` |
| Documentos históricos | ADR-002 a ADR-006, CHANGELOG, tracker y auditorías fechadas conservan los IDs antiguos; sus enlaces apuntan a la clase migrada |
