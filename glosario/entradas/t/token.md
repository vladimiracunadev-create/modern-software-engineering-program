# Token

[↑ Glosario](../../README.md) · [← Tipos y flujo](./tipos-y-flujo.md) · [Token de diseño →](./token-de-diseno.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Credencial firmada que transporta afirmaciones sobre un sujeto y su vigencia.

Definición de trabajo de [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md).

## Por qué importa

En [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md), el tema «Autenticación» importa porque sin una verificación completa, un token falsificado o ajeno se acepta como si fuera válido.

## Cómo funciona

Según [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md):

Autenticar es establecer *quién* hace la solicitud. Un token firmado transporta un sujeto y unas afirmaciones, y su verificación exige varias comprobaciones: que el algoritmo sea el esperado (no el que declara la cabecera), que la firma coincida con la clave del emisor, que el emisor y la audiencia sean los de esta API, y que la hora actual esté entre `nbf` y `exp`. Cada comprobación omitida es un ataque: `alg: none` evita la firma, un token expirado se acepta para siempre, uno de otra audiencia funciona en esta API.

Según [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md):

La plataforma verifica cada token con algoritmo fijado, emisor, audiencia y vigencia; extrae sujeto y rol del token; y aplica una política en tabla con denegación por defecto. Cada lectura de una entrega comprueba que el sujeto sea su dueño o un docente del curso, y devuelve 404 si no. El contexto (sujeto, curso, correlación) viaja a la capa de datos y al trabajo diferido. Compara este diseño con el original en tres casos: un token de otra API, un identificador filtrado en un registro y un rol nuevo (ayudante) que se añade a la tabla.

## Ejemplo

Ejemplo de [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) (sección «Ejemplo profesional»):

La plataforma verifica cada token con algoritmo fijado, emisor, audiencia y vigencia; extrae sujeto y rol del token; y aplica una política en tabla con denegación por defecto. Cada lectura de una entrega comprueba que el sujeto sea su dueño o un docente del curso, y devuelve 404 si no. El contexto (sujeto, curso, correlación) viaja a la capa de datos y al trabajo diferido. Compara este diseño con el original en tres casos: un token de otra API, un identificador filtrado en un registro y un rol nuevo (ayudante) que se añade a la tabla.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un token vencido sigue funcionando** — causa: el verificador no comprueba `exp`. Corrección: comprobar vigencia con un margen de reloj acotado. ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md))
- **Un token de otra API funciona aquí** — causa: no se comprueba la audiencia. Corrección: exigir audiencia y emisor. ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md))
- **El rol llega en un encabezado del cliente** — causa: contexto tomado de datos controlados por el cliente. Corrección: derivar rol y sujeto del token verificado. ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un token firmado transporta un sujeto y unas afirmaciones, y su verificación exige varias comprobaciones: que el algoritmo sea el esperado (no el que declara la cabecera), que la firma coincida con la clave del emisor, que el emisor y la audiencia sean los de esta API, y que la hora actual esté entre `nbf` y `exp`. ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md))
- **Prueba:** repite la solicitud con un token de otro alumno y con un token falso, y observa que las dos devuelven lo mismo. ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Sobre](../s/sobre.md), [Sujeto](../s/sujeto.md), [Vigencia](../v/vigencia.md), [Audiencia](../a/audiencia.md), [Autenticación](../a/autenticacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (105 clases más lo mencionan; las que más):

[SE-467](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), [SE-175](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), [SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md), [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/) — requisitos de verificación de control de acceso; autoridad: OWASP.
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — gestión de claves y secretos; autoridad: OWASP.
- [Python: hmac](https://docs.python.org/3/library/hmac.html) — HMAC y comparación en tiempo constante; autoridad: Python Software Foundation.
- [Python: hashlib](https://docs.python.org/3/library/hashlib.html) — funciones hash del experimento; autoridad: Python Software Foundation.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — códigos 401, 403 y 404; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Tipos y flujo](./tipos-y-flujo.md) · [Token de diseño →](./token-de-diseno.md)
