# Resultado

[↑ Glosario](../../README.md) · [← Restricciones y marcadores](./restricciones-y-marcadores.md) · [Resultado explícito →](./resultado-explicito.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

En métricas de producto, el **resultado** (*outcome*) es el cambio observable en quien usa el producto o en su organización, con definición calculable y fuente de datos ([SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md)): la persona logra su objetivo, el docente tarda menos, el centro reduce reclamos. Es el tercer escalón de la cadena producción → actividad → resultado.

## Por qué importa

Es lo que de verdad importa y lo que más cuesta medir. Cambia a qué se le llama éxito: no a cuántas funciones se lanzaron ni a cuánta gente entró, sino a si algo mejoró para alguien. [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) lo contrasta con la producción: un equipo con alta producción y resultados nulos es posible, y también uno con poca producción y alto resultado.

## Cómo funciona

El resultado se mide con **eventos de logro, tiempos y encuestas** con definición calculable (numerador, denominador, ventana, filtros). «La entrega llegó» es un evento de logro; «el docente corrigió en menos tiempo» es un tiempo comparado; «el centro redujo reclamos» es un conteo por periodo. La definición calculable es lo que evita que dos paneles den cifras distintas para «lo mismo».

Dos propiedades lo distinguen. Primero, es **más difícil de falsear** que la producción: cerrar más tickets se logra con fraccionarlos, pero hacer que más entregas lleguen requiere que el flujo funcione. Segundo, **se atribuye con cautela**: que el resultado mejore tras un cambio no prueba que el cambio lo causó, y [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md) enseña los experimentos, los controles y la regresión a la media precisamente para eso.

Aun así, el resultado no se persigue solo: se acompaña de una **métrica contraria** (algo que no debe empeorar mientras se mejora, como la calidad de lo entregado o el tiempo de respuesta), y la regla de la auditoría de métricas de [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) es que ninguna métrica se convierte en meta sin su contraria y sin la pregunta «qué haría distinto si bajara».

## Ejemplo

En la plataforma de entregas, **producción**: funciones lanzadas en el trimestre. **Actividad**: inicios de sesión de estudiantes. **Resultado**: proporción de entregas aceptadas antes del plazo, o minutos que tarda un docente en revisar un lote. Si se lanza un panel de seguimiento y el tiempo de revisión baja de 40 a 25 minutos por lote, hay un resultado asociado (con las cautelas de atribución). (Cifras ilustrativas.)

## Errores y confusiones comunes

- **La meta se cumple y nadie mejora**: se premió la producción; corrección: reemplazar o acompañar con un resultado y su contraria.
- **Un equipo gana premios con malos resultados**: se compararon producciones.
- **Confundir resultado con actividad**: en el experimento de equipos de [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), la actividad correlaciona 0,20 con el resultado.
- **Atribuir causalidad sin diseño**: una mejora tras un cambio puede tener otras causas.

## Límites y cuándo no aplica

Los resultados suelen tardar en notarse y requieren instrumentación y a veces encuestas, lo que no siempre es viable. Para productos en fase muy temprana, con pocos usuarios, el resultado tiene mucha incertidumbre (intervalos anchos). Hay resultados que no se miden de forma directa y se aproximan con indicadores sustitutos; hay que declararlo. Y optimizar un solo resultado puede dañar otros, por eso la métrica contraria.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Organización](../o/organizacion.md), [Actividad](../a/actividad.md), [Ley de Goodhart](../l/ley-de-goodhart.md), [Métrica de vanidad](../m/metrica-de-vanidad.md), [Producción](../p/produccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (604 clases más lo mencionan; las que más):

[SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md), [SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), [SE-539](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md), [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md), [SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «outcome».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — definir qué medir a partir de lo que se necesita saber; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: Measuring user satisfaction](https://www.gov.uk/service-manual/measuring-success/measuring-user-satisfaction) — cómo medir satisfacción como complemento de indicadores de uso; autoridad: Government Digital Service.
- [Categorizing Variants of Goodhart's Law](https://arxiv.org/abs/1803.04585) — mecanismos por los que una medida deja de informar al volverse objetivo; autoridad: investigación publicada en arXiv (D. Manheim y S. Garrabrant).
- [DORA: Software delivery performance metrics](https://dora.dev/guides/dora-metrics-four-keys/) — conjunto equilibrado de métricas de entrega; autoridad: DORA (Google Cloud).
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — medición y economía de la ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Restricciones y marcadores](./restricciones-y-marcadores.md) · [Resultado explícito →](./resultado-explicito.md)
