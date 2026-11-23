# Traducción

[↑ Glosario](../../README.md) · [← Trade-off](./trade-off.md) · [Traducción con pérdida →](./traduccion-con-perdida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Una **capa anticorrupción** es un componente cuya única tarea es traducir entre el modelo externo y el propio, y es el único lugar que conoce ambos. Traduce cuatro cosas: **nombres** (`cod_alumno` a `estudiante_id`), **formatos y unidades** (coma decimal, escala de 0 a 100, formatos de fecha), **vocabulario** (nueve códigos de estado a los cuatro conceptos de la plataforma) y **estructura** (un registro plano a un agregado).

Explicación de la sección «Traducción» de [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md).

## Por qué importa

En [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md), el tema «Traducción» importa porque convertir formato, unidad y vocabulario en un solo lugar.

En [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), el tema «Traducción» importa porque fuente, AST y bytecode

## Cómo funciona

Según [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md), en la sección «Traducción»:

Una **capa anticorrupción** es un componente cuya única tarea es traducir entre el modelo externo y el propio, y es el único lugar que conoce ambos. Traduce cuatro cosas: **nombres** (`cod_alumno` a `estudiante_id`), **formatos y unidades** (coma decimal, escala de 0 a 100, formatos de fecha), **vocabulario** (nueve códigos de estado a los cuatro conceptos de la plataforma) y **estructura** (un registro plano a un agregado). Todo lo que sale de ella ya es lenguaje del dominio propio y valida sus invariantes: una nota fuera de 1,0 a 7,0 no cruza la frontera. El resto del código no importa el módulo externo ni usa sus nombres.

## Ejemplo

Ejemplo de [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md) (sección «Ejemplo mínimo»):

El fragmento convierte una nota con coma y una en escala de 0 a 100. Antes de ejecutarlo, predice el resultado de `float` directo sobre cada una y el de la traducción.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El sistema falla en muchas funciones cuando el proveedor cambia** — causa: el nombre externo se usa en todo el código. Corrección: capa de traducción como único lugar que conoce el modelo externo. ([SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md))
- **No se puede devolver el dato al proveedor** — causa: la traducción resumió varios valores en uno. Corrección: conservar el original o ampliar la precisión. ([SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md))
- **La capa crece sin control** — causa: hace más de traducir. Corrección: mantener solo traducción, validación y cuarentena. ([SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Cómo leer la figura.** Cada barra es una traducción y su segmento coral es la parte de los 5 000 registros que no se recupera al volver; el verde azulado es la que sí. ([SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa anticorrupción](../c/capa-anticorrupcion.md), [Conformista](../c/conformista.md), [Contexto delimitado](../c/contexto-delimitado.md), [Cuarentena](../c/cuarentena.md), [Fixture](../f/fixture.md), [Instrumento](../i/instrumento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (41 clases más lo mencionan; las que más):

[SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md), [SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md), [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), [SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md), [SE-039](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md), [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md), [SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md).

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md).

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

[↑ Glosario](../../README.md) · [← Trade-off](./trade-off.md) · [Traducción con pérdida →](./traduccion-con-perdida.md)
