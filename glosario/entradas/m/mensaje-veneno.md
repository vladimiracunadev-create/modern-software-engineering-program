# Mensaje veneno

[↑ Glosario](../../README.md) · [← Mensaje de error asociado](./mensaje-de-error-asociado.md) · [Mensaje venenoso →](./mensaje-venenoso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Mensaje que falla en cada intento de proceso.

Definición de trabajo de [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md).

## Por qué importa

La clase donde se define, [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), existe con este propósito: la clase existe para que uses los patrones de integración como un **lenguaje para razonar sobre garantías**: qué promete un canal de mensajes, qué obligación traslada esa promesa al receptor y qué patrón la cumple.

## Cómo funciona

Según [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md):

Un mensaje **veneno** es el que falla siempre (un formato inesperado, una regla que no puede cumplirse). Si el consumidor lo reintenta sin límite, bloquea la cola o gasta recursos sin fin. Un **Dead Letter Channel** impone un tope de intentos y mueve el mensaje a otra cola. En el experimento, de los primeros 200 mensajes, 2 son veneno (se sembraron 25 en los 1000); con un tope de 3 intentos, se procesan **198**, se apartan **2** y se hacen **204** intentos en total; sin tope, cada veneno exigiría reintentos sin fin. La cola de cartas muertas **sin alarma** es un cementerio: lo que importa no es que exista sino que alguien reciba un aviso cuando crece y tenga un procedimiento para revisar, corregir y reinyectar.

Según [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md):

Tras el incidente de contabilidad, el equipo de *Avisos* escribe una tabla de garantías del canal de pagos: entrega al menos una vez, sin orden entre particiones, mensajes veneno posibles por cambios del proveedor. Para cada fila elige un patrón: tabla de identificadores procesados con ventana de 14 días y transacción conjunta, reordenamiento innecesario porque la suma es conmutativa (decisión explícita), cola de cartas muertas con alarma cuando supera diez mensajes y un procedimiento de reinyección. Añade una prueba de idempotencia que envía cada mensaje tres veces y compara con la suma esperada, y una prueba de veneno que comprueba que el consumidor sigue procesando.

## Ejemplo

Ejemplo de [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md) (sección «Ejemplo profesional»):

Tras el incidente de contabilidad, el equipo de *Avisos* escribe una tabla de garantías del canal de pagos: entrega al menos una vez, sin orden entre particiones, mensajes veneno posibles por cambios del proveedor. Para cada fila elige un patrón: tabla de identificadores procesados con ventana de 14 días y transacción conjunta, reordenamiento innecesario porque la suma es conmutativa (decisión explícita), cola de cartas muertas con alarma cuando supera diez mensajes y un procedimiento de reinyección. Añade una prueba de idempotencia que envía cada mensaje tres veces y compara con la suma esperada, y una prueba de veneno que comprueba que el consumidor sigue procesando.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un mensaje **veneno** es el que falla siempre (un formato inesperado, una regla que no puede cumplirse). ([SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Proceso](../p/proceso.md), [Cola de cartas muertas](../c/cola-de-cartas-muertas.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md), [Identificador de correlación](../i/identificador-de-correlacion.md), [Receptor idempotente](../r/receptor-idempotente.md), [Reordenador](../r/reordenador.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Mensaje de error asociado](./mensaje-de-error-asociado.md) · [Mensaje venenoso →](./mensaje-venenoso.md)
