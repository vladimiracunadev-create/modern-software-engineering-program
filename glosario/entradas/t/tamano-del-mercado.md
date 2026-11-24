# Tamaño del mercado

[↑ Glosario](../../README.md) · [← Tail latency](./tail-latency.md) · [Tamaño y potencia →](./tamano-y-potencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

El **tamaño del mercado** es la estimación de cuántas personas o cuánto dinero hay detrás de un segmento, con el método y los rangos usados a la vista ([SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md)). No es una cifra dada: es una estimación con supuestos, y por eso debe publicarse siempre con su rango.

## Por qué importa

Estimar con «el 1 % de un mercado grande» esconde una incertidumbre que cambia la decisión. Una cifra única transmite una precisión que no existe y conduce a apostar sin ver cuánto de ella es conocimiento. Cambia cómo se presenta un tamaño: método, supuestos y rango, no solo el número.

## Cómo funciona

[SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md) describe **dos maneras de estimar**. **Arriba-abajo** parte de un total (personas en el sector) y aplica una cuota; es rápida y se apoya en un porcentaje que nadie ha observado («si capturamos el 1 %»). **Abajo-arriba** parte de lo que se puede alcanzar con un canal concreto, aplica una conversión y un precio, y se parece a un plan de ventas; multiplica tres incertidumbres (alcance, conversión, precio) y por eso su rango es ancho.

**Ninguna da «el» tamaño**: ambas dan rangos que dependen de sus supuestos. Contrastarlas es útil: si el arriba-abajo da 10.000 personas y el abajo-arriba, 300, la diferencia señala que alguno de los supuestos es muy optimista y dónde investigar.

La regla de la plataforma de entregas es que el tamaño de cada segmento se conserva **como rango con método y supuestos**, junto con el criterio de definición, los trabajos, los contextos, los resultados insatisfechos, el canal de acceso y las alternativas, y que **ninguna cifra de mercado se publica sin su rango**. Para propagar la incertidumbre se muestrean los rangos de cada factor (por simulación) y se informa la mediana y el intervalo. El tamaño se conecta con la oportunidad (cuántas personas, con qué frecuencia, qué costo) y con la elección del segmento inicial.

## Ejemplo

Arriba-abajo: 40.000 docentes en el país × 1 % = 400 (pero ese 1 % nadie lo ha observado). Abajo-arriba: 2 departamentos con los que ya se trabaja × entre 15 y 40 docentes × conversión entre 20 % y 60 % = entre 6 y 48 docentes. El rango del segundo es honesto y alcanzable; el primero ilustra el peligro de la cuota imaginaria. (Cálculo propio para ilustrar los dos métodos de [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md).)

## Errores y confusiones comunes

- **«El 1 % de un mercado grande»**: cuota sin evidencia.
- **Publicar una cifra única** sin rango.
- **Segmentos inestables** o que nadie reconoce, sobre los que se calcula el tamaño.
- **Confundir tamaño de mercado con ingresos esperados.**

## Límites y cuándo no aplica

Para mercados nuevos no hay datos de base; las estimaciones son especulativas. El tamaño no dice si el segmento pagaría ni si se puede alcanzar. Las cifras de [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md) son supuestos del autor que muestran el método.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Rango](../r/rango.md), [Segmento](../s/segmento.md), [Vista](../v/vista.md), [Alternativas existentes](../a/alternativas-existentes.md), [Estabilidad de segmentos](../e/estabilidad-de-segmentos.md), [Segmentación por necesidad](../s/segmentacion-por-necesidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-126 — Segmentación, mercado y alternativas existentes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Ben-Hur, Elisseeff y Guyon (2002): A stability based method for discovering structure in clustered data](https://psb.stanford.edu/psb-online/proceedings/psb02/benhur.pdf) — estabilidad de agrupamientos ante submuestras; autoridad: Pacific Symposium on Biocomputing.
- [Strategyn: Outcome-Driven Innovation](https://strategyn.com/outcome-driven-innovation-process/) — segmentación por necesidades insatisfechas; autoridad: Strategyn (fuente del autor del método).
- [Douglas Hubbard: How to Measure Anything](https://www.howtomeasureanything.com/) — rangos e incertidumbre en la estimación; autoridad: Hubbard Decision Research.
- [Strategyzer: Value Proposition Canvas](https://www.strategyzer.com/library/the-value-proposition-canvas) — ajuste entre propuesta y perfil de cliente; autoridad: Strategyzer.
- [Know Your Customers' «Jobs to Be Done» (Harvard Business Review, 2016)](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) — trabajos como base de la competencia; autoridad: Harvard Business Review (artículo parcialmente de pago).

---

[↑ Glosario](../../README.md) · [← Tail latency](./tail-latency.md) · [Tamaño y potencia →](./tamano-y-potencia.md)
