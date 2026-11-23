# Bind mount

[↑ Glosario](../../README.md) · [← Biblioteca](./biblioteca.md) · [Bisección →](./biseccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Exposición de una ruta del anfitrión dentro de otro contexto.

Definición de trabajo de [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md).

## Por qué importa

La clase donde se define, [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), existe con este propósito: la clase existe para distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.

## Cómo funciona

Según [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md):

La imagen agrupa capas inmutables de referencia y metadatos. Al ejecutar se agrega estado escribible y montajes. Guardar datos importantes solo en la capa efímera los ata al ciclo de vida de esa instancia. Los volúmenes y bind mounts cruzan la frontera y necesitan permisos, backup y ruta explícita.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md):

Un repositorio se compila en WSL sobre `/mnt/c` y las operaciones de muchos archivos son lentas. Una prueba equivalente dentro del sistema de archivos Linux mejora. El equipo mueve el árbol activo y conserva interoperabilidad solo para artefactos necesarios, documentando el costo de frontera.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)) son:

- **“Está aislado porque está en un contenedor”** — causa: se ignoraron kernel, montajes y privilegios compartidos. Corrección: enumerar fronteras y capacidades efectivas.
- **Los datos desaparecen al recrear** — causa: se confundió capa escribible con almacenamiento persistente. Corrección: definir volumen y probar ciclo de vida.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)) son: No cubrimos orquestación, hardening avanzado ni escapes. Con el modelo de plataforma completo, la próxima clase integra los mecanismos en una reparación controlada de un entorno defectuoso.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Anfitrión](../a/anfitrion.md), [Contextos](../c/contextos.md), [Exposición](../e/exposicion.md), [Ruta](../r/ruta.md), [Contenedor](../c/contenedor.md), [Frontera](../f/frontera.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-104](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — WSL documentation](https://learn.microsoft.com/windows/wsl/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Linux kernel — namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Linux kernel — cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Docker documentation — storage](https://docs.docker.com/engine/storage/) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.

---

[↑ Glosario](../../README.md) · [← Biblioteca](./biblioteca.md) · [Bisección →](./biseccion.md)
