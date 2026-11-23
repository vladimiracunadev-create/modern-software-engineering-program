# Reconciliación

[↑ Glosario](../../README.md) · [← Recomposición](./recomposicion.md) · [Reconstrucción de la solución →](./reconstruccion-de-la-solucion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Comparación periódica de dos registros independientes del mismo hecho.

Definición de trabajo de [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md): Comparación periódica entre lo recibido y el listado del proveedor para procesar lo que faltó.
- En [SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md): Comparación periódica del estado real con el deseado y aplicación de la diferencia.
- En [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md): Comparación de dos copias para encontrar y reparar diferencias.
- En [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md): Comparación periódica entre dos fuentes para detectar y reparar diferencias que ninguna restricción impide.

## Por qué importa

En [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), el tema «Reconciliación» importa porque es la única defensa contra lo que ningún mecanismo ve.

En [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md), el tema «Reconciliación» importa porque detecta lo que el diario no pudo saber.

En [SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), el tema «Reconciliación» importa porque el tiempo que una réplica falta depende de cada cuánto mira el controlador.

## Cómo funciona

Según [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), en la sección «Reconciliación»:

Ningún mecanismo es infalible: una lápida olvidada, un conector parado dos días o un esquema que cambió sin aviso dejan divergencias. La **reconciliación** compara periódicamente origen y destino con conteos, sumas de control por rangos o muestras, y reporta las diferencias antes de que las encuentre un usuario. Es también la herramienta de arranque y reparación: cuando se detecta una divergencia, se vuelve a tomar una instantánea del rango afectado. Su costo se acota comparando agregados por rango y descendiendo solo donde difieren.

## Ejemplo

Ejemplo de [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma decide por destino. **Portal de reportes:** consulta una vista del propio origen, sin copia, porque tolera la carga y necesita el valor actual. **Analítica:** captura de cambios sobre el registro de la base con instantánea inicial, carga cruda (ELT) en una zona sin datos de contacto y transformación posterior, con la versión de cada fila como guarda; el flujo se aplica de forma idempotente y se descarta cualquier cambio con versión menor. **Búsqueda de entregas:** los eventos de negocio del outbox de `SE-377`, porque solo le interesan los cambios con significado de negocio.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se pierden avisos tras un mantenimiento** — causa: no hay reconciliación periódica. Corrección: listado desde un punto de control y alerta si no avanza. ([SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md))
- **La reconciliación tarda horas** — causa: compara todo siempre. Corrección: sumas por rangos y bajar solo a los distintos. ([SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **reconciliación** compara periódicamente origen y destino con conteos, sumas de control por rangos o muestras, y reporta las diferencias antes de que las encuentre un usuario. ([SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md))
- La transferencia está lograda cuando puedes decir qué se perdería sin la reconciliación, no cuando el manejador devuelve 200. ([SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md))

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
