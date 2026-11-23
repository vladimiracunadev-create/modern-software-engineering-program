# Hipervisor

[↑ Glosario](../../README.md) · [← Hilo](./hilo.md) · [Hipótesis →](./hipotesis.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Programa que presenta hardware virtual a uno o varios sistemas invitados y los aísla entre sí.

Definición de trabajo de [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md): Capa que administra máquinas virtuales y recursos virtualizados.

## Por qué importa

La clase donde se define, [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), existe con este propósito: la clase existe para que distingas tres fronteras que suelen llamarse «aislamiento» sin serlo en el mismo grado: la que separa procesos dentro de un sistema operativo, la que separa contenedores que comparten un núcleo y la que separa máquinas virtuales con su propio núcleo.

## Cómo funciona

Según [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md):

Una máquina virtual ejecuta un sistema operativo completo sobre hardware que un monitor, el hipervisor, presenta como propio. El núcleo invitado no comparte memoria ni estructuras del núcleo anfitrión, y la separación la aplican instrucciones del procesador pensadas para virtualizar. La superficie por la que un invitado puede alcanzar al anfitrión es la interfaz del monitor: dispositivos emulados, llamadas al hipervisor. Es una superficie más pequeña que la de todas las llamadas al sistema de un núcleo, y por eso las máquinas virtuales se consideran la frontera fuerte entre inquilinos que no se conocen. El precio es que cada una carga su propio sistema operativo: memoria base, arranque medido en segundos y un disco.

Según [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md):

Un hipervisor presenta CPU, memoria y dispositivos virtuales a un sistema invitado. El invitado ejecuta su propio kernel y gestiona sus procesos. El anfitrión conserva recursos físicos y una capa de control. Esto ofrece una frontera distinta a ejecutar otro proceso directamente, pero configuración, integraciones y vulnerabilidades todavía importan.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md):

El equipo de la plataforma separa tres piezas con fronteras distintas. La aplicación web y el servicio de informes, del mismo equipo y con código revisado, corren como contenedores con límites de CPU y memoria y un sistema de archivos de solo lectura, en el mismo anfitrión. El corrector de entregas, que ejecuta código de estudiantes, corre cada ejecución en una unidad con su propio núcleo (una microVM o una máquina virtual efímera), sin red y con un tiempo máximo, y se destruye al terminar.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md)) son:

- **Un contenedor agota la memoria del anfitrión** — causa: se aisló la vista y no se limitó el consumo. Corrección: fijar límite de memoria y de procesos.
- **Se asume que un contenedor contiene código hostil** — causa: se confunde la vista restringida con una frontera de hardware. Corrección: usar una máquina virtual o microVM para código ajeno.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md)) son: Las definiciones son operativas para la plataforma de entregas. Los productos usan estos términos con matices (por ejemplo, contenedores que se ejecutan dentro de una máquina virtual ligera) y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en un equipo con Windows y Ubuntu (WSL2) y los tiempos cambiaron entre ejecuciones; el cálculo de densidad es un modelo con sobrecostes supuestos. No se arrancó ninguna máquina virtual ni contenedor, no se probaron cuotas ni cgroups, y no se evaluó ninguna vulnerabilidad de escape. La siguiente clase mira quién decide dónde corre cada unidad y qué hace cuando alguna falla.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa](../c/capa.md), [Invitado](../i/invitado.md), [Recurso](../r/recurso.md), [Anfitrión](../a/anfitrion.md), [Bind mount](../b/bind-mount.md), [Contenedor](../c/contenedor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [namespaces(7)](https://man7.org/linux/man-pages/man7/namespaces.7.html) — espacios de nombres como vista propia de recursos globales; autoridad: manual de Linux (proyecto man-pages).
- [Control Group v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) — grupos de control y distribución de recursos; autoridad: documentación del núcleo Linux.
- [OCI Runtime Specification](https://github.com/opencontainers/runtime-spec) — configuración y ciclo de vida de un contenedor; autoridad: Open Container Initiative.
- [Firecracker: Lightweight Virtualization for Serverless Applications](https://www.usenix.org/conference/nsdi20/presentation/agache) — microVMs como compromiso entre aislamiento y arranque; autoridad: artículo de USENIX NSDI 2020.
- [Python: subprocess](https://docs.python.org/3/library/subprocess.html) — API usada para medir procesos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Hilo](./hilo.md) · [Hipótesis →](./hipotesis.md)
