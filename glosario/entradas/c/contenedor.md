# Contenedor

[↑ Glosario](../../README.md) · [← Contención](./contencion.md) · [Contenedor de desarrollo →](./contenedor-de-desarrollo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Un **contenedor** es un proceso, o un grupo de procesos, al que el núcleo muestra una vista restringida y cuyos recursos limita, sin un núcleo propio ([SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md)). [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) lo describe como un conjunto de procesos con vistas y límites que suele compartir el kernel. No es un objeto del núcleo ni una máquina virtual ligera: es una combinación de funciones del sistema operativo.

## Por qué importa

Permite empaquetar y repetir un entorno (dependencias, configuración, binarios) y arrancarlo en cualquier anfitrión compatible. Pero el error costoso es tomarlo por una frontera de seguridad fuerte: [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) lo califica como una frontera más débil que una máquina virtual. La decisión que cambia es dónde ejecutar código propio y dónde código ajeno.

## Cómo funciona

Dos mecanismos del núcleo ([SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md)):

- **Espacios de nombres:** dan al proceso una vista propia de procesos, red, montajes o usuarios.
- **Grupos de control (cgroups):** limitan recursos como memoria, procesos y CPU.

Las especificaciones de OCI fijan cómo se describe su configuración, su sistema de archivos y su ciclo de vida, de modo que distintos entornos de ejecución cumplen el mismo contrato. Como el contenedor comparte núcleo con el anfitrión y los demás contenedores, una vulnerabilidad del núcleo o una configuración con demasiados privilegios puede permitir que un proceso salga de su vista. De ahí que el aislamiento sea una propiedad de la configuración efectiva (montajes, capacidades, usuario), no de la palabra «contenedor» ([SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)).

## Ejemplo

Un contenedor sin límite de memoria que sufre una fuga consume el anfitrión: se aisló la vista, no el consumo. Ilustración:

```bash
docker run --memory=256m --pids-limit=100 imagen
```

Para ejecutar código ajeno, [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) recomienda una máquina virtual o microVM.

## Errores y confusiones comunes

- **Un contenedor agota la memoria del anfitrión.** Causa: se aisló la vista y no el consumo; corrección: límites de memoria y procesos ([SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md)).
- **Suponer que contiene código hostil.** Causa: confundir vista restringida con frontera de hardware; corrección: VM o microVM ([SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md)).
- **«Está aislado porque está en un contenedor».** Causa: se ignoraron kernel, montajes y privilegios compartidos; corrección: enumerar fronteras y capacidades efectivas ([SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)).

## Límites y cuándo no aplica

No sustituye a una VM cuando la amenaza es el propio código. No es portable entre núcleos distintos: un contenedor Linux necesita un núcleo Linux. Y una imagen empaqueta un entorno, no garantiza por sí sola reproducibilidad ni seguridad: ambas dependen de cómo se construya y se configure.

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
