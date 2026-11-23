# Aislamiento del sistema operativo

[↑ Glosario](../../README.md) · [← Aislamiento de datos](./aislamiento-de-datos.md) · [Ajuste →](./ajuste.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Restricción impuesta por el sistema operativo a los procesos, independiente de las reglas del agente.

Definición de trabajo de [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md).

## Por qué importa

En [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), el tema «Aislamiento del sistema operativo» importa porque una segunda barrera cuando la regla falla.

## Cómo funciona

Según [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* hace el inventario de las doce herramientas de su agente y anota para cada una la autoridad en sus cuatro dimensiones. Para corregir errores, el agente necesita leer, buscar, listar, escribir en el espacio de trabajo, confirmar cambios y consultar la base de pruebas; el resto —borrar archivos, ejecutar la shell sin restricciones, enviar correos, empujar a un remoto, escribir en la base real y abrir direcciones externas— se quita de la tarea. La escritura se confina al directorio del proyecto y las órdenes de shell restantes (pruebas, `git status`) se permiten con análisis de segmentos y confinamiento de rutas, con la denegación explícita de `curl`, `wget` y `rm`.

Según [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md):

Porque una orden es una cadena, y la misma cadena puede encadenar otras órdenes, sustituir resultados o apuntar fuera del espacio de trabajo. Una lista de permitidos es útil como parte de una política que analiza segmentos y rutas y se acompaña de aislamiento del sistema operativo; sola, deja pasar lo que el prefijo no revela.

## Ejemplo

Ejemplo de [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* hace el inventario de las doce herramientas de su agente y anota para cada una la autoridad en sus cuatro dimensiones. Para corregir errores, el agente necesita leer, buscar, listar, escribir en el espacio de trabajo, confirmar cambios y consultar la base de pruebas; el resto —borrar archivos, ejecutar la shell sin restricciones, enviar correos, empujar a un remoto, escribir en la base real y abrir direcciones externas— se quita de la tarea.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md)) son:

- **El agente ejecuta algo no previsto con una orden permitida** — causa: comprobación por prefijo. Corrección: analizar segmentos y sustituciones antes de decidir.
- **Lee archivos fuera del proyecto** — causa: rutas sin resolver. Corrección: normalizar y comparar con la ruta del espacio de trabajo, rechazar el byte nulo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una lista de permitidos es útil como parte de una política que analiza segmentos y rutas y se acompaña de aislamiento del sistema operativo; sola, deja pasar lo que el prefijo no revela. ([SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sistema operativo](../s/sistema-operativo.md), [Agente](./agente.md), [Proceso](../p/proceso.md), [Regla](../r/regla.md), [Autoridad de un agente](./autoridad-de-un-agente.md), [Confinamiento](../c/confinamiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Saltzer y Schroeder](https://doi.org/10.1109/PROC.1975.9939) — mínimo privilegio y protección de la información; autoridad: Proceedings of the IEEE, 1975.
- [Claude Code: permisos](https://code.claude.com/docs/en/permissions) — orden de evaluación, órdenes compuestas y fragilidad de los patrones sobre argumentos; autoridad: documentación de Anthropic.
- [Claude Code: aislamiento (sandbox)](https://code.claude.com/docs/en/sandboxing) — aislamiento de sistema de archivos y red a nivel del sistema operativo; autoridad: documentación de Anthropic.
- [OWASP Top 10 para aplicaciones con LLM](https://genai.owasp.org/llm-top-10/) — riesgos, entre ellos la agencia excesiva; autoridad: proyecto OWASP GenAI.

---

[↑ Glosario](../../README.md) · [← Aislamiento de datos](./aislamiento-de-datos.md) · [Ajuste →](./ajuste.md)
