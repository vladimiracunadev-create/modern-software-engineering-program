# Nodo completo

[↑ Glosario](../../README.md) · [← No-code](./no-code.md) · [Noindex →](./noindex.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Un **nodo completo** de un árbol de métricas es un nodo con nombre, fórmula o fuente, responsable nombrado, decisión que informa y, en la raíz, métrica contraria ([SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md)). Es la unidad de un árbol de métricas, que descompone una métrica raíz (por ejemplo, ingresos o entregas aceptadas) en factores y hojas medibles.

## Por qué importa

Un nodo sin responsable, fuente o decisión es una métrica sin dueño ni uso. Un árbol con nodos incompletos se ve bien en un diagrama y no sirve para actuar: nadie sabe de dónde sale cada cifra ni qué se hace con ella. Cambia la disciplina de construir y mantener un árbol: cada nodo se añade con todos sus campos o no se añade.

## Cómo funciona

[SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) enumera los campos de cada nodo:

- **nombre**;
- **fórmula** (si el nodo no es hoja, cómo se calcula a partir de sus hijos) o **fuente** (si es hoja, de dónde viene el dato);
- **responsable nombrado**, una persona o un rol con nombre, **no «el equipo»**;
- **decisión que informa**, qué se hace distinto si el valor cambia;
- en la raíz, una **métrica contraria** que vigila el daño posible de optimizarla.

La razón de cada campo es la ausencia que evita. Una hoja con fuente pero sin decisión **no se usa**; una con decisión pero sin fuente **no se puede calcular**. Sin responsable, nadie atiende cuando el valor se desvía. Sin fórmula, la raíz no se puede recuperar de las hojas.

El árbol de la plataforma vive en un archivo con una fila por nodo, un validador y dieciséis mutaciones que miden qué detecta. El contrato es que **ningún nodo se añade sin los cinco campos** y que cada cambio de fórmula conserva la raíz exacta. Dos fallos con causa conocida: el árbol con dos raíces (se mezclaron métricas de dos objetivos; se elige una raíz y se mueve la otra a una guarda) y la raíz que no se recupera de las hojas (la fórmula suma donde debía multiplicar; se valida la aritmética con los valores declarados).

El validador comprueba la completitud de forma mecánica; que la decisión sea relevante o que el responsable sea adecuado lo juzga una persona.

## Ejemplo

Raíz: «entregas aceptadas a tiempo por semana» = «estudiantes activos» × «entregas por estudiante» × «tasa de aceptación a tiempo». Nodo hoja «tasa de aceptación a tiempo»: fuente, tabla de entregas; responsable, la coordinadora de producto; decisión que informa, si se revisa el flujo de validación; sin métrica contraria porque no es la raíz. La raíz lleva como contraria la tasa de reclamos. (Árbol ilustrativo en el estilo de [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md).)

## Errores y confusiones comunes

- **Árbol con dos raíces**: se mezclaron objetivos.
- **Raíz que no se recupera de las hojas**: error de aritmética (suma en lugar de producto).
- **Responsable «el equipo».**
- **Hojas con fuente pero sin decisión**: métricas decorativas.

## Límites y cuándo no aplica

Un árbol completo no garantiza que las métricas sean las correctas ni que el responsable actúe. El validador de [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) se evaluó con dieciséis mutaciones elegidas por el autor, de modo que su exactitud real es desconocida. Para métricas efímeras de un experimento, la formalidad completa puede ser excesiva.

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
