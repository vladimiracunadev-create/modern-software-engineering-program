# Complemento

[↑ Glosario](../../README.md) · [← Complejidad esencial](./complejidad-esencial.md) · [Compliance Engineer →](./compliance-engineer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Módulo que cumple el contrato del núcleo y se descubre, no se enlaza.

Definición de trabajo de [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md).

## Por qué importa

En [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), el tema «Núcleo mínimo» importa porque todo lo que vive en el núcleo es contrato implícito para los complementos.

## Cómo funciona

Según [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md):

Un microkernel conserva en el núcleo solo lo que todos los complementos necesitan y que cambia poco: registrar complementos, despachar eventos y fallar de forma controlada. Todo lo demás vive fuera. En el laboratorio el núcleo (`Kernel`) tiene tres métodos: cargar un directorio, comprobar la versión del contrato y despachar un evento a cada complemento. La tentación contraria es dejar en el núcleo «lo común», que crece hasta que el núcleo es el sistema y los complementos son decoración. La pregunta de control es: ¿esta función la necesitan todos los complementos y la voy a poder mantener igual durante años?

Según [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md):

Una universidad cliente pide que *Avisos* envíe cada aviso también a su campus virtual por webhook. Con el núcleo de complementos, su equipo de integración escribe el módulo, lo prueba contra la clase de pruebas de contrato que publica el equipo del núcleo y lo coloca en el directorio. Dos semanas después, el equipo del núcleo necesita añadir un campo de prioridad al evento y decide subir el contrato a la versión 2. Antes de publicar, ejecuta el cargador contra los diez complementos conocidos con la política de rechazo al arrancar: siete son suyos y se migran en el mismo cambio; tres son de universidades, que quedan con el adaptador de la versión 1 durante un trimestre y con un aviso de retirada.

## Ejemplo

Ejemplo de [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md) (sección «Ejemplo mínimo»):

Un complemento es un archivo de tres líneas: `API = 1`, `NAME = "sms"` y una función `handle(event)` que devuelve `"sms:" + event["id"]`. Copiarlo a la carpeta añade el canal; ningún archivo del núcleo cambia.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un microkernel conserva en el núcleo solo lo que todos los complementos necesitan y que cambia poco: registrar complementos, despachar eventos y fallar de forma controlada. ([SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrato](./contrato.md), [Módulo](../m/modulo.md), [Núcleo](../n/nucleo.md), [Adaptador de compatibilidad](../a/adaptador-de-compatibilidad.md), [Aislamiento](../a/aislamiento.md), [Descubrimiento](../d/descubrimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (32 clases más lo mencionan; las que más):

[SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md), [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-116](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md), [SE-113](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-113-cli-flags-configuracion-y-codigos-de-salida/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «plugin».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Complejidad esencial](./complejidad-esencial.md) · [Compliance Engineer →](./compliance-engineer.md)
