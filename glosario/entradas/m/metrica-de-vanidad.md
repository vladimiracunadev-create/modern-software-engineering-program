# Métrica de vanidad

[↑ Glosario](../../README.md) · [← Métrica de valor](./metrica-de-valor.md) · [Métrica facturable →](./metrica-facturable.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Una **métrica de vanidad** es una cifra que sube sin que ninguna decisión cambie si baja, a menudo porque es acumulada ([SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md)). Ejemplos de la clase: registros acumulados, descargas, páginas vistas. Favorece la presentación pero no informa una decisión.

## Por qué importa

Una organización que se guía por métricas de vanidad se siente bien y no aprende. Estas cifras son agradables de mostrar y siempre crecen, así que no revelan problemas. Cambia el diseño de un panel: qué se muestra, con qué ventana y qué se hace con cada número.

## Cómo funciona

[SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) da la prueba de detección: **preguntar qué se haría distinto si la cifra bajara a la mitad**. Si la respuesta es «nada», es de vanidad; si hay una acción concreta, la métrica informa una decisión. Tiene dos defectos típicos: es **acumulada** (solo sube, aunque la gente deje de usar el producto) y **no está ligada a un comportamiento de valor** (descargar no es usar; registrarse no es lograr algo).

La clase la ubica en una clasificación de cuatro tipos (producción, actividad, resultado, vanidad) en una auditoría de métricas con una fila por métrica: definición calculable (numerador, denominador, ventana, filtros), tipo, decisión que informa, métrica contraria y fecha de revisión. El contrato es que ninguna métrica se convierte en meta sin su métrica contraria y sin la pregunta «qué haría distinto si bajara». La corrección más frecuente es reemplazar el acumulado por una métrica **por periodo** (activos del mes, retenidos) y acompañarla de un resultado.

Cuando una cifra de vanidad se convierte en meta ocurre lo que describe la ley de Goodhart: la gente ajusta su conducta para mover la cifra, y esta deja de medir lo que medía. La meta se cumple y nadie mejora, porque se premió la producción.

## Ejemplo

El panel de la plataforma muestra «estudiantes registrados: 12.480» (acumulado). Si baja a la mitad, ¿qué decisión cambia? Ninguna, porque no sabemos cuántos usan la plataforma. Sustituirla por «estudiantes con al menos una entrega aceptada en el mes» sí informa: si cae, hay que investigar qué pasó con el flujo de entrega. (Cifras ilustrativas.)

## Errores y confusiones comunes

- **El panel solo muestra crecimiento**: la métrica es acumulada; corrección: métricas por periodo.
- **La meta se cumple y nadie mejora**: se premió la producción; corrección: acompañar con un resultado y su métrica contraria.
- **Llamar «vanidad» a toda actividad**: la actividad puede ser un indicio útil, mientras informe una decisión.
- **Creer que basta cambiar la métrica**: sin decisión asociada, la nueva métrica se vuelve de vanidad.

## Límites y cuándo no aplica

La etiqueta depende del contexto: una cifra es de vanidad para una decisión y útil para otra (los registros acumulados importan para dimensionar infraestructura). Para presentaciones externas puede haber motivos legítimos para mostrarlas, siempre que no gobiernen decisiones internas. La prueba de la mitad es una heurística, no un cálculo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Baja](../b/baja.md), [Actividad](../a/actividad.md), [Ley de Goodhart](../l/ley-de-goodhart.md), [Producción](../p/produccion.md), [Resultado](../r/resultado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**Aparece en los casos de estudio:** [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Métricas de vanidad».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — definir qué medir a partir de lo que se necesita saber; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: Measuring user satisfaction](https://www.gov.uk/service-manual/measuring-success/measuring-user-satisfaction) — cómo medir satisfacción como complemento de indicadores de uso; autoridad: Government Digital Service.
- [Categorizing Variants of Goodhart's Law](https://arxiv.org/abs/1803.04585) — mecanismos por los que una medida deja de informar al volverse objetivo; autoridad: investigación publicada en arXiv (D. Manheim y S. Garrabrant).
- [DORA: Software delivery performance metrics](https://dora.dev/guides/dora-metrics-four-keys/) — conjunto equilibrado de métricas de entrega; autoridad: DORA (Google Cloud).
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — medición y economía de la ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Métrica de valor](./metrica-de-valor.md) · [Métrica facturable →](./metrica-facturable.md)
