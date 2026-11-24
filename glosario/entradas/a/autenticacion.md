# Autenticación

[↑ Glosario](../../README.md) · [← Audiencia](./audiencia.md) · [Auto-actualización →](./auto-actualizacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

La **autenticación** es el proceso de establecer quién hace una solicitud: comprobar que quien llama controla la identidad que afirma. El programa la define así en [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) («establecimiento de la identidad de quien hace una solicitud»), la precisa en [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) como la prueba de que quien llama controla esa identidad mediante algo que sabe, tiene o es, y en [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) como el proceso de establecer una identidad en un sistema operativo. Es distinta de la autorización: autenticar responde «quién eres», no «qué puedes hacer».

## Por qué importa

Toda decisión posterior de seguridad (permisos, auditoría, límites de uso) se apoya en la identidad que la autenticación establece. Si esa identidad es falsa o se acepta sin comprobar, el resto del control se aplica a la persona equivocada. Según [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md), sin una verificación completa un token falsificado o ajeno se acepta como si fuera válido. Cambia una decisión profesional concreta: qué comprobaciones debe hacer el servidor sobre cada credencial y cuáles no puede delegar al cliente.

## Cómo funciona

Un patrón habitual es el token firmado: transporta un sujeto y unas afirmaciones, y el servidor lo verifica en varias comprobaciones ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)):

- que el algoritmo sea el que el servidor espera, no el que declara la cabecera del propio token;
- que la firma coincida con la clave del emisor;
- que el emisor y la audiencia sean los de esta API;
- que la hora actual esté entre `nbf` (no antes de) y `exp` (expiración).

La causa de cada fallo es una comprobación omitida: `alg: none` evita la firma, un token expirado se acepta para siempre, uno emitido para otra audiencia funciona en esta API. En [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) la autenticación se mira como política con mediciones: los factores (saber, tener, ser), la sesión que sigue a la prueba y qué defensa pasa a ser decisiva cuando cambia un dato como la reutilización de contraseñas.

## Ejemplo

Ilustración mínima, no código de una clase:

```python
claims = decode(token, key, algorithms=["RS256"], audience="api-entregas",
                issuer="https://idp.ejemplo")
```

Fijar `algorithms`, `audience` y `issuer` en la llamada cierra los tres ataques anteriores. En la plataforma de entregas de tareas que [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) usa como caso conductor, la política de autenticación y sesión es un artefacto que se mide, no una opinión.

## Errores y confusiones comunes

- **Un token vencido sigue funcionando.** Causa: el verificador no comprueba `exp`; corrección: comprobar vigencia con un margen de reloj acotado ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)).
- **Un token de otra API funciona aquí.** Causa: no se comprueba la audiencia; corrección: exigir audiencia y emisor ([SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)).
- **Confundir autenticación con autorización.** Haber demostrado quién eres no dice qué puedes hacer; [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) trata esa segunda decisión por separado.

## Límites y cuándo no aplica

Autenticar bien no protege por sí solo: [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) muestra casos donde el sistema funciona como debía (la identidad existe, no tiene el permiso, y la elevación exige una autenticación que ese contexto no ofrece). Una autenticación correcta tampoco impide el abuso por una persona legítima. Y las cifras de [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md) son de un caso de estudio: otro sistema pide otras mediciones.

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
