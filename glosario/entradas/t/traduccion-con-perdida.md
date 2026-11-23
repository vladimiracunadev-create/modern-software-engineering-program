# Traducción con pérdida

[↑ Glosario](../../README.md) · [← Traducción](./traduccion.md) · [Tráfico norte-sur y este-oeste →](./trafico-norte-sur-y-este-oeste.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Conversión en la que dos valores de origen distintos producen el mismo valor de destino.

Definición de trabajo de [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md).

## Por qué importa

La clase donde se define, [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md), existe con este propósito: la clase existe para que protejas el modelo de tu sistema de las rarezas de otro que no controlas: aprenderás a medir qué ocurre cuando los datos de un sistema externo entran sin traducir (cuántos registros rompen el sistema y cuántos entran con otro significado), cuántos puntos de tu código se ven afectados cuando el proveedor cambia un nombre y cuánta información pierde una traducción que resume varios códigos en uno.

## Cómo funciona

[SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md):

El equipo de la plataforma crea el módulo `integracion/academico/` con tres archivos. **`mapa.md`** documenta cada campo (nombre externo, tipo, unidad, nombre interno y regla), los nueve estados y su traducción a los cuatro conceptos de la plataforma, y qué se conserva. **`traducir.py`** es la única parte del código que importa el esquema externo: produce objetos del dominio, aparta a la cuarentena (con motivo) lo que no puede traducir y guarda siempre el código de estado original junto al traducido.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md)) son:

- **El sistema falla en muchas funciones cuando el proveedor cambia** — causa: el nombre externo se usa en todo el código. Corrección: capa de traducción como único lugar que conoce el modelo externo.
- **Valores absurdos en un cálculo** — causa: datos externos aceptados sin validar la invariante. Corrección: validar rango y unidad en la frontera.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún sistema académico, API ni dato real: los formatos y sus proporciones, el mapa de nueve a cuatro estados, las seis funciones y la escala lineal son construcciones del autor, y los resultados no se extrapolan a ningún proveedor. Las reglas de normalización se escribieron mirando estos mismos formatos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Origen](../o/origen.md), [Valor](../v/valor.md), [Capa anticorrupción](../c/capa-anticorrupcion.md), [Conformista](../c/conformista.md), [Contexto delimitado](../c/contexto-delimitado.md), [Cuarentena](../c/cuarentena.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

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

[↑ Glosario](../../README.md) · [← Traducción](./traduccion.md) · [Tráfico norte-sur y este-oeste →](./trafico-norte-sur-y-este-oeste.md)
