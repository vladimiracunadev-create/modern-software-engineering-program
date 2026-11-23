# Anfitrión

[↑ Glosario](../../README.md) · [← Andamiaje](./andamiaje.md) · [Anomalía de actualización →](./anomalia-de-actualizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Sistema que posee o administra recursos físicos.

Definición de trabajo de [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md).

## Por qué importa

La clase donde se define, [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), existe con este propósito: la clase existe para distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.

## Cómo funciona

Según [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md):

Un hipervisor presenta CPU, memoria y dispositivos virtuales a un sistema invitado. El invitado ejecuta su propio kernel y gestiona sus procesos. El anfitrión conserva recursos físicos y una capa de control. Esto ofrece una frontera distinta a ejecutar otro proceso directamente, pero configuración, integraciones y vulnerabilidades todavía importan.

Según [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md):

No. Una máquina virtual ejecuta su propio kernel; un contenedor es un proceso (o grupo de procesos) del anfitrión, con una vista aislada. Esa diferencia explica que el contenedor arranque más rápido y que no pueda ejecutar un kernel distinto del anfitrión.

## Ejemplo

Ejemplo de [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) (sección «Ejemplo mínimo»):

Dentro de un contenedor, PID 1 no es necesariamente el PID 1 del anfitrión. La vista está aislada; el kernel subyacente puede ser el mismo. Esa pareja muestra aislamiento de espacio de nombres sin kernel invitado.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)) son:

- **“Está aislado porque está en un contenedor”** — causa: se ignoraron kernel, montajes y privilegios compartidos. Corrección: enumerar fronteras y capacidades efectivas.
- **Los datos desaparecen al recrear** — causa: se confundió capa escribible con almacenamiento persistente. Corrección: definir volumen y probar ciclo de vida.

Según [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md): «Aislamiento» no es sinónimo de «seguridad»: el anfitrión, el kernel y los volúmenes montados siguen formando parte del límite de confianza, y los datos dentro de un contenedor pueden persistir en volúmenes más allá de su vida.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- «Aislamiento» no es sinónimo de «seguridad»: el anfitrión, el kernel y los volúmenes montados siguen formando parte del límite de confianza, y los datos dentro de un contenedor pueden persistir en volúmenes más allá de su vida. ([SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Recurso](../r/recurso.md), [Bind mount](../b/bind-mount.md), [Contenedor](../c/contenedor.md), [Frontera](../f/frontera.md), [Hipervisor](../h/hipervisor.md), [Imagen](../i/imagen.md).
- **Se confunde con:** «Aislamiento» no es sinónimo de «seguridad»: el anfitrión, el kernel y los volúmenes montados siguen formando parte del límite de confianza, y los datos dentro de un contenedor pueden persistir en volúmenes más allá de su vida.

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (16 clases más lo mencionan; las que más):

[SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md).

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — WSL documentation](https://learn.microsoft.com/windows/wsl/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Linux kernel — namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Linux kernel — cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Docker documentation — storage](https://docs.docker.com/engine/storage/) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.

---

[↑ Glosario](../../README.md) · [← Andamiaje](./andamiaje.md) · [Anomalía de actualización →](./anomalia-de-actualizacion.md)
