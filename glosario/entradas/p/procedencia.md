# Procedencia

[↑ Glosario](../../README.md) · [← Problemas](./problemas.md) · [Procedimiento y contrato →](./procedimiento-y-contrato.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

La **procedencia** (*provenance*) es el registro de quién construyó un artefacto, a partir de qué fuente y con qué materiales y parámetros ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md)). Otras clases la usan con matices: origen, versión, autor, URL, hash y transformación que permiten rastrear un componente ([SE-117](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md)); evidencia sobre origen y cadena de publicación ([SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md)); información sobre qué construyó un artefacto y con qué proceso ([SE-202](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md)); cadena que permite rastrear evidencia ([SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md)).

## Por qué importa

Sin procedencia, un binario o un paquete es una caja cerrada: no se sabe de qué código salió ni quién lo produjo. Eso impide verificar que lo que se despliega es lo que se revisó. Cambia qué se exige de una dependencia o de un artefacto propio: no solo un hash, sino de dónde viene.

## Cómo funciona

[SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) dice que la procedencia responde cinco preguntas: quién lo construyó (el *constructor*), a partir de qué fuente (repositorio y commit), con qué materiales (dependencias, herramientas), con qué parámetros y cuál es su huella (el *sujeto*). Un marco como SLSA organiza esos campos en niveles según cuánta confianza hay que depositar en el constructor: en los niveles bajos la procedencia existe y la genera el propio *build*; en los altos la genera una plataforma de construcción aislada, de la que el equipo de desarrollo no puede alterar los datos. La diferencia es esencial: una procedencia escrita por quien construye prueba lo que el constructor *dice*; una generada por una plataforma independiente prueba algo mucho más difícil de falsificar.

[SE-117](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md) añade para componentes copiados: registrar cambios y conservar atribución. Y recuerda que un SBOM describe composición pero no certifica que cada dato sea correcto.

## Ejemplo

Un artefacto publicado lleva una declaración con: constructor (la plataforma de CI), repositorio y commit, parámetros del build, y el hash del archivo. El consumidor verifica la declaración contra valores esperados fijados de antemano. Ilustración:

```json
{"sujeto": {"sha256": "..."}, "constructor": "ci.ejemplo", "fuente": "repo@commit", "materiales": ["dep@1.2.3"]}
```

## Errores y confusiones comunes

- **La verificación pasa siempre.** Causa: los valores esperados se tomaron del propio documento; corrección: fijar de antemano constructor, repositorio y rama ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md)).
- **Confundir procedencia con SBOM.** La primera dice cómo se produjo; el segundo, qué contiene ([SE-117](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md)).
- **Creer que firmar equivale a procedencia.** Una firma dice quién firmó, no cómo se construyó.

## Límites y cuándo no aplica

La procedencia demuestra origen, no ausencia de defectos ni de código malicioso en la fuente. Los niveles de SLSA son un marco externo cuyo detalle conviene contrastar con su especificación. Y la procedencia autogenerada por el constructor solo vale si se confía en el constructor.

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
