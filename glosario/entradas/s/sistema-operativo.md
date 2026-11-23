# Sistema operativo

[↑ Glosario](../../README.md) · [← Sistema de referencia](./sistema-de-referencia.md) · [Site Reliability Engineer →](./site-reliability-engineer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Software que administra recursos y ofrece abstracciones protegidas a programas.

Definición de trabajo de [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md).

## Por qué importa

La clase donde se define, [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), existe con este propósito: la clase existe para comparar Windows, Linux y macOS por contratos observables y no por estereotipos.

## Cómo funciona

Según [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md):

El hardware expone procesadores, memoria y dispositivos con detalles muy específicos. El sistema operativo arbitra su uso y ofrece abstracciones estables: procesos en vez de secuencias crudas de instrucciones; archivos en vez de bloques físicos; sockets en vez de manipular directamente una interfaz de red.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md):

Un instalador falla solo en equipos corporativos. La misma versión funciona en un equipo personal. El kit de diagnóstico multiplataforma detecta que la API existe y el binario coincide, pero la ejecución está bloqueada por una política. La corrección se dirige al canal autorizado de distribución; recompilar al azar no aborda el mecanismo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md)) son:

- **“Linux” aparece como una sola plataforma uniforme** — causa: se confundió kernel con distribución y espacio de usuario. Corrección: registrar kernel, distribución, versión y herramientas relevantes por separado.
- **Se usa “64 bits” como diagnóstico completo** — causa: se mezclaron ISA, arquitectura del proceso y formato del artefacto. Corrección: identificar cada contrato y verificar el binario real.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El kit de diagnóstico multiplataforma registra sistema operativo y arquitectura porque “Windows 11” no informa si un artefacto es x86-64 o Arm64. ([SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Abstracción](../a/abstraccion.md), [Recurso](../r/recurso.md), [ABI](../a/abi.md), [API](../a/api.md), [Capacidad](../c/capacidad.md), [Espacio de usuario](../e/espacio-de-usuario.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-025 — Windows, Linux, macOS y sus modelos operativos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (92 clases más lo mencionan; las que más):

[SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Amazon](../../../casos/exito/amazon.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — Windows documentation](https://learn.microsoft.com/windows/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Linux man-pages project](https://man7.org/linux/man-pages/) — delimita el contrato técnico que debe cumplirse al comparar Windows, Linux y macOS por contratos observables y no por estereotipos.
- [Apple Developer Documentation](https://developer.apple.com/documentation/) — delimita el contrato técnico que debe cumplirse al comparar Windows, Linux y macOS por contratos observables y no por estereotipos.
- [The Open Group Base Specifications, Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.

---

[↑ Glosario](../../README.md) · [← Sistema de referencia](./sistema-de-referencia.md) · [Site Reliability Engineer →](./site-reliability-engineer.md)
