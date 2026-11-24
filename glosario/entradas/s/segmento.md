# Segmento

[↑ Glosario](../../README.md) · [← Segmentación por necesidad](./segmentacion-por-necesidad.md) · [Segmento inicial →](./segmento-inicial.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

En monitoreo y despliegue de modelos, un **segmento** es una subpoblación definida de antemano que se vigila por separado ([SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md)).

## Por qué importa

Un indicador global puede mejorar mientras un grupo empeora. [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) lo muestra: el Brier global dice que el candidato mejora (0,163 a 0,159) mientras el AUC baja (0,837 a 0,819), y el daño se concentra en un segmento.

## Cómo funciona

El modelo vigente es una regresión logística entrenada con 8 000 filas del periodo antiguo; el candidato es un boosting entrenado con 40 000 filas del periodo reciente, en el que una anomalía de etiquetado registró como puntual el 60 % de las entregas tardías del segmento que usa móvil y entrega de noche. Al medir por segmento, el candidato empeora en el segmento móvil y nocturno aunque mejore en el total. El plan de despliegue vigila segmentos definidos antes de empezar.

## Ejemplo

[SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md): en la etapa de sombra de 24 horas, se vigila el desacuerdo y la tasa de marcados en cuatro segmentos (dispositivo y franja horaria); la regla es pausar si alguno se aparta más de 10 puntos. La primera noche, en el segmento móvil y nocturno el candidato marca al 4 % frente al 59 % del vigente: el plan se pausa y se descubre el problema de etiquetado.

## Errores y confusiones comunes

Definir los segmentos después de ver los resultados; vigilar solo agregados.

## Límites y cuándo no aplica

Demasiados segmentos producen alarmas por azar; deben elegirse por razón de negocio o de riesgo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ejecución en sombra](../e/ejecucion-en-sombra.md), [Escalón de tráfico](../e/escalon-de-trafico.md), [Guarda](../g/guarda.md), [Potencia](../p/potencia.md), [Registro de modelos](../r/registro-de-modelos.md), [Retroceso](../r/retroceso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (64 clases más lo mencionan; las que más):

[SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md), [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), [SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md), [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md), [SE-415](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md), [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Segmentación por necesidad](./segmentacion-por-necesidad.md) · [Segmento inicial →](./segmento-inicial.md)
