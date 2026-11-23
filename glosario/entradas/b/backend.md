# Backend

[↑ Glosario](../../README.md) · [← Autoservicio](../a/autoservicio.md) · [Backend Engineer →](./backend-engineer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Parte del sistema que recibe solicitudes de otros programas, aplica reglas y modifica estado persistente.

Definición de trabajo de [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md).

## Por qué importa

En [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), el tema «Responsabilidades del backend» importa porque si no se nombra quién valida, quién identifica y quién persiste, esas tareas se duplican o se omiten entre capas.

## Cómo funciona

Según [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md):

Un backend recibe un contrato (la interfaz que otros programas usan) y lo convierte en cambios de estado. Eso implica al menos seis responsabilidades: **contrato** (qué formas de solicitud y respuesta existen), **validación** (rechazar lo que no cumple las precondiciones), **identidad y autorización** (quién pide y qué le corresponde), **estado** (qué se guarda y con qué garantías), **trabajo diferido** (lo que no cabe en la solicitud) y **operación** (cómo se observa, se despliega y se apaga). Nombrarlas importa porque los fallos aparecen en las costuras: una validación hecha solo en la interfaz de usuario se salta llamando a la API; una autorización hecha solo en la pantalla no protege el recurso.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md):

La plataforma publica el alta de una entrega con este reparto: la frontera HTTP valida el cuerpo y la identidad; una transacción guarda la fila y una fila de outbox; el archivo se escribe antes con un nombre derivado de su huella; la respuesta es 201 con la ubicación del recurso y un campo `estado: recibida`; el análisis de archivo y el correo se encolan.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md)) son:

- **Estudiantes ven «tiempo agotado» pero la entrega existe** — causa: la cadena síncrona termina después de que el cliente se rindió. Corrección: responder tras guardar y encolar; devolver el identificador para consultar el estado.
- **Hay archivos sin fila en el almacenamiento** — causa: el archivo se escribe y el proceso cae antes de insertar la fila. Corrección: escribir el archivo con nombre por huella y limpiar huérfanos con una tarea periódica.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): dos simulaciones idénticas en ambos sistemas y una medición de servidores locales con tiempos propios de cada equipo. No se midió ningún servicio real, proveedor de correo ni a personas: las latencias y las proporciones de fallo son construcciones del autor. La siguiente clase pregunta cómo se nombran y se tratan los recursos que esta frontera expone.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Regla](../r/regla.md), [Cola larga](../c/cola-larga.md), [Contrato público](../c/contrato-publico.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md), [Frontera de confirmación](../f/frontera-de-confirmacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (18 clases más lo mencionan; las que más):

[SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md), [SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md), [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), [SE-112](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-112-paquetes-modulos-y-publicacion/README.md), [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-072](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md), [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Slack](../../../casos/exito/slack.md).

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

[↑ Glosario](../../README.md) · [← Autoservicio](../a/autoservicio.md) · [Backend Engineer →](./backend-engineer.md)
