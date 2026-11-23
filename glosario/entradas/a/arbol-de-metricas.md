# Árbol de métricas

[↑ Glosario](../../README.md) · [← Árbol de búsqueda](./arbol-de-busqueda.md) · [Árbol de trabajo →](./arbol-de-trabajo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Descomposición de una métrica norte en factores calculables, con responsable, fuente y decisión en cada nodo.

Definición de trabajo de [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md).

## Por qué importa

La clase donde se define, [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md), existe con este propósito: el taller existe para que las métricas de la [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md) dejen de ser una lista y pasen a ser un árbol: una métrica norte descompuesta en factores calculables, cada uno con responsable, fuente, decisión y contrapeso, que otra persona puede revisar con un validador y recalcular con otros valores.

## Cómo funciona

[SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final.

## Ejemplo

Ejemplo de [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) (sección «Caso conductor»):

La plataforma de entregas continúa como caso. Este taller deja el árbol de métricas con la raíz de `SE-139`, las definiciones de `SE-136`, los eventos de `SE-137`, los costos de `SE-140` y las reglas de revisión de `SE-141` y `SE-142`. `SE-144` lo usará como base del caso de viabilidad. Cambia después una sola hoja —por ejemplo, la tasa de aceptación— y revisa qué conclusiones del árbol cambian.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md)) son:

- **El árbol tiene dos raíces** — causa: se mezclaron métricas de dos objetivos. Corrección: elegir una raíz y mover la otra a una guarda.
- **La raíz no se recupera de las hojas** — causa: la fórmula suma donde debía multiplicar. Corrección: validar aritmética con los valores declarados.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El validador se evaluó con dieciséis mutaciones elegidas por el autor y tres árboles nuevos, por lo que su exactitud real es desconocida; los costos de mejora y los baselines son supuestos. La siguiente clase integra el árbol en un caso de viabilidad técnico-económica.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-142](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Métrica norte](../m/metrica-norte.md), [Descomposición](../d/descomposicion.md), [Métrica](../m/metrica.md), [Descomposición exacta](../d/descomposicion-exacta.md), [Efecto por costo](../e/efecto-por-costo.md), [Mutación](../m/mutacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-143 — Taller: diseñar un árbol de métricas](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), [SE-142](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md).

**Aparece en los casos de estudio:** [Quibi](../../../casos/fallo/quibi.md).

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

[↑ Glosario](../../README.md) · [← Árbol de búsqueda](./arbol-de-busqueda.md) · [Árbol de trabajo →](./arbol-de-trabajo.md)
