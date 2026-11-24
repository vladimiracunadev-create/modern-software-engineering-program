# Descomposición

[↑ Glosario](../../README.md) · [← Descomponer la petición](./descomponer-la-peticion.md) · [Descomposición exacta →](./descomposicion-exacta.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

**Descomposición** es separar un todo en partes que se puedan tratar por separado. El programa usa la palabra con tres sentidos:

- **De un problema** ([SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md)): separarlo en resultados coordinables.
- **De una métrica** ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md)): repartir el cambio de una métrica entre los factores que la componen, con convención y orden declarados.
- **De un requisito de seguridad** ([SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md)): satisfacerlo con elementos redundantes de nivel menor que sean independientes.

## Por qué importa

Un problema grande no se puede estimar, repartir ni verificar; uno partido en piezas sí. Y una métrica agregada que cambia sin explicación no sirve para decidir: hay que saber qué factor se movió. La decisión que cambia es qué criterio se usa para cortar, porque dos cortes distintos pueden ser ambos «razonables» y llevar a trabajos diferentes.

## Cómo funciona

- **Problemas** ([SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md)): se declara un **criterio de descomposición** (por pregunta, no por herramienta) y se revisa el árbol contra él. Las partes deben ser coordinables: tener entradas y resultados claros.
- **Métricas** ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md)): una métrica norte producto de factores (alcance × frecuencia × éxito) se descompone para saber qué factor explicó un cambio. Con logaritmos, la contribución de cada factor suma el cambio total sin depender del orden; con sustitución secuencial depende del orden y se informa un rango. Si el cambio total es pequeño, las participaciones son inestables y no se informan como porcentajes.
- **Seguridad** ([SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md)): se cubre un requisito con elementos redundantes independientes de nivel menor; la independencia es lo que se comprueba.

## Ejemplo

[SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md): si el alcance sube un 10 % y el éxito baja un 5 %, el logaritmo reparte el cambio total en dos aportes que suman exactamente el total. Ilustración:

```python
import math
aporte = {k: math.log(nuevo[k]/viejo[k]) for k in viejo}
total = math.log(prod(nuevo.values())/prod(viejo.values()))   # == sum(aporte.values())
```

## Errores y confusiones comunes

- **Atribuir 90 % a un factor.** Causa: un solo orden de sustitución; corrección: logaritmos o informar el rango de órdenes ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md)).
- **Dos árboles distintos, ambos «válidos».** Causa: falta criterio de descomposición; corrección: declararlo y revisar contra él ([SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md)).
- **Creer que la descomposición explica el porqué.** Dice cuánto aportó cada factor, no por qué cambió.

## Límites y cuándo no aplica

Supone que la métrica es un producto exacto de los factores y que no hay interacciones fuera del producto ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md)). En problemas muy acoplados, partir sin criterio ofrece una ilusión de orden. Y los tres sentidos no son intercambiables: descomponer un problema no es descomponer una métrica.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Métrica](../m/metrica.md), [Problemas](../p/problemas.md), [Resultado](../r/resultado.md), [Abstracción](../a/abstraccion.md), [Corrección por comparaciones múltiples](../c/correccion-por-comparaciones-multiples.md), [Dominio](./dominio.md).
- **Se confunde con:** `problem-tree.md` debe conservar autorización y presupuesto como restricciones transversales y proponer una segunda descomposición; una lista de funciones del programa no equivale a descomponer el problema.

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (18 clases más lo mencionan; las que más):

[SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md), [SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), [SE-050](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md), [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: `itertools.permutations`](https://docs.python.org/3/library/itertools.html#itertools.permutations) — órdenes de sustitución de la descomposición.
- [Measuring the User Experience on a Large Scale: HEART (Google Research)](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) — dimensiones de experiencia y su traducción a objetivos y métricas; autoridad: Google Research.
- [Google SRE Book: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — presupuestos de error como límite explícito al riesgo; autoridad: Google SRE.
- [Categorizing Variants of Goodhart's Law](https://arxiv.org/abs/1803.04585) — cómo una medida deja de informar al volverse objetivo; autoridad: investigación publicada en arXiv.
- [DORA: Software delivery performance metrics](https://dora.dev/guides/dora-metrics-four-keys/) — métricas equilibradas de velocidad y estabilidad; autoridad: DORA (Google Cloud).

---

[↑ Glosario](../../README.md) · [← Descomponer la petición](./descomponer-la-peticion.md) · [Descomposición exacta →](./descomposicion-exacta.md)
