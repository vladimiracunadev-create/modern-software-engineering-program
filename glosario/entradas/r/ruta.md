# Ruta

[↑ Glosario](../../README.md) · [← Runtime e implementación](./runtime-e-implementacion.md) · [Ruta ambigua →](./ruta-ambigua.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Expresión interpretada bajo reglas y una base.

Definición de trabajo de [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md): Regla para elegir interfaz y siguiente salto.

## Por qué importa

En [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md), el tema «Espacio de nombres» importa porque vincula rutas con objetos

## Cómo funciona

Según [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md):

Una ruta absoluta parte de una raíz o volumen definido por la plataforma. Una ruta relativa parte del directorio de trabajo del proceso, no necesariamente del directorio donde está el script. Ese detalle causa muchos “funciona en mi máquina”.

Según [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md):

Una causa frecuente es que el repositorio contiene dos archivos cuyos nombres difieren solo en mayúsculas (por ejemplo, `Readme.md` y `README.md`). En un sistema que distingue mayúsculas ambos coexisten; en NTFS, uno sobrescribe al otro o el cliente avisa. Otras causas son nombres con caracteres no válidos en Windows (como `:`), enlaces simbólicos sin el privilegio necesario y rutas muy largas. Comprueba estas hipótesis antes de culpar a la herramienta.

## Ejemplo

Ejemplo de [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) (sección «Preguntas frecuentes»):

Una causa frecuente es que el repositorio contiene dos archivos cuyos nombres difieren solo en mayúsculas (por ejemplo, `Readme.md` y `README.md`). En un sistema que distingue mayúsculas ambos coexisten; en NTFS, uno sobrescribe al otro o el cliente avisa. Otras causas son nombres con caracteres no válidos en Windows (como `:`), enlaces simbólicos sin el privilegio necesario y rutas muy largas. Comprueba estas hipótesis antes de culpar a la herramienta.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una ruta portable se construye reemplazando `/`** — causa: se trataron rutas como cadenas. Corrección: usar la biblioteca de rutas y probar raíces, volúmenes y UNC. ([SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una ruta relativa parte del directorio de trabajo del proceso, no necesariamente del directorio donde está el script. ([SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md))
- La corrección debe explicar el contexto; no codificar una ruta personal absoluta. ([SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Expresión](../e/expresion.md), [Interfaz](../i/interfaz.md), [Regla](./regla.md), [Alcance](../a/alcance.md), [CIDR](../c/cidr.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-039 — IPv4, IPv6, subredes, rutas y NAT](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (200 clases más lo mencionan; las que más):

[SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md), [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md), [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md), [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md), [SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), [SE-467](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md), [SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md).

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md), [Slack](../../../casos/exito/slack.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Open Group — Pathname Resolution](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html#tag_04_16) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Apple Platform Deployment — File system basics](https://support.apple.com/guide/deployment/intro-to-file-system-apd0b895e8e1/web) — delimita el contrato técnico que debe cumplirse al razonar sobre identidad de archivos mediante rutas, enlaces, metadatos y resolución.
- [Microsoft Learn — Naming Files, Paths, and Namespaces](https://learn.microsoft.com/windows/win32/fileio/naming-a-file) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Python documentation — pathlib](https://docs.python.org/3/library/pathlib.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [RFC 8200 — Internet Protocol, Version 6](https://www.rfc-editor.org/rfc/rfc8200) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Runtime e implementación](./runtime-e-implementacion.md) · [Ruta ambigua →](./ruta-ambigua.md)
