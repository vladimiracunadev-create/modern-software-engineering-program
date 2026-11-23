# Tabla amenaza-mecanismo-prueba

[↑ Glosario](../../README.md) · [← Systems Programmer](../s/systems-programmer.md) · [Tabla de diferencias →](./tabla-de-diferencias.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Correspondencia que exige una prueba por cada mecanismo.

Definición de trabajo de [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md).

## Por qué importa

En [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), el tema «Tabla amenaza-mecanismo-prueba» importa porque evita mecanismos sin prueba.

## Cómo funciona

Según [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md):

Elige una carga de tu sistema que hoy ejecute código de terceros o configuración de clientes. Escribe su modelo de amenazas, la tabla amenaza-mecanismo-prueba, el contrato de ejecución y la política de fallo. Implementa la mínima plataforma que haga cumplir el contrato con registro encadenado y entrega el expediente con una sección «no cubierto» que otra persona pueda discutir.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md)) son: La referencia es una plataforma mínima ejecutada en una máquina: sin autenticación de clientes, sin frontera alrededor del anfitrión, sin hardware seguro, sin almacenamiento durable y con una biblioteca de firma de estudio. Con este proyecto se cierra la [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md).

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Mecanismo](../m/mecanismo.md), [Cabeza de la cadena](../c/cabeza-de-la-cadena.md), [Contrato de ejecución](../c/contrato-de-ejecucion.md), [Expediente](../e/expediente.md), [Plataforma de ejecución aislada](../p/plataforma-de-ejecucion-aislada.md), [Política de falla](../p/politica-de-falla.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Systems Programmer](../s/systems-programmer.md) · [Tabla de diferencias →](./tabla-de-diferencias.md)
