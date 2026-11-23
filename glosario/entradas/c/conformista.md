# Conformista

[↑ Glosario](../../README.md) · [← Conformidad](./conformidad.md) · [Confusor →](./confusor.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Relación en la que un sistema adopta tal cual el modelo de otro.

Definición de trabajo de [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md).

## Por qué importa

La clase donde se define, [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md), existe con este propósito: la clase existe para que protejas el modelo de tu sistema de las rarezas de otro que no controlas: aprenderás a medir qué ocurre cuando los datos de un sistema externo entran sin traducir (cuántos registros rompen el sistema y cuántos entran con otro significado), cuántos puntos de tu código se ven afectados cuando el proveedor cambia un nombre y cuánta información pierde una traducción que resume varios códigos en uno.

## Cómo funciona

Según [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md):

La capa tiene un dueño (el equipo que integra con el proveedor), un lugar (un módulo o un servicio) y pruebas propias con ejemplos reales del proveedor, incluidas sus rarezas. No es gratuita: añade código, retrasa los cambios que sí quieres adoptar y puede esconder semánticas que convendría discutir con el proveedor. Hay relaciones en que no hace falta: si el modelo externo es bueno y estable, se puede adoptar tal cual (**conformista**); si dos equipos cooperan estrechamente, pueden compartir un modelo (**núcleo compartido**). La capa se justifica cuando el modelo ajeno es peor que el propio, cambia sin avisar o no se puede influir.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md):

El equipo de la plataforma crea el módulo `integracion/academico/` con tres archivos. **`mapa.md`** documenta cada campo (nombre externo, tipo, unidad, nombre interno y regla), los nueve estados y su traducción a los cuatro conceptos de la plataforma, y qué se conserva. **`traducir.py`** es la única parte del código que importa el esquema externo: produce objetos del dominio, aparta a la cuarentena (con motivo) lo que no puede traducir y guarda siempre el código de estado original junto al traducido.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md)) son:

- **El sistema falla en muchas funciones cuando el proveedor cambia** — causa: el nombre externo se usa en todo el código. Corrección: capa de traducción como único lugar que conoce el modelo externo.
- **Valores absurdos en un cálculo** — causa: datos externos aceptados sin validar la invariante. Corrección: validar rango y unidad en la frontera.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Hay relaciones en que no hace falta: si el modelo externo es bueno y estable, se puede adoptar tal cual (**conformista**); si dos equipos cooperan estrechamente, pueden compartir un modelo (**núcleo compartido**). ([SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Relación](../r/relacion.md), [Capa anticorrupción](./capa-anticorrupcion.md), [Contexto delimitado](./contexto-delimitado.md), [Cuarentena](./cuarentena.md), [Traducción con pérdida](../t/traduccion-con-perdida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft: patrón Anti-Corruption Layer](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) — capa que traduce entre subsistemas con semánticas distintas; autoridad: documentación de Microsoft.
- [Evans, «Domain-Driven Design Reference»](https://www.domainlanguage.com/ddd/reference/) — capa anticorrupción y otras relaciones entre contextos; autoridad: autor del libro.
- [Fowler, «Bounded Context»](https://martinfowler.com/bliki/BoundedContext.html) — cada contexto con su modelo y vocabulario; autoridad: autor del texto.
- [EIP: Message Translator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageTranslator.html) — conversión entre formatos de mensaje; autoridad: autores del libro.
- [RFC 3339: fechas y horas en Internet](https://www.rfc-editor.org/rfc/rfc3339) — formato de fecha sin ambigüedad; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Conformidad](./conformidad.md) · [Confusor →](./confusor.md)
