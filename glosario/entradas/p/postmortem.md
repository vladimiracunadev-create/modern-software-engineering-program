# Postmortem

[↑ Glosario](../../README.md) · [← Postcondición](./postcondicion.md) · [Postmortem sin culpa →](./postmortem-sin-culpa.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Documento que reconstruye un incidente para aprender de él y cambiar el sistema.

Definición de trabajo de [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md).

## Por qué importa

En [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md), el tema «Postmortem sin culpa» importa porque la culpa esconde información y desincentiva el reporte.

## Cómo funciona

Según [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md):

Un **postmortem** (o revisión posterior al incidente) es el documento que reconstruye un incidente para aprender de él. **Sin culpa** significa que el análisis parte de que cada persona actuó con la mejor información y las herramientas disponibles, y se pregunta por qué esa acción tenía sentido en ese momento, qué señales faltaban y qué lo hacía fácil de equivocar. No elimina la responsabilidad: la desplaza del individuo al sistema que dejó un camino fácil hacia el fallo. La razón es práctica: si nombrar una acción propia tiene consecuencias personales, la información se esconde, y sin información el análisis es mentira. El **sesgo de retrospectiva** refuerza el problema: quien conoce el desenlace lo ve como previsible.

Según [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo escribe el postmortem del incidente del certificado con esta estructura. Resumen: entregas rechazadas durante 47 minutos por un certificado vencido. Impacto: 1 240 entregas rechazadas, 12 % de las peticiones en la franja, 4 instituciones afectadas, 31 % del presupuesto de error de 28 días. Línea de tiempo con horas: 14:02 vence el certificado, 14:09 salta la alerta de consumo, 14:21 se identifica la causa, 14:49 se instala el certificado nuevo. Factores: renovación manual, alerta de vencimiento silenciada por fatiga (`SE-498`), runbook sin mención, propietario ausente, sin verificación posterior al despliegue. Lo que funcionó: la alerta de consumo detectó en 7 minutos y el escalamiento llegó a la segunda persona en 4.

## Ejemplo

Ejemplo de [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo escribe el postmortem del incidente del certificado con esta estructura. Resumen: entregas rechazadas durante 47 minutos por un certificado vencido. Impacto: 1 240 entregas rechazadas, 12 % de las peticiones en la franja, 4 instituciones afectadas, 31 % del presupuesto de error de 28 días. Línea de tiempo con horas: 14:02 vence el certificado, 14:09 salta la alerta de consumo, 14:21 se identifica la causa, 14:49 se instala el certificado nuevo. Factores: renovación manual, alerta de vencimiento silenciada por fatiga (`SE-498`), runbook sin mención, propietario ausente, sin verificación posterior al despliegue.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El postmortem culpa a una persona** — causa: análisis detenido en «error humano». Corrección: preguntar por qué la acción tenía sentido y qué lo facilitó. ([SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** el postmortem base, la lista de ocho expresiones de culpa y los nueve operadores son construcciones del autor, y el verificador se afinó con las mismas mutaciones que lo evalúan. ([SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md))
- **cerrar un postmortem con «error humano» como causa y una acción sin dueño**. ([SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Incidente](../i/incidente.md).
- **Ver también:** [Documento](../d/documento.md), [Acción correctiva verificable](../a/accion-correctiva-verificable.md), [Factor contribuyente](../f/factor-contribuyente.md), [Postmortem sin culpa](./postmortem-sin-culpa.md), [Sesgo de retrospectiva](../s/sesgo-de-retrospectiva.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md), [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md).

**Aparece en los casos de estudio:** [Slack](../../../casos/exito/slack.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) — práctica sin culpa; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE Workbook: Postmortem Culture](https://sre.google/workbook/postmortem-culture/) — adopción y errores comunes; autoridad: Google, SRE Workbook.
- [GitLab, postmortem de la interrupción de la base de datos del 31 de enero de 2017](https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/) — ejemplo público de postmortem; autoridad: publicación de la propia organización.
- [Cook, «How Complex Systems Fail»](https://how.complexsystems.fail/) — múltiples causas contribuyentes; autoridad: texto del autor, Richard I. Cook.
- [Fischhoff, «Hindsight ≠ foresight»](https://doi.org/10.1037/0096-1523.1.3.288) — sesgo de retrospectiva; autoridad: Journal of Experimental Psychology, 1975.

---

[↑ Glosario](../../README.md) · [← Postcondición](./postcondicion.md) · [Postmortem sin culpa →](./postmortem-sin-culpa.md)
