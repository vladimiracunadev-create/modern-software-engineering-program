# ADR-007 — Secuencia pedagógica: renumeración y dos partes nuevas

- Estado: aceptada el 2026-11-23.
- Sustituye, para la numeración, a [ADR-003](ADR-003-reconcile-480-baseline-with-progressive-expansion.md)
  («no se renumera») y al principio «al final, sin renumerar nada» de
  [ADR-006](ADR-006-extend-program-parts-45-48-and-roles.md). Los demás acuerdos de ADR-004 y
  ADR-006 (alcance de contenido, contrato de clase, roles) siguen vigentes.
- Contexto: el programa creció por orden de aparición. Las Partes 40–48 se añadieron al final
  porque [ADR-003](ADR-003-reconcile-480-baseline-with-progressive-expansion.md) prohibía
  renumerar, de modo que la numeración quedó en conflicto con la secuencia de estudio: los
  patrones de diseño (antigua 43) y los estilos arquitectónicos (antigua 44) venían después de
  la operación y la gestión; datos (antigua 45), sistemas críticos (antigua 47) y runtimes
  (antigua 48) se leían después de las partes de inteligencia artificial, de las que no
  dependen; y las metodologías de desarrollo (antigua 40) se intercalaban entre las de
  agentes (antiguas 39 y 41). Quien seguía el índice en orden numérico estudiaba concurrencia
  antes de patrones y ML en producción antes de la ingeniería de datos. Además faltaban dos
  disciplinas que las guías de rol ya mencionaban sin parte propia: el producto SaaS
  multi-tenant y la ingeniería del caos.
- Decisión:
  1. **Secuencia pedagógica.** Las partes se ordenan por dependencia de estudio, con la
     inteligencia artificial al final: fundamentos (etapa A, 00–04), programación (B, 05–09),
     producto y especificación (C, 10–17), superficies y formas de software (D, 18–24),
     diseño, arquitectura, datos e integración (E, 25–34), calidad, seguridad y entrega
     (F, 35–40), operación y liderazgo (G, 41–44) e ingeniería con IA (H, 45–50). Las
     **Partes 00–22 conservan número, clases e IDs**.
  2. **Dos partes nuevas reservadas.** La Parte 34, *SaaS y plataformas de producto*
     (`SE-409`–`SE-420`, etapa E), y la Parte 42, *Ingeniería del caos* (`SE-505`–`SE-516`,
     etapa G). Nacen **planificadas**: no tienen carpeta en `classes/`, página en `site/`
     ni enlaces en las guías de rol hasta que exista su contenido completo. Los títulos de
     sus doce clases están fijados en `scripts/build_program_blueprint.py` y solo cambian
     con un ADR. Mientras no existan son **huecos**: la navegación anterior/siguiente salta
     de la última clase desarrollada de la parte anterior a la primera de la siguiente.
  3. **Dos roles nuevos, decididos pero no creados todavía.** *SaaS & Product Platform
     Engineer* y *Chaos Engineer* se crean cuando sus partes se desarrollen, con el esquema,
     la longitud y los gráficos de las demás guías. Hasta entonces las partes reservadas
     figuran como contexto planificado (`PLANNED_BY_ROLE` en `scripts/role_profiles.py`) de
     las guías existentes a las que servirán, y el programa mantiene 45 roles.
  4. **Alcance resultante.** 51 partes, 612 posiciones (`SE-001`–`SE-612`) y 2.754 horas
     planificadas; hoy hay 588 clases desarrolladas en 49 partes y 24 posiciones planificadas
     en dos partes. La regla de ID es `ID nuevo = 12 × parte nueva + posición dentro de la
     parte`; la posición no cambia (diez clases, un taller y un proyecto).
  5. **Núcleo de roles.** Cada parte desarrollada queda como núcleo de al menos un rol. La
     Parte 06 (Paradigmas de programación), que ningún rol apuntaba, pasa a ser núcleo de
     Software Engineer, Systems Programmer, Domain & Methodology Engineer y Frontend
     Engineer, que deciden con ella (modelo de estado y concurrencia, semánticas
     alternativas, reglas y eventos).
  6. **Alcance de las fases 3 y 4 por parte.** Los contratos de actividad y rúbrica
     (`activity.yaml`, `rubric.json`) cubren 360 clases: las Partes 00–14 (fase 3) y las
     antiguas 15–29, hoy 15–22, 24–25, 27, 29 y 31–33 (fase 4). Se declaran por parte en
     `scripts/program_state.py` (`PHASE3_PARTS`, `PHASE4_PARTS`) en lugar de por rango de
     `SE-nnn`, porque ese rango ya no es contiguo.
