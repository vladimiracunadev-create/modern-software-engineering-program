# Sistema de aprendizaje automático

[↑ Glosario](../../README.md) · [← Síntomas y peticiones](./sintomas-y-peticiones.md) · [Sistema de gestión de IA →](./sistema-de-gestion-de-ia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Conjunto de datos, código, modelo e infraestructura que decide en producción.

Definición de trabajo de [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md).

## Por qué importa

La clase donde se define, [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md), existe con este propósito: la clase existe para que dejes de tratar un modelo de aprendizaje automático como un componente que se entrega y se olvida, y lo trates como un sistema con ciclo de vida: datos, etiquetas, características, entrenamiento, evaluación, registro, despliegue, servicio, monitoreo y reentrenamiento, cada uno con dueño, entradas y modos de fallo propios.

## Cómo funciona

Según [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md):

Un sistema de aprendizaje automático en producción reúne diez piezas: datos de origen, etiquetas, características, entrenamiento, evaluación, registro del modelo, despliegue, servicio, monitoreo y reentrenamiento. El modelo ocupa dos de ellas. El código que lo rodea (recolección, validación, configuración, infraestructura de servicio, monitoreo) es la mayor parte del sistema y la mayor parte de su mantenimiento. Esa es la tesis del artículo de deuda técnica de Sculley y colegas, y es la razón de que la parte comience por el sistema y no por el modelo: las clases siguientes recorren los eslabones uno a uno y cada una responde a la pregunta «qué falla aquí y cómo lo vemos».

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md)) son: Las cuatro fallas, su magnitud, el efecto del recordatorio y la regla son construcciones del autor sobre datos sintéticos; los números muestran que las causas son distintas y que el bucle existe, no su frecuencia en ningún sistema real. No se evaluó ninguna plataforma de MLOps. El siguiente paso, `SE-602`, abre el primer eslabón: cómo se construyen los datos, las etiquetas y las características para que no mientan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Modelo](../m/modelo.md), [Producción](../p/produccion.md), [Bucle de realimentación](../b/bucle-de-realimentacion.md), [Ciclo de vida](../c/ciclo-de-vida.md), [Deriva de concepto](../d/deriva-de-concepto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-601 — Ciclo de vida de ML y por qué falla en producción](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md), [SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md), [SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), [SE-291](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Síntomas y peticiones](./sintomas-y-peticiones.md) · [Sistema de gestión de IA →](./sistema-de-gestion-de-ia.md)
