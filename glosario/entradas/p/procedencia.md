# Procedencia

[↑ Glosario](../../README.md) · [← Problemas](./problemas.md) · [Procedimiento y contrato →](./procedimiento-y-contrato.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Registro de quién construyó un artefacto, a partir de qué fuente y con qué materiales y parámetros.

Definición de trabajo de [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-117 — Licencias, procedencia y reutilización](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md): Origen, versión, autor, url, hash y transformación permiten rastrear un componente.
- En [SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md): Evidencia sobre origen y cadena de publicación.
- En [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md): Información sobre qué construyó un artefacto, desde qué entradas y con qué proceso.
- En [SE-024 — Proyecto: informe reproducible de comportamiento y recursos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md): Cadena que permite rastrear evidencia.

## Por qué importa

En [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), el tema «Procedencia» importa porque permite comprobar quién construyó qué y con qué.

En [SE-117 — Licencias, procedencia y reutilización](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md), el tema «Procedencia» importa porque origen, versión, autor, URL, hash y transformación permiten rastrear un componente.

En [SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), el tema «Procedencia» importa porque relaciona artefacto con publicador y canal

## Cómo funciona

Según [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), en la sección «Procedencia»:

La **procedencia** de un artefacto responde cinco preguntas: quién lo construyó (el *constructor*), a partir de qué fuente (repositorio y commit), con qué materiales (dependencias, herramientas), con qué parámetros y cuál es su huella (el *sujeto*). Un marco como SLSA organiza estos campos en niveles según cuánta confianza hay que depositar en el constructor: en los niveles bajos la procedencia existe y la genera el propio build; en los altos la genera una plataforma de construcción aislada de la que el equipo de desarrollo no puede alterar los datos. La diferencia es esencial: una procedencia que escribe quien construye prueba lo que el constructor *dice*, y una que genera una plataforma independiente prueba algo mucho más difícil de falsificar.

Según [SE-117 — Licencias, procedencia y reutilización](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md), en la sección «Procedencia»:

Origen, versión, autor, URL, hash y transformación permiten rastrear un componente. Copiar y modificar requiere registrar cambios y conservar atribución. Un SBOM describe composición; no certifica que cada dato sea correcto.

## Ejemplo

Ejemplo de [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) (sección «Ejemplo profesional»):

El CI de la API de entregas genera el SBOM a partir del bloqueo y del contenido del artefacto final (escaneo de los archivos copiados en `third_party/`), y escribe una procedencia con el commit, el identificador del trabajo de construcción, el hash del bloqueo y la huella del artefacto. Ambos documentos tienen como sujeto la huella del artefacto y se almacenan junto a él como metadatos (`SE-470`).

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La verificación de la procedencia pasa siempre** — causa: valores esperados tomados del propio documento. Corrección: fijar de antemano constructor, repositorio y rama. ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **procedencia** de un artefacto responde cinco preguntas: quién lo construyó (el *constructor*), a partir de qué fuente (repositorio y commit), con qué materiales (dependencias, herramientas), con qué parámetros y cuál es su huella (el *sujeto*). ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](../a/artefacto.md), [Componente](../c/componente.md), [Evidencia](../e/evidencia.md), [Huella](../h/huella.md), [Amenaza a validez](../a/amenaza-a-validez.md), [Control](../c/control.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-024 — Proyecto: informe reproducible de comportamiento y recursos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-117 — Licencias, procedencia y reutilización](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.
- [SE-202 — Firmas, procedencia y protección del repositorio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.
- [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (316 clases más lo mencionan; las que más):

[SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-536](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md), [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md), [SE-116](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md), [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), [SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md).

**Aparece en los casos de estudio:** [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SLSA v1.0: procedencia](https://slsa.dev/spec/v1.0/provenance) — contenido de una procedencia; autoridad: proyecto SLSA, OpenSSF.
- [SPDX Specification 3.0](https://spdx.dev/use/specifications/) — Identificadores, sbom y procedencia legible por máquinas; autoridad: Linux Foundation.
- [Debian Administrator's Handbook — APT](https://www.debian.org/doc/manuals/debian-handbook/apt.en.html) — delimita el contrato técnico que debe cumplirse al distinguir paquetes del sistema, del lenguaje y artefactos descargados por procedencia y alcance.
- [Homebrew Documentation](https://docs.brew.sh/) — delimita el contrato técnico que debe cumplirse al distinguir paquetes del sistema, del lenguaje y artefactos descargados por procedencia y alcance.
- [SLSA v1.0](https://slsa.dev/spec/v1.0/) — niveles de procedencia de artefactos; autoridad: proyecto SLSA, OpenSSF.

---

[↑ Glosario](../../README.md) · [← Problemas](./problemas.md) · [Procedimiento y contrato →](./procedimiento-y-contrato.md)
