# Disponibilidad

[↑ Glosario](../../README.md) · [← Dispersión](./dispersion.md) · [Disponibilidad compuesta →](./disponibilidad-compuesta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

La **disponibilidad** es la fracción del tiempo en que un sistema cumple su función; para un componente es MTBF / (MTBF + MTTR), con MTBF el tiempo medio entre fallos y MTTR el tiempo medio de reparación ([SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md)).

## Por qué importa

[SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) existe para distinguir tres promesas que se confunden bajo la palabra «fiable»: que el servicio responda (disponibilidad), que los datos no se pierdan (durabilidad) y que, si algo se rompe, se vuelva a un estado conocido en un tiempo y con una pérdida acotados (recuperación). Mezclarlas lleva a medir una y prometer otra.

## Cómo funciona

Mejorar la disponibilidad se logra alargando el MTBF o acortando el MTTR; acortar la reparación suele ser más barato. En arquitecturas con varias capas, las capas en **serie** multiplican sus disponibilidades (la cadena es más débil que su eslabón más débil) y las réplicas en **paralelo** la mejoran, pero solo si fallan de forma independiente. Una causa común (el mismo despliegue, la misma zona) anula el beneficio.

## Ejemplo

Un componente con MTBF de 999 horas y MTTR de 1 hora tiene 999/1000 = 99,9 %. Si cinco capas en serie tienen cada una 99,9 %, la cadena ronda el 99,5 %. (Cálculo ilustrativo de la fórmula de la clase.)

## Errores y confusiones comunes

- **El sistema cae más de lo que da la cuenta.** Fallos en serie ignorados o causa común; calcular con todas las capas y listar lo que comparten las réplicas.
- **Duplicar un componente no mejora nada.** La limitación está en otra capa; mejorar el eslabón más débil.

## Límites y cuándo no aplica

La fórmula supone fallos y reparaciones independientes y estadísticamente estables; no describe degradaciones parciales (lentitud) ni pérdida de datos. Para esas, el SLI debe medir buenos eventos, no tiempo en pie.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Función](../f/funcion.md), [Causa común](../c/causa-comun.md), [Durabilidad](./durabilidad.md), [Objetivo de punto de recuperación](../o/objetivo-de-punto-de-recuperacion.md), [RTO](../r/rto.md).
- **Se confunde con:** **Punto profesional.** La clase existe para que distingas tres promesas que se confunden bajo la palabra «fiable»: que el servicio responda (disponibilidad), que los datos no se pierdan (durabilidad) y que, si algo se rompe, se vuelva a un estado conocido en un tiempo y con una pérdida acotados (recuperación).

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (75 clases más lo mencionan; las que más):

[SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-535](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — disponibilidad como objetivo con costo y presupuesto de error; autoridad: Google, libro de ingeniería de confiabilidad.
- [Ford et al., «Availability in globally distributed storage systems»](https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Ford.pdf) — fallos correlacionados en almacenamiento; autoridad: OSDI 2010.
- [Schroeder y Gibson, «Disk failures in the real world»](https://www.usenix.org/legacy/events/fast07/tech/schroeder.html) — tasas de fallo de discos en campo; autoridad: FAST 2007.
- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) — planes de contingencia y objetivos de recuperación; autoridad: NIST.
- [Chen, Toueg y Aguilera, «On the quality of service of failure detectors»](https://doi.org/10.1109/12.980014) — métricas de detectores de fallos; autoridad: IEEE Transactions on Computers, 2002.

---

[↑ Glosario](../../README.md) · [← Dispersión](./dispersion.md) · [Disponibilidad compuesta →](./disponibilidad-compuesta.md)
