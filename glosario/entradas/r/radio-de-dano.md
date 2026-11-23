# Radio de daño

[↑ Glosario](../../README.md) · [← Qubit lógico y físico](../q/qubit-logico-y-fisico.md) · [Radio de efecto →](./radio-de-efecto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Conjunto de recursos alcanzables con una credencial comprometida.

Definición de trabajo de [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md): Conjunto de efectos que una acción errónea o maliciosa puede causar con la autoridad disponible.

## Por qué importa

En [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), el tema «Radio de daño» importa porque es la métrica que importa.

## Cómo funciona

Según [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), en la sección «Radio de daño»:

Con el modelo de 200 servicios en 5 segmentos y una credencial robada de un servicio elegido al azar (5 000 repeticiones, semilla 48): en una red plana de confianza interna, el atacante alcanza 200 servicios; con segmentación de red en cinco partes, 40; con credenciales limitadas por destinatario a las 3 dependencias autorizadas del servicio, 3. Son valores del modelo, no medidas, pero la estructura es la importante: segmentar divide por el número de segmentos, y limitar por destinatario reduce al grado de dependencia del servicio comprometido. Ambas se combinan: la segmentación contiene lo que la política no previó. La métrica del trabajo no es «cuántos controles hay» sino *cuántos servicios alcanza una credencial robada y durante cuánto tiempo*, y ese número se calcula para tu sistema.

## Ejemplo

Ejemplo de [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md) (sección «Ejemplo profesional»):

Tras el incidente, el equipo de *Avisos* hace tres cambios por orden de rendimiento. Primero, mapea los flujos entre servicios y descubre que el servicio de informes llamaba a doce servicios cuando solo necesitaba dos: reduce permisos por destinatario y el radio de daño de una credencial de ese servicio pasa de doce a dos. Segundo, sustituye las credenciales de larga vida (tokens de 30 días en variables de entorno) por credenciales emitidas por un servicio de identidad con vida de 15 minutos y destinatario; para ello debe resolver la renovación automática y descubre dos servicios que guardaban el token en un archivo de configuración.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md)) son: Se verificaron tokens firmados con HMAC y se modelaron el radio de daño y la ventana de uso indebido con supuestos del autor; no se ejecutó ningún emisor de identidad, punto de decisión, malla de servicios ni revocación. El siguiente paso, `SE-287`, es el taller: una batería de comportamientos hostiles contra tres formas de ejecutar código ajeno, con el resultado a la vista.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Efecto](../e/efecto.md), [Recurso](./recurso.md), [Aislamiento del sistema operativo](../a/aislamiento-del-sistema-operativo.md), [Audiencia](../a/audiencia.md), [Autoridad de un agente](../a/autoridad-de-un-agente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-286 — Confianza cero en la práctica](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-569 — Agentes, herramientas, permisos y límites de autoridad](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Saltzer y Schroeder](https://doi.org/10.1109/PROC.1975.9939) — mínimo privilegio y protección de la información; autoridad: Proceedings of the IEEE, 1975.
- [Claude Code: permisos](https://code.claude.com/docs/en/permissions) — orden de evaluación, órdenes compuestas y fragilidad de los patrones sobre argumentos; autoridad: documentación de Anthropic.
- [Claude Code: aislamiento (sandbox)](https://code.claude.com/docs/en/sandboxing) — aislamiento de sistema de archivos y red a nivel del sistema operativo; autoridad: documentación de Anthropic.
- [OWASP Top 10 para aplicaciones con LLM](https://genai.owasp.org/llm-top-10/) — riesgos, entre ellos la agencia excesiva; autoridad: proyecto OWASP GenAI.

---

[↑ Glosario](../../README.md) · [← Qubit lógico y físico](../q/qubit-logico-y-fisico.md) · [Radio de efecto →](./radio-de-efecto.md)
