# Sujeto

[↑ Glosario](../../README.md) · [← Suite dinámica de fallas](./suite-dinamica-de-fallas.md) · [Suma de verificación →](./suma-de-verificacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Notificación que identifica quién pide, por ejemplo un repositorio y una rama.

Definición de trabajo de [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md): Identidad autenticada que realiza la solicitud.
- En [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md): Artefacto al que se refiere una atestación, identificado por su huella.
- En [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md): Proceso y contexto de identidad que solicita una acción.

## Por qué importa

La clase donde se define, [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), existe con este propósito: la clase existe para que sustituyas la credencial que alguien copió en un secreto del repositorio por una identidad que la canalización demuestra en cada ejecución y que el proveedor cambia por una credencial de minutos.

## Cómo funciona

Según [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md):

El esquema general, que GitHub Actions implementa sobre OpenID Connect, tiene cuatro pasos. El job, si tiene permiso para ello, pide al emisor de la plataforma de integración continua un **token de identidad**: un documento firmado que dice quién es (repositorio, rama, entorno, flujo de trabajo), quién lo emitió (`iss`), a quién va dirigido (`aud`), hasta cuándo vale (`exp`) y desde cuándo (`nbf`). El job presenta ese token al proveedor de la nube. El proveedor lo valida (firma con las claves públicas del emisor, vigencia, emisor y audiencia esperados) y comprueba la **regla de confianza** configurada en su lado: «acepto tokens cuyo sujeto sea exactamente este repositorio y esta rama». Si coincide, devuelve una credencial temporal con los permisos del rol asociado.

Según [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md):

El equipo de la API de entregas retira la clave de la nube del repositorio. El job de despliegue pide el permiso de identidad y ningún otro job lo tiene. En la nube crean un rol que solo puede publicar en un registro y actualizar un servicio, y una regla de confianza con emisor de la plataforma, audiencia propia del receptor, sujeto exacto del repositorio y del entorno de producción —que exige una aprobación humana— y vida máxima del token de quince minutos. Escriben diez pruebas con tokens manipulados (sujeto de otro repositorio, de una bifurcación, de una rama sin proteger, audiencia ajena, expirado) y exigen que todas sean rechazadas.

## Ejemplo

Ejemplo de [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md) (sección «Ejemplo mínimo»):

El fragmento firma un token y muestra que alterar una sola notificación invalida la firma. Antes de ejecutarlo, predice si cambiar el sujeto sin volver a firmar deja el token aceptable.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un repositorio ajeno obtiene credenciales** — causa: sujeto con prefijo o comodín. Corrección: sujeto exacto y pruebas con tokens manipulados. ([SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md))
- **El rol llega en un encabezado del cliente** — causa: contexto tomado de datos controlados por el cliente. Corrección: derivar rol y sujeto del token verificado. ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md))
- **Un SBOM válido describe otro artefacto** — causa: sin vínculo por huella. Corrección: sujeto identificado por la huella del artefacto. ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Solo el sujeto exacto y la vida corta dejan fuera los doce y mantienen los legítimos. ([SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md))
- Un token firmado transporta un sujeto y unas afirmaciones, y su verificación exige varias comprobaciones: que el algoritmo sea el esperado (no el que declara la cabecera), que la firma coincida con la clave del emisor, que el emisor y la audiencia sean los de esta API, y que la hora actual esté entre `nbf` y `exp`. ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](../a/artefacto.md), [Atestación](../a/atestacion.md), [Contextos](../c/contextos.md), [Huella](../h/huella.md), [ACL](../a/acl.md), [Audiencia](../a/audiencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-472 — SBOM, procedencia y atestaciones](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), [SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), [SE-479](../../../classes/part-39-build-release-y-cadena-de-suministro/se-479-taller-verificar-la-procedencia-de-un-release/README.md), [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md), [SE-543](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md).

**Aparece en los casos de estudio:** [Mercado Libre](../../../casos/exito/mercado-libre.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «sub».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub: OpenID Connect en Actions](https://docs.github.com/en/actions/concepts/security/openid-connect) — identidad federada para flujos de trabajo y formato del sujeto; autoridad: documentación de GitHub, consultada el 15 de noviembre de 2026.
- [in-toto: declaración (Statement)](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) — atestaciones ligadas a un sujeto; autoridad: proyecto in-toto.
- [RFC 7519: JSON Web Token](https://www.rfc-editor.org/rfc/rfc7519) — notificaciones registradas y vigencia; autoridad: IETF.
- [RFC 8725: buenas prácticas para JWT](https://www.rfc-editor.org/rfc/rfc8725) — validación del algoritmo, emisor y audiencia; autoridad: IETF.
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) — token de identidad y su validación; autoridad: OpenID Foundation.

---

[↑ Glosario](../../README.md) · [← Suite dinámica de fallas](./suite-dinamica-de-fallas.md) · [Suma de verificación →](./suma-de-verificacion.md)
