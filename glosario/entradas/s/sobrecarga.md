# Sobrecarga

[↑ Glosario](../../README.md) · [← Sobreasignación](./sobreasignacion.md) · [Sobremuestreo →](./sobremuestreo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

La **sobrecarga** es una carga mayor que la capacidad del servicio ([SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md), en el contexto de servir modelos).

## Por qué importa

Cuando la demanda supera la capacidad, la cola crece mientras dura la sobrecarga y la latencia de cola deja de estar acotada. La decisión es si hace falta una política de sobrecarga, procesamiento por lotes o nada.

## Cómo funciona

[SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) simula un servicio de modelo con y sin lotes dinámicos. Con una carga igual a la capacidad sin lotes, el p99 fue 9,4 ms sin lotes y 2,3 ms con lote dinámico de 2 ms y 64. Con el doble de la capacidad, el servicio sin lotes acumuló una cola de la que el p99 llegó a 858 ms (y crece mientras dura la sobrecarga), mientras que el servicio con lote dinámico mantuvo un p99 de 1,9 ms, porque su capacidad en peticiones por segundo es mucho mayor. Con cuatro veces la capacidad, 1 291 ms contra 1,1 ms.

## Ejemplo

La clase pide medir el costo por petición contra el tamaño de lote, localizar el óptimo, calcular cuánta espera cabe en el SLO y simular el doble de tráfico.

## Errores y confusiones comunes

Probar solo con la carga esperada; creer que más lote siempre ayuda, cuando la espera de formar el lote consume el SLO.

## Límites y cuándo no aplica

Son resultados de una simulación. Frente a una sobrecarga sostenida, ninguna técnica de lotes sustituye al descarte de carga o a más capacidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Servicio](./servicio.md), [Acelerador](../a/acelerador.md), [Arranque en frío](../a/arranque-en-frio.md), [Cuantización](../c/cuantizacion.md), [Latencia](../l/latencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (25 clases más lo mencionan; las que más):

[SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md), [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Sobreasignación](./sobreasignacion.md) · [Sobremuestreo →](./sobremuestreo.md)
