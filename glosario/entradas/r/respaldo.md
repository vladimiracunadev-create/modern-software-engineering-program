# Respaldo

[↑ Glosario](../../README.md) · [← Resolver la ruta](./resolver-la-ruta.md) · [Responsabilidad →](./responsabilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Alternativa simple que se usa cuando el modelo no sirve.

Definición de trabajo de [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md).

## Por qué importa

La clase donde se define, [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), existe con este propósito: el taller existe para que ensayes, con fallas inyectadas y mediciones, lo que la parte describió: ver una degradación a tiempo, distinguir su causa, mitigarla sin empeorar las cosas y volver a un estado sano con evidencia.

## Cómo funciona

Según [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md):

Durante la falla de unidad, medida sobre 48 horas desde la inyección, el AUC fue 0,849 antes, 0,791 con el modelo degradado, 0,752 con una regla de respaldo (el historial de tardanzas más una fracción de la carga) y 0,849 tras corregir la conversión de unidad en el servicio. La regla fue peor que el modelo degradado: porque el modelo, con una sola entrada mal escalada, conservaba la señal de las otras cinco y la regla solo usa dos características. La mitigación correcta fue corregir la causa. Lo que el ensayo enseña no es que «la regla es mala»: enseña que cada mitigación debe medirse en el ensayo antes de depender de ella y que, cuando la causa se conoce, corregirla es mejor que degradar.

Según [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md):

El equipo de *Avisos-ML* ejecuta el ensayo un martes con la persona de guardia sin aviso. La falla de unidad se inyecta a las 10:00. A las 10:02 llega el aviso de la validación de entrada a la persona de guardia, que abre el runbook, ve la rama «falla de calidad de entrada» y confirma que la tasa de lectura llega en porcentaje. A las 10:20 despliega una corrección de la conversión en el servicio y verifica en el tablero que la tasa de marcados vuelve a su banda. El incidente se cierra a las 10:45.

## Ejemplo

Ejemplo de [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* ejecuta el ensayo un martes con la persona de guardia sin aviso. La falla de unidad se inyecta a las 10:00. A las 10:02 llega el aviso de la validación de entrada a la persona de guardia, que abre el runbook, ve la rama «falla de calidad de entrada» y confirma que la tasa de lectura llega en porcentaje. A las 10:20 despliega una corrección de la conversión en el servicio y verifica en el tablero que la tasa de marcados vuelve a su banda. El incidente se cierra a las 10:45.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Las acciones sugeridas por el ensayo son concretas: añadir la tasa de nulos al monitor de distribución; poner una muestra etiquetada de 200 casos por semana para ver la deriva de concepto antes de las 57 horas; documentar que el respaldo por reglas solo se usa si el modelo está inutilizado; ensayar el rollback cada trimestre. ([SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md), [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Exposición](../e/exposicion.md), [Inyección de fallas](../i/inyeccion-de-fallas.md), [Mitigación](../m/mitigacion.md), [Monitor](../m/monitor.md), [Postmortem sin culpa](../p/postmortem-sin-culpa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (42 clases más lo mencionan; las que más):

[SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md), [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-358](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md), [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), [SE-291](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md), [SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Resolver la ruta](./resolver-la-ruta.md) · [Responsabilidad →](./responsabilidad.md)
