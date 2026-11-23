# Contenedor

[↑ Glosario](../../README.md) · [← Contención](./contencion.md) · [Contenedor de desarrollo →](./contenedor-de-desarrollo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Proceso o grupo de procesos al que el núcleo muestra una vista restringida y limita los recursos, sin un núcleo propio.

Definición de trabajo de [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md): Conjunto de procesos con vistas y límites que suele compartir kernel.

## Por qué importa

En [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), el tema «Contenedores» importa porque son procesos del anfitrión con vista y recursos acotados; arrancan casi como un proceso.

En [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), el tema «Contenedor» importa porque aísla procesos sobre kernel compartido

## Cómo funciona

Según [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), en la sección «Contenedores»:

Un contenedor no es un objeto del núcleo: es un proceso, o un grupo de procesos, al que el núcleo muestra una vista restringida mediante espacios de nombres y al que limita los recursos mediante grupos de control. Las especificaciones de OCI fijan cómo se describe su configuración, su sistema de archivos y su ciclo de vida, lo que permite que distintos entornos de ejecución cumplan el mismo contrato. Como comparte núcleo con el anfitrión y con los demás contenedores, una vulnerabilidad del núcleo o una configuración que concede demasiados privilegios puede dejar a un proceso salir de su vista. Un contenedor es excelente para empaquetar y repetir un entorno, y es una frontera de seguridad más débil que una máquina virtual.

## Ejemplo

Ejemplo de [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma separa tres piezas con fronteras distintas. La aplicación web y el servicio de informes, del mismo equipo y con código revisado, corren como contenedores con límites de CPU y memoria y un sistema de archivos de solo lectura, en el mismo anfitrión. El corrector de entregas, que ejecuta código de estudiantes, corre cada ejecución en una unidad con su propio núcleo (una microVM o una máquina virtual efímera), sin red y con un tiempo máximo, y se destruye al terminar. La base de datos está en un servicio gestionado y no comparte anfitrión con ninguna de las anteriores.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un contenedor agota la memoria del anfitrión** — causa: se aisló la vista y no se limitó el consumo. Corrección: fijar límite de memoria y de procesos. ([SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md))
- **Se asume que un contenedor contiene código hostil** — causa: se confunde la vista restringida con una frontera de hardware. Corrección: usar una máquina virtual o microVM para código ajeno. ([SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md))
- **“Está aislado porque está en un contenedor”** — causa: se ignoraron kernel, montajes y privilegios compartidos. Corrección: enumerar fronteras y capacidades efectivas. ([SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un contenedor no es un objeto del núcleo: es un proceso, o un grupo de procesos, al que el núcleo muestra una vista restringida mediante espacios de nombres y al que limita los recursos mediante grupos de control. ([SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Kernel](../k/kernel.md).
- **Ver también:** [Conjunto](./conjunto.md), [Límite](../l/limite.md), [Núcleo](../n/nucleo.md), [Proceso](../p/proceso.md), [Anfitrión](../a/anfitrion.md), [Bind mount](../b/bind-mount.md).
- **Se confunde con:** «Aislamiento» no es sinónimo de «seguridad»: el anfitrión, el kernel y los volúmenes montados siguen formando parte del límite de confianza, y los datos dentro de un contenedor pueden persistir en volúmenes más allá de su vida.

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (92 clases más lo mencionan; las que más):

[SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-104](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md), [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), [SE-108](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md), [SE-175](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md), [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Contenedores».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OCI Runtime Specification](https://github.com/opencontainers/runtime-spec) — configuración y ciclo de vida de un contenedor; autoridad: Open Container Initiative.
- [Linux kernel — namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Linux kernel — cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Docker documentation — storage](https://docs.docker.com/engine/storage/) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Firecracker: Lightweight Virtualization for Serverless Applications](https://www.usenix.org/conference/nsdi20/presentation/agache) — microVMs como compromiso entre aislamiento y arranque; autoridad: artículo de USENIX NSDI 2020.

---

[↑ Glosario](../../README.md) · [← Contención](./contencion.md) · [Contenedor de desarrollo →](./contenedor-de-desarrollo.md)
