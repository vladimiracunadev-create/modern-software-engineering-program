# Fuerza

[↑ Glosario](../../README.md) · [← Fuentes de no determinismo](./fuentes-de-no-determinismo.md) · [Fuerzas del problema →](./fuerzas-del-problema.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Presión de diseño con dolor observable que el patrón equilibra.

Definición de trabajo de [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md).

## Por qué importa

En [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), el tema «Fuerza antes que forma» importa porque la forma sin fuerza se aplica por costumbre

## Cómo funciona

Según [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md):

Una **fuerza** es la presión de diseño que empuja en dos direcciones: «quiero añadir canales sin tocar lo probado» y «quiero que el código sea corto». El patrón es una forma de resolver el conflicto, no de eliminarlo. Si no puedes decir la fuerza en una frase con un dato (por ejemplo «cada canal nuevo ha tocado la función de tarifas, y en el último trimestre se tocó cuatro veces»), todavía no hay una razón. Una fuerza que existe solo en el futuro imaginado («podríamos necesitar más canales») es la razón con la que se justifican los diseños que nunca se usan.

Según [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md):

El equipo de *Avisos* revisa el cálculo de tarifas antes de añadir el canal de mensajería instantánea. Escribe en el `criterio-de-patron.md`: fuerza («cada canal nuevo ha obligado a editar `precio_aviso` y a repasar las pruebas de los otros»), evidencia («tres canales nuevos en seis meses y dos más en el backlog con responsable»), costo («el Strategy usa un 44 % más de nodos y añade un salto de indirección; la complejidad por función baja»), alternativa («un diccionario de funciones haría lo mismo con menos piezas, pero las tarifas de voz necesitan estado») y salida («si en un año no entra un canal nuevo, se vuelve a la función simple»). Con eso la discusión pasa de gusto a evidencia, y la decisión queda registrada para quien la revise.

## Ejemplo

Ejemplo de [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md) (sección «Ejemplo mínimo»):

La segunda no es un patrón con nombre y resuelve la fuerza «añadir un canal sin tocar la función» con una línea de datos. Es el diseño más barato que da la propiedad buscada, y por eso el patrón completo con clases solo se justifica si cada canal necesita **comportamiento** propio y no solo un número.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si no puedes decir la fuerza en una frase con un dato (por ejemplo «cada canal nuevo ha tocado la función de tarifas, y en el último trimestre se tocó cuatro veces»), todavía no hay una razón. ([SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Patrón](../p/patron.md), [Condición de salida](../c/condicion-de-salida.md), [Consecuencia](../c/consecuencia.md), [Costo estructural](../c/costo-estructural.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (64 clases más lo mencionan; las que más):

[SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), [SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md), [SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-056](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md), [SE-091](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Fuentes de no determinismo](./fuentes-de-no-determinismo.md) · [Fuerzas del problema →](./fuerzas-del-problema.md)
