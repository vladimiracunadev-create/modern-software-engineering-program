# Política de presupuesto

[↑ Glosario](../../README.md) · [← Política de permisos](./politica-de-permisos.md) · [Política de reentrenamiento →](./politica-de-reentrenamiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Acuerdo previo sobre qué cambia cuando el presupuesto se agota o se consume demasiado rápido.

Definición de trabajo de [SE-497 — SLI, SLO, SLA y presupuestos de error](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md).

## Por qué importa

La clase donde se define, [SE-497 — SLI, SLO, SLA y presupuestos de error](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), existe con este propósito: la clase existe para que conviertas «el servicio debe ser fiable» en una promesa medible: un indicador (SLI) que mida lo que siente quien usa el servicio, un objetivo (SLO) con ventana y un presupuesto de error que diga cuánto fallo se puede gastar y quién decide qué hacer cuando se acaba.

## Cómo funciona

Según [SE-497 — SLI, SLO, SLA y presupuestos de error](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md):

El **presupuesto de error** es el fallo que el SLO permite: 1 − objetivo. Con 99,9 % en 30 días son 43,2 minutos de caída total, o 0,1 % de las peticiones. Convierte la fiabilidad en una moneda: mientras queda presupuesto, el equipo puede desplegar con ritmo y asumir riesgo; cuando se agota, una **política de presupuesto** acordada de antemano dice qué cambia (pausar despliegues no urgentes, dedicar el sprint a fiabilidad, escalar a quien decide). Sin política, el presupuesto es un número en un panel. La política debe tener un responsable que la aplique y una excepción explícita para lo que el presupuesto no puede frenar (una corrección de seguridad).

Según [SE-497 — SLI, SLO, SLA y presupuestos de error](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md):

El SLO es un objetivo interno que guía decisiones de ingeniería; el SLA es un compromiso externo con consecuencias. El SLA debe ser más laxo que el SLO para que haya un margen antes de pagar. Un SLO puede incumplirse sin consecuencia contractual; la consecuencia es la política de presupuesto.

## Ejemplo

Ejemplo de [SE-497 — SLI, SLO, SLA y presupuestos de error](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) (sección «Preguntas frecuentes»):

El SLO es un objetivo interno que guía decisiones de ingeniería; el SLA es un compromiso externo con consecuencias. El SLA debe ser más laxo que el SLO para que haya un margen antes de pagar. Un SLO puede incumplirse sin consecuencia contractual; la consecuencia es la política de presupuesto.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-497 — SLI, SLO, SLA y presupuestos de error](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)) son:

- **El SLO se cumple y hay quejas** — causa: se mide donde no se ve el problema, o se promedia una ventana larga. Corrección: medir cerca de la persona y añadir ventana corta o segmento.
- **Dos paneles dan consumos opuestos** — causa: uno cuenta peticiones y otro minutos. Corrección: declarar la forma de contar en el SLO.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Convierte la fiabilidad en una moneda: mientras queda presupuesto, el equipo puede desplegar con ritmo y asumir riesgo; cuando se agota, una **política de presupuesto** acordada de antemano dice qué cambia (pausar despliegues no urgentes, dedicar el sprint a fiabilidad, escalar a quien decide). ([SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Presupuesto](./presupuesto.md), [Sobre](../s/sobre.md), [Presupuesto de error](./presupuesto-de-error.md), [SLA](../s/sla.md), [SLI](../s/sli.md), [SLO](../s/slo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-497 — SLI, SLO, SLA y presupuestos de error](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — definición de SLI, SLO y SLA; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) — proporción de eventos buenos, presupuesto y política; autoridad: Google, SRE Workbook.
- [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — señales de oro; autoridad: libro de ingeniería de confiabilidad de Google.
- [Dean y Barroso, «The tail at scale»](https://doi.org/10.1145/2408776.2408794) — latencia de cola; autoridad: Communications of the ACM, 2013.
- [Python: random](https://docs.python.org/3/library/random.html) — generador usado en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Política de permisos](./politica-de-permisos.md) · [Política de reentrenamiento →](./politica-de-reentrenamiento.md)
