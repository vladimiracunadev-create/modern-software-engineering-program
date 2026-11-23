# Ampliar, migrar y contraer

[↑ Glosario](../../README.md) · [← Amortizado](./amortizado.md) · [Amplificación de reintentos →](./amplificacion-de-reintentos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Estrategia de cambio en tres fases: añadir la forma nueva, mover a los consumidores y retirar la vieja.

Definición de trabajo de [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md).

## Por qué importa

En [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), el tema «Evolución por fases» importa porque ampliar, migrar y contraer evita el cambio simultáneo de todos.

## Cómo funciona

[SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md):

El equipo de `tarifas` entrega un paquete de evolución para sus cuatro cambios. Para cada uno aplica el filtro de firma y los contratos de los ocho consumidores, que cada equipo escribió en media hora. El parámetro de moneda obligatorio falla el filtro y se programa en tres fases: ampliar (la moneda es opcional con el valor actual), migrar (cada consumidor pasa la moneda, con seguimiento por una cabecera de uso) y contraer (se hace obligatoria cuando el 95 % migró y los demás recibieron aviso individual).

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md)) son:

- **Un cambio «compatible» rompe a un consumidor** — causa: el verificador comprueba solo la firma. Corrección: añadir contratos de consumidor.
- **La suite del proveedor no ve un cambio que rompe a otros** — causa: comprueba pocos campos. Corrección: ejecutar los contratos de los consumidores.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md)) son: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final. Se ejecutaron tres análisis con consumidores y clientes sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún consumidor real, ningún tráfico real ni ninguna infraestructura de despliegue; los ocho consumidores, los 500 clientes, los tiempos de migración y los contratos son construcciones del autor. La siguiente parte pasa a la arquitectura y pregunta qué restricciones condicionan lo que un sistema puede evolucionar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-311](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estrategia](../e/estrategia.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Contrato de consumidor](../c/contrato-de-consumidor.md), [Lector tolerante](../l/lector-tolerante.md), [Prueba de contrato dirigida por el consumidor](../p/prueba-de-contrato-dirigida-por-el-consumidor.md), [Ventana de deprecación](../v/ventana-de-deprecacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «Parallel Change»](https://martinfowler.com/bliki/ParallelChange.html) — ampliar, migrar y contraer; autoridad: Martin Fowler.
- [Semantic Versioning 2.0.0](https://semver.org/) — versionado para comunicar compatibilidad; autoridad: sus autores.
- [Hyrum's Law](https://www.hyrumslaw.com/) — usos no documentados de una interfaz; autoridad: Hyrum Wright.
- [Pact: documentación](https://docs.pact.io/) — pruebas de contrato dirigidas por el consumidor; autoridad: proyecto Pact.
- [Fowler, «Tolerant Reader»](https://martinfowler.com/bliki/TolerantReader.html) — lectores que toleran campos que no conocen; autoridad: Martin Fowler.

---

[↑ Glosario](../../README.md) · [← Amortizado](./amortizado.md) · [Amplificación de reintentos →](./amplificacion-de-reintentos.md)
