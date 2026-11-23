# Consulta parametrizada

[↑ Glosario](../../README.md) · [← Constructor de datos](./constructor-de-datos.md) · [Consulta recursiva →](./consulta-recursiva.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Consulta en la que los datos se pasan separados de la instrucción SQL.

Definición de trabajo de [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md): Sentencia SQL enviada al motor separada de los valores, de modo que los valores no pueden alterar su estructura.

## Por qué importa

La clase donde se define, [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md), existe con este propósito: el taller existe para que repares una API que funciona y está mal: diez defectos de seguridad y consistencia que ninguna prueba de camino feliz ve.

## Cómo funciona

Según [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md):

Con SQL concatenado, **3 de 12** cargas devuelven filas de otro usuario y **2** provocan un error del motor; con consulta parametrizada, **0** y **0**. Los parámetros no sustituyen la autorización, y no protegen los nombres de columna u orden que vengan del cliente: esos se validan contra una lista cerrada.

Según [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md):

Previenen la forma más común si se usan como están pensados (consultas parametrizadas, autoescape de plantillas). Fallan cuando se desactiva el autoescape, se arma una consulta a mano para un caso especial o se pasa un nombre de columna del cliente. Los frameworks reducen la superficie; no la eliminan.

## Ejemplo

Ejemplo de [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md) (sección «Preguntas frecuentes»):

Previenen la forma más común si se usan como están pensados (consultas parametrizadas, autoescape de plantillas). Fallan cuando se desactiva el autoescape, se arma una consulta a mano para un caso especial o se pasa un nombre de columna del cliente. Los frameworks reducen la superficie; no la eliminan.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md)) son:

- **Todas las pruebas pasan y la API es vulnerable** — causa: solo existen pruebas de camino feliz. Corrección: añadir suites de contrato y adversaria.
- **Un defecto reparado reaparece** — causa: no hay prueba de regresión que falle sin la reparación. Corrección: reintroducir el defecto y comprobar que falla.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con una API de laboratorio en proceso en Windows y Ubuntu (WSL2), con resultados idénticos. No se probó ningún servidor con red ni una API real, y nadie fue evaluado: los diez defectos y las tres suites son construcciones del autor. La siguiente clase integra los mecanismos en un servicio contractual y operable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estructura](../e/estructura.md), [Instrucción](../i/instruccion.md), [Motor](../m/motor.md), [Valor](../v/valor.md), [Asignación masiva](../a/asignacion-masiva.md), [Camino feliz](./camino-feliz.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md), [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP: Injection Flaws](https://owasp.org/www-community/Injection_Flaws) — inyección y consultas parametrizadas; autoridad: OWASP.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — consultas parametrizadas; autoridad: Python Software Foundation.
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/) — requisitos verificables de seguridad; autoridad: OWASP.
- [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) — validación en el servidor; autoridad: OWASP.
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — registro útil sin datos sensibles; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← Constructor de datos](./constructor-de-datos.md) · [Consulta recursiva →](./consulta-recursiva.md)
