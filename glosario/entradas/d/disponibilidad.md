# Disponibilidad

[↑ Glosario](../../README.md) · [← Dispersión](./dispersion.md) · [Disponibilidad compuesta →](./disponibilidad-compuesta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Fracción del tiempo en que un sistema cumple su función, igual a MTBF/(MTBF + MTTR) para un componente.

Definición de trabajo de [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md).

## Por qué importa

En [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), el tema «Disponibilidad y su aritmética» importa porque convierte un porcentaje en minutos y muestra qué capa manda.

## Cómo funciona

Según [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md):

La **disponibilidad** de un componente es la fracción del tiempo en que funciona: MTBF/(MTBF + MTTR), donde MTBF es el tiempo medio entre fallos y MTTR el tiempo medio de reparación. Con un MTBF de 500 h y un MTTR de 0,5 h resulta 0,999. Para pasar de un porcentaje a minutos: el 99 % deja 5 256 minutos de caída al año, el 99,9 % deja 526, el 99,99 % deja 52,6 y el 99,999 % deja 5,3. La composición importa más que cada cifra. En **serie** (la solicitud necesita web, aplicación y base de datos) las disponibilidades se multiplican: 0,999³ = 0,997, tres veces peor que cada una.

Según [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md):

El equipo escribe el presupuesto de fiabilidad de la plataforma. Para disponibilidad prometen el 99,5 % mensual en el horario de entregas (unos 3,6 horas de caída al mes) y lo desglosan: web 99,95 %, aplicación 99,9 %, base de datos 99,9 %, con una causa común declarada de despliegue: cuatro al año, con un procedimiento de reversión en diez minutos como mitigación. Para durabilidad, tres réplicas en dominios de fallo distintos y un tiempo de reparación objetivo de 24 h, con una prueba mensual que restaura una copia en un entorno aparte.

## Ejemplo

Ejemplo de [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la disponibilidad de tres capas en serie. Antes de ejecutarlo, predice si supera el 99,8 %.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md)) son:

- **El sistema cae más de lo que da la cuenta** — causa: fallos en serie ignorados o causa común. Corrección: calcular con todas las capas y listar lo que comparten las réplicas.
- **Duplicar un componente no mejora nada** — causa: la limitación está en otra capa. Corrección: mejorar el eslabón más débil de la serie.

Según [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md): **Punto profesional.** La clase existe para que distingas tres promesas que se confunden bajo la palabra «fiable»: que el servicio responda (disponibilidad), que los datos no se pierdan (durabilidad) y que, si algo se rompe, se vuelva a un estado conocido en un tiempo y con una pérdida acotados (recuperación).

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Además, la redundancia solo beneficia a la capa donde se aplica: duplicar la aplicación no mejora la disponibilidad de la base de datos. ([SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md))
- **una réplica que no mejora la disponibilidad porque comparte la causa del fallo**. ([SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md))

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
