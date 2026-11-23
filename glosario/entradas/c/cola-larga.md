# Cola larga

[↑ Glosario](../../README.md) · [← Cola justa](./cola-justa.md) · [Cola y disciplina fifo →](./cola-y-disciplina-fifo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Porción de las solicitudes más lentas de una distribución, que domina el tiempo que perciben los clientes en servicios compuestos.

Definición de trabajo de [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md): Distribución donde una fracción pequeña de observaciones es mucho mayor que la mediana.

## Por qué importa

En [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), el tema «Frontera síncrona y diferida» importa porque todo paso que está antes de la respuesta suma su latencia y su cola larga al tiempo que ve el cliente.

## Cómo funciona

Según [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md):

Traslada el experimento a otro de los dominios persistentes (por ejemplo, un servicio de pedidos que cobra, reserva existencias y envía un aviso): cambia los pasos y conserva el procedimiento de enumerar los puntos de caída y medir la cola larga. La transferencia está lograda cuando explicas qué parte dependía del alta de entregas y cuál es el patrón general, no cuando el código se parece.

Según [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md):

La latencia de una llamada a un modelo no es un número sino una distribución con **cola larga**: la mayoría responde en torno a la mediana y una fracción tarda mucho más. En la simulación (log-normal con mediana de 1,2 s más 0,2 s de herramienta), una llamada tiene mediana 1,40 s, p95 3,50 s y p99 5,11 s. Encadenar llamadas suma: cinco llamadas dan mediana 7,90 s, p95 12,05 s y p99 14,48 s; ocho, mediana 12,74 s y p95 17,97 s. El p95 crece más despacio que la mediana relativa porque las colas se promedian entre llamadas, pero el tiempo absoluto que espera el 5 % más desafortunado supera los 12 segundos con cinco pasos.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md):

La plataforma publica el alta de una entrega con este reparto: la frontera HTTP valida el cuerpo y la identidad; una transacción guarda la fila y una fila de outbox; el archivo se escribe antes con un nombre derivado de su huella; la respuesta es 201 con la ubicación del recurso y un campo `estado: recibida`; el análisis de archivo y el correo se encolan.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md)) son:

- **Estudiantes ven «tiempo agotado» pero la entrega existe** — causa: la cadena síncrona termina después de que el cliente se rindió. Corrección: responder tras guardar y encolar; devolver el identificador para consultar el estado.
- **Hay archivos sin fila en el almacenamiento** — causa: el archivo se escribe y el proceso cae antes de insertar la fila. Corrección: escribir el archivo con nombre por huella y limpiar huérfanos con una tarea periódica.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La latencia de una llamada a un modelo no es un número sino una distribución con **cola larga**: la mayoría responde en torno a la mediana y una fracción tarda mucho más. ([SE-598](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Observación](../o/observacion.md), [Servicio](../s/servicio.md), [Backend](../b/backend.md), [Caché de prefijo](./cache-de-prefijo.md), [Contrato público](./contrato-publico.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (35 clases más lo mencionan; las que más):

[SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md), [SE-415](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md), [SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md), [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md), [SE-533](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Dean y Barroso, «The tail at scale» (CACM, 2013)](https://doi.org/10.1145/2408776.2408794) — latencia de servicios compuestos y cola larga; autoridad: Communications of the ACM.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — significado de 201, 202 y 503 y de los métodos HTTP; autoridad: IETF.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — transacciones, `with` y revertir; autoridad: Python Software Foundation.
- [Python: http.server](https://docs.python.org/3/library/http.server.html) — servidores HTTP de laboratorio; autoridad: Python Software Foundation.
- [Python: threading](https://docs.python.org/3/library/threading.html) — hilos y semáforos del experimento de capacidad; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Cola justa](./cola-justa.md) · [Cola y disciplina fifo →](./cola-y-disciplina-fifo.md)
