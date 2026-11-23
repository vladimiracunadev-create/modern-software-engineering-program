# Transferencia

[↑ Glosario](../../README.md) · [← Transacción única de clave y efecto](./transaccion-unica-de-clave-y-efecto.md) · [Transferencia de estado en el evento →](./transferencia-de-estado-en-el-evento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Movimiento de datos entre memoria del anfitrión y del acelerador.

Definición de trabajo de [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md).

## Por qué importa

En [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md), el tema «Transferencia» importa porque mover datos al acelerador y de vuelta también cuesta.

## Cómo funciona

Según [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md):

Un acelerador discreto tiene su propia memoria. Para usarlo hay que mover datos desde la memoria del anfitrión y devolver el resultado, y ese movimiento se hace por un bus mucho más lento que la memoria del propio acelerador. La consecuencia de diseño es que conviene hacer *mucho trabajo por dato transferido* y mantener los datos en el acelerador entre operaciones. Una operación elemental sola, aunque sea 100 veces más rápida en el acelerador, puede perderse en la transferencia. `SE-281` pone números a esa pérdida con la ley de Amdahl ampliada con un término de transferencia.

Según [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md):

El equipo de *Avisos* revisa el cálculo de riesgo antes de pedir presupuesto para un acelerador. Primero vectoriza el bucle de Python con NumPy: el tiempo nocturno baja de forma que cabe en la ventana sin hardware nuevo. Después mide qué parte del tiempo restante corresponde a leer las tablas de historial: los datos están organizados por estudiante y cada cálculo lee campos dispersos. Reorganizan los datos por columnas y el tiempo baja de nuevo. Entonces estiman el caso del panel bajo demanda: una petición evalúa a un grupo de 40 estudiantes y necesita responder en menos de 200 ms; un acelerador requeriría mover esos 40 registros y traerlos de vuelta por cada petición, y el trabajo por petición es demasiado pequeño para amortizar la transferencia.

## Ejemplo

Ejemplo de [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* revisa el cálculo de riesgo antes de pedir presupuesto para un acelerador. Primero vectoriza el bucle de Python con NumPy: el tiempo nocturno baja de forma que cabe en la ventana sin hardware nuevo. Después mide qué parte del tiempo restante corresponde a leer las tablas de historial: los datos están organizados por estudiante y cada cálculo lee campos dispersos. Reorganizan los datos por columnas y el tiempo baja de nuevo.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- `SE-281` pone números a esa pérdida con la ley de Amdahl ampliada con un término de transferencia. ([SE-280](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Acelerador](../a/acelerador.md), [Anfitrión](../a/anfitrion.md), [Bloque y rejilla](../b/bloque-y-rejilla.md), [Coalescencia](../c/coalescencia.md), [Divergencia](../d/divergencia.md), [Intensidad aritmética](../i/intensidad-aritmetica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (610 clases más lo mencionan; las que más):

[SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), [SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md), [SE-009](../../../classes/part-00-ingenieria-de-software-como-profesion/se-009-sostenibilidad-inclusion-y-responsabilidad-social/README.md), [SE-071](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md), [SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md), [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md), [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Transacción única de clave y efecto](./transaccion-unica-de-clave-y-efecto.md) · [Transferencia de estado en el evento →](./transferencia-de-estado-en-el-evento.md)
