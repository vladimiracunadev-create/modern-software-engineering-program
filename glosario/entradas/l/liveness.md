# Liveness

[↑ Glosario](../../README.md) · [← Lista y matriz de adyacencia](./lista-y-matriz-de-adyacencia.md) · [Llamada a procedimiento remoto →](./llamada-a-procedimiento-remoto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Propiedad de progreso eventual bajo supuestos.

Definición de trabajo de [SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md).

## Por qué importa

La clase donde se define, [SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md), existe con este propósito: la clase existe para modelar estado, transiciones y eventos para detectar secuencias imposibles o ambiguas.

## Cómo funciona

Según [SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md):

Safety afirma que algo malo nunca ocurre: no ejecutar sin autorización. Liveness afirma que algo bueno eventualmente ocurre bajo supuestos: toda ejecución termina o se cancela. Probar safety no garantiza progreso; reintentar eternamente puede mantener invariantes y violar liveness.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md):

El modelo de decisión diagnóstica persiste transición y versión antes de emitir efectos. Cada ejecución tiene ID; eventos duplicados son idempotentes y tardíos se archivan sin mutar el estado actual. Un diagrama se acompaña con tabla completa de eventos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md)) son:

- **Un pedido sin pagar aparece enviado** — causa: transición ilegal aceptada. Corrección: validar contra la tabla y rechazar.
- **El estado cambia al recibir un evento inválido** — causa: error silencioso. Corrección: mantener el estado y registrar el rechazo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Liveness afirma que algo bueno eventualmente ocurre bajo supuestos: toda ejecución termina o se cancela. ([SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Progreso](../p/progreso.md), [Propiedad](../p/propiedad.md), [Supuestos](../s/supuestos.md), [Dominio](../d/dominio.md), [Estado](../e/estado.md), [Estrategia](../e/estrategia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md), [SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.

---

[↑ Glosario](../../README.md) · [← Lista y matriz de adyacencia](./lista-y-matriz-de-adyacencia.md) · [Llamada a procedimiento remoto →](./llamada-a-procedimiento-remoto.md)
