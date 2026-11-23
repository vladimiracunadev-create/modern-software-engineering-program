# Estado actual

[↑ Glosario](../../README.md) · [← Estado](./estado.md) · [Estado como memoria de la ejecución →](./estado-como-memoria-de-la-ejecucion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Valor presente de una entidad, sin historia.

Definición de trabajo de [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md).

## Por qué importa

La clase donde se define, [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), existe con este propósito: la clase existe para que decidas cuándo y cómo sacar datos de la base que sirve a la aplicación y llevarlos a un lugar pensado para responder preguntas, y para que sepas por qué esa decisión no es solo «copiar tablas».

## Cómo funciona

Según [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md):

La tabla `orders` guarda el estado actual de cada pedido. Cuando un pedido pasa de `paid` a `shipped`, la fila se actualiza y `paid` desaparece. La pregunta «¿cuántos pedidos estaban pagados y sin enviar el día 100?» necesita saber qué estado tenía cada pedido ese día. Con 20 000 pedidos y 70 745 cambios de estado, la respuesta correcta, calculada sobre el registro de cambios, fue 989; la tabla de estado actual solo permite contar cuántos están en `paid` hoy, 1 486, que responde otra pregunta. La corrección no es una consulta mejor sino conservar lo que se perdió: un registro de eventos o filas con vigencia (`valid_from`, `valid_to`). Es la razón de que un modelo analítico guarde historia aunque la operación no la necesite.

Según [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md):

Resuelve la interferencia y no la historia ni la forma. Para volúmenes pequeños y preguntas sobre el presente, basta; para preguntas sobre el pasado o agregados sobre años, la réplica sigue guardando solo el estado actual y recorriendo filas completas.

## Ejemplo

Ejemplo de [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md) (sección «Preguntas frecuentes»):

Resuelve la interferencia y no la historia ni la forma. Para volúmenes pequeños y preguntas sobre el presente, basta; para preguntas sobre el pasado o agregados sobre años, la réplica sigue guardando solo el estado actual y recorriendo filas completas.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Con 20 000 pedidos y 70 745 cambios de estado, la respuesta correcta, calculada sobre el registro de cambios, fue 989; la tabla de estado actual solo permite contar cuántos están en `paid` hoy, 1 486, que responde otra pregunta. ([SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md))
- Para volúmenes pequeños y preguntas sobre el presente, basta; para preguntas sobre el pasado o agregados sobre años, la réplica sigue guardando solo el estado actual y recorriendo filas completas. ([SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor](../v/valor.md), [Capa](../c/capa.md), [Carga analítica](../c/carga-analitica.md), [Carga operacional](../c/carga-operacional.md), [Extracción](./extraccion.md), [Interferencia](../i/interferencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), [SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), [SE-010](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md), [SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md), [SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md), [SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md), [SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Slack](../../../casos/exito/slack.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Estado](./estado.md) · [Estado como memoria de la ejecución →](./estado-como-memoria-de-la-ejecucion.md)
