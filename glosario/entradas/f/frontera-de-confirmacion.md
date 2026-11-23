# Frontera de confirmación

[↑ Glosario](../../README.md) · [← Frontera de confianza](./frontera-de-confianza.md) · [Frontera de equipo →](./frontera-de-equipo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Punto de la secuencia de una solicitud a partir del cual lo anterior se cuenta como hecho y lo posterior como intención.

Definición de trabajo de [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md).

## Por qué importa

La clase donde se define, [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), existe con este propósito: la clase existe para que decidas qué trabajo cabe dentro de una solicitud, qué se promete al responder y qué se difiere, y para que puedas medir qué ocurre con esa promesa cuando algo cae a mitad del camino.

## Cómo funciona

[SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Ejemplo de [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) (sección «Caso conductor»):

La plataforma de entregas de tareas es el caso conductor de la [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md). Esta clase deja el primer artefacto: el reparto de responsabilidades del alta y su frontera de confirmación. Las clases siguientes lo concretarán: la interfaz (`SE-242` y `SE-243`), el contrato de errores (`SE-244`), la identidad (`SE-245`), los reintentos (`SE-246`), el trabajo diferido (`SE-247`), los archivos (`SE-248`), la protección (`SE-249`) y la operación (`SE-250`). Cambia después una sola decisión, mover el análisis de archivo al lado diferido, y revisa qué artefactos hay que tocar.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md)) son:

- **Estudiantes ven «tiempo agotado» pero la entrega existe** — causa: la cadena síncrona termina después de que el cliente se rindió. Corrección: responder tras guardar y encolar; devolver el identificador para consultar el estado.
- **Hay archivos sin fila en el almacenamiento** — causa: el archivo se escribe y el proceso cae antes de insertar la fila. Corrección: escribir el archivo con nombre por huella y limpiar huérfanos con una tarea periódica.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): dos simulaciones idénticas en ambos sistemas y una medición de servidores locales con tiempos propios de cada equipo. No se midió ningún servicio real, proveedor de correo ni a personas: las latencias y las proporciones de fallo son construcciones del autor. La siguiente clase pregunta cómo se nombran y se tratan los recursos que esta frontera expone.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Hecho](../h/hecho.md), [Intención](../i/intencion.md), [Secuencia](../s/secuencia.md), [Backend](../b/backend.md), [Cola larga](../c/cola-larga.md), [Contrato público](../c/contrato-publico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

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

[↑ Glosario](../../README.md) · [← Frontera de confianza](./frontera-de-confianza.md) · [Frontera de equipo →](./frontera-de-equipo.md)
