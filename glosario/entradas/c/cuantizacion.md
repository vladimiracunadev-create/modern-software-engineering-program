# Cuantización

[↑ Glosario](../../README.md) · [← Cuantificador](./cuantificador.md) · [Cuarentena →](./cuarentena.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Representación de pesos con menos bits.

Definición de trabajo de [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md).

## Por qué importa

La clase donde se define, [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md), existe con este propósito: la clase existe para que dimensiones el servicio de un modelo con mediciones y no con la ficha del hardware.

## Cómo funciona

Según [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md):

Reducir los bits de los pesos disminuye memoria y, en hardware adecuado, el tiempo. En el modelo lineal de *Avisos-ML* con seis pesos, pasar de 64 bits (48 bytes) a 16 bits (12 bytes) o a enteros de 8 bits con escala (6 bytes) mantuvo el AUC en 0,862 y movió la salida en promedio 0,00035 y 0,0071. En un modelo de lenguaje, la cuantización a pocos bits reduce memoria de forma importante y su efecto en la calidad se mide con la evaluación de la tarea (`SE-561`); la fuente citada reporta pérdidas pequeñas en los modelos y las tareas que estudió, y eso no se traslada sin medirlo. La decisión de precisión se toma con la misma evaluación de `SE-604`, no con la del tamaño del archivo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En un modelo de lenguaje, la cuantización a pocos bits reduce memoria de forma importante y su efecto en la calidad se mide con la evaluación de la tarea (`SE-561`); la fuente citada reporta pérdidas pequeñas en los modelos y las tareas que estudió, y eso no se traslada sin medirlo. ([SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Representación](../r/representacion.md), [Acelerador](../a/acelerador.md), [Arranque en frío](../a/arranque-en-frio.md), [Latencia](../l/latencia.md), [Lote](../l/lote.md), [Lote dinámico](../l/lote-dinamico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cuantificador](./cuantificador.md) · [Cuarentena →](./cuarentena.md)
