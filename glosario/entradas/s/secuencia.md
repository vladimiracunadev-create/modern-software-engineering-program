# Secuencia

[↑ Glosario](../../README.md) · [← Secretos y configuración](./secretos-y-configuracion.md) · [Secuencia de escape →](./secuencia-de-escape.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Número monótono dentro de lo firmado que impide aceptar una versión anterior.

Definición de trabajo de [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-066 — Colecciones y transformación de datos](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md): Colección ordenada accesible por posición.
- En [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md): Orden de ejecución de las tareas que respeta las dependencias.

## Por qué importa

La clase donde se define, [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), existe con este propósito: la clase existe para que puedas decidir qué comprueba quien instala tu software antes de ejecutarlo, y para que sepas qué ataque detiene cada comprobación y cuál no.

## Cómo funciona

Según [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md):

Una **firma digital** se calcula con una clave privada sobre unos datos y se verifica con la clave pública correspondiente. La verificación correcta prueba que quien posee la clave privada firmó exactamente esos bytes; no prueba quién es esa persona, que la clave sea de quien se cree, que el contenido sea benigno ni que sea reciente. Ed25519 es un algoritmo de firma moderno, con claves y firmas cortas (32 y 64 bytes) y verificación rápida, especificado en el RFC 8032. Usar firmas en lugar de solo huellas permite que el publicador y el verificador no compartan un secreto y que cualquiera pueda comprobar.

Según [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md):

La API de entregas publica un manifiesto (`release.json`) con nombre, versión, número de secuencia y las huellas del artefacto, del SBOM y de la procedencia, firmado con Ed25519. El cliente de línea de órdenes incorpora la clave pública en cada versión que él mismo distribuye y recuerda la mayor secuencia vista; antes de instalar calcula la huella del archivo descargado, comprueba la firma del manifiesto con la clave incorporada, comprueba el nombre, rechaza una secuencia inferior a la recordada y falla cerrado ante cualquier discrepancia. La clave de firma vive en un servicio de claves con acceso solo desde el trabajo de publicación, y existe una declaración de rotación firmada y preparada con una clave de reserva guardada fuera de línea.

## Ejemplo

Ejemplo de [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) (sección «Ejemplo profesional»):

La API de entregas publica un manifiesto (`release.json`) con nombre, versión, número de secuencia y las huellas del artefacto, del SBOM y de la procedencia, firmado con Ed25519. El cliente de línea de órdenes incorpora la clave pública en cada versión que él mismo distribuye y recuerda la mayor secuencia vista; antes de instalar calcula la huella del archivo descargado, comprueba la firma del manifiesto con la clave incorporada, comprueba el nombre, rechaza una secuencia inferior a la recordada y falla cerrado ante cualquier discrepancia.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se acepta una versión antigua vulnerable** — causa: sin secuencia ni caducidad en lo firmado. Corrección: número monótono firmado y recordado por el cliente. ([SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Las defensas son un número de **secuencia** o versión monótono dentro de lo firmado, que el cliente recuerda y no acepta que disminuya, y una **fecha de caducidad** en los metadatos que obliga a renovarlos con regularidad. ([SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Colección](../c/coleccion.md), [Dependencia](../d/dependencia.md), [Tarea](../t/tarea.md), [Versión](../v/version.md), [Arrepentimiento](../a/arrepentimiento.md), [Comprensión](../c/comprension.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-066 — Colecciones y transformación de datos](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-473 — Firmas, checksums y verificación](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

**También se usa en** (592 clases más lo mencionan; las que más):

[SE-425](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-425-pruebas-basadas-en-propiedades-y-modelos/README.md), [SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md), [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), [SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md), [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Update Framework: especificación](https://theupdateframework.io/specification/) — actualizaciones seguras, secuencia y caducidad; autoridad: proyecto TUF, CNCF.
- [RFC 8032: EdDSA](https://www.rfc-editor.org/rfc/rfc8032) — algoritmo de firma Ed25519; autoridad: IETF.
- [Samuel et al., «Survivable key compromise in software update systems»](https://doi.org/10.1145/1866307.1866315) — diseño frente al compromiso de claves; autoridad: ACM CCS 2010.
- [Sigstore: documentación](https://docs.sigstore.dev/) — firma con identidades efímeras y registro de transparencia; autoridad: proyecto Sigstore, OpenSSF.
- [OpenSSL: pkeyutl](https://docs.openssl.org/3.0/man1/openssl-pkeyutl/) — firma y verificación en los experimentos; autoridad: proyecto OpenSSL.

---

[↑ Glosario](../../README.md) · [← Secretos y configuración](./secretos-y-configuracion.md) · [Secuencia de escape →](./secuencia-de-escape.md)
