# Cuarentena

[↑ Glosario](../../README.md) · [← Cuantización](./cuantizacion.md) · [Cuasi-identificador →](./cuasi-identificador.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Destino de los registros que no se pueden traducir sin ambigüedad, con el motivo del rechazo.

Definición de trabajo de [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md): Estado en el que una prueba se ejecuta sin bloquear, con responsable y fecha de salida.
- En [SE-558 — Generación de pruebas, documentación y migraciones](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md): Conjunto de filas apartadas durante una migración por no cumplir la validación, conservadas sin cambios.

## Por qué importa

En [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md), el tema «Cuarentena» importa porque lo ambiguo no se adivina: se aparta con un motivo.

## Cómo funciona

Según [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md), en la sección «Cuarentena»:

No todo se puede traducir sin ambigüedad. Una nota vacía no es una nota cero; `"N/P"` puede significar «no presentó» o «no procede»; una fecha `03/04/2026` es el 3 de abril o el 4 de marzo según una convención que el proveedor puede no haber declarado. Adivinar es fabricar datos. La política correcta es **apartar** el registro a una cuarentena con su motivo, contar cuántos hay por motivo y decidir con el dueño del dato si se añade una regla, se pide una aclaración o se descarta. La capa que rechaza en silencio es tan peligrosa como la que acepta todo; la cuarentena hace visible lo que no se pudo traducir.

## Ejemplo

Ejemplo de [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma crea el módulo `integracion/academico/` con tres archivos. **`mapa.md`** documenta cada campo (nombre externo, tipo, unidad, nombre interno y regla), los nueve estados y su traducción a los cuatro conceptos de la plataforma, y qué se conserva. **`traducir.py`** es la única parte del código que importa el esquema externo: produce objetos del dominio, aparta a la cuarentena (con motivo) lo que no puede traducir y guarda siempre el código de estado original junto al traducido. **`tests/`** contiene 30 registros reales anonimizados del proveedor, cada uno con su rareza, y una prueba de contrato que falla si el proveedor cambia un nombre.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Registros que desaparecen sin rastro** — causa: la capa rechaza en silencio. Corrección: cuarentena con motivo, conteo y alarma. ([SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md))
- **La capa crece sin control** — causa: hace más de traducir. Corrección: mantener solo traducción, validación y cuarentena. ([SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md))
- **Las pruebas en cuarentena se olvidan** — causa: sin responsable ni fecha. Corrección: responsable, fecha de revisión y criterio de salida. ([SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La capa que rechaza en silencio es tan peligrosa como la que acepta todo; la cuarentena hace visible lo que no se pudo traducir. ([SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ambigüedad](../a/ambiguedad.md), [Conjunto](./conjunto.md), [Estado](../e/estado.md), [Migración](../m/migracion.md), [Capa anticorrupción](./capa-anticorrupcion.md), [Condición de carrera](./condicion-de-carrera.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-558 — Generación de pruebas, documentación y migraciones](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), [SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md).

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

[↑ Glosario](../../README.md) · [← Cuantización](./cuantizacion.md) · [Cuasi-identificador →](./cuasi-identificador.md)
