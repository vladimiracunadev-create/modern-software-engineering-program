# Radio de daño

[↑ Glosario](../../README.md) · [← Qubit lógico y físico](../q/qubit-logico-y-fisico.md) · [Radio de efecto →](./radio-de-efecto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

El **radio de daño** (*blast radius*) es el conjunto de recursos alcanzables con una credencial comprometida. Es el sentido de [SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md) (confianza cero en la práctica). [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md) lo extiende a agentes: el conjunto de efectos que una acción errónea o maliciosa puede causar con la autoridad disponible. Es una medida de lo que se puede perder, no de la probabilidad de que ocurra.

## Por qué importa

Según [SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), es la métrica que importa. No importa cuántos controles tiene un sistema, sino *cuántos servicios alcanza una credencial robada y durante cuánto tiempo*. Pasa la pregunta de «¿nos pueden entrar?» a «si entran, ¿hasta dónde llegan?».

## Cómo funciona

[SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md) modela 200 servicios en 5 segmentos y una credencial robada de un servicio elegido al azar (5 000 repeticiones, semilla 48):

- **Red plana de confianza interna:** el atacante alcanza 200 servicios.
- **Segmentación de red en cinco partes:** 40.
- **Credenciales limitadas por destinatario** a las 3 dependencias autorizadas del servicio: 3.

Son valores del modelo, no medidas, pero la estructura es el punto: segmentar divide por el número de segmentos, y limitar por destinatario reduce el alcance al grado de dependencia del servicio comprometido. Ambas se combinan: la segmentación contiene lo que la política no previó. Para tu sistema, la cifra se calcula con el mapa real de dependencias.

En agentes ([SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md)), el radio es lo que el agente *podría* hacer con las herramientas y permisos que tiene; se reduce con mínimo privilegio y confirmación humana para efectos graves.

## Ejemplo

Tras un incidente, el equipo de *Avisos* hace en [SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md) tres cambios por orden de rendimiento. Primero, mapea los flujos entre servicios y descubre que el servicio de informes llamaba a doce servicios cuando solo necesitaba dos: reduce permisos por destinatario y el radio de daño de una credencial de ese servicio pasa de doce a dos.

## Errores y confusiones comunes

- **Medir cuántos controles hay** en vez de cuánto alcanza una credencial robada.
- **Credenciales amplias «por comodidad»,** compartidas entre servicios.
- **Confundirlo con la probabilidad de intrusión:** reduce el impacto, no la ocurrencia.
- **No acotar la duración:** una credencial que no caduca amplía el radio en el tiempo.

## Límites y cuándo no aplica

El número del modelo es de una simulación, no una medida de un sistema. El radio de daño solo contempla lo alcanzable con la credencial; no cubre daños por otros medios (ingeniería social, fallos de lógica). Reducirlo tiene costo operativo: más credenciales, más rotación y más reglas que mantener.

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
