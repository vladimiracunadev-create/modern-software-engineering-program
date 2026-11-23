# Asignación masiva

[↑ Glosario](../../README.md) · [← Asignación aleatoria](./asignacion-aleatoria.md) · [Asignación, aliasing y mutación →](./asignacion-aliasing-y-mutacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Vulnerabilidad por la que se aceptan campos que el cliente no debería fijar.

Definición de trabajo de [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md): Vulnerabilidad por la que el servicio acepta campos que el cliente no debería poder fijar.

## Por qué importa

En [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md), el tema «Autorización y objeto» importa porque un acceso sin comprobar dueño y una asignación masiva rompen lo que `SE-245` fija.

## Cómo funciona

Según [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md):

Dos defectos son de autorización. **D1** no comprueba el dueño de la entrega: cualquier usuario autenticado lee cualquier identificador (`SE-245`). **D2** acepta en el `PATCH` campos que el cliente no debe fijar (`nota`, `owner`): asignación masiva, que `SE-244` previene con un esquema cerrado. Un tercero, **D10**, acepta un token sin verificar su firma. Los tres comparten el síntoma de que nada falla con usuarios bien intencionados.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md):

El equipo recibe la API con los diez defectos y trabaja en seis pasos: escribe las tres suites; mide qué falla; repara por orden de riesgo (D3, D1, D10, D2, D4, D8, D6, D7, D9, D5); añade una prueba de regresión para cada reparación; reintroduce cada defecto y registra qué suite lo detecta; y publica la lista de defectos dormidos. Compara con el original en tres casos: un usuario normal, un integrador con un script y alguien que prueba la API sin permiso.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md)) son:

- **Todas las pruebas pasan y la API es vulnerable** — causa: solo existen pruebas de camino feliz. Corrección: añadir suites de contrato y adversaria.
- **Un defecto reparado reaparece** — causa: no hay prueba de regresión que falle sin la reparación. Corrección: reintroducir el defecto y comprobar que falla.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **D2** acepta en el `PATCH` campos que el cliente no debe fijar (`nota`, `owner`): asignación masiva, que `SE-244` previene con un esquema cerrado. ([SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Servicio](../s/servicio.md), [Vulnerabilidad](../v/vulnerabilidad.md), [Camino feliz](../c/camino-feliz.md), [Consulta parametrizada](../c/consulta-parametrizada.md), [Defecto dormido](../d/defecto-dormido.md), [Deriva del contrato](../d/deriva-del-contrato.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP: Injection Flaws](https://owasp.org/www-community/Injection_Flaws) — inyección y consultas parametrizadas; autoridad: OWASP.
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/) — requisitos verificables de seguridad; autoridad: OWASP.
- [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) — validación en el servidor; autoridad: OWASP.
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — registro útil sin datos sensibles; autoridad: OWASP.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — métodos y códigos de estado; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Asignación aleatoria](./asignacion-aleatoria.md) · [Asignación, aliasing y mutación →](./asignacion-aliasing-y-mutacion.md)
