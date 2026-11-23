# Aislamiento

[↑ Glosario](../../README.md) · [← AI-Augmented Software Engineer](./ai-augmented-software-engineer.md) · [Aislamiento de datos →](./aislamiento-de-datos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Técnica que impide que el fallo de un complemento se propague al núcleo o a otros complementos.

Definición de trabajo de [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md).

## Por qué importa

En [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), el tema «Aislamiento» importa porque contiene fallos y bloqueos a costos muy distintos.

## Cómo funciona

Según [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md):

Un complemento puede lanzar una excepción, quedarse bloqueado, consumir memoria sin límite o terminar el proceso. La defensa más barata es capturar la excepción en el despachador (`try`/`except`) y continuar con el siguiente complemento. En el experimento, con ocho complementos de los cuales uno lanza `RuntimeError`, el despachador entrega siete resultados y registra el error; sin captura, la excepción detiene la entrega a los demás. Esa defensa no ayuda con un complemento lento: uno que duerme un segundo bloquea al núcleo durante 1,00 s en el mismo hilo. Para el bloqueo hace falta ejecutar el complemento en otro hilo o proceso con un límite de tiempo: un proceso con `timeout` de 0,3 s cortó al lento a los 314 ms.

Según [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md):

**Diagnóstico paso a paso.** (1) Se revisa el cargador: no comprueba la versión del complemento, de modo que los cinco complementos de la versión 1 se cargaron. (2) Se despacha un evento de prueba: cada complemento devuelve una cadena y el despachador espera un diccionario; el acceso `res["status"]` lanza `TypeError`. (3) El despachador captura la excepción y la registra con un nivel que nadie vigila. (4) El aislamiento funcionó como estaba diseñado y por eso el fallo fue silencioso.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Son más de cinco órdenes de magnitud de diferencia, y por eso el aislamiento por proceso se reserva para complementos de terceros no confiables o para tareas poco frecuentes. ([SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Complemento](../c/complemento.md), [Núcleo](../n/nucleo.md), [Adaptador de compatibilidad](./adaptador-de-compatibilidad.md), [Contrato](../c/contrato.md), [Descubrimiento](../d/descubrimiento.md), [Microkernel](../m/microkernel.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (105 clases más lo mencionan; las que más):

[SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), [SE-103](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← AI-Augmented Software Engineer](./ai-augmented-software-engineer.md) · [Aislamiento de datos →](./aislamiento-de-datos.md)
