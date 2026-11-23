# Votación

[↑ Glosario](../../README.md) · [← Volumen](./volumen.md) · [Vulnerabilidad →](./vulnerabilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Ejecución repetida de la misma tarea y decisión por mayoría.

Definición de trabajo de [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md).

## Por qué importa

En [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md), el tema «Votación» importa porque compra calidad solo si los errores son independientes.

## Cómo funciona

Según [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md):

La votación ejecuta la misma tarea varias veces y toma la mayoría. Con cinco muestras que aciertan el 80 % de forma independiente, la mayoría acierta el 94,0 %. Pero si en la mitad de las ejecuciones las cinco muestras comparten el mismo sesgo (todas aciertan o todas fallan juntas, porque la entrada es ambigua o el prompt induce el mismo error), la mayoría acierta el 87,4 %. El voto reduce el ruido aleatorio y no toca el sesgo sistemático. Para que sea útil, las muestras deben variar de verdad (temperatura, redacción del prompt, modelo distinto) y hay que medir la correlación en datos reales; si no, se paga cinco veces por la misma respuesta.

Según [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md):

No: reduce el tiempo de reloj. Las llamadas se pagan igual y la votación las multiplica. El beneficio es de latencia, y a veces de calidad.

## Ejemplo

Ejemplo de [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md) (sección «Preguntas frecuentes»):

No: reduce el tiempo de reloj. Las llamadas se pagan igual y la votación las multiplica. El beneficio es de latencia, y a veces de calidad.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md)) son: El éxito por paso, la detección de la puerta, el acierto por muestra y la correlación son parámetros del autor; el enrutador usa cuatro intenciones y plantillas escritas a mano; los tiempos paralelos usan esperas de sueño. No se midió ningún modelo de lenguaje ni ningún proveedor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tarea](../t/tarea.md), [Cobertura con umbral](../c/cobertura-con-umbral.md), [Encadenado](../e/encadenado.md), [Enrutador](../e/enrutador.md), [Puerta](../p/puerta.md), [Seccionamiento](../s/seccionamiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), [SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), [SE-531](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-531-comunicacion-facilitacion-y-conflicto/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Volumen](./volumen.md) · [Vulnerabilidad →](./vulnerabilidad.md)
