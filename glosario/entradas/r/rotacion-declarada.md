# Rotación declarada

[↑ Glosario](../../README.md) · [← Rotación](./rotacion.md) · [RPN →](./rpn.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Cambio de clave anunciado con una declaración firmada por la clave vigente antes de usar la nueva.

Definición de trabajo de [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md).

## Por qué importa

La clase donde se define, [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), existe con este propósito: el proyecto existe para que construyas un canal de release completo y lo defiendas: que produzca un artefacto reproducible, lo acompañe de un SBOM y una procedencia, lo firme con una política de verificación explícita, permita volver atrás sin perder lo que importa y sobreviva a la pérdida del repositorio de releases y de una clave.

## Cómo funciona

Según [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md):

El proyecto se acepta cuando cada afirmación del expediente tiene una prueba ejecutable con un resultado esperado. Los criterios mínimos son: (a) dos construcciones en entornos distintos producen la misma huella; (b) el release legítimo pasa las doce comprobaciones del verificador en ambos sistemas; (c) las doce manipulaciones del taller se rechazan, cada una por una comprobación nombrada; (d) los seis casos coherentes se documentan como no rechazados, con el control que los vería; (e) un retroceso se logra publicando un release nuevo con la secuencia mayor, y el bundle antiguo se rechaza; (f) tras destruir el repositorio de releases, la reconstrucción desde la fuente produce la misma huella; (g) una rotación declarada con la clave vigente permite verificar con la nueva;

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md):

El equipo entrega un expediente con esta estructura. `artefacto/` con el zip y su huella; `sbom.json` y `procedencia.json` ligados por huella; `manifiesto.json` y `manifiesto.sig`; `esperados.json` con la clave pública, el nombre, el constructor, el repositorio y la secuencia, con una nota sobre cómo se obtuvo cada valor; `verificar.py` y `casos.py` con las doce manipulaciones y los seis casos coherentes; `registro-verificacion-windows.txt` y `registro-verificacion-ubuntu.txt`; `simulacros.md` con los cuatro simulacros y su resultado; `informe-verificacion.md` con los tres estados; y `LIMITES.md`.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md)) son:

- **El cliente rechaza el retroceso** — causa: se reinstala un bundle de secuencia menor. Corrección: republicar el contenido anterior con secuencia mayor.
- **Los hashes difieren entre sistemas** — causa: campo de formato dependiente del sistema. Corrección: fijar el sistema de creación y normalizar el build.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutó un proyecto de integración con un canal sintético (zip de 42 archivos, SBOM y procedencia simplificados, firmas Ed25519 de `openssl`), con verificación cruzada entre Windows 11 (CPython 3.12.9, OpenSSL 3.5.7) y Ubuntu bajo WSL2 (3.12.3, OpenSSL 3.0.13): las huellas y los rechazos fueron idénticos y los tiempos no.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Caducidad de la evidencia](../c/caducidad-de-la-evidencia.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Expediente de release](../e/expediente-de-release.md), [Recuperación](./recuperacion.md), [Simulacro](../s/simulacro.md).
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

[↑ Glosario](../../README.md) · [← Rotación](./rotacion.md) · [RPN →](./rpn.md)
