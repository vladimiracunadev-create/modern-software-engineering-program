# Inyección de fallas

[↑ Glosario](../../README.md) · [← Inyección de dependencias](./inyeccion-de-dependencias.md) · [Inyección de fallos →](./inyeccion-de-fallos.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

La **inyección de fallas** es introducir a propósito una falla controlada para comprobar que el sistema la detecta y se recupera ([SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md)). [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) la usa en el sentido más concreto de provocar caídas, duplicados, retrasos y mensajes inválidos para comprobar las invariantes de un flujo. Es la técnica de base de la ingeniería del caos.

## Por qué importa

Un diseño que *declara* resiliencia (hay tiempos de espera, reintentos y cortacircuitos) no es lo mismo que una resiliencia *demostrada*, el comportamiento observado cuando alguien provocó la falla. La decisión que cambia es cómo se gana confianza: no por la lectura del diseño, sino por haber visto al sistema fallar y recuperarse en condiciones controladas.

## Cómo funciona

El mecanismo es el de un experimento: se define qué se espera (el estado estable o las invariantes), se provoca una falla acotada y se observa si lo esperado se mantiene. En [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), las fallas provocadas son caídas del consumidor, duplicados, retrasos y mensajes inválidos; lo que se comprueba son las cinco invariantes del flujo (una calificación por entrega, un aviso como máximo, etc.). Si una invariante se viola, se sabe qué mecanismo falta.

[SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) fija las precondiciones. Ensayar con inyección de fallas en un sistema que **no tiene aún monitores ni runbook** produce un incidente en lugar de un ensayo: primero el diseño y las pruebas por separado. Y en producción real las fallas necesitan **límites**: un segmento, una fracción, una hora acordada, y un acuerdo previo con quien está de guardia. Esos límites son los mismos que usa la ingeniería del caos: alcance acotado, grupo de control, condición de aborto.

La clase además es honesta con su alcance: el taller usa un modelo y datos sintéticos en una máquina de escritorio, y no sustituye un ensayo de recuperación completo con la infraestructura real ([SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md)).

## Ejemplo

Un equipo quiere comprobar que un mensaje inválido no detiene el flujo. Inyecta un mensaje mal formado entre mil válidos y observa: los demás se procesan y el inválido termina en la cola de mensajes fallidos, visible y con alarma. Si el flujo se detuviera, la prueba habría revelado la falta de esa cola. Escenario basado en [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md).

## Errores y confusiones comunes

- **Inyectar sin monitores ni runbook**: produce un incidente real en vez de un ensayo ([SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md)).
- **Inyectar sin límites** en producción: segmento, fracción y hora acordada son parte del diseño.
- **Confundirla con una prueba de carga**: busca fallos, no capacidad.
- **Considerar el ensayo sintético un ensayo de recuperación completo**.

## Límites y cuándo no aplica

No se hace en sistemas que no pueden ya observarse ni recuperarse, ni sin permiso de quienes operan. Un ensayo con modelo sintético demuestra la lógica del diseño, no el comportamiento de la infraestructura real. Y lo que se prueba es solo lo que se inyectó: una recuperación comprobada para una falla no implica que lo sea para otra.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Invariante](./invariante.md), [Recuperación](../r/recuperacion.md), [Cola de mensajes fallidos](../c/cola-de-mensajes-fallidos.md), [Exposición](../e/exposicion.md), [Falla inyectada](../f/falla-inyectada.md), [Horizonte de reintentos](../h/horizonte-de-reintentos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), [SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS Builders' Library: timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — retroceso exponencial y aleatoriedad; autoridad: Amazon Web Services.
- [Amazon SQS: colas de mensajes fallidos](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) — apartar mensajes que no se pueden procesar; autoridad: Amazon Web Services.
- [microservices.io: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html) — outbox y relevo; autoridad: Chris Richardson, autor del catálogo.
- [EIP: Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html) — canal de mensajes no procesables; autoridad: autores del libro.
- [Google SRE: addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/) — reintentos y fallos en cascada; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Inyección de dependencias](./inyeccion-de-dependencias.md) · [Inyección de fallos →](./inyeccion-de-fallos.md)
