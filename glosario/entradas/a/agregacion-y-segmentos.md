# Agregación y segmentos

[↑ Glosario](../../README.md) · [← Agregación](./agregacion.md) · [Agregado →](./agregado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Forma de combinar o separar grupos al calcular una medida; decide si una diferencia aparece, desaparece o se invierte.

Definición de trabajo de [SE-122 — Usuarios, actores, trabajos y contextos](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md).

## Por qué importa

En [SE-122 — Usuarios, actores, trabajos y contextos](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md), el tema «Agregación y segmentos» importa porque una métrica agregada puede dar la conclusión contraria a la de cada contexto por separado.

## Cómo funciona

Según [SE-122 — Usuarios, actores, trabajos y contextos](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md), en la sección «Agregación y segmentos»:

Agregar es resumir, y resumir descarta estructura. Cuando dos opciones se prueban sobre mezclas de contextos distintas, la mejor en cada contexto puede resultar peor en el total (paradoja de Simpson). No es un error de cálculo: es una consecuencia de que la composición de la muestra difiere. La defensa es declarar de antemano por qué dimensiones se desagrega, mirar la métrica por contexto relevante y preguntar cómo se asignó cada opción a cada grupo. Un segmento útil es el que cambia una decisión, no el que reduce el promedio de varianza.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-122 — Usuarios, actores, trabajos y contextos](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md):

En la plataforma de entregas, el mapa de actores conserva por cada actor: rol, qué decide o veta, qué evidencia aceptaría, qué teme y qué contexto habita. Un trabajo conserva circunstancia, deseo, resultado y contexto que lo altera. El contrato es que ninguna afirmación de mejora se publica sin su desagregación por los contextos declarados.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-122 — Usuarios, actores, trabajos y contextos](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md)) son:

- **La opción «ganadora» empeora la experiencia de un grupo específico** — causa: se decidió con la métrica agregada y composiciones distintas por opción. Corrección: desagregar por los contextos declarados y comparar con la misma mezcla (estandarizar) antes de decidir.
- **La persona-ficha no se parece a nadie que se haya entrevistado** — causa: se construyó con promedios o con intuición. Corrección: construir la persona desde observaciones concretas y declarar de dónde viene cada rasgo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-122 — Usuarios, actores, trabajos y contextos](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones con datos sintéticos en Windows y Ubuntu (WSL2), con salidas idénticas. No se entrevistó a nadie, las dimensiones se simularon independientes y las tasas de Simpson son un cálculo reciclado. La siguiente clase pregunta cómo obtener evidencia cualitativa de las personas del mapa sin convertir una anécdota en verdad general.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medida](../m/medida.md), [Actores y cadena de decisión](./actores-y-cadena-de-decision.md), [Contextos](../c/contextos.md), [Personas y promedios](../p/personas-y-promedios.md), [Trabajos por hacer](../t/trabajos-por-hacer.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-122 — Usuarios, actores, trabajos y contextos](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Stanford Encyclopedia of Philosophy: Simpson's Paradox](https://plato.stanford.edu/entries/paradox-simpson/) — definición, ejemplos y discusión causal de la inversión por agregación; autoridad: Stanford University.
- [Know Your Customers' «Jobs to Be Done» (Harvard Business Review, 2016)](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) — describir al cliente por el trabajo que intenta hacer; autoridad: Harvard Business Review (artículo parcialmente de pago).
- [Strategyzer: Value Proposition Canvas](https://www.strategyzer.com/library/the-value-proposition-canvas) — perfil de cliente con trabajos, frustraciones y ganancias; autoridad: Strategyzer.
- [GOV.UK Service Standard](https://www.gov.uk/service-manual/service-standard) — su punto 1 es entender a las personas usuarias y sus necesidades y su punto 5 asegurar que todas puedan usar el servicio; autoridad: Government Digital Service.
- [GOV.UK Service Manual: User research](https://www.gov.uk/service-manual/user-research) — cómo investigar a las personas usuarias a lo largo del desarrollo; autoridad: Government Digital Service.

---

[↑ Glosario](../../README.md) · [← Agregación](./agregacion.md) · [Agregado →](./agregado.md)
