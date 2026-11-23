# Divergencia

[↑ Glosario](../../README.md) · [← Distributed Systems Engineer](./distributed-systems-engineer.md) · [Divide y vencerás →](./divide-y-venceras.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Situación en que los hilos de un grupo toman caminos distintos y el grupo ejecuta ambos.

Definición de trabajo de [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md).

## Por qué importa

En [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md), el tema «Divergencia» importa porque si un grupo toma caminos distintos, ejecuta ambos.

## Cómo funciona

Según [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md):

Si dentro de un grupo de 32 hilos algunos toman el camino A de una rama y otros el B, el grupo ejecuta ambos caminos en serie, con los hilos que no corresponden inactivos. El modelo de la clase (semilla 48, 20 000 repeticiones) supone que cada hilo toma el camino A con probabilidad `p` de forma independiente y cuenta con qué frecuencia el grupo necesita ejecutar ambos caminos. Con `p = 0` nunca (costo relativo 1,00); con `p = 0,01` en el 27,8 % de los grupos (1,28); con `p = 0,05` en el 80,4 % (1,80); con `p = 0,5` en todos (2,00). La lectura útil es la segunda fila:

## Ejemplo

Caso medido en la sección «Divergencia: cuando el grupo no está de acuerdo» de [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md):

Si dentro de un grupo de 32 hilos algunos toman el camino A de una rama y otros el B, el grupo ejecuta ambos caminos en serie, con los hilos que no corresponden inactivos. El modelo de la clase (semilla 48, 20 000 repeticiones) supone que cada hilo toma el camino A con probabilidad `p` de forma independiente y cuenta con qué frecuencia el grupo necesita ejecutar ambos caminos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md)) son: No se ejecutó ningún núcleo en una GPU; las medidas son de CPU y NumPy y la divergencia es un modelo con semilla 48. El siguiente paso, `SE-281`, lleva el modelo al terreno económico: qué rendimiento y qué costo por petición se obtienen según el tamaño del lote, la precisión y la utilización, con parámetros del autor para los precios.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Hilo](../h/hilo.md), [Bloque y rejilla](../b/bloque-y-rejilla.md), [Coalescencia](../c/coalescencia.md), [Intensidad aritmética](../i/intensidad-aritmetica.md), [Proxy](../p/proxy.md), [Roofline](../r/roofline.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (52 clases más lo mencionan; las que más):

[SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md), [SE-346](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md), [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md), [SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Distributed Systems Engineer](./distributed-systems-engineer.md) · [Divide y vencerás →](./divide-y-venceras.md)
