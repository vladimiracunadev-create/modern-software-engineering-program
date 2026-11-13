# Auditoría de brechas: metodologías de desarrollo en la era de la IA

Fecha: 2026-11-13. Estado: **alcance decidido el 2026-11-13: 540 clases en cinco partes nuevas (40–44)**; pendiente de aplicar a `curriculum.yaml`, roadmap y conteos, sin cambios en `curriculum.yaml`,
README ni conteos. Complementa `ROADMAP.md` y el plan maestro; no los sustituye.

## 1. Hallazgos sobre el programa actual

| Hallazgo | Evidencia | Consecuencia |
|---|---|---|
| Las metodologías guiadas por IA están casi sin desarrollar | Partes 38 y 39 son 24 clases de estructura; `SE-457` tiene 281 palabras frente a ~2000–2400 de las clases 00–06 | La brecha es de desarrollo, no solo de títulos |
| Harness engineering, EDD, ODD, loops de agentes y AI-DLC no aparecen como unidades | La búsqueda en el repositorio solo halla menciones sueltas en roadmap, roles y plan maestro | Requieren clases propias o una parte nueva |
| SDD está parcialmente cubierto | `SE-469`–`SE-472` (constitución, specify/clarify/plan/tasks) siguen el flujo de Spec Kit | Falta comparar spec-first, spec-anchored y spec-as-source y sus límites |
| Visuales escasos en las 72 clases | 84 bloques de figura para 72 clases (~1,2 por clase), casi todos un único mapa conceptual Mermaid | Se puede mejorar con diagramas de mecanismo, secuencia, fallo y comparación |
| Profundidad desigual en 00–05 | Entre 17 000 y 28 000 palabras por parte; la longitud no demuestra profundidad | Hace falta revisión cualitativa clase a clase, no más texto |

## 2. Metodologías investigadas

Las fuentes son mayoritariamente blogs de proveedores y preprints recientes; los
términos son jóvenes y sus definiciones varían. Cada clase debe contrastar con fuentes
primarias antes de publicar y declarar qué es consenso y qué es opinión.

