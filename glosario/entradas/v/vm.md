# VM

[↑ Glosario](../../README.md) · [← VLAN](./vlan.md) · [Vocabulario controlado →](./vocabulario-controlado.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Define una máquina abstracta.

Es uno de los temas de [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), donde se enseña como «VM».

## Por qué importa

En [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), el tema «VM» importa porque define una máquina abstracta

En [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), el tema «VM» importa porque virtualiza hardware para un kernel invitado

## Cómo funciona

Según [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md):

La JVM especifica tipos, class files, instrucciones y áreas de ejecución, pero deja a la implementación políticas como el algoritmo de recolección. CPython tiene una máquina de bytecode propia con detalles distintos. “Corre en una VM” no informa automáticamente aislamiento de seguridad, portabilidad total ni costo.

Según [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md):

Una VM completa consume más recursos que un proceso aislado y puede reproducir un sistema diferente con mayor fidelidad. Una instantánea captura cierto estado de discos/memoria según la herramienta; no sustituye backup ni garantiza consistencia de aplicaciones.

## Ejemplo

Ejemplo de [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) (sección «Preguntas frecuentes»):

No en el modelo común: comparte kernel y aísla procesos; algunas plataformas añaden una VM debajo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **VM = seguridad** — causa: abstracción confundida con aislamiento. Corrección: evalúa permisos y sandbox real. ([SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- CPython tiene una máquina de bytecode propia con detalles distintos. “Corre en una VM” no informa automáticamente aislamiento de seguridad, portabilidad total ni costo. ([SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md))
- No en el modelo común: comparte kernel y aísla procesos; algunas plataformas añaden una VM debajo. ([SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Anfitrión](../a/anfitrion.md), [Bind mount](../b/bind-mount.md), [Contenedor](../c/contenedor.md), [Finalización](../f/finalizacion.md), [Frontera](../f/frontera.md), [Hipervisor](../h/hipervisor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — WSL documentation](https://learn.microsoft.com/windows/wsl/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Linux kernel — namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Linux kernel — cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Docker documentation — storage](https://docs.docker.com/engine/storage/) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.

---

[↑ Glosario](../../README.md) · [← VLAN](./vlan.md) · [Vocabulario controlado →](./vocabulario-controlado.md)
