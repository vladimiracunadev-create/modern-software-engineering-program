# Superficie compartida

[↑ Glosario](../../README.md) · [← Suma de verificación por rango](./suma-de-verificacion-por-rango.md) · [Superficie de acción →](./superficie-de-accion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Código y dispositivos del anfitrión alcanzables desde la carga.

Definición de trabajo de [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md).

## Por qué importa

En [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), el tema «Superficie compartida» importa porque es lo que un escape alcanza.

## Cómo funciona

[SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md)) son: Se midieron tres fronteras y se ejecutaron cuatro comprobaciones de un sandbox casero; no se ejecutó ningún contenedor, microVM ni núcleo de aplicación, y las probabilidades del modelo de capas son del autor. El siguiente paso, `SE-283`, estudia el hardware seguro: entornos de ejecución aislados cuyo estado puede demostrarse a distancia, y lo que esa demostración no prueba.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md), [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Anfitrión](../a/anfitrion.md), [Dispositivo](../d/dispositivo.md), [Causa común](../c/causa-comun.md), [Espacio de nombres](../e/espacio-de-nombres.md), [Frontera de aislamiento](../f/frontera-de-aislamiento.md), [MicroVM](../m/microvm.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Suma de verificación por rango](./suma-de-verificacion-por-rango.md) · [Superficie de acción →](./superficie-de-accion.md)
