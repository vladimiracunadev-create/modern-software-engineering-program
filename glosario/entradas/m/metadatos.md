# Metadatos

[↑ Glosario](../../README.md) · [← Metadato de versión](./metadato-de-version.md) · [Metadatos de documento →](./metadatos-de-documento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Los **metadatos** son las propiedades de un objeto distintas de su contenido principal ([SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)). [SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) los define como datos que describen otros datos: dueño, significado, sensibilidad y frescura. Son un mismo concepto en dos escalas: en un sistema de archivos describen cada archivo; en un pipeline de datos describen conjuntos y columnas.

## Por qué importa

Sin metadatos, un dato no se puede gobernar: no se sabe quién es responsable, qué significa, si contiene información personal ni si está al día. Con ellos, se pueden automatizar controles y trazar el origen de un valor. En el sistema de archivos, los metadatos deciden si una operación sobre el archivo se permite o cómo se ordena.

## Cómo funciona

**En archivos** ([SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)): el archivo que una aplicación percibe no es «un bloque del disco». El sistema de archivos relaciona nombres con objetos, organiza directorios y conserva metadatos como tipo, tamaño, marcas temporales y permisos. El núcleo traduce operaciones de alto nivel a la implementación montada y, finalmente, al dispositivo o servicio remoto.

**En datos** ([SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md)): los metadatos del catálogo (dueño, capa, columnas con tipo, sensibilidad, antigüedad máxima) permiten construir el **linaje**, la relación entre columnas de entrada y de salida. El laboratorio de [SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) usa un analizador de expresiones regulares sobre seis sentencias `CREATE TABLE ... AS SELECT` para registrar de qué columnas de origen sale cada columna: sirve para el estilo que reconoce y falla en silencio con otro. Un analizador real usa la gramática completa del dialecto y los metadatos del catálogo para expandir comodines.

## Ejemplo

Ilustración en Python sobre archivos:

```python
import os, time
st = os.stat("informe.csv")
print(st.st_size, time.ctime(st.st_mtime), oct(st.st_mode))
```

Aquí el tamaño, la fecha de modificación y los permisos son metadatos; el contenido del CSV no. En un catálogo de datos, el equivalente sería `owner: finanzas`, `pii: false`, `max_age_days: 1`.

## Errores y confusiones comunes

- **El archivo se busca en lugares distintos.** Causa: se confundió directorio del script con directorio de trabajo; corrección: elegir una base explícita y mostrarla en diagnóstico ([SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)).
- **Ruta portable construida reemplazando `/`.** Causa: se trataron rutas como cadenas; corrección: biblioteca de rutas y pruebas con raíces, volúmenes y UNC ([SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)).
- **Confiar en un analizador que falla en silencio.** Si el estilo no coincide, el linaje queda incompleto sin avisar ([SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md)).

## Límites y cuándo no aplica

[SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) no cubre recuperación forense ni sistemas distribuidos ni todas las garantías de cada sistema de archivos; una ruta resoluble todavía puede estar prohibida por permisos. Los metadatos pueden estar desactualizados o ser incorrectos: un campo «sensibilidad» sin proceso que lo mantenga es una promesa vacía. Y los metadatos también pueden filtrar información (autor, ubicación), de modo que a veces hay que eliminarlos.

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
