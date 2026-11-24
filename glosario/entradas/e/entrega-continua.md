# Entrega continua

[↑ Glosario](../../README.md) · [← Entrega al menos una vez / como máximo una vez](./entrega-al-menos-una-vez-como-maximo-una-vez.md) · [Entrelazamiento →](./entrelazamiento.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

La **entrega continua** (*continuous delivery*) es la capacidad de que todo cambio verificado pueda desplegarse a producción en cualquier momento, por decisión humana ([SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md)).

## Por qué importa

Se confunde con dos cosas cercanas, y la confusión lleva a prometer lo que el proceso no hace. [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) separa tres decisiones: **entregar** (dejar cada cambio listo para producción), **desplegar** y **exponer** (quién usa la versión nueva y cuándo).

## Cómo funciona

Cada cambio que pasa la canalización queda en un estado desplegable; la decisión de hacerlo es humana. El **despliegue continuo** (*continuous deployment*) elimina esa decisión: todo cambio que pasa se despliega automáticamente. La **exposición** (liberación, *release*) puede separarse del despliegue con una bandera o con un porcentaje de tráfico. Las tres se confunden porque en muchos equipos ocurren juntas. Para comprobar un despliegue gradual, un **canario** compara la versión nueva con la anterior; su veredicto solo vale con tráfico suficiente.

## Ejemplo

Un equipo despliega cada cambio verificado a producción detrás de una bandera apagada (despliegue continuo), y una persona de producto decide cuándo activarla para el 5 % del tráfico (exposición). Si además la canalización exige una aprobación humana antes de producción, es entrega continua sin despliegue continuo.

## Errores y confusiones comunes

- **El canario dice «sin errores» y producción falla.** Tráfico insuficiente para ver el cambio; calcular la potencia y exigir un tráfico mínimo ([SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md)).
- **Se retiran versiones buenas.** Umbral laxo o tasa base inestable; calcular la tasa de falsas alarmas y usar ventanas comparables.

## Límites y cuándo no aplica

La entrega continua exige pruebas automáticas confiables y desplegar sin dolor; sin eso, «siempre desplegable» es una promesa vacía. En entornos regulados puede haber aprobaciones que deban permanecer.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Producción](../p/produccion.md), [Bandera de funcionalidad](../b/bandera-de-funcionalidad.md), [Canario](../c/canario.md), [Despliegue continuo](../d/despliegue-continuo.md), [Potencia](../p/potencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (20 clases más lo mencionan; las que más):

[SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md), [SE-002](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md), [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md), [SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [DORA: entrega continua](https://dora.dev/capabilities/continuous-delivery/) — capacidad de liberar con seguridad en cualquier momento; autoridad: DORA, Google Cloud.
- [Fowler: BlueGreenDeployment](https://martinfowler.com/bliki/BlueGreenDeployment.html) — dos entornos y cambio de tráfico; autoridad: Martin Fowler.
- [Fowler: CanaryRelease](https://martinfowler.com/bliki/CanaryRelease.html) — exposición a un subconjunto; autoridad: Martin Fowler.
- [Google SRE Workbook: canarying releases](https://sre.google/workbook/canarying-releases/) — decisión estadística del canario; autoridad: Google.
- [Fowler: feature toggles](https://martinfowler.com/articles/feature-toggles.html) — tipos de banderas y su costo; autoridad: Pete Hodgson en martinfowler.com.

---

[↑ Glosario](../../README.md) · [← Entrega al menos una vez / como máximo una vez](./entrega-al-menos-una-vez-como-maximo-una-vez.md) · [Entrelazamiento →](./entrelazamiento.md)
