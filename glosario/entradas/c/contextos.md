# Contextos

[↑ Glosario](../../README.md) · [← Contexto delimitado](./contexto-delimitado.md) · [Contingencia →](./contingencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

En descubrimiento de producto, los **contextos** son el conjunto de condiciones físicas, sociales y técnicas en que ocurre un trabajo y que alteran su probabilidad de éxito ([SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md)). No son los «contextos delimitados» del diseño dirigido por el dominio, que son otro concepto; aquí se trata de la situación en que una persona intenta hacer algo.

## Por qué importa

El mismo trabajo se cumple o fracasa según dispositivo, conexión, tiempo, ayuda disponible y consecuencias de equivocarse. Un producto que funciona en el contexto del equipo de desarrollo puede fallar en el de quien lo usa. Cambia cómo se evalúa una mejora: una afirmación de que algo mejoró debe decir para qué contextos.

## Cómo funciona

[SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md) ejemplifica el contexto como lo que **no está en la pantalla**: una conexión que se corta, un teléfono compartido, la ayuda de un familiar, una fecha límite que cae un domingo, un lector de pantalla. Dos personas con el mismo trabajo y contextos distintos pueden necesitar productos distintos. Por eso la descripción de un trabajo se acompaña de una lista corta de contextos que cambian el resultado.

La consecuencia metodológica es la **desagregación**. Si se decide con una métrica agregada, y las composiciones de contextos son distintas en cada opción, la opción «ganadora» puede empeorar la experiencia de un grupo específico. La corrección es desagregar por los contextos declarados y comparar con la misma mezcla (estandarizar) antes de decidir. [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md) incluye un ejercicio con versión, comando y salida registrados, donde se añade un tercer contexto para comprobar si la inversión se mantiene: depende de cuántos intentos aporta cada plan a cada contexto, no solo de las tasas. Es el mismo mecanismo de la paradoja de Simpson.

Esto afecta también a las personas-ficha: una «persona» de producto no puede ser el promedio de nadie; debe ser un caso concreto con un contexto reconocible, construido a partir de observaciones, y declarada como ilustración, no como estadística. Su función es comunicar un contexto concreto, no representar estadísticamente.

## Ejemplo

Trabajo: «confirmar que mi entrega llegó». Contexto A: escritorio con buena conexión; contexto B: móvil con conexión inestable. Una mejora que acelera la confirmación un 20 % en promedio puede mejorar A un 30 % y empeorar B un 5 %. Con el agregado se declara éxito; desagregado por contexto, se ve el daño a B. (Cifras ilustrativas del razonamiento de [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md).)

## Errores y confusiones comunes

- **La opción «ganadora» empeora a un grupo**: se decidió con la métrica agregada; corrección: desagregar y estandarizar la mezcla.
- **Describir el trabajo sin contextos.**
- **Persona-ficha como promedio.**
- **Confundir contexto con segmento**: el contexto describe la situación; el segmento, a un grupo de personas.

## Límites y cuándo no aplica

No se pueden enumerar todos los contextos posibles: se eligen los que cambian el resultado según evidencia. Con pocas observaciones, la lista de contextos es hipótesis. Y desagregar demasiado deja grupos tan pequeños que sus cifras no son fiables.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](./condicion.md), [Conjunto](./conjunto.md), [Trabajo](../t/trabajo.md), [Actores y cadena de decisión](../a/actores-y-cadena-de-decision.md), [Agregación y segmentos](../a/agregacion-y-segmentos.md), [Personas y promedios](../p/personas-y-promedios.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-122 — Usuarios, actores, trabajos y contextos](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (524 clases más lo mencionan; las que más):

[SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md), [SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), [SE-580](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md), [SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

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

[↑ Glosario](../../README.md) · [← Contexto delimitado](./contexto-delimitado.md) · [Contingencia →](./contingencia.md)
