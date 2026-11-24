# Trabajos por hacer

[↑ Glosario](../../README.md) · [← Trabajo venenoso](./trabajo-venenoso.md) · [Traceability →](./traceability.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Un **trabajo por hacer** (*job to be done*) es el progreso que una persona intenta lograr en una circunstancia concreta, formulado como «cuando… quiero… para…» ([SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md)). La idea central es que las personas «contratan» un producto para progresar en una situación, no para tener sus características.

## Por qué importa

El trabajo describe la situación y el progreso buscado, y admite soluciones muy distintas; el rol o la edad no. Cambia la unidad con que se piensa a quien usa el producto: en lugar de «los estudiantes de primer año» (un segmento demográfico que no dice qué hacen), se piensa en «quien se acerca al plazo sin saber si su borrador se guardó». Eso abre el espacio de soluciones y apunta al problema real.

## Cómo funciona

[SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md) da una formulación con tres partes: una **circunstancia** («cuando se acerca el plazo y no estoy segura de que mi borrador se guardó»), un **deseo** («quiero confirmar que mi trabajo está a salvo») y un **resultado** («para dejar de pensar en ello»). La formulación **no nombra una solución**: puede resolverse con un indicador de guardado, un correo de confirmación o un recibo.

Un buen trabajo es lo bastante específico para distinguir situaciones y lo bastante abstracto para admitir soluciones. Además tiene **contextos que lo alteran**: el mismo trabajo se hace distinto desde un móvil con mala conexión que desde un escritorio. Por eso el expediente de la plataforma conserva, por cada trabajo, la circunstancia, el deseo, el resultado y el contexto, junto al mapa de actores (rol, qué decide o veta, qué evidencia aceptaría, qué teme, qué contexto habita).

La consecuencia metodológica es desagregar: ninguna afirmación de mejora se publica sin su desagregación por los contextos declarados. [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md) describe un riesgo concreto: la opción «ganadora» empeora la experiencia de un grupo específico porque se decidió con la métrica agregada y composiciones distintas por opción; la corrección es desagregar por contextos y comparar con la misma mezcla. Y otro: la persona-ficha que no se parece a nadie entrevistado porque se construyó con promedios o intuición; se construye desde observaciones concretas declarando el origen de cada rasgo.

## Ejemplo

Trabajo: «Cuando se acerca el plazo y no estoy segura de que mi borrador se guardó, quiero confirmar que mi trabajo está a salvo, para dejar de pensar en ello». Actor: estudiante. Contexto: entrega desde móvil con conexión inestable. Soluciones posibles: un indicador visible de guardado, un correo de recibo, un historial. Cualquiera se evalúa por si cumple el trabajo. (Ejemplo de [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md).)

## Errores y confusiones comunes

- **Describir segmentos demográficos en lugar de trabajos.**
- **Incluir la solución en el trabajo**: «quiero un botón de guardar» no es un trabajo.
- **Decidir con la métrica agregada** y empeorar a un grupo.
- **Personas-ficha inventadas** sin observación detrás.

## Límites y cuándo no aplica

El marco no ayuda a medir ni a priorizar por sí solo; hay que combinarlo con evidencia y tamaño de oportunidad. Algunos productos sirven a trabajos emocionales o sociales difíciles de observar. Los trabajos se descubren con entrevistas sobre episodios pasados; si la muestra es pequeña, son hipótesis.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Progreso](../p/progreso.md), [Actores y cadena de decisión](../a/actores-y-cadena-de-decision.md), [Agregación y segmentos](../a/agregacion-y-segmentos.md), [Contextos](../c/contextos.md), [Personas y promedios](../p/personas-y-promedios.md).
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

[↑ Glosario](../../README.md) · [← Trabajo venenoso](./trabajo-venenoso.md) · [Traceability →](./traceability.md)
