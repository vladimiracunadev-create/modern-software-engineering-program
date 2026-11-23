# Tenant

[↑ Glosario](../../README.md) · [← Temporizador de vigilancia](./temporizador-de-vigilancia.md) · [Terminación →](./terminacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Unidad aislada (institución o curso) a la que pertenecen los datos y que limita el alcance de un sujeto.

Definición de trabajo de [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md).

## Por qué importa

En [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md), el tema «Contexto de la solicitud» importa porque rol, tenant y sujeto deben venir del token verificado y no de campos que el cliente controla.

## Cómo funciona

Según [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md):

El **contexto** es la información que acompaña cada solicitud y condiciona su tratamiento: el sujeto, el rol, el curso o institución (tenant) y el identificador de correlación. La regla es que todo dato de identidad sale del token verificado en el servidor; un encabezado `X-Rol: docente` enviado por el cliente es una afirmación sin respaldo. El contexto se propaga a las capas inferiores (consulta, cola, registro) para que cada una pueda aplicar la misma política.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md):

La plataforma verifica cada token con algoritmo fijado, emisor, audiencia y vigencia; extrae sujeto y rol del token; y aplica una política en tabla con denegación por defecto. Cada lectura de una entrega comprueba que el sujeto sea su dueño o un docente del curso, y devuelve 404 si no. El contexto (sujeto, curso, correlación) viaja a la capa de datos y al trabajo diferido.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)) son:

- **Un token vencido sigue funcionando** — causa: el verificador no comprueba `exp`. Corrección: comprobar vigencia con un margen de reloj acotado.
- **Un token de otra API funciona aquí** — causa: no se comprueba la audiencia. Corrección: exigir audiencia y emisor.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2); las cifras deterministas son idénticas, los tiempos de comparación son de cada equipo. No se auditó ninguna API ni biblioteca real, ni se midió a ninguna persona: los tokens, los usuarios y los roles son construcciones del autor. La siguiente clase pregunta qué ocurre cuando una solicitud autenticada y autorizada se repite.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Sujeto](../s/sujeto.md), [Audiencia](../a/audiencia.md), [Autenticación](../a/autenticacion.md), [Autorización](../a/autorizacion.md), [Autorización a nivel de objeto](../a/autorizacion-a-nivel-de-objeto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-245 — Autenticación, autorización y contexto](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-411](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md).

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

[↑ Glosario](../../README.md) · [← Temporizador de vigilancia](./temporizador-de-vigilancia.md) · [Terminación →](./terminacion.md)
