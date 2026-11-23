# Namespace

[↑ Glosario](../../README.md) · [← N+1](./n-mas-1.md) · [NaN →](./nan.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Mecanismo que proporciona a procesos una vista aislada de un recurso del kernel.

Definición de trabajo de [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md).

## Por qué importa

La clase donde se define, [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), existe con este propósito: la clase existe para distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.

## Cómo funciona

[SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md):

Un repositorio se compila en WSL sobre `/mnt/c` y las operaciones de muchos archivos son lentas. Una prueba equivalente dentro del sistema de archivos Linux mejora. El equipo mueve el árbol activo y conserva interoperabilidad solo para artefactos necesarios, documentando el costo de frontera.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)) son:

- **“Está aislado porque está en un contenedor”** — causa: se ignoraron kernel, montajes y privilegios compartidos. Corrección: enumerar fronteras y capacidades efectivas.
- **Los datos desaparecen al recrear** — causa: se confundió capa escribible con almacenamiento persistente. Corrección: definir volumen y probar ciclo de vida.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)) son: No cubrimos orquestación, hardening avanzado ni escapes. Con el modelo de plataforma completo, la próxima clase integra los mecanismos en una reparación controlada de un entorno defectuoso.

## Relación con otros conceptos

- **Prerrequisito:** [Kernel](../k/kernel.md).
- **Ver también:** [Mecanismo](../m/mecanismo.md), [Proceso](../p/proceso.md), [Recurso](../r/recurso.md), [Vista](../v/vista.md), [Anfitrión](../a/anfitrion.md), [Bind mount](../b/bind-mount.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-068](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md), [SE-112](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-112-paquetes-modulos-y-publicacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — WSL documentation](https://learn.microsoft.com/windows/wsl/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Linux kernel — namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Linux kernel — cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Docker documentation — storage](https://docs.docker.com/engine/storage/) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.

---

[↑ Glosario](../../README.md) · [← N+1](./n-mas-1.md) · [NaN →](./nan.md)
