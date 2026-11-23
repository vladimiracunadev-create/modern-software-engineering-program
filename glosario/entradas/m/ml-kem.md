# ML-KEM

[↑ Glosario](../../README.md) · [← ML-DSA](./ml-dsa.md) · [MLOps / ML Platform Engineer →](./mlops-ml-platform-engineer.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Mecanismo de encapsulación de claves basado en retículos modulares (FIPS 203).

Definición de trabajo de [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md).

## Por qué importa

En [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), el tema «ML-KEM» importa porque reemplaza el acuerdo de claves; mucho más grande.

## Cómo funciona

Según [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md):

En agosto de 2024, NIST publicó los tres primeros estándares: FIPS 203 (ML-KEM, derivado de CRYSTALS-Kyber) para acordar claves; FIPS 204 (ML-DSA, derivado de CRYSTALS-Dilithium) para firmar; y FIPS 205 (SLH-DSA, derivado de SPHINCS+) como firma sin estado basada solo en funciones de resumen, con una base de seguridad distinta. Las implementaciones del laboratorio dieron, para ML-KEM-768: clave pública de 1 184 bytes, clave privada de 2 400, texto cifrado de 1 088 y secreto compartido de 32. Para ML-DSA-65: clave pública de 1 952, clave privada de 4 032 y firma de 3 309. Como referencia, X25519 usa claves públicas de 32 bytes, Ed25519 claves públicas de 32 y firmas de 64, y RSA-2048 claves y firmas de 256.

Según [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md):

**Diagnóstico paso a paso.** (1) Se agrupan los fallos por red de origen: son clientes detrás de un mismo tipo de cortafuegos. (2) Se capturan los paquetes del saludo: el primer mensaje supera ahora un segmento, porque contiene la clave pública de ML-KEM-768. (3) Ese cortafuegos analiza solo el primer paquete del saludo y descarta lo que no entiende. (4) El saludo clásico cabía en un paquete. (5) Se mantiene el algoritmo clásico para las redes afectadas con una excepción registrada, se informa a los operadores del cortafuegos y se mide el porcentaje de clientes afectados antes de ampliar el despliegue.

## Ejemplo

Ejemplo de [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) (sección «Ejemplo mínimo»):

Acordar una clave con ML-KEM-768 y comprobar el secreto compartido:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En ML-KEM, descapsular un texto cifrado alterado no devuelve un error: devuelve otro secreto aparentemente válido. ([SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), [SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Encapsulación](../e/encapsulacion.md), [Mecanismo](./mecanismo.md), [Agilidad criptográfica](../a/agilidad-criptografica.md), [Criptografía poscuántica](../c/criptografia-poscuantica.md), [Desigualdad de Mosca](../d/desigualdad-de-mosca.md), [Híbrido](../h/hibrido.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← ML-DSA](./ml-dsa.md) · [MLOps / ML Platform Engineer →](./mlops-ml-platform-engineer.md)
