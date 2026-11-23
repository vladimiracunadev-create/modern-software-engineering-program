# Atestación

[↑ Glosario](../../README.md) · [← ATDD](./atdd.md) · [Atomicidad →](./atomicidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Afirmación sobre un artefacto, ligada a su huella y normalmente firmada.

Definición de trabajo de [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md).

## Por qué importa

En [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), el tema «Atestaciones y vínculo con la huella» importa porque un documento sin vínculo puede acompañar a cualquier artefacto.

## Cómo funciona

Según [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md):

Una **atestación** es una afirmación firmada sobre un artefacto: «este artefacto fue construido así», «este artefacto no contiene vulnerabilidades críticas conocidas». El esquema de in-toto la estructura como una declaración (*Statement*) con un **sujeto** (el artefacto, identificado por su huella) y un **predicado** (la afirmación, cuyo tipo define su contenido). El vínculo por huella es lo que impide que un SBOM correcto se adjunte a otro archivo. Para el verificador, el procedimiento es: calcular la huella del artefacto que va a desplegar, buscar las atestaciones cuyo sujeto tenga esa huella y evaluar sus predicados contra una política. La firma de la atestación (clase siguiente) añade quién responde por ella.

Según [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md):

El CI de la API de entregas genera el SBOM a partir del bloqueo y del contenido del artefacto final (escaneo de los archivos copiados en `third_party/`), y escribe una procedencia con el commit, el identificador del trabajo de construcción, el hash del bloqueo y la huella del artefacto. Ambos documentos tienen como sujeto la huella del artefacto y se almacenan junto a él como metadatos (`SE-470`). El verificador del despliegue calcula la huella, busca las atestaciones, comprueba que el constructor y el repositorio coinciden con los valores esperados que la política fija de antemano, que el SBOM no contiene componentes de una lista de prohibidos y que la procedencia corresponde a la rama protegida.

## Ejemplo

Ejemplo de [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) (sección «Ejemplo profesional»):

El CI de la API de entregas genera el SBOM a partir del bloqueo y del contenido del artefacto final (escaneo de los archivos copiados en `third_party/`), y escribe una procedencia con el commit, el identificador del trabajo de construcción, el hash del bloqueo y la huella del artefacto. Ambos documentos tienen como sujeto la huella del artefacto y se almacenan junto a él como metadatos (`SE-470`).

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md)) son:

- **El SBOM no contiene una pieza que está en el artefacto** — causa: generado desde el manifiesto. Corrección: generar desde el bloqueo y escanear el artefacto final.
- **Un SBOM válido describe otro artefacto** — causa: sin vínculo por huella. Corrección: sujeto identificado por la huella del artefacto.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos de semilla fija (más un análisis lógico) en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](./afirmacion.md), [Artefacto](./artefacto.md), [Huella](../h/huella.md), [Sobre](../s/sobre.md), [Package URL](../p/package-url.md), [Procedencia](../p/procedencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md), [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-202](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md).

**Aparece en los casos de estudio:** [TSB Bank](../../../casos/fallo/tsb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [in-toto: declaración (Statement)](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) — atestaciones ligadas a un sujeto; autoridad: proyecto in-toto.
- [CycloneDX: visión general de la especificación](https://cyclonedx.org/specification/overview/) — formato de lista de materiales; autoridad: proyecto CycloneDX, OWASP.
- [SPDX 2.3](https://spdx.github.io/spdx-spec/v2.3/) — formato alternativo normalizado; autoridad: proyecto SPDX, Linux Foundation.
- [NTIA: elementos mínimos de un SBOM](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom) — datos mínimos; autoridad: Administración Nacional de Telecomunicaciones e Información de EE. UU.
- [SLSA v1.0: procedencia](https://slsa.dev/spec/v1.0/provenance) — contenido de una procedencia; autoridad: proyecto SLSA, OpenSSF.

---

[↑ Glosario](../../README.md) · [← ATDD](./atdd.md) · [Atomicidad →](./atomicidad.md)
