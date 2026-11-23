# Revisión

[↑ Glosario](../../README.md) · [← Reversión automática](./reversion-automatica.md) · [Revisión de la política →](./revision-de-la-politica.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Una política de capacidad es una apuesta sobre el futuro del tráfico. Cuando el patrón cambia, por una nueva universidad cliente o un cambio de calendario, la política se vuelve incorrecta sin que nada falle. Por eso se escribe con su señal de revisión: qué métrica la reabre y cada cuánto se mira.

Explicación de la sección «Revisión» de [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md).

## Por qué importa

En [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), el tema «Revisión» importa porque el patrón cambia y la decisión caduca.

En [SE-012 — Proyecto: mapa profesional y contrato personal de aprendizaje](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md), el tema «Revisión» importa porque ¿qué señal cambia la ruta?

## Cómo funciona

Según [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), en la sección «Revisión»:

Una política de capacidad es una apuesta sobre el futuro del tráfico. Cuando el patrón cambia, por una nueva universidad cliente o un cambio de calendario, la política se vuelve incorrecta sin que nada falle. Por eso se escribe con su señal de revisión: qué métrica la reabre y cada cuánto se mira.

## Ejemplo

Ejemplo de [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma describe la demanda de siete días con mínimo, mediana, percentil 99 y máximo, y concluye que 12 instancias cubren el día normal y 30 el peor pico. Elige una política programada con una base de 7 instancias, una subida programada para las horas del cierre y un margen reactivo con objetivo de utilización del 60 % y arranque de 2 minutos, y mide con su propio tráfico cuánta demanda pierde en los picos aleatorios. Para las notificaciones, que toleran retraso, usa una cola en lugar de instancias.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La política se vuelve incorrecta sin avisar** — causa: el patrón de tráfico cambió. Corrección: señal de revisión sobre la mediana y los picos. ([SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md))
- **completar un curso es criterio de salida** — causa: consumo confundido con desempeño. Corrección: exige tarea, evidencia y revisión externa. ([SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un artefacto demuestra más cuando conserva propósito, contexto, alternativas, método, resultado, revisión y límite. ([SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md))
- **Corrección:** reduce el trabajo en curso a uno, dos o tres experimentos; ordena por dependencia (qué habilita qué) y por riesgo; y exige para cada uno un artefacto, un criterio de salida y una revisión. ([SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Brecha](../b/brecha.md), [Competencia](../c/competencia.md), [Compromiso de capacidad](../c/compromiso-de-capacidad.md), [Criterio de salida](../c/criterio-de-salida.md), [Escalado programado](../e/escalado-programado.md), [Escalado reactivo](../e/escalado-reactivo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-012 — Proyecto: mapa profesional y contrato personal de aprendizaje](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (376 clases más lo mencionan; las que más):

[SE-539](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md), [SE-564](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), [SE-586](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md), [SE-529](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-529-liderazgo-tecnico-sin-autoridad-formal/README.md), [SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md), [SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Slack](../../../casos/exito/slack.md), [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Kubernetes: Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) — cálculo de réplicas y ventanas de estabilización; autoridad: documentación oficial de Kubernetes.
- [Little (1961), A Proof for the Queuing Formula: L = λW](https://doi.org/10.1287/opre.9.3.383) — relación entre llegadas, tiempo y elementos en el sistema; autoridad: artículo original (Operations Research, 9(3)).
- [Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/) — capacidad y sobrecarga como ingeniería; autoridad: libro de Google publicado en línea.
- [FinOps Framework](https://www.finops.org/framework/) — optimización de tarifas y compromisos; autoridad: FinOps Foundation.
- [Python: random](https://docs.python.org/3/library/random.html) — generador usado en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Reversión automática](./reversion-automatica.md) · [Revisión de la política →](./revision-de-la-politica.md)
