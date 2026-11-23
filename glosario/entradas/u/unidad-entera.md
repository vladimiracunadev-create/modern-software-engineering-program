# Unidad entera

[↑ Glosario](../../README.md) · [← Una variable por experimento](./una-variable-por-experimento.md) · [Unidad funcional →](./unidad-funcional.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

La capacidad se compra en unidades indivisibles.

Definición de trabajo de [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md).

## Por qué importa

En [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md), el tema «Unidades enteras» importa porque se paga la unidad aunque esté ociosa.

## Cómo funciona

Según [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md):

Se compran unidades enteras. Con los supuestos del autor (acelerador 3,00 USD/h con 2 000 peticiones/s por unidad; CPU 0,40 USD/h con 150 peticiones/s por unidad), el costo por millón de peticiones para una demanda sostenida `d` es `precio × unidades / (d × 3600) × 10⁶`, con `unidades = ⌈d / capacidad⌉`. Resultados de la tabla del experimento: demanda 20/s, acelerador 41,67 y CPU 5,56 USD por millón; 100/s, 8,33 y 1,11; 400/s, 2,08 y 0,83; 1 000/s, 0,83 y 0,78; 2 000/s, 0,42 y 0,78; 6 000/s, 0,42 y 0,74. El acelerador gana a partir de unos 1 000 a 2 000 peticiones por segundo *con estos supuestos*; por debajo, se paga una unidad entera que pasa ociosa.

Según [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md):

Entonces el costo se acerca al de la capacidad usada y la tabla de unidades enteras es menos pesimista; se cambia el modelo (precio por segundo × segundos usados) y se mantiene la sensibilidad. El arranque de la unidad sigue contando.

## Ejemplo

Ejemplo de [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md) (sección «Preguntas frecuentes»):

Entonces el costo se acerca al de la capacidad usada y la tabla de unidades enteras es menos pesimista; se cambia el modelo (precio por segundo × segundos usados) y se mantiene la sensibilidad. El arranque de la unidad sigue contando.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md)) son: Las medidas son de una CPU con NumPy; el modelo de costo usa supuestos del autor; no se ejecutó nada en un acelerador ni se consultó el precio de ningún proveedor. El siguiente paso, `SE-282`, estudia las fronteras para ejecutar código ajeno o cargas de varios clientes: procesos, contenedores, microVM y sandboxes, con lo que cuesta crear cada una y lo que contiene.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-280](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md), [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Latencia de cola](../l/latencia-de-cola.md), [Ley de Amdahl](../l/ley-de-amdahl.md), [Lote](../l/lote.md), [Precisión](../p/precision.md), [Sensibilidad](../s/sensibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Unidades enteras».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Una variable por experimento](./una-variable-por-experimento.md) · [Unidad funcional →](./unidad-funcional.md)
