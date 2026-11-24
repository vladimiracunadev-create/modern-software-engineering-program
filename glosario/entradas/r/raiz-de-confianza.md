# Raíz de confianza

[↑ Glosario](../../README.md) · [← Raíz](./raiz.md) · [Rama por abstracción →](./rama-por-abstraccion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

La **raíz de confianza** (*root of trust*) es la clave o el dato que el verificador da por bueno sin comprobarlo. Es el sentido de [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) (firmas, checksums y verificación); [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md) (hardware seguro: TEE y atestación) lo aplica al hardware: el componente del que se parte sin verificación adicional. Toda cadena de verificación termina en algo así: no existe verificación sin un punto de partida aceptado.

## Por qué importa

La clave fijada es el punto que debe protegerse. Una firma impecable no vale nada si el atacante controla la clave pública con la que se comprueba. Por eso la pregunta útil no es «¿está firmado?» sino «¿de dónde obtuvo el verificador la clave, y quién puede alterarla?».

## Cómo funciona

[SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) contrasta dos situaciones:

- **La clave pública llega con el archivo:** la raíz es el sitio de descarga, y el atacante que controla el sitio controla la raíz. La firma no aporta nada.
- **La clave se fija de antemano** (viene en el instalador anterior, en el sistema operativo, en un repositorio de claves independiente, en el propio cliente): el atacante tiene que comprometer esa distribución anterior.

La estrategia es **mover la raíz a un lugar más pequeño, de actualización rara y mejor vigilado**. No se elimina la confianza, se la confina. Por eso los sistemas de actualización robustos distinguen claves por rol (raíz, objetivos, marca de tiempo) y guardan las de mayor valor fuera de línea.

En hardware ([SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md)), la raíz es un componente, normalmente de silicio, cuyo comportamiento se asume correcto; la atestación demuestra a un tercero que el código arrancó sobre esa raíz.

## Ejemplo

[SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) compara con una alternativa que no usa claves de larga vida: se confía en un proveedor de identidad y en un registro público auditable. Eso desplaza el problema: ya no custodias una clave de larga vida, pero confías en el proveedor y en el registro. Cambia la superficie de ataque y la raíz; no las elimina. La recomendación de la clase es evaluar qué raíz es más fácil de proteger en tu caso.

## Errores y confusiones comunes

- **Verificar una firma con una clave obtenida del mismo canal que el archivo.**
- **Creer que firmar elimina la confianza:** solo cambia su ubicación.
- **Una sola clave para todo:** un compromiso lo expone todo; se separan por rol.
- **Confundirla con un certificado de servidor TLS,** que se verifica contra raíces preinstaladas, que son a su vez la raíz.

## Límites y cuándo no aplica

Una raíz fija es difícil de rotar: si se compromete, hay que actualizarla por un canal que ya no es de fiar; por eso se planifica la rotación y la revocación antes de necesitarlas. En hardware, un defecto de la raíz es irreparable sin reemplazar el dispositivo.

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
