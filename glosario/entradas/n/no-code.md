# No-code

[↑ Glosario](../../README.md) · [← No verificable](./no-verificable.md) · [Nodo completo →](./nodo-completo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Enfoque que busca que quien construye no escriba código, sustituido por configuración visual.

Definición de trabajo de [SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md).

## Por qué importa

En [SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md), el tema «Qué es low-code y no-code» importa porque delimita qué se gana, qué se pierde y qué sigue siendo ingeniería.

## Cómo funciona

Según [SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md):

Las plataformas **low-code** reducen la cantidad de código que se escribe, ofreciendo bloques y plantillas con código en los huecos; las **no-code** buscan que no se escriba ninguno. Ambas trasladan la complejidad: el lenguaje deja de ser texto y pasa a ser un diagrama con una semántica propia, y la plataforma decide cómo se ejecuta, se reintenta y se factura. Lo que no desaparece: requisitos, datos, condiciones, pruebas, seguridad, mantenimiento. Ganan velocidad cuando el problema encaja en la plataforma y pierden cuando hay que salirse de ella; su coste oculto aparece en el cambio, la depuración y la salida.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md):

El equipo de la plataforma establece cuatro condiciones para aceptar una automatización en producción. Primera: un documento de una página con qué hace, qué datos toca y qué cuota consume. Segunda: un conjunto de pruebas de pares sobre un entorno de prueba con datos sintéticos, con el resultado archivado. Tercera: un receptor idempotente que guarda el identificador del evento durante 24 horas, medido a partir de la cola de re-entregas del proveedor.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md)) son:

- **Un caso inusual no recibe aviso** — causa: combinación de decisiones sin probar. Corrección: conjunto de pruebas de pares con los factores relevantes.
- **Los avisos se envían dos veces** — causa: disparador al menos una vez sin receptor idempotente. Corrección: guardar identificadores de evento con un tiempo medido.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Las plataformas **low-code** reducen la cantidad de código que se escribe, ofreciendo bloques y plantillas con código en los huecos; las **no-code** buscan que no se escriba ninguno. ([SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cobertura de pares](../c/cobertura-de-pares.md), [Flujo huérfano](../f/flujo-huerfano.md), [Low-code](../l/low-code.md), [Receptor idempotente](../r/receptor-idempotente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md), [SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Kuhn, Kacker y Lei, NIST SP 800-142, «Practical Combinatorial Testing»](https://csrc.nist.gov/pubs/sp/800/142/final) — pruebas combinatorias y cobertura de pares; autoridad: NIST.
- [Stripe, documentación de webhooks](https://docs.stripe.com/webhooks) — entrega repetida de eventos y receptores idempotentes; autoridad: documentación del proveedor.
- [Hohpe y Woolf, «Idempotent Receiver»](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) — receptor que tolera mensajes repetidos; autoridad: Enterprise Integration Patterns.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← No verificable](./no-verificable.md) · [Nodo completo →](./nodo-completo.md)
