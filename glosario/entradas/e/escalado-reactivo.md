# Escalado reactivo

[↑ Glosario](../../README.md) · [← Escalado programado](./escalado-programado.md) · [Escalamiento →](./escalamiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Ajuste del número de instancias según una métrica observada, con un retardo hasta que las nuevas estén listas.

Definición de trabajo de [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md).

## Por qué importa

La clase donde se define, [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), existe con este propósito: la clase existe para que puedas decidir cuánta capacidad tener, cuándo cambiarla y cuánto pagar por ella con evidencia y no con una impresión.

## Cómo funciona

Según [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md):

**Cómo leer la figura.** Cada punto es una política: el eje horizontal es el costo en instancias-hora de siete días y el vertical, la demanda que no se atendió. Lo mejor está abajo a la izquierda; mira que el escalado reactivo con arranque lento se acerca a ese rincón y que reservar para el pico lo abandona por la derecha. **Dónde deja de valer:** el tráfico lo generé yo, y los picos de un cierre de entregas real tienen una subida más brusca o más lenta; la solicitud no atendida se pierde, sin cola ni reintento, que es una simplificación.

Según [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** durante la subida del pico, una fracción visible de las solicitudes de ese cuarto de hora se pierde y después todo se normaliza. **Hipótesis rivales:** (a) el autoescalador está mal configurado; (b) hay un defecto en la aplicación; (c) las instancias nuevas tardan en estar listas. **Prueba:** compara en el tiempo la demanda, las instancias pedidas y las instancias listas; si las pedidas suben de inmediato y las listas lo hacen cinco minutos después, la causa es el arranque. **Conclusión:** el escalado reactivo no cubre el primer tramo del pico. **Regresión:** añade una subida programada previa al cierre y repite la simulación comprobando la pérdida.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md):

El equipo de la plataforma describe la demanda de siete días con mínimo, mediana, percentil 99 y máximo, y concluye que 12 instancias cubren el día normal y 30 el peor pico. Elige una política programada con una base de 7 instancias, una subida programada para las horas del cierre y un margen reactivo con objetivo de utilización del 60 % y arranque de 2 minutos, y mide con su propio tráfico cuánta demanda pierde en los picos aleatorios.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se paga el pico todo el año** — causa: capacidad fija dimensionada al máximo. Corrección: escalado reactivo con base programada. ([SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Conclusión:** el escalado reactivo no cubre el primer tramo del pico. ([SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-403](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-403-entornos-cuentas-y-separacion-de-responsabilidades/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ajuste](../a/ajuste.md), [Instancia](../i/instancia.md), [Métrica](../m/metrica.md), [Compromiso de capacidad](../c/compromiso-de-capacidad.md), [Escalado programado](./escalado-programado.md), [Ley de Little](../l/ley-de-little.md).
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

[↑ Glosario](../../README.md) · [← Escalado programado](./escalado-programado.md) · [Escalamiento →](./escalamiento.md)
