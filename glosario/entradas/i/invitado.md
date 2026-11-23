# Invitado

[↑ Glosario](../../README.md) · [← Inversión de prioridad](./inversion-de-prioridad.md) · [Inyección →](./inyeccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Sistema operativo ejecutado sobre hardware virtualizado.

Definición de trabajo de [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md).

## Por qué importa

En [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), el tema «VM» importa porque virtualiza hardware para un kernel invitado

## Cómo funciona

Según [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md):

Un hipervisor presenta CPU, memoria y dispositivos virtuales a un sistema invitado. El invitado ejecuta su propio kernel y gestiona sus procesos. El anfitrión conserva recursos físicos y una capa de control. Esto ofrece una frontera distinta a ejecutar otro proceso directamente, pero configuración, integraciones y vulnerabilidades todavía importan.

## Ejemplo

Ejemplo de [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) (sección «Ejemplo mínimo»):

Dentro de un contenedor, PID 1 no es necesariamente el PID 1 del anfitrión. La vista está aislada; el kernel subyacente puede ser el mismo. Esa pareja muestra aislamiento de espacio de nombres sin kernel invitado.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)) son:

- **“Está aislado porque está en un contenedor”** — causa: se ignoraron kernel, montajes y privilegios compartidos. Corrección: enumerar fronteras y capacidades efectivas.
- **Los datos desaparecen al recrear** — causa: se confundió capa escribible con almacenamiento persistente. Corrección: definir volumen y probar ciclo de vida.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)) son: No cubrimos orquestación, hardening avanzado ni escapes. Con el modelo de plataforma completo, la próxima clase integra los mecanismos en una reparación controlada de un entorno defectuoso.

## Relación con otros conceptos

- **Prerrequisito:** [Sistema operativo](../s/sistema-operativo.md).
- **Ver también:** [Sobre](../s/sobre.md), [Anfitrión](../a/anfitrion.md), [Bind mount](../b/bind-mount.md), [Contenedor](../c/contenedor.md), [Frontera](../f/frontera.md), [Hipervisor](../h/hipervisor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — WSL documentation](https://learn.microsoft.com/windows/wsl/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Linux kernel — namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Linux kernel — cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Docker documentation — storage](https://docs.docker.com/engine/storage/) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.

---

[↑ Glosario](../../README.md) · [← Inversión de prioridad](./inversion-de-prioridad.md) · [Inyección →](./inyeccion.md)
