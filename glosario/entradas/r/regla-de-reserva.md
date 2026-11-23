# Regla de reserva

[↑ Glosario](../../README.md) · [← Regla de permisos](./regla-de-permisos.md) · [Regla de tres →](./regla-de-tres.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Respuesta alternativa, más simple que el modelo, que se sirve cuando las entradas no son confiables.

Definición de trabajo de [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md).

## Por qué importa

La clase donde se define, [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), existe con este propósito: la clase existe para que apliques el método a los sistemas donde la falla más dañina **no hace ruido**: bases de datos y colas que pierden o duplican datos sin lanzar un error, réplicas que sirven lecturas viejas y modelos de aprendizaje automático que siguen respondiendo, solo que peor.

## Cómo funciona

Según [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md):

Se simula un modelo logístico de seis características entrenado sobre 3 000 ejemplos sintéticos (exactitud de 80,2 % sobre 4 000 de prueba), con una **regla de reserva** de dos características que un equipo escribiría a mano (exactitud de 73,6 %, frente a 51,1 % del azar informado). Se afecta una fracción de las peticiones cuyas dos características más informativas llegan de tres formas: con un **valor por omisión** (cero), con un **valor obsoleto** (de otra petición) o se sirve la respuesta de la **regla de reserva** en lugar del modelo.

Según [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md):

Supón, como caso hipotético y no como medición, que el equipo del almacenamiento escribe tres experimentos de datos. El primero mata el primario en preproducción con una carga sintética de 200 escrituras por segundo y compara el registro de confirmaciones del cliente con la réplica promovida; la hipótesis es «se pierden menos de 5 escrituras» y la señal, el conteo diferencial. El segundo inyecta 100 ms de retraso en la réplica y comprueba que el flujo «subir y recargar» muestra la entrega propia en el 99,9 % de los casos. El tercero apaga el almacén de características del modelo de revisión prioritaria durante 10 minutos y comprueba que la tasa de uso de valores por omisión alerta en menos de 2 minutos y que se activa la regla de reserva.

## Ejemplo

Ejemplo de [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético y no como medición, que el equipo del almacenamiento escribe tres experimentos de datos. El primero mata el primario en preproducción con una carga sintética de 200 escrituras por segundo y compara el registro de confirmaciones del cliente con la réplica promovida; la hipótesis es «se pierden menos de 5 escrituras» y la señal, el conteo diferencial. El segundo inyecta 100 ms de retraso en la réplica y comprueba que el flujo «subir y recargar» muestra la entrega propia en el 99,9 % de los casos.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md)) son:

- **Escrituras confirmadas desaparecen tras una conmutación** — causa: replicación asíncrona con RPO declarado de cero. Corrección: medir la pérdida y elegir replicación semisíncrona o ajustar el RPO.
- **Una persona no ve lo que acaba de subir** — causa: lectura desde una réplica atrasada. Corrección: leer del primario tras escribir o devolver el estado en la escritura.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se simula un modelo logístico de seis características entrenado sobre 3 000 ejemplos sintéticos (exactitud de 80,2 % sobre 4 000 de prueba), con una **regla de reserva** de dos características que un equipo escribiría a mano (exactitud de 73,6 %, frente a 51,1 % del azar informado). ([SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Almacén de características](../a/almacen-de-caracteristicas.md), [Escritura confirmada perdida](../e/escritura-confirmada-perdida.md), [Lectura obsoleta](../l/lectura-obsoleta.md), [Replicación asíncrona](./replicacion-asincrona.md), [Retraso de replicación](./retraso-de-replicacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Jepsen](https://jepsen.io/) — análisis de seguridad de sistemas distribuidos de datos; autoridad: proyecto de investigación Jepsen.
- [Sculley et al., Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — riesgos propios de los sistemas de ML; autoridad: artículo de NIPS 2015.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — variar eventos reales y medir la salida; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Google SRE: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — pruebas de recuperación e integridad de datos; autoridad: libro de ingeniería de confiabilidad de Google.
- [Python: random](https://docs.python.org/3/library/random.html) — generador con semilla usado en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Regla de permisos](./regla-de-permisos.md) · [Regla de tres →](./regla-de-tres.md)
