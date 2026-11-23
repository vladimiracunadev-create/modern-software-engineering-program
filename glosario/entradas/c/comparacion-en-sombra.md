# Comparación en sombra

[↑ Glosario](../../README.md) · [← Comparación diferencial](./comparacion-diferencial.md) · [Comparación pareada →](./comparacion-pareada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Ejecución del sistema nuevo con una copia del tráfico real, sin servir su respuesta, para compararla con la del antiguo.

Definición de trabajo de [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md).

## Por qué importa

En [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), el tema «Comparación en sombra» importa porque detecta diferencias antes de servir a nadie.

## Cómo funciona

Según [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), en la sección «Comparación en sombra»:

Antes de servir tráfico real desde el sistema nuevo, se le puede enviar una **copia** de cada petición y comparar su respuesta con la del antiguo, sin que la persona vea la respuesta nueva. La técnica (lanzamiento oscuro, ejecución en paralelo) detecta diferencias sin exponer a nadie, con tres cautelas. Los efectos secundarios no deben duplicarse: la copia en sombra no puede escribir en la base real ni enviar correos. La comparación debe tener una **regla de equivalencia** (qué diferencias importan: los décimos de una nota sí, el orden de los campos o la hora de generación no).

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo divide el módulo en cuatro rebanadas: consulta de nota (poco tráfico, lectura), cálculo de nota, cierre de acta y exportación. Empieza por la consulta: la fachada la envía al sistema nuevo al 5 % y copia el 100 % en sombra al antiguo para comparar; la regla de equivalencia compara la nota al décimo y estado traducido, e ignora la marca de tiempo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md)) son:

- **El corte se pospone una y otra vez** — causa: el paso es demasiado grande para verificarse. Corrección: dividir en rebanadas con retroceso independiente.
- **La sombra no muestra diferencias y hay error en producción** — causa: la ventana no incluye el tráfico raro. Corrección: elegir la ventana por calendario y reproducir tráfico grabado.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Ejecuta la comparación en sombra durante cuatro semanas en las que no hay cierre y observa que no hay diferencias. ([SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa anticorrupción](./capa-anticorrupcion.md), [Estrangulamiento](../e/estrangulamiento.md), [Rama por abstracción](../r/rama-por-abstraccion.md), [Rebanada](../r/rebanada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «StranglerFigApplication»](https://martinfowler.com/bliki/StranglerFigApplication.html) — el patrón de estrangulamiento; autoridad: autor del texto.
- [Microsoft Azure Architecture Center: Strangler Fig](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) — fachada y migración incremental; autoridad: documentación de Microsoft.
- [Microsoft Azure Architecture Center: Anti-corruption Layer](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) — traducción entre modelos; autoridad: documentación de Microsoft.
- [Fowler, «DarkLaunching»](https://martinfowler.com/bliki/DarkLaunching.html) — ejecutar con tráfico real sin exponer el resultado; autoridad: autor del texto.
- [Fowler, «FeatureToggle»](https://martinfowler.com/bliki/FeatureToggle.html) — banderas de funcionalidad y su costo; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Comparación diferencial](./comparacion-diferencial.md) · [Comparación pareada →](./comparacion-pareada.md)
