# Enlace simbólico

[↑ Glosario](../../README.md) · [← Enlace roto](./enlace-roto.md) · [Enlace sospechoso →](./enlace-sospechoso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Objeto que referencia otra ruta y puede quedar sin destino.

Definición de trabajo de [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md).

## Por qué importa

La clase donde se define, [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md), existe con este propósito: la clase existe para razonar sobre identidad de archivos mediante rutas, enlaces, metadatos y resolución.

## Cómo funciona

Según [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md):

Un enlace simbólico almacena una referencia que puede quedar colgante si cambia el objetivo. Un enlace físico agrega otro nombre a un mismo objeto subyacente y suele estar limitado al mismo sistema de archivos. Borrar un nombre no necesariamente borra los datos si quedan otros enlaces o descriptores abiertos.

Según [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md):

No. Un enlace simbólico es un archivo pequeño que *contiene una ruta* y se resuelve al abrirlo; si el destino cambia o desaparece, el enlace se rompe. Un enlace físico es un segundo nombre para el *mismo contenido* (`nlink = 2`); borrar uno no borra los datos mientras quede el otro. Ninguno es una copia: cambiar el contenido por uno se ve por el otro.

## Ejemplo

Ejemplo de [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) (sección «Preguntas frecuentes»):

No. Un enlace simbólico es un archivo pequeño que *contiene una ruta* y se resuelve al abrirlo; si el destino cambia o desaparece, el enlace se rompe. Un enlace físico es un segundo nombre para el *mismo contenido* (`nlink = 2`); borrar uno no borra los datos mientras quede el otro. Ninguno es una copia: cambiar el contenido por uno se ve por el otro.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)) son:

- **El archivo se busca en lugares distintos** — causa: se confundió directorio del script con directorio de trabajo. Corrección: elegir una base explícita y mostrarla en diagnóstico.
- **Una ruta portable se construye reemplazando `/`** — causa: se trataron rutas como cadenas. Corrección: usar la biblioteca de rutas y probar raíces, volúmenes y UNC.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El enlace simbólico falla en NTFS sin el privilegio correspondiente (`WinError 1314`) y funciona en ext4. ([SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Objeto](../o/objeto.md), [Referencia](../r/referencia.md), [Ruta](../r/ruta.md), [Directorio de trabajo](../d/directorio-de-trabajo.md), [Entrada de directorio](./entrada-de-directorio.md), [Espacio de nombres](./espacio-de-nombres.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md), [SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-103](../../../classes/part-08-entornos-herramientas-y-depuracion/se-103-entornos-virtuales-y-aislamiento-de-dependencias/README.md), [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md), [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md), [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Open Group — Pathname Resolution](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html#tag_04_16) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Naming Files, Paths, and Namespaces](https://learn.microsoft.com/windows/win32/fileio/naming-a-file) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Python documentation — pathlib](https://docs.python.org/3/library/pathlib.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Apple Platform Deployment — File system basics](https://support.apple.com/guide/deployment/intro-to-file-system-apd0b895e8e1/web) — delimita el contrato técnico que debe cumplirse al razonar sobre identidad de archivos mediante rutas, enlaces, metadatos y resolución.

---

[↑ Glosario](../../README.md) · [← Enlace roto](./enlace-roto.md) · [Enlace sospechoso →](./enlace-sospechoso.md)
