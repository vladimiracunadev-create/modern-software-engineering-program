# Simulacro

[↑ Glosario](../../README.md) · [← SIMT](./simt.md) · [Simulado →](./simulado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Ensayo controlado de una pérdida (de una versión, de un repositorio, de una clave) con resultado registrado.

Definición de trabajo de [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md): Ejercicio que inyecta incidentes conocidos en un sistema de prueba para medir qué se pierde y qué se recupera.

## Por qué importa

La clase donde se define, [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), existe con este propósito: el proyecto existe para que construyas un canal de release completo y lo defiendas: que produzca un artefacto reproducible, lo acompañe de un SBOM y una procedencia, lo firme con una política de verificación explícita, permita volver atrás sin perder lo que importa y sobreviva a la pérdida del repositorio de releases y de una clave.

## Cómo funciona

Según [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md):

El **expediente de release** es el conjunto de documentos y pruebas que permite a otra persona decidir si confía en un release sin recurrir a quien lo produjo. Contiene: el artefacto y su huella; el SBOM con su método y su alcance; la procedencia (constructor, fuente, commit, materiales); el manifiesto con nombre, versión y secuencia, y su firma; la política de verificación con los valores esperados y su origen; los comandos y versiones para reconstruir y verificar; el registro de la verificación en al menos dos sistemas; el registro de los simulacros de recuperación; el informe de verificación con tres estados; y un archivo de límites. El criterio de calidad es operativo: otra persona debe poder reproducir cada afirmación desde un checkout limpio con los comandos del expediente.

Según [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md):

El equipo entrega un expediente con esta estructura. `artefacto/` con el zip y su huella; `sbom.json` y `procedencia.json` ligados por huella; `manifiesto.json` y `manifiesto.sig`; `esperados.json` con la clave pública, el nombre, el constructor, el repositorio y la secuencia, con una nota sobre cómo se obtuvo cada valor; `verificar.py` y `casos.py` con las doce manipulaciones y los seis casos coherentes; `registro-verificacion-windows.txt` y `registro-verificacion-ubuntu.txt`; `simulacros.md` con los cuatro simulacros y su resultado; `informe-verificacion.md` con los tres estados; y `LIMITES.md`. Un trabajo trimestral repite la reconstrucción independiente en una máquina distinta, ensaya el retroceso y la rotación y renueva el expediente con nueva fecha. La clave de firma vive en un servicio de claves, hay una clave de reserva fuera de línea y una declaración de rotación preparada.

## Ejemplo

Ejemplo de [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md) (sección «Ejemplo profesional»):

El equipo entrega un expediente con esta estructura. `artefacto/` con el zip y su huella; `sbom.json` y `procedencia.json` ligados por huella; `manifiesto.json` y `manifiesto.sig`; `esperados.json` con la clave pública, el nombre, el constructor, el repositorio y la secuencia, con una nota sobre cómo se obtuvo cada valor; `verificar.py` y `casos.py` con las doce manipulaciones y los seis casos coherentes; `registro-verificacion-windows.txt` y `registro-verificacion-ubuntu.txt`; `simulacros.md` con los cuatro simulacros y su resultado; `informe-verificacion.md` con los tres estados; y `LIMITES.md`. Un trabajo trimestral repite la reconstrucción independiente en una máquina distinta, ensaya el retroceso y la rotación y renueva el expediente con nueva fecha.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md)) son:

- **El cliente rechaza el retroceso** — causa: se reinstala un bundle de secuencia menor. Corrección: republicar el contenido anterior con secuencia mayor.
- **Los hashes difieren entre sistemas** — causa: campo de formato dependiente del sistema. Corrección: fijar el sistema de creación y normalizar el build.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** son simulacros lógicos de un solo proceso, sin red ni clientes reales; una rotación real debe tener en cuenta clientes desconectados durante meses, y un retroceso real, datos escritos por la versión defectuosa (`SE-476`). ([SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md))
- Traslada el proyecto a otro artefacto (una imagen de contenedor, una aplicación móvil, una biblioteca publicada): cambia el formato, la herramienta de firma y el repositorio y conserva el expediente, los criterios de aceptación, la verificación cruzada, los simulacros y los límites. ([SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ensayo](../e/ensayo.md), [Incidente](../i/incidente.md), [Resultado](../r/resultado.md), [Versión](../v/version.md), [Bitácora de cambios](../b/bitacora-de-cambios.md), [Caducidad de la evidencia](../c/caducidad-de-la-evidencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-360 — Proyecto: capa de datos recuperable](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md).

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

[↑ Glosario](../../README.md) · [← SIMT](./simt.md) · [Simulado →](./simulado.md)
