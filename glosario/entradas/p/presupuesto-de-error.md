# Presupuesto de error

[↑ Glosario](../../README.md) · [← Presupuesto de contexto](./presupuesto-de-contexto.md) · [Presupuesto de fotograma →](./presupuesto-de-fotograma.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

El **presupuesto de error** es la cantidad de fallo que un SLO permite en su ventana: uno menos el objetivo. [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) lo formula así, [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) como la fracción de solicitudes que pueden fallar sin incumplir el objetivo y [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md) como el complemento del objetivo expresado como cantidad de fallo tolerable. Con un SLO de 99,9 % en 30 días, el presupuesto es 0,1 % de las peticiones o 43,2 minutos de caída total.

## Por qué importa

Convierte la fiabilidad en una moneda que se gasta. Según [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), mientras queda presupuesto, el equipo puede desplegar con ritmo y asumir riesgo; cuando se agota, una política acordada de antemano decide qué cambia. Así la discusión entre «entregar más» y «estabilizar» deja de ser una opinión y pasa a ser una cantidad: [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) lo resume como un número que obliga a elegir entre cambiar y estabilizar.

## Cómo funciona

El presupuesto se **gasta** con incidentes, con despliegues arriesgados y con mantenimientos ([SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md)). Lo que da sentido al número es la **política de presupuesto**, que las clases describen con un ejemplo de tres tramos ([SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md)): por debajo del 50 % de consumo, el equipo despliega con normalidad; entre 50 % y 100 %, se exige revisión adicional de los cambios riesgosos; al agotarse, se detienen los lanzamientos de funcionalidad hasta restablecer el margen y se prioriza la fiabilidad. [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) añade que la política necesita un responsable que la aplique y una excepción explícita para lo que el presupuesto no puede frenar, como una corrección de seguridad. Sin política, el presupuesto es un número en un panel.

Para alertar, [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) usa la **tasa de consumo**: cuántas veces más rápido que lo permitido se gasta el presupuesto. La alerta rápida salta si la tasa supera 14,4 en una hora y en cinco minutos; la lenta, si supera 6 en seis horas y en 30 minutos.

## Ejemplo

En [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), con SLO de 99,5 % en 30 días (presupuesto de 0,5 %), tres incidentes sintéticos comienzan el día 20. Una caída total de 10 minutos consume el 14,6 % del presupuesto y la alerta rápida salta a los 4 minutos. Un 5 % de errores durante 6 horas consume el 18,3 %; la alerta rápida no salta y la lenta lo hace a los 215 minutos. Una degradación lenta del 0,8 % consume el 63,3 % y ninguna de las dos alertas salta, porque su tasa de consumo (unas 1,7 veces) queda por debajo de ambos umbrales: es un incidente que gasta mucho presupuesto sin que nadie sea avisado.

En [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), un mes tranquilo termina en 12 minutos (28 %), uno con un incidente grande de 40 minutos cierra en 44 (102 %). Las series son inventadas para mostrar la lectura.

## Errores y confusiones comunes

- **Un presupuesto sin política.** Es un número en un panel que no cambia ninguna decisión ([SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)).
- **Alertar solo por picos.** Una degradación lenta puede consumir la mayor parte del presupuesto sin cruzar ningún umbral rápido ([SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md)).

## Límites y cuándo no aplica

Las cifras de las clases suponen un mes de 30 días y que toda caída cuenta; en un sistema real el presupuesto se calcula con SLI por solicitud y se consume también por degradaciones parciales ([SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md)). El presupuesto no decide solo: necesita una excepción explícita para lo que no puede frenarse ([SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)), y las alertas por tasa de consumo de [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) se calibraron con tráfico constante y un error de base del 0,05 %, supuestos que no siempre se cumplen.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Complemento](../c/complemento.md), [Ventana](../v/ventana.md), [Burn rate](../b/burn-rate.md), [Conformidad](../c/conformidad.md), [Crédito de servicio](../c/credito-de-servicio.md), [Disponibilidad compuesta](../d/disponibilidad-compuesta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-419 — SLA por nivel, soporte y operación del producto](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-497 — SLI, SLO, SLA y presupuestos de error](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (15 clases más lo mencionan; las que más):

[SE-513](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md), [SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), [SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), [SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md).

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Presupuesto de errores».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE Book: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — indicadores, objetivos y presupuesto de error; autoridad: Google.
- [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) — proporción de eventos buenos, presupuesto y política; autoridad: Google, SRE Workbook.
- [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — señales de oro; autoridad: libro de ingeniería de confiabilidad de Google.
- [Dean y Barroso, «The tail at scale»](https://doi.org/10.1145/2408776.2408794) — latencia de cola; autoridad: Communications of the ACM, 2013.
- [Python: random](https://docs.python.org/3/library/random.html) — generador usado en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Presupuesto de contexto](./presupuesto-de-contexto.md) · [Presupuesto de fotograma →](./presupuesto-de-fotograma.md)
