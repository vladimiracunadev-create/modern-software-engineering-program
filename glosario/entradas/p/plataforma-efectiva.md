# Plataforma efectiva

[↑ Glosario](../../README.md) · [← Plataforma de ejecución aislada](./plataforma-de-ejecucion-aislada.md) · [Plataforma interna →](./plataforma-interna.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Combinación de sistema, versión, arquitectura, políticas y capacidades observadas.

Definición de trabajo de [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md).

## Por qué importa

La clase donde se define, [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), existe con este propósito: la clase existe para comparar Windows, Linux y macOS por contratos observables y no por estereotipos.

## Cómo funciona

Según [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md):

**Cómo leer la figura.** Cada fila es un dato que un programa podría usar para decidir, y de ella salen dos cajas: la dorada es Windows y la teal es Linux. Las dos son *el mismo equipo físico*: lo que cambia es la plataforma efectiva que el programa ve, y en estos siete datos ninguno coincide. **Dónde deja de valer:** es una comparación entre Windows y *una* distribución de Linux virtualizada; no describe macOS (no se ejecutó aquí) ni otras distribuciones, y la información de versión depende de cada configuración. La ficha omite deliberadamente el nombre del equipo y del usuario, que `platform.uname()` sí devuelve: un diagnóstico minimiza los identificadores que recoge.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md):

Un instalador falla solo en equipos corporativos. La misma versión funciona en un equipo personal. El kit de diagnóstico multiplataforma detecta que la API existe y el binario coincide, pero la ejecución está bloqueada por una política. La corrección se dirige al canal autorizado de distribución; recompilar al azar no aborda el mecanismo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md)) son:

- **“Linux” aparece como una sola plataforma uniforme** — causa: se confundió kernel con distribución y espacio de usuario. Corrección: registrar kernel, distribución, versión y herramientas relevantes por separado.
- **Se usa “64 bits” como diagnóstico completo** — causa: se mezclaron ISA, arquitectura del proceso y formato del artefacto. Corrección: identificar cada contrato y verificar el binario real.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Las dos son *el mismo equipo físico*: lo que cambia es la plataforma efectiva que el programa ve, y en estos siete datos ninguno coincide. ([SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Arquitectura](../a/arquitectura.md), [Capacidad](../c/capacidad.md), [Combinación](../c/combinacion.md), [Versión](../v/version.md), [ABI](../a/abi.md), [API](../a/api.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — Windows documentation](https://learn.microsoft.com/windows/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Linux man-pages project](https://man7.org/linux/man-pages/) — delimita el contrato técnico que debe cumplirse al comparar Windows, Linux y macOS por contratos observables y no por estereotipos.
- [Apple Developer Documentation](https://developer.apple.com/documentation/) — delimita el contrato técnico que debe cumplirse al comparar Windows, Linux y macOS por contratos observables y no por estereotipos.
- [The Open Group Base Specifications, Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.

---

[↑ Glosario](../../README.md) · [← Plataforma de ejecución aislada](./plataforma-de-ejecucion-aislada.md) · [Plataforma interna →](./plataforma-interna.md)
