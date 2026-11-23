# SLA

[↑ Glosario](../../README.md) · [← Sketches y aproximación](./sketches-y-aproximacion.md) · [SLH-DSA →](./slh-dsa.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Acuerdo contractual con consecuencias si no se cumple.

Definición de trabajo de [SE-419 — SLA por nivel, soporte y operación del producto](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-497 — SLI, SLO, SLA y presupuestos de error](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md): Compromiso contractual con una consecuencia si no se cumple un nivel de servicio.

## Por qué importa

En [SE-419 — SLA por nivel, soporte y operación del producto](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), el tema «SLI, SLO, SLA» importa porque separan medir, objetivo interno y compromiso con consecuencia.

## Cómo funciona

Según [SE-419 — SLA por nivel, soporte y operación del producto](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md):

Un **SLI** (indicador de nivel de servicio) es una medición de lo que el usuario experimenta: la proporción de solicitudes que tienen éxito, la proporción que responde en menos de un umbral, la proporción de trabajos que terminan a tiempo. Un **SLO** (objetivo) es el valor que el equipo se propone para ese indicador en una ventana («99,95 % de solicitudes con éxito en 30 días»). Un **SLA** (acuerdo) es el compromiso contractual con el cliente, con consecuencias (créditos) si no se cumple. El SLO interno debe ser más estricto que el SLA: si se promete 99,9 % al cliente y el equipo se fija 99,9 % por dentro, el primer mes malo ya es un incumplimiento. Esa diferencia es el margen operativo.

Según [SE-419 — SLA por nivel, soporte y operación del producto](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md):

El equipo de *Tablero* rehace sus niveles tras la queja del cliente empresa. Define el SLI («proporción de solicitudes de la API y de la aplicación con respuesta distinta de 5xx en menos de 2 segundos, medida en el borde y verificada con sondas externas cada minuto, por inquilino») y fija un SLO interno de 99,95 % mensual para el plan empresa frente a un SLA de 99,9 %. Calcula la composición de su cadena crítica, descubre que ofrece 99,75 % y decide dos mejoras antes de firmar el SLA: una réplica de lectura que saque a un componente del camino crítico y un modo degradado para el servicio de archivos.

## Ejemplo

Ejemplo de [SE-419 — SLA por nivel, soporte y operación del producto](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md) (sección «Ejemplo profesional»):

El equipo de *Tablero* rehace sus niveles tras la queja del cliente empresa. Define el SLI («proporción de solicitudes de la API y de la aplicación con respuesta distinta de 5xx en menos de 2 segundos, medida en el borde y verificada con sondas externas cada minuto, por inquilino») y fija un SLO interno de 99,95 % mensual para el plan empresa frente a un SLA de 99,9 %.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El SLA es más estricto que el SLO** — causa: se firmó sin margen interno. Corrección: fijar el SLA por debajo del SLO. ([SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **SLA** (acuerdo) es el compromiso contractual con el cliente, con consecuencias (créditos) si no se cumple. ([SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md))
- La que puedas demostrar con datos de al menos tres meses, con margen entre el SLO interno y el SLA, y que puedas costear. ([SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-418](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Compromiso](../c/compromiso.md), [Consecuencia](../c/consecuencia.md), [Servicio](./servicio.md), [Crédito de servicio](../c/credito-de-servicio.md), [Disponibilidad compuesta](../d/disponibilidad-compuesta.md), [Política de presupuesto](../p/politica-de-presupuesto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-419 — SLA por nivel, soporte y operación del producto](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-497 — SLI, SLO, SLA y presupuestos de error](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

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

[↑ Glosario](../../README.md) · [← Sketches y aproximación](./sketches-y-aproximacion.md) · [SLH-DSA →](./slh-dsa.md)
