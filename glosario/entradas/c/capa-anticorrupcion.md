# Capa anticorrupción

[↑ Glosario](../../README.md) · [← Capa](./capa.md) · [Capa de acceso al hardware →](./capa-de-acceso-al-hardware.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Traductor que impide que el modelo del sistema antiguo se imponga al del nuevo.

Definición de trabajo de [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-546 — DDD como lenguaje ubicuo y contexto para agentes](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md): Traducción entre contextos que protege al modelo propio.
- En [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md): Componente que traduce entre el modelo de otro sistema y el propio, y es el único que conoce ambos.

## Por qué importa

En [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), el tema «Capa anticorrupción» importa porque evita que el modelo antiguo se vuelva el nuevo.

En [SE-546 — DDD como lenguaje ubicuo y contexto para agentes](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md), el tema «Capa anticorrupción» importa porque evita que el modelo de otro contexto contamine el propio.

## Cómo funciona

Según [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), en la sección «Capa anticorrupción»:

El sistema antiguo tiene un modelo con sus propias convenciones: textos con coma decimal, estados de una letra con significados implícitos, fechas de dos dígitos, nulos y espacios que significan cosas distintas. Si el sistema nuevo habla ese lenguaje directamente, lo hereda. La **capa anticorrupción** (concepto del diseño orientado al dominio) es un traductor entre los dos modelos: expone al sistema nuevo un modelo limpio y se ocupa de convertir. Sus decisiones son semánticas: qué se hace con una nota vacía, con un estado desconocido, con una fecha imposible. Una buena capa **no lanza excepciones** ante datos raros: los clasifica (traducido, traducido con advertencia, no traducible) y envía lo no traducible a una cuarentena para revisión.

Según [SE-546 — DDD como lenguaje ubicuo y contexto para agentes](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md), en la sección «Capa anticorrupción»:

La **capa anticorrupción** es la traducción entre contextos que impide que el modelo de uno contamine al otro. En el laboratorio es una función de seis líneas que convierte `entrega_id` en `id`, `estudiante` en `student`, `vence_en` en `due` y, lo más importante, el estado textual en un booleano: «recibida» pasa a verdadero y «pendiente» a falso. La función es el único lugar donde se conocen ambos vocabularios. Si mañana la plataforma añade un estado «en revisión», se decide en un solo lugar si cuenta como entregada.

## Ejemplo

Ejemplo de [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo divide el módulo en cuatro rebanadas: consulta de nota (poco tráfico, lectura), cálculo de nota, cierre de acta y exportación. Empieza por la consulta: la fachada la envía al sistema nuevo al 5 % y copia el 100 % en sombra al antiguo para comparar; la regla de equivalencia compara la nota al décimo y estado traducido, e ignora la marca de tiempo. Antes de subir a 25 % exige 3 000 comparaciones sin diferencias, calculadas para detectar una tasa del 0,1 %.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El sistema nuevo adopta las rarezas del antiguo** — causa: no hay capa de traducción. Corrección: introducir una capa anticorrupción con cuarentena. ([SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **capa anticorrupción** es la traducción entre contextos que impide que el modelo de uno contamine al otro. ([SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](./componente.md), [Contextos](./contextos.md), [Modelo](../m/modelo.md), [Traducción](../t/traduccion.md), [Comparación en sombra](./comparacion-en-sombra.md), [Conformista](./conformista.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.
- [SE-546 — DDD como lenguaje ubicuo y contexto para agentes](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md), [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md), [SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Evans, «Domain-Driven Design Reference»](https://www.domainlanguage.com/ddd/reference/) — capa anticorrupción y otras relaciones entre contextos; autoridad: autor del libro.
- [Fowler, «StranglerFigApplication»](https://martinfowler.com/bliki/StranglerFigApplication.html) — el patrón de estrangulamiento; autoridad: autor del texto.
- [Microsoft Azure Architecture Center: Strangler Fig](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) — fachada y migración incremental; autoridad: documentación de Microsoft.
- [Microsoft Azure Architecture Center: Anti-corruption Layer](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) — traducción entre modelos; autoridad: documentación de Microsoft.
- [Fowler, «DarkLaunching»](https://martinfowler.com/bliki/DarkLaunching.html) — ejecutar con tráfico real sin exponer el resultado; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Capa](./capa.md) · [Capa de acceso al hardware →](./capa-de-acceso-al-hardware.md)
