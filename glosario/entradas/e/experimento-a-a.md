# Experimento A/A

[↑ Glosario](../../README.md) · [← Expediente de release](./expediente-de-release.md) · [Experimento concentrado →](./experimento-concentrado.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Medición con el sistema sano para estimar el ruido y las falsas refutaciones de una regla.

Definición de trabajo de [SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md).

## Por qué importa

La clase donde se define, [SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md), existe con este propósito: la clase existe para que conviertas «el sistema aguanta» en una afirmación que pueda salir falsa: un **estado estable** medido como salida del sistema, con su ruido natural, y una **hipótesis** que diga qué se mantendrá y con qué banda cuando se inyecte una falla.

## Cómo funciona

Según [SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md):

Una **regla de refutación** decide, a partir de una ventana, si la hipótesis queda refutada. Se evalúa antes con un **experimento A/A**: se aplica la regla a ventanas de un sistema sano y se cuenta cuántas refuta. Una regla que refuta ventanas sanas produce falsas alarmas y destruye la confianza en el método. Se comparan tres reglas: «menor que la media» (cualquier caída), «menor que la media menos tres desviaciones» (la banda) y «menor que el SLO de 96 %» (el objetivo del servicio).

Según [SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md):

Supón, como caso hipotético y no como medición, que el equipo reescribe su hipótesis: «con 100 ms más de lentitud en el 5 % de las llamadas al almacenamiento durante diez minutos, la proporción de entregas aceptadas en menos de 400 ms de los grupos experimental y de control diferirá menos de 1,5 puntos en cada ventana de 60 s». Agrega la métrica de negocio (entregas confirmadas por minuto) como segunda salida, tres métricas técnicas solo para vigilar (p99, errores, profundidad de la cola), una línea base de dos semanas de martes y un experimento A/A previo con el mismo grupo repartido al azar, para verificar que la regla no refuta en el sistema sano.

## Ejemplo

Ejemplo de [SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético y no como medición, que el equipo reescribe su hipótesis: «con 100 ms más de lentitud en el 5 % de las llamadas al almacenamiento durante diez minutos, la proporción de entregas aceptadas en menos de 400 ms de los grupos experimental y de control diferirá menos de 1,5 puntos en cada ventana de 60 s».

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md)) son:

- **La hipótesis se refuta con el sistema sano** — causa: regla sin banda. Corrección: medir la línea base y usar media menos tres desviaciones.
- **La hipótesis nunca se refuta** — causa: potencia baja: ventana corta o efecto pequeño. Corrección: ampliar la ventana o repetir y declarar el efecto mínimo detectable.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se evalúa antes con un **experimento A/A**: se aplica la regla a ventanas de un sistema sano y se cuenta cuántas refuta. ([SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medición](../m/medicion.md), [Regla](../r/regla.md), [Ruido](../r/ruido.md), [Banda](../b/banda.md), [Estado estable](./estado-estable.md), [Grupo de control](../g/grupo-de-control.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Principles of Chaos Engineering](https://principlesofchaos.org/) — estado estable, hipótesis y salida medible; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Netflix: «Chaos Engineering Upgraded»](https://netflixtechblog.com/chaos-engineering-upgraded-878d341f15fa) — ejemplo de experimento con estado estable, hipótesis y grupo de control; autoridad: blog de ingeniería de Netflix.
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — indicadores, ventanas y percentiles; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — presupuesto de error; autoridad: libro de ingeniería de confiabilidad de Google.
- [Python: statistics](https://docs.python.org/3/library/statistics.html) — desviación típica usada en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Expediente de release](./expediente-de-release.md) · [Experimento concentrado →](./experimento-concentrado.md)
