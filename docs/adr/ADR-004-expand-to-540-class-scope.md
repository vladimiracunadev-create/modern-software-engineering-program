# ADR-004 — Ampliar el alcance planificado de 480 a 540 clases

- Estado: aceptada el 2026-11-13; implementación pendiente.
- Contexto: la [auditoría de brechas](../METHODOLOGY-GAP-AUDIT-2026-11-13.md) halló que las
  metodologías de desarrollo guiadas por IA (TDD, BDD, ATDD, DDD, contratos, SDD, EDD,
  ODD, harness engineering), los patrones de diseño y los estilos arquitectónicos no
  tienen unidades propias en las 480 clases.
- Decisión: mantener `SE-001`–`SE-480` sin renumerar y añadir cinco partes de doce clases:
  Parte 40 (`SE-481`–`SE-492`, metodologías de TDD a ODD), Parte 41 (`SE-493`–`SE-504`,
  harness y agentic engineering), Parte 42 (`SE-505`–`SE-516`, patrones agénticos y
  sistemas con LLM), Parte 43 (`SE-517`–`SE-528`, patrones de diseño, empresariales y de
  resiliencia) y Parte 44 (`SE-529`–`SE-540`, estilos arquitectónicos).
- Consecuencias: el alcance planificado es de 540 clases. Hasta que cada parte nueva
  tenga contenido completo, `curriculum.yaml`, el catálogo, el portal y los validadores
  siguen describiendo 480 clases y 40 partes. No se publica una clase nueva sin
  contenido, figuras interpretadas, fuentes y revisión por parte.
- Relación con otras decisiones: complementa [ADR-003](ADR-003-reconcile-480-baseline-with-progressive-expansion.md);
  no la sustituye.
