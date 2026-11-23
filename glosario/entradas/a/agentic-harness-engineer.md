# Agentic Harness Engineer

[↑ Glosario](../../README.md) · [← Agentic engineering](./agentic-engineering.md) · [Agilidad criptográfica →](./agilidad-criptografica.md)

> **Tipo:** rol profesional · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** Rutas por rol · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Diseña y opera el entorno que rodea a un agente de IA —contexto, herramientas, permisos, bucles, evaluación y recuperación— para que su trabajo sea verificable, acotado y reversible, en lugar de depender de que el modelo «se porte bien».

Guía completa: [Agentic Harness Engineer](../../../roles/agentic-harness-engineer.md).

## Por qué importa

Un agente no es sólo un modelo: es un modelo dentro de un **harness**. El harness decide qué ve el modelo en cada paso (instrucciones del repositorio, archivos, resultados previos), qué puede hacer (herramientas con esquema, permisos y efectos acotados), cuándo termina (criterios de parada y presupuesto), cómo se comprueba su trabajo (pruebas, linters y evaluaciones externas al propio agente) y cómo se vuelve atrás cuando falla. Como el componente central es probabilístico, la fiabilidad no sale de pedirle al modelo que sea cuidadoso: sale de andamiaje determinista alrededor de él.

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

Guía de rol: [Agentic Harness Engineer](../../../roles/agentic-harness-engineer.md).

**Se define o se desarrolla en:**

- [SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-250 — Health, readiness y shutdown ordenado](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de la ruta están en la sección «Fuentes» de la guía de rol enlazada.

---

[↑ Glosario](../../README.md) · [← Agentic engineering](./agentic-engineering.md) · [Agilidad criptográfica →](./agilidad-criptografica.md)
