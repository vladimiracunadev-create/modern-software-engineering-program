# Sujeto

[↑ Glosario](../../README.md) · [← Suite dinámica de fallas](./suite-dinamica-de-fallas.md) · [Suma de verificación →](./suma-de-verificacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

**Sujeto** es la identidad, o el objeto, a quien se refiere una afirmación de seguridad. El programa lo usa con tres sentidos relacionados:

- **Identidad autenticada que realiza una solicitud** ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)): la parte de un token que dice *quién* actúa.
- **Proceso y contexto de identidad que solicita una acción** ([SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md)): quien intenta usar un recurso en un sistema operativo.
- **Artefacto al que se refiere una atestación** ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md)): el objeto sobre el que se afirma algo, identificado por su huella.

En [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md) se emplea para la afirmación de un token de identidad: repositorio, rama o entorno que pide una credencial.

## Por qué importa

Toda decisión de acceso se toma sobre un sujeto. Si el sujeto se define de forma laxa (con prefijo o comodín), un tercero que coincida con el patrón obtiene acceso. Si el rol del sujeto se toma de datos que controla el cliente, el control es ilusorio. La decisión que cambia es de dónde se deriva el sujeto y con qué exactitud se compara.

## Cómo funciona

**En tokens** ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)): un token firmado transporta un sujeto y unas afirmaciones; su verificación exige comprobar el algoritmo, la firma, el emisor, la audiencia y la vigencia. El sujeto y el rol se derivan del token verificado, no de lo que el cliente declara.

**En identidad de integración continua** ([SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md)): el *job* pide a la plataforma un token de identidad (firmado, con repositorio, rama, entorno, emisor, audiencia y vigencia); la nube lo valida y comprueba una **regla de confianza** del tipo «acepto tokens cuyo sujeto sea exactamente este repositorio y esta rama». Si coincide, entrega una credencial temporal. Solo el sujeto exacto y la vida corta dejan fuera los casos ilegítimos y mantienen los legítimos.

**En atestaciones** ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md)): el sujeto es el artefacto, identificado por su huella; así un SBOM o una declaración de procedencia queda vinculado al objeto exacto.

## Ejemplo

```text
sujeto aceptado:   repo:universidad/api-entregas:environment:produccion
sujeto rechazado:  repo:universidad/api-entregas-fork:ref:refs/heads/feature   (otro repositorio / rama sin proteger)
regla:             igualdad exacta, no prefijo ni comodín; token con vida máxima de 15 minutos
```

## Errores y confusiones comunes

- **Un repositorio ajeno obtiene credenciales.** Causa: sujeto con prefijo o comodín; corrección: sujeto exacto y pruebas con tokens manipulados ([SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md)).
- **El rol llega en un encabezado del cliente.** Causa: contexto tomado de datos controlados por el cliente; corrección: derivar rol y sujeto del token verificado ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)).
- **Un SBOM válido describe otro artefacto.** Causa: sin vínculo por huella; corrección: sujeto identificado por la huella del artefacto ([SE-472](../../../classes/part-39-build-release-y-cadena-de-suministro/se-472-sbom-procedencia-y-atestaciones/README.md)).

## Límites y cuándo no aplica

El sentido de la palabra cambia con el contexto: no es lo mismo el sujeto de una solicitud que el de una atestación. La regla de confianza de [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md) protege si el emisor del token es de fiar; si la plataforma de integración continua está comprometida, un sujeto exacto no basta. Y un sujeto bien verificado solo responde «quién»: «qué puede hacer» es autorización.

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
