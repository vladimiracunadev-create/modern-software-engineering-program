# Espacio de nombres

[↑ Glosario](../../README.md) · [← Espacio de interpretaciones](./espacio-de-interpretaciones.md) · [Espacio de usuario →](./espacio-de-usuario.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Mecanismo del núcleo que da a un conjunto de procesos una vista propia de un recurso global.

Definición de trabajo de [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md): Vista restringida de un recurso del sistema (procesos, red, montajes, usuarios).

## Por qué importa

En [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md), el tema «Espacio de nombres» importa porque vincula rutas con objetos

## Cómo funciona

Según [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md):

Un contenedor no es un objeto del núcleo: es un proceso, o un grupo de procesos, al que el núcleo muestra una vista restringida mediante espacios de nombres y al que limita los recursos mediante grupos de control. Las especificaciones de OCI fijan cómo se describe su configuración, su sistema de archivos y su ciclo de vida, lo que permite que distintos entornos de ejecución cumplan el mismo contrato. Como comparte núcleo con el anfitrión y con los demás contenedores, una vulnerabilidad del núcleo o una configuración que concede demasiados privilegios puede dejar a un proceso salir de su vista. Un contenedor es excelente para empaquetar y repetir un entorno, y es una frontera de seguridad más débil que una máquina virtual.

Según [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md):

Las fronteras se ordenan por lo que comparten con el anfitrión. Un **hilo** comparte todo el proceso. Un **proceso** comparte el núcleo, pero tiene memoria virtual propia y puede restringirse con límites de CPU y memoria y un conjunto de llamadas de sistema permitidas. Un **contenedor** es un proceso con espacios de nombres (que limitan lo que ve: otros procesos, la red, los montajes, los usuarios), grupos de control (cuánto consume) y filtros de llamadas de sistema; comparte el núcleo. Un **núcleo de aplicación** como gVisor interpone en espacio de usuario un núcleo propio (el Sentry) que implementa las llamadas de sistema del contenedor y reduce las que llegan al núcleo real.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md):

Un actualizador escribe sobre el archivo final y se interrumpe, dejando JSON truncado. El equipo cambia a temporal en el mismo volumen, valida el contenido y reemplaza según la garantía documentada. Mantiene copia o recuperación porque atomicidad no equivale a persistencia ante toda falla.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)) son:

- **El archivo se busca en lugares distintos** — causa: se confundió directorio del script con directorio de trabajo. Corrección: elegir una base explícita y mostrarla en diagnóstico.
- **Una ruta portable se construye reemplazando `/`** — causa: se trataron rutas como cadenas. Corrección: usar la biblioteca de rutas y probar raíces, volúmenes y UNC.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un contenedor no es un objeto del núcleo: es un proceso, o un grupo de procesos, al que el núcleo muestra una vista restringida mediante espacios de nombres y al que limita los recursos mediante grupos de control. ([SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Mecanismo](../m/mecanismo.md), [Montaje](../m/montaje.md), [Núcleo](../n/nucleo.md), [Causa común](../c/causa-comun.md), [Directorio de trabajo](../d/directorio-de-trabajo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-282 — Contenedores, microVM y sandboxes](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), [SE-112](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-112-paquetes-modulos-y-publicacion/README.md), [SE-513](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md), [SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md), [SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md), [SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md), [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [namespaces(7)](https://man7.org/linux/man-pages/man7/namespaces.7.html) — espacios de nombres como vista propia de recursos globales; autoridad: manual de Linux (proyecto man-pages).
- [The Open Group — Pathname Resolution](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html#tag_04_16) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Naming Files, Paths, and Namespaces](https://learn.microsoft.com/windows/win32/fileio/naming-a-file) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Python documentation — pathlib](https://docs.python.org/3/library/pathlib.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Apple Platform Deployment — File system basics](https://support.apple.com/guide/deployment/intro-to-file-system-apd0b895e8e1/web) — delimita el contrato técnico que debe cumplirse al razonar sobre identidad de archivos mediante rutas, enlaces, metadatos y resolución.

---

[↑ Glosario](../../README.md) · [← Espacio de interpretaciones](./espacio-de-interpretaciones.md) · [Espacio de usuario →](./espacio-de-usuario.md)
