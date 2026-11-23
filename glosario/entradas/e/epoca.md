# Época

[↑ Glosario](../../README.md) · [← Envoltura de un byte](./envoltura-de-un-byte.md) · [Equivalencia funcional →](./equivalencia-funcional.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Una pasada completa por los datos de entrenamiento.

Definición de trabajo de [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md).

## Por qué importa

La clase donde se define, [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md), existe con este propósito: la clase existe para que decidas con números cuándo vale la pena adaptar un modelo existente, cuánto cuesta hacerlo y qué se pierde por el camino.

## Cómo funciona

Según [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md):

Antes de adaptar, hay que medir el modelo base en la población nueva. En el laboratorio, el modelo base se entrenó con 40 000 filas durante 30 épocas (1,14 s) y alcanzó un AUC de 0,858 en su población de origen; en el dominio nuevo, sin adaptación, alcanzó 0,840. La adaptación solo puede justificarse por la diferencia sobre esos 0,840, no sobre cero. Con modelos de lenguaje ocurre lo mismo: antes de ajustar hay que medir qué hace el modelo con un buen *prompt*, con ejemplos y con recuperación de contexto (`SE-554`, `SE-594`), porque si eso alcanza, el ajuste es un costo evitable.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En el laboratorio, el modelo base se entrenó con 40 000 filas durante 30 épocas (1,14 s) y alcanzó un AUC de 0,858 en su población de origen; en el dominio nuevo, sin adaptación, alcanzó 0,840. ([SE-605](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), [SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Adaptación de rango bajo](../a/adaptacion-de-rango-bajo.md), [Ajuste fino](../a/ajuste-fino.md), [Cómputo de entrenamiento](../c/computo-de-entrenamiento.md), [Modelo base](../m/modelo-base.md), [Olvido catastrófico](../o/olvido-catastrofico.md), [Variante](../v/variante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-605 — Ajuste fino, adaptación y costo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-291](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md), [SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md), [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Envoltura de un byte](./envoltura-de-un-byte.md) · [Equivalencia funcional →](./equivalencia-funcional.md)
