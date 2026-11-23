# Batería hostil

[↑ Glosario](../../README.md) · [← Baseline](./baseline.md) · [Benchmark →](./benchmark.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Conjunto de comportamientos que ejercen una propiedad de aislamiento cada uno.

Definición de trabajo de [SE-287 — Taller: elegir y aislar un runtime para una carga no confiable](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md).

## Por qué importa

La clase donde se define, [SE-287 — Taller: elegir y aislar un runtime para una carga no confiable](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), existe con este propósito: el taller existe para que la elección de un runtime y de una frontera de aislamiento deje de ser una opinión y se convierta en un resultado que cualquiera puede repetir: seis comportamientos hostiles, tres formas de ejecutar código ajeno, una matriz de qué contiene cada una y una decisión por carga de trabajo con su costo.

## Cómo funciona

[SE-287 — Taller: elegir y aislar un runtime para una carga no confiable](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-287 — Taller: elegir y aislar un runtime para una carga no confiable](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-287 — Taller: elegir y aislar un runtime para una carga no confiable](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md)) son: El taller probó tres candidatos con seis comportamientos en una máquina Windows; no probó contenedores, microVM, núcleo de aplicación, perfiles de llamadas de sistema ni límites de memoria del sistema operativo, y dos celdas del primer candidato quedaron sin ejecutar. El siguiente paso, `SE-288`, integra los candidatos en una plataforma con validación, límites, evidencia encadenada e informe firmado.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Aislamiento](../a/aislamiento.md), [Conjunto](../c/conjunto.md), [Propiedad](../p/propiedad.md), [Alcance](../a/alcance.md), [Capacidad](../c/capacidad.md), [Condición de revisión](../c/condicion-de-revision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-287 — Taller: elegir y aislar un runtime para una carga no confiable](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Baseline](./baseline.md) · [Benchmark →](./benchmark.md)
