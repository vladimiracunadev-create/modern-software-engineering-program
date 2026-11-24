# Cuarentena

[↑ Glosario](../../README.md) · [← Cuantización](./cuantizacion.md) · [Cuasi-identificador →](./cuasi-identificador.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

La **cuarentena** es, en el sentido principal del programa ([SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md)), el destino de los registros que no se pueden traducir sin ambigüedad, conservados con el motivo del rechazo. El término tiene otros sentidos en el programa, que esta entrada distingue:

- En [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) (pruebas): estado en el que una prueba se ejecuta sin bloquear la integración, con responsable y fecha de salida.
- En [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md) (desarrollo asistido por IA): conjunto de filas apartadas durante una migración por no cumplir la validación, conservadas sin cambios.

Los tres comparten la idea de apartar algo sin descartarlo ni dejarlo pasar, con registro de por qué.

## Por qué importa

Ante un dato ambiguo hay tres respuestas malas: aceptarlo adivinando, rechazarlo en silencio o romper el flujo entero. [SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md) lo dice así: adivinar es fabricar datos. La cuarentena es la cuarta respuesta, y la que permite decidir con información. La decisión que cambia es tratar lo no traducible como un resultado esperado del proceso, con un destino y un responsable.

## Cómo funciona

En [SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md), una nota vacía no es una nota cero; `"N/P"` puede significar «no presentó» o «no procede»; una fecha `03/04/2026` es el 3 de abril o el 4 de marzo según una convención que el proveedor puede no haber declarado. La política correcta es **apartar** el registro a una cuarentena con su motivo, **contar** cuántos hay por motivo y **decidir** con el dueño del dato si se añade una regla, se pide una aclaración o se descarta. La cuarentena hace visible lo que no se pudo traducir, y por eso la capa que rechaza en silencio es tan peligrosa como la que acepta todo.

En pruebas ([SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md)), una prueba inestable se pone en cuarentena para que no bloquee a todos, pero con responsable, fecha de revisión y criterio de salida; sin eso se olvida. En migraciones ([SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md)), las filas que no cumplen la validación se apartan sin modificarse para revisarlas después.

## Ejemplo

Una capa recibe filas de un sistema antiguo. Una fila trae `"N/P"` en la nota. La capa no la traduce: la envía a la cuarentena con el motivo «nota ambigua». Al final del día se cuenta: 14 por «nota ambigua», 3 por «fecha imposible». Con el dueño del dato se añade la regla correspondiente y se reprocesan. Ejemplo ilustrativo del flujo de [SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md).

## Errores y confusiones comunes

- **Registros que desaparecen sin rastro**: la capa rechaza en silencio; se corrige con cuarentena con motivo, conteo y alarma ([SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md)).
- **La capa crece sin control**: hace más que traducir; debe limitarse a traducción, validación y cuarentena.
- **Las pruebas en cuarentena se olvidan**: sin responsable ni fecha; se corrige con responsable, fecha de revisión y criterio de salida ([SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md)).
- **Tratar la cuarentena como basurero**: si nadie la revisa, equivale a descartar.

## Límites y cuándo no aplica

La cuarentena solo vale si alguien la revisa; sin conteo, alarma y dueño, es una pérdida disfrazada. No resuelve la ambigüedad, solo la aplaza con evidencia. Para datos cuyo significado es inequívoco, o cuyo volumen ambiguo sea cero, no hace falta. Y en pruebas, mantener demasiadas en cuarentena oculta una regresión real.

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
