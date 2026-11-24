# Reconciliación

[↑ Glosario](../../README.md) · [← Recomposición](./recomposicion.md) · [Reconstrucción de la solución →](./reconstruccion-de-la-solucion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

La **reconciliación** es la comparación periódica de dos registros independientes del mismo hecho, para detectar y reparar sus diferencias ([SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md)). El programa la usa con matices:

- En [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) y [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md) (datos): comparación periódica entre dos fuentes para detectar y reparar diferencias que ninguna restricción impide.
- En [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md) (integración): comparación periódica entre lo recibido y el listado del proveedor para procesar lo que faltó.
- En [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md) (CI/CD): comparación periódica del estado real con el deseado y aplicación de la diferencia.
- En [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md) (modernización): comparación de dos copias para encontrar y reparar diferencias.

No debe confundirse con la conciliación contable de [SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md) (otra entrada), aunque comparten la idea de contrastar fuentes.

## Por qué importa

Ningún mecanismo de sincronización es infalible: un evento perdido, un conector parado dos días o un esquema que cambió sin aviso dejan divergencias silenciosas. La decisión que cambia es no confiar solo en el flujo en tiempo real: se añade una verificación periódica que encuentre lo que falló antes que un usuario.

## Cómo funciona

[SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) explica el mecanismo: una lápida olvidada, un conector parado o un cambio de esquema dejan divergencias. La reconciliación **compara periódicamente origen y destino** con conteos, sumas de control por rangos o muestras, y reporta las diferencias. Es también la herramienta de arranque y reparación: al detectar una divergencia, se vuelve a tomar una instantánea del rango afectado.

Su costo se acota comparando **agregados por rango** y descendiendo solo donde difieren ([SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md)): si la suma del rango coincide, no hace falta mirar sus filas; si difiere, se parte el rango y se repite. Así la reconciliación que tardaba horas porque comparaba todo siempre pasa a comparar solo lo distinto.

En integración ([SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md)), recibir webhooks no basta: pueden perderse. Se compara periódicamente lo recibido con el listado del proveedor, desde un punto de control, y se alerta si el avance se detiene. En despliegue ([SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md)), la reconciliación continua del estado real contra el deseado es el principio de los controladores declarativos.

## Ejemplo

Un servicio recibe eventos de pago por webhook. Tras un mantenimiento, el endpoint estuvo caído y se perdieron algunos. Cada hora, un trabajo lista los pagos del proveedor desde el último punto de control, compara con lo recibido y procesa lo que faltó. Si el punto de control no avanza, genera una alerta. Mecanismo de [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md).

## Errores y confusiones comunes

- **Se pierden avisos tras un mantenimiento**: no hay reconciliación periódica; se corrige con listado desde un punto de control y alerta si no avanza.
- **La reconciliación tarda horas**: compara todo siempre; se corrige con sumas por rangos y descendiendo solo a los distintos.
- **Confundirla con reintentar**: reintentar repara fallos conocidos; reconciliar encuentra los desconocidos.
- **Reconciliar sin decidir cuál fuente manda**.

## Límites y cuándo no aplica

Detecta divergencias con un retraso igual a su periodo: no sustituye la consistencia en tiempo real. Requiere dos fuentes realmente independientes y una clave común para compararlas; si ambas comparten el error, no lo ve. Y la reparación automática exige criterio claro sobre qué fuente es la verdad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Hecho](../h/hecho.md), [Registro](./registro.md), [Restricciones](./restricciones.md), [Captura de cambios](../c/captura-de-cambios.md), [Clave foránea](../c/clave-foranea.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.
- [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.
- [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (16 clases más lo mencionan; las que más):

[SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md), [SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md), [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md), [SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [TSB Bank](../../../casos/fallo/tsb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [PostgreSQL: decodificación lógica](https://www.postgresql.org/docs/current/logicaldecoding.html) — extracción de cambios desde el registro de escritura anticipada; autoridad: documentación oficial de PostgreSQL.
- [Debezium: conector de PostgreSQL](https://debezium.io/documentation/reference/stable/connectors/postgresql.html) — instantánea y flujo de cambios con entrega al menos una vez; autoridad: proyecto Debezium.
- [SQLite: CREATE TRIGGER](https://www.sqlite.org/lang_createtrigger.html) — disparadores en la misma transacción; autoridad: documentación oficial de SQLite.
- [Microsoft: ETL y ELT](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl) — transformar antes o después de cargar; autoridad: documentación de Microsoft.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — captura de cambios y sistemas derivados; autoridad: autor del libro.

---

[↑ Glosario](../../README.md) · [← Recomposición](./recomposicion.md) · [Reconstrucción de la solución →](./reconstruccion-de-la-solucion.md)
