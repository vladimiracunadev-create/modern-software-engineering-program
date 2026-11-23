# Inyección

[↑ Glosario](../../README.md) · [← Invitado](./invitado.md) · [Inyección de comandos →](./inyeccion-de-comandos.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Vulnerabilidad en la que datos controlados por quien ataca se interpretan como instrucciones por un intérprete que los recibe junto con ellas.

Definición de trabajo de [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md).

## Por qué importa

En [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), el tema «La inyección como cambio de papel» importa porque explica por qué los filtros fallan y la separación de canales no.

## Cómo funciona

Según [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md):

La misma estructura se repite: una ruta que viene del cliente es dato hasta que el sistema de archivos la resuelve (`..`, enlaces simbólicos, separadores distintos en Windows y POSIX); la defensa es resolver y comprobar el prefijo (la clase `SE-467` la reutiliza). Un comando armado como texto y pasado a un shell es la inyección de orden por excelencia; la defensa es no usar shell, pasar una lista de argumentos y validar los argumentos contra la forma esperada. Una plantilla del servidor que incluye datos del cliente puede ejecutar expresiones; una consulta a un directorio de usuarios y un documento XML con entidades externas son otros intérpretes. La pregunta es siempre la misma: ¿qué programa recibe este valor y qué sintaxis tiene?

Según [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md):

Sí, por otra razón. La validación de forma (longitud, rango, formato) reduce errores y abuso, y es una capa más; no es la defensa contra la inyección, que es la separación de canales. Mezclar ambas ideas es lo que lleva a confiar en un filtro.

## Ejemplo

Ejemplo de [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md) (sección «Preguntas frecuentes»):

Sí, por otra razón. La validación de forma (longitud, rango, formato) reduce errores y abuso, y es una capa más; no es la defensa contra la inyección, que es la separación de canales. Mezclar ambas ideas es lo que lleva a confiar en un filtro.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md)) son:

- **Se escapan comillas y una consulta numérica sigue vulnerable** — causa: defensa de literal aplicada a un número. Corrección: parámetros enlazados para todos los valores.
- **Una lista de palabras no detiene `' OR 1=1 --`** — causa: la carga no contiene ninguna palabra de la lista. Corrección: separar canales; usar la lista blanca solo para identificadores.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un comando armado como texto y pasado a un shell es la inyección de orden por excelencia; la defensa es no usar shell, pasar una lista de argumentos y validar los argumentos contra la forma esperada. ([SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Instrucción](./instruccion.md), [Vulnerabilidad](../v/vulnerabilidad.md), [Canonicalización](../c/canonicalizacion.md), [Codificación de salida](../c/codificacion-de-salida.md), [Consulta parametrizada](../c/consulta-parametrizada.md), [Lista blanca](../l/lista-blanca.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (61 clases más lo mencionan; las que más):

[SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), [SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md), [SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md), [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [CWE-89](https://cwe.mitre.org/data/definitions/89.html) — inyección SQL; autoridad: MITRE.
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) — sentencias parametrizadas y listas blancas; autoridad: OWASP.
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) — codificación de salida por contexto; autoridad: OWASP.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — marcadores de posición; autoridad: documentación de Python.
- [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986) — codificación porcentual; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Invitado](./invitado.md) · [Inyección de comandos →](./inyeccion-de-comandos.md)
