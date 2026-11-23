# Tope de solicitudes en curso

[↑ Glosario](../../README.md) · [← Tope de salida](./tope-de-salida.md) · [Tope de vueltas →](./tope-de-vueltas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Límite de solicitudes simultáneas que un proceso acepta; las que exceden reciben 503 y no consumen recursos.

Definición de trabajo de [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md).

## Por qué importa

La clase donde se define, [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), existe con este propósito: la clase existe para que decidas qué trabajo cabe dentro de una solicitud, qué se promete al responder y qué se difiere, y para que puedas medir qué ocurre con esa promesa cuando algo cae a mitad del camino.

## Cómo funciona

Según [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md):

Un servidor de un solo hilo atiende una solicitud a la vez: si cada una tarda 50 ms, 40 clientes simultáneos tardan unos 2 s en total y el último espera casi todo. Un hilo por solicitud reparte la espera pero no pone límite: con mil clientes habría mil hilos disputando memoria y base de datos. Un tope de solicitudes en curso devuelve 503 a las que no caben, lo que protege al proceso y traslada la decisión de reintentar al cliente. Ninguno es «el correcto»: cada uno fija qué se degrada primero.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md):

La plataforma publica el alta de una entrega con este reparto: la frontera HTTP valida el cuerpo y la identidad; una transacción guarda la fila y una fila de outbox; el archivo se escribe antes con un nombre derivado de su huella; la respuesta es 201 con la ubicación del recurso y un campo `estado: recibida`; el análisis de archivo y el correo se encolan.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md)) son:

- **Estudiantes ven «tiempo agotado» pero la entrega existe** — causa: la cadena síncrona termina después de que el cliente se rindió. Corrección: responder tras guardar y encolar; devolver el identificador para consultar el estado.
- **Hay archivos sin fila en el almacenamiento** — causa: el archivo se escribe y el proceso cae antes de insertar la fila. Corrección: escribir el archivo con nombre por huella y limpiar huérfanos con una tarea periódica.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un tope de solicitudes en curso devuelve 503 a las que no caben, lo que protege al proceso y traslada la decisión de reintentar al cliente. ([SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Límite](../l/limite.md), [Proceso](../p/proceso.md), [Recurso](../r/recurso.md), [Backend](../b/backend.md), [Cola larga](../c/cola-larga.md), [Contrato público](../c/contrato-publico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md).

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

[↑ Glosario](../../README.md) · [← Tope de salida](./tope-de-salida.md) · [Tope de vueltas →](./tope-de-vueltas.md)