- **Harness engineering.** Agente = modelo + harness: contexto, herramientas,
  restricciones, bucles de retroalimentación y recuperación alrededor del modelo. Se
  distingue de prompt engineering (una llamada) y de context engineering (una ventana).
  Patrones citados: `AGENTS.md`/`CLAUDE.md`, repositorio como base de conocimiento,
  menú único de validación para humanos, agentes y CI, bucles validar-corregir con
  límite de reintentos, y cumplimiento determinista (CI, permisos) porque las reglas en
  texto no garantizan conducta. Fuentes de partida:
  [Faros](https://www.faros.ai/blog/harness-engineering),
  [estudio de código fuente de once sistemas (arXiv)](https://arxiv.org/html/2609.00006v1),
  [decisiones de diseño en harnesses (arXiv)](https://arxiv.org/pdf/2604.18071).
- **Spec-driven development (SDD).** Tres niveles: spec-first (Spec Kit, Kiro),
  spec-anchored (OpenSpec, con deltas ADDED/MODIFIED/REMOVED para brownfield) y
  spec-as-source (Tessl). Riesgo señalado: sobrecarga de artefactos. Fuentes:
  [Wikipedia](https://en.wikipedia.org/wiki/Spec-driven_development),
  [comparativa de herramientas](https://ssojet.com/blog/best-spec-driven-development-tools).
- **Eval-driven development (EDD).** Las evaluaciones actúan como especificación y como
  puerta de release; no equivale a TDD porque las evals son lentas, costosas y
  probabilísticas, y un conjunto pequeño y curado supera a uno grande y débil. Fuentes:
  [Braintrust](https://braintrust.dev/articles/eval-driven-development),
  [DeepEval](https://deepeval.com/blog/eval-driven-development),
  [Xia et al. (arXiv)](https://arxiv.org/pdf/2411.13768v2.pdf).
- **AI-DLC (AWS).** Inception → Construction → Operations; la IA propone y las personas
  validan. Es método, no producto. Fuente:
  [AWS Builder](https://builder.aws.com/content/3KjWpM4sqd5f0zjUtE67OfUa7rk/ai-driven-development-life-cycle-ai-dlc-on-aws-a-new-approach-to-software-engineering).
- **Vibe coding vs. agentic engineering vs. loop engineering.** Exploración desechable
  frente a responsabilidad delegada con verificación. El bucle Ralph (atribuido a
  Geoffrey Huntley): un agente por tarea, contexto limpio en cada iteración, spec
  escrita como ancla, para combatir la degradación de contexto. Fuentes:
  [MindStudio](https://www.mindstudio.ai/blog/what-is-agentic-engineering),
  [Lushbinary](https://lushbinary.com/blog/loop-engineering-ai-coding-agents-guide/).
- **Organic Driven Development (ODD).** Flujo del ecosistema gentle-ai (Gentleman
  Programming) para agentes de código; no es una metodología académica y casi toda la
  evidencia es documentación del propio proyecto. Reglas: la autorización va primero
  (explicar e investigar son solo lectura); cambios pequeños sin archivo persistente;
  trabajo sustancial con un documento `odd/tasks/<feature>.md` (alcance, tareas,
  evidencia, siguiente paso) creado antes de tocar el código y reflejado en memoria
  para retomar entre sesiones; test-first (RED, GREEN, REFACTOR) por defecto cuando
  existe una prueba determinista relevante; commits en tramos de ~400 líneas; push, PR
  y merge son decisiones aparte. Un artículo de terceros lo presenta como relevo del SDD
  que el mismo equipo usaba antes; la página oficial no hace esa comparación, así que
  se enseña como contraste a verificar, no como hecho. Fuentes:
  [gentle-ai](https://github.com/Gentleman-Programming/gentle-ai),
  [uso previsto](https://github.com/Gentleman-Programming/gentle-ai/blob/main/docs/intended-usage.md),
  [artículo en español](https://cursosdesarrolloweb.com/articulos/organic-driven-development-odd/).
- **TDD, BDD, DDD y ATDD: cobertura real.** BDD existe en `SE-158` (Specification by
  Example y BDD) y DDD en `SE-305` (estratégico y táctico). TDD **no tiene clase
  propia**: solo hay `SE-363` "Pruebas unitarias y diseño testable" y menciones en
  Parte 05; ningún archivo de clases desarrolla el ciclo rojo-verde-refactor, sus
  críticas (escuela de Londres y clásica) ni su papel con agentes. ATDD tampoco aparece.

## 3. Propuesta estructural (sin renumerar `SE-001`–`SE-480`)

Añadir dos partes al final, para que el programa pase de 480 a 504 clases
(coherente con "aproximadamente 500"):

**Parte 40 · Metodologías de desarrollo: de TDD a ODD (`SE-481`–`SE-492`).** Mapa y
criterios para elegir metodología; TDD (ciclo, escuelas, límites); BDD y ATDD como
puente con `SE-158`; DDD como lenguaje ubicuo y contexto para agentes, enlazado con
`SE-305`; diseño por contrato como oráculo; SDD en sus tres niveles; EDD y gates;
ODD con su contraste frente a SDD; taller de comparación sobre un mismo cambio;
proyecto. `SE-363` y `SE-158` no se renumeran: se amplían o se referencian.

**Parte 41 · Harness y agentic engineering (`SE-493`–`SE-504`).** Anatomía de un
harness; instrucciones de repositorio y su cumplimiento determinista; herramientas y
permisos; gestión de contexto, resets y handoffs; loops (Ralph) y criterios de parada;
sandboxes y reversibilidad; verificación y gates; multiagente y coordinación;
observabilidad y evals del propio harness; AI-DLC y gobierno; taller de fallo;
proyecto.

Las Partes 38 y 39 se profundizan primero (hoy son estructura) y la 40–41 evitan
duplicarlas: 38–39 enseñan a usar la IA; 40–41 enseñan a organizar el desarrollo
alrededor de ella.

## 4. Mejora de las clases 00–05

Revisión cualitativa por clase con este criterio, además de `PEDAGOGICAL-STANDARD.md`:

1. Al menos tres figuras con función distinta: modelo del mecanismo, secuencia o
   línea de tiempo del fallo, y comparación o árbol de decisión.
2. Cada figura se acompaña de texto alternativo y de la afirmación que ilustra.
3. Un error realista con su diagnóstico paso a paso, no solo un ejemplo feliz.
4. Fuentes primarias enlazadas a cada afirmación técnica no trivial.
5. Un puente explícito hacia lo agentic: qué parte de la clase se delega, cuál se
   verifica y qué evidencia acepta el cambio.

## 5. Decisión pendiente

Orden recomendado: (1) profundizar 00–05 con
visuales, una parte por commit; (2) desarrollar 38–39; (3) crear 40–41; (4) retomar
06–37. Alterno: crear 40–41 primero, pero sin 38–39 desarrolladas quedarían sin base.

## 6. Segunda pasada: patrones, arquitecturas y patrones agénticos

Método: búsqueda de términos en los `README.md` de `classes/` (ausencia = 0 archivos).
Los borradores 06–37 comparten plantilla, así que una ausencia indica que el tema
anunciado en el título no se desarrolla, no que la clase falte.

| Área | Qué existe | Qué falta (0 menciones) |
|---|---|---|
| Patrones de diseño | `SE-292` agrupa creacionales, estructurales y conductuales en una clase; `SE-293` agrupa funcionales, reactivos y concurrentes | Ningún patrón GoF se nombra (ni Decorator, ni Strategy…); GRASP; Repository, Unit of Work y Active Record; catálogo de antipatrones |
| Patrones de resiliencia y nube | Circuit breaker y bulkhead aparecen en 5–6 archivos como mención | Tratamiento propio con mecanismo, parámetros y fallo; sidecar, ambassador, retry con jitter |
| Estilos de arquitectura | `SE-303`–`SE-307` cubren monolito/servicios, capas/hexagonal, event-driven y serverless | Microkernel/plugin, pipes and filters, BFF, service mesh, multi-tenancy, data mesh, arquitectura celular, 12-factor |
| Integración empresarial | `SE-325`–`SE-336` | Catálogo Enterprise Integration Patterns como lenguaje común |
| Patrones agénticos | `SE-473`–`SE-478` (agentes, permisos, skills, MCP, multiagente) a nivel de estructura | Orquestador-trabajadores, evaluador-optimizador, enrutamiento, paralelización, encadenado, ReAct, plan-and-execute, reflexión, memoria, embeddings y agentic RAG, A2A, ejecución durable, LLMOps |

Fuentes de partida para los patrones agénticos (blogs; el marco más citado es
*Building Effective Agents* de Anthropic, a leer en su fuente primaria):
[mapa de 12 patrones](https://uvik.net/blog/agentic-design-patterns/),
[8 arquitecturas](https://dataaspirant.com/blog/ai-agent-design-patterns/),
[patrones que reutilizan los agentes de código](https://dev.to/thesmartdude/agentic-design-patterns-the-shapes-every-coding-agent-reuses-3m15).
Los autores discrepan en la clasificación; la clase debe presentar el criterio de
cada uno y cuándo **no** usar un patrón (un agente cuesta más y falla más que un flujo
fijo).

### Propuesta ampliada (sustituye la de la sección 3 en alcance)

Sin renumerar `SE-001`–`SE-480`, cinco partes nuevas de 12 clases (+60 → 540):

| Parte | Tema | Clases |
|---|---|---|
| 40 | Metodologías de desarrollo: de TDD a ODD | `SE-481`–`SE-492` |
| 41 | Harness y agentic engineering | `SE-493`–`SE-504` |
| 42 | Patrones agénticos y sistemas con LLM (workflows, agentes, RAG, memoria, A2A/MCP, evals, ejecución durable, coste) | `SE-505`–`SE-516` |
| 43 | Catálogo de patrones de diseño, empresariales y de resiliencia (GoF en tres clases, GRASP, Repository/UoW, EIP, resiliencia, antipatrones) | `SE-517`–`SE-528` |
| 44 | Catálogo de estilos arquitectónicos (microkernel, pipes and filters, microservicios con sus costes, BFF/gateway/mesh, multi-tenancy, data mesh, celular, 12-factor) | `SE-529`–`SE-540` |

Compromiso: 540 se aleja de "aproximadamente 500". Alternativa: fusionar 43 y 44 en
una sola parte de 12 clases (528 en total) y llevar el resto como ampliación de
`SE-292` y `SE-303`–`SE-307`, que ya existen. Decisión pendiente; el roadmap exige
que cada ampliación resuelva una brecha real, y aquí cada fila lo hace.

### Decisión registrada (2026-11-13)

Estado de ejecución (2026-11-13): se profundizaron las Partes 00–26 (`SE-001`–`SE-324`);
quedan por desarrollar las Partes 27–29 (borradores), 30–39 (estructura) y crear 40–44
(planificadas, sin clases). El orden restante es: 27–29, 38–39 y 40–44, luego 30–37.

Se adopta el alcance de **540 clases** (Partes 40–44). Orden de ejecución: profundizar
las Partes 00–05 con visuales; desarrollar 38–39; crear 40–44; retomar 06–37. La
estructura nueva no se publica en `curriculum.yaml`, README, Pages ni About hasta que
cada parte tenga contenido real, para no inflar conteos sin evidencia. El número del
roadmap ("aproximadamente 500") deberá actualizarse con esa misma evidencia.
