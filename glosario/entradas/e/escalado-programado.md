# Escalado programado

[↑ Glosario](../../README.md) · [← Escalada de privilegios](./escalada-de-privilegios.md) · [Escalado reactivo →](./escalado-reactivo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Ajuste del número de instancias según un calendario basado en un patrón conocido.

Definición de trabajo de [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md).

## Por qué importa

La clase donde se define, [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), existe con este propósito: la clase existe para que puedas decidir cuánta capacidad tener, cuándo cambiarla y cuánto pagar por ella con evidencia y no con una impresión.

## Cómo funciona

[SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. Cada proveedor y cada herramienta usan estos términos con matices y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md):

El equipo de la plataforma describe la demanda de siete días con mínimo, mediana, percentil 99 y máximo, y concluye que 12 instancias cubren el día normal y 30 el peor pico. Elige una política programada con una base de 7 instancias, una subida programada para las horas del cierre y un margen reactivo con objetivo de utilización del 60 % y arranque de 2 minutos, y mide con su propio tráfico cuánta demanda pierde en los picos aleatorios.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md)) son:

- **Se pierden solicitudes en cada pico aunque el autoescalador funcione** — causa: el arranque tarda más que la subida. Corrección: subida programada previa o instancias de reserva.
- **Se paga el pico todo el año** — causa: capacidad fija dimensionada al máximo. Corrección: escalado reactivo con base programada.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. Cada proveedor y cada herramienta usan estos términos con matices y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna plataforma ni un autoescalador real: el tráfico, la capacidad por instancia, el arranque y los precios son supuestos del autor y la cola es un modelo de un servidor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ajuste](../a/ajuste.md), [Instancia](../i/instancia.md), [Patrón](../p/patron.md), [Compromiso de capacidad](../c/compromiso-de-capacidad.md), [Escalado reactivo](./escalado-reactivo.md), [Ley de Little](../l/ley-de-little.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

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

[↑ Glosario](../../README.md) · [← Escalada de privilegios](./escalada-de-privilegios.md) · [Escalado reactivo →](./escalado-reactivo.md)
