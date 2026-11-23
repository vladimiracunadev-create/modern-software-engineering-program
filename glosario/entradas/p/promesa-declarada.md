# Promesa declarada

[↑ Glosario](../../README.md) · [← Progreso](./progreso.md) · [Promoción →](./promocion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Garantía escrita en el contrato que todavía no tiene una comprobación que la ejecute.

Definición de trabajo de [SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md).

## Por qué importa

La clase donde se define, [SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), existe con este propósito: el proyecto existe para que entregues un servicio pequeño pero completo cuyo contrato se pueda comprobar y cuyo comportamiento ante fallos se pueda demostrar: alta con clave de idempotencia, trabajo diferido con outbox, errores con forma única, política de acceso, límites y sondeos.

## Cómo funciona

[SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md):

El servicio de la plataforma ofrece 12 rutas: alta con clave de idempotencia (201), lectura, listado paginado por clave, edición con `If-Match`, anulación, apelación (202), estado de trabajo, cancelación, nota, resumen del curso y dos sondeos de salud. Entrega tres artefactos: el contrato OpenAPI con esquemas cerrados, el comprobador que lo compara con las rutas reales y el informe de inyección de caídas con los cuatro invariantes. Se opera con un SLO de 99,5 %, dos alertas por tasa de consumo y un informe semanal del presupuesto.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md)) son:

- **El contrato y el código divergen** — causa: no hay comprobación de conformidad. Corrección: comparador en la integración continua con esquema cerrado.
- **Hay entregas duplicadas o sin nota tras un reinicio** — causa: efectos fuera de la transacción y handler no idempotente. Corrección: clave, outbox y efecto idempotente.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se desplegó ningún servicio ni se midió a ninguna persona: las caídas, el SLO, los incidentes y las mutaciones son construcciones del autor. La [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md) lleva el producto a móviles y escritorio.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrato](../c/contrato.md), [Garantía](../g/garantia.md), [Burn rate](../b/burn-rate.md), [Conformidad](../c/conformidad.md), [Indicador de nivel de servicio](../i/indicador-de-nivel-de-servicio.md), [Invariante](../i/invariante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE Book: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — indicadores, objetivos y presupuesto de error; autoridad: Google.
- [Google SRE Book: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — señales y alertas sobre síntomas; autoridad: Google.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — descripción de contratos de API; autoridad: OpenAPI Initiative.
- [JSON Schema 2020-12: Validation](https://json-schema.org/draft/2020-12/json-schema-validation) — esquemas cerrados de entrada y salida; autoridad: proyecto JSON Schema.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — semántica de métodos y códigos de estado; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Progreso](./progreso.md) · [Promoción →](./promocion.md)
