# Chaos & Resilience Engineer

[↑ Glosario](../../README.md) · [← Chaining](./chaining.md) · [Checksum →](./checksum.md)

> **Tipo:** rol profesional · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** Rutas por rol · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Comprueba con experimentos controlados que un sistema sigue cumpliendo su tarea útil cuando algo falla: formula la hipótesis, acota el daño, inyecta el fallo, observa y corrige lo que la evidencia refute.

Guía completa: [Chaos & Resilience Engineer](../../../roles/chaos-resilience-engineer.md).

## Por qué importa

Los sistemas distribuidos fallan por partes: una dependencia se vuelve lenta, una réplica diverge, un reintento amplifica una caída, una zona se pierde. Las pruebas unitarias y de integración rara vez ejercitan esas condiciones, y los diagramas de arquitectura prometen tolerancia que nadie ha comprobado. La ingeniería del caos propone una respuesta empírica: tratar cada promesa de resiliencia como una hipótesis y buscar activamente la evidencia que la refute, de forma controlada y antes de que el fallo llegue solo.

## Cómo funciona

La guía conecta cada responsabilidad del puesto con partes y clases concretas, con evidencia y proyecto integrador; el recorrido está en la guía enlazada.

## Ejemplo

La guía incluye un escenario de fallo, métricas con sus trampas y un plan 30/60/90; ábrela para el ejemplo completo.

## Errores y confusiones comunes

Un rol no es un cargo ni una lista de herramientas: la guía separa responsabilidades, límites y roles adyacentes.

## Límites y cuándo no aplica

Una ruta profesional no elimina prerrequisitos: las clases siguen la secuencia del programa y la guía solo ordena las de apoyo.

## Relación con otros conceptos

- **Prerrequisito:** las partes del núcleo de la guía.
- **Ver también:** las demás guías del [índice de rutas](../../../roles/README.md).
- **Se confunde con:** un cargo de empresa; la guía describe una ruta de aprendizaje, no un puesto.

## Dónde se enseña

Guía de rol: [Chaos & Resilience Engineer](../../../roles/chaos-resilience-engineer.md).

**Se define o se desarrolla en:**

- [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.
- [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.
- [SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.
- [SE-391 — Consenso, elección y coordinación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.
- [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.
- [SE-394 — Caos controlado y pruebas de distribución](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de la ruta están en la sección «Fuentes» de la guía de rol enlazada.

---

[↑ Glosario](../../README.md) · [← Chaining](./chaining.md) · [Checksum →](./checksum.md)
