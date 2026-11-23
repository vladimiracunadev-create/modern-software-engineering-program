# Lote dinámico

[↑ Glosario](../../README.md) · [← Lote](./lote.md) · [Low-code →](./low-code.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Agrupación de peticiones hasta un tamaño o una espera máximos.

Definición de trabajo de [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md).

## Por qué importa

En [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md), el tema «Lote dinámico» importa porque intercambia latencia por rendimiento.

## Cómo funciona

Según [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md):

Un lote dinámico agrupa las peticiones que llegan hasta alcanzar un tamaño máximo o agotar una espera máxima, lo que ocurra primero. Se simularon 40 000 llegadas de Poisson a una tasa del 80 % de la capacidad sin lotes (18 391 por segundo, con una capacidad sin lotes de 22 989), con el tiempo de servicio medido (interpolado). Con 0 ms de espera y lote de 1, el p50 fue 0,10 ms y el p99 0,47 ms. Con 0,5 ms de espera y lote máximo de 8: 0,32 y 0,64 ms. Con 2 ms y lote de 32: 1,12 y 2,21 ms. Con 5 ms y 64: 2,03 y 4,25 ms. Con 20 ms y 256: 7,67 y 15,16 ms.

Según [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md):

El equipo de *Avisos-ML* afronta el pico de cierre de notas. Mide el costo por petición contra el tamaño de lote en la máquina de producción y descubre que a partir de 512 el beneficio se acaba. Configura un lote dinámico de 256 con una espera máxima de 2 ms, para mantener el p99 por debajo de 5 ms, y fija una cola máxima de 2 000 peticiones; por encima, el servicio responde de inmediato con una clasificación de reglas (`SE-601`) y marca la respuesta como degradada. Simula el doble del tráfico del año anterior y verifica que el p99 se mantiene y que la tasa de degradación es menor del 1 %. No compra aceleradores: el modelo es pequeño y la utilización de CPU medida es del 35 %.

## Ejemplo

Ejemplo de [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* afronta el pico de cierre de notas. Mide el costo por petición contra el tamaño de lote en la máquina de producción y descubre que a partir de 512 el beneficio se acaba. Configura un lote dinámico de 256 con una espera máxima de 2 ms, para mantener el p99 por debajo de 5 ms, y fija una cola máxima de 2 000 peticiones; por encima, el servicio responde de inmediato con una clasificación de reglas (`SE-601`) y marca la respuesta como degradada.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El lote dinámico no es una optimización gratuita: se paga con latencia a cambio de capacidad, y si la capacidad sobra, es un costo sin beneficio. ([SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agrupación](../a/agrupacion.md), [Espera](../e/espera.md), [Acelerador](../a/acelerador.md), [Arranque en frío](../a/arranque-en-frio.md), [Cuantización](../c/cuantizacion.md), [Latencia](./latencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Lote](./lote.md) · [Low-code →](./low-code.md)
