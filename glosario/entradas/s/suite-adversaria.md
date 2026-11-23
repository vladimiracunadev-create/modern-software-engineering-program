# Suite adversaria

[↑ Glosario](../../README.md) · [← Sugerencia](./sugerencia.md) · [Suite dinámica de fallas →](./suite-dinamica-de-fallas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Conjunto de pruebas que envía entradas hostiles o inesperadas.

Definición de trabajo de [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md).

## Por qué importa

La clase donde se define, [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md), existe con este propósito: el taller existe para que repares una API que funciona y está mal: diez defectos de seguridad y consistencia que ninguna prueba de camino feliz ve.

## Cómo funciona

Según [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md):

Para cada uno de los diez defectos se toma la API reparada, se reintroduce solo ese defecto y se ejecutan las tres suites. Resultado: los **siete** defectos D1 (dueño), D2 (asignación masiva), D3 (inyección), D4 (GET con efecto), D6 (cuerpo sin tope), D8 (sin idempotencia) y D10 (token sin verificar) los detecta solo la suite adversaria; D7 (validación laxa) y D9 (códigos de estado) solo la de contrato; la de camino feliz no detecta ninguno. **D5** (error con detalles internos) **no lo detecta ninguna suite** cuando se reintroduce solo.

Según [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md):

Reproduce el fallo de la clase: **creer que la API es correcta porque superó el camino feliz**. Ejecuta solo la suite de camino feliz contra la API con los diez defectos. **Síntoma:** 5 de 5 pruebas verdes. **Hipótesis rivales:** (a) la API es correcta; (b) las pruebas no ejercitan los defectos. **Prueba:** ejecuta la suite adversaria y observa 7 de 9 fallos; ejecuta la de contrato y observa 7 de 8. **Causa:** el camino feliz no envía entradas hostiles ni compara códigos de estado. **Corrección:** añadir las dos suites y reparar. **Regresión:** reintroducir cada defecto y exigir que alguna suite falle.

## Ejemplo

Ejemplo de [SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md) (sección «Caso conductor»):

El taller reúne el recorrido de la [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) sobre la plataforma de entregas. Recupera `SE-245` para D1, D2 y D10, `SE-246` para D8, `SE-248` para D6 y `SE-250` para el error de D5. La clase siguiente integra los mecanismos en un servicio contractual y operable. Cambia después una sola decisión, la suite adversaria, y revisa cuántos defectos quedan sin detectar.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-251 — Taller: reparar una API insegura e inconsistente](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md)) son:

- **Todas las pruebas pasan y la API es vulnerable** — causa: solo existen pruebas de camino feliz. Corrección: añadir suites de contrato y adversaria.
- **Un defecto reparado reaparece** — causa: no hay prueba de regresión que falle sin la reparación. Corrección: reintroducir el defecto y comprobar que falla.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Resultado: los **siete** defectos D1 (dueño), D2 (asignación masiva), D3 (inyección), D4 (GET con efecto), D6 (cuerpo sin tope), D8 (sin idempotencia) y D10 (token sin verificar) los detecta solo la suite adversaria; ([SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Asignación masiva](../a/asignacion-masiva.md), [Camino feliz](../c/camino-feliz.md), [Consulta parametrizada](../c/consulta-parametrizada.md), [Defecto dormido](../d/defecto-dormido.md), [Falso verde](../f/falso-verde.md).
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

[↑ Glosario](../../README.md) · [← Sugerencia](./sugerencia.md) · [Suite dinámica de fallas →](./suite-dinamica-de-fallas.md)
