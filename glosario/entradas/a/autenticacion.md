# Autenticación

[↑ Glosario](../../README.md) · [← Audiencia](./audiencia.md) · [Auto-actualización →](./auto-actualizacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Establecimiento de la identidad de quien hace una solicitud.

Definición de trabajo de [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md): Prueba de que quien llama controla la identidad que afirma, mediante algo que sabe, tiene o es.
- En [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md): Proceso de establecer una identidad.

## Por qué importa

En [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md), el tema «Autenticación» importa porque sin una verificación completa, un token falsificado o ajeno se acepta como si fuera válido.

## Cómo funciona

Según [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md), en la sección «Autenticación»:

Autenticar es establecer *quién* hace la solicitud. Un token firmado transporta un sujeto y unas afirmaciones, y su verificación exige varias comprobaciones: que el algoritmo sea el esperado (no el que declara la cabecera), que la firma coincida con la clave del emisor, que el emisor y la audiencia sean los de esta API, y que la hora actual esté entre `nbf` y `exp`. Cada comprobación omitida es un ataque: `alg: none` evita la firma, un token expirado se acepta para siempre, uno de otra audiencia funciona en esta API.

## Ejemplo

Ejemplo de [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) (sección «Caso conductor»):

La plataforma de entregas de tareas continúa como caso conductor de la [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md). Esta clase deja el segundo artefacto: la política de autenticación y sesión con sus mediciones. `SE-459` preguntará qué puede hacer una persona ya autenticada y por qué un identificador adivinable no es un control. Cambia después un solo dato, la reutilización de contraseñas del 2 % al 10 %, y observa qué defensa pasa a ser decisiva.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)) son:

- **Un token vencido sigue funcionando** — causa: el verificador no comprueba `exp`. Corrección: comprobar vigencia con un margen de reloj acotado.
- **Un token de otra API funciona aquí** — causa: no se comprueba la audiencia. Corrección: exigir audiencia y emisor.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En ambos casos el sistema funcionó como debía: el archivo existe, la identidad no tiene el permiso y la elevación exige una autenticación que ese contexto no ofrece. ([SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Proceso](../p/proceso.md), [ACL](./acl.md), [Audiencia](./audiencia.md), [Autorización](./autorizacion.md), [Autorización a nivel de objeto](./autorizacion-a-nivel-de-objeto.md), [Denegación por defecto](../d/denegacion-por-defecto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-458 — Identidad, autenticación y sesiones](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (61 clases más lo mencionan; las que más):

[SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), [SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md), [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md), [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md), [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Amazon](../../../casos/exito/amazon.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) — requisitos de autenticación y de contraseñas; autoridad: NIST.
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/) — requisitos de verificación de control de acceso; autoridad: OWASP.
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — gestión de claves y secretos; autoridad: OWASP.
- [Python: hmac](https://docs.python.org/3/library/hmac.html) — HMAC y comparación en tiempo constante; autoridad: Python Software Foundation.
- [Python: hashlib](https://docs.python.org/3/library/hashlib.html) — funciones hash del experimento; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Audiencia](./audiencia.md) · [Auto-actualización →](./auto-actualizacion.md)
