# Checksum

[↑ Glosario](../../README.md) · [← Chaos & Resilience Engineer](./chaos-resilience-engineer.md) · [Churn →](./churn.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Huella criptográfica de un archivo usada para detectar cambios.

Definición de trabajo de [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md).

## Por qué importa

En [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), el tema «Checksums» importa porque detectan corrupción; no autentican a nadie.

## Cómo funciona

Según [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md):

Un **checksum** criptográfico (SHA-256, por ejemplo) es la huella de un archivo. Si coincide con el valor esperado, el archivo no se corrompió ni se alteró *respecto de ese valor*. La seguridad de la comprobación está en cómo se obtuvo el valor esperado: si llega por el mismo canal que el archivo, quien controla el canal cambia ambos. Un checksum sirve para detectar descargas truncadas y errores de transmisión, y sirve contra manipulación solo cuando el valor viene por un canal independiente y anterior al ataque. Además, en una cadena de comprobaciones el hash protege la integridad de un documento (un manifiesto) cuya firma se comprueba una sola vez: se firma una lista de huellas, no cada archivo.

Según [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md):

Para detectar descargas corruptas, sí; contra manipulación, no, porque quien cambia el archivo cambia el checksum. Gana valor cuando el valor esperado llega por un canal independiente, anterior al ataque, o está dentro de un documento firmado con una clave fijada.

## Ejemplo

Ejemplo de [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) (sección «Ejemplo mínimo»):

El fragmento comprueba un checksum y detecta un cambio de un byte. Antes de ejecutarlo, predice si una comparación de huellas detectaría también un cambio hecho por quien controla el valor esperado.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md)) son:

- **El atacante firma con su clave y pasa** — causa: clave de verificación descargada de la misma página. Corrección: clave fijada de antemano en una fuente independiente.
- **Se acepta una versión antigua vulnerable** — causa: sin secuencia ni caducidad en lo firmado. Corrección: número monótono firmado y recordado por el cliente.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un checksum sirve para detectar descargas truncadas y errores de transmisión, y sirve contra manipulación solo cuando el valor viene por un canal independiente y anterior al ataque. ([SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Huella](../h/huella.md), [Firma digital](../f/firma-digital.md), [Raíz de confianza](../r/raiz-de-confianza.md), [Revocación](../r/revocacion.md), [Secuencia](../s/secuencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md), [SE-474](../../../classes/part-39-build-release-y-cadena-de-suministro/se-474-versionado-compatibilidad-y-changelog/README.md), [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md), [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), [SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Checksums».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 8032: EdDSA](https://www.rfc-editor.org/rfc/rfc8032) — algoritmo de firma Ed25519; autoridad: IETF.
- [The Update Framework: especificación](https://theupdateframework.io/specification/) — actualizaciones seguras, secuencia y caducidad; autoridad: proyecto TUF, CNCF.
- [Samuel et al., «Survivable key compromise in software update systems»](https://doi.org/10.1145/1866307.1866315) — diseño frente al compromiso de claves; autoridad: ACM CCS 2010.
- [Sigstore: documentación](https://docs.sigstore.dev/) — firma con identidades efímeras y registro de transparencia; autoridad: proyecto Sigstore, OpenSSF.
- [OpenSSL: pkeyutl](https://docs.openssl.org/3.0/man1/openssl-pkeyutl/) — firma y verificación en los experimentos; autoridad: proyecto OpenSSL.

---

[↑ Glosario](../../README.md) · [← Chaos & Resilience Engineer](./chaos-resilience-engineer.md) · [Churn →](./churn.md)
