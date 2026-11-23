# Trabajo diferido

[↑ Glosario](../../README.md) · [← Trabajo](./trabajo.md) · [Trabajo en curso →](./trabajo-en-curso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Tarea que se acepta ahora y se ejecuta después, fuera de la solicitud que la originó.

Definición de trabajo de [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md).

## Por qué importa

La clase donde se define, [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), existe con este propósito: la clase existe para que decidas qué trabajo cabe dentro de una solicitud, qué se promete al responder y qué se difiere, y para que puedas medir qué ocurre con esa promesa cuando algo cae a mitad del camino.

## Cómo funciona

Según [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md):

Un backend recibe un contrato (la interfaz que otros programas usan) y lo convierte en cambios de estado. Eso implica al menos seis responsabilidades: **contrato** (qué formas de solicitud y respuesta existen), **validación** (rechazar lo que no cumple las precondiciones), **identidad y autorización** (quién pide y qué le corresponde), **estado** (qué se guarda y con qué garantías), **trabajo diferido** (lo que no cabe en la solicitud) y **operación** (cómo se observa, se despliega y se apaga). Nombrarlas importa porque los fallos aparecen en las costuras: una validación hecha solo en la interfaz de usuario se salta llamando a la API; una autorización hecha solo en la pantalla no protege el recurso.

## Ejemplo

Ejemplo de [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) (sección «Caso conductor»):

La plataforma de entregas de tareas es el caso conductor de la [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md). Esta clase deja el primer artefacto: el reparto de responsabilidades del alta y su frontera de confirmación. Las clases siguientes lo concretarán: la interfaz (`SE-242` y `SE-243`), el contrato de errores (`SE-244`), la identidad (`SE-245`), los reintentos (`SE-246`), el trabajo diferido (`SE-247`), los archivos (`SE-248`), la protección (`SE-249`) y la operación (`SE-250`). Cambia después una sola decisión, mover el análisis de archivo al lado diferido, y revisa qué artefactos hay que tocar.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md)) son:

- **Estudiantes ven «tiempo agotado» pero la entrega existe** — causa: la cadena síncrona termina después de que el cliente se rindió. Corrección: responder tras guardar y encolar; devolver el identificador para consultar el estado.
- **Hay archivos sin fila en el almacenamiento** — causa: el archivo se escribe y el proceso cae antes de insertar la fila. Corrección: escribir el archivo con nombre por huella y limpiar huérfanos con una tarea periódica.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **contrato** (qué formas de solicitud y respuesta existen), **validación** (rechazar lo que no cumple las precondiciones), **identidad y autorización** (quién pide y qué le corresponde), **estado** (qué se guarda y con qué garantías), **trabajo diferido** (lo que no cabe en la solicitud) y **operación** (cómo se observa, se despliega y se apaga). ([SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tarea](./tarea.md), [Backend](../b/backend.md), [Cola larga](../c/cola-larga.md), [Contrato público](../c/contrato-publico.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md), [Frontera de confirmación](../f/frontera-de-confirmacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md), [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — significado de 201, 202 y 503 y de los métodos HTTP; autoridad: IETF.
- [Dean y Barroso, «The tail at scale» (CACM, 2013)](https://doi.org/10.1145/2408776.2408794) — latencia de servicios compuestos y cola larga; autoridad: Communications of the ACM.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — transacciones, `with` y revertir; autoridad: Python Software Foundation.
- [Python: http.server](https://docs.python.org/3/library/http.server.html) — servidores HTTP de laboratorio; autoridad: Python Software Foundation.
- [Python: threading](https://docs.python.org/3/library/threading.html) — hilos y semáforos del experimento de capacidad; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Trabajo](./trabajo.md) · [Trabajo en curso →](./trabajo-en-curso.md)
