# Lista blanca

[↑ Glosario](../../README.md) · [← Liquidez](./liquidez.md) · [Lista de escenarios →](./lista-de-escenarios.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Conjunto finito de valores o formas permitidas que se compara con la entrada, en lugar de enumerar lo prohibido.

Definición de trabajo de [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md).

## Por qué importa

En [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), el tema «SQL: parámetros, escape e identificadores» importa porque el parámetro cierra valores; los nombres exigen una lista blanca.

## Cómo funciona

Según [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md):

Un intérprete (el motor SQL, el navegador, el sistema de archivos, un shell) distingue entre **datos** y **órdenes** por la sintaxis. Si el programa construye una orden pegando texto, la sintaxis del dato puede cerrar el dato y empezar una orden. La cadena `' OR 1=1 --` no es peligrosa en sí: lo es porque, pegada dentro de `WHERE titulo LIKE '%…%'`, las comillas cierran el literal, `OR 1=1` añade una condición siempre verdadera y `--` anula el resto. El principio que lo evita es el mismo en todos los intérpretes: **mantener los canales separados**.

Según [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md):

El equipo inventaría los intérpretes de la plataforma: SQL en doce consultas, HTML en nueve plantillas, el sistema de archivos en dos puntos (adjuntos y exportaciones) y un proceso que convierte documentos a PDF. Sustituye cada concatenación de SQL por parámetros enlazados a través de una capa de acceso a datos, define una lista blanca para columnas de orden y sentido, activa el autoescape de la plantilla y revisa los tres lugares donde se desactivaba, valida las URL de los enlaces con una lista de esquemas, resuelve las rutas y comprueba el prefijo de la raíz, y llama al conversor con una lista de argumentos y sin shell.

## Ejemplo

Ejemplo de [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md) (sección «Ejemplo profesional»):

El equipo inventaría los intérpretes de la plataforma: SQL en doce consultas, HTML en nueve plantillas, el sistema de archivos en dos puntos (adjuntos y exportaciones) y un proceso que convierte documentos a PDF. Sustituye cada concatenación de SQL por parámetros enlazados a través de una capa de acceso a datos, define una lista blanca para columnas de orden y sentido, activa el autoescape de la plantilla y revisa los tres lugares donde se desactivaba, valida las URL de los enlaces con una lista de esquemas, resuelve las rutas y comprueba el prefijo de la raíz, y llama al conversor con una lista de argumentos y sin shell.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una lista de palabras no detiene `' OR 1=1 --`** — causa: la carga no contiene ninguna palabra de la lista. Corrección: separar canales; usar la lista blanca solo para identificadores. ([SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md))
- **El orden de resultados acepta cualquier cosa** — causa: nombre de columna del cliente concatenado. Corrección: lista blanca de columnas y sentido definidos por la aplicación. ([SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cuando no existe un canal separado (el nombre de una columna en `ORDER BY`), se usa una **lista blanca** con valores de la aplicación, nunca del cliente. ([SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Valor](../v/valor.md), [Canonicalización](../c/canonicalizacion.md), [Codificación de salida](../c/codificacion-de-salida.md), [Consulta parametrizada](../c/consulta-parametrizada.md), [Inyección](../i/inyeccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md), [SE-467](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) — sentencias parametrizadas y listas blancas; autoridad: OWASP.
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) — codificación de salida por contexto; autoridad: OWASP.
- [CWE-89](https://cwe.mitre.org/data/definitions/89.html) — inyección SQL; autoridad: MITRE.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — marcadores de posición; autoridad: documentación de Python.
- [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986) — codificación porcentual; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Liquidez](./liquidez.md) · [Lista de escenarios →](./lista-de-escenarios.md)
