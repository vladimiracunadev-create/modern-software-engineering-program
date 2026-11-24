# Requisitos de datos

[↑ Glosario](../../README.md) · [← Requisito negativo](./requisito-negativo.md) · [Requisitos universales y negativos →](./requisitos-universales-y-negativos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Los **requisitos de datos** son las condiciones sobre qué datos se guardan, por cuánto tiempo, quién accede, cómo se borran y qué excepciones existen ([SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md)). Forman parte de los requisitos de un sistema y suelen venir de obligaciones externas (privacidad, retención legal).

## Por qué importa

Fijan qué se conserva, cuánto y con qué excepciones. Una regla de retención aparentemente simple («borrar a los 365 días») oculta decisiones de política que, si no se explicitan, se toman por defecto en el código. Cambia el contenido de un requisito de datos: no basta con la frase de retención; hay que responder un conjunto de preguntas.

## Cómo funciona

[SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) propone que, para cada categoría de datos, un requisito completo responda:

- **qué se guarda**;
- **con qué finalidad**;
- **por cuánto tiempo**;
- **quién accede**;
- **cómo se borra**;
- **qué excepciones hay** (retención legal, litigio);
- **cómo se demuestra el borrado**.

La regla de retención del experimento de la clase **parece una línea y contiene decisiones**: de política (365 o 730 días según el tipo de dato), de semántica («más de» 365 días o «al menos» 365, desde qué fecha se cuenta) y de excepciones (qué ocurre con un registro sujeto a retención legal). Cada una debe tener respuesta y responsable.

La prueba del requisito incluye **frontera** (un registro de 365 días y uno de 366) y **excepción** (un registro con marca de retención no se borra). Dos fallos con causa conocida: se borraron datos bajo retención legal porque la regla ignoró una excepción (se incluyen las excepciones en el requisito y en las pruebas), y una auditoría pide evidencia del borrado y no hay porque no se diseñó cómo generarla (se define la evidencia junto con el requisito, **sin guardar contenido**: el recuento de registros borrados por día, no los registros). Los conflictos entre obligaciones (una exige conservar más y otra menos) se resuelven con negociación por intereses, por ejemplo con una copia anonimizada de los metadatos.

## Ejemplo

Categoría «borradores de entrega». Se guarda: texto y archivos adjuntos; finalidad: permitir recuperar el trabajo; plazo: 90 días desde la última edición; acceso: la estudiante y soporte con registro; borrado: tarea diaria que elimina contenido y conserva solo el identificador; excepción: marca de retención por reclamo abierto; evidencia: recuento diario de registros borrados. (Requisito ilustrativo con las preguntas de [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md).)

## Errores y confusiones comunes

- **Se borraron datos bajo retención legal**: se ignoró una excepción.
- **Auditoría sin evidencia del borrado.**
- **Una sola línea de retención para todo.**
- **Guardar contenido para demostrar su borrado.**

## Límites y cuándo no aplica

Los plazos y excepciones los define quien interpreta la obligación (ver obligaciones externas), no el equipo técnico. El requisito no resuelve cómo borrar de respaldos y réplicas, que debe tratarse aparte. Para datos no personales y sin obligación, una política de retención sencilla puede bastar.

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