- Mapa de partes (antiguo → nuevo):

  | Parte nueva | Parte antigua | Título | Clases nuevas | Clases antiguas |
  | ---: | ---: | --- | --- | --- |
  | 00 | 00 | Ingeniería de software como profesión | `SE-001`–`SE-012` | `SE-001`–`SE-012` |
  | 01 | 01 | Computadores y representación de información | `SE-013`–`SE-024` | `SE-013`–`SE-024` |
  | 02 | 02 | Sistemas operativos, terminal y automatización base | `SE-025`–`SE-036` | `SE-025`–`SE-036` |
  | 03 | 03 | Redes, Internet y protocolos | `SE-037`–`SE-048` | `SE-037`–`SE-048` |
  | 04 | 04 | Pensamiento computacional y resolución de problemas | `SE-049`–`SE-060` | `SE-049`–`SE-060` |
  | 05 | 05 | Fundamentos de programación | `SE-061`–`SE-072` | `SE-061`–`SE-072` |
  | 06 | 06 | Paradigmas de programación | `SE-073`–`SE-084` | `SE-073`–`SE-084` |
  | 07 | 07 | Estructuras de datos y algoritmos | `SE-085`–`SE-096` | `SE-085`–`SE-096` |
  | 08 | 08 | Entornos, herramientas y depuración | `SE-097`–`SE-108` | `SE-097`–`SE-108` |
  | 09 | 09 | Bibliotecas, paquetes, SDK y automatización | `SE-109`–`SE-120` | `SE-109`–`SE-120` |
  | 10 | 10 | Descubrimiento y estrategia de producto | `SE-121`–`SE-132` | `SE-121`–`SE-132` |
  | 11 | 11 | Economía, métricas y decisiones de producto | `SE-133`–`SE-144` | `SE-133`–`SE-144` |
  | 12 | 12 | Ingeniería de requisitos | `SE-145`–`SE-156` | `SE-145`–`SE-156` |
  | 13 | 13 | Especificaciones, contratos y modelos | `SE-157`–`SE-168` | `SE-157`–`SE-168` |
  | 14 | 14 | Experiencia, accesibilidad e internacionalización | `SE-169`–`SE-180` | `SE-169`–`SE-180` |
  | 15 | 15 | Procesos, planificación y estimación | `SE-181`–`SE-192` | `SE-181`–`SE-192` |
  | 16 | 16 | Git, colaboración y código abierto | `SE-193`–`SE-204` | `SE-193`–`SE-204` |
  | 17 | 17 | Documentación y conocimiento técnico | `SE-205`–`SE-216` | `SE-205`–`SE-216` |
  | 18 | 18 | CLI, TUI, servicios y automatización | `SE-217`–`SE-228` | `SE-217`–`SE-228` |
  | 19 | 19 | Web, frontend y aplicaciones progresivas | `SE-229`–`SE-240` | `SE-229`–`SE-240` |
  | 20 | 20 | Backend, APIs y procesamiento asíncrono | `SE-241`–`SE-252` | `SE-241`–`SE-252` |
  | 21 | 21 | Software móvil, escritorio y multiplataforma | `SE-253`–`SE-264` | `SE-253`–`SE-264` |
  | 22 | 22 | Embedded, IoT y tiempo real | `SE-265`–`SE-276` | `SE-265`–`SE-276` |
  | 23 | 48 | Runtimes y plataformas modernas | `SE-277`–`SE-288` | `SE-577`–`SE-588` |
  | 24 | 23 | Software especializado y dominios | `SE-289`–`SE-300` | `SE-277`–`SE-288` |
  | 25 | 24 | Diseño, patrones y refactorización | `SE-301`–`SE-312` | `SE-289`–`SE-300` |
  | 26 | 43 | Patrones de diseño, empresariales y de resiliencia | `SE-313`–`SE-324` | `SE-517`–`SE-528` |
  | 27 | 25 | Arquitectura de software y dominio | `SE-325`–`SE-336` | `SE-301`–`SE-312` |
  | 28 | 44 | Estilos arquitectónicos | `SE-337`–`SE-348` | `SE-529`–`SE-540` |
  | 29 | 26 | Datos, persistencia y recuperación | `SE-349`–`SE-360` | `SE-313`–`SE-324` |
  | 30 | 45 | Ingeniería de datos y plataformas de datos | `SE-361`–`SE-372` | `SE-541`–`SE-552` |
  | 31 | 27 | Integración, eventos y mensajería | `SE-373`–`SE-384` | `SE-325`–`SE-336` |
  | 32 | 28 | Concurrencia y sistemas distribuidos | `SE-385`–`SE-396` | `SE-337`–`SE-348` |
  | 33 | 29 | Cloud, plataforma e infraestructura | `SE-397`–`SE-408` | `SE-349`–`SE-360` |
  | 34 | — | SaaS y plataformas de producto **(nueva, reservada)** | `SE-409`–`SE-420` | — |
  | 35 | 30 | Estrategia y técnicas de prueba | `SE-421`–`SE-432` | `SE-361`–`SE-372` |
  | 36 | 31 | Calidad, rendimiento y resiliencia | `SE-433`–`SE-444` | `SE-373`–`SE-384` |
  | 37 | 47 | Sistemas críticos, tiempo real y normas de seguridad | `SE-445`–`SE-456` | `SE-565`–`SE-576` |
  | 38 | 32 | Seguridad, privacidad y cumplimiento | `SE-457`–`SE-468` | `SE-385`–`SE-396` |
  | 39 | 33 | Build, release y cadena de suministro | `SE-469`–`SE-480` | `SE-397`–`SE-408` |
  | 40 | 34 | CI/CD, IaC y platform engineering | `SE-481`–`SE-492` | `SE-409`–`SE-420` |
  | 41 | 35 | Observabilidad, SRE e incidentes | `SE-493`–`SE-504` | `SE-421`–`SE-432` |
  | 42 | — | Ingeniería del caos **(nueva, reservada)** | `SE-505`–`SE-516` | — |
  | 43 | 36 | Mantenimiento y modernización legacy | `SE-517`–`SE-528` | `SE-433`–`SE-444` |
  | 44 | 37 | Gestión, liderazgo y práctica profesional | `SE-529`–`SE-540` | `SE-445`–`SE-456` |
  | 45 | 40 | Metodologías de desarrollo: de TDD a ODD | `SE-541`–`SE-552` | `SE-481`–`SE-492` |
  | 46 | 38 | Desarrollo de software asistido por IA | `SE-553`–`SE-564` | `SE-457`–`SE-468` |
  | 47 | 39 | SPEC, agentes y ciclo de vida agentic | `SE-565`–`SE-576` | `SE-469`–`SE-480` |
  | 48 | 41 | Harness y agentic engineering | `SE-577`–`SE-588` | `SE-493`–`SE-504` |
  | 49 | 42 | Patrones agénticos y sistemas con LLM | `SE-589`–`SE-600` | `SE-505`–`SE-516` |
  | 50 | 46 | Machine learning en producción y MLOps | `SE-601`–`SE-612` | `SE-553`–`SE-564` |

  El mapa clase por clase está en [`ID-MIGRATION.json`](../ID-MIGRATION.json) y se resume en
  [`ID-MIGRATION.md`](../ID-MIGRATION.md). Las clases se mueven por partes completas y conservan
  su posición y su título; la herramienta comprobó que los 588 títulos coinciden antes y después.
