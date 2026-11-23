# Requisitos de datos

[↑ Glosario](../../README.md) · [← Requisito negativo](./requisito-negativo.md) · [Requisitos universales y negativos →](./requisitos-universales-y-negativos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Condiciones sobre qué datos se guardan, por cuánto tiempo, quién accede, cómo se borran y qué excepciones existen.

Definición de trabajo de [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md).

## Por qué importa

En [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), el tema «Requisitos de datos» importa porque fijan qué se conserva, cuánto y con qué excepciones.

## Cómo funciona

Según [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), en la sección «Requisitos de datos»:

Para cada categoría de datos, un requisito completo responde: qué se guarda, con qué finalidad, por cuánto tiempo, quién accede, cómo se borra, qué excepciones hay (retención legal, litigio) y cómo se demuestra el borrado. La regla de retención del experimento parece una línea; en realidad contiene decisiones de política (365 o 730 días según el tipo), de semántica («más de» o «al menos»), de calendario (qué es un año) y de excepción (retención legal). Cada una puede fallar por separado.

## Ejemplo

Caso medido en la sección «Requisitos de datos» de [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md):

Para cada categoría de datos, un requisito completo responde: qué se guarda, con qué finalidad, por cuánto tiempo, quién accede, cómo se borra, qué excepciones hay (retención legal, litigio) y cómo se demuestra el borrado. La regla de retención del experimento parece una línea; en realidad contiene decisiones de política (365 o 730 días según el tipo), de semántica («más de» o «al menos»), de calendario (qué es un año) y de excepción (retención legal). Cada una puede fallar por separado.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md)) son:

- **Se borraron datos bajo retención legal** — causa: la regla ignoró una excepción. Corrección: incluir las excepciones en el requisito y en las pruebas.
- **Una auditoría pide evidencia del borrado y no hay** — causa: no se diseñó cómo generarla. Corrección: definir la evidencia junto con el requisito, sin guardar contenido.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se interpretó ninguna norma para un caso real, no es asesoría legal, el diagrama y las retenciones son ejemplos del autor y la cadena de hashes no incluye claves ni sellado de tiempo. La siguiente clase protege el conjunto de requisitos con líneas base y control de cambios.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Excepción](../e/excepcion.md), [Sobre](../s/sobre.md), [Amenazas y requisitos de seguridad](../a/amenazas-y-requisitos-de-seguridad.md), [Evidencia de cumplimiento](../e/evidencia-de-cumplimiento.md), [Obligaciones externas](../o/obligaciones-externas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md).

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

[↑ Glosario](../../README.md) · [← Requisito negativo](./requisito-negativo.md) · [Requisitos universales y negativos →](./requisitos-universales-y-negativos.md)
