# Potencia

[↑ Glosario](../../README.md) · [← Postura del dispositivo](./postura-del-dispositivo.md) · [Potencia estadística →](./potencia-estadistica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

La **potencia** (estadística) es la probabilidad de detectar un efecto real ([SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md)). El programa la formula con el mismo núcleo en varias clases: la probabilidad de que un experimento refute una hipótesis falsa con el efecto y la ventana dados ([SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md)), de que un contraste detecte un efecto real de un tamaño dado ([SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md)), de detectar una mejora real ([SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md)) o de detectarlo con un procedimiento y un tamaño de muestra dados ([SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md)). Es la otra cara del error de no detectar.

## Por qué importa

Un resultado «sin efecto» solo significa algo si el experimento podía haberlo visto. Sin potencia, «no se encontró nada» es compatible con «no se podía encontrar». [SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md) lo traduce a decisiones: no confirmar una hipótesis con 2 % de potencia, y escribir el efecto mínimo detectable junto con la conclusión.

## Cómo funciona

La potencia depende del tamaño del efecto, de la variabilidad, del tamaño de muestra o ventana y del umbral de decisión. Aumentarla cuesta datos o tiempo. [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md) muestra el compromiso con una regla sobre discordancias: se cuentan las tareas en que solo una de dos versiones acierta; con *b* tareas en que solo B acierta y *c* en que solo A, se declara mejor a B si (*b* − *c*)/√(*b* + *c*) supera 1,96. Comparar el harness contra sí mismo declara «mejora» 2,1 %, 3,0 % y 3,0 % de las veces, cerca del 2,5 % de una prueba de una cola al 95 %. Esa regla controla el error de falsas mejoras y cobra su precio: la potencia, porque exige diferencias mayores para declararlas.

En despliegue ([SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md)), el canario que dice «sin errores» puede carecer de tráfico suficiente para ver el cambio: hay que calcular la potencia y exigir un tráfico mínimo.

## Ejemplo

[SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md): un umbral de SLO parece detectar más (53 % con 5 s), pero lo consigue porque el indicador sano (96,5 %) ya está pegado al umbral (96 %) y refuta ventanas sanas con frecuencia: su «potencia» incluye las falsas alarmas. Moraleja: potencia sin tasa de falsas alarmas engaña. Ilustración de simulación:

```python
detecta = sum(prueba(simular(efecto=0.05, n=200)) for _ in range(5000)) / 5000
```

## Errores y confusiones comunes

- **La hipótesis nunca se refuta.** Causa: potencia baja (ventana corta o efecto pequeño); corrección: ampliar la ventana o repetir y declarar el efecto mínimo detectable ([SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md)).
- **Confirmar con 2 % de potencia.** Causa: no se calculó lo que el experimento podía ver ([SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md)).
- **El canario sin errores y producción que falla.** Causa: tráfico insuficiente; corrección: calcular la potencia ([SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md)).

## Límites y cuándo no aplica

Las cifras son de simulaciones de las clases con datos sintéticos. La potencia se calcula para un efecto supuesto: si el efecto real es menor, la potencia real también. Y una potencia alta no valida el procedimiento por sí sola: hay que controlar también el error de falsa alarma.

## Relación con otros conceptos

- **Prerrequisito:** [Hipótesis](../h/hipotesis.md).
- **Ver también:** [Efecto](../e/efecto.md), [Ventana](../v/ventana.md), [Benchmark](../b/benchmark.md), [Capacidad de mejora](../c/capacidad-de-mejora.md), [Cuello de botella](../c/cuello-de-botella.md), [Intervención sobre el sistema](../i/intervencion-sobre-el-sistema.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-022 — Rendimiento, consumo energético y límites físicos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-190 — Retrospectivas y mejora del sistema de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.
- [SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.
- [SE-585 — Observabilidad y evals del propio harness](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.
- [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.
- [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (24 clases más lo mencionan; las que más):

[SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md), [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md), [SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md), [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md), [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md).

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

[↑ Glosario](../../README.md) · [← Postura del dispositivo](./postura-del-dispositivo.md) · [Potencia estadística →](./potencia-estadistica.md)
