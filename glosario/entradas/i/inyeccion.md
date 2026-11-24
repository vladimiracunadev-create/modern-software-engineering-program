# Inyección

[↑ Glosario](../../README.md) · [← Invitado](./invitado.md) · [Inyección de comandos →](./inyeccion-de-comandos.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

La **inyección** es una vulnerabilidad en la que datos controlados por quien ataca se interpretan como instrucciones por un intérprete que los recibe junto con ellas ([SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md)). Los ejemplos clásicos son SQL, órdenes del sistema y plantillas.

## Por qué importa

Es una de las clases de vulnerabilidad más repetidas y su causa es de diseño, no de descuido: mezclar datos e instrucciones en el mismo canal. La defensa efectiva no depende de recordar escapar cada caso.

## Cómo funciona

Si una consulta se construye concatenando texto del usuario, el intérprete no sabe dónde terminan las instrucciones del programador y dónde empiezan los datos. La carga `' OR 1=1 --` cierra el literal y añade lógica propia. La defensa correcta **separa los canales**: parámetros enlazados, de modo que el valor viaja aparte y nunca se interpreta como sintaxis. Una lista blanca se reserva para identificadores (nombres de columnas) que no pueden parametrizarse.

## Ejemplo

```python
# vulnerable
cur.execute("SELECT * FROM notas WHERE id = " + entrada)
# seguro
cur.execute("SELECT * FROM notas WHERE id = ?", (entrada,))
```

## Errores y confusiones comunes

- **Se escapan comillas y una consulta numérica sigue vulnerable.** La defensa de literal no sirve para un número; usar parámetros enlazados para todos los valores ([SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md)).
- **Una lista de palabras no detiene `' OR 1=1 --`.** La carga no contiene ninguna palabra de la lista; separar canales.

## Límites y cuándo no aplica

Los parámetros enlazados protegen los *valores*, no los identificadores ni las estructuras de la consulta. El mismo principio se extiende a otros intérpretes (órdenes, plantillas, instrucciones a modelos), donde separar datos de instrucciones es más difícil.

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
