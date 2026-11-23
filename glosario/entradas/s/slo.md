# SLO

[↑ Glosario](../../README.md) · [← Slicing, vistas y copias](./slicing-vistas-y-copias.md) · [Sobre →](./sobre.md)

> **Tipo:** sigla · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Un **SLO** (*service level objective*, objetivo de nivel de servicio) es el valor objetivo de un indicador de nivel de servicio (SLI) durante una ventana de tiempo. [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) lo define como el valor mínimo comprometido de un indicador en una ventana, [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md) como el valor objetivo de un SLI en una ventana y [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) como el valor objetivo de un SLI durante una ventana de tiempo. Un ejemplo de [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md): 99,5 % de solicitudes buenas en 30 días. Es una meta interna de fiabilidad: no es lo mismo que un SLA, que es un compromiso contractual.

## Por qué importa

El SLO convierte «el servicio debe ser fiable» en un número, con una ventana, que el equipo y el producto pueden discutir y verificar. De él se deriva el presupuesto de error, que permite decidir cuánto riesgo se puede asumir; [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md) muestra que operar un producto incluye guardias con alertas basadas en SLO, que despiertan por consumo de presupuesto y no por cada pico. Sin SLO, la fiabilidad se negocia con adjetivos.

## Cómo funciona

Un SLO se construye sobre un **SLI** y se completa con una ventana y una forma de contar. [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) pide escribir tres decisiones que definen el SLI y que determinan lo que el SLO significa: qué es un evento «bueno» (estado y umbral de latencia), qué es un evento «válido» (qué se excluye) y dónde se mide. A partir de ahí:

- **El objetivo** fija el mínimo aceptable. Con 99,9 % en 30 días, la fracción tolerable es 0,1 %, equivalente a 43,2 minutos de caída total ([SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)).
- **El presupuesto de error** es 1 − objetivo y se gasta con incidentes, despliegues y mantenimientos ([SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md)).
- **Las dependencias componen:** si el servicio depende en serie de otros, su SLO no puede superar el producto de los de sus dependencias ([SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)), y por eso hay que revisar la redundancia.
- **El SLA** se fija por debajo del SLO, con margen interno; si el SLA es más estricto que el SLO, se firmó sin margen ([SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)).

## Ejemplo

En [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), la API de entregas define el SLI como la proporción de peticiones con respuesta exitosa en menos de 1 s, con un SLO de 99,9 % en 30 días. El equipo escribe además el límite de la promesa: el SLO no cubre la red del cliente ni los mantenimientos anunciados, y las dependencias externas (almacenamiento y correo) tienen SLO propios, de modo que la disponibilidad compuesta esperada es 99,7 %; se acuerda con producto revisar el objetivo cada cierto tiempo. Son datos sintéticos de la clase.

## Errores y confusiones comunes

- **«El SLO se cumple y hay quejas».** Se mide donde no se ve el problema o se promedia una ventana larga; corrección ([SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)): medir cerca de la persona y añadir ventana corta o segmento.
- **Dos paneles con consumos opuestos.** Uno cuenta peticiones y otro minutos; hay que declarar la forma de contar en el SLO.
- **SLA más estricto que el SLO.** Se firmó sin margen interno; el SLA se fija por debajo del SLO.
- **SLO superior al de las dependencias.** Se ignoró la composición en serie; se calcula el producto y se revisa la redundancia.

## Límites y cuándo no aplica

El SLO es tan bueno como su SLI: un SLI de disponibilidad sin umbral de latencia da por buena una respuesta correcta pero lenta ([SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md)). Las series de [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md) son inventadas para mostrar la lectura; en un sistema real el presupuesto se calcula con SLI por solicitud y se consume también por degradaciones parciales, no solo por caídas totales. Un SLA real excluye mantenimientos con aviso y define ventanas distintas (trimestral, anual), cosa que los ejemplos simplificados de la clase no modelan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Objetivo de nivel de servicio](../o/objetivo-de-nivel-de-servicio.md), [Indicador](../i/indicador.md), [Servicio](./servicio.md), [Valor](../v/valor.md), [Burn rate](../b/burn-rate.md), [Conformidad](../c/conformidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-419 — SLA por nivel, soporte y operación del producto](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-497 — SLI, SLO, SLA y presupuestos de error](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — definición de SLI, SLO y SLA; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) — proporción de eventos buenos, presupuesto y política; autoridad: Google, SRE Workbook.
- [Google SRE Book: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — señales y alertas sobre síntomas; autoridad: Google.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — descripción de contratos de API; autoridad: OpenAPI Initiative.
- [JSON Schema 2020-12: Validation](https://json-schema.org/draft/2020-12/json-schema-validation) — esquemas cerrados de entrada y salida; autoridad: proyecto JSON Schema.

---

[↑ Glosario](../../README.md) · [← Slicing, vistas y copias](./slicing-vistas-y-copias.md) · [Sobre →](./sobre.md)
