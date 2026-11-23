# SLI

[↑ Glosario](../../README.md) · [← SLH-DSA](./slh-dsa.md) · [Slice reusable →](./slice-reusable.md)

> **Tipo:** sigla · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Un **SLI** (*service level indicator*, indicador de nivel de servicio) es una medida cuantitativa de un aspecto del servicio que importa a quien lo usa. [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) lo define como esa medida, normalmente la proporción de eventos buenos sobre eventos válidos; [SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md) lo presenta como medida cuantitativa del comportamiento del servicio y [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md) como la medición de un aspecto de lo que la persona usuaria experimenta. Es la base sobre la que se escribe un SLO.

## Por qué importa

Un objetivo solo es verificable si lo que mide está bien definido. [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) insiste en que el SLI se mide desde la perspectiva de quien usa el servicio, no desde la comodidad de quien lo opera: un SLI mal elegido produce un SLO que se cumple mientras hay quejas.

## Cómo funciona

La forma más útil, según [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), es una **proporción**: eventos buenos entre eventos válidos, expresada como porcentaje. Para la API de entregas del caso conductor, «una entrega es buena si el servidor responde con éxito y en menos de 1 s». La definición exige tres decisiones que se escriben:

1. **Qué es «bueno»:** el estado de la respuesta y el umbral de latencia.
2. **Qué es «válido»:** qué eventos se excluyen porque no son culpa del servicio, como una petición mal formada.
3. **Dónde se mide:** [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) recomienda medir cerca de la persona usuaria.

La causa de la tercera decisión es que lo medido depende del punto de medida: un indicador tomado en el servidor no ve lo que ocurre en la red del cliente. Y un SLI de disponibilidad sin umbral de latencia da por buena una respuesta correcta pero lenta, lo que [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) señala como un fallo de definición.

## Ejemplo

En [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), la API de entregas define su SLI como la proporción de peticiones respondidas con éxito en menos de 1 s sobre las peticiones válidas. Con eso, un 99,9 % de ese SLI sostenido en 30 días es el SLO del servicio. Si un panel cuenta peticiones y otro cuenta minutos, los consumos del presupuesto divergen: la clase pide declarar la forma de contar en el SLO.

## Errores y confusiones comunes

- **Medir donde no se ve el problema.** El SLO se cumple y hay quejas; hay que medir cerca de la persona y añadir ventana corta o segmento ([SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)).
- **Contar de dos maneras.** Dos paneles dan consumos opuestos porque uno cuenta peticiones y otro minutos ([SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)).
- **Confundir SLI, SLO y SLA.** El SLI es la medida, el SLO su valor objetivo en una ventana y el SLA el compromiso con el cliente, que debe fijarse por debajo del SLO ([SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)).

## Límites y cuándo no aplica

Un SLI es una simplificación: [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md) señala que la caída parcial (algunos clientes, algunas funciones) se mide con SLI por solicitud y no por tiempo, y que las series de la clase son inventadas para mostrar la lectura.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Medición](../m/medicion.md), [Medida](../m/medida.md), [Servicio](./servicio.md), [Alcance](../a/alcance.md), [Backoff](../b/backoff.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-048 — Proyecto: servicio observable y tolerante a fallos de red](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
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

[↑ Glosario](../../README.md) · [← SLH-DSA](./slh-dsa.md) · [Slice reusable →](./slice-reusable.md)
