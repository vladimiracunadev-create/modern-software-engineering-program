# Mapa

[↑ Glosario](../../README.md) · [← Mantenimiento y deterioro](./mantenimiento-y-deterioro.md) · [Mapa de contextos →](./mapa-de-contextos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Estructura de datos del núcleo compartida entre programas y espacio de usuario.

Definición de trabajo de [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md).

## Por qué importa

En [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md), el tema «Mapas y nulos» importa porque toda búsqueda puede fallar y el programa debe comprobarlo.

## Cómo funciona

Según [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md):

Un mapa es una estructura de datos del núcleo (arreglo, tabla hash, cola, entre otras) a la que el programa accede con ayudantes y el espacio de usuario con llamadas de sistema. La búsqueda en un mapa devuelve un puntero al valor *o nulo*. El verificador rastrea ese hecho: tras la búsqueda, `r0` tiene el tipo «valor de mapa o nulo» y cualquier desreferencia antes de compararlo con cero se rechaza. Es el mismo error que, en C, produce una caída en tiempo de ejecución; aquí se convierte en un rechazo en tiempo de carga. El caso que sorprende es el último de la lista: con una clave constante 0 sobre un mapa de arreglo de una entrada, la desreferencia sin comprobación fue **aceptada**.

## Ejemplo

Caso medido en la sección «Los mapas y la comprobación de nulo» de [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md):

Un mapa es una estructura de datos del núcleo (arreglo, tabla hash, cola, entre otras) a la que el programa accede con ayudantes y el espacio de usuario con llamadas de sistema. La búsqueda en un mapa devuelve un puntero al valor *o nulo*. El verificador rastrea ese hecho: tras la búsqueda, `r0` tiene el tipo «valor de mapa o nulo» y cualquier desreferencia antes de compararlo con cero se rechaza. Es el mismo error que, en C, produce una caída en tiempo de ejecución; aquí se convierte en un rechazo en tiempo de carga.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El caso que sorprende es el último de la lista: con una clave constante 0 sobre un mapa de arreglo de una entrada, la desreferencia sin comprobación fue **aceptada**. ([SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espacio de usuario](../e/espacio-de-usuario.md), [Estructura](../e/estructura.md), [Núcleo](../n/nucleo.md), [BPF_PROG_TEST_RUN](../b/bpf-prog-test-run.md), [Compilación JIT](../c/compilacion-jit.md), [EBPF](../e/ebpf.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (611 clases más lo mencionan; las que más):

[SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md), [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md), [SE-601](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md), [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [Slack](../../../casos/exito/slack.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Mantenimiento y deterioro](./mantenimiento-y-deterioro.md) · [Mapa de contextos →](./mapa-de-contextos.md)
