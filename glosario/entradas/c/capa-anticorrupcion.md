# Capa anticorrupción

[↑ Glosario](../../README.md) · [← Capa](./capa.md) · [Capa de acceso al hardware →](./capa-de-acceso-al-hardware.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

La **capa anticorrupción** es un traductor entre dos modelos que impide que el modelo de un sistema se imponga al del otro. Es un concepto del diseño orientado al dominio. [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) la usa en la modernización de un sistema antiguo; [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) la define como la traducción entre contextos que protege al modelo propio; [SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md) la describe como el componente que traduce entre el modelo de otro sistema y el propio, y es el único que conoce ambos.

## Por qué importa

Un sistema antiguo tiene convenciones propias: textos con coma decimal, estados de una letra con significado implícito, fechas de dos dígitos, nulos y espacios que significan cosas distintas. Si el sistema nuevo habla ese lenguaje directamente, lo hereda, y la modernización reproduce las rarezas del pasado. La decisión que cambia es dónde vive la traducción: en un lugar único y explícito, no repartida por todo el código nuevo.

## Cómo funciona

El mecanismo tiene dos partes. Primero, **aislamiento**: solo la capa conoce los dos vocabularios; el resto del sistema nuevo ve únicamente el modelo limpio. [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) lo muestra con una función de seis líneas que convierte `entrega_id` en `id`, `estudiante` en `student`, `vence_en` en `due` y, lo más importante, el estado textual en un booleano («recibida» verdadero, «pendiente» falso). Si mañana aparece un estado «en revisión», se decide en un solo sitio si cuenta como entregada.

Segundo, **decisiones semánticas ante lo raro**. [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) pide que una buena capa no lance excepciones ante datos extraños: los clasifica (traducido, traducido con advertencia, no traducible) y envía lo no traducible a una cuarentena para revisión. Qué hacer con una nota vacía, un estado desconocido o una fecha imposible es una decisión de negocio que la capa vuelve explícita.

## Ejemplo

Un sistema legado entrega una calificación como el texto `"8,5"` y un estado `"R"`. La capa produce `grade = 8.5` y `received = true`. Si llega `"R "` con espacio o una fecha `31/02`, no se detiene el flujo: el registro se marca con advertencia o va a cuarentena, y el equipo lo revisa sin que el sistema nuevo tenga que conocer el formato antiguo. Ilustración basada en los casos de [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) y [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md).

## Errores y confusiones comunes

- **El sistema nuevo adopta las rarezas del antiguo** ([SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md)): no hay capa de traducción; se corrige introduciéndola con cuarentena.
- **Dejar que la capa lance excepciones** ante datos raros: detiene el flujo en vez de clasificar.
- **Dispersar la traducción** en varios módulos: se pierde la propiedad esencial de que un solo componente conoce ambos modelos.
- **Confundirla con una simple conversión de formato**: traduce también significados.

## Límites y cuándo no aplica

Añade un componente que mantener y un salto más en el camino de los datos. Si ambos sistemas comparten ya el mismo modelo, o el externo es tan estable y limpio que adoptarlo no daña al propio, la capa sobra; en la relación entre contextos, aceptar el modelo ajeno tal cual es la opción llamada conformista. Tampoco corrige problemas de calidad del origen: los hace visibles y los aísla.

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
