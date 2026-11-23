# MicroVM

[↑ Glosario](../../README.md) · [← Microtarea](./microtarea.md) · [Migración →](./migracion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Máquina virtual con núcleo propio y un modelo mínimo de dispositivos.

Definición de trabajo de [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md).

## Por qué importa

La clase donde se define, [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), existe con este propósito: la clase existe para que elijas una frontera de aislamiento con una pregunta de ingeniería y no con una marca:

## Cómo funciona

Según [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md):

Las fronteras se ordenan por lo que comparten con el anfitrión. Un **hilo** comparte todo el proceso. Un **proceso** comparte el núcleo, pero tiene memoria virtual propia y puede restringirse con límites de CPU y memoria y un conjunto de llamadas de sistema permitidas. Un **contenedor** es un proceso con espacios de nombres (que limitan lo que ve: otros procesos, la red, los montajes, los usuarios), grupos de control (cuánto consume) y filtros de llamadas de sistema; comparte el núcleo. Un **núcleo de aplicación** como gVisor interpone en espacio de usuario un núcleo propio (el Sentry) que implementa las llamadas de sistema del contenedor y reduce las que llegan al núcleo real.

Según [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md):

El equipo de *Avisos* resuelve el caso del script de Python con una escala. Los scripts de una misma universidad corren en un proceso con entorno vacío, directorio temporal, tiempo máximo y límite de memoria, sin red, dentro de un contenedor con un perfil de llamadas de sistema restringido y por universidad. Antes de aceptar la solución, el equipo de seguridad pregunta qué comparte ese contenedor con el servicio de correo: el mismo anfitrión y el mismo núcleo. Como el script puede incluir bibliotecas de terceros y la amenaza incluye código arbitrario, deciden ejecutar esos contenedores en un conjunto de máquinas separado, sin las claves de correo, y evaluar un núcleo de aplicación en el siguiente trimestre.

## Ejemplo

Ejemplo de [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* resuelve el caso del script de Python con una escala. Los scripts de una misma universidad corren en un proceso con entorno vacío, directorio temporal, tiempo máximo y límite de memoria, sin red, dentro de un contenedor con un perfil de llamadas de sistema restringido y por universidad. Antes de aceptar la solución, el equipo de seguridad pregunta qué comparte ese contenedor con el servicio de correo: el mismo anfitrión y el mismo núcleo.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No se midieron contenedores ni microVM: el equipo tiene Docker Desktop, pero su arranque mide la capa de WSL2 y no la frontera aislada, de modo que un número obtenido así no sería honesto. ([SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md), [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Máquina virtual](./maquina-virtual.md), [Dispositivo](../d/dispositivo.md), [Modelo](./modelo.md), [Núcleo](../n/nucleo.md), [Causa común](../c/causa-comun.md), [Espacio de nombres](../e/espacio-de-nombres.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Microtarea](./microtarea.md) · [Migración →](./migracion.md)
