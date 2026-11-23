# Estilo arquitectónico

[↑ Glosario](../../README.md) · [← Estándar de codificación segura](./estandar-de-codificacion-segura.md) · [Estimación con incertidumbre →](./estimacion-con-incertidumbre.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Conjunto de restricciones sobre las unidades, sus conexiones y su despliegue que favorece unos atributos de calidad.

Definición de trabajo de [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md).

## Por qué importa

La clase donde se define, [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), existe con este propósito: la clase existe para que dejes de elegir una arquitectura por su nombre y empieces a elegirla por las fuerzas que debe resistir.

## Cómo funciona

Según [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md):

Un estilo arquitectónico dice qué tipos de unidades existen, cómo se comunican y qué está prohibido. Un monolito en capas prohíbe que una capa inferior llame a una superior; un sistema de pipes and filters prohíbe que un filtro conozca a los demás; una arquitectura de microservicios prohíbe compartir la base de datos entre servicios. Cada restricción compra una propiedad: la prohibición de compartir la base de datos permite desplegar un servicio sin coordinar con otros, y a cambio obliga a que los datos viajen por la red y a que las transacciones se repartan. Elegir un estilo es aceptar el paquete entero; por eso no se puede tomar solo «la parte buena».

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md)) son: La matriz, los pesos y los cuatro contextos son construcciones del autor; los resultados muestran el mecanismo de decisión y no recomiendan ningún estilo para un sistema real. No se midió ningún sistema, equipo ni producto. El siguiente paso, `SE-338`, estudia el primer estilo concreto: el microkernel, que compra extensión por terceros y paga con un contrato que hay que mantener.

## Relación con otros conceptos

- **Prerrequisito:** [Restricciones](../r/restricciones.md).
- **Ver también:** [Atributos de calidad](../a/atributos-de-calidad.md), [Atributo](../a/atributo.md), [Conjunto](../c/conjunto.md), [Sobre](../s/sobre.md), [Escenario de calidad](./escenario-de-calidad.md), [Margen](../m/margen.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Estándar de codificación segura](./estandar-de-codificacion-segura.md) · [Estimación con incertidumbre →](./estimacion-con-incertidumbre.md)
