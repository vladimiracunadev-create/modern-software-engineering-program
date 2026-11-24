# Partición

[↑ Glosario](../../README.md) · [← Paridad entre entornos](./paridad-entre-entornos.md) · [Partición de red →](./particion-de-red.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

**Partición** es una subdivisión de un conjunto mayor tratada como unidad. El programa la usa con varios sentidos:

- **De una tabla** ([SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md)): un subconjunto, normalmente por fecha, que se escribe y se reescribe como unidad.
- **De un log** ([SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md)): una subdivisión que se lee en orden y se asigna a un solo consumidor de un grupo.
- **De un dominio de entrada** ([SE-060](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md), [SE-062](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md)): un subdominio tratado de forma equivalente por una rama o por una prueba.

## Por qué importa

Particionar permite reprocesar, paralelizar o probar por partes en lugar de tocar todo. En datos, es lo que hace que corregir un error de origen cueste una tarde y no una semana. En mensajería, determina cuánto paralelismo admite un grupo de consumidores. En pruebas, permite cubrir un dominio infinito con un representante por clase.

## Cómo funciona

- **Tablas** ([SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md)): una carga idempotente por partición. Una operación es idempotente si aplicarla varias veces produce el mismo estado que aplicarla una; la propiedad es del trabajo completo, no de cada sentencia: un `INSERT` solo no lo es, y un `DELETE` de la partición seguido de un `INSERT` dentro de una transacción sí lo es. En un lago de datos sin transacciones de fila, reemplazar particiones suele ser la opción realista.
- **Logs** ([SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md)): cada partición se lee en orden y se asigna a un solo consumidor del grupo. Eso garantiza orden dentro de la partición, no entre particiones, y limita el paralelismo al número de particiones.
- **Dominios** ([SE-060](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md), [SE-062](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md)): se parte el espacio de entradas en clases de equivalencia; basta un representante de cada una, más las fronteras.

## Ejemplo

[SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md): el equipo de *Avisos* descubre que su trabajo de lecturas diarias usa `date('now')` y añade filas sin condición. Lo reescribe: recibe la fecha de la partición como parámetro, borra e inserta la partición dentro de una transacción y reprocesa los tres días anteriores para recoger lecturas tardías. Ilustración:

```sql
BEGIN;
DELETE FROM lecturas WHERE dia = :dia;
INSERT INTO lecturas SELECT * FROM staging WHERE dia = :dia;
COMMIT;
```

## Errores y confusiones comunes

- **Un consumidor ocioso y otro saturado.** Causa: pocas particiones o clave popular; corrección: más particiones solo si no es una clave caliente, y revisar la clave ([SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md)).
- **Usar `date('now')` para elegir la partición.** Hace el trabajo no repetible; la fecha debe ser un parámetro ([SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md)).
- **Confundir las particiones de datos con las de dominio.** Comparten el verbo, no el mecanismo.

## Límites y cuándo no aplica

Más particiones no siempre dan más rendimiento: el orden solo se garantiza dentro de cada una, y una clave mal elegida concentra la carga. Reemplazar particiones supone que la unidad de reescritura es la correcta. Y la idempotencia de [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md) se prueba ejecutando dos veces y comparando filas y suma de control, no se asume.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Condición](../c/condicion.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Cortocircuito](../c/cortocircuito.md), [Dominio](../d/dominio.md), [Efecto](../e/efecto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-060 — Proyecto: especificación y solución contrastable](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (43 clases más lo mencionan; las que más):

[SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md), [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md), [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), [SE-368](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md), [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), [SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md), [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Slack](../../../casos/exito/slack.md), [Shopify](../../../casos/exito/shopify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Apache Kafka: documentación](https://kafka.apache.org/documentation/) — particiones, desplazamientos, retención y compactación; autoridad: proyecto Apache Kafka.
- [EIP: Point-to-Point Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html) — canal con un único receptor por mensaje; autoridad: autores del libro.
- [EIP: Publish-Subscribe Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html) — canal que entrega una copia a cada suscriptor; autoridad: autores del libro.
- [EIP: Competing Consumers](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CompetingConsumers.html) — varios consumidores que reparten los mensajes de un canal; autoridad: autores del libro.
- [Amazon SQS: colas estándar](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html) — entrega al menos una vez y orden de mejor esfuerzo; autoridad: Amazon Web Services.

---

[↑ Glosario](../../README.md) · [← Paridad entre entornos](./paridad-entre-entornos.md) · [Partición de red →](./particion-de-red.md)
