# Escalamiento

[↑ Glosario](../../README.md) · [← Escalado reactivo](./escalado-reactivo.md) · [Escalar →](./escalar.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Paso de una página al siguiente nivel de respuesta cuando el anterior no contesta a tiempo.

Definición de trabajo de [SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-529 — Liderazgo técnico sin autoridad formal](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-529-liderazgo-tecnico-sin-autoridad-formal/README.md): Llevar una decisión a quien tiene autoridad sobre ella, con el problema, las opciones y sus costos.
- En [SE-005 — Roles, especialidades y colaboración interdisciplinaria](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md): Traslado explícito a autoridad capaz de decidir.

## Por qué importa

En [SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md), el tema «Escalamiento» importa porque un nivel solo cubre un fallo; la causa común cubre varios.

## Cómo funciona

Según [SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md), en la sección «Escalamiento»:

El **escalamiento** define qué ocurre si la persona de guardia no responde. Cada nivel tiene un tiempo máximo (cinco minutos es habitual para el reconocimiento) tras el cual la página pasa al siguiente: guardia primaria, secundaria, responsable. La probabilidad de que alguien conteste mejora de manera notable con niveles independientes: con 85 % de respuesta por nivel y fallos independientes, tres niveles atienden el 99,8 % de las páginas en 15 minutos, frente al 84,8 % de un solo nivel.

## Ejemplo

Ejemplo de [SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo reescribe el runbook de `EntregasConsumoRapido` con el formato anterior, lo añade al repositorio junto al código del servicio y escribe un verificador que se ejecuta en la integración continua (campos, comandos con salida esperada, reversión de lo destructivo, fecha menor de 90 días y alerta existente en el catálogo). Cada trimestre una persona que no escribió el runbook lo ejecuta en el entorno de pruebas, con un despliegue defectuoso inyectado, y anota qué paso falló o confundió.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md)) son:

- **El runbook dice «revisa los servicios»** — causa: pasos sin comando ni salida esperada. Corrección: un paso por acción, con comando y resultado esperado.
- **La guardia es siempre la misma persona** — causa: equipo pequeño o ausencias sin plan. Corrección: calcular la carga y ampliar la rotación o reducir el alcance.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **escalamiento** define qué ocurre si la persona de guardia no responde. ([SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md), [SE-004](../../../classes/part-00-ingenieria-de-software-como-profesion/se-004-etica-interes-publico-y-consecuencias-de-las-decisiones-tecnicas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](../c/costo.md), [Opción](../o/opcion.md), [Página](../p/pagina.md), [Problemas](../p/problemas.md), [Causa común](../c/causa-comun.md), [Ejercicio de runbook](./ejercicio-de-runbook.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-005 — Roles, especialidades y colaboración interdisciplinaria](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.
- [SE-529 — Liderazgo técnico sin autoridad formal](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-529-liderazgo-tecnico-sin-autoridad-formal/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-511](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md), [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), [SE-004](../../../classes/part-00-ingenieria-de-software-como-profesion/se-004-etica-interes-publico-y-consecuencias-de-las-decisiones-tecnicas/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-534](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md), [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Being On-Call](https://sre.google/sre-book/being-on-call/) — carga y tamaño de la guardia; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE Workbook: On-Call](https://sre.google/workbook/on-call/) — medir y mejorar la guardia; autoridad: Google, SRE Workbook.
- [PagerDuty Incident Response](https://response.pagerduty.com/) — procesos públicos de guardia y respuesta; autoridad: documentación pública de PagerDuty.
- [Google SRE: Practical Alerting](https://sre.google/sre-book/practical-alerting/) — alertas con acción clara; autoridad: libro de ingeniería de confiabilidad de Google.
- [Python: datetime](https://docs.python.org/3/library/datetime.html) — fechas usadas por el verificador; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Escalado reactivo](./escalado-reactivo.md) · [Escalar →](./escalar.md)
