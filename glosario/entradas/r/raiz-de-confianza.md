# Raíz de confianza

[↑ Glosario](../../README.md) · [← Raíz](./raiz.md) · [Rama por abstracción →](./rama-por-abstraccion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Clave o dato que el verificador da por bueno sin comprobarlo.

Definición de trabajo de [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md): Componente (normalmente de hardware) del que se parte sin verificación adicional.

## Por qué importa

En [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), el tema «Raíz de confianza» importa porque la clave fijada es el punto que debe protegerse.

## Cómo funciona

Según [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), en la sección «Raíz de confianza»:

Toda verificación termina en algo que se da por bueno sin comprobarlo: la **raíz de confianza**. Si la clave pública llega con el archivo, la raíz es el sitio de descarga y el atacante que controla el sitio controla la raíz. Si la clave se **fija de antemano** (viene en el instalador anterior, en el sistema operativo, en un repositorio de claves independiente, en el propio cliente), el atacante tiene que comprometer esa distribución anterior. Mover la raíz a un lugar más pequeño, de actualización rara y mejor vigilado es la estrategia: no se elimina la confianza, se la confina. Por eso los sistemas de actualización robustos distinguen claves por rol (raíz, objetivos, marca de tiempo) y guardan las de mayor valor fuera de línea.

## Ejemplo

Ejemplo de [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) (sección «Preguntas frecuentes»):

Desplaza el problema: ya no custodias una clave de larga vida, pero confías en el proveedor de identidad y en un registro público que permita auditar. Cambia la superficie de ataque y la raíz de confianza; no las elimina. Evalúa qué raíz es más fácil de proteger para tu caso.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md)) son:

- **El atacante firma con su clave y pasa** — causa: clave de verificación descargada de la misma página. Corrección: clave fijada de antemano en una fuente independiente.
- **Se acepta una versión antigua vulnerable** — causa: sin secuencia ni caducidad en lo firmado. Corrección: número monótono firmado y recordado por el cliente.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Toda verificación termina en algo que se da por bueno sin comprobarlo: la **raíz de confianza**. ([SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Verificación](../v/verificacion.md), [Verificador](../v/verificador.md), [Checksum](../c/checksum.md), [Extensión](../e/extension.md), [Firma digital](../f/firma-digital.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-283 — Hardware seguro: TEE y atestación](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 8032: EdDSA](https://www.rfc-editor.org/rfc/rfc8032) — algoritmo de firma Ed25519; autoridad: IETF.
- [The Update Framework: especificación](https://theupdateframework.io/specification/) — actualizaciones seguras, secuencia y caducidad; autoridad: proyecto TUF, CNCF.
- [Samuel et al., «Survivable key compromise in software update systems»](https://doi.org/10.1145/1866307.1866315) — diseño frente al compromiso de claves; autoridad: ACM CCS 2010.
- [Sigstore: documentación](https://docs.sigstore.dev/) — firma con identidades efímeras y registro de transparencia; autoridad: proyecto Sigstore, OpenSSF.
- [OpenSSL: pkeyutl](https://docs.openssl.org/3.0/man1/openssl-pkeyutl/) — firma y verificación en los experimentos; autoridad: proyecto OpenSSL.

---

[↑ Glosario](../../README.md) · [← Raíz](./raiz.md) · [Rama por abstracción →](./rama-por-abstraccion.md)
