# Despliegue continuo

[↑ Glosario](../../README.md) · [← Desplazamiento](./desplazamiento.md) · [Despliegue escalonado →](./despliegue-escalonado.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Despliegue automático a producción de todo cambio que pasa la canalización.

Definición de trabajo de [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md).

## Por qué importa

La clase donde se define, [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), existe con este propósito: la clase existe para que distingas entregar de exponer y decidas con números cuánta gente ve una versión nueva antes de saber si funciona.

## Cómo funciona

Según [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md):

La **entrega continua** (continuous delivery) significa que cada cambio que pasa la canalización queda en un estado que podría desplegarse a producción: la decisión de hacerlo es humana y se puede tomar en cualquier momento. El **despliegue continuo** (continuous deployment) elimina esa decisión: todo cambio que pasa la canalización se despliega automáticamente. Una tercera decisión, la **exposición** (liberación, release), es quién usa la versión nueva y cuándo; puede separarse del despliegue con una bandera o con un porcentaje de tráfico. Las tres se confunden porque en equipos pequeños ocurren a la vez, pero son decisiones distintas con riesgos distintos: desplegar cambia el software que corre, exponer cambia lo que experimentan las personas. DORA mide la capacidad de liberar con seguridad en cualquier momento, no cuántas veces se hace.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md):

El equipo de la API de entregas fija su criterio de despliegue. Un canario del 5 % durante diez minutos, porque con el 1 % no podrían ver una degradación de un punto y sus picos de cierre de plazo no dejan margen para un error sutil; si la señal es buena amplían a 25 %, 50 % y 100 % con cinco minutos entre cada paso.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md)) son:

- **El canario dice «sin errores» y producción falla** — causa: tráfico insuficiente para ver el cambio. Corrección: calcular la potencia y exigir tráfico mínimo.
- **Se retiran versiones buenas** — causa: umbral laxo o tasa base inestable. Corrección: calcular la tasa de falsas alarmas y usar ventanas comparables.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md)) son: Las definiciones son operativas para la canalización de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Producción](../p/produccion.md), [Bandera de funcionalidad](../b/bandera-de-funcionalidad.md), [Canario](../c/canario.md), [Entrega continua](../e/entrega-continua.md), [Potencia](../p/potencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-002](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

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

[↑ Glosario](../../README.md) · [← Desplazamiento](./desplazamiento.md) · [Despliegue escalonado →](./despliegue-escalonado.md)
