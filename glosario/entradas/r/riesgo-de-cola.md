# Riesgo de cola

[↑ Glosario](../../README.md) · [← Riesgo arquitectónico](./riesgo-arquitectonico.md) · [Riesgo residual →](./riesgo-residual.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md)

## Definición

Evento de probabilidad baja y consecuencia alta, cuyo impacto domina el valor esperado o es inaceptable por sí mismo.

Definición de trabajo de [SE-534 — Gestión de riesgos y decisiones ejecutivas](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md).

## Por qué importa

La clase donde se define, [SE-534 — Gestión de riesgos y decisiones ejecutivas](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md), existe con este propósito: la clase existe para que gestiones riesgos con números que sirvan a una decisión y para que presentes esa decisión a quien tiene autoridad para tomarla.

## Cómo funciona

Según [SE-534 — Gestión de riesgos y decisiones ejecutivas](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** un riesgo «amarillo» ocurre y cuesta más que tres «rojos» mitigados. **Hipótesis rivales:** (a) la probabilidad estaba mal estimada; (b) el impacto estaba subestimado; (c) la celda agrupó impactos de órdenes de magnitud distintos. **Prueba:** recalcula el valor esperado con rangos numéricos y ordena; si el riesgo sube al primer lugar, la causa es la agrupación. **Conclusión:** la matriz deja fuera el mayor riesgo en el 8,5 % de las carteras de la simulación. **Regresión:** exige que cada riesgo de cola tenga un impacto numérico y se revise aparte, y compara cada trimestre el orden por matriz con el orden por valor esperado.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-534 — Gestión de riesgos y decisiones ejecutivas](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo prepara una petición para la dirección académica sobre la exportación. Registra doce riesgos con rangos de probabilidad e impacto y calcula el valor esperado de cada uno; tres suman casi dos tercios de la pérdida esperada, y uno de ellos, la pérdida de datos de actas, es un evento de cola que además considera inaceptable por sí mismo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El riesgo de cola se ignora** — causa: probabilidad baja domina el color. Corrección: tratar la cola como restricción aparte. ([SE-534](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-534 — Gestión de riesgos y decisiones ejecutivas](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md)) son: Las definiciones son operativas para el equipo de plataforma educativa. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes primarias enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se evaluó ningún riesgo ni decisión real; las distribuciones, los cortes de la matriz, el ruido de la prueba, la fracción de decisiones irreversibles y los costos son construcciones del autor, y el modelo supone riesgos independientes y decisiones de todo o nada.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-533](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor esperado](../v/valor-esperado.md), [Baja](../b/baja.md), [Consecuencia](../c/consecuencia.md), [Evento](../e/evento.md), [Decisión reversible](../d/decision-reversible.md), [Petición de decisión](../p/peticion-de-decision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-534 — Gestión de riesgos y decisiones ejecutivas](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Cox, «What's Wrong with Risk Matrices?»](https://doi.org/10.1111/j.1539-6924.2008.01030.x) — límites de las matrices de riesgo; autoridad: Risk Analysis.
- [Howard, «Information Value Theory»](https://doi.org/10.1109/TSSC.1966.300074) — valor de la información en la decisión; autoridad: IEEE Transactions on Systems Science and Cybernetics.
- [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) — guía de evaluación de riesgos; autoridad: NIST.
- [Google SRE, «Embracing Risk»](https://sre.google/sre-book/embracing-risk/) — riesgo como costo aceptado con objetivo; autoridad: equipo de SRE de Google.
- [Nygard, «Documenting Architecture Decisions»](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — registro breve de decisiones; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Riesgo arquitectónico](./riesgo-arquitectonico.md) · [Riesgo residual →](./riesgo-residual.md)
