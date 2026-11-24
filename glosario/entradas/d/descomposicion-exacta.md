# Descomposición exacta

[↑ Glosario](../../README.md) · [← Descomposición](./descomposicion.md) · [Descomposición por responsabilidad →](./descomposicion-por-responsabilidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

La **descomposición exacta** es el reparto del cambio de la métrica raíz de un árbol de métricas entre sus factores sin depender del orden de sustitución. Es el sentido de [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md). Responde a la pregunta «¿qué factor movió el resultado y cuánto?» sin los errores que aparecen al sumar porcentajes.

## Por qué importa

Cambia qué se le atribuye a cada factor. Un árbol de métricas (por ejemplo, ingresos = usuarios × conversión × valor) sirve para decidir dónde actuar, pero si el reparto del cambio es incorrecto se celebra o se corrige el factor equivocado. [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) da un caso típico: se celebra que un factor explica el 90 % del cambio porque se usó sustitución en un solo orden.

## Cómo funciona

Cuando todos los factores cambian a la vez, la suma de sus cambios porcentuales subestima el cambio del producto, y el error crece con el tamaño de los cambios (efecto cruzado). Sustituir un factor por vez da resultados distintos según el orden elegido, de modo que la atribución depende de una convención arbitraria.

La descomposición logarítmica evita ambas cosas: el logaritmo del producto es la suma de los logaritmos de los factores, por lo que cada factor aporta una parte exacta del cambio total y el resultado no depende del orden. Su límite es que, expresada como porcentaje de participación, **explota cuando el cambio total es casi cero** (se divide por una cantidad diminuta). La regla del taller, por eso, es informar tres cosas: el cambio por factor, el cambio exacto del padre, y las participaciones solo si el cambio total supera un umbral declarado.

## Ejemplo

En [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md), `metric-tree.md` contiene el árbol completo con una fila por nodo (nombre, fórmula o fuente, responsable, decisión, contraria), el validador, las dieciséis mutaciones con su resultado, la tabla de descomposición y el orden de hojas. El contrato es que ningún nodo se añade sin esos cinco campos y que cada cambio de fórmula conserva la raíz exacta; otra persona puede recalcular la raíz con otros valores y ver qué cambia.

## Errores y confusiones comunes

- **Celebrar que un factor explica el 90 %.** Se usó sustitución en un solo orden; usar descomposición exacta y umbral para participaciones.
- **Sumar porcentajes de los factores.** Subestima el cambio del producto.
- **Informar participaciones con cambio total casi cero.** El reparto se vuelve inestable.
- **Confundir exactitud matemática con causalidad.** Repartir el cambio no dice por qué se movió el factor.

## Límites y cuándo no aplica

Solo vale para métricas que se componen multiplicativamente o de forma que permita el logaritmo; con suma de componentes basta una resta. Los resultados de [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) vienen de datos sintéticos y de un validador evaluado con dieciséis mutaciones elegidas por el autor, por lo que su exactitud real es desconocida. Describe aritmética, no causa.

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
