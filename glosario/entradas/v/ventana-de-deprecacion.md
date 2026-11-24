# Ventana de deprecación

[↑ Glosario](../../README.md) · [← Ventana de deduplicación](./ventana-de-deduplicacion.md) · [Ventana de exposición →](./ventana-de-exposicion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

La **ventana de deprecación** es el periodo entre el aviso de retirada de una versión (o característica) y su eliminación efectiva ([SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md)). Es el plazo que se da a quienes consumen una interfaz para migrar.

## Por qué importa

Equilibra el costo de mantener dos versiones con el de romper a quien no migró. Una ventana demasiado corta rompe a consumidores que no tuvieron tiempo; una demasiado larga obliga a mantener lo viejo indefinidamente. Cambia la planificación de la evolución de un contrato: retirar es una decisión con plazo, aviso y responsable.

## Cómo funciona

[SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md) dice que retirar una versión antigua exige **un aviso, un plazo y una forma de saber quién sigue usándola**. El plazo equilibra dos costos: **mantener dos versiones** (crece con la ventana) y **romper a quien no migró** (decrece con ella, pero **no llega a cero**, porque algunos consumidores nunca migrarán por sí solos). Hay, por tanto, una ventana razonable más allá de la cual alargar poco aporta.

Para comunicar el plazo, los protocolos de red ofrecen cabeceras de deprecación y retirada (`Deprecation` y `Sunset` en HTTP), que anuncian a los clientes la fecha. En la plataforma de entregas, la política es que los renombrados, los campos requeridos nuevos y las eliminaciones exigen versión mayor, aviso con esas cabeceras y una ventana mínima de 180 días ([SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md)).

El mecanismo para saber quién usa lo viejo es **medir el uso**: registrar qué versión llama cada cliente. [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) describe el síntoma que ocurre sin ello: la ventana termina y quedan clientes activos porque parte de los consumidores no migra sola. La corrección es **medir quién usa lo viejo, contactar directamente y decidir el corte con un responsable**. En [SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), el componente `tarifas` cierra la parte con un plan de evolución que incluye una ventana de deprecación estimada, contratos de ocho consumidores y las tres fases de cada cambio (añadir lo nuevo, migrar, retirar lo viejo).

## Ejemplo

Se anuncia que `GET /v1/entregas` se retira el 1 de diciembre. La respuesta incluye `Deprecation: true` y `Sunset: <fecha>`. Un panel muestra cuántas llamadas a `/v1` reciben cada semana y de qué clientes: de 12 clientes iniciales quedan 3 a un mes del corte. El equipo los contacta uno a uno y decide, con el responsable del producto, si aplaza o corta. (Ilustración del mecanismo de [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) y [SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md).)

## Errores y confusiones comunes

- **La ventana termina y quedan clientes activos**: no migran solos; corrección: medir, contactar y decidir con un responsable.
- **Avisar sin fecha ni cabeceras.**
- **No medir el uso de lo viejo.**
- **Fijar la ventana por calendario interno** sin considerar los ciclos de los consumidores (aplicaciones móviles instaladas).

## Límites y cuándo no aplica

Para interfaces internas con consumidores conocidos y coordinables, una ventana formal puede sobrar. Cuando la retirada es urgente por seguridad, se acorta o se omite a cambio de un costo de ruptura explícito. Los 180 días de la plataforma son una política de ese caso, no un estándar universal.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Característica](../c/caracteristica.md), [Versión](./version.md), [Ampliar, migrar y contraer](../a/ampliar-migrar-y-contraer.md), [Compatibilidad hacia adelante](../c/compatibilidad-hacia-adelante.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Compatibilidad hacia atrás y hacia adelante](../c/compatibilidad-hacia-atras-y-hacia-adelante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Semantic Versioning 2.0.0](https://semver.org/) — versionado para comunicar compatibilidad; autoridad: sus autores.
- [Hyrum's Law](https://www.hyrumslaw.com/) — usos no documentados de una interfaz; autoridad: Hyrum Wright.
- [Pact: documentación](https://docs.pact.io/) — pruebas de contrato dirigidas por el consumidor; autoridad: proyecto Pact.
- [Fowler, «Tolerant Reader»](https://martinfowler.com/bliki/TolerantReader.html) — lectores que toleran campos que no conocen; autoridad: Martin Fowler.
- [Fowler, «Parallel Change»](https://martinfowler.com/bliki/ParallelChange.html) — ampliar, migrar y contraer; autoridad: Martin Fowler.

---

[↑ Glosario](../../README.md) · [← Ventana de deduplicación](./ventana-de-deduplicacion.md) · [Ventana de exposición →](./ventana-de-exposicion.md)
