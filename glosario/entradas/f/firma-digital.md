# Firma digital

[↑ Glosario](../../README.md) · [← Firma de una falla](./firma-de-una-falla.md) · [Firmantes permitidos →](./firmantes-permitidos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Una **firma digital** es un valor calculado con una clave privada sobre unos datos, que cualquiera puede verificar con la clave pública correspondiente. [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) (firmas, checksums y verificación) la define así; [SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md) la presenta como prueba de que el publicador es quien dice ser y de que el contenido no cambió, y [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) subraya que quien no tiene la clave privada no puede producirla. Prueba procedencia (de la clave) e integridad (de esos bytes).

## Por qué importa

Quien instala o actualiza software decide en qué confiar antes de ejecutarlo. [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) existe para que sepas qué ataque detiene cada comprobación y cuál no: una huella (checksum) detecta corrupción pero no a un atacante que reemplaza archivo y huella; una firma sí, mientras la clave privada permanezca secreta.

## Cómo funciona

El publicador firma los datos con su clave privada; el verificador comprueba la firma con la clave pública. Dos propiedades de diseño que [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) destaca:

- **No hay secreto compartido.** Publicador y verificador no comparten un secreto, y cualquiera puede comprobar (a diferencia de un código de autenticación con clave compartida).
- **Qué prueba y qué no.** Una verificación correcta prueba que quien posee la clave privada firmó *exactamente esos bytes*. No prueba quién es esa persona, que la clave sea de quien se cree, que el contenido sea benigno ni que sea reciente.

Ed25519, algoritmo moderno especificado en el RFC 8032, usa claves de 32 bytes y firmas de 64, con verificación rápida. Lo que une la clave pública con una identidad es otro mecanismo (certificados, una raíz de confianza); y lo que impide reinstalar una versión vieja firmada es un número de secuencia dentro de lo firmado.

## Ejemplo

La API de entregas de [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) publica un manifiesto (`release.json`) con nombre, versión, número de secuencia y las huellas de los artefactos; la firma cubre el manifiesto. Quien instala verifica la firma y luego compara las huellas. Ilustración propia del paso: `verificar(clave_publica, manifiesto, firma)` devuelve verdadero o falso; si el atacante cambia un byte del manifiesto, falla.

## Errores y confusiones comunes

- **Confundir firma con huella:** la huella no prueba procedencia.
- **Creer que firmado significa seguro:** prueba quién firmó, no que el contenido sea benigno.
- **Ignorar la actualidad:** una versión vieja firmada sigue verificando; hace falta número de secuencia.
- **Guardar la clave privada en el repositorio o en el mismo equipo que compila sin protección.**

## Límites y cuándo no aplica

No resuelve la distribución de la clave pública: si el atacante cambia esa clave, todo verifica. No protege contra un publicador comprometido. Las pruebas de la clase usan datos sintéticos; no sustituyen una cadena de suministro con procedimientos de gestión de claves y revocación.

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