- Qué cambia en rutas y archivos (regla, no lista):
  - `content/part-AA/` pasa a `content/part-NN/`; `SE-aaa.md` a `SE-nnn.md`;
    `figures/se-aaa-<nombre>.svg` a `figures/se-nnn-<nombre>.svg` (el `<nombre>` no cambia).
  - `classes/part-AA-<parte>/se-aaa-<clase>/` pasa a `classes/part-NN-<parte>/se-nnn-<clase>/`
    (el slug no cambia; se regenera con los generadores).
  - `site/classes/SE-aaa.html` y `site/parts/AA.html` pasan a los números nuevos.
  - `scripts/figures_partAA_*.py` y `scripts/experiments_partAA_*.py` pasan a `partNN`.
  - Los encabezados `# SE-NNN —`, los enlaces, las figuras, las fuentes, los casos de estudio,
    las guías de rol, `curriculum.yaml`, `catalog.json`, `llms.txt`, el portal, el README y los
    validadores se reescriben con la misma regla.
- Compatibilidad:
  - **Etiqueta Git `pre-reorder-2026-11-23`**: conserva el árbol anterior completo.
  - **Mapa**: `docs/ID-MIGRATION.json` (fuente) y `docs/ID-MIGRATION.md` (lectura).
  - **Portal**: `site/legacy/` ofrece una página por cada ID y parte antiguos (588 clases y 49
    partes), con un aviso y un enlace al destino actual, y un índice con el mapa completo. Una URL
    antigua `classes/SE-nnn.html` **no puede** redirigir sola cuando el número cambió y sigue
    ocupado: ese ID pertenece ahora a otra clase. Las direcciones que quedaron vacantes
    (`SE-409`–`SE-420`, `SE-505`–`SE-516` y las partes 34 y 42) no tienen página: GitHub Pages
    sirve `site/404.html`, que explica el cambio y enlaza el mapa. Las páginas `legacy` no
    actualizan la dirección por sí solas, para que quien llega con un identificador antiguo vea el
    cambio.
  - **Documentos históricos** (ADR-002 a ADR-006, CHANGELOG, tracker y auditorías fechadas):
    conservan los IDs antiguos como evidencia de lo que se decidió entonces; llevan una nota
    que remite al mapa y sus enlaces apuntan a la clase migrada.
