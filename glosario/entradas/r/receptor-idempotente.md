# Receptor idempotente

[↑ Glosario](../../README.md) · [← Recarga única](./recarga-unica.md) · [Rechazo implícito →](./rechazo-implicito.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Un **receptor idempotente** es un receptor para el que procesar un mensaje repetido no cambia el resultado: ante un duplicado, no repite el efecto. Es el sentido de [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md) (Enterprise Integration Patterns como lenguaje común) y de [SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md) (low-code y automatización visual). Es el patrón que acompaña a un canal de entrega al menos una vez.

## Por qué importa

Convierte «al menos una vez» en efecto único. Un canal que puede duplicar mensajes no es defectuoso: cumple lo que promete. La responsabilidad de que un duplicado no cobre dos veces es del receptor.

## Cómo funciona

[SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md) lo muestra con un experimento: 1000 mensajes (60 % pagos, 20 % avisos, 20 % bajas) por un canal al menos una vez que duplica un 20 % y reordena en ventanas de 6. Se entregan 1208 mensajes (208 duplicados).

- La suma real de pagos es **15 682**.
- Sin receptor idempotente, el consumidor suma **18 759**, un error de **+3 077**.
- Con un receptor que guarda los identificadores vistos y descarta los repetidos, suma **15 682**.

Dos decisiones de diseño:

1. **El identificador del mensaje debe ser estable:** el mismo en cada reenvío. Un identificador generado en el receptor no sirve, porque cada llegada parecería un mensaje nuevo.
2. **Cuánto conservar los identificadores.** Una ventana finita (por ejemplo, 7 días) acota la memoria, pero exige que el canal no reenvíe más tarde que esa ventana.

El diagnóstico de la clase es ordenado: contar cuántos identificadores aparecen más de una vez (208 de 1208), comprobar la garantía del proveedor (al menos una vez), y concluir que la causa no es el código de suma sino la ausencia de receptor idempotente.

## Ejemplo

Ilustración propia: la tabla `procesados(mensaje_id primary key)`. El receptor inserta el identificador en la misma transacción que aplica el efecto; si el `INSERT` choca con la clave, el mensaje ya se procesó y se descarta. Es la *inbox* de [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md).

## Errores y confusiones comunes

- **Generar el identificador en el receptor** o derivarlo de datos que cambian en cada reenvío.
- **Comprobar el identificador y aplicar el efecto en transacciones separadas:** una caída entre ambos rompe la garantía.
- **Olvidar la caducidad de los identificadores** y quedarse sin memoria.
- **Confundirlo con la idempotencia de la operación:** puede lograrse de dos modos (la operación es naturalmente idempotente, o el receptor deduplica).

## Límites y cuándo no aplica

La ventana de retención limita la protección. Si el efecto es sobre un sistema externo sin clave de idempotencia, la deduplicación local no basta. El experimento de [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md) es una simulación con duplicados y reordenamientos construidos por el autor.

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
