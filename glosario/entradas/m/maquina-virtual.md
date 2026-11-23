# Máquina virtual

[↑ Glosario](../../README.md) · [← Máquina de estados](./maquina-de-estados.md) · [Marca de agua →](./marca-de-agua.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Arquitectura abstracta ejecutada por software o hardware.

Definición de trabajo de [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md).

## Por qué importa

La clase donde se define, [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), existe con este propósito: la clase existe para razonar sobre carga, memoria y recolección separando especificación de estrategia del runtime.

## Cómo funciona

Según [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md):

No. Una máquina virtual de lenguaje ejecuta bytecode con una semántica definida, pero el aislamiento de seguridad exige un mecanismo añadido (permisos, un gestor de seguridad, procesos separados, contenedores). Ejecutar código no confiable en la misma máquina virtual que tus datos no aísla nada por sí mismo.

## Ejemplo

Ejemplo de [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md) (sección «Preguntas frecuentes»):

No. Una máquina virtual de lenguaje ejecuta bytecode con una semántica definida, pero el aislamiento de seguridad exige un mecanismo añadido (permisos, un gestor de seguridad, procesos separados, contenedores). Ejecutar código no confiable en la misma máquina virtual que tus datos no aísla nada por sí mismo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md)) son:

- **toda memoria creciente = fuga GC** — causa: causas no separadas. Corrección: inspecciona alcanzabilidad, caché y memoria nativa.
- **`del` = liberación física** — causa: niveles confundidos. Corrección: habla de referencias y política del runtime.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Ejecutar código no confiable en la misma máquina virtual que tus datos no aísla nada por sí mismo. ([SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Arquitectura](../a/arquitectura.md), [Finalización](../f/finalizacion.md), [Objeto alcanzable](../o/objeto-alcanzable.md), [Raíz](../r/raiz.md), [Runtime](../r/runtime.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (20 clases más lo mencionan; las que más):

[SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-104](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md), [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Discord](../../../casos/exito/discord.md), [Cloudflare](../../../casos/exito/cloudflare.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Máquina de estados](./maquina-de-estados.md) · [Marca de agua →](./marca-de-agua.md)
