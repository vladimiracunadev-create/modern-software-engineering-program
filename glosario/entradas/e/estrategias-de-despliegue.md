# Estrategias de despliegue

[↑ Glosario](../../README.md) · [← Estrategia voraz](./estrategia-voraz.md) · [Estructura →](./estructura.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

El **despliegue de una vez** reemplaza todas las instancias: simple, rápido y con la exposición máxima si falla. El **despliegue progresivo** (rolling) reemplaza las instancias por tandas, con comprobaciones entre ellas; limita el alcance pero mezcla versiones durante el cambio. El **azul-verde** mantiene dos entornos y cambia el tráfico de uno a otro; permite volver al anterior de inmediato, a costa de duplicar infraestructura y de tener que resolver los datos compartidos.

Explicación de la sección «Estrategias de despliegue» de [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md).

## Por qué importa

En [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), el tema «Estrategias de despliegue» importa porque la fracción expuesta decide cuántos usuarios sufren un fallo.

En [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md), el tema «Estrategias de despliegue» importa porque cada una reduce un riesgo distinto.

## Cómo funciona

Según [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), en la sección «Estrategias de despliegue»:

El **despliegue de una vez** reemplaza todas las instancias: simple, rápido y con la exposición máxima si falla. El **despliegue progresivo** (rolling) reemplaza las instancias por tandas, con comprobaciones entre ellas; limita el alcance pero mezcla versiones durante el cambio. El **azul-verde** mantiene dos entornos y cambia el tráfico de uno a otro; permite volver al anterior de inmediato, a costa de duplicar infraestructura y de tener que resolver los datos compartidos. El **canario** expone la versión nueva a una fracción pequeña del tráfico real y amplía solo si la señal es buena. Ninguna estrategia ve el defecto por sí misma: reducen cuántos usuarios lo sufren mientras algo —una alarma, una comparación estadística, una persona— lo detecta. Elegir es decidir qué daño máximo se acepta antes de la detección.

Según [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md), en la sección «Estrategias de despliegue»:

Un despliegue **por oleadas** (*rolling*) reemplaza servidores en lotes: el riesgo se reparte en el tiempo, pero ambas versiones conviven y el retroceso es otra oleada. **Blue-green** mantiene dos entornos completos; el tráfico se dirige a uno, y el otro recibe la versión nueva y se prueba sin usuarios; el cambio es instantáneo y el retroceso, volver a dirigir el tráfico, pero el cambio expone a todas las personas a la vez y el coste es doble infraestructura. **Canary** dirige una fracción pequeña del tráfico a la versión nueva y compara con la anterior en paralelo; reduce el número de personas expuestas al defecto y obtiene evidencia con tráfico real.

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

- **Prerrequisito:** las clases previas [SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Bandera de funcionalidad](../b/bandera-de-funcionalidad.md), [Blue-green](../b/blue-green.md), [Canario](../c/canario.md), [Despliegue continuo](../d/despliegue-continuo.md), [Entrega continua](./entrega-continua.md), [Escalón de tráfico](./escalon-de-trafico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-485 — Entrega y despliegue continuos](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md).

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

[↑ Glosario](../../README.md) · [← Estrategia voraz](./estrategia-voraz.md) · [Estructura →](./estructura.md)
