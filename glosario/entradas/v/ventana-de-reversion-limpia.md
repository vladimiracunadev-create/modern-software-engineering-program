# Ventana de reversión limpia

[↑ Glosario](../../README.md) · [← Ventana de retención](./ventana-de-retencion.md) · [Verdad de referencia →](./verdad-de-referencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Periodo en que un cambio puede deshacerse sin conflictos.

Definición de trabajo de [SE-564 — Proyecto: cambio real con trazabilidad y revisión humana](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md).

## Por qué importa

La clase donde se define, [SE-564 — Proyecto: cambio real con trazabilidad y revisión humana](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md), existe con este propósito: el proyecto cierra la [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md) con el ejercicio que la justifica: llevar un cambio real, hecho con ayuda de un asistente, desde el criterio de aceptación hasta la integración, de modo que cualquier persona pueda reconstruir quién decidió qué, qué propuso la herramienta, qué se rechazó, qué se comprobó y cómo se deshace.

## Cómo funciona

[SE-564 — Proyecto: cambio real con trazabilidad y revisión humana](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-564 — Proyecto: cambio real con trazabilidad y revisión humana](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones ejecuta el proyecto sobre el cambio de las notas ausentes. El `PLAN.md` fija el criterio («una nota ausente lanza `ValueError` con el nombre del alumno y la evaluación; ninguna otra función cambia»), cinco casos derivados del reglamento y el límite de 40 líneas de diff; el flujo es el asistido, con las compuertas de pruebas, análisis y revisión nombrada.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-564 — Proyecto: cambio real con trazabilidad y revisión humana](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md)) son:

- **No se sabe qué criterio se usó** — causa: el plan se escribió después de la solución. Corrección: criterios por escrito antes de pedir nada.
- **«Se revisó» sin saber quién ni qué** — causa: aprobación sin nombre ni alcance. Corrección: registro con persona, archivos y comprobaciones.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-564 — Proyecto: cambio real con trazabilidad y revisión humana](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una bitácora encadenada real escrita en un directorio temporal y atacada de cinco maneras, una simulación de compuertas independientes con una curva de fatiga y una simulación de reversión con ediciones al azar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md), [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md), [SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md), [SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conflicto](../c/conflicto.md), [Ancla externa](../a/ancla-externa.md), [Bitácora encadenada](../b/bitacora-encadenada.md), [Compuerta](../c/compuerta.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Reversibilidad](../r/reversibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-564 — Proyecto: cambio real con trazabilidad y revisión humana](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Haber y Stornetta, «How to time-stamp a digital document»](https://doi.org/10.1007/BF00196791) — encadenado de registros con resúmenes criptográficos; autoridad: Journal of Cryptology.
- [SLSA: provenance](https://slsa.dev/spec/v1.0/provenance) — formato de declaración de procedencia; autoridad: especificación del proyecto SLSA.
- [NIST SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final) — prácticas de desarrollo seguro para IA generativa; autoridad: NIST.
- [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) — supervisión humana y registro de eventos en sistemas de alto riesgo; autoridad: Unión Europea.
- [Git: git-revert](https://git-scm.com/docs/git-revert) — reversión de cambios; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Ventana de retención](./ventana-de-retencion.md) · [Verdad de referencia →](./verdad-de-referencia.md)
