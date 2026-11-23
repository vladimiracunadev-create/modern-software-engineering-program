# Amenazas y requisitos de seguridad

[↑ Glosario](../../README.md) · [← Amenaza a validez](./amenaza-a-validez.md) · [AMFE →](./amfe.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Hipótesis de ataque enumeradas por elemento del sistema y los requisitos que las mitigan o las aceptan.

Definición de trabajo de [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md).

## Por qué importa

En [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), el tema «Amenazas y requisitos de seguridad» importa porque derivan los requisitos de amenazas enumeradas en lugar de listas genéricas.

## Cómo funciona

Según [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), en la sección «Amenazas y requisitos de seguridad»:

Una lista de requisitos de seguridad copiada de un estándar es útil como punto de partida y mala como argumento. El modelado de amenazas parte de un diagrama de flujo de datos (entidades externas, procesos, almacenes y flujos) y pregunta, por tipo de elemento, qué categoría de amenaza puede aplicar: suplantación, manipulación, repudio, divulgación de información, denegación de servicio, elevación de privilegios (STRIDE). Cada pregunta termina en un requisito, en una aceptación explícita del riesgo con responsable o en una nota de «no aplica» con su razón. Una pregunta sin respuesta es un requisito que nadie escribió.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md):

La obligación de limitar la conservación del borrador, trazada hasta su evidencia:

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md)) son:

- **Se borraron datos bajo retención legal** — causa: la regla ignoró una excepción. Corrección: incluir las excepciones en el requisito y en las pruebas.
- **Una auditoría pide evidencia del borrado y no hay** — causa: no se diseñó cómo generarla. Corrección: definir la evidencia junto con el requisito, sin guardar contenido.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se interpretó ninguna norma para un caso real, no es asesoría legal, el diagrama y las retenciones son ejemplos del autor y la cadena de hashes no incluye claves ni sellado de tiempo. La siguiente clase protege el conjunto de requisitos con líneas base y control de cambios.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Hipótesis](../h/hipotesis.md), [Evidencia de cumplimiento](../e/evidencia-de-cumplimiento.md), [Obligaciones externas](../o/obligaciones-externas.md), [Registro de auditoría](../r/registro-de-auditoria.md), [Requisitos de datos](../r/requisitos-de-datos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

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

[↑ Glosario](../../README.md) · [← Amenaza a validez](./amenaza-a-validez.md) · [AMFE →](./amfe.md)
