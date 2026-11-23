# Regla de las tres condiciones

[↑ Glosario](../../README.md) · [← Regla de dependencia](./regla-de-dependencia.md) · [Regla de negocio →](./regla-de-negocio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Datos privados, contenido no confiable y canal de salida en un mismo agente.

Definición de trabajo de [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md).

## Por qué importa

La clase donde se define, [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md), existe con este propósito: la clase existe para que trates **costo, latencia y seguridad** de un sistema con LLM como restricciones de diseño que se calculan y se miden, no como propiedades que aparecen sueltas al final.

## Cómo funciona

Según [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md):

Estima el costo y el p95 de un flujo de tu sistema con tus números de pasos y contexto, y compáralos con tu presupuesto. Evalúa las capacidades del agente con la regla de las tres condiciones. Si viola, propón la separación mínima y mide qué usos legítimos se pierden. Escribe la prueba del documento hostil.

## Ejemplo

Caso medido en la sección «Seguridad: la regla de las tres condiciones» de [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md):

Un modelo trata todo el contexto como texto: una instrucción en un documento tiene la misma forma que una del operador. La inyección de prompt, directa o indirecta, es el riesgo principal de OWASP para estas aplicaciones. Simon Willison propone un marco: un agente es peligroso cuando reúne **tres condiciones**: acceso a **datos privados**, exposición a **contenido no confiable** (correos, páginas, documentos de terceros) y capacidad de **comunicar hacia fuera** (enviar un mensaje, hacer una petición). Con las tres, un texto hostil puede pedir al agente que envíe los datos privados.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md)) son: Las unidades de costo son supuestos y no precios; la latencia es una distribución sintética; las probabilidades de obediencia, de éxito del atacante y de fatiga humana son supuestos del autor; no se atacó ningún modelo real ni se midió ningún proveedor. El siguiente paso, `SE-599`, es un taller: elegir un patrón agéntico para tareas distintas y degradarlo con un interruptor cuando el proveedor falla.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contenido no confiable](../c/contenido-no-confiable.md), [Agente](../a/agente.md), [Caché de prefijo](../c/cache-de-prefijo.md), [Cola larga](../c/cola-larga.md), [Inyección de prompt](../i/inyeccion-de-prompt.md), [Percentil 95](../p/percentil-95.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Regla de dependencia](./regla-de-dependencia.md) · [Regla de negocio →](./regla-de-negocio.md)
