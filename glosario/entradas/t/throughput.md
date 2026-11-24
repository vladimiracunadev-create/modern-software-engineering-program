# Throughput

[↑ Glosario](../../README.md) · [← Throttle](./throttle.md) · [Tiempo agotado ambiguo →](./tiempo-agotado-ambiguo.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

El **throughput** (rendimiento, caudal) es la cantidad de trabajo completado por unidad de tiempo: peticiones atendidas por segundo ([SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md)), unidades completadas por tiempo ([SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md)) o, en redes, la cantidad *útil* transferida por unidad de tiempo ([SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md)). Es distinto de la **latencia** (cuánto tarda una unidad) y de la **utilización** (cuánto ocupa un recurso).

## Por qué importa

Es la medida de cuánta carga soporta un sistema, pero se optimiza a costa de otras: [SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) advierte que mejorar una de las tres medidas puede empeorar otra. Quien solo persigue throughput puede degradar la latencia que sienten las personas. Cambia lo que se declara como objetivo: una capacidad y una latencia máxima, no un número aislado.

## Cómo funciona

[SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) fija el vocabulario: latencia mide cuánto tarda una unidad; throughput, cuántas se completan por tiempo; utilización, cuánto ocupa un recurso. La carga incluye tamaño, distribución, concurrencia, estado y criterio de corrección.

[SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md) muestra la causa de un compromiso clásico: una llamada a un cálculo tiene un costo fijo (lanzar, sincronizar, mover datos) y otro variable por elemento. Agrupar peticiones en un lote reparte el costo fijo y sube el throughput, pero cada petición espera a que el lote se llene y termine. En la CPU del laboratorio, una capa densa de 1024×1024 en 32 bits dio, por lote: lote 1, 0,27 ms y unas 3 700 peticiones por segundo; lote 16, 4,8 ms y 3 300; lote 64, 7,9 ms y 8 100; lote 256, 14,3 ms y 17 900. El throughput sube casi cinco veces mientras la latencia por lote se multiplica por más de cincuenta.

En redes ([SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md)), el throughput es lo que realmente llega útil al destino, no el ancho de banda teórico del enlace.

## Ejemplo

```text
demanda: 200 peticiones/s ; lote 256 -> llenar el lote tarda > 1 s
=> el throughput del lote grande no se materializa y la latencia crece
```

Ilustración de cálculo: throughput = n / tiempo = 256 / 0,0143 s ≈ 17 900 peticiones/s en el experimento de lote 256.

## Errores y confusiones comunes

- **Confundirlo con ancho de banda teórico.** El throughput es lo útil y efectivamente transferido ([SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md)).
- **Maximizar throughput sin mirar latencia.** El lote óptimo es el que cabe en el tiempo de espera que el objetivo de latencia permite ([SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md)).
- **Comparar throughput de versiones que dan resultados distintos.** No es un benchmark válido ([SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md)).

## Límites y cuándo no aplica

Con baja demanda el throughput alcanzable es irrelevante: manda la latencia. Las cifras de [SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md) son de una CPU y una capa concretas. Y el throughput máximo medido en un banco no se sostiene en producción si hay contención, colas o dependencias (véase *utilización* y *ley de Little*).

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Benchmark](../b/benchmark.md), [Correlación](../c/correlacion.md), [Cuello de botella](../c/cuello-de-botella.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-022 — Rendimiento, consumo energético y límites físicos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-046 — Captura, medición y diagnóstico de tráfico](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md), [SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md).

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 1122 — Requirements for Internet Hosts: Communication Layers](https://www.rfc-editor.org/rfc/rfc1122) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Throttle](./throttle.md) · [Tiempo agotado ambiguo →](./tiempo-agotado-ambiguo.md)
