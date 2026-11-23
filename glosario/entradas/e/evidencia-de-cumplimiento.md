# Evidencia de cumplimiento

[↑ Glosario](../../README.md) · [← Evidencia](./evidencia.md) · [Evidencia de ejecución →](./evidencia-de-ejecucion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Artefactos fechados que sostienen una afirmación de que se cumple una obligación.

Definición de trabajo de [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md): Registro verificable de un procedimiento de prueba, su criterio y su resultado.

## Por qué importa

En [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), el tema «Evidencia de cumplimiento» importa porque una afirmación de cumplimiento vale lo que la evidencia que la sostiene.

En [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md), el tema «Evidencia de cumplimiento» importa porque un tercero debe poder comprobar el resultado.

## Cómo funciona

Según [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), en la sección «Evidencia de cumplimiento»:

Cumplir es una afirmación; la evidencia es lo que la sostiene: la configuración vigente, el resultado fechado de una prueba, el registro del borrado. Una auditoría pregunta por ambas. La evidencia debe poder generarse sin intervención heroica y sin exponer datos personales: por ejemplo, el recuento de registros borrados por día, no los registros. Un requisito sin una forma de generar su evidencia cumplida es un requisito que no se puede defender.

Según [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md), en la sección «Evidencia de cumplimiento»:

Una norma o un auditor no pide que el sistema sea seguro: pide **evidencia** de que los controles funcionan. El reglamento europeo DORA sobre resiliencia operativa digital del sector financiero, por ejemplo, incluye requisitos de gestión del riesgo de TIC y de pruebas de resiliencia, y la guía de planificación de contingencias del NIST trata la elaboración, la prueba y el mantenimiento de los planes. No se aplican a la plataforma educativa del caso, pero ilustran la forma: lo que se exige es un procedimiento de prueba repetible y un registro.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md):

La obligación de limitar la conservación del borrador, trazada hasta su evidencia:

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md)) son:

- **Se borraron datos bajo retención legal** — causa: la regla ignoró una excepción. Corrección: incluir las excepciones en el requisito y en las pruebas.
- **Una auditoría pide evidencia del borrado y no hay** — causa: no se diseñó cómo generarla. Corrección: definir la evidencia junto con el requisito, sin guardar contenido.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-152 — Requisitos regulatorios, de datos y seguridad](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se interpretó ninguna norma para un caso real, no es asesoría legal, el diagrama y las retenciones son ejemplos del autor y la cadena de hashes no incluye claves ni sellado de tiempo. La siguiente clase protege el conjunto de requisitos con líneas base y control de cambios.

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
