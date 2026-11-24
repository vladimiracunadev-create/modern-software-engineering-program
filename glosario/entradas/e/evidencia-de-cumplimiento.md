# Evidencia de cumplimiento

[↑ Glosario](../../README.md) · [← Evidencia](./evidencia.md) · [Evidencia de ejecución →](./evidencia-de-ejecucion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

La **evidencia de cumplimiento** son los artefactos fechados que sostienen una afirmación de que se cumple una obligación ([SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md)). [SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md) la formula como un registro verificable de un procedimiento de prueba, su criterio y su resultado. Cumplir es una afirmación; la evidencia es lo que la sostiene.

## Por qué importa

Una afirmación de cumplimiento vale lo que la evidencia que la sostiene. Una norma o un auditor no pide que el sistema sea seguro o resiliente: pide **evidencia de que los controles funcionan**. Cambia el diseño: un requisito necesita, desde su redacción, una forma de producir su evidencia, no solo una forma de cumplirse.

## Cómo funciona

[SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) enumera ejemplos: la configuración vigente, el resultado fechado de una prueba, el registro del borrado. Una auditoría pregunta por ambas cosas, el control y la evidencia. Tres propiedades se piden a la evidencia: que pueda **generarse sin intervención heroica** (automática o con poco esfuerzo, no reconstruida a mano antes de la auditoría), que **no exponga datos personales** (el recuento de registros borrados por día, no los registros) y que sea **verificable por un tercero**.

Un requisito sin una forma de generar su evidencia cumplida es un requisito que no se puede demostrar. Por eso el síntoma «una auditoría pide evidencia del borrado y no hay» tiene como corrección definir la evidencia junto con el requisito, sin guardar contenido. También las excepciones de la regla (retención legal) deben incluirse en el requisito y en las pruebas.

[SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md) la sitúa en la resiliencia: el reglamento europeo DORA sobre resiliencia operativa digital del sector financiero incluye requisitos de gestión del riesgo de TIC y de pruebas de resiliencia, y la guía de planificación de contingencias del NIST trata la elaboración, la prueba y el mantenimiento de los planes. La clase aclara que no se aplican a la plataforma como obligaciones; sirven de marco para ver qué clase de evidencia piden. El paquete de cumplimiento se estructura con estado del requisito, control, prueba, evidencia, fecha, alcance y dueño, y la evidencia es el resultado ejecutable de una prueba, no una captura de pantalla.

## Ejemplo

Requisito: «los datos de entregas se borran a los 365 días». Evidencia: un informe diario generado por la tarea de borrado con el recuento de registros eliminados por día y la fecha de corte, más el resultado de una prueba que crea un registro de 366 días y comprueba que desaparece. No se guardan los registros borrados. Un auditor puede verificar el control sin ver datos personales. (Ilustración del tipo de evidencia de [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md).)

## Errores y confusiones comunes

- **Pedir evidencia después**: se reconstruye a mano y no es fiable.
- **Evidencia con datos personales** que crea otro riesgo.
- **Capturas de pantalla** en lugar de resultados ejecutables.
- **Confundir control con evidencia**: el control actúa; la evidencia lo demuestra.

## Límites y cuándo no aplica

La evidencia demuestra que el control se aplicó en un momento, no que sea suficiente. Su generación tiene un costo que debe ponderarse con la obligación. Si la obligación no aplica a la organización (como DORA para la plataforma del programa), la evidencia es un buen hábito, pero no una exigencia legal.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Artefacto](../a/artefacto.md), [Registro](../r/registro.md), [Resultado](../r/resultado.md), [Amenazas y requisitos de seguridad](../a/amenazas-y-requisitos-de-seguridad.md), [Caos de seguridad](../c/caos-de-seguridad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md), [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md).

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

[↑ Glosario](../../README.md) · [← Evidencia](./evidencia.md) · [Evidencia de ejecución →](./evidencia-de-ejecucion.md)
