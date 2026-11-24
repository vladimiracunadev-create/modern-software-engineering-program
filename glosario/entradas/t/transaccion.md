# Transacción

[↑ Glosario](../../README.md) · [← Trampa de foco](./trampa-de-foco.md) · [Transacción única →](./transaccion-unica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Una **transacción** es un conjunto de operaciones que se aplican enteras o no se aplican, y que se observan según el nivel de aislamiento ([SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md)). [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md) la formula como un grupo de escrituras que se confirman o se descartan juntas y que, en una base transaccional, deja siempre un estado completo; [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md) la usa para un conjunto de cambios tratado como unidad según las garantías del gestor (por ejemplo, de paquetes).

## Por qué importa

Sin transacciones, una falla a mitad de camino deja datos a medias: una transferencia cortada puede descontar de un lado y no acreditar del otro. La transacción delimita qué es «un cambio» para la base y permite razonar sobre el sistema en términos de antes y después. Cambia dónde se escriben los límites de una operación de negocio.

## Cómo funciona

El modelo clásico (ACID) combina cuatro garantías: **atomicidad** (todo o nada), **consistencia** (se respetan las reglas), **aislamiento** (cómo se ven entre sí las transacciones concurrentes) y **durabilidad** (lo confirmado sobrevive). [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) destaca que el aislamiento tiene niveles: cuanto más débil, más anomalías observables. El mecanismo típico es un registro de escritura previa: la base anota los cambios antes de aplicarlos y, ante una caída, rehace o deshace según corresponda.

Costos concretos ([SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md)): una transacción por cada edición con sincronización completa a disco hace que guardar un borrador tarde segundos con muchas ediciones; la solución es agrupar escrituras y elegir un modo de sincronización explícito.

Atomicidad no es idempotencia: [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md) muestra que un `INSERT` solo no es idempotente, pero un `DELETE` de la partición seguido de un `INSERT` dentro de una transacción sí lo es; la propiedad es del trabajo completo, no de cada sentencia.

## Ejemplo

```sql
BEGIN;
UPDATE cupos SET libres = libres - 1 WHERE curso = 'SE-101' AND libres > 0;
INSERT INTO matriculas(curso, estudiante) VALUES ('SE-101', 42);
COMMIT;      -- o ROLLBACK si falla cualquiera de los dos pasos
```

## Errores y confusiones comunes

- **Una transferencia cortada deja cupos perdidos.** Causa: sentencias confirmadas por separado; corrección: envolver los pasos en una transacción e idempotencia ([SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md)).
- **Guardar un borrador tarda segundos con muchas ediciones.** Causa: una transacción por edición con sincronización completa; corrección: agrupar escrituras y elegir un modo de sincronización explícito ([SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md)).
- **Suponer transacciones entre servicios.** Una operación que cruza servicios deja de ser atómica; se necesita una saga.

## Límites y cuándo no aplica

En un lago de datos sin transacciones de fila, reemplazar particiones suele ser la opción realista ([SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md)). Un aislamiento fuerte cuesta rendimiento y puede provocar esperas o reintentos; elegir el nivel es una decisión por operación. Y una transacción no protege efectos fuera de la base (correos enviados, llamadas externas): esos requieren compensación o idempotencia.

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
