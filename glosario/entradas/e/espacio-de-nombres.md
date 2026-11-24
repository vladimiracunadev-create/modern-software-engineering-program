# Espacio de nombres

[↑ Glosario](../../README.md) · [← Espacio de interpretaciones](./espacio-de-interpretaciones.md) · [Espacio de usuario →](./espacio-de-usuario.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Un **espacio de nombres** (*namespace*) del núcleo es el mecanismo que da a un conjunto de procesos una vista propia de un recurso global ([SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md)): otros procesos, la red, los montajes o los usuarios ([SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md)). Es una pieza del sistema operativo, no una carpeta ni un paquete de lenguaje. Otras disciplinas usan «espacio de nombres» para evitar colisiones de identificadores; aquí el sentido es de aislamiento de vista.

## Por qué importa

Es lo que permite que un contenedor «crea» que es el único proceso de su máquina, que tiene su propia red y su propio sistema de archivos. Entender qué aísla y qué no cambia una decisión de seguridad: la vista restringida no es una frontera de hardware ([SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md)).

## Cómo funciona

Según [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), un contenedor es un proceso, o un grupo de procesos, al que el núcleo muestra una vista restringida mediante espacios de nombres y al que limita los recursos mediante **grupos de control** (otro mecanismo, que decide cuánto se consume). [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md) ordena las fronteras por lo que comparten con el anfitrión:

- un **hilo** comparte todo el proceso;
- un **proceso** comparte el núcleo pero tiene memoria virtual propia;
- un **contenedor** es un proceso con espacios de nombres (lo que ve), grupos de control (cuánto consume) y filtros de llamadas de sistema; sigue compartiendo el núcleo;
- un **núcleo de aplicación** como gVisor interpone un núcleo propio en espacio de usuario que reduce las llamadas que llegan al núcleo real.

La causa de la debilidad es que los espacios de nombres cambian lo que el proceso *ve*, no lo que el núcleo *ejecuta*.

## Ejemplo

En Linux, `unshare` crea un proceso con un espacio de nombres de procesos propio:

```bash
sudo unshare --pid --fork --mount-proc ps aux
```

El `ps` dentro solo lista sus propios procesos, aunque el anfitrión ejecute miles. Es la vista, no un núcleo nuevo.

## Errores y confusiones comunes

- **Creer que equivale a una máquina virtual.** Comparte núcleo; una vulnerabilidad del núcleo atraviesa la vista ([SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md)).
- **Confundir vista con límite de consumo.** Sin grupos de control, un proceso aislado agota la memoria del anfitrión.
- **Confundirlo con el directorio de trabajo o los alcances de nombres de un lenguaje.** Son conceptos de capas distintas ([SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) trata el directorio de trabajo).

## Límites y cuándo no aplica

No protege contra código hostil: para eso [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) recomienda una máquina virtual o microVM. Su eficacia depende de la configuración (montajes, privilegios, capacidades concedidas). Y existen espacios de nombres solo en núcleos que los implementan (Linux); en otros sistemas el aislamiento se logra con mecanismos distintos.

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
