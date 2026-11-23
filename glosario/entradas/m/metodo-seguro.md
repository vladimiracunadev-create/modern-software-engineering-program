# Método seguro

[↑ Glosario](../../README.md) · [← Método idempotente](./metodo-idempotente.md) · [Métrica →](./metrica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Método que no pretende cambiar el estado del servidor y puede repetirse o precargarse.

Definición de trabajo de [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md): Método cuya semántica solicitada es de solo lectura.

## Por qué importa

La clase donde se define, [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), existe con este propósito: la clase existe para que modeles la plataforma como recursos con identidad y operaciones de semántica conocida, y para que sepas qué garantiza cada método HTTP (seguro, idempotente, cacheable) y qué se rompe cuando un diseño usa un método con otro sentido.

## Cómo funciona

Según [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md):

Resultado: con el borrado como GET, **200 de 200 entregas** quedan borradas; con `DELETE`, **0**, porque un rastreador no emite `DELETE`. La salida es idéntica en Windows y Ubuntu. Es una consecuencia directa de la definición de método seguro: la especificación autoriza a cualquiera a repetir o precargar un GET.

Según [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md):

Reproduce el fallo de la clase: **un GET con efecto lateral ejecutado por un intermediario**. Modela el borrado como GET y deja que un script siga todos los enlaces. **Síntoma:** la lista queda vacía sin que nadie haya pulsado nada. **Hipótesis rivales:** (a) un usuario borró todo; (b) un cliente automático siguió los enlaces. **Prueba:** busca en el registro el agente de usuario y el encabezado `Purpose` o `Sec-Purpose` de la solicitud, y comprueba que las 200 solicitudes llegaron en milisegundos. **Causa:** una operación destructiva expuesta como método seguro. **Corrección:** mover el borrado a `DELETE` y exigir identidad. **Regresión:** una prueba que recorra todos los enlaces de la página y compruebe que el recuento de entregas no cambia.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md):

La plataforma define cinco recursos: la colección `/entregas`, la entrega, la nota, la apelación y el estado de un trabajo. Cada operación del panel se asigna a un método: listar y leer con GET (cacheable con revalidación), crear con POST y respuesta 201, editar con PUT y `If-Match` obligatorio, anular con DELETE y apelar con POST sobre `/entregas/{id}/apelaciones`. La colección pagina por clave (fecha y identificador).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md)) son:

- **Entregas que desaparecen al abrir una página** — causa: una operación destructiva usa GET. Corrección: mover a DELETE y probar con un rastreador.
- **Un docente pierde su cambio sin error** — causa: PUT ciego sobre un recurso editable por varias personas. Corrección: ETag, If-Match y 412 con releer.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se levantó un servidor ni se midió a ninguna persona: los rastreadores, los conflictos y las inserciones son construcciones del autor. La siguiente clase pregunta cuándo REST deja de ser la forma adecuada y qué otros estilos de interfaz existen.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Solo lectura](../s/solo-lectura.md), [Estado](../e/estado.md), [Semántica](../s/semantica.md), [Actualización perdida](../a/actualizacion-perdida.md), [Alcance](../a/alcance.md), [Colección](../c/coleccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — métodos seguros e idempotentes, `ETag`, 412 y 428; autoridad: IETF.
- [HTTP Caching (RFC 9111)](https://www.rfc-editor.org/rfc/rfc9111) — reutilización y revalidación de respuestas cacheadas; autoridad: IETF.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — transacciones y consultas del experimento de paginación; autoridad: Python Software Foundation.
- [SQLite: The Query Planner](https://www.sqlite.org/queryplanner.html) — cómo un índice sirve a una consulta por rango; autoridad: SQLite.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — descripción de recursos y métodos de una API; autoridad: OpenAPI Initiative.

---

[↑ Glosario](../../README.md) · [← Método idempotente](./metodo-idempotente.md) · [Métrica →](./metrica.md)
