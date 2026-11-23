# Defecto dormido

[↑ Glosario](../../README.md) · [← Defecto de sentido](./defecto-de-sentido.md) · [Defecto enmascarado →](./defecto-enmascarado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Defecto que no tiene síntoma observable hasta que otro fallo lo activa.

Definición de trabajo de [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md).

## Por qué importa

La clase donde se define, [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md), existe con este propósito: el taller existe para que repares una API que funciona y está mal: diez defectos de seguridad y consistencia que ninguna prueba de camino feliz ve.

## Cómo funciona

Según [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md):

La razón de D5 es instructiva: el defecto está en el camino de error, y con la inyección corregida ya no hay ningún error de la base de datos que lo active. Es un defecto dormido: existe en el código, no tiene síntoma observable y se despertará cuando otro fallo lo ejercite. Para verlo hace falta una prueba que fuerce un error interno por otro medio.

Según [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md):

El equipo recibe la API con los diez defectos y trabaja en seis pasos: escribe las tres suites; mide qué falla; repara por orden de riesgo (D3, D1, D10, D2, D4, D8, D6, D7, D9, D5); añade una prueba de regresión para cada reparación; reintroduce cada defecto y registra qué suite lo detecta; y publica la lista de defectos dormidos. Compara con el original en tres casos: un usuario normal, un integrador con un script y alguien que prueba la API sin permiso.

## Ejemplo

Ejemplo de [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md) (sección «Ejemplo profesional»):

El equipo recibe la API con los diez defectos y trabaja en seis pasos: escribe las tres suites; mide qué falla; repara por orden de riesgo (D3, D1, D10, D2, D4, D8, D6, D7, D9, D5); añade una prueba de regresión para cada reparación; reintroduce cada defecto y registra qué suite lo detecta; y publica la lista de defectos dormidos. Compara con el original en tres casos: un usuario normal, un integrador con un script y alguien que prueba la API sin permiso.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md)) son:

- **Todas las pruebas pasan y la API es vulnerable** — causa: solo existen pruebas de camino feliz. Corrección: añadir suites de contrato y adversaria.
- **Un defecto reparado reaparece** — causa: no hay prueba de regresión que falle sin la reparación. Corrección: reintroducir el defecto y comprobar que falla.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Es un defecto dormido: existe en el código, no tiene síntoma observable y se despertará cuando otro fallo lo ejercite. ([SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Asignación masiva](../a/asignacion-masiva.md), [Camino feliz](../c/camino-feliz.md), [Consulta parametrizada](../c/consulta-parametrizada.md), [Falso verde](../f/falso-verde.md), [Mutación](../m/mutacion.md), [Prueba de regresión](../p/prueba-de-regresion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

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

[↑ Glosario](../../README.md) · [← Defecto de sentido](./defecto-de-sentido.md) · [Defecto enmascarado →](./defecto-enmascarado.md)
