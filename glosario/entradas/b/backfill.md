# Backfill

[↑ Glosario](../../README.md) · [← Backend Engineer](./backend-engineer.md) · [Backlog →](./backlog.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Ejecución del trabajo sobre un intervalo pasado.

Definición de trabajo de [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md).

## Por qué importa

En [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), el tema «Backfill» importa porque corrige el pasado sin tocar lo demás.

## Cómo funciona

Según [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md):

Cuando se corrige un dato de origen o un error de transformación, hay que volver a calcular las particiones afectadas. Un backfill es la ejecución del mismo trabajo sobre un intervalo pasado. En el laboratorio, cinco días de origen se corrigieron (+100 en el importe); reescribir esas cinco particiones tocó 248 filas de 1 790 (13,9 %) y dejó la suma igual a la de la fuente corregida. Dos condiciones lo hacen seguro: que el trabajo sea idempotente por partición y que reciba la fecha como parámetro y no la lea del reloj. Un trabajo que usa «hoy» en lugar de la fecha de la partición produce resultados distintos al ejecutarlo en otro momento, y el backfill no reproduce el pasado.

Según [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md):

El equipo de *Avisos* revisa su trabajo de lecturas diarias. Descubre que usa `date('now')` para decidir qué partición carga y que añade filas sin condición. Lo reescribe en tres cambios: recibe la fecha de la partición como parámetro, borra e inserta la partición dentro de una transacción y reprocesa los tres días anteriores en cada ejecución para recoger lecturas tardías. Añade una prueba que ejecuta el trabajo dos veces sobre una partición de ejemplo y compara filas y suma de control. Con esa base, el siguiente error de origen (un campo mal convertido durante cuatro días) se corrige con un backfill de cuatro particiones y los tres marts que dependen de ellas, y la corrección tarda una tarde en lugar de una semana de reconciliaciones manuales.

## Ejemplo

Ejemplo de [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* revisa su trabajo de lecturas diarias. Descubre que usa `date('now')` para decidir qué partición carga y que añade filas sin condición. Lo reescribe en tres cambios: recibe la fecha de la partición como parámetro, borra e inserta la partición dentro de una transacción y reprocesa los tres días anteriores en cada ejecución para recoger lecturas tardías. Añade una prueba que ejecuta el trabajo dos veces sobre una partición de ejemplo y compara filas y suma de control.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un trabajo que usa «hoy» en lugar de la fecha de la partición produce resultados distintos al ejecutarlo en otro momento, y el backfill no reproduce el pasado. ([SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-363](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md), [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Intervalo](../i/intervalo.md), [Sobre](../s/sobre.md), [Trabajo](../t/trabajo.md), [Dato tardío](../d/dato-tardio.md), [Determinismo](../d/determinismo.md), [Fusión por clave](../f/fusion-por-clave.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Backend Engineer](./backend-engineer.md) · [Backlog →](./backlog.md)
