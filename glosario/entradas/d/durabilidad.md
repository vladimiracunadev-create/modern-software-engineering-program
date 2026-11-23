# Durabilidad

[↑ Glosario](../../README.md) · [← Duplicación de conocimiento](./duplicacion-de-conocimiento.md) · [Duración inclusiva →](./duracion-inclusiva.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Probabilidad de no perder un dato durante un periodo.

Definición de trabajo de [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md): Propiedad de que una escritura confirmada sobreviva a una caída; su coste crece con la frecuencia con que se fuerza la sincronización con el almacenamiento.

## Por qué importa

En [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), el tema «Durabilidad» importa porque el tiempo de reparación pesa más que el número de copias.

En [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md), el tema «Durabilidad» importa porque sin diario y clave hay duplicados.

## Cómo funciona

Según [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), en la sección «Durabilidad»:

La **durabilidad** es la probabilidad de no perder un dato en un periodo, y no coincide con la disponibilidad: un sistema puede estar caído una hora y no perder nada, o estar siempre disponible y perder el 0,01 % de los datos al año. Con N réplicas independientes que fallan con una tasa anual λ y se reparan en R horas, se pierde el objeto cuando fallan todas durante la ventana de reparación. La aproximación de primer orden es 8 760 · N · (λ/8 760)ᴺ · Rᴺ⁻¹: crece con el cubo de la tasa para tres réplicas, pero también con el cuadrado del tiempo de reparación.

## Ejemplo

Ejemplo de [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) (sección «Ejemplo profesional»):

El equipo escribe el presupuesto de fiabilidad de la plataforma. Para disponibilidad prometen el 99,5 % mensual en el horario de entregas (unos 3,6 horas de caída al mes) y lo desglosan: web 99,95 %, aplicación 99,9 %, base de datos 99,9 %, con una causa común declarada de despliegue: cuatro al año, con un procedimiento de reversión en diez minutos como mitigación. Para durabilidad, tres réplicas en dominios de fallo distintos y un tiempo de reparación objetivo de 24 h, con una prueba mensual que restaura una copia en un entorno aparte.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md)) son:

- **El sistema cae más de lo que da la cuenta** — causa: fallos en serie ignorados o causa común. Corrección: calcular con todas las capas y listar lo que comparten las réplicas.
- **Duplicar un componente no mejora nada** — causa: la limitación está en otra capa. Corrección: mejorar el eslabón más débil de la serie.

Según [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md): **Punto profesional.** La clase existe para que distingas tres promesas que se confunden bajo la palabra «fiable»: que el servicio responda (disponibilidad), que los datos no se pierdan (durabilidad) y que, si algo se rompe, se vuelva a un estado conocido en un tiempo y con una pérdida acotados (recuperación).

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **durabilidad** es la probabilidad de no perder un dato en un periodo, y no coincide con la disponibilidad: un sistema puede estar caído una hora y no perder nada, o estar siempre disponible y perder el 0,01 % de los datos al año. ([SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Fuerza](../f/fuerza.md), [Propiedad](../p/propiedad.md), [Causa común](../c/causa-comun.md), [Disponibilidad](./disponibilidad.md), [Escritura atómica](../e/escritura-atomica.md), [Fusión](../f/fusion.md).
- **Se confunde con:** **Punto profesional.** La clase existe para que distingas tres promesas que se confunden bajo la palabra «fiable»: que el servicio responda (disponibilidad), que los datos no se pierdan (durabilidad) y que, si algo se rompe, se vuelva a un estado conocido en un tiempo y con una pérdida acotados (recuperación).

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (13 clases más lo mencionan; las que más):

[SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md), [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md), [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

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

[↑ Glosario](../../README.md) · [← Duplicación de conocimiento](./duplicacion-de-conocimiento.md) · [Duración inclusiva →](./duracion-inclusiva.md)
