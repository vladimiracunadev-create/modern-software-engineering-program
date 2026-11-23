# Canario

[↑ Glosario](../../README.md) · [← Canal de distribución](./canal-de-distribucion.md) · [Cancelación →](./cancelacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Exposición de una versión nueva a una fracción pequeña del tráfico real para decidir si se amplía.

Definición de trabajo de [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md).

## Por qué importa

En [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), el tema «Detección estadística» importa porque un canario pequeño no ve cambios pequeños.

## Cómo funciona

Según [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md):

El **despliegue de una vez** reemplaza todas las instancias: simple, rápido y con la exposición máxima si falla. El **despliegue progresivo** (rolling) reemplaza las instancias por tandas, con comprobaciones entre ellas; limita el alcance pero mezcla versiones durante el cambio. El **azul-verde** mantiene dos entornos y cambia el tráfico de uno a otro; permite volver al anterior de inmediato, a costa de duplicar infraestructura y de tener que resolver los datos compartidos. El **canario** expone la versión nueva a una fracción pequeña del tráfico real y amplía solo si la señal es buena. Ninguna estrategia ve el defecto por sí misma: reducen cuántos usuarios lo sufren mientras algo —una alarma, una comparación estadística, una persona— lo detecta. Elegir es decidir qué daño máximo se acepta antes de la detección.

Según [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md):

El equipo de la API de entregas fija su criterio de despliegue. Un canario del 5 % durante diez minutos, porque con el 1 % no podrían ver una degradación de un punto y sus picos de cierre de plazo no dejan margen para un error sutil; si la señal es buena amplían a 25 %, 50 % y 100 % con cinco minutos entre cada paso. El criterio de retroceso es automático: más de 29 errores acumulados en la ventana del canario, con tráfico mínimo de 3 000 solicitudes; si el tráfico es menor, el canario se mantiene sin ampliar hasta alcanzarlo. Los fines de semana de cierre de plazos no se despliega salvo correcciones.

## Ejemplo

Ejemplo de [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula cuántos errores hay que observar en un canario para rechazar el azar al 0,1 %. Antes de ejecutarlo, predice si con 600 solicitudes y una tasa base de 0,5 % el umbral es mayor que 10.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El canario dice «sin errores» y producción falla** — causa: tráfico insuficiente para ver el cambio. Corrección: calcular la potencia y exigir tráfico mínimo. ([SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **canario** expone la versión nueva a una fracción pequeña del tráfico real y amplía solo si la señal es buena. ([SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Exposición](../e/exposicion.md), [Versión](../v/version.md), [Bandera de funcionalidad](../b/bandera-de-funcionalidad.md), [Despliegue continuo](../d/despliegue-continuo.md), [Entrega continua](../e/entrega-continua.md), [Potencia](../p/potencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), [SE-564](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md), [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), [SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE Workbook: canarying releases](https://sre.google/workbook/canarying-releases/) — decisión estadística del canario; autoridad: Google.
- [DORA: entrega continua](https://dora.dev/capabilities/continuous-delivery/) — capacidad de liberar con seguridad en cualquier momento; autoridad: DORA, Google Cloud.
- [Fowler: BlueGreenDeployment](https://martinfowler.com/bliki/BlueGreenDeployment.html) — dos entornos y cambio de tráfico; autoridad: Martin Fowler.
- [Fowler: CanaryRelease](https://martinfowler.com/bliki/CanaryRelease.html) — exposición a un subconjunto; autoridad: Martin Fowler.
- [Fowler: feature toggles](https://martinfowler.com/articles/feature-toggles.html) — tipos de banderas y su costo; autoridad: Pete Hodgson en martinfowler.com.

---

[↑ Glosario](../../README.md) · [← Canal de distribución](./canal-de-distribucion.md) · [Cancelación →](./cancelacion.md)
