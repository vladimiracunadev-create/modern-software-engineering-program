# Registro de auditoría

[↑ Glosario](../../README.md) · [← Registro](./registro.md) · [Registro de cambios →](./registro-de-cambios.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Un **registro de auditoría** es un historial de acciones que responde quién hizo qué, sobre qué, cuándo y con qué resultado, protegido frente a la alteración ([SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md)). [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) lo exige también en sistemas con agentes de IA: sin él no se reconstruye lo ocurrido ni se puede responder por ello. No es un registro técnico de depuración (logs de errores), aunque pueda convivir con ellos.

## Por qué importa

Es lo que permite reconstruir los hechos y detectar manipulaciones. Una auditoría, una investigación de incidente o una disputa necesitan evidencia de lo que ocurrió y de quién lo hizo. Si el registro puede alterarse sin dejar rastro, no sirve como evidencia. Cambia el diseño: no basta escribir líneas; hay que decidir su contenido, su integridad y su retención.

## Cómo funciona

[SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) distingue dos requisitos. El **contenido**: quién (identidad), qué (acción), sobre qué (objeto), cuándo (hora) y con qué resultado. Y la **integridad**: que no se pueda alterar o borrar sin que alguien lo note. Un mecanismo básico es la **cadena de hashes**: cada entrada incluye el hash de la anterior, de modo que modificar o eliminar una entrada intermedia rompe la cadena y se detecta.

La clase precisa sus límites: la cadena de hashes **no detecta el truncado del final** (borrar las últimas entradas deja una cadena válida) ni la **reconstrucción completa** por alguien con acceso de escritura que recalcule todos los hashes. Esas amenazas se cubren con un **ancla externa**: publicar periódicamente el hash más reciente en un lugar que el atacante no controle, o enviarlo a un sistema de solo anexar. NIST SP 800-53 incluye controles de generación y protección de registros de auditoría, como marco de referencia.

Hay una tensión con la privacidad: el registro debe permitir demostrar lo ocurrido sin guardar el contenido sensible. [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) la ilustra con el borrado de datos: si una auditoría pide evidencia de que se borró algo y no hay, es porque no se diseñó cómo generarla; se define la evidencia junto con el requisito, sin guardar el contenido borrado. Y bajo retención legal el borrado no procede: la regla debe incluir las excepciones.

## Ejemplo

Cada entrada de un registro de la plataforma incluye: `{actor: "docente-17", acción: "conceder_prórroga", objeto: "entrega-342", hora: "…", resultado: "ok", hash_anterior: "…"}`. Si alguien edita la entrada 40, el `hash_anterior` de la 41 deja de coincidir; si borra las entradas 90–100 y reescribe el final, solo el ancla publicada ayer lo delata. (Estructura ilustrativa; [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) desarrolla la técnica.)

## Errores y confusiones comunes

- **Registrar sin integridad**: se puede editar sin que nadie lo note.
- **Pensar que la cadena de hashes lo resuelve todo**: no ve el truncado ni la reconstrucción completa.
- **Guardar contenido sensible en el registro** para «tener evidencia».
- **No diseñar la evidencia del borrado** y fallar la auditoría.

## Límites y cuándo no aplica

El registro prueba que algo se registró, no que sea verdad: si el sistema que escribe está comprometido, escribirá lo que el atacante quiera. Necesita retención acotada y control de acceso, porque también es un blanco. Para sistemas de bajo riesgo, un registro estructurado sin cadena de hashes puede bastar; el nivel de protección se calibra con el costo de una disputa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](./resultado.md), [Agente en cuarentena](../a/agente-en-cuarentena.md), [Amenazas y requisitos de seguridad](../a/amenazas-y-requisitos-de-seguridad.md), [Cadena de huellas](../c/cadena-de-huellas.md), [Contenido no confiable](../c/contenido-no-confiable.md), [Evidencia de cumplimiento](../e/evidencia-de-cumplimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (13 clases más lo mencionan; las que más):

[SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md), [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md), [SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md), [SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md), [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), [SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Registros de auditoría», «registros de auditoría».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — limitación del plazo de conservación, supresión y protección desde el diseño; autoridad: Unión Europea.
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — gestión del riesgo de privacidad; autoridad: NIST.
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/) — requisitos de seguridad verificables; autoridad: OWASP.
- [Microsoft: amenazas del Threat Modeling Tool](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats) — categorías STRIDE; autoridad: Microsoft.
- [Schneier y Kelsey: Secure audit logs to support computer forensics (1999)](https://doi.org/10.1145/317087.317089) — registros con integridad encadenada; autoridad: ACM Transactions on Information and System Security.

---

[↑ Glosario](../../README.md) · [← Registro](./registro.md) · [Registro de cambios →](./registro-de-cambios.md)
