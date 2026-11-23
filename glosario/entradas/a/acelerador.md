# Acelerador

[↑ Glosario](../../README.md) · [← Acción verificable](./accion-verificable.md) · [Aceptación desde el consumidor →](./aceptacion-desde-el-consumidor.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Hardware (GPU y similares) que ejecuta en paralelo masivo operaciones de matrices.

Definición de trabajo de [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md).

## Por qué importa

En [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md), el tema «Aceleradores» importa porque rinden con trabajo paralelo y memoria suficiente.

## Cómo funciona

Según [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md):

A partir de cierto tamaño el beneficio se acaba y la curva sube: con 1 024 peticiones el costo por petición fue 8,3 µs, más del triple que con 512. En una CPU con matrices que ya no caben en la caché, o en un acelerador con memoria limitada, agrandar el lote deja de ayudar y añade latencia. La forma de la curva depende del hardware, del modelo y de las bibliotecas, y por eso se mide con el modelo propio y la máquina de producción. El experimento mostró además tiempos irregulares en lotes pequeños (con dos peticiones el costo por petición fue mayor que con una), que reflejan la gestión de hilos de la biblioteca numérica: un motivo más para medir y no extrapolar.

Según [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md):

El equipo de *Avisos-ML* afronta el pico de cierre de notas. Mide el costo por petición contra el tamaño de lote en la máquina de producción y descubre que a partir de 512 el beneficio se acaba. Configura un lote dinámico de 256 con una espera máxima de 2 ms, para mantener el p99 por debajo de 5 ms, y fija una cola máxima de 2 000 peticiones; por encima, el servicio responde de inmediato con una clasificación de reglas (`SE-601`) y marca la respuesta como degradada. Simula el doble del tráfico del año anterior y verifica que el p99 se mantiene y que la tasa de degradación es menor del 1 %. No compra aceleradores: el modelo es pequeño y la utilización de CPU medida es del 35 %.

## Ejemplo

Ejemplo de [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* afronta el pico de cierre de notas. Mide el costo por petición contra el tamaño de lote en la máquina de producción y descubre que a partir de 512 el beneficio se acaba. Configura un lote dinámico de 256 con una espera máxima de 2 ms, para mantener el p99 por debajo de 5 ms, y fija una cola máxima de 2 000 peticiones; por encima, el servicio responde de inmediato con una clasificación de reglas (`SE-601`) y marca la respuesta como degradada.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En una CPU con matrices que ya no caben en la caché, o en un acelerador con memoria limitada, agrandar el lote deja de ayudar y añade latencia. ([SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Matriz](../m/matriz.md), [Operación](../o/operacion.md), [Arranque en frío](./arranque-en-frio.md), [Cuantización](../c/cuantizacion.md), [Latencia](../l/latencia.md), [Lote](../l/lote.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-280](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md), [SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md), [SE-605](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md), [SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Therac-25](../../../casos/fallo/therac-25.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Aceleradores».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Acción verificable](./accion-verificable.md) · [Aceptación desde el consumidor →](./aceptacion-desde-el-consumidor.md)
