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
| 04 | Profundizada con cálculos y mediciones reales (pendiente de CI verde) | — |
| 05 | Desarrollada; pendiente de profundizar en contenido y figuras | — |
| 06 | Profundizada con experimentos de paradigmas ejecutados en Windows y Linux (pendiente de CI verde) | — |
| 07 | Profundizada con experimentos de estructuras y algoritmos ejecutados en Windows y Linux (pendiente de CI verde) | — |
| 08–29 | Borradores; requieren desarrollo completo | — |
| 30–39 | Estructura; requieren desarrollo completo | — |
| 40–44 | Propuestas en la auditoría; aún sin publicar | — |
