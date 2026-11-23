# Regla de permisos

[↑ Glosario](../../README.md) · [← Regla de negocio](./regla-de-negocio.md) · [Regla de reserva →](./regla-de-reserva.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Condición sobre una acción que decide si procede, se pregunta o se bloquea.

Definición de trabajo de [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md).

## Por qué importa

La clase donde se define, [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), existe con este propósito: la clase existe para que dejes de describir a un agente por lo que sabe y empieces a describirlo por lo que puede hacer.

## Cómo funciona

Según [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md):

Las reglas de permisos actúan sobre lo que el agente intenta hacer a través de sus herramientas; el aislamiento a nivel del sistema operativo actúa sobre lo que los procesos pueden hacer, sea cual sea quien los lanzó. Claude Code documenta un aislamiento del sistema de archivos y de la red para las órdenes de shell, implementado con las primitivas del sistema operativo (por ejemplo, Seatbelt en macOS y bubblewrap en Linux y WSL2), independiente de las reglas. Las dos barreras fallan de forma distinta: la regla se equivoca por un patrón mal escrito, el aislamiento por una configuración demasiado abierta, y por eso se usan juntas. El aislamiento no cubre las herramientas que no pasan por la shell ni lo que ocurre dentro de los dominios permitidos.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* hace el inventario de las doce herramientas de su agente y anota para cada una la autoridad en sus cuatro dimensiones. Para corregir errores, el agente necesita leer, buscar, listar, escribir en el espacio de trabajo, confirmar cambios y consultar la base de pruebas; el resto —borrar archivos, ejecutar la shell sin restricciones, enviar correos, empujar a un remoto, escribir en la base real y abrir direcciones externas— se quita de la tarea.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md)) son:

- **El agente ejecuta algo no previsto con una orden permitida** — causa: comprobación por prefijo. Corrección: analizar segmentos y sustituciones antes de decidir.
- **Lee archivos fuera del proyecto** — causa: rutas sin resolver. Corrección: normalizar y comparar con la ruta del espacio de trabajo, rechazar el byte nulo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: el motor de reglas es código real que analiza cadenas sin ejecutarlas, y el radio de daño y la acumulación son simulaciones con semilla fija. No se invocó ningún modelo, no se ejecutó ninguna orden del conjunto de prueba y no se observó ningún sistema real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Sobre](../s/sobre.md), [Aislamiento del sistema operativo](../a/aislamiento-del-sistema-operativo.md), [Autoridad de un agente](../a/autoridad-de-un-agente.md), [Confinamiento](../c/confinamiento.md), [Mínimo privilegio](../m/minimo-privilegio.md).
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

[↑ Glosario](../../README.md) · [← Regla de negocio](./regla-de-negocio.md) · [Regla de reserva →](./regla-de-reserva.md)
