# Entrada de directorio

[↑ Glosario](../../README.md) · [← Entorno virtual](./entorno-virtual.md) · [Entrada de portafolio comprobable →](./entrada-de-portafolio-comprobable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Asociación entre un nombre y un objeto del sistema de archivos.

Definición de trabajo de [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md).

## Por qué importa

La clase donde se define, [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md), existe con este propósito: la clase existe para razonar sobre identidad de archivos mediante rutas, enlaces, metadatos y resolución.

## Cómo funciona

[SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md):

Un actualizador escribe sobre el archivo final y se interrumpe, dejando JSON truncado. El equipo cambia a temporal en el mismo volumen, valida el contenido y reemplaza según la garantía documentada. Mantiene copia o recuperación porque atomicidad no equivale a persistencia ante toda falla.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)) son:

- **El archivo se busca en lugares distintos** — causa: se confundió directorio del script con directorio de trabajo. Corrección: elegir una base explícita y mostrarla en diagnóstico.
- **Una ruta portable se construye reemplazando `/`** — causa: se trataron rutas como cadenas. Corrección: usar la biblioteca de rutas y probar raíces, volúmenes y UNC.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)) son: No cubrimos recuperación forense, sistemas distribuidos ni todas las garantías de cada sistema de archivos. Una ruta resoluble todavía puede estar prohibida. La próxima clase incorpora identidad, grupos, permisos y elevación para explicar esa decisión.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Objeto](../o/objeto.md), [Directorio de trabajo](../d/directorio-de-trabajo.md), [Enlace simbólico](./enlace-simbolico.md), [Espacio de nombres](./espacio-de-nombres.md), [Metadatos](../m/metadatos.md), [Reemplazo atómico](../r/reemplazo-atomico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Open Group — Pathname Resolution](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html#tag_04_16) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Naming Files, Paths, and Namespaces](https://learn.microsoft.com/windows/win32/fileio/naming-a-file) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Python documentation — pathlib](https://docs.python.org/3/library/pathlib.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Apple Platform Deployment — File system basics](https://support.apple.com/guide/deployment/intro-to-file-system-apd0b895e8e1/web) — delimita el contrato técnico que debe cumplirse al razonar sobre identidad de archivos mediante rutas, enlaces, metadatos y resolución.

---

[↑ Glosario](../../README.md) · [← Entorno virtual](./entorno-virtual.md) · [Entrada de portafolio comprobable →](./entrada-de-portafolio-comprobable.md)
