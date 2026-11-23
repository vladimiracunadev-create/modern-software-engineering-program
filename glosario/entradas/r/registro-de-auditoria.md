# Registro de auditoría

[↑ Glosario](../../README.md) · [← Registro](./registro.md) · [Registro de cambios →](./registro-de-cambios.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Historial de acciones con quién, qué, cuándo y resultado, con protección frente a alteración.

Definición de trabajo de [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md).

## Por qué importa

En [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), el tema «Registros de auditoría» importa porque permiten reconstruir quién hizo qué y detectar manipulaciones.

En [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), el tema «Registro de auditoría» importa porque sin él no se reconstruye ni se responde.

## Cómo funciona

Según [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), en la sección «Registros de auditoría»:

Un registro de auditoría responde quién hizo qué, sobre qué, cuándo y con qué resultado. Para que sirva como evidencia, además de contenido necesita integridad: que no se pueda alterar o borrar sin que alguien lo note. Una cadena de hashes (cada entrada incluye el hash de la anterior) detecta la modificación y la eliminación de una entrada intermedia; no detecta el truncado del final ni la reconstrucción completa por alguien con acceso de escritura. Esas se cubren con un ancla externa: un hash publicado o guardado fuera del alcance de quien escribe el registro.

## Ejemplo

Ejemplo de [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* modela las amenazas de su agente que resume notas. Marca las capacidades: lee notas de docentes (contenido de terceros: N), accede a la base con datos de matrícula (D) y tiene una herramienta de envío de correos (E). Las tres coinciden. Rompe una: el resumen de notas pasa a un agente en cuarentena, sin base de datos ni correo, que devuelve un objeto con tres campos de valores acotados (tono, urgencia, un identificador de entrega); el agente con la base y el correo solo recibe ese objeto, nunca el texto de la nota.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md)) son:

- **Se borraron datos bajo retención legal** — causa: la regla ignoró una excepción. Corrección: incluir las excepciones en el requisito y en las pruebas.
- **Una auditoría pide evidencia del borrado y no hay** — causa: no se diseñó cómo generarla. Corrección: definir la evidencia junto con el requisito, sin guardar contenido.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- NIST SP 800-53 incluye entre sus controles la generación de registros de auditoría y la protección de su información; la clase aplica la idea sin sustituir el control completo. ([SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md))

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
