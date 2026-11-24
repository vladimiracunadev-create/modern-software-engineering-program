# Prueba de carga

[↑ Glosario](../../README.md) · [← Prueba de caracterización](./prueba-de-caracterizacion.md) · [Prueba de contrato →](./prueba-de-contrato.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Una **prueba de carga** aplica la carga esperada (o la prevista para un evento) durante el tiempo suficiente para que el sistema alcance su régimen estable, y comprueba que el escenario de calidad se cumple ([SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md)).

## Por qué importa

Responde «¿cumple en el uso esperado?», pero no responde «¿qué pasa en un pico?» ni «¿qué pasa tras horas de uso?». Confundir los tipos de prueba lleva a declarar «aguanta» y caer en el cierre.

## Cómo funciona

En el simulador de [SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), cuatro servidores con 50 ms de servicio medio tienen una capacidad nominal de 80 solicitudes por segundo. A 60 solicitudes por segundo la utilización es del 75 %, y con llegadas aleatorias eso ya produce colas pasajeras: mediana de 57 ms, p95 de 202 ms y p99 de 285 ms. Por eso se miden percentiles y no solo la media. Otras pruebas responden otras preguntas: la de **pico** el comportamiento ante una ráfaga; la de **resistencia** (*soak*) el desgaste en el tiempo.

## Ejemplo

En la misma clase, a 60 solicitudes por segundo se pierden unas tres conexiones en cinco minutos (6 % del pool); una prueba de carga de esa duración no lo vería, y el pool se agota a los 67 minutos tras 241 135 solicitudes. Solo una prueba de resistencia larga lo detecta.

## Errores y confusiones comunes

**La prueba «aguanta» y el sistema cae en el cierre.** Solo se hizo prueba de carga; añadir prueba de pico y de resistencia.

## Límites y cuándo no aplica

Las cifras son de un simulador. Una prueba de carga con datos o patrones de uso poco realistas da confianza falsa; el generador de carga también puede ser el cuello de botella.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Omisión coordinada](../o/omision-coordinada.md), [Prueba de estrés](./prueba-de-estres.md), [Prueba de pico](./prueba-de-pico.md), [Prueba de resistencia](./prueba-de-resistencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (15 clases más lo mencionan; las que más):

[SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-072](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md), [SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md).

**Aparece en los casos de estudio:** [Shopify](../../../casos/exito/shopify.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [TSB Bank](../../../casos/fallo/tsb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Grafana k6: tipos de pruebas](https://grafana.com/docs/k6/latest/testing-guides/test-types/) — carga, estrés, pico y resistencia; autoridad: documentación de la herramienta.
- [Schroeder, Wierman y Harchol-Balter, «Open versus closed: a cautionary tale»](https://www.usenix.org/legacy/event/nsdi06/tech/full_papers/schroeder/schroeder.pdf) — modelos abierto y cerrado; autoridad: artículo de NSDI 2006.
- [wrk2](https://github.com/giltene/wrk2) — omisión coordinada y su corrección; autoridad: repositorio del autor de la herramienta.
- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — sobrecarga que se amplifica y descarte de trabajo; autoridad: Google, libro de ingeniería de confiabilidad.
- [Python: heapq](https://docs.python.org/3/library/heapq.html) — cola de prioridad usada en el simulador; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Prueba de caracterización](./prueba-de-caracterizacion.md) · [Prueba de contrato →](./prueba-de-contrato.md)
