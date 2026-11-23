# Enumeración de identificadores

[↑ Glosario](../../README.md) · [← Enumeración](./enumeracion.md) · [Envenenamiento →](./envenenamiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Recorrido sistemático de identificadores para descubrir recursos accesibles.

Definición de trabajo de [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md).

## Por qué importa

La clase donde se define, [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md), existe con este propósito: la clase existe para que distingas quién hace la solicitud (autenticación), qué le corresponde (autorización) y en qué contexto actúa (tenant, rol, solicitud), para que verifiques un token con todas sus comprobaciones y para que midas cuánto de una política de acceso protege realmente una suite de pruebas.

## Cómo funciona

[SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md):

La plataforma verifica cada token con algoritmo fijado, emisor, audiencia y vigencia; extrae sujeto y rol del token; y aplica una política en tabla con denegación por defecto. Cada lectura de una entrega comprueba que el sujeto sea su dueño o un docente del curso, y devuelve 404 si no. El contexto (sujeto, curso, correlación) viaja a la capa de datos y al trabajo diferido.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)) son:

- **Un token vencido sigue funcionando** — causa: el verificador no comprueba `exp`. Corrección: comprobar vigencia con un margen de reloj acotado.
- **Un token de otra API funciona aquí** — causa: no se comprueba la audiencia. Corrección: exigir audiencia y emisor.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2); las cifras deterministas son idénticas, los tiempos de comparación son de cada equipo. No se auditó ninguna API ni biblioteca real, ni se midió a ninguna persona: los tokens, los usuarios y los roles son construcciones del autor. La siguiente clase pregunta qué ocurre cuando una solicitud autenticada y autorizada se repite.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Recurso](../r/recurso.md), [Audiencia](../a/audiencia.md), [Autenticación](../a/autenticacion.md), [Autorización](../a/autorizacion.md), [Autorización a nivel de objeto](../a/autorizacion-a-nivel-de-objeto.md), [Denegación por defecto](../d/denegacion-por-defecto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md).

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

[↑ Glosario](../../README.md) · [← Enumeración](./enumeracion.md) · [Envenenamiento →](./envenenamiento.md)
