# Controlador

[↑ Glosario](../../README.md) · [← Control aparente](./control-aparente.md) · [Convalidación →](./convalidacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Objeto que recibe y coordina un evento externo.

Definición de trabajo de [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md).

## Por qué importa

En [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md), el tema «Creador y Controlador» importa porque deciden quién instancia y quién recibe eventos

## Cómo funciona

Según [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md):

El **Creador** asigna la creación de un objeto a quien lo contiene, lo registra, lo usa mucho o tiene los datos para inicializarlo; un `Pedido` crea sus `Linea`. El **Controlador** asigna la recepción de un evento externo (una petición, un mensaje) a un objeto que representa el caso de uso o el sistema, y no a la interfaz. Los dos criterios son los que menos a menudo se discuten y más a menudo se violan: la creación repartida en veinte lugares es el origen de la fábrica de `SE-314`, y un controlador que contiene reglas de negocio es la clase de dios de `SE-322`.

Según [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md):

El equipo de *Avisos* aplica la tabla de responsabilidades a «enviar el recordatorio de una entrega». Descubre que la regla «no avisar si ya se entregó» está en el controlador de la interfaz, en el servicio de envío y en un trabajo nocturno. Asigna la regla al objeto `Entrega` (Experto: tiene la fecha y el estado), mueve las otras dos copias con el refactor `Move Function`, añade una prueba que cubre los tres caminos y mide con `ast` que las tres clases ya no leen el estado de la entrega a través de otros objetos. Anota la alternativa descartada: dejar la regla en el servicio de envío, por ser lo que cambió más a menudo; se descartó porque el trabajo nocturno no pasa por el servicio.

## Ejemplo

Ejemplo de [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* aplica la tabla de responsabilidades a «enviar el recordatorio de una entrega». Descubre que la regla «no avisar si ya se entregó» está en el controlador de la interfaz, en el servicio de envío y en un trabajo nocturno. Asigna la regla al objeto `Entrega` (Experto: tiene la fecha y el estado), mueve las otras dos copias con el refactor `Move Function`, añade una prueba que cubre los tres caminos y mide con `ast` que las tres clases ya no leen el estado de la entrega a través de otros objetos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **Controlador** asigna la recepción de un evento externo (una petición, un mensaje) a un objeto que representa el caso de uso o el sistema, y no a la interfaz. ([SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Objeto](../o/objeto.md), [Acoplamiento](../a/acoplamiento.md), [Cohesión](./cohesion.md), [Creador](./creador.md), [Experto en información](../e/experto-en-informacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (32 clases más lo mencionan; las que más):

[SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), [SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), [SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md), [SE-454](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md), [SE-511](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Control aparente](./control-aparente.md) · [Convalidación →](./convalidacion.md)
