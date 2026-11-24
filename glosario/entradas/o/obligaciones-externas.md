# Obligaciones externas

[↑ Glosario](../../README.md) · [← Objetos de valor y entidades](./objetos-de-valor-y-entidades.md) · [Observabilidad →](./observabilidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Las **obligaciones externas** son exigencias de una ley, un contrato o una norma que el equipo no puede negociar como preferencias ([SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md)). También pueden venir de una política institucional. Se distinguen de los requisitos que el equipo elige: estas llegan impuestas.

## Por qué importa

No se negocian como preferencias y exigen un responsable que las interprete. Tratarlas como un requisito más, con prioridad discutible, lleva a incumplir cuando el calendario aprieta. Cambia la gestión del requisito: se registra quién lo interpretó, con qué fuente, y se diseña desde el principio cómo se demostrará su cumplimiento.

## Cómo funciona

[SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) explica que la redacción de una obligación **rara vez es un requisito**. Una frase como «los datos personales se conservarán de forma que permita identificar a los interesados durante no más tiempo del necesario» no dice cuántos días ni a qué datos. Alguien con la competencia debe **interpretarla para el caso**. La regla de la clase: el ingeniero **no interpreta la ley**; pide la interpretación a quien tiene la competencia (jurídica, de privacidad, de cumplimiento) y la registra con su fuente y su fecha.

El proceso es una cadena de trazabilidad: obligación → interpretación (quién, cuándo) → requisito (qué hace el sistema) → prueba → evidencia. La clase muestra la cadena para la obligación de limitar la conservación del borrador, desde el texto de la obligación hasta su evidencia. Dos fallos con causa conocida: se borraron datos bajo retención legal porque la regla ignoró una excepción (se incluyen las excepciones en el requisito y en las pruebas), y una auditoría pide evidencia del borrado y no hay porque no se diseñó cómo generarla (se define la evidencia junto con el requisito, sin guardar contenido).

También hay conflictos entre obligaciones: una exige retener 730 días y otra no tener datos personales más de 365; la solución no es elegir una sino interpretar el interés de cada una y diseñar una solución que cumpla ambas, por ejemplo una copia anonimizada de los metadatos.

## Ejemplo

Obligación (texto general): limitar la conservación de datos personales. Interpretación (de privacidad, fechada): «los borradores no entregados se borran a los 90 días; las entregas aceptadas se conservan 365 días; excepción: retención legal por reclamo abierto». Requisito: «el sistema borra borradores a los 90 días salvo marca de retención». Prueba y evidencia: recuento diario de registros borrados. (Ilustración de la cadena de [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md); los plazos son de ejemplo.)

## Errores y confusiones comunes

- **Borrar bajo retención legal**: la regla ignoró una excepción.
- **Auditoría sin evidencia**: no se diseñó su generación.
- **Interpretar la ley el propio equipo** sin respaldo competente.
- **Tratarla como preferencia negociable.**

## Límites y cuándo no aplica

Las referencias normativas varían por jurisdicción y sector; el programa no las aplica como obligaciones propias. La interpretación puede cambiar con la norma, por lo que se fecha y se revisa. Una obligación interna de la organización (política) puede tener más margen que una ley, pero debe tratarse con el mismo registro.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrato](../c/contrato.md), [Preferencia](../p/preferencia.md), [Amenazas y requisitos de seguridad](../a/amenazas-y-requisitos-de-seguridad.md), [Evidencia de cumplimiento](../e/evidencia-de-cumplimiento.md), [Registro de auditoría](../r/registro-de-auditoria.md), [Requisitos de datos](../r/requisitos-de-datos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — limitación del plazo de conservación, supresión y protección desde el diseño; autoridad: Unión Europea.
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — gestión del riesgo de privacidad; autoridad: NIST.
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/) — requisitos de seguridad verificables; autoridad: OWASP.
- [Microsoft: amenazas del Threat Modeling Tool](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats) — categorías STRIDE; autoridad: Microsoft.
- [Schneier y Kelsey: Secure audit logs to support computer forensics (1999)](https://doi.org/10.1145/317087.317089) — registros con integridad encadenada; autoridad: ACM Transactions on Information and System Security.

---

[↑ Glosario](../../README.md) · [← Objetos de valor y entidades](./objetos-de-valor-y-entidades.md) · [Observabilidad →](./observabilidad.md)
