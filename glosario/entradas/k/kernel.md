# Kernel

[↑ Glosario](../../README.md) · [← Kappa ponderado](./kappa-ponderado.md) · [Keyset →](./keyset.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Componente privilegiado que arbitra recursos y expone operaciones controladas.

Definición de trabajo de [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md).

## Por qué importa

En [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), el tema «Protección» importa porque separa kernel y procesos de usuario

## Cómo funciona

Según [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md):

La abstracción no elimina el hardware. Lo representa con un contrato. Cuando una aplicación abre un archivo, una biblioteca prepara la operación, una llamada al sistema cruza la frontera de protección y el kernel consulta permisos y delega en el sistema de archivos o el controlador correspondiente.

Según [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md):

Linux nombra el kernel; una instalación utilizable combina distribución, bibliotecas, herramientas y políticas.

## Ejemplo

Ejemplo de [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) (sección «Preguntas frecuentes»):

Linux nombra el kernel; una instalación utilizable combina distribución, bibliotecas, herramientas y políticas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **“Linux” aparece como una sola plataforma uniforme** — causa: se confundió kernel con distribución y espacio de usuario. Corrección: registrar kernel, distribución, versión y herramientas relevantes por separado. ([SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La Figura 1 las reúne: la aplicación puede haber construido mal la petición (se comprueba con los argumentos y la traza del propio programa), la biblioteca puede no ofrecer la función en esa versión, la API del sistema puede no existir en la plataforma, el kernel puede haber denegado la operación y el recurso puede no haber podido atenderla. ([SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Operación](../o/operacion.md), [Recurso](../r/recurso.md), [ABI](../a/abi.md), [API](../a/api.md), [Capacidad](../c/capacidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (14 clases más lo mencionan; las que más):

[SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), [SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md), [SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md), [SE-104](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md), [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), [SE-103](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md), [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — Windows documentation](https://learn.microsoft.com/windows/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Linux man-pages project](https://man7.org/linux/man-pages/) — delimita el contrato técnico que debe cumplirse al comparar Windows, Linux y macOS por contratos observables y no por estereotipos.
- [Apple Developer Documentation](https://developer.apple.com/documentation/) — delimita el contrato técnico que debe cumplirse al comparar Windows, Linux y macOS por contratos observables y no por estereotipos.
- [The Open Group Base Specifications, Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.

---

[↑ Glosario](../../README.md) · [← Kappa ponderado](./kappa-ponderado.md) · [Keyset →](./keyset.md)
