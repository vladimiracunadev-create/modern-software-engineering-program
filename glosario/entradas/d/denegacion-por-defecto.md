# Denegación por defecto

[↑ Glosario](../../README.md) · [← Deliberate practice](./deliberate-practice.md) · [Dependencia →](./dependencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Regla por la que todo lo que la política no permite explícitamente se niega.

Definición de trabajo de [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md).

## Por qué importa

La clase donde se define, [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md), existe con este propósito: la clase existe para que distingas quién hace la solicitud (autenticación), qué le corresponde (autorización) y en qué contexto actúa (tenant, rol, solicitud), para que verifiques un token con todas sus comprobaciones y para que midas cuánto de una política de acceso protege realmente una suite de pruebas.

## Cómo funciona

Según [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md):

Una política legible es una tabla de tuplas permitidas (rol, recurso, acción) con **denegación por defecto**: lo que no está en la tabla se niega. La tabla puede revisarse en una reunión, compararse con la anterior y probarse celda a celda. Con 3 roles, 4 recursos y 4 acciones hay 48 decisiones; en la plataforma, 12 son permitidas y 36 son denegaciones. Esa asimetría importa para las pruebas.

Según [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md):

La plataforma verifica cada token con algoritmo fijado, emisor, audiencia y vigencia; extrae sujeto y rol del token; y aplica una política en tabla con denegación por defecto. Cada lectura de una entrega comprueba que el sujeto sea su dueño o un docente del curso, y devuelve 404 si no. El contexto (sujeto, curso, correlación) viaja a la capa de datos y al trabajo diferido. Compara este diseño con el original en tres casos: un token de otra API, un identificador filtrado en un registro y un rol nuevo (ayudante) que se añade a la tabla.

## Ejemplo

Ejemplo de [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) (sección «Ejemplo profesional»):

La plataforma verifica cada token con algoritmo fijado, emisor, audiencia y vigencia; extrae sujeto y rol del token; y aplica una política en tabla con denegación por defecto. Cada lectura de una entrega comprueba que el sujeto sea su dueño o un docente del curso, y devuelve 404 si no. El contexto (sujeto, curso, correlación) viaja a la capa de datos y al trabajo diferido. Compara este diseño con el original en tres casos: un token de otra API, un identificador filtrado en un registro y un rol nuevo (ayudante) que se añade a la tabla.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)) son:

- **Un token vencido sigue funcionando** — causa: el verificador no comprueba `exp`. Corrección: comprobar vigencia con un margen de reloj acotado.
- **Un token de otra API funciona aquí** — causa: no se comprueba la audiencia. Corrección: exigir audiencia y emisor.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una política legible es una tabla de tuplas permitidas (rol, recurso, acción) con **denegación por defecto**: lo que no está en la tabla se niega. ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](../r/regla.md), [Audiencia](../a/audiencia.md), [Autenticación](../a/autenticacion.md), [Autorización](../a/autorizacion.md), [Autorización a nivel de objeto](../a/autorizacion-a-nivel-de-objeto.md), [Enumeración de identificadores](../e/enumeracion-de-identificadores.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md).

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

[↑ Glosario](../../README.md) · [← Deliberate practice](./deliberate-practice.md) · [Dependencia →](./dependencia.md)
