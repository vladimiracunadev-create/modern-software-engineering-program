# Descomposición exacta

[↑ Glosario](../../README.md) · [← Descomposición](./descomposicion.md) · [Descomposición por responsabilidad →](./descomposicion-por-responsabilidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Reparto del cambio de la raíz entre factores sin depender del orden de sustitución.

Definición de trabajo de [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md).

## Por qué importa

En [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md), el tema «Descomposición exacta» importa porque explica qué factor movió la raíz sin los errores de sumar porcentajes.

## Cómo funciona

Según [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md), en la sección «Descomposición exacta»:

Cuando todos los factores cambian, la suma de sus porcentajes subestima el cambio del producto, y el error crece con el tamaño de los cambios. La descomposición logarítmica es exacta y no depende del orden, pero su reparto en porcentajes explota cuando el cambio total es casi cero. La regla del taller: informar cambios por factor, el exacto del padre y las participaciones solo si el cambio total supera un umbral declarado.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md):

En la plataforma, `metric-tree.md` contiene el árbol completo con una fila por nodo (nombre, fórmula o fuente, responsable, decisión, contraria), el validador, las dieciséis mutaciones con su resultado, la tabla de descomposición y el orden de hojas. El contrato es que ningún nodo se añade sin los cinco campos y que cada cambio de fórmula conserva la raíz exacta. Esa estructura permite que otra persona recalcule la raíz con otros valores y vea qué cambia.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se celebra que un factor explica 90 % del cambio** — causa: se usó sustitución en un solo orden. Corrección: usar descomposición exacta y umbral para participaciones. ([SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El validador se evaluó con dieciséis mutaciones elegidas por el autor y tres árboles nuevos, por lo que su exactitud real es desconocida; los costos de mejora y los baselines son supuestos. La siguiente clase integra el árbol en un caso de viabilidad técnico-económica.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-142](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Raíz](../r/raiz.md), [Sustitución](../s/sustitucion.md), [Árbol de métricas](../a/arbol-de-metricas.md), [Efecto por costo](../e/efecto-por-costo.md), [Mutación](../m/mutacion.md), [Nodo completo](../n/nodo-completo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — definir indicadores con su cálculo, fuente y uso; autoridad: Government Digital Service (Reino Unido).
- [Measuring the User Experience on a Large Scale: HEART (Google Research)](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) — de objetivos a señales y métricas; autoridad: Google Research.
- [DORA: Software delivery performance metrics](https://dora.dev/guides/dora-metrics-four-keys/) — conjunto equilibrado de métricas con contrapesos; autoridad: DORA (Google Cloud).
- [Categorizing Variants of Goodhart's Law](https://arxiv.org/abs/1803.04585) — por qué cada nodo necesita un contrapeso; autoridad: investigación publicada en arXiv.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — medición en ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Descomposición](./descomposicion.md) · [Descomposición por responsabilidad →](./descomposicion-por-responsabilidad.md)
