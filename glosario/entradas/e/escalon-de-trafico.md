# Escalón de tráfico

[↑ Glosario](../../README.md) · [← Escalera de herramientas](./escalera-de-herramientas.md) · [Escáner previo al envío →](./escaner-previo-al-envio.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Despliegue de un cambio a una fracción pequeña y limitada del tráfico.

Definición de trabajo de [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md): Despliegue de una versión nueva a una fracción pequeña del tráfico para compararla con la anterior.
- En [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md): Fracción creciente del tráfico dirigida al sistema nuevo.

## Por qué importa

En [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md), el tema «Canary» importa porque expone poco tráfico con criterios de parada.

## Cómo funciona

Según [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md):

Un canary sirve el candidato a una fracción del tráfico y compara una métrica de error con la del modelo vigente. Con etiquetas que tardan siete días, solo se puede medir el error de las decisiones ya etiquetadas, y la potencia depende de cuántas decisiones del segmento afectado hay en la fracción.

Según [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md):

El equipo de *Avisos-ML* escribe el plan de despliegue del candidato. Etapa 1, sombra durante 24 horas: se vigila el desacuerdo y la tasa de marcados en cuatro segmentos definidos de antemano (dispositivo y franja horaria); la regla es pausar si algún segmento se aparta más de 10 puntos. La sombra de la primera noche pausa el plan: en el segmento móvil y nocturno el candidato marca al 4 % frente al 59 % del vigente. El equipo revisa los datos de entrenamiento y encuentra la anomalía de etiquetado, reentrena con el segmento corregido y repite la sombra. Etapa 2, canary del 5 % durante cinco días con guardas de latencia, errores y marcados por segmento, y la métrica con etiquetas cuando llegan.

## Ejemplo

Ejemplo de [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) (sección «Ejemplo mínimo»):

La guarda de un canary sobre la tasa de marcados en cinco líneas:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un canary del 1 % por prudencia es demasiado pequeño para ver una regresión de un segmento minoritario en una semana: ofrece una sensación de seguridad que no tiene potencia. ([SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md))
- La sombra no sirve decisiones; el canary las sirve a una fracción. ([SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Versión](../v/version.md), [Abstracción de rama](../a/abstraccion-de-rama.md), [Blue-green](../b/blue-green.md), [Criterio de retroceso](../c/criterio-de-retroceso.md), [Estrangulamiento](./estrangulamiento.md), [Expandir, migrar y contraer](./expandir-migrar-y-contraer.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md), [SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md), [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), [SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md), [SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «canary».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «CanaryRelease»](https://martinfowler.com/bliki/CanaryRelease.html) — despliegue progresivo; autoridad: autor del texto.
- [Fowler, «BlueGreenDeployment»](https://martinfowler.com/bliki/BlueGreenDeployment.html) — dos entornos y cambio de tráfico; autoridad: autor del texto.
- [Google SRE Workbook: Canarying Releases](https://sre.google/workbook/canarying-releases/) — diseño de un canario; autoridad: Google, libro de ingeniería de confiabilidad.
- [Fowler, «ParallelChange»](https://martinfowler.com/bliki/ParallelChange.html) — expandir, migrar y contraer; autoridad: autor del texto.
- [Google SRE: Release Engineering](https://sre.google/sre-book/release-engineering/) — entrega y retroceso; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Escalera de herramientas](./escalera-de-herramientas.md) · [Escáner previo al envío →](./escaner-previo-al-envio.md)
