# Ventana de deprecación

[↑ Glosario](../../README.md) · [← Ventana de deduplicación](./ventana-de-deduplicacion.md) · [Ventana de exposición →](./ventana-de-exposicion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Periodo entre el aviso de retirada de una versión y su retirada efectiva.

Definición de trabajo de [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md): Periodo entre el aviso de retirada de una característica y su eliminación efectiva.

## Por qué importa

En [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), el tema «Ventana de deprecación» importa porque equilibra el costo de mantener dos versiones con el de romper.

## Cómo funciona

Según [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), en la sección «Ventana de deprecación»:

Retirar una versión antigua exige un aviso, un plazo y una forma de saber quién sigue usándola. El plazo equilibra dos costos: mantener dos versiones (que crece con la ventana) y romper a quien no migró (que decrece con ella, pero no llega a cero porque algunos nunca migrarán por sí solos). Las cabeceras de deprecación y retirada de los protocolos de red permiten anunciar el plazo a los clientes en cada respuesta. La fecha de retirada final es una decisión de producto con aviso, no un cálculo.

## Ejemplo

Ejemplo de [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md) (sección «Caso conductor»):

El componente `tarifas` cierra la [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md) con un plan de evolución: un verificador de firmas como filtro, contratos de ocho consumidores, un redondeo histórico conservado con nombre, una ventana de deprecación estimada y las tres fases de cada cambio. Conserva los artefactos de `SE-301` a `SE-311`. La [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md) sube de nivel y se pregunta qué restricciones arquitectónicas condicionan lo que un componente puede evolucionar. Cambia después una sola decisión, la fecha de retirada de la versión antigua, y observa cuántos consumidores quedan sin migrar.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La ventana de deprecación termina y quedan clientes activos** — causa: parte de los consumidores no migra sola. Corrección: medir quién usa lo viejo, contactar directamente y decidir el corte con un responsable. ([SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md)) son: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final. Se ejecutaron tres análisis con consumidores y clientes sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún consumidor real, ningún tráfico real ni ninguna infraestructura de despliegue; los ocho consumidores, los 500 clientes, los tiempos de migración y los contratos son construcciones del autor. La siguiente parte pasa a la arquitectura y pregunta qué restricciones condicionan lo que un sistema puede evolucionar.

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
