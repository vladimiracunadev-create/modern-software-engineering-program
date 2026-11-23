# WASI

[↑ Glosario](../../README.md) · [← Warp](./warp.md) · [Webhook →](./webhook.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Interfaz de sistema estandarizada para módulos, basada en capacidades.

Definición de trabajo de [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md).

## Por qué importa

En [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), el tema «WASI y capacidades» importa porque el sistema de archivos se concede por directorio, no por ruta global.

## Cómo funciona

Según [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md):

WASI (WebAssembly System Interface) es un conjunto de importaciones estandarizadas para lo que casi todos los programas necesitan: salida estándar, archivos, reloj, aleatoriedad, argumentos. Su diseño se basa en capacidades: un módulo no abre «la ruta /etc/passwd», abre una ruta relativa a un descriptor que ya posee. El anfitrión *preabre* directorios y los entrega con un nombre. En el experimento, un mismo módulo imprime «hola desde wasm» por su salida estándar y luego intenta `path_open('secreto.txt')` sobre el descriptor 3. Sin ningún directorio concedido, la llamada devuelve el código WASI 8 (`EBADF`: ese descriptor no existe); con el directorio temporal concedido como `/datos`, devuelve 0 (abierto). No hay una instrucción para nombrar una ruta absoluta del anfitrión: el alcance del módulo es el conjunto de descriptores que recibió.

Según [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md):

No. WASI toma ideas de POSIX (descriptores, archivos, reloj) pero cambia el modelo: no hay ruta global ni usuario ni permisos del sistema; hay capacidades que el anfitrión concede.

## Ejemplo

Ejemplo de [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md) (sección «Preguntas frecuentes»):

No. WASI toma ideas de POSIX (descriptores, archivos, reloj) pero cambia el modelo: no hay ruta global ni usuario ni permisos del sistema; hay capacidades que el anfitrión concede.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Sin ningún directorio concedido, la llamada devuelve el código WASI 8 (`EBADF`: ese descriptor no existe); con el directorio temporal concedido como `/datos`, devuelve 0 (abierto). ([SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Interfaz](../i/interfaz.md), [Módulo](../m/modulo.md), [Combustible](../c/combustible.md), [Importación](../i/importacion.md), [Instancia](../i/instancia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Warp](./warp.md) · [Webhook →](./webhook.md)
