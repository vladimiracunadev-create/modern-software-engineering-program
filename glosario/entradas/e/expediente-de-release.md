# Expediente de release

[↑ Glosario](../../README.md) · [← Expediente de la decisión](./expediente-de-la-decision.md) · [Experimento A/A →](./experimento-a-a.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Conjunto de documentos y pruebas que permite verificar un release sin recurrir a quien lo produjo.

Definición de trabajo de [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md).

## Por qué importa

En [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), el tema «Expediente de release» importa porque es lo que otra persona revisa sin pedirte nada.

## Cómo funciona

Según [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md):

El **expediente de release** es el conjunto de documentos y pruebas que permite a otra persona decidir si confía en un release sin recurrir a quien lo produjo. Contiene: el artefacto y su huella; el SBOM con su método y su alcance; la procedencia (constructor, fuente, commit, materiales); el manifiesto con nombre, versión y secuencia, y su firma; la política de verificación con los valores esperados y su origen; los comandos y versiones para reconstruir y verificar; el registro de la verificación en al menos dos sistemas; el registro de los simulacros de recuperación; el informe de verificación con tres estados; y un archivo de límites. El criterio de calidad es operativo: otra persona debe poder reproducir cada afirmación desde un checkout limpio con los comandos del expediente.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md):

El equipo entrega un expediente con esta estructura. `artefacto/` con el zip y su huella; `sbom.json` y `procedencia.json` ligados por huella; `manifiesto.json` y `manifiesto.sig`; `esperados.json` con la clave pública, el nombre, el constructor, el repositorio y la secuencia, con una nota sobre cómo se obtuvo cada valor; `verificar.py` y `casos.py` con las doce manipulaciones y los seis casos coherentes; `registro-verificacion-windows.txt` y `registro-verificacion-ubuntu.txt`; `simulacros.md` con los cuatro simulacros y su resultado; `informe-verificacion.md` con los tres estados; y `LIMITES.md`.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md)) son:

- **El cliente rechaza el retroceso** — causa: se reinstala un bundle de secuencia menor. Corrección: republicar el contenido anterior con secuencia mayor.
- **Los hashes difieren entre sistemas** — causa: campo de formato dependiente del sistema. Corrección: fijar el sistema de creación y normalizar el build.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **expediente de release** es el conjunto de documentos y pruebas que permite a otra persona decidir si confía en un release sin recurrir a quien lo produjo. ([SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Documento](../d/documento.md), [Caducidad de la evidencia](../c/caducidad-de-la-evidencia.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Recuperación](../r/recuperacion.md), [Rotación declarada](../r/rotacion-declarada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SLSA v1.0](https://slsa.dev/spec/v1.0/) — niveles de garantía de la cadena de suministro; autoridad: proyecto SLSA, OpenSSF.
- [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro de software; autoridad: NIST.
- [The Update Framework](https://theupdateframework.io/specification/) — roles de claves, secuencia, caducidad y recuperación; autoridad: proyecto TUF, CNCF.
- [Samuel et al., «Survivable key compromise in software update systems»](https://doi.org/10.1145/1866307.1866315) — supervivencia al compromiso de claves; autoridad: ACM CCS 2010.
- [Reproducible Builds: definición](https://reproducible-builds.org/docs/definition/) — reproducibilidad y verificación independiente; autoridad: proyecto Reproducible Builds.

---

[↑ Glosario](../../README.md) · [← Expediente de la decisión](./expediente-de-la-decision.md) · [Experimento A/A →](./experimento-a-a.md)
