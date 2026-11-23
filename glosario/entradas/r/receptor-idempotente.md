# Receptor idempotente

[↑ Glosario](../../README.md) · [← Recarga única](./recarga-unica.md) · [Rechazo implícito →](./rechazo-implicito.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Receptor para el que procesar un mensaje repetido no cambia el resultado.

Definición de trabajo de [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md): Receptor que, ante un mensaje repetido, no repite el efecto.

## Por qué importa

En [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), el tema «Receptor idempotente» importa porque convierte entrega al menos una vez en efecto único

## Cómo funciona

Según [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md):

El experimento simula 1000 mensajes (60 % pagos, 20 % avisos, 20 % bajas) con un canal al menos una vez que duplica un 20 % y reordena en ventanas de 6. Se entregan 1208 mensajes (208 duplicados). La suma real de pagos es **15.682**; sin receptor idempotente, el consumidor suma **18.759**, un error de **+3.077**; con un receptor que guarda los identificadores vistos y descarta los repetidos, suma **15.682**. La clave es que el identificador del mensaje es **estable** (el mismo en cada reenvío); un identificador generado en el receptor no sirve. Guardar los identificadores plantea otra decisión: cuánto tiempo conservarlos. Una ventana finita (por ejemplo, 7 días) acota la memoria y exige que el canal no reenvíe más tarde de esa ventana.

Según [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md):

**Diagnóstico paso a paso.** (1) Se cuenta cuántos identificadores de mensaje aparecen más de una vez: 208 de 1208 entregas. (2) Se comprueba la garantía del proveedor: al menos una vez. (3) La causa no es el código de suma sino la ausencia de un receptor idempotente: el canal hizo lo que prometía.

## Ejemplo

Ejemplo de [SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma establece cuatro condiciones para aceptar una automatización en producción. Primera: un documento de una página con qué hace, qué datos toca y qué cuota consume. Segunda: un conjunto de pruebas de pares sobre un entorno de prueba con datos sintéticos, con el resultado archivado. Tercera: un receptor idempotente que guarda el identificador del evento durante 24 horas, medido a partir de la cola de re-entregas del proveedor. Cuarta: dos responsables, una revisión trimestral que comprueba que la persona sigue en la organización y las credenciales son las mínimas, y un registro de ejecuciones que se conserva 90 días.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los avisos se envían dos veces** — causa: disparador al menos una vez sin receptor idempotente. Corrección: guardar identificadores de evento con un tiempo medido. ([SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La suma real de pagos es **15.682**; sin receptor idempotente, el consumidor suma **18.759**, un error de **+3.077**; con un receptor que guarda los identificadores vistos y descarta los repetidos, suma **15.682**. ([SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Resultado](./resultado.md), [Cobertura de pares](../c/cobertura-de-pares.md), [Cola de cartas muertas](../c/cola-de-cartas-muertas.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md), [Flujo huérfano](../f/flujo-huerfano.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-298 — Low-code, no-code y automatización visual](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md), [SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), [SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md), [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Stripe, documentación de webhooks](https://docs.stripe.com/webhooks) — entrega repetida de eventos y receptores idempotentes; autoridad: documentación del proveedor.
- [Kuhn, Kacker y Lei, NIST SP 800-142, «Practical Combinatorial Testing»](https://csrc.nist.gov/pubs/sp/800/142/final) — pruebas combinatorias y cobertura de pares; autoridad: NIST.
- [Hohpe y Woolf, «Idempotent Receiver»](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) — receptor que tolera mensajes repetidos; autoridad: Enterprise Integration Patterns.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Recarga única](./recarga-unica.md) · [Rechazo implícito →](./rechazo-implicito.md)
