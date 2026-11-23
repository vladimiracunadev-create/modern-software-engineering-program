# Firma digital

[↑ Glosario](../../README.md) · [← Firma de una falla](./firma-de-una-falla.md) · [Firmantes permitidos →](./firmantes-permitidos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Valor calculado con una clave privada que cualquiera puede verificar con la clave pública.

Definición de trabajo de [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md): Prueba, con una clave privada, de que el publicador es quien dice ser y de que el contenido no cambió.
- En [SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md): Valor que se calcula con una clave privada y se verifica con una pública y que prueba procedencia e integridad; quien no tiene la privada no puede producirlo.

## Por qué importa

La clase donde se define, [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), existe con este propósito: la clase existe para que puedas decidir qué comprueba quien instala tu software antes de ejecutarlo, y para que sepas qué ataque detiene cada comprobación y cuál no.

## Cómo funciona

Según [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md):

Una **firma digital** se calcula con una clave privada sobre unos datos y se verifica con la clave pública correspondiente. La verificación correcta prueba que quien posee la clave privada firmó exactamente esos bytes; no prueba quién es esa persona, que la clave sea de quien se cree, que el contenido sea benigno ni que sea reciente. Ed25519 es un algoritmo de firma moderno, con claves y firmas cortas (32 y 64 bytes) y verificación rápida, especificado en el RFC 8032. Usar firmas en lugar de solo huellas permite que el publicador y el verificador no compartan un secreto y que cualquiera pueda comprobar.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md):

La API de entregas publica un manifiesto (`release.json`) con nombre, versión, número de secuencia y las huellas del artefacto, del SBOM y de la procedencia, firmado con Ed25519. El cliente de línea de órdenes incorpora la clave pública en cada versión que él mismo distribuye y recuerda la mayor secuencia vista; antes de instalar calcula la huella del archivo descargado, comprueba la firma del manifiesto con la clave incorporada, comprueba el nombre, rechaza una secuencia inferior a la recordada y falla cerrado ante cualquier discrepancia.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md)) son:

- **El atacante firma con su clave y pasa** — causa: clave de verificación descargada de la misma página. Corrección: clave fijada de antemano en una fuente independiente.
- **Se acepta una versión antigua vulnerable** — causa: sin secuencia ni caducidad en lo firmado. Corrección: número monótono firmado y recordado por el cliente.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos, con firmas Ed25519 reales de `openssl` y hashes de `hashlib`, en Windows 11 (CPython 3.12.9, OpenSSL 3.5.7) y Ubuntu bajo WSL2 (3.12.3, OpenSSL 3.0.13); la matriz de ataques fue idéntica en ambos y las mediciones de tiempo, no. No hay red, servidor, usuarios, GPG, Sigstore ni infraestructura de claves real, y los nueve ataques y la independencia del canal del checksum son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Procedencia](../p/procedencia.md), [Valor](../v/valor.md), [Artefacto](../a/artefacto.md), [Confinamiento de rutas](../c/confinamiento-de-rutas.md), [Despliegue escalonado](../d/despliegue-escalonado.md), [Huella](../h/huella.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-225 — Distribución de binarios y actualizaciones](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), [SE-564](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md).

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

[↑ Glosario](../../README.md) · [← Firma de una falla](./firma-de-una-falla.md) · [Firmantes permitidos →](./firmantes-permitidos.md)
