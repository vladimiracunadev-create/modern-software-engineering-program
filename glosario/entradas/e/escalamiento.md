# Escalamiento

[↑ Glosario](../../README.md) · [← Escalado reactivo](./escalado-reactivo.md) · [Escalar →](./escalar.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

**Escalamiento** (en el sentido de *escalada*, no de escalar capacidad) es llevar un asunto al nivel siguiente de respuesta o de autoridad cuando el actual no puede o no llega a resolverlo. El programa lo usa en dos contextos:

- **En guardia** ([SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md)): el paso de una página al siguiente nivel de respuesta cuando el anterior no contesta a tiempo.
- **En gestión** ([SE-529](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-529-liderazgo-tecnico-sin-autoridad-formal/README.md), [SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md)): llevar una decisión a quien tiene autoridad sobre ella, con el problema, las opciones y sus costos, como traslado explícito a autoridad capaz de decidir.

No debe confundirse con el escalamiento de capacidad (más recursos), que el programa trata como escalado.

## Por qué importa

Un incidente sin dueño que responda se alarga: cada minuto sin reconocimiento es daño que continúa. Y en la gestión, una decisión atascada en quien no tiene autoridad no avanza. Escalar es una acción profesional que se diseña antes de necesitarla: quién, cuándo, con qué información.

## Cómo funciona

- **Guardia** ([SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md)): cada nivel tiene un tiempo máximo (cinco minutos es habitual para el reconocimiento) tras el cual la página pasa al siguiente: guardia primaria, secundaria, responsable. Cuenta la independencia de los niveles: con 85 % de respuesta por nivel y fallos independientes, tres niveles atienden el 99,8 % de las páginas en 15 minutos, frente al 84,8 % de un solo nivel. El cálculo es 1 − 0,15³ frente a 0,85 (tres niveles contra uno).
- **Gestión** ([SE-529](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-529-liderazgo-tecnico-sin-autoridad-formal/README.md)): se lleva la decisión con el problema, las opciones y sus costos, no solo una queja; quien tiene autoridad debe poder decidir sin reconstruir el contexto.

## Ejemplo

Una alerta de pago caído llega a la guardia primaria a las 03:00; no hay reconocimiento en cinco minutos y pasa a la secundaria; en otros cinco, al responsable. Ilustración del cálculo:

```python
p = 0.85
uno, tres = p, 1 - (1 - p) ** 3   # 0.85 y 0.996
```

La clase da 99,8 % para tres niveles al incluir reintentos dentro de los 15 minutos; el cálculo mínimo anterior ilustra el principio de niveles independientes.

## Errores y confusiones comunes

- **Un runbook que dice «revisa los servicios».** Causa: pasos sin comando ni salida esperada; corrección: un paso por acción, con comando y resultado esperado ([SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md)).
- **La guardia es siempre la misma persona.** Causa: equipo pequeño o ausencias sin plan; corrección: calcular la carga y ampliar la rotación o reducir el alcance ([SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md)).
- **Escalar sin opciones.** Trasladar un problema sin alternativas ni costos devuelve el trabajo de análisis al superior ([SE-529](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-529-liderazgo-tecnico-sin-autoridad-formal/README.md)).

## Límites y cuándo no aplica

Las cifras de [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) suponen fallos independientes: una causa común (por ejemplo, una caída de red que afecta a todos) invalida el cálculo. El escalamiento no corrige un diseño de alertas ruidoso. Y escalar demasiado pronto o por reflejo desgasta a los niveles superiores y reduce la confianza en las páginas.

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

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md), [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

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
