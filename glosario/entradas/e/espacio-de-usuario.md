# Espacio de usuario

[↑ Glosario](../../README.md) · [← Espacio de nombres](./espacio-de-nombres.md) · [Especialidad →](./especialidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Dominio de ejecución restringido donde viven aplicaciones y servicios no privilegiados.

Definición de trabajo de [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md).

## Por qué importa

La clase donde se define, [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), existe con este propósito: la clase existe para comparar Windows, Linux y macOS por contratos observables y no por estereotipos.

## Cómo funciona

Según [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md):

El kernel ejecuta con privilegios para administrar memoria, planificación, interrupciones y dispositivos. Las aplicaciones normales viven en espacio de usuario con autoridad limitada. El cruce se realiza mediante interfaces controladas; no es una llamada de función ordinaria aunque una biblioteca la haga parecer así.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md):

Un instalador falla solo en equipos corporativos. La misma versión funciona en un equipo personal. El kit de diagnóstico multiplataforma detecta que la API existe y el binario coincide, pero la ejecución está bloqueada por una política. La corrección se dirige al canal autorizado de distribución; recompilar al azar no aborda el mecanismo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **“Linux” aparece como una sola plataforma uniforme** — causa: se confundió kernel con distribución y espacio de usuario. Corrección: registrar kernel, distribución, versión y herramientas relevantes por separado. ([SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md)) son: Esta clase no enseña administración profunda de kernels ni promete que una API conserve idéntica conducta entre versiones. Tampoco demuestra compatibilidad por detectar el nombre del sistema. La siguiente clase baja a una abstracción concreta —el sistema de archivos— donde pequeñas diferencias de rutas, enlaces y metadatos producen fallos muy visibles.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dominio](../d/dominio.md), [Servicio](../s/servicio.md), [ABI](../a/abi.md), [API](../a/api.md), [Capacidad](../c/capacidad.md), [Kernel](../k/kernel.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — Windows documentation](https://learn.microsoft.com/windows/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Linux man-pages project](https://man7.org/linux/man-pages/) — delimita el contrato técnico que debe cumplirse al comparar Windows, Linux y macOS por contratos observables y no por estereotipos.
- [Apple Developer Documentation](https://developer.apple.com/documentation/) — delimita el contrato técnico que debe cumplirse al comparar Windows, Linux y macOS por contratos observables y no por estereotipos.
- [The Open Group Base Specifications, Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.

---

[↑ Glosario](../../README.md) · [← Espacio de nombres](./espacio-de-nombres.md) · [Especialidad →](./especialidad.md)
