# Metadatos

[↑ Glosario](../../README.md) · [← Metadato de versión](./metadato-de-version.md) · [Metadatos de documento →](./metadatos-de-documento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Propiedades del objeto distintas de su contenido principal.

Definición de trabajo de [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md): Datos que describen otros datos (dueño, significado, sensibilidad, frescura).

## Por qué importa

En [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md), el tema «Metadatos» importa porque describen tipo, tamaño, tiempos y acceso

## Cómo funciona

Según [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md):

El archivo que una aplicación percibe no es simplemente “un bloque del disco”. El sistema de archivos relaciona nombres con objetos, organiza directorios y conserva metadatos como tipo, tamaño, marcas temporales y permisos. El kernel traduce operaciones de alto nivel a la implementación montada y, finalmente, al dispositivo o servicio remoto.

Según [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md):

El laboratorio tiene seis sentencias `CREATE TABLE ... AS SELECT` en el estilo del pipeline (alias explícitos, un `FROM`, un `JOIN` como máximo). El analizador separa la lista de selección, resuelve alias de tabla y registra, para cada columna de salida, las columnas de origen que aparecen en su expresión. Es un pequeño analizador de expresiones regulares: sirve para el estilo que reconoce y falla en silencio con otro. Un analizador real usa la gramática completa del dialecto y los metadatos del catálogo para expandir comodines.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md):

Un actualizador escribe sobre el archivo final y se interrumpe, dejando JSON truncado. El equipo cambia a temporal en el mismo volumen, valida el contenido y reemplaza según la garantía documentada. Mantiene copia o recuperación porque atomicidad no equivale a persistencia ante toda falla.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)) son:

- **El archivo se busca en lugares distintos** — causa: se confundió directorio del script con directorio de trabajo. Corrección: elegir una base explícita y mostrarla en diagnóstico.
- **Una ruta portable se construye reemplazando `/`** — causa: se trataron rutas como cadenas. Corrección: usar la biblioteca de rutas y probar raíces, volúmenes y UNC.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)) son: No cubrimos recuperación forense, sistemas distribuidos ni todas las garantías de cada sistema de archivos. Una ruta resoluble todavía puede estar prohibida. La próxima clase incorpora identidad, grupos, permisos y elevación para explicar esa decisión.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Frescura](../f/frescura.md), [Objeto](../o/objeto.md), [Principal](../p/principal.md), [Propiedad](../p/propiedad.md), [Arista de condición](../a/arista-de-condicion.md), [Arista de valor](../a/arista-de-valor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (67 clases más lo mencionan; las que más):

[SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md), [SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md), [SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), [SE-238](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md), [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), [SE-117](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md), [SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Spotify](../../../casos/exito/spotify.md), [Stripe](../../../casos/exito/stripe.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Apple Platform Deployment — File system basics](https://support.apple.com/guide/deployment/intro-to-file-system-apd0b895e8e1/web) — delimita el contrato técnico que debe cumplirse al razonar sobre identidad de archivos mediante rutas, enlaces, metadatos y resolución.
- [The Open Group — Pathname Resolution](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html#tag_04_16) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Naming Files, Paths, and Namespaces](https://learn.microsoft.com/windows/win32/fileio/naming-a-file) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Python documentation — pathlib](https://docs.python.org/3/library/pathlib.html) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Metadato de versión](./metadato-de-version.md) · [Metadatos de documento →](./metadatos-de-documento.md)
