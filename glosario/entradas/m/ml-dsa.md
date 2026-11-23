# ML-DSA

[↑ Glosario](../../README.md) · [← Mitigación](./mitigacion.md) · [ML-KEM →](./ml-kem.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Firma digital basada en retículos modulares (FIPS 204).

Definición de trabajo de [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md).

## Por qué importa

En [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), el tema «ML-DSA y SLH-DSA» importa porque reemplazan firmas; tamaños de kilobytes.

## Cómo funciona

Según [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md):

En agosto de 2024, NIST publicó los tres primeros estándares: FIPS 203 (ML-KEM, derivado de CRYSTALS-Kyber) para acordar claves; FIPS 204 (ML-DSA, derivado de CRYSTALS-Dilithium) para firmar; y FIPS 205 (SLH-DSA, derivado de SPHINCS+) como firma sin estado basada solo en funciones de resumen, con una base de seguridad distinta. Las implementaciones del laboratorio dieron, para ML-KEM-768: clave pública de 1 184 bytes, clave privada de 2 400, texto cifrado de 1 088 y secreto compartido de 32. Para ML-DSA-65: clave pública de 1 952, clave privada de 4 032 y firma de 3 309. Como referencia, X25519 usa claves públicas de 32 bytes, Ed25519 claves públicas de 32 y firmas de 64, y RSA-2048 claves y firmas de 256.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- FIPS 204 (ML-DSA, derivado de CRYSTALS-Dilithium) para firmar; y FIPS 205 (SLH-DSA, derivado de SPHINCS+) como firma sin estado basada solo en funciones de resumen, con una base de seguridad distinta. ([SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Firma digital](../f/firma-digital.md).
- **Ver también:** [Agilidad criptográfica](../a/agilidad-criptografica.md), [Criptografía poscuántica](../c/criptografia-poscuantica.md), [Desigualdad de Mosca](../d/desigualdad-de-mosca.md), [Híbrido](../h/hibrido.md), [ML-KEM](./ml-kem.md), [Rechazo implícito](../r/rechazo-implicito.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Mitigación](./mitigacion.md) · [ML-KEM →](./ml-kem.md)
