# Transacción

[↑ Glosario](../../README.md) · [← Trampa de foco](./trampa-de-foco.md) · [Transacción única →](./transaccion-unica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Conjunto de operaciones que se aplican enteras o no se aplican, y que se observan según el nivel de aislamiento.

Definición de trabajo de [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md): Grupo de escrituras que se confirman o se descartan juntas y que, en una base transaccional, deja siempre un estado completo.
- En [SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md): Conjunto de cambios tratado como una unidad según garantías del gestor.

## Por qué importa

En [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), el tema «Transacción» importa porque evita cargas a medias.

## Cómo funciona

Según [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md):

Una operación es idempotente si aplicarla varias veces produce el mismo estado que aplicarla una. En datos, la prueba es operativa: ejecuta el trabajo, anota el resultado (filas y suma de control), ejecútalo otra vez con la misma entrada y compara. Si cambia, no es idempotente. Es una propiedad del trabajo completo y no de cada sentencia: un `INSERT` solo no lo es, y un `DELETE` de la partición seguido de un `INSERT` dentro de una transacción sí lo es.

Según [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md):

El equipo de *Avisos* revisa su trabajo de lecturas diarias. Descubre que usa `date('now')` para decidir qué partición carga y que añade filas sin condición. Lo reescribe en tres cambios: recibe la fecha de la partición como parámetro, borra e inserta la partición dentro de una transacción y reprocesa los tres días anteriores en cada ejecución para recoger lecturas tardías. Añade una prueba que ejecuta el trabajo dos veces sobre una partición de ejemplo y compara filas y suma de control. Con esa base, el siguiente error de origen (un campo mal convertido durante cuatro días) se corrige con un backfill de cuatro particiones y los tres marts que dependen de ellas, y la corrección tarda una tarde en lugar de una semana de reconciliaciones manuales.

## Ejemplo

Ejemplo de [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* revisa su trabajo de lecturas diarias. Descubre que usa `date('now')` para decidir qué partición carga y que añade filas sin condición. Lo reescribe en tres cambios: recibe la fecha de la partición como parámetro, borra e inserta la partición dentro de una transacción y reprocesa los tres días anteriores en cada ejecución para recoger lecturas tardías. Añade una prueba que ejecuta el trabajo dos veces sobre una partición de ejemplo y compara filas y suma de control.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una transferencia cortada deja cupos perdidos** — causa: sentencias confirmadas por separado. Corrección: envolver los pasos en una transacción e idempotencia. ([SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md))
- **Guardar un borrador tarda segundos con muchas ediciones** — causa: una transacción por edición con sincronización completa. Corrección: agrupar escrituras y elegir un modo de sincronización explícito. ([SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Es una propiedad del trabajo completo y no de cada sentencia: un `INSERT` solo no lo es, y un `DELETE` de la partición seguido de un `INSERT` dentro de una transacción sí lo es. ([SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md))
- En un lago sin transacciones de fila, reemplazar particiones suele ser la opción realista. ([SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Aislamiento](../a/aislamiento.md), [Base](../b/base.md), [Conjunto](../c/conjunto.md), [Estado](../e/estado.md), [Alcance](../a/alcance.md), [Dependencia](../d/dependencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (61 clases más lo mencionan; las que más):

[SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), [SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md), [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [PostgreSQL: aislamiento de transacciones](https://www.postgresql.org/docs/current/transaction-iso.html) — niveles y anomalías; autoridad: documentación oficial de PostgreSQL.
- [SQLite: transacciones](https://www.sqlite.org/lang_transaction.html) — `BEGIN` diferido e inmediato; autoridad: documentación oficial de SQLite.
- [SQLite, «Atomic Commit In SQLite»](https://www.sqlite.org/atomiccommit.html) — mecanismo de transacciones atómicas y sus supuestos; autoridad: SQLite.
- [SQLite: aislamiento](https://www.sqlite.org/isolation.html) — comportamiento entre conexiones; autoridad: documentación oficial de SQLite.
- [Berenson et al., «A Critique of ANSI SQL Isolation Levels»](https://arxiv.org/abs/cs/0701157) — anomalías no cubiertas por el estándar; autoridad: artículo de los autores.

---

[↑ Glosario](../../README.md) · [← Trampa de foco](./trampa-de-foco.md) · [Transacción única →](./transaccion-unica.md)
