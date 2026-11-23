# Nodo completo

[↑ Glosario](../../README.md) · [← No-code](./no-code.md) · [Noindex →](./noindex.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Nodo con nombre, fórmula o fuente, responsable nombrado, decisión que informa y, en la raíz, métrica contraria.

Definición de trabajo de [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md).

## Por qué importa

En [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md), el tema «Nodos completos» importa porque un nodo sin responsable, fuente o decisión es una métrica sin dueño ni uso.

## Cómo funciona

Según [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md), en la sección «Nodos completos»:

Cada nodo lleva: nombre, fórmula (si no es hoja) o fuente (si lo es), responsable nombrado, decisión que informa y, en la raíz, una métrica contraria. Una hoja con fuente pero sin decisión no se usa; una con decisión pero sin fuente no se puede calcular. El campo «responsable» debe ser una persona o un rol con nombre, no «el equipo».

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md):

En la plataforma, `metric-tree.md` contiene el árbol completo con una fila por nodo (nombre, fórmula o fuente, responsable, decisión, contraria), el validador, las dieciséis mutaciones con su resultado, la tabla de descomposición y el orden de hojas. El contrato es que ningún nodo se añade sin los cinco campos y que cada cambio de fórmula conserva la raíz exacta. Esa estructura permite que otra persona recalcule la raíz con otros valores y vea qué cambia.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md)) son:

- **El árbol tiene dos raíces** — causa: se mezclaron métricas de dos objetivos. Corrección: elegir una raíz y mover la otra a una guarda.
- **La raíz no se recupera de las hojas** — causa: la fórmula suma donde debía multiplicar. Corrección: validar aritmética con los valores declarados.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El validador se evaluó con dieciséis mutaciones elegidas por el autor y tres árboles nuevos, por lo que su exactitud real es desconocida; los costos de mejora y los baselines son supuestos. La siguiente clase integra el árbol en un caso de viabilidad técnico-económica.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-142](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Métrica contraria](../m/metrica-contraria.md), [Métrica](../m/metrica.md), [Raíz](../r/raiz.md), [Árbol de métricas](../a/arbol-de-metricas.md), [Descomposición exacta](../d/descomposicion-exacta.md), [Efecto por costo](../e/efecto-por-costo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Nodos completos».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — definir indicadores con su cálculo, fuente y uso; autoridad: Government Digital Service (Reino Unido).
- [Measuring the User Experience on a Large Scale: HEART (Google Research)](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) — de objetivos a señales y métricas; autoridad: Google Research.
- [DORA: Software delivery performance metrics](https://dora.dev/guides/dora-metrics-four-keys/) — conjunto equilibrado de métricas con contrapesos; autoridad: DORA (Google Cloud).
- [Categorizing Variants of Goodhart's Law](https://arxiv.org/abs/1803.04585) — por qué cada nodo necesita un contrapeso; autoridad: investigación publicada en arXiv.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — medición en ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← No-code](./no-code.md) · [Noindex →](./noindex.md)
