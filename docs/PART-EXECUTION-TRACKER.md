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
| 20 | Desarrollada y profundizada con experimentos sintéticos y modelos de backend, APIs y procesamiento asíncrono ejecutados en Windows y Linux (pendiente de CI verde) | — |
| 21 | Desarrollada y profundizada con experimentos sintéticos y modelos de software móvil, escritorio y multiplataforma ejecutados en Windows y Linux (pendiente de CI verde) | pendiente |
| 22–29 | Borradores; requieren desarrollo completo | — |
| 30–39 | Estructura; requieren desarrollo completo | — |
| 40–44 | Propuestas en la auditoría; aún sin publicar | — |
