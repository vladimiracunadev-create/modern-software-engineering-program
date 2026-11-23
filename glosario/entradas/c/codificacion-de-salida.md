# Codificación de salida

[↑ Glosario](../../README.md) · [← Codificación](./codificacion.md) · [Codificación de salida por contexto →](./codificacion-de-salida-por-contexto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Transformación de un dato a la sintaxis segura del contexto donde se va a insertar, aplicada al generar la salida.

Definición de trabajo de [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md).

## Por qué importa

La clase donde se define, [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), existe con este propósito: la clase existe para que entiendas por qué una entrada del cliente se convierte en una vulnerabilidad en el momento en que cambia de papel, de dato a código, y para que dejes de defender con filtros lo que se defiende separando los canales.

## Cómo funciona

[SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md):

El equipo inventaría los intérpretes de la plataforma: SQL en doce consultas, HTML en nueve plantillas, el sistema de archivos en dos puntos (adjuntos y exportaciones) y un proceso que convierte documentos a PDF.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md)) son:

- **Se escapan comillas y una consulta numérica sigue vulnerable** — causa: defensa de literal aplicada a un número. Corrección: parámetros enlazados para todos los valores.
- **Una lista de palabras no detiene `' OR 1=1 --`** — causa: la carga no contiene ninguna palabra de la lista. Corrección: separar canales; usar la lista blanca solo para identificadores.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se atacó ninguna aplicación ni servicio reales; las 36 cargas SQL, las 8 de salida, las 12 base y las 7 transformaciones son listas del autor, los contextos de salida son reglas del autor y no un navegador, y la lista de palabras es una elección ilustrativa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](./contextos.md), [Canonicalización](./canonicalizacion.md), [Consulta parametrizada](./consulta-parametrizada.md), [Inyección](../i/inyeccion.md), [Lista blanca](../l/lista-blanca.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), [SE-113](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-113-cli-flags-configuracion-y-codigos-de-salida/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) — codificación de salida por contexto; autoridad: OWASP.
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) — sentencias parametrizadas y listas blancas; autoridad: OWASP.
- [CWE-89](https://cwe.mitre.org/data/definitions/89.html) — inyección SQL; autoridad: MITRE.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — marcadores de posición; autoridad: documentación de Python.
- [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986) — codificación porcentual; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Codificación](./codificacion.md) · [Codificación de salida por contexto →](./codificacion-de-salida-por-contexto.md)