- Consecuencias:
  - Las citas externas a un `SE-nnn` anterior al 2026-11-23 deben leerse con el mapa. Ninguna
    clase se perdió ni cambió de título o de contenido más allá de los identificadores.
  - Los resultados que una clase cita de un experimento sobre el propio corpus del programa
    (por ejemplo `SE-594`, recuperación sobre las Partes 47 y 45) cambian de forma mínima
    porque el texto del corpus lleva identificadores nuevos; ya diferían de la cifra citada
    antes de esta decisión y deben leerse como la medición del momento.
  - Los validadores, generadores y pruebas leen el estado de `program_state.py`; ya no
    asumen rangos contiguos ni 49 partes.
  - Las sesiones que desarrollen las Partes 34 y 42 solo añaden contenido, figuras,
    experimentos y su rol; no editan contadores, tablas ni guías compartidas.
- Alternativas descartadas:
  - **Mantener la numeración y ordenar solo el índice.** Deja `SE-nnn` y rutas en orden de
    aparición: los enlaces y las citas seguirían mostrando un orden que no es el de estudio.
  - **Añadir las partes nuevas al final.** Prolonga el problema: SaaS y caos quedarían
    después de la IA, lejos de la arquitectura, la nube y la operación de las que dependen.
  - **Redirigir cada URL antigua en su mismo lugar.** Imposible: los números antiguos se
    reutilizan, de modo que una URL no puede servir a la vez la clase nueva y una redirección.
    Por eso se publica un mapa y una sección `legacy` con URLs propias.
- Verificación: `scripts/migrate_renumber.py` (con `dry-run`, `apply`, `verify` y `emit-map`)
  calculó la migración antes de aplicarla y comprobó 588 clases migradas, 51 partes con dos
  planificadas, 45 roles y 16 casos intactos; los generadores y validadores del repositorio
  se ejecutan sin diferencias pendientes. Ninguna de estas comprobaciones sustituye una
  revisión editorial humana independiente.
